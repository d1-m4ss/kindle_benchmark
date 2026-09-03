local WidgetContainer = require("ui/widget/container/widgetcontainer")
local UIManager = require("ui/uimanager")
local Device = require("device")
local Screen = Device.screen
local time = require("ui/time")
local ffi = require("ffi")
local json = require("json")
local lfs = require("libs/libkoreader-lfs")
local PluginLoader = require("pluginloader")
local logger = require("logger")

local Geometry = require("geometry")
local Adapters = require("adapters")

ffi.cdef[[
    struct rusage {
        struct { long tv_sec; int tv_usec; } ru_utime;
        struct { long tv_sec; int tv_usec; } ru_stime;
        long ru_maxrss; long ru_ixrss; long ru_idrss; long ru_isrss;
        long ru_minflt; long ru_majflt; long ru_nswap; long ru_inblock;
        long ru_oublock; long ru_msgsnd; long ru_msgrcv; long ru_nsignals;
        long ru_nvcsw; long ru_nivcsw;
    };
    int getrusage(int who, struct rusage *usage);
]]

local Benchmark = WidgetContainer:extend{ name = "benchmark" }
local SCREEN_W, SCREEN_H = 1236, 1648

local function precise_ms(delta_fts)
    -- time.to_ms() intentionally integer-rounds. Preserve the monotonic clock's
    -- microsecond representation in raw JSON instead.
    return time.to_us(delta_fts) / 1000.0
end

