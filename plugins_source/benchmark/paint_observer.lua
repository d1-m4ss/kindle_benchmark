-- Target-content paint observation. Records are scoped to one action and never
-- escape into result history with widget/owner references attached.
local Observer = {}

function Observer.effectiveMode(chooser, library)
    return chooser and (chooser._leanui_view or chooser._leanui_visual_mode
        or chooser.display_mode or chooser.display_mode_type)
        or library and library.mode or "stock"
end

function Observer.install(UI, resolve, signature, now)
    local original_repaint = UI._repaint
    local samples
    local observer = {}
    local function pack(...) return {n=select("#", ...), ...} end
    local function repaint(manager, ...)
        if not samples then return original_repaint(manager, ...) end
        -- Resolve on every repaint, AFTER the action may have replaced chooser.
        local target = resolve()
        local own = target and rawget(target, "paintTo")
        local paint = target and target.paintTo
        local painted = {}
        if paint then
            target.paintTo = function(widget, ...)
                local result = pack(paint(widget, ...))
                if widget == target then
                    painted[#painted+1] = {owner=target, page=target.page, signature=signature(target)}
                end
                return unpack(result, 1, result.n)
            end
        end
        local result = pack(pcall(original_repaint, manager, ...))
        if target then target.paintTo = own end
        if not result[1] then error(result[2], 0) end
        local at = now()
        for _, frame in ipairs(painted) do
            frame.at = at
            -- A pathological action fails closed instead of retaining trees
            -- indefinitely. Normal library actions paint once or twice.
            if #samples < 64 then samples[#samples+1] = frame end
        end
        return unpack(result, 2, result.n)
    end
    UI._repaint = repaint
    function observer:begin() samples = {} end
    function observer:first()
        local target = resolve()
        if not target then return nil end
        local wanted = signature(target)
        for _, frame in ipairs(samples or {}) do
            if frame.owner == target and frame.page == target.page
                    and frame.signature ~= nil and frame.signature == wanted then
                return frame.at, frame.signature
            end
        end
    end
    function observer:stop() samples = nil end
    function observer:restore()
        if UI._repaint == repaint then UI._repaint = original_repaint end
        samples = nil
    end
    return observer
end

return Observer
