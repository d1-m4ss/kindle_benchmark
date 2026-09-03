-- geometry.lua — Exact spatial union and clipping for E-ink display regions
local Geometry = {}

local SCREEN_W = 1236
local SCREEN_H = 1648
local SCREEN_TOTAL_PIXELS = SCREEN_W * SCREEN_H

function Geometry.clip_rect(r)
    if not r then return 0, 0, 0, 0, 0 end
    local x = r.x or 0
    local y = r.y or 0
    local w = math.max(0, r.w or SCREEN_W)
    local h = math.max(0, r.h or SCREEN_H)
    local x1 = math.max(0, math.min(SCREEN_W, x))
    local y1 = math.max(0, math.min(SCREEN_H, y))
    local x2 = math.max(0, math.min(SCREEN_W, x + w))
    local y2 = math.max(0, math.min(SCREEN_H, y + h))
    local clipped_w = math.max(0, x2 - x1)
    local clipped_h = math.max(0, y2 - y1)
    local area = clipped_w * clipped_h
    return x1, y1, clipped_w, clipped_h, area
end

-- Coordinate-compression sweep-line algorithm for exact 2D rectangle union area
function Geometry.calculate_spatial_union(rects)
    if not rects or #rects == 0 then
        return 0, 0, 0, 0, 0
    end

    local clipped = {}
    local x_coords_map = {}
    local cumulative_area = 0
    local largest_single_area = 0

    for _, r in ipairs(rects) do
        local rx, ry, rw, rh, area = Geometry.clip_rect(r)
        if rw > 0 and rh > 0 then
            table.insert(clipped, { x1 = rx, y1 = ry, x2 = rx + rw, y2 = ry + rh, area = area })
            x_coords_map[rx] = true
            x_coords_map[rx + rw] = true
            cumulative_area = cumulative_area + area
            if area > largest_single_area then
                largest_single_area = area
            end
        end
    end

    if #clipped == 0 then
        return 0, 0, 0, 0, 0
    end

    local x_coords = {}
    for x in pairs(x_coords_map) do
        table.insert(x_coords, x)
    end
    table.sort(x_coords)

    local total_union_area = 0

    for i = 1, #x_coords - 1 do
        local x1 = x_coords[i]
        local x2 = x_coords[i + 1]
        local dx = x2 - x1
        if dx > 0 then
            -- Collect all y-intervals active in this vertical stripe [x1, x2]
            local y_intervals = {}
            for _, r in ipairs(clipped) do
                if r.x1 <= x1 and r.x2 >= x2 then
                    table.insert(y_intervals, { y1 = r.y1, y2 = r.y2 })
                end
            end

            if #y_intervals > 0 then
                -- Sort by y1 and merge overlapping y-intervals
                table.sort(y_intervals, function(a, b) return a.y1 < b.y1 end)
                local merged_y_len = 0
                local cur_y1 = y_intervals[1].y1
                local cur_y2 = y_intervals[1].y2

                for j = 2, #y_intervals do
                    local next_y1 = y_intervals[j].y1
                    local next_y2 = y_intervals[j].y2
                    if next_y1 <= cur_y2 then
                        if next_y2 > cur_y2 then
                            cur_y2 = next_y2
                        end
                    else
                        merged_y_len = merged_y_len + (cur_y2 - cur_y1)
                        cur_y1 = next_y1
                        cur_y2 = next_y2
                    end
                end
                merged_y_len = merged_y_len + (cur_y2 - cur_y1)

                total_union_area = total_union_area + (dx * merged_y_len)
            end
        end
    end

    -- Strict Invariant assertions
    total_union_area = math.max(0, math.min(SCREEN_TOTAL_PIXELS, total_union_area))
    if total_union_area > cumulative_area then
        total_union_area = cumulative_area
    end

    local unique_dirty_pct = (total_union_area / SCREEN_TOTAL_PIXELS) * 100.0
    local cumulative_dirty_screen_equivalents = cumulative_area / SCREEN_TOTAL_PIXELS
    local largest_single_pct = (largest_single_area / SCREEN_TOTAL_PIXELS) * 100.0

    return total_union_area, cumulative_area, unique_dirty_pct, cumulative_dirty_screen_equivalents, largest_single_pct
end

return Geometry
