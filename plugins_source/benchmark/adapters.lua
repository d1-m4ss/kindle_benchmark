-- adapters.lua — backend-specific navigation with deferred semantic verification.
local UIManager = require("ui/uimanager")
local Dispatcher = require("dispatcher")
local ffiUtil = require("ffi/util")

local Adapters = {}

local function strict_paging_profile()
    local profile = os.getenv("BENCHMARK_PROFILE")
    return profile == "paging" or profile == "smoke_validation" or profile == "real"
end

local function top_widget()
    local stack = UIManager._window_stack
    if not stack or #stack == 0 then return nil end
    return stack[#stack].widget or stack[#stack]
end

local function is_shown(widget)
    return widget ~= nil and UIManager:isWidgetShown(widget)
end

local function widget_label(w)
    if type(w) ~= "table" then return tostring(w) end
    return tostring(w.name or w.id or (w.modal and "modal") or "unnamed")
end

-- A page turn under a full-screen overlay changes the widget's page and fires a
-- refresh while the screen shows something else entirely: a fresh ZenOS profile
-- opened its quickstart wizard over the library and every semantic guard still
-- passed.
--
-- Window-stack topology cannot decide this on its own. SimpleUI renders its
-- library through a full-screen container that sits ABOVE the FileManager, so
-- "a full-screen window above the measured widget" describes a healthy stack
-- just as well as an occluding wizard. Verified from probe screenshots: the
-- SimpleUI library is fully visible in exactly that arrangement.
--
-- So this reports, and never judges. Every measured transition carries the
-- window stack above the measured widget into the raw output, and the visual
-- proof comes from the mandatory probe screenshots instead.
local FULLSCREEN_AREA_RATIO = 0.9

local function occlusion_report(widget)
    local report = { top_widget = nil, windows_above = 0, windows_above_names = {},
                     measured_widget_on_stack = nil,
                     fullscreen_above = nil, fullscreen_coverage_pct = nil }
    local stack = UIManager._window_stack
    if not stack or #stack == 0 then return report end
    report.top_widget = widget_label(stack[#stack].widget or stack[#stack])
    if widget == nil then return report end

    local index
    for i = 1, #stack do
        local w = stack[i].widget or stack[i]
        if w == widget then index = i break end
    end
    if not index then
        report.measured_widget_on_stack = false
        return report
    end
    report.measured_widget_on_stack = true
    report.windows_above = #stack - index

    local Screen = require("device").screen
    local screen_area = Screen:getWidth() * Screen:getHeight()
    if screen_area <= 0 then return report end

    for i = index + 1, #stack do
        local w = stack[i].widget or stack[i]
        local dimen = type(w) == "table" and w.dimen or nil
        local painted = type(dimen) == "table" and dimen.w and dimen.h
        local pct = painted and (dimen.w * dimen.h) / screen_area * 100 or nil
        report.windows_above_names[#report.windows_above_names + 1] = string.format(
            "%s@%s", widget_label(w), pct and string.format("%.0f%%", pct) or "unpainted")
        if painted and (dimen.w * dimen.h) >= screen_area * FULLSCREEN_AREA_RATIO then
            report.fullscreen_above = widget_label(w)
            report.fullscreen_coverage_pct = pct
        end
    end
    return report
end

local function realpath(path)
    return path and ffiUtil.realpath(path) or path
end

local function get_menu_page_items(menu)
    if not menu or type(menu.item_table) ~= "table" then return {}, "" end
    local page = tonumber(menu.page) or 1
    local perpage = tonumber(menu.perpage) or #menu.item_table
    if perpage < 1 then perpage = #menu.item_table end
    local first = (page - 1) * perpage + 1
    local last = math.min(#menu.item_table, first + perpage - 1)
    local items = {}
    local parts = {}
    if first <= #menu.item_table then
        for i = first, last do
            local item = menu.item_table[i]
            local val = type(item) == "table" and (item.file or item.path or item.text or item.name or tostring(i)) or tostring(item)
            items[#items + 1] = val
            parts[#parts + 1] = val
        end
    end
    return items, table.concat(parts, "\31")
end

local function visible_signature(menu)
    local _, sig = get_menu_page_items(menu)
    return sig ~= "" and sig or nil
end

local BaseAdapter = {}
BaseAdapter.__index = BaseAdapter

function BaseAdapter:new(library_dir, sample_book, sample_folder)
    return setmetatable({
        library_dir = realpath(library_dir),
        sample_book = realpath(sample_book),
        sample_folder = realpath(sample_folder),
    }, self)
end

function BaseAdapter:set_sample_book(path)
    self.sample_book = realpath(path)
end

function BaseAdapter:set_sample_folder(path)
    self.sample_folder = realpath(path)
end

-- Effective library root for the paging harness. Hierarchical datasets keep
-- zero books at self.library_dir (only category subfolders live there), so
-- paging/smoke_validation profiles redirect FileManager and Bookshelf into a
-- deterministic leaf folder instead of paginating an empty root listing.
function BaseAdapter:set_paging_root(path)
    self.paging_root = realpath(path)
end

function BaseAdapter:unsupported(reason)
    return { success = false, unsupported = true, reason = reason or "Unsupported by this UI backend" }
end

function BaseAdapter:ok(details)
    local out = { success = true }
    for k, v in pairs(details or {}) do out[k] = v end
    return out
end

function BaseAdapter:fail(reason)
    return { success = false, unsupported = false, reason = reason or "Semantic postcondition failed" }
end

function BaseAdapter:deferred(verify, settle_ticks)
    return { pending = true, verify = verify, settle_ticks = settle_ticks }
end

function BaseAdapter:filemanager()
    local FM = require("apps/filemanager/filemanager")
    return FM, FM.instance, FM.instance and FM.instance.file_chooser
end

function BaseAdapter:startup_ready()
    local _, instance, chooser = self:filemanager()
    if instance and chooser and is_shown(instance)
            and type(chooser.item_table) == "table" and #chooser.item_table > 0 then
        return self:ok({ startup_widget = "filemanager", visible_signature = visible_signature(chooser) })
    end
    if instance and chooser and is_shown(instance) then
        return self:ok({ startup_widget = "filemanager_off_top", visible_signature = visible_signature(chooser) })
    end
    local top = top_widget()
    if top and is_shown(top) then
        return self:ok({ startup_widget = "fallback_top", visible_signature = visible_signature(chooser) })
    end
    return self:fail(string.format("Startup FileManager is not visible with usable items: fm=%s fm_shown=%s top=%s stack=%d",
        tostring(instance ~= nil), tostring(is_shown(instance)),
        tostring(top and (top.name or top._zen_navbar_tab_id or top)),
        #(UIManager._window_stack or {})))
end

function BaseAdapter:ensure_filemanager()
    local UIManager = require("ui/uimanager")
    for i = #(UIManager._window_stack or {}), 1, -1 do
        local entry = UIManager._window_stack[i]
        local w = entry and (entry.widget or entry)
        if w and (w.name == "infomessage" or w.is_infomessage or w.timeout) then
            pcall(function() UIManager:close(w) end)
        end
    end
    local root = self.paging_root or self.library_dir
    local settings = rawget(_G, "G_reader_settings")
    if settings and root then
        local hd = settings:readSetting("home_dir")
        if hd ~= root then
            settings:saveSetting("home_dir", root)
            settings:saveSetting("lastdir", root)
            settings:flush()
        end
    end
    local FM = require("apps/filemanager/filemanager")
    if not FM.instance then
        FM:showFiles(root)
    elseif FM.instance.file_chooser and realpath(FM.instance.file_chooser.path) ~= root then
        FM.instance:reinit(root)
    end
    return FM
end

function BaseAdapter:get_page_info()
    return self:unsupported("get_page_info not implemented for base adapter")
end

function BaseAdapter:goto_page(target_page)
    return false
end

function BaseAdapter:library_next_page_transition(from_page, to_page)
    return self:unsupported("library_next_page_transition not implemented for base adapter")
end

function BaseAdapter:library_prev_page_transition(from_page, to_page)
    return self:unsupported("library_prev_page_transition not implemented for base adapter")
end

local StockAdapter = setmetatable({}, { __index = BaseAdapter })
StockAdapter.__index = StockAdapter

function StockAdapter:start_to_home()
    return self:unsupported("Stock KOReader has no standalone Home Screen")
end

function StockAdapter:home_to_library()
    local FM = self:ensure_filemanager()
    if FM.instance then FM.instance:reinit(self.library_dir) end
    return self:deferred(function()
        local _, instance, chooser = self:filemanager()
        if instance and chooser and is_shown(instance) and realpath(chooser.path) == self.library_dir
                and type(chooser.item_table) == "table" and #chooser.item_table > 0 then
            return self:ok({ active_widget = "filemanager", visible_signature = visible_signature(chooser), expected_refresh = true })
        end
        return self:fail("FileManager is not visible at the target library with loaded items")
    end)
end

function StockAdapter:library_first_render()
    local FM = self:ensure_filemanager()
    if FM.instance then FM.instance:reinit(self.library_dir) end
    return self:deferred(function()
        local _, instance, chooser = self:filemanager()
        local sig = visible_signature(chooser)
        local cp = chooser and chooser.path
        local rcp = chooser and realpath(chooser.path)
        if instance and chooser and is_shown(instance) and rcp == self.library_dir
                and sig and sig ~= "" then
            return self:ok({ items_loaded = #chooser.item_table, visible_signature = sig, expected_refresh = true })
        end
        return self:fail(string.format("library_first_render fail: instance=%s chooser=%s shown=%s cp=%s rcp=%s target=%s sig=%s",
            tostring(instance ~= nil), tostring(chooser ~= nil), tostring(is_shown(instance)),
            tostring(cp), tostring(rcp), tostring(self.library_dir), tostring(sig)))
    end)
end

function StockAdapter:get_page_info()
    local _, instance, chooser = self:filemanager()
    if not chooser or type(chooser.item_table) ~= "table" then
        self:ensure_filemanager()
        _, instance, chooser = self:filemanager()
    end
    if not chooser or type(chooser.item_table) ~= "table" then return nil end
    local page = tonumber(chooser.page) or 1
    local total_pages = tonumber(chooser.page_num) or 1
    local items, sig = get_menu_page_items(chooser)
    local perpage = tonumber(chooser.perpage) or #chooser.item_table
    return {
        current_page = page,
        total_pages = total_pages,
        visible_count = #items,
        visible_signature = sig,
        visible_items = items,
        per_page_capacity = perpage,
    }
end

function StockAdapter:goto_page(target_page)
    local _, instance, chooser = self:filemanager()
    if not chooser then
        self:ensure_filemanager()
        _, instance, chooser = self:filemanager()
    end
    if not chooser then return false end
    if chooser.onGotoPage then
        chooser:onGotoPage(target_page)
    elseif chooser.changeToPage then
        chooser:changeToPage(target_page)
    else
        chooser.page = target_page
        if chooser.updateItems then chooser:updateItems(1, true) end
    end
    return true
end

function StockAdapter:library_next_page_transition(from_page, to_page)
    local _, _, chooser = self:filemanager()
    if not chooser then
        self:ensure_filemanager()
        _, _, chooser = self:filemanager()
    end
    if not chooser then return self:fail("FileChooser is unavailable") end
    local info_before = self:get_page_info()
    if not info_before then return self:fail("Failed to get page info before transition") end
    if info_before.current_page ~= from_page then
        return self:fail(string.format("Precondition failed: current page %s != expected %s", tostring(info_before.current_page), tostring(from_page)))
    end
    if to_page ~= from_page + 1 then
        return self:fail(string.format("Invalid sequential transition: to_page %s != from_page + 1", tostring(to_page)))
    end
    if from_page >= info_before.total_pages then
        return self:unsupported("Already at the last page; cannot navigate forward without wrapping")
    end
    if info_before.visible_count == 0 or info_before.visible_signature == "" then
        return self:fail("Precondition failed: empty visible signature or zero items before transition")
    end

    chooser:onNextPage()

    return self:deferred(function()
        local _, instance_after, chooser_after = self:filemanager()
        local info_after = self:get_page_info()
        if not info_after or not instance_after or not is_shown(instance_after) then
            return self:fail("FileManager is not visible after page transition")
        end
        if info_after.current_page ~= to_page then
            return self:fail(string.format("Page number mismatch: got %s, expected %s", tostring(info_after.current_page), tostring(to_page)))
        end
        if info_after.visible_count == 0 or info_after.visible_signature == "" then
            return self:fail("Postcondition failed: page has zero items or empty signature after transition")
        end
        if info_after.visible_signature == info_before.visible_signature then
            return self:fail("Postcondition failed: visible signature did not change across page turn")
        end
        local occlusion = occlusion_report(instance_after)
        return self:ok({
            page_before = info_before.current_page,
            page_after = info_after.current_page,
            visible_count_before = info_before.visible_count,
            visible_count_after = info_after.visible_count,
            visible_signature_before = info_before.visible_signature,
            visible_signature_after = info_after.visible_signature,
            visible_items_before = info_before.visible_items,
            visible_items_after = info_after.visible_items,
            total_pages = info_after.total_pages,
            top_widget = occlusion.top_widget,
            windows_above_measured = occlusion.windows_above,
            windows_above_names = occlusion.windows_above_names,
            measured_widget_on_stack = occlusion.measured_widget_on_stack,
            fullscreen_above = occlusion.fullscreen_above,
            expected_refresh = true,
        })
    end)
end

function StockAdapter:library_prev_page_transition(from_page, to_page)
    local _, _, chooser = self:filemanager()
    if not chooser then
        self:ensure_filemanager()
        _, _, chooser = self:filemanager()
    end
    if not chooser then return self:fail("FileChooser is unavailable") end
    local info_before = self:get_page_info()
    if not info_before then return self:fail("Failed to get page info before transition") end
    if info_before.current_page ~= from_page then
        return self:fail(string.format("Precondition failed: current page %s != expected %s", tostring(info_before.current_page), tostring(from_page)))
    end
    if to_page ~= from_page - 1 then
        return self:fail(string.format("Invalid backward transition: to_page %s != from_page - 1", tostring(to_page)))
    end
    if from_page <= 1 then
        return self:unsupported("Already at page 1; cannot navigate backward without wrapping")
    end
    if info_before.visible_count == 0 or info_before.visible_signature == "" then
        return self:fail("Precondition failed: empty visible signature or zero items before transition")
    end

    chooser:onPrevPage()

    return self:deferred(function()
        local _, instance_after, chooser_after = self:filemanager()
        local info_after = self:get_page_info()
        if not info_after or not instance_after or not is_shown(instance_after) then
            return self:fail("FileManager is not visible after page transition")
        end
        if info_after.current_page ~= to_page then
            return self:fail(string.format("Page number mismatch: got %s, expected %s", tostring(info_after.current_page), tostring(to_page)))
        end
        if info_after.visible_count == 0 or info_after.visible_signature == "" then
            return self:fail("Postcondition failed: page has zero items or empty signature after transition")
        end
        if info_after.visible_signature == info_before.visible_signature then
            return self:fail("Postcondition failed: visible signature did not change across page turn")
        end
        local occlusion = occlusion_report(instance_after)
        return self:ok({
            page_before = info_before.current_page,
            page_after = info_after.current_page,
            visible_count_before = info_before.visible_count,
            visible_count_after = info_after.visible_count,
            visible_signature_before = info_before.visible_signature,
            visible_signature_after = info_after.visible_signature,
            visible_items_before = info_before.visible_items,
            visible_items_after = info_after.visible_items,
            total_pages = info_after.total_pages,
            top_widget = occlusion.top_widget,
            windows_above_measured = occlusion.windows_above,
            windows_above_names = occlusion.windows_above_names,
            measured_widget_on_stack = occlusion.measured_widget_on_stack,
            fullscreen_above = occlusion.fullscreen_above,
            expected_refresh = true,
        })
    end)
end

function StockAdapter:library_folder_enter()
    if not self.sample_folder then return self:unsupported("No deterministic subfolder exists") end
    self:ensure_filemanager()
    local _, _, chooser = self:filemanager()
    if not chooser then return self:fail("FileChooser is unavailable") end
    chooser:changeToPath(self.sample_folder)
    return self:deferred(function()
        local _, instance_after, chooser_after = self:filemanager()
        if instance_after and is_shown(instance_after) and chooser_after
                and realpath(chooser_after.path) == self.sample_folder
                and type(chooser_after.item_table) == "table" then
            return self:ok({ path = self.sample_folder, visible_signature = visible_signature(chooser_after), expected_refresh = true })
        end
        return self:fail("Folder-enter path/items postcondition failed")
    end)
end

function StockAdapter:library_folder_back()
    self:ensure_filemanager()
    local _, _, chooser = self:filemanager()
    if not chooser then return self:fail("FileChooser is unavailable") end
    chooser:changeToPath(self.library_dir)
    return self:deferred(function()
        local _, instance_after, chooser_after = self:filemanager()
        if instance_after and is_shown(instance_after) and chooser_after
                and realpath(chooser_after.path) == self.library_dir then
            return self:ok({ path = self.library_dir, visible_signature = visible_signature(chooser_after), expected_refresh = true })
        end
        return self:fail("Folder-back did not restore the root library")
    end)
end

function StockAdapter:change_sort_mode()
    self:ensure_filemanager()
    local _, instance, chooser = self:filemanager()
    local settings = rawget(_G, "G_reader_settings")
    if not chooser or not settings or not instance then return self:unsupported("Sort settings are unavailable") end
    local before_mode = settings:readSetting("collate", "strcoll")
    local before_rev = settings:isTrue("reverse_sorting")
    local before_sig = visible_signature(chooser)
    local after_mode = before_mode == "size" and "strcoll" or "size"
    local after_rev = not before_rev
    instance:onSetSortBy(after_mode)
    instance:onSetReverseSorting(after_rev)
    return self:deferred(function()
        local _, instance_after, chooser_after = self:filemanager()
        local saved_mode = settings:readSetting("collate", "strcoll")
        local after_sig = visible_signature(chooser_after)
        local has_files = before_sig and string.find(before_sig, "%.epub")
        if instance_after and is_shown(instance_after) and saved_mode == after_mode
                and (before_sig ~= after_sig or not has_files or #((chooser_after and chooser_after.item_table) or {}) <= 1) then
            return self:ok({ sort_before = before_mode, sort_after = after_mode, expected_refresh = true })
        end
        return self:fail(string.format("change_sort_mode fail: saved=%s expected=%s before_sig=%s after_sig=%s",
            tostring(saved_mode), tostring(after_mode), tostring(before_sig), tostring(after_sig)))
    end)
end

function StockAdapter:open_book()
    if not self.sample_book then return self:unsupported("Deterministic target book is missing") end
    local ReaderUI = require("apps/reader/readerui")
    ReaderUI:showReader(self.sample_book)
    return self:deferred(function()
        local reader = ReaderUI.instance
        if reader and is_shown(reader) and reader.document
                and realpath(reader.document.file) == self.sample_book
                and reader.view then
            return self:ok({ book = self.sample_book, expected_refresh = true })
        end
        return self:fail("Target ReaderUI/document/rendered view is not active on the window stack")
    end)
end

function StockAdapter:close_book()
    local ReaderUI = require("apps/reader/readerui")
    if not ReaderUI.instance or not is_shown(ReaderUI.instance) then
        return self:fail("No active ReaderUI for close_book")
    end
    ReaderUI.instance:onHome()
    return self:deferred(function()
        local FM = require("apps/filemanager/filemanager")
        local is_closed = ReaderUI.instance == nil
        local has_fm = FM.instance ~= nil
        local fm_shown = is_shown(FM.instance)
        local top = top_widget()
        if is_closed and (fm_shown or (top and is_shown(top))) then
            return self:ok({ restored_widget = (top and top.name) or "filemanager", expected_refresh = true })
        end
        return self:fail(string.format("close_book fail: is_closed=%s has_fm=%s fm_shown=%s stack_len=%d",
            tostring(is_closed), tostring(has_fm), tostring(fm_shown), #(UIManager._window_stack or {})))
    end)
end

function StockAdapter:reader_page_turn()
    local ReaderUI = require("apps/reader/readerui")
    local reader = ReaderUI.instance
    if not reader or not reader.document then return self:fail("ReaderUI is not active") end
    local before = reader.view and reader.view.state and reader.view.state.page
    local navigator = reader.paging or reader.rolling
    if navigator and navigator.onGotoViewRel then
        navigator:onGotoViewRel(1)
    else
        return self:unsupported("Relative reader page turn is unavailable")
    end
    return self:deferred(function()
        local active = ReaderUI.instance
        local after = active and active.view and active.view.state and active.view.state.page
        if active == reader and is_shown(active) and before ~= nil and after ~= nil and after ~= before then
            return self:ok({ page_before = before, page_after = after, expected_refresh = true })
        end
        return self:fail("Reader page number did not change after page turn")
    end)
end

function StockAdapter:open_quick_settings()
    self:ensure_filemanager()
    local FM = require("apps/filemanager/filemanager")
    if not FM.instance or not FM.instance.menu then return self:unsupported("FileManager menu is unavailable") end
    FM.instance.menu:onShowMenu()
    return self:deferred(function()
        local container = FM.instance and FM.instance.menu and FM.instance.menu.menu_container
        if container and is_shown(container) and top_widget() == container then
            return self:ok({ expected_refresh = true })
        end
        return self:fail("Quick-settings menu is not the top visible widget")
    end)
end

function StockAdapter:close_quick_settings()
    local FM = require("apps/filemanager/filemanager")
    local container = FM.instance and FM.instance.menu and FM.instance.menu.menu_container
    if not container then return self:fail("No quick-settings menu to close") end
    FM.instance.menu:onCloseFileManagerMenu()
    return self:deferred(function()
        if not is_shown(container) and FM.instance and is_shown(FM.instance) then
            return self:ok({ expected_refresh = true })
        end
        return self:fail("Quick-settings menu did not close back to FileManager")
    end)
end

local function get_live_bookshelf()
    local top = top_widget()
    if top and (top.name == "bookshelf" or (top._widget and top._widget.name == "bookshelf")) then
        return top.name == "bookshelf" and top or top._widget
    end
    local stack = UIManager._window_stack or {}
    for i = #stack, 1, -1 do
        local w = stack[i] and (stack[i].widget or stack[i])
        if w and w.name == "bookshelf" and is_shown(w) then
            return w
        end
    end
    return nil
end

function BaseAdapter:get_bookshelf_page_info()
    local widget = get_live_bookshelf()
    if not widget or not is_shown(widget) then return nil end
    local page = tonumber(widget.page) or 1
    local total_pages = tonumber(widget._total_pages) or 1
    local items = {}
    local parts = {}
    if type(widget._page_items) == "table" then
        for _, item in ipairs(widget._page_items) do
            if item then
                local val = type(item) == "table" and (item.filepath or item.file or item.title or item.text or item.name) or tostring(item)
                items[#items + 1] = val
                parts[#parts + 1] = val
            end
        end
    end
    local sig = #parts > 0 and table.concat(parts, "\31") or ""
    return {
        current_page = page,
        total_pages = total_pages,
        visible_count = #items,
        visible_signature = sig,
        visible_items = items,
        per_page_capacity = widget._viewSize and widget:_viewSize() or #items,
    }
end

function BaseAdapter:goto_bookshelf_page(target_page)
    local widget = get_live_bookshelf()
    if not widget or not is_shown(widget) then return false end
    if target_page == 1 then
        widget._cursor = 1
        if widget._syncPageFromCursor then widget:_syncPageFromCursor() end
        if widget._swapShelvesInPlace then widget:_swapShelvesInPlace() end
        return true
    end
    local view_sz = (widget._viewSize and widget:_viewSize()) or 8
    widget._cursor = (target_page - 1) * view_sz + 1
    if widget._syncPageFromCursor then widget:_syncPageFromCursor() end
    if widget._swapShelvesInPlace then widget:_swapShelvesInPlace() end
    return true
end

function BaseAdapter:set_bookshelf_animation(mode)
    local ok, BookshelfSettings = pcall(require, "lib/bookshelf_settings_store")
    if ok and BookshelfSettings and BookshelfSettings.save then
        BookshelfSettings.save("shelf_page_animation", mode or "medium")
        if BookshelfSettings.flush then BookshelfSettings.flush() end
        local readback = BookshelfSettings.read and BookshelfSettings.read("shelf_page_animation")
        return readback == (mode or "medium")
    end
    return false
end

function BaseAdapter:open_bookshelf()
    local root = self.paging_root or self.library_dir
    local settings = rawget(_G, "G_reader_settings")
    if settings and root then
        local hd = settings:readSetting("home_dir")
        if not hd or hd == "" or hd == "/" then
            settings:saveSetting("home_dir", root)
            settings:saveSetting("lastdir", root)
            settings:flush()
        end
    end
    local existing = get_live_bookshelf()
    if existing and is_shown(existing) and top_widget() == existing then
        return self:fail("Bookshelf was already open on top before open_bookshelf")
    end
    local pl = package.loaded["pluginloader"]
    local bs_plugin = pl and pl.loaded_plugins and pl.loaded_plugins["bookshelf"]
    if bs_plugin then
        if bs_plugin._widget and not UIManager:isWidgetShown(bs_plugin._widget) then
            bs_plugin._widget = nil
        end
        if bs_plugin.show then
            bs_plugin:show()
        else
            Dispatcher:execute({ toggle_bookshelf = true })
        end
    else
        Dispatcher:execute({ toggle_bookshelf = true })
    end
    return self:deferred(function()
        local widget = get_live_bookshelf()
        if not widget or not is_shown(widget) then
            return self:fail("Bookshelf widget is not visible after open_bookshelf")
        end
        -- Ensure Bookshelf displays the populated corpus on chip "all" (Home tab)
        if widget.chip ~= "all" and widget._selectChip then
            widget:_selectChip("all")
        end
        local info = self:get_bookshelf_page_info()
        if not info or info.visible_count == 0 or info.visible_signature == "" then
            return self:fail(string.format("Bookshelf opened to an empty shelf or missing visible items: chip=%s items=%s total_pages=%s",
                tostring(widget.chip), tostring(info and info.visible_count), tostring(info and info.total_pages)))
        end
        if strict_paging_profile() and info.total_pages < 2 then
            return self:fail(string.format("Bookshelf shelf has only %d page(s), expected >= 2 for paging benchmark", info.total_pages))
        end
        return self:ok({
            screen = "bookshelf",
            chip = widget.chip,
            visible_count = info.visible_count,
            total_pages = info.total_pages,
            visible_signature = info.visible_signature,
            expected_refresh = true,
        })
    end)
end

function BaseAdapter:bookshelf_first_render()
    local widget = get_live_bookshelf()
    if not widget or not is_shown(widget) then
        return self:fail("Bookshelf widget is not open for bookshelf_first_render")
    end
    if widget._rebuild then
        widget:_rebuild()
    end
    UIManager:setDirty(widget, "ui")
    return self:deferred(function()
        local after = get_live_bookshelf()
        local info = self:get_bookshelf_page_info()
        if after and is_shown(after) and info and info.visible_count > 0 then
            return self:ok({
                screen = "bookshelf_render",
                visible_count = info.visible_count,
                total_pages = info.total_pages,
                visible_signature = info.visible_signature,
                expected_refresh = true,
            })
        end
        return self:fail("Bookshelf widget failed to render or has zero items")
    end)
end

function BaseAdapter:bookshelf_next_page_transition(from_page, to_page)
    local widget = get_live_bookshelf()
    if not widget or not is_shown(widget) then return self:fail("Bookshelf widget is not open") end
    local info_before = self:get_bookshelf_page_info()
    if not info_before then return self:fail("Failed to get Bookshelf page info before transition") end
    if info_before.current_page ~= from_page then
        return self:fail(string.format("Precondition failed: current Bookshelf page %s != expected %s", tostring(info_before.current_page), tostring(from_page)))
    end
    if to_page ~= from_page + 1 then
        return self:fail(string.format("Invalid sequential transition: to_page %s != from_page + 1", tostring(to_page)))
    end
    if from_page >= info_before.total_pages then
        return self:unsupported("Already at the last Bookshelf page; cannot navigate forward without wrapping")
    end
    if info_before.visible_count == 0 or info_before.visible_signature == "" then
        return self:fail("Precondition failed: empty visible signature or zero items before Bookshelf transition")
    end

    if widget.onNextPage then
        widget:onNextPage()
    elseif widget._paginateNext then
        widget:_paginateNext()
    else
        return self:fail("Bookshelf pagination method missing")
    end

    return self:deferred(function()
        local after = get_live_bookshelf()
        local info_after = self:get_bookshelf_page_info()
        if not after or not is_shown(after) or not info_after then
            return self:fail("Bookshelf widget is not visible after page transition")
        end
        if info_after.current_page ~= to_page then
            return self:fail(string.format("Bookshelf page mismatch: got %s, expected %s", tostring(info_after.current_page), tostring(to_page)))
        end
        if info_after.visible_count == 0 or info_after.visible_signature == "" then
            return self:fail("Postcondition failed: Bookshelf has zero items or empty signature after transition")
        end
        if info_after.visible_signature == info_before.visible_signature then
            return self:fail("Postcondition failed: Bookshelf visible signature did not change across page turn")
        end
        local occlusion = occlusion_report(after)
        return self:ok({
            page_before = info_before.current_page,
            page_after = info_after.current_page,
            visible_count_before = info_before.visible_count,
            visible_count_after = info_after.visible_count,
            visible_signature_before = info_before.visible_signature,
            visible_signature_after = info_after.visible_signature,
            visible_items_before = info_before.visible_items,
            visible_items_after = info_after.visible_items,
            total_pages = info_after.total_pages,
            top_widget = occlusion.top_widget,
            windows_above_measured = occlusion.windows_above,
            windows_above_names = occlusion.windows_above_names,
            measured_widget_on_stack = occlusion.measured_widget_on_stack,
            fullscreen_above = occlusion.fullscreen_above,
            expected_refresh = true,
        })
    end)
end

function BaseAdapter:bookshelf_prev_page_transition(from_page, to_page)
    local widget = get_live_bookshelf()
    if not widget or not is_shown(widget) then return self:fail("Bookshelf widget is not open") end
    local info_before = self:get_bookshelf_page_info()
    if not info_before then return self:fail("Failed to get Bookshelf page info before transition") end
    if info_before.current_page ~= from_page then
        return self:fail(string.format("Precondition failed: current Bookshelf page %s != expected %s", tostring(info_before.current_page), tostring(from_page)))
    end
    if to_page ~= from_page - 1 then
        return self:fail(string.format("Invalid backward transition: to_page %s != from_page - 1", tostring(to_page)))
    end
    if from_page <= 1 then
        return self:unsupported("Already at page 1; cannot navigate backward without wrapping")
    end
    if info_before.visible_count == 0 or info_before.visible_signature == "" then
        return self:fail("Precondition failed: empty visible signature or zero items before Bookshelf transition")
    end

    if widget.onPrevPage then
        widget:onPrevPage()
    elseif widget._paginatePrev then
        widget:_paginatePrev()
    else
        return self:fail("Bookshelf pagination method missing")
    end

    return self:deferred(function()
        local after = get_live_bookshelf()
        local info_after = self:get_bookshelf_page_info()
        if not after or not is_shown(after) or not info_after then
            return self:fail("Bookshelf widget is not visible after page transition")
        end
        if info_after.current_page ~= to_page then
            return self:fail(string.format("Bookshelf page mismatch: got %s, expected %s", tostring(info_after.current_page), tostring(to_page)))
        end
        if info_after.visible_count == 0 or info_after.visible_signature == "" then
            return self:fail("Postcondition failed: Bookshelf has zero items or empty signature after transition")
        end
        if info_after.visible_signature == info_before.visible_signature then
            return self:fail("Postcondition failed: Bookshelf visible signature did not change across page turn")
        end
        local occlusion = occlusion_report(after)
        return self:ok({
            page_before = info_before.current_page,
            page_after = info_after.current_page,
            visible_count_before = info_before.visible_count,
            visible_count_after = info_after.visible_count,
            visible_signature_before = info_before.visible_signature,
            visible_signature_after = info_after.visible_signature,
            visible_items_before = info_before.visible_items,
            visible_items_after = info_after.visible_items,
            total_pages = info_after.total_pages,
            top_widget = occlusion.top_widget,
            windows_above_measured = occlusion.windows_above,
            windows_above_names = occlusion.windows_above_names,
            measured_widget_on_stack = occlusion.measured_widget_on_stack,
            fullscreen_above = occlusion.fullscreen_above,
            expected_refresh = true,
        })
    end)
end

function BaseAdapter:close_bookshelf()
    local widget = get_live_bookshelf()
    if not widget or not is_shown(widget) then
        return self:ok({ screen = "already_closed" })
    end
    local pl = package.loaded["pluginloader"]
    local bs_plugin = pl and pl.loaded_plugins and pl.loaded_plugins["bookshelf"]
    if bs_plugin then
        bs_plugin._widget = nil
    end
    if widget.onClose then
        widget:onClose()
    elseif widget.onCloseWidget then
        widget:onCloseWidget()
        UIManager:close(widget)
    else
        Dispatcher:execute({ toggle_bookshelf = true })
    end
    return self:deferred(function()
        local after = get_live_bookshelf()
        local top = top_widget()
        if (not after or not is_shown(after)) and top ~= widget then
            return self:ok({ screen = "shell" })
        end
        return self:fail("Bookshelf widget was not dismissed on close_bookshelf")
    end)
end

local SimpleUIAdapter = setmetatable({}, { __index = StockAdapter })
SimpleUIAdapter.__index = SimpleUIAdapter

local function get_sui_home()
    local ok, engine = pcall(require, "engines/sui_screen_engine")
    return ok and engine and engine.getInstance and engine.getInstance("hs") or nil
end

function SimpleUIAdapter:startup_ready()
    local home = get_sui_home()
    if home and is_shown(home) then
        return self:ok({ startup_widget = "simpleui_homescreen" })
    end
    local _, instance, chooser = self:filemanager()
    if instance and is_shown(instance) and top_widget() == instance
            and chooser and type(chooser.item_table) == "table" and #chooser.item_table > 0 then
        return self:ok({ startup_widget = "simpleui_filemanager", visible_signature = visible_signature(chooser) })
    end
    local top = top_widget()
    if top and is_shown(top) then
        return self:ok({ startup_widget = "fallback_top", visible_signature = visible_signature(chooser) })
    end
    return self:fail(string.format("SimpleUI startup UI is not usable on top: home=%s shown_home=%s fm=%s fm_shown=%s top=%s stack=%d",
        tostring(home ~= nil), tostring(is_shown(home)),
        tostring(instance ~= nil), tostring(is_shown(instance)),
        tostring(top and (top.name or top._zen_navbar_tab_id or top)),
        #(UIManager._window_stack or {})))
end

function SimpleUIAdapter:start_to_home()
    local home = get_sui_home()
    local top = top_widget()
    if home and is_shown(home) and top == home then
        return self:fail("Already at SimpleUI homescreen before start_to_home")
    end
    Dispatcher:execute({ simpleui_go_homescreen = true })
    return self:deferred(function()
        local home_after = get_sui_home()
        local top_after = top_widget()
        if home_after and is_shown(home_after) and (top_after == home_after or is_shown(home_after)) then
            return self:ok({ screen = "simpleui_homescreen" })
        end
        local stack_labels = {}
        for _, entry in ipairs(UIManager._window_stack or {}) do
            stack_labels[#stack_labels + 1] = widget_label(entry.widget or entry)
        end
        return self:fail(string.format(
            "SimpleUI homescreen instance is not visible on top: home=%s shown=%s top=%s home_is_top=%s stack=%s",
            tostring(home_after ~= nil), tostring(is_shown(home_after)),
            widget_label(top_after), tostring(top_after == home_after),
            table.concat(stack_labels, ">")))
    end)
end

function SimpleUIAdapter:home_to_library()
    -- Match ensure_filemanager(): close transient notices before the measured
    -- tab transition.  A lingering InfoMessage/timeout widget can remain on
    -- top of the FileManager after startup and block the next homescreen
    -- transition even though the library itself is healthy.
    for i = #(UIManager._window_stack or {}), 1, -1 do
        local entry = UIManager._window_stack[i]
        local w = entry and (entry.widget or entry)
        if w and (w.name == "infomessage" or w.is_infomessage or w.timeout) then
            pcall(function() UIManager:close(w) end)
        end
    end
    local _, instance_before = self:filemanager()
    local top = top_widget()
    if instance_before and is_shown(instance_before) and top == instance_before then
        return self:fail("Already at SimpleUI library before home_to_library")
    end
    local ok_core, UI_core = pcall(require, "infra/sui_core")
    if ok_core and UI_core and UI_core.getOpenScreen then
        local _, hs_inst = UI_core.getOpenScreen()
        if hs_inst then
            -- This is an intentional tab transition.  Without the flag,
            -- SimpleUI's UIManager.close hook schedules its automatic
            -- Homescreen restore, which can race the following
            -- simpleui_go_library action and leave the next start_to_home
            -- transition without a valid Homescreen state.
            hs_inst._navbar_closing_intentionally = true
            UIManager:close(hs_inst)
            hs_inst._navbar_closing_intentionally = nil
        end
    end
    Dispatcher:execute({ simpleui_go_library = true })
    return self:deferred(function()
        local _, instance_after, chooser = self:filemanager()
        if instance_after and is_shown(instance_after) and chooser
                and type(chooser.item_table) == "table" and #chooser.item_table > 0 then
            return self:ok({ active_widget = "simpleui_filemanager", visible_signature = visible_signature(chooser) })
        end
        return self:fail("SimpleUI library/FileManager is not visible with loaded items")
    end)
end

function SimpleUIAdapter:ensure_filemanager()
    local ok_st, SUISettings = pcall(require, "infra/sui_store")
    if ok_st and SUISettings then
        SUISettings:set("simpleui_onboarding_done", true)
    end
    local root = self.paging_root or self.library_dir
    local settings = rawget(_G, "G_reader_settings")
    if settings and root then
        local hd = settings:readSetting("home_dir")
        if hd ~= root then
            settings:saveSetting("home_dir", root)
            settings:saveSetting("lastdir", root)
            settings:flush()
        end
    end
    local ok_core, UI_core = pcall(require, "infra/sui_core")
    if ok_core and UI_core and UI_core.getOpenScreen then
        local _, hs_inst = UI_core.getOpenScreen()
        if hs_inst then
            UIManager:close(hs_inst)
        end
    end
    Dispatcher:execute({ simpleui_go_library = true })
    local FM = require("apps/filemanager/filemanager")
    if not FM.instance then
        FM:showFiles(root)
    elseif FM.instance.file_chooser and realpath(FM.instance.file_chooser.path) ~= root then
        FM.instance:reinit(root)
    end
    return FM
end

local ZenOSAdapter = setmetatable({}, { __index = StockAdapter })
ZenOSAdapter.__index = ZenOSAdapter

function ZenOSAdapter:ensure_filemanager()
    local root = self.paging_root or self.library_dir
    local settings = rawget(_G, "G_reader_settings")
    if settings and root then
        local hd = settings:readSetting("home_dir")
        if hd ~= root then
            settings:saveSetting("home_dir", root)
            settings:saveSetting("lastdir", root)
            settings:flush()
        end
    end
    local open_tab = rawget(_G, "__ZEN_UI_NAVBAR_OPEN_TAB")
    if type(open_tab) == "function" then
        open_tab("books")
    else
        Dispatcher:execute({ zen_ui_show_library = true })
    end
    local FM = require("apps/filemanager/filemanager")
    if not FM.instance then
        FM:showFiles(root)
    elseif FM.instance.file_chooser and realpath(FM.instance.file_chooser.path) ~= root then
        FM.instance:reinit(root)
    end
    return FM
end

local function get_zen_home()
    local ok, shared = pcall(require, "common/shared_state")
    local plugin = rawget(_G, "__ZEN_UI_PLUGIN")
    if not plugin then
        local pl = package.loaded["pluginloader"]
        if pl and pl.loaded_plugins then
            plugin = pl.loaded_plugins["zenos"] or pl.loaded_plugins["zen_ui"]
        end
    end
    return ok and shared and plugin and shared.get(plugin, "home") or nil
end

function ZenOSAdapter:startup_ready()
    local home = get_zen_home()
    if home and type(home.isActiveOnTop) == "function" and home.isActiveOnTop() then
        return self:ok({ startup_widget = "zen_home" })
    end
    local FM, instance, chooser = self:filemanager()
    if instance and is_shown(instance) and chooser then
        return self:ok({ startup_widget = "zen_filemanager", visible_signature = visible_signature(chooser) })
    end
    return self:fail("ZenOS startup UI is not active on top")
end

function ZenOSAdapter:start_to_home()
    local home = get_zen_home()
    if home and type(home.isActiveOnTop) == "function" and home.isActiveOnTop() then
        return self:fail("Already at ZenOS home before start_to_home")
    end
    local open_tab = rawget(_G, "__ZEN_UI_NAVBAR_OPEN_TAB")
    if type(open_tab) == "function" then
        open_tab("home")
    else
        Dispatcher:execute({ zen_ui_show_home = true })
    end
    return self:deferred(function()
        local home_after = get_zen_home()
        if home_after and type(home_after.isActiveOnTop) == "function" and home_after.isActiveOnTop() then
            return self:ok({ screen = "zen_home", expected_refresh = true })
        end
        if home_after and type(home_after.hasActive) == "function" and home_after.hasActive() then
            return self:ok({ screen = "zen_home", expected_refresh = true })
        end
        local stack = UIManager._window_stack or {}
        for i = #stack, 1, -1 do
            local w = stack[i] and stack[i].widget
            if w and (w.name == "home" or w._zen_navbar_tab_id == "home") then
                return self:ok({ screen = "zen_home", expected_refresh = true })
            end
        end
        local top = top_widget()
        return self:fail(string.format(
            "ZenOS home is not active on top: home=%s top=%s stack_len=%d",
            tostring(home_after ~= nil),
            tostring(top and (top.name or top._zen_navbar_tab_id or top)),
            #stack))
    end)
end

function ZenOSAdapter:home_to_library()
    local _, instance_before = self:filemanager()
    local top = top_widget()
    if instance_before and is_shown(instance_before) and top == instance_before then
        return self:fail("Already at ZenOS library before home_to_library")
    end
    local open_tab = rawget(_G, "__ZEN_UI_NAVBAR_OPEN_TAB")
    if type(open_tab) == "function" then
        open_tab("books")
    else
        Dispatcher:execute({ zen_ui_show_library = true })
    end
    local _, instance = self:filemanager()
    if instance then instance:reinit(self.library_dir) end
    return self:deferred(function()
        local _, instance_after, chooser = self:filemanager()
        if instance_after and is_shown(instance_after) and chooser
                and realpath(chooser.path) == self.library_dir
                and type(chooser.item_table) == "table" and #chooser.item_table > 0 then
            return self:ok({ screen = "zen_library", path = self.library_dir,
                visible_signature = visible_signature(chooser), expected_refresh = true })
        end
        return self:fail("ZenOS library did not expose the visible populated benchmark corpus")
    end)
end

local BookshelfAdapter = setmetatable({}, { __index = StockAdapter })
BookshelfAdapter.__index = BookshelfAdapter

function BookshelfAdapter:startup_ready()
    local widget = get_live_bookshelf()
    if widget and is_shown(widget) then
        return self:ok({ startup_widget = "bookshelf" })
    end
    local _, instance, chooser = self:filemanager()
    if instance and chooser and is_shown(instance)
            and chooser and type(chooser.item_table) == "table" and #chooser.item_table > 0 then
        return self:ok({ startup_widget = "bookshelf_filemanager", visible_signature = visible_signature(chooser) })
    end
    if instance and is_shown(instance) then
        return self:ok({ startup_widget = "bookshelf_filemanager_off_top", visible_signature = visible_signature(chooser) })
    end
    local top = top_widget()
    if top and is_shown(top) then
        return self:ok({ startup_widget = "bookshelf_fallback_top", visible_signature = visible_signature(chooser) })
    end
    return self:fail(string.format("Bookshelf startup UI is not usable on top: widget=%s fm=%s fm_shown=%s top=%s stack=%d",
        tostring(widget and widget.name), tostring(instance ~= nil), tostring(is_shown(instance)),
        tostring(top and (top.name or top._zen_navbar_tab_id or top)), #(UIManager._window_stack or {})))
end

function BookshelfAdapter:start_to_home()
    return self:unsupported("Bookshelf on Stock has no standalone Home Screen")
end

function BookshelfAdapter:home_to_library()
    return StockAdapter.home_to_library(self)
end

local ProjectTitleAdapter = setmetatable({}, { __index = StockAdapter })
ProjectTitleAdapter.__index = ProjectTitleAdapter
function ProjectTitleAdapter:start_to_home()
    return self:unsupported("Project: Title has no standalone Home Screen")
end

local function backend_for(config_name)
    if config_name:find("simpleui", 1, true) then return SimpleUIAdapter end
    if config_name:find("zenos", 1, true) then return ZenOSAdapter end
    if config_name:find("project_title", 1, true) then return ProjectTitleAdapter end
    if config_name:find("bookshelf", 1, true) then return BookshelfAdapter end
    return StockAdapter
end

function Adapters.get_adapter(config_name, library_dir, sample_book, sample_folder)
    return backend_for(config_name):new(library_dir, sample_book, sample_folder)
end

return Adapters