local function percentile(sorted, fraction)
    if #sorted == 0 then return nil end
    return sorted[math.max(1, math.ceil(#sorted * fraction))]
end

local function stats(values)
    if #values == 0 then return nil end
    table.sort(values)
    local sum = 0
    for _, value in ipairs(values) do sum = sum + value end
    local n = #values
    local median = n % 2 == 1 and values[(n + 1) / 2]
        or (values[n / 2] + values[n / 2 + 1]) / 2
    local mean = sum / n
    local sq = 0
    for _, value in ipairs(values) do sq = sq + (value - mean) ^ 2 end
    return {
        count = n,
        mean = mean,
        median = median,
        min = values[1],
        max = values[n],
        p10 = percentile(values, 0.10),
        p90 = percentile(values, 0.90),
        stdev = math.sqrt(sq / (n > 1 and n - 1 or 1)),
    }
end

local function memory_snapshot(force_gc)
    local natural = collectgarbage("count")
    if force_gc then collectgarbage("collect") end
    local live = collectgarbage("count")
    local usage = ffi.new("struct rusage")
    ffi.C.getrusage(0, usage)
    return {
        natural_lua_heap_kb = natural,
        forced_gc_live_heap_kb = live,
        rss_kb = tonumber(usage.ru_maxrss) / (jit.os == "OSX" and 1024 or 1),
    }
end

local function emit_marker(name)
    io.stdout:write("\n[" .. name .. "]\n")
    io.stdout:flush()
end

function Benchmark:_scheduleRunner()
    local function step()
        local ok, err = coroutine.resume(self._runner)
        if not ok then
            logger.err("Benchmark coroutine failed:", err)
            emit_marker("BENCHMARK_FAILED")
            UIManager:quit(1)
            return
        end
        if coroutine.status(self._runner) ~= "dead" then UIManager:nextTick(step) end
    end
    UIManager:nextTick(step)
end

function Benchmark:_settleNaturally(ticks)
    for _ = 1, ticks or 2 do coroutine.yield() end
end

function Benchmark:init()
    local enabled = os.getenv("BENCHMARK_ENABLE")
    if enabled ~= "1" and enabled ~= "true" then return end
    if rawget(_G, "__BENCHMARK_RUNNING") then return end
    rawset(_G, "__BENCHMARK_RUNNING", true)
    self.harness_init_fts = time.monotonic()
    self._runner = coroutine.create(function() self:runHarness() end)
    self:_scheduleRunner()
end

function Benchmark:runHarness()
    local config_name = os.getenv("BENCHMARK_CONFIG") or "A_stock"
    local mode = os.getenv("BENCHMARK_MODE") or "warm"
    local profile = os.getenv("BENCHMARK_PROFILE") or "synthetic"
    local library_dir = os.getenv("BENCHMARK_LIBRARY_DIR")
    local output_file = os.getenv("BENCHMARK_OUTPUT_FILE") or "benchmark_results.json"
    local warmup_count = tonumber(os.getenv("BENCHMARK_WARMUP_COUNT")) or 5
    local measure_count = tonumber(os.getenv("BENCHMARK_MEASURE_COUNT")) or 30
    local book_count = tonumber(os.getenv("BENCHMARK_BOOK_COUNT")) or 50
    local dataset_mode = os.getenv("BENCHMARK_DATASET_MODE") or "hierarchical"
    local settle_ticks = tonumber(os.getenv("BENCHMARK_SETTLE_TICKS")) or 2

    -- Pixel proof for every measured transition. A PNG per transition would
    -- need its own settle pass and a synchronous encode of the whole
    -- framebuffer between measurements, which changes the very sequence being
    -- measured; xxHash3 over the already-repainted buffer costs a fraction of
    -- a millisecond and is taken outside the timing window. Two consecutive
    -- transitions that leave an identical screen mean nothing visibly moved,
    -- which is exactly how a static overlay looks.
    local frame_hasher
    do
        local ok_hash, Hashoir = pcall(require, "ffi/hashoir")
        if ok_hash and Hashoir then
            local ok_new, hs = pcall(function() return Hashoir:new() end)
            if ok_new and hs then frame_hasher = hs end
        end
    end

    local function framebuffer_hash()
        if not frame_hasher then return nil end
        local bb = Screen and Screen.bb
        if not bb or not bb.data or not bb.stride or not bb.h then return nil end
        local ok, digest = pcall(function()
            frame_hasher:reset()
            frame_hasher:update(bb.data, bb.stride * bb.h)
            return frame_hasher:hexdigest()
        end)
        return ok and digest or nil
    end
    local screenshot_dir = os.getenv("BENCHMARK_SCREENSHOT_DIR")

    local function dismiss_transient_dialogs()
        local stack = UIManager._window_stack or {}
        local closed = false
        for i = #stack, 1, -1 do
            local entry = stack[i]
            local w = entry and (entry.widget or entry)
            if w and (w.name == "infomessage" or w.is_infomessage or w.timeout) then
                pcall(function() UIManager:close(w) end)
                closed = true
            end
        end
        return closed
    end

    -- Capture visual evidence only after a settled UI turn contains no transient
    -- dialog. This is outside any measured interval.
    local function probe_screenshot(label)
        if not screenshot_dir then return nil end
        local stable = false
        for _ = 1, 4 do
            self:_settleNaturally(settle_ticks)
            if not dismiss_transient_dialogs() then
                stable = true
                break
            end
        end
        if not stable then
            logger.warn("probe_screenshot skipped; transient dialog did not settle:", label)
            return nil
        end
        local basename = label .. ".png"
        local path = screenshot_dir .. "/" .. basename
        local ok, err = pcall(function() Screen:shot(path) end)
        if ok and lfs.attributes(path, "mode") == "file" then
            return basename
        end
        logger.warn("probe_screenshot failed for", label, ":", err or "file not created")
        return nil
    end

    local active_plugins, active_set = {}, {}
    if PluginLoader and PluginLoader.loaded_plugins then
        for name, plugin in pairs(PluginLoader.loaded_plugins) do
            local loaded_name = type(name) == "string" and name
                or (type(plugin) == "table" and plugin.name) or tostring(name)
            active_plugins[#active_plugins + 1] = loaded_name
            active_set[loaded_name] = true
        end
    end
    if PluginLoader and PluginLoader.enabled_plugins then
        for _, plugin in ipairs(PluginLoader.enabled_plugins) do
            local enabled_name = type(plugin) == "table" and plugin.name
            if enabled_name and not active_set[enabled_name] then
                active_plugins[#active_plugins + 1] = enabled_name
                active_set[enabled_name] = true
            end
        end
    end
    table.sort(active_plugins)

    local expected_plugins, missing_plugins = {}, {}
    for name in string.gmatch(os.getenv("BENCHMARK_EXPECTED_PLUGINS") or "", "[^,]+") do
        expected_plugins[#expected_plugins + 1] = name
        if not active_set[name] then missing_plugins[#missing_plugins + 1] = name end
    end

    local raw_size = Screen:getRawSize()
    local fb_w = (type(raw_size) == "table" and raw_size.w) or Screen:getWidth()
    local fb_h = (type(raw_size) == "table" and raw_size.h) or Screen:getHeight()
    if fb_w ~= 1236 or fb_h ~= 1648 then
        error(string.format("FATAL: Framebuffer resolution mismatch: expected 1236x1648, got %s x %s", tostring(fb_w), tostring(fb_h)))
    end

    local results = {
        schema_version = 2,
        config = config_name,
        mode = mode,
        profile = profile,
        dataset_mode = dataset_mode,
        book_count = book_count,
        library_dir = library_dir,
        screen_size = { w = fb_w, h = fb_h },
        framebuffer_resolution = string.format("%dx%d", fb_w, fb_h),
        iterations_warmup = warmup_count,
        iterations_measured = measure_count,
        active_plugins = active_plugins,
        plugin_load_assertion = {
            status = #missing_plugins == 0 and "PASS" or "FAILED",
            expected = expected_plugins,
            missing = missing_plugins,
        },
        timing = {
            source = "clock_gettime(CLOCK_MONOTONIC)",
            raw_unit = "milliseconds",
            raw_resolution = "microsecond representation (time.to_us / 1000)",
            integer_rounding = false,
        },
        memory_checkpoints = {},
        scenarios = {},
        timestamp = os.date("!%Y-%m-%dT%H:%M:%SZ"),
    }

    local inst = {
        active = false,
        set_dirty_calls = 0,
        refresh_count = 0,
        full_refreshes = 0,
        partial_refreshes = 0,
        count = 0,
        rect_x = {},
        rect_y = {},
        rect_w = {},
        rect_h = {},
        req_type = {},
        req_dither = {},
        req_full = {},
    }
    local orig_setDirty = UIManager.setDirty
    local orig_refreshUI = Screen.refreshUI

    local function record_refresh(x, y, w, h, refresh_type, full)
        local n = inst.count + 1
        inst.refresh_count = inst.refresh_count + 1
        inst.rect_x[n] = x or 0
        inst.rect_y[n] = y or 0
        inst.rect_w[n] = w or SCREEN_W
        inst.rect_h[n] = h or SCREEN_H
        inst.req_type[n] = refresh_type or "direct_refresh"
        inst.req_dither[n] = false
        inst.req_full[n] = full == true or x == nil
        inst.count = n
        if inst.req_full[n] then inst.full_refreshes = inst.full_refreshes + 1
        else inst.partial_refreshes = inst.partial_refreshes + 1 end
    end

    local function reset_recording()
        inst.set_dirty_calls = 0
        inst.refresh_count = 0
        inst.full_refreshes = 0
        inst.partial_refreshes = 0
        inst.count = 0
    end

    UIManager.setDirty = function(manager, widget, refresh_type, region, dither)
        if inst.active then
            local n = inst.count + 1
            inst.set_dirty_calls = inst.set_dirty_calls + 1
            inst.refresh_count = inst.refresh_count + 1
            local full = region == nil or refresh_type == "full"
            if full then inst.full_refreshes = inst.full_refreshes + 1
            else inst.partial_refreshes = inst.partial_refreshes + 1 end
            if region then
                inst.rect_x[n] = region.x
                inst.rect_y[n] = region.y
                inst.rect_w[n] = region.w
                inst.rect_h[n] = region.h
            else
                inst.rect_x[n] = 0
                inst.rect_y[n] = 0
                inst.rect_w[n] = SCREEN_W
                inst.rect_h[n] = SCREEN_H
            end
            inst.req_type[n] = refresh_type or "default"
            inst.req_dither[n] = dither == true
            inst.req_full[n] = full
            inst.count = n
        end
        return orig_setDirty(manager, widget, refresh_type, region, dither)
    end

    if type(orig_refreshUI) == "function" then
        Screen.refreshUI = function(screen, x, y, w, h, ...)
            if inst.active then
                record_refresh(x, y, w, h, "direct_refresh", x == nil)
            end
            return orig_refreshUI(screen, x, y, w, h, ...)
        end
    end

    local function invoke(action_fn)
        local ok, result = pcall(action_fn)
        if not ok then return { success = false, reason = "Action exception: " .. tostring(result) } end
        if type(result) == "table" and result.pending then
            self:_settleNaturally(result.settle_ticks or settle_ticks)
            local verify_ok, verified = pcall(result.verify)
            if not verify_ok then return { success = false, reason = "Verification exception: " .. tostring(verified) } end
            return verified
        end
        return result
    end

    local function prepare(reset_fn)
        if not reset_fn then return { success = true } end
        local result = invoke(reset_fn)
        self:_settleNaturally(1)
        return result or { success = false, reason = "Reset returned no result" }
    end

    local function measured(action_fn, instrumented)
        local before = memory_snapshot(false)
        reset_recording()
        inst.active = instrumented ~= false
        local t0 = time.monotonic()
        local result = invoke(action_fn)
        local elapsed = precise_ms(time.monotonic() - t0)
        inst.active = false
        -- invoke() already settled and repainted inside the timed window, so
        -- the buffer here is the finished frame for this transition.
        local frame_hash = framebuffer_hash()
        local after = memory_snapshot(false)

        if type(result) ~= "table" then
            return { status = "FAILED", success = false, reason = "Adapter returned no structured result", wall_time_ms = nil }
        end
        if result.unsupported then
            return { status = "UNSUPPORTED", success = false, reason = result.reason, wall_time_ms = nil }
        end
        if not result.success then
            return { status = "FAILED", success = false, reason = result.reason or "Semantic verification failed", wall_time_ms = nil }
        end
        if result.expected_refresh and instrumented ~= false and inst.refresh_count == 0 then
            return { status = "FAILED", success = false, reason = "Semantic state changed but no natural refresh request was observed", wall_time_ms = nil }
        end

        local dirty_rects = {}
        local refresh_requests = {}
        for i = 1, inst.count or 0 do
            local rx = inst.rect_x[i]
            local ry = inst.rect_y[i]
            local rw = inst.rect_w[i]
            local rh = inst.rect_h[i]
            dirty_rects[i] = { x = rx, y = ry, w = rw, h = rh }
            refresh_requests[i] = {
                x = rx, y = ry, w = rw, h = rh,
                refresh_type = tostring(inst.req_type[i]),
                dither = inst.req_dither[i],
                is_full = inst.req_full[i],
            }
        end

        local union_area, cumulative_area, unique_pct, cumulative_eq, largest_pct =
            Geometry.calculate_spatial_union(dirty_rects)
        if union_area > cumulative_area or unique_pct < 0 or unique_pct > 100 then
            return { status = "FAILED", success = false, reason = "Dirty-region invariant violation", wall_time_ms = nil }
        end
        local out = {
            status = "PASS",
            success = true,
            wall_time_ms = elapsed,
            natural_lua_heap_kb = after.natural_lua_heap_kb,
            lua_heap_delta_kb = after.natural_lua_heap_kb - before.natural_lua_heap_kb,
            rss_kb = after.rss_kb,
            set_dirty_calls = inst.set_dirty_calls,
            refresh_count = inst.refresh_count,
            full_refreshes = inst.full_refreshes,
            partial_refreshes = inst.partial_refreshes,
            cumulative_dirty_area_pixels = cumulative_area,
            spatial_union_dirty_area_pixels = union_area,
            unique_dirty_pct = unique_pct,
            cumulative_dirty_screen_equivalents = cumulative_eq,
            largest_single_dirty_pct = largest_pct,
            refresh_requests = refresh_requests,
            semantic_evidence = result,
        }
        if result.page_before ~= nil then out.page_before = result.page_before end
        if result.page_after ~= nil then out.page_after = result.page_after end
        if result.visible_count_before ~= nil then out.visible_count_before = result.visible_count_before end
        if result.visible_count_after ~= nil then out.visible_count_after = result.visible_count_after end
        if result.total_pages ~= nil then out.total_pages = result.total_pages end
        if result.visible_signature_before ~= nil then out.visible_signature_before = result.visible_signature_before end
        if result.visible_signature_after ~= nil then out.visible_signature_after = result.visible_signature_after end
        if result.visible_items_before ~= nil then out.visible_items_before = result.visible_items_before end
        if result.visible_items_after ~= nil then out.visible_items_after = result.visible_items_after end
        -- Proof that nothing covered the measured widget. Without it a page turn
        -- under a full-screen overlay satisfies every other guard.
        if result.top_widget ~= nil then out.top_widget = result.top_widget end
        if result.windows_above_measured ~= nil then out.windows_above_measured = result.windows_above_measured end
        if result.windows_above_names ~= nil then out.windows_above_names = result.windows_above_names end
        if frame_hash ~= nil then out.framebuffer_hash = frame_hash end
        if result.measured_widget_on_stack ~= nil then out.measured_widget_on_stack = result.measured_widget_on_stack end
        if result.fullscreen_above ~= nil then out.fullscreen_above = result.fullscreen_above end
        return out
    end

    local metric_keys = {
        "wall_time_ms", "natural_lua_heap_kb", "lua_heap_delta_kb", "rss_kb",
        "set_dirty_calls", "refresh_count", "full_refreshes", "partial_refreshes",
        "unique_dirty_pct", "cumulative_dirty_screen_equivalents", "largest_single_dirty_pct",
        "visible_count_before", "visible_count_after", "total_pages",
    }
    local function aggregate(iterations)
        local valid = {}
        for _, iteration in ipairs(iterations) do
            if iteration.status == "PASS" and iteration.wall_time_ms ~= nil then valid[#valid + 1] = iteration end
        end
        if #valid == 0 then
            local first = iterations[1] or {}
            return {
                status = first.status or "FAILED",
                success = false,
                reason = first.reason or "No valid iterations",
                count = #iterations,
                valid_count = 0,
                iterations = iterations,
            }
        end
        local out = { status = "PASS", success = true, count = #iterations, valid_count = #valid, iterations = iterations }
        for _, key in ipairs(metric_keys) do
            local values = {}
            for _, iteration in ipairs(valid) do
                if type(iteration[key]) == "number" then values[#values + 1] = iteration[key] end
            end
            if #values > 0 then
                out[key] = stats(values)
            end
        end
        return out
    end

    local sample_book, sample_folder
    local function scan(path)
        if not path or lfs.attributes(path, "mode") ~= "directory" then return end
        local entries = {}
        for entry in lfs.dir(path) do
            if entry ~= "." and entry ~= ".." and not entry:find("^%.") then entries[#entries + 1] = entry end
        end
        table.sort(entries)
        for _, entry in ipairs(entries) do
            local full = path .. "/" .. entry
            local kind = lfs.attributes(full, "mode")
            if kind == "file" and entry:lower():sub(-5) == ".epub" and not sample_book then sample_book = full end
            if kind == "directory" and not sample_folder then sample_folder = full end
            if kind == "directory" and not sample_book then scan(full) end
        end
    end
    scan(library_dir)
    local target_books, target_folders = {}, {}
    local target_leaf_folder = nil
    local target_leaf_folder_book_count = nil
    local target_reader_book = nil
    local target_reader_book_bytes = nil
    local targets_path = os.getenv("BENCHMARK_TARGETS_FILE")
    if targets_path then
        local target_file = io.open(targets_path, "r")
        if target_file then
            local encoded = target_file:read("*a")
            target_file:close()
            local ok_targets, decoded = pcall(json.decode, encoded)
            if ok_targets and type(decoded) == "table" then
                if type(decoded.books) == "table" then target_books = decoded.books end
                if type(decoded.folders) == "table" then target_folders = decoded.folders end
                if type(decoded.leaf_folder) == "string" then target_leaf_folder = decoded.leaf_folder end
                if type(decoded.leaf_folder_book_count) == "number" then
                    target_leaf_folder_book_count = decoded.leaf_folder_book_count
                end
                if type(decoded.reader_book) == "string" then target_reader_book = decoded.reader_book end
                if type(decoded.reader_book_bytes) == "number" then
                    target_reader_book_bytes = decoded.reader_book_bytes
                end
                results.target_seed = decoded.seed
            end
        end
    end
    if #target_books > 0 then sample_book = target_books[1] end
    if #target_folders > 0 then sample_folder = target_folders[1] end
    results.deterministic_target_counts = { books = #target_books, folders = #target_folders }
    local adapter = Adapters.get_adapter(config_name, library_dir, sample_book, sample_folder)
    if (profile == "paging" or profile == "smoke_validation") and target_leaf_folder then
        -- The runner only names a leaf folder when the library root holds too
        -- few books to page through. This narrows the measured workload, so
        -- record it explicitly: a leaf of a 2692-book corpus is NOT "paging
        -- over 2692 books".
        adapter:set_paging_root(target_leaf_folder)
        results.paging_root = {
            path = target_leaf_folder,
            book_count = target_leaf_folder_book_count,
            dataset_mode = dataset_mode,
            library_book_count = book_count,
        }
    end
    local book_target_index, folder_target_index = 0, 0
    local function select_next_book()
        if #target_books == 0 then return end
        book_target_index = book_target_index % #target_books + 1
        adapter:set_sample_book(target_books[book_target_index])
    end
    -- Reader page turns must stay inside one document: latency tracks document
    -- size and complexity, and this corpus spans 59 KB to 29 MB, so rotating
    -- books would blend unrelated documents into a single median. open_book
    -- keeps rotating on purpose, to measure cold opens rather than a warm
    -- document cache.
    local function select_reader_book()
        local pinned = target_reader_book or target_books[1]
        if not pinned then return false end
        adapter:set_sample_book(pinned)
        return true
    end
    local function select_next_folder()
        if #target_folders == 0 then return end
        folder_target_index = folder_target_index % #target_folders + 1
        adapter:set_sample_folder(target_folders[folder_target_index])
    end

    local startup_settle = settle_ticks
    if config_name:find("simpleui", 1, true) then startup_settle = math.max(settle_ticks, 4) end
    self:_settleNaturally(startup_settle)
    local startup_ready = #missing_plugins == 0 and adapter:startup_ready()
        or { success = false, reason = "Expected plugins are missing" }
    results.startup_ready_assertion = startup_ready
    if startup_ready.success then
        results.internal_harness_to_ui_ready_ms = precise_ms(time.monotonic() - self.harness_init_fts)
        emit_marker("BENCHMARK_UI_READY")
    else
        results.ui_ready_error = startup_ready.reason or "Startup UI semantic readiness failed"
    end

    local function execute(name, action_fn, reset_fn, warmups_override, measures_override, instrumented)
        local warmups = warmups_override or warmup_count
        local measures = measures_override or measure_count
        if mode ~= "warm" then warmups, measures = 0, 1 end
        for _ = 1, warmups do
            prepare(reset_fn)
            measured(action_fn, instrumented)
        end
        local iterations = {}
        for _ = 1, measures do
            prepare(reset_fn)
            iterations[#iterations + 1] = measured(action_fn, instrumented)
        end
        results.scenarios[name] = aggregate(iterations)
        return results.scenarios[name]
    end

    -- Two consecutive transitions that leave a byte-identical framebuffer mean
    -- nothing visibly moved between them, which is what a static overlay covering
    -- the measured widget looks like from the outside.
    local function check_frames_changed(iterations)
        local previous, previous_index
        for index, iteration in ipairs(iterations) do
            local hash = iteration.framebuffer_hash
            if iteration.status == "PASS" and hash then
                if previous and hash == previous then
                    return string.format(
                        "screen did not change between transitions %d and %d (identical framebuffer %s)",
                        previous_index, index, hash)
                end
                previous, previous_index = hash, index
            end
        end
        return nil
    end

    local function run_sequential_paging(scenario_name, adapter_next_fn, adapter_goto_fn, adapter_info_fn, max_target_transitions)
        local cap = max_target_transitions or 30
        local goto_ok = adapter_goto_fn(1)
        self:_settleNaturally(settle_ticks)
        local info = adapter_info_fn()
        local total_pages = (info and info.total_pages) or 1
        local available_transitions = math.max(0, total_pages - 1)
        local requested_transitions = math.min(cap, available_transitions)

        if total_pages <= 1 or available_transitions <= 0 then
            results.scenarios[scenario_name] = {
                status = "UNSUPPORTED", success = false, count = 0, valid_count = 0,
                transition_cap = cap, available_transitions = 0,
                requested_transitions = 0, actual_transitions = 0,
                total_pages = total_pages,
                reason = "Library has only 1 page, cannot measure sequential paging", iterations = {},
            }
            return results.scenarios[scenario_name]
        end

        if not goto_ok or not info or (info.current_page and info.current_page ~= 1) then
            results.scenarios[scenario_name] = {
                status = "FAILED", success = false, count = 0, valid_count = 0,
                transition_cap = cap, available_transitions = available_transitions,
                requested_transitions = requested_transitions, actual_transitions = 0,
                total_pages = total_pages,
                reason = "Failed to navigate to page 1 before sequential paging", iterations = {},
            }
            return results.scenarios[scenario_name]
        end

        local iterations = {}
        local current_p = 1
        for _ = 1, requested_transitions do
            local from_p = current_p
            local to_p = from_p + 1
            local iteration_result = measured(function()
                return adapter_next_fn(from_p, to_p)
            end)
            iterations[#iterations + 1] = iteration_result
            if iteration_result.status ~= "PASS" then
                break
            end
            current_p = to_p
        end
        local agg = aggregate(iterations)
        agg.transition_cap = cap
        agg.available_transitions = available_transitions
        agg.requested_transitions = requested_transitions
        agg.actual_transitions = agg.valid_count or 0
        agg.total_pages = total_pages
        if agg.actual_transitions ~= requested_transitions then
            agg.status = "FAILED"
            agg.success = false
            agg.reason = agg.reason or string.format("Actual transitions (%d) did not match requested transitions (%d)", agg.actual_transitions, requested_transitions)
        end
        local frozen = check_frames_changed(iterations)
        if frozen and agg.status == "PASS" then
            agg.status = "FAILED"
            agg.success = false
            agg.reason = frozen
        end
        results.scenarios[scenario_name] = agg
        return results.scenarios[scenario_name]
    end

    local function run_cached_paging(scenario_name, adapter_next_fn, adapter_prev_fn, adapter_goto_fn, adapter_info_fn, target_transitions)
        local cap = target_transitions or 30
        local goto_ok = adapter_goto_fn(1)
        self:_settleNaturally(settle_ticks)
        local info = adapter_info_fn()
        local total_pages = (info and info.total_pages) or 1
        if total_pages < 2 then
            results.scenarios[scenario_name] = {
                status = "UNSUPPORTED", success = false, count = 0, valid_count = 0,
                transition_cap = cap, available_transitions = 0,
                requested_transitions = 0, actual_transitions = 0,
                total_pages = total_pages,
                reason = "Library requires at least 2 pages for cached paging", iterations = {},
            }
            return results.scenarios[scenario_name]
        end

        if not goto_ok or not info or (info.current_page and info.current_page ~= 1) then
            results.scenarios[scenario_name] = {
                status = "FAILED", success = false, count = 0, valid_count = 0,
                transition_cap = cap, available_transitions = total_pages - 1,
                requested_transitions = cap, actual_transitions = 0,
                total_pages = total_pages,
                reason = "Failed to navigate to page 1 before cached paging warmup", iterations = {},
            }
            return results.scenarios[scenario_name]
        end

        -- Cache warm-up (unmeasured): 1 -> 2, then 2 -> 1
        local w1 = invoke(function() return adapter_next_fn(1, 2) end)
        self:_settleNaturally(1)
        local w1_info = adapter_info_fn()
        if not w1.success or not w1_info or (w1_info.current_page and w1_info.current_page ~= 2) then
            results.scenarios[scenario_name] = {
                status = "FAILED", success = false, count = 0, valid_count = 0,
                transition_cap = cap, available_transitions = total_pages - 1,
                requested_transitions = cap, actual_transitions = 0,
                total_pages = total_pages,
                reason = "Cached paging warmup 1->2 failed: " .. tostring(w1.reason), iterations = {},
            }
            return results.scenarios[scenario_name]
        end

        local w2 = invoke(function() return adapter_prev_fn(2, 1) end)
        self:_settleNaturally(1)
        local w2_info = adapter_info_fn()
        if not w2.success or not w2_info or (w2_info.current_page and w2_info.current_page ~= 1) then
            results.scenarios[scenario_name] = {
                status = "FAILED", success = false, count = 0, valid_count = 0,
                transition_cap = cap, available_transitions = total_pages - 1,
                requested_transitions = cap, actual_transitions = 0,
                total_pages = total_pages,
                reason = "Cached paging warmup 2->1 failed: " .. tostring(w2.reason), iterations = {},
            }
            return results.scenarios[scenario_name]
        end

        local requested_transitions = cap
        local iterations = {}
        local cur_page = 1
        for _ = 1, requested_transitions do
            local from_p = cur_page
            local to_p = (cur_page == 1) and 2 or 1
            local action_fn = (cur_page == 1)
                and (function() return adapter_next_fn(from_p, to_p) end)
                or  (function() return adapter_prev_fn(from_p, to_p) end)
            local iteration_result = measured(action_fn)
            iterations[#iterations + 1] = iteration_result
            if iteration_result.status ~= "PASS" then
                break
            end
            cur_page = to_p
        end
        local agg = aggregate(iterations)
        agg.transition_cap = cap
        agg.available_transitions = total_pages - 1
        agg.requested_transitions = requested_transitions
        agg.actual_transitions = agg.valid_count or 0
        agg.warmup_verified = true
        agg.total_pages = total_pages
        if agg.actual_transitions ~= requested_transitions then
            agg.status = "FAILED"
            agg.success = false
            agg.reason = agg.reason or string.format("Actual transitions (%d) did not match requested transitions (%d)", agg.actual_transitions, requested_transitions)
        end
        local frozen = check_frames_changed(iterations)
        if frozen and agg.status == "PASS" then
            agg.status = "FAILED"
            agg.success = false
            agg.reason = frozen
        end
        results.scenarios[scenario_name] = agg
        return results.scenarios[scenario_name]
    end

    -- A dataset/config combination that silently yields zero measured paging
    -- transitions (e.g. a hierarchical root with no descent, or an empty
    -- Bookshelf) must not be reported as a passing run.
    local function require_real_paging_data(has_bookshelf)
        local problems = {}
        local measured_names = { "library_sequential_paging", "library_cached_paging" }
        if has_bookshelf then
            table.insert(measured_names, "bookshelf_sequential_paging")
            table.insert(measured_names, "bookshelf_cached_paging")
            table.insert(measured_names, "bookshelf_sequential_paging_anim_off")
            table.insert(measured_names, "bookshelf_cached_paging_anim_off")
        end
        for _, name in ipairs(measured_names) do
            local sc = results.scenarios[name]
            if not sc or sc.status ~= "PASS" or not ((sc.actual_transitions or 0) > 0) then
                problems[#problems + 1] = string.format("%s=%s", name, tostring(sc and sc.status))
            end
        end
        if has_bookshelf then
            for _, name in ipairs({ "open_bookshelf", "close_bookshelf" }) do
                local sc = results.scenarios[name]
                if not sc or sc.status ~= "PASS" then
                    problems[#problems + 1] = string.format("%s=%s", name, tostring(sc and sc.status))
                end
            end
        end
        return problems
    end

    results.memory_checkpoints.post_init_idle = memory_snapshot(true)

    if #missing_plugins > 0 or not startup_ready.success then
        results.run_status = "FAILED"
        results.failure_reason = #missing_plugins > 0
            and "Expected plugins were not loaded"
            or "Startup UI readiness assertion failed"
    else
        if profile == "paging" then
            -- Unmeasured setup: deterministically enter library and settle page 1
            adapter:ensure_filemanager()
            adapter:goto_page(1)
            self:_settleNaturally(settle_ticks)
            emit_marker("BENCHMARK_LIBRARY_READY")

            -- Paging Scenario 1: library_sequential_paging (uncached forward navigation)
            run_sequential_paging("library_sequential_paging",
                function(f, t) return adapter:library_next_page_transition(f, t) end,
                function(p) return adapter:goto_page(p) end,
                function() return adapter:get_page_info() end, 30)

            -- Visual proof that the measured library was actually on screen.
            -- Window-stack topology cannot tell a stack's own full-screen
            -- library container from an overlay hiding it, so every paging run
            -- carries an unmeasured before/after capture of a real 2->3 turn.
            local probe_info = adapter:get_page_info()
            if probe_info and (probe_info.total_pages or 1) >= 3 then
                adapter:goto_page(2)
                self:_settleNaturally(settle_ticks)
                local shot_before = probe_screenshot("paging_probe_page2_before")
                local probe_res = measured(function() return adapter:library_next_page_transition(2, 3) end)
                local shot_after = probe_screenshot("paging_probe_page3_after")
                local probe_agg = aggregate({ probe_res })
                probe_agg.transition_cap = 1
                probe_agg.available_transitions = probe_info.total_pages - 1
                probe_agg.requested_transitions = 1
                probe_agg.actual_transitions = probe_res.status == "PASS" and 1 or 0
                probe_agg.total_pages = probe_info.total_pages
                probe_agg.screenshot_before = shot_before
                probe_agg.screenshot_after = shot_after
                results.scenarios["paging_probe_step_2_to_3"] = probe_agg
            else
                results.scenarios["paging_probe_step_2_to_3"] = {
                    status = "UNSUPPORTED", success = false, count = 0, valid_count = 0,
                    transition_cap = 1, available_transitions = 0,
                    requested_transitions = 0, actual_transitions = 0,
                    total_pages = probe_info and probe_info.total_pages or 1,
                    reason = "Library has <3 pages, probe 2->3 skipped", iterations = {},
                }
            end
            adapter:goto_page(1)
            self:_settleNaturally(settle_ticks)

            -- Paging Scenario 2: library_cached_paging (repeated 1->2 and 2->1 between rendered pages)
            run_cached_paging("library_cached_paging",
                function(f, t) return adapter:library_next_page_transition(f, t) end,
                function(f, t) return adapter:library_prev_page_transition(f, t) end,
                function(p) return adapter:goto_page(p) end,
                function() return adapter:get_page_info() end, 30)

            local has_bookshelf = config_name:lower():find("bookshelf", 1, true) ~= nil
            if has_bookshelf then
                execute("open_bookshelf", function() return adapter:open_bookshelf() end,
                    function() return adapter:close_bookshelf() end, 1, 1)

                -- Mode 1: animation_on_default
                local anim1_ok = adapter:set_bookshelf_animation("medium")
                local bs_seq = run_sequential_paging("bookshelf_sequential_paging",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_seq.animation = "animation_on_default"
                bs_seq.animation_verified = anim1_ok

                local bs_cac = run_cached_paging("bookshelf_cached_paging",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(f, t) return adapter:bookshelf_prev_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_cac.animation = "animation_on_default"
                bs_cac.animation_verified = anim1_ok

                -- Mode 2: animation_off
                local anim2_ok = adapter:set_bookshelf_animation("off")
                local bs_seq_off = run_sequential_paging("bookshelf_sequential_paging_anim_off",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_seq_off.animation = "animation_off"
                bs_seq_off.animation_verified = anim2_ok

                local bs_cac_off = run_cached_paging("bookshelf_cached_paging_anim_off",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(f, t) return adapter:bookshelf_prev_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_cac_off.animation = "animation_off"
                bs_cac_off.animation_verified = anim2_ok

                adapter:set_bookshelf_animation("medium")

                execute("close_bookshelf", function() return adapter:close_bookshelf() end,
                    function() return adapter:open_bookshelf() end, 1, 1)
            end
            results.memory_checkpoints.post_stress_idle = memory_snapshot(true)
            local paging_problems = require_real_paging_data(has_bookshelf)
            if #paging_problems > 0 then
                results.run_status = "FAILED"
                results.failure_reason = "Paging profile produced no measured transitions for: " .. table.concat(paging_problems, ", ")
            else
                results.run_status = "PASS"
            end
        elseif profile == "smoke_validation" then
            -- Unmeasured setup: deterministically enter library and settle page 1
            adapter:ensure_filemanager()
            adapter:goto_page(1)
            self:_settleNaturally(settle_ticks)
            emit_marker("BENCHMARK_LIBRARY_READY")

            -- Smoke Step 1: verify 1 -> 2 transition (transition_cap = 1)
            run_sequential_paging("library_sequential_paging",
                function(f, t) return adapter:library_next_page_transition(f, t) end,
                function(p) return adapter:goto_page(p) end,
                function() return adapter:get_page_info() end, 1)

            -- Return to page 1, then explicitly exercise the invalid no-op request.
            -- The adapter must reject it before touching the UI; the guard itself is
            -- a PASS only when the attempted transition status is FAILED.
            adapter:goto_page(1)
            self:_settleNaturally(settle_ticks)
            local noop = adapter:library_next_page_transition(1, 1)
            local noop_rejected = type(noop) == "table"
                and noop.success == false and noop.unsupported ~= true
            results.scenarios["smoke_noop_guard"] = {
                status = noop_rejected and "PASS" or "FAILED",
                success = noop_rejected,
                attempted_status = noop_rejected and "FAILED" or "PASS",
                attempted_page_before = 1,
                attempted_page_after = 1,
                reason = noop_rejected and noop.reason or "Adapter accepted a page no-op request",
                iterations = {},
            }

            -- Smoke Step 2 Probe: validation probe 2 -> 3 (if page 3 available)
            local pinfo = adapter:get_page_info()
            if pinfo and (pinfo.total_pages or 1) >= 3 then
                adapter:goto_page(2)
                self:_settleNaturally(settle_ticks)
                local shot_before = probe_screenshot("smoke_probe_page2_before")
                local probe_res = measured(function() return adapter:library_next_page_transition(2, 3) end)
                local shot_after = probe_screenshot("smoke_probe_page3_after")
                local probe_agg = aggregate({ probe_res })
                probe_agg.transition_cap = 1
                probe_agg.available_transitions = pinfo.total_pages - 1
                probe_agg.requested_transitions = 1
                probe_agg.actual_transitions = probe_res.status == "PASS" and 1 or 0
                probe_agg.total_pages = pinfo.total_pages
                probe_agg.screenshot_before = shot_before
                probe_agg.screenshot_after = shot_after
                results.scenarios["smoke_probe_step_2_to_3"] = probe_agg
            else
                results.scenarios["smoke_probe_step_2_to_3"] = {
                    status = "UNSUPPORTED", success = false, count = 0, valid_count = 0,
                    transition_cap = 1, available_transitions = 0,
                    requested_transitions = 0, actual_transitions = 0,
                    total_pages = pinfo and pinfo.total_pages or 1,
                    reason = "Library has <3 pages, probe 2->3 skipped", iterations = {},
                }
            end

            -- Smoke Cached paging: warmup + 30 alternating
            run_cached_paging("library_cached_paging",
                function(f, t) return adapter:library_next_page_transition(f, t) end,
                function(f, t) return adapter:library_prev_page_transition(f, t) end,
                function(p) return adapter:goto_page(p) end,
                function() return adapter:get_page_info() end, 30)

            local has_bookshelf = config_name:lower():find("bookshelf", 1, true) ~= nil
            if has_bookshelf then
                execute("open_bookshelf", function() return adapter:open_bookshelf() end,
                    function() return adapter:close_bookshelf() end, 1, 1)

                -- Mode 1: animation_on_default
                local anim1_ok = adapter:set_bookshelf_animation("medium")
                local bs_seq = run_sequential_paging("bookshelf_sequential_paging",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 1)
                bs_seq.animation = "animation_on_default"
                bs_seq.animation_verified = anim1_ok

                -- Step 2 Probe Bookshelf:
                local bs_info = adapter:get_bookshelf_page_info()
                if bs_info and (bs_info.total_pages or 1) >= 3 then
                    adapter:goto_bookshelf_page(2)
                    self:_settleNaturally(settle_ticks)
                    local shot_before = probe_screenshot("bookshelf_probe_page2_before")
                    local probe_res = measured(function() return adapter:bookshelf_next_page_transition(2, 3) end)
                    local shot_after = probe_screenshot("bookshelf_probe_page3_after")
                    local probe_agg = aggregate({ probe_res })
                    probe_agg.transition_cap = 1
                    probe_agg.available_transitions = bs_info.total_pages - 1
                    probe_agg.requested_transitions = 1
                    probe_agg.actual_transitions = probe_res.status == "PASS" and 1 or 0
                    probe_agg.total_pages = bs_info.total_pages
                    probe_agg.animation = "animation_on_default"
                    probe_agg.animation_verified = anim1_ok
                    probe_agg.screenshot_before = shot_before
                    probe_agg.screenshot_after = shot_after
                    results.scenarios["bookshelf_probe_step_2_to_3"] = probe_agg
                else
                    results.scenarios["bookshelf_probe_step_2_to_3"] = {
                        status = "UNSUPPORTED", success = false, count = 0, valid_count = 0,
                        transition_cap = 1, available_transitions = 0,
                        requested_transitions = 0, actual_transitions = 0,
                        total_pages = bs_info and bs_info.total_pages or 1,
                        animation = "animation_on_default",
                        animation_verified = anim1_ok,
                        reason = "Bookshelf has <3 pages, probe 2->3 skipped", iterations = {},
                    }
                end

                local bs_cac = run_cached_paging("bookshelf_cached_paging",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(f, t) return adapter:bookshelf_prev_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_cac.animation = "animation_on_default"
                bs_cac.animation_verified = anim1_ok

                -- Mode 2: animation_off
                local anim2_ok = adapter:set_bookshelf_animation("off")
                local bs_seq_off = run_sequential_paging("bookshelf_sequential_paging_anim_off",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 1)
                bs_seq_off.animation = "animation_off"
                bs_seq_off.animation_verified = anim2_ok

                local bs_cac_off = run_cached_paging("bookshelf_cached_paging_anim_off",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(f, t) return adapter:bookshelf_prev_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_cac_off.animation = "animation_off"
                bs_cac_off.animation_verified = anim2_ok

                adapter:set_bookshelf_animation("medium")

                execute("close_bookshelf", function() return adapter:close_bookshelf() end,
                    function() return adapter:open_bookshelf() end, 1, 1)
            end
            results.memory_checkpoints.post_stress_idle = memory_snapshot(true)
            local smoke_paging_problems = require_real_paging_data(has_bookshelf)
            if #smoke_paging_problems > 0 then
                results.run_status = "FAILED"
                results.failure_reason = "Smoke validation profile produced no measured transitions for: " .. table.concat(smoke_paging_problems, ", ")
            else
                results.run_status = "PASS"
            end
        elseif profile == "startup" then
            execute("home_to_library", function() return adapter:home_to_library() end,
                function() return adapter:start_to_home() end)
            local library_result = execute("library_first_render", function() return adapter:library_first_render() end)
            if library_result.status == "PASS" then emit_marker("BENCHMARK_LIBRARY_READY") end
            results.memory_checkpoints.post_library_render_idle = memory_snapshot(true)
            results.run_status = library_result.status == "PASS" and "PASS" or "FAILED"
            if results.run_status == "FAILED" then
                results.failure_reason = "Startup profile did not reach a usable library"
            end
        else
            execute("start_to_home", function() return adapter:start_to_home() end,
                function() return adapter:home_to_library() end)
            execute("home_to_library", function() return adapter:home_to_library() end,
                function() return adapter:start_to_home() end)
            local library_result = execute("library_first_render", function() return adapter:library_first_render() end)
            if library_result.status == "PASS" then emit_marker("BENCHMARK_LIBRARY_READY") end
            results.memory_checkpoints.post_library_render_idle = memory_snapshot(true)

            local folder_count = profile == "real" and 10 or measure_count
            local book_ops = profile == "real" and 10 or measure_count

            -- Paging Scenario 1: library_sequential_paging (uncached forward navigation)
            run_sequential_paging("library_sequential_paging",
                function(f, t) return adapter:library_next_page_transition(f, t) end,
                function(p) return adapter:goto_page(p) end,
                function() return adapter:get_page_info() end, 30)

            -- Paging Scenario 2: library_cached_paging (repeated 1->2 and 2->1 between rendered pages)
            run_cached_paging("library_cached_paging",
                function(f, t) return adapter:library_next_page_transition(f, t) end,
                function(f, t) return adapter:library_prev_page_transition(f, t) end,
                function(p) return adapter:goto_page(p) end,
                function() return adapter:get_page_info() end, 30)

            if sample_folder then
                execute("library_folder_enter", function()
                        select_next_folder()
                        return adapter:library_folder_enter()
                    end,
                    function() return adapter:library_folder_back() end, nil, folder_count)
                execute("library_folder_back", function() return adapter:library_folder_back() end,
                    function()
                        select_next_folder()
                        return adapter:library_folder_enter()
                    end, nil, folder_count)
            end
            execute("change_sort_mode", function() return adapter:change_sort_mode() end)
            if sample_book then
                execute("open_book_minimal", function()
                        select_next_book()
                        return adapter:open_book()
                    end,
                    function() return adapter:close_book() end, nil, book_ops, false)
                execute("open_book", function()
                        select_next_book()
                        return adapter:open_book()
                    end,
                    function() return adapter:close_book() end, nil, book_ops, true)
                if profile == "bookends_control" then
                    local pinned_reader = select_reader_book()
                    results.reader_book = {
                        path = pinned_reader and (target_reader_book or target_books[1]) or nil,
                        bytes = pinned_reader and target_reader_book_bytes or nil,
                        pinned = pinned_reader,
                    }
                    local post_reader_heap_samples = {}
                    local reader_cycle_failures = {}
                    for cycle_index = 1, 10 do
                        select_reader_book()
                        local opened = invoke(function() return adapter:open_book() end)
                        self:_settleNaturally(1)
                        local cycle_ok = type(opened) == "table" and opened.success == true
                        local failure_reason = cycle_ok and nil
                            or "open failed: " .. tostring(type(opened) == "table" and opened.reason or opened)
                        for turn_index = 1, 10 do
                            if not cycle_ok then break end
                            local turned = invoke(function() return adapter:reader_page_turn() end)
                            if type(turned) ~= "table" or turned.success ~= true then
                                cycle_ok = false
                                failure_reason = string.format("turn %d failed: %s", turn_index,
                                    tostring(type(turned) == "table" and turned.reason or turned))
                            end
                        end
                        local closed = invoke(function() return adapter:close_book() end)
                        self:_settleNaturally(1)
                        if type(closed) ~= "table" or closed.success ~= true then
                            cycle_ok = false
                            failure_reason = failure_reason or
                                "close failed: " .. tostring(type(closed) == "table" and closed.reason or closed)
                        end
                        if cycle_ok then
                            local snap = memory_snapshot(true)
                            post_reader_heap_samples[#post_reader_heap_samples + 1] = snap.forced_gc_live_heap_kb
                        else
                            collectgarbage("collect")
                            reader_cycle_failures[#reader_cycle_failures + 1] = {
                                cycle = cycle_index,
                                reason = failure_reason or "reader cycle failed",
                            }
                        end
                    end
                    results.bookends_reader_cycles_completed = #post_reader_heap_samples
                    results.bookends_reader_cycle_failures = #reader_cycle_failures > 0 and reader_cycle_failures or nil
                    results.bookends_reader_cycles_live_heap_kb = post_reader_heap_samples
                    results.bookends_reader_cycles_stats = stats(post_reader_heap_samples)
                    execute("reader_page_turn", function() return adapter:reader_page_turn() end,
                        function()
                            select_reader_book()
                            return adapter:open_book()
                        end, 0, 10)
                end
                execute("close_book", function() return adapter:close_book() end,
                    function()
                        select_next_book()
                        return adapter:open_book()
                    end, nil, book_ops)
            end

            local has_bookshelf = config_name:lower():find("bookshelf", 1, true) ~= nil
            if has_bookshelf and profile ~= "startup" and mode ~= "first_run_cold" and mode ~= "real_first_run" then
                execute("open_bookshelf", function() return adapter:open_bookshelf() end,
                    function() return adapter:close_bookshelf() end, 1, 10)
                execute("bookshelf_first_render", function() return adapter:bookshelf_first_render() end, nil, 1, 10)

                -- Mode 1: animation_on_default (standard default user experience)
                local anim1_ok = adapter:set_bookshelf_animation("medium")
                local bs_seq = run_sequential_paging("bookshelf_sequential_paging",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_seq.animation = "animation_on_default"
                bs_seq.animation_verified = anim1_ok

                local bs_cac = run_cached_paging("bookshelf_cached_paging",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(f, t) return adapter:bookshelf_prev_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_cac.animation = "animation_on_default"
                bs_cac.animation_verified = anim1_ok

                -- Mode 2: animation_off (renderer comparison without animation latency)
                local anim2_ok = adapter:set_bookshelf_animation("off")
                local bs_seq_off = run_sequential_paging("bookshelf_sequential_paging_anim_off",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_seq_off.animation = "animation_off"
                bs_seq_off.animation_verified = anim2_ok

                local bs_cac_off = run_cached_paging("bookshelf_cached_paging_anim_off",
                    function(f, t) return adapter:bookshelf_next_page_transition(f, t) end,
                    function(f, t) return adapter:bookshelf_prev_page_transition(f, t) end,
                    function(p) return adapter:goto_bookshelf_page(p) end,
                    function() return adapter:get_bookshelf_page_info() end, 30)
                bs_cac_off.animation = "animation_off"
                bs_cac_off.animation_verified = anim2_ok

                -- Restore default animation
                adapter:set_bookshelf_animation("medium")

                execute("close_bookshelf", function() return adapter:close_bookshelf() end,
                    function() return adapter:open_bookshelf() end, 1, 10)
            end

            if profile ~= "bookends_control" then
                execute("open_quick_settings", function() return adapter:open_quick_settings() end,
                    function() return adapter:close_quick_settings() end)
                execute("close_quick_settings", function() return adapter:close_quick_settings() end,
                    function() return adapter:open_quick_settings() end)
                local transitions = profile == "real" and 30 or 10
                local rep_action = function()
                    local performed = 0
                    for _ = 1, transitions / 2 do
                        local forward = invoke(function() return adapter:library_next_page_transition(1, 2) end)
                        if forward.unsupported then
                            return adapter:unsupported("Library has only one page, repeated navigation requires multiple pages")
                        end
                        if not forward.success then return forward end
                        performed = performed + 1
                        local backward = invoke(function() return adapter:library_prev_page_transition(2, 1) end)
                        if backward.unsupported then
                            return adapter:unsupported("Library has only one page, repeated navigation requires multiple pages")
                        end
                        if not backward.success then return backward end
                        performed = performed + 1
                    end
                    return adapter:ok({ transitions = performed, expected_refresh = true })
                end
                adapter:goto_page(1)
                execute("repeated_nav", rep_action, function() return adapter:goto_page(1) end, profile == "real" and 0 or 1, profile == "real" and 1 or 2)
            end
            results.memory_checkpoints.post_stress_idle = memory_snapshot(true)
            results.run_status = "PASS"
        end
    end

    -- Dedicated control only; it is not multiplied across the full matrix.
    if profile ~= "startup" and os.getenv("BENCHMARK_RUN_OVERHEAD") == "1" and config_name == "A_stock" then
        local controls = {}
        if profile == "paging" or profile == "smoke_validation" then
            controls.library_sequential_paging = {
                action = function() return adapter:library_next_page_transition(1, 2) end,
                reset = function() return adapter:goto_page(1) end,
            }
        else
            controls.library_first_render = {
                action = function() return adapter:library_first_render() end,
                reset = nil,
            }
            controls.library_sequential_paging = {
                action = function() return adapter:library_next_page_transition(1, 2) end,
                reset = function() return adapter:goto_page(1) end,
            }
            controls.open_book = {
                action = function() return adapter:open_book() end,
                reset = function() return adapter:close_book() end,
            }
        end
        local repetitions = tonumber(os.getenv("BENCHMARK_OVERHEAD_COUNT")) or 30
        results.instrumentation_overhead_validation = {}
        for scenario, control in pairs(controls) do
            local minimal, full = {}, {}
            for index = 1, repetitions do
                prepare(control.reset)
                local first_full = index % 2 == 0
                local a = measured(control.action, first_full)
                prepare(control.reset)
                local b = measured(control.action, not first_full)
                local full_sample = first_full and a or b
                local minimal_sample = first_full and b or a
                if full_sample.status == "PASS" then full[#full + 1] = full_sample.wall_time_ms end
                if minimal_sample.status == "PASS" then minimal[#minimal + 1] = minimal_sample.wall_time_ms end
            end
            local minimal_stats, full_stats = stats(minimal), stats(full)
            local delta = minimal_stats and full_stats and full_stats.median - minimal_stats.median or nil
            results.instrumentation_overhead_validation[scenario] = {
                sample_count = math.min(#minimal, #full),
                minimal = minimal_stats,
                full = full_stats,
                median_delta_ms = delta,
                relative_overhead_pct = delta and minimal_stats.median > 0 and delta / minimal_stats.median * 100 or nil,
            }
        end
    end

    UIManager.setDirty = orig_setDirty
    local file = io.open(output_file, "w")
    if file then file:write(json.encode(results)); file:close() end
    emit_marker("BENCHMARK_COMPLETE")
    UIManager:nextTick(function() UIManager:quit(results.run_status == "PASS" and 0 or 1) end)
end

return Benchmark
