-- Energy proxies: what a stack makes the machine do, per window of real time.
-- Battery itself cannot be read in the emulator. These counters say how much
-- work happens, not what that work costs in mAh on a device.
--
-- During a window the harness sleeps through UIManager:scheduleIn, so the main
-- loop blocks in input polling as it does for a reader, instead of the
-- nextTick polling the latency scenarios use.
local ffi = require("ffi")
local time = require("ui/time")

local Energy = {}

Energy.REFRESH_IMPS = {
    refreshFullImp = "full", refreshFlashPartialImp = "full", refreshFlashUIImp = "full",
    refreshPartialImp = "partial", refreshNoMergePartialImp = "partial",
    refreshUIImp = "ui", refreshNoMergeUIImp = "ui",
    refreshFastImp = "fast", refreshA2Imp = "fast",
}

local RUSAGE_SELF, RUSAGE_CHILDREN = 0, -1

local function usage(who)
    local u = ffi.new("struct rusage")
    if ffi.C.getrusage(who, u) ~= 0 then error("getrusage failed") end
    local function ms(tv) return tonumber(tv.tv_sec) * 1000 + tonumber(tv.tv_usec) / 1000 end
    return {
        user_ms = ms(u.ru_utime), sys_ms = ms(u.ru_stime),
        nvcsw = tonumber(u.ru_nvcsw), nivcsw = tonumber(u.ru_nivcsw),
        inblock = tonumber(u.ru_inblock), oublock = tonumber(u.ru_oublock),
    }
end

-- "/a/b/plugins/m1n1mal.koplugin/main.lua", 12 -> "plugins/m1n1mal.koplugin/main.lua:12"
function Energy.task_label(action)
    if type(action) ~= "function" then return "non_function:0" end
    local info = debug.getinfo(action, "S")
    local src = (info.source or "?"):gsub("^@", "")
    src = src:match("(plugins/.*)$") or src:match("(frontend/.*)$") or src:match("(ffi/.*)$") or src
    return src .. ":" .. tostring(info.linedefined or 0)
end

local function is_harness_task(label)
    return label:find("benchmark.koplugin", 1, true) ~= nil
end

-- deps: UIManager, Screen, input (the object UIManager calls waitEvent on)
function Energy.install(deps)
    local UI, Screen, input = deps.UIManager, deps.Screen, deps.input
    local c
    local saved = {}
    local function save(owner, key)
        saved[#saved + 1] = { owner = owner, key = key, raw = rawget(owner, key) }
    end

    local function reset()
        c = { wakeups = 0, tasks_fired = 0, tasks_by_source = {}, set_dirty_calls = 0,
              refreshes = 0, refresh_pixels = 0, refresh_by_type = {} }
    end
    reset()

    local active = false

    save(input, "waitEvent")
    local waitEvent = input.waitEvent
    input.waitEvent = function(...)
        local a, b, d = waitEvent(...)
        if active then c.wakeups = c.wakeups + 1 end
        return a, b, d
    end

    -- Tasks due now, read before the queue is consumed. A task that becomes due
    -- in the microseconds before _checkTasks reads its own clock runs uncounted.
    save(UI, "_checkTasks")
    local checkTasks = UI._checkTasks
    UI._checkTasks = function(manager)
        if active then
            local queue, now = manager._task_queue, time.now()
            for i = #queue, 1, -1 do
                if queue[i].time > now then break end
                local label = Energy.task_label(queue[i].action)
                if not is_harness_task(label) then
                    c.tasks_fired = c.tasks_fired + 1
                    c.tasks_by_source[label] = (c.tasks_by_source[label] or 0) + 1
                end
            end
        end
        return checkTasks(manager)
    end

    save(UI, "setDirty")
    local setDirty = UI.setDirty
    UI.setDirty = function(...)
        if active then c.set_dirty_calls = c.set_dirty_calls + 1 end
        return setDirty(...)
    end

    -- The Imp methods call each other, so only the outermost one is the request.
    local depth = 0
    local names = {}
    for name in pairs(Energy.REFRESH_IMPS) do names[#names + 1] = name end
    table.sort(names)
    for _, name in ipairs(names) do
        local kind = Energy.REFRESH_IMPS[name]
        save(Screen, name)
        local native = Screen[name]
        Screen[name] = function(screen, x, y, w, h, ...)
            if active and depth == 0 then
                local bb = screen.full_bb or screen.bb
                local pixels
                if x and bb and bb.getBoundedRect then
                    local _, _, bw, bh = bb:getBoundedRect(x, y, w, h)
                    pixels = bw * bh
                else
                    pixels = screen:getWidth() * screen:getHeight()
                end
                c.refreshes = c.refreshes + 1
                c.refresh_pixels = c.refresh_pixels + pixels
                local slot = c.refresh_by_type[kind] or { count = 0, pixels = 0 }
                slot.count = slot.count + 1
                slot.pixels = slot.pixels + pixels
                c.refresh_by_type[kind] = slot
            end
            depth = depth + 1
            local r = table.pack(pcall(native, screen, x, y, w, h, ...))
            depth = depth - 1
            if not r[1] then error(r[2], 0) end
            return table.unpack(r, 2, r.n)
        end
    end

    local E = {}

    -- Runs body inside a counted window; returns the record for that window.
    function E.window(name, body)
        reset()
        local rec = { name = name, status = "PASS", actions = 0 }
        local self_0, kids_0 = usage(RUSAGE_SELF), usage(RUSAGE_CHILDREN)
        local heap_0 = collectgarbage("count")
        local t0 = time.monotonic()
        active = true
        local ok, actions, reason = pcall(body)
        active = false
        rec.wall_s = time.to_s(time.monotonic() - t0)
        local self_1, kids_1 = usage(RUSAGE_SELF), usage(RUSAGE_CHILDREN)
        if not ok then
            rec.status, rec.reason = "FAILED", tostring(actions)
        elseif reason then
            rec.status, rec.reason, rec.actions = "FAILED", tostring(reason), actions or 0
        else
            rec.actions = actions or 0
        end
        rec.cpu_user_ms = self_1.user_ms - self_0.user_ms
        rec.cpu_sys_ms = self_1.sys_ms - self_0.sys_ms
        -- Only children already reaped are visible here.
        rec.cpu_children_ms = (kids_1.user_ms - kids_0.user_ms) + (kids_1.sys_ms - kids_0.sys_ms)
        rec.cpu_total_ms = rec.cpu_user_ms + rec.cpu_sys_ms + rec.cpu_children_ms
        rec.voluntary_switches = self_1.nvcsw - self_0.nvcsw
        rec.involuntary_switches = self_1.nivcsw - self_0.nivcsw
        rec.disk_reads = self_1.inblock - self_0.inblock
        rec.disk_writes = self_1.oublock - self_0.oublock
        rec.heap_delta_kb = collectgarbage("count") - heap_0
        rec.wakeups = c.wakeups
        rec.tasks_fired = c.tasks_fired
        rec.tasks_by_source = c.tasks_by_source
        rec.set_dirty_calls = c.set_dirty_calls
        rec.refreshes = c.refreshes
        rec.refresh_pixels = c.refresh_pixels
        rec.refresh_by_type = c.refresh_by_type
        return rec
    end

    function E.restore()
        active = false
        for i = #saved, 1, -1 do
            local s = saved[i]
            s.owner[s.key] = s.raw
        end
    end

    return E
end

-- ctx: adapter, sleep(s), settle(ticks), settle_ticks, emit_ready(), select_next_book(),
-- select_next_folder(), select_reader_book(), meter (from install), idle_s, tail_s, pace_s,
-- turns, cycles, nav_cycles, reader_short_turns, reader_long_turns
function Energy.run(ctx)
    local adapter, sleep, meter = ctx.adapter, ctx.sleep, ctx.meter
    local windows = {}
    local failure

    local function act(fn)
        local ok, result = pcall(fn)
        if not ok then return false, "action exception: " .. tostring(result) end
        if type(result) == "table" and result.pending then
            ctx.settle(result.settle_ticks or ctx.settle_ticks)
            local verify_ok, verified = pcall(result.verify)
            if not verify_ok then return false, "verify exception: " .. tostring(verified) end
            result = verified
        end
        if type(result) ~= "table" or result.success == false then
            return false, type(result) == "table" and tostring(result.reason) or "no result"
        end
        return true
    end

    -- Progress for whoever watches the log: a long window is otherwise silent.
    local function heartbeat(text)
        io.stdout:write("[ENERGY] " .. text .. "\n")
        io.stdout:flush()
    end

    local function record(name, body)
        if failure then return end
        heartbeat("window " .. name)
        local rec = meter.window(name, body)
        windows[name] = rec
        if rec.status ~= "PASS" then failure = name .. ": " .. tostring(rec.reason) end
    end

    local function idle(name, seconds)
        record(name, function() sleep(seconds) return 0 end)
    end

    local function show_book()
        if adapter.show_book_page and not adapter.library_hides_file_chooser then
            adapter:show_book_page()
        end
    end

    local function paced(count, step)
        for index = 1, count do
            local ok, reason = step(index)
            if not ok then return index - 1, reason end
            if index % 10 == 0 then heartbeat("action " .. index .. "/" .. count) end
            sleep(ctx.pace_s)
        end
        return count
    end

    adapter:ensure_filemanager()
    adapter:goto_page(1)
    ctx.settle(ctx.settle_ticks)
    ctx.emit_ready()

    idle("library_startup_tail", ctx.tail_s)
    idle("library_idle", ctx.idle_s)
    record("library_paging", function()
        local page = 1
        return paced(ctx.turns, function()
            local ok, reason = act(function() return adapter:library_next_page_transition(page, page + 1) end)
            page = page + 1
            return ok, reason
        end)
    end)
    if not failure then
        adapter:goto_page(1)
        ctx.settle(ctx.settle_ticks)
    end
    record("book_cycles", function()
        return paced(ctx.cycles, function()
            ctx.select_next_book()
            show_book()
            local ok, reason = act(function() return adapter:open_book() end)
            if not ok then return false, reason end
            sleep(ctx.pace_s)
            return act(function() return adapter:close_book() end)
        end)
    end)
    record("library_navigation", function()
        return paced(ctx.nav_cycles, function()
            ctx.select_next_folder()
            local ok, reason = act(function() return adapter:library_folder_enter() end)
            if not ok then return false, reason end
            sleep(ctx.pace_s)
            return act(function() return adapter:library_folder_back() end)
        end)
    end)
    if not failure then
        if not ctx.select_reader_book() then
            failure = "reader book is not available"
        else
            show_book()
            local ok, reason = act(function() return adapter:open_book() end)
            if not ok then failure = "open reader book: " .. tostring(reason) end
        end
    end
    idle("reader_open_tail", ctx.tail_s)
    idle("reader_idle", ctx.idle_s)
    -- Two lengths in one document: the cost per page should not grow with the
    -- count, and the tail after the long run shows what keeps working once it stops.
    local function turn() return act(function() return adapter:reader_page_turn() end) end
    record("reader_turns_short", function() return paced(ctx.reader_short_turns, turn) end)
    record("reader_turns_long", function() return paced(ctx.reader_long_turns, turn) end)
    idle("reader_after_turns_tail", ctx.tail_s)
    if not failure then
        local ok, reason = act(function() return adapter:close_book() end)
        if not ok then failure = "close reader book: " .. tostring(reason) end
    end
    idle("library_after_close_tail", ctx.tail_s)

    return windows, failure
end

return Energy
