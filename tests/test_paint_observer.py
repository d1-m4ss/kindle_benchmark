"""Production observer must bind timestamp to owner/content, not the final tick."""
from pathlib import Path
import subprocess
import unittest
from scripts.run_benchmarks import KOREADER_DIR, ROOT


class PaintObserver(unittest.TestCase):
    def test_target_content_and_replacement(self):
        module = ROOT / 'plugins_source/benchmark/paint_observer.lua'
        self.assertTrue(module.exists(), 'content-bound observer is missing')
        lua = r'''
local Observer = dofile(arg[0])
local clock, current = 0
local draw, fail_repaint = true, false
local function chooser(page)
    return {page=page, signature="page"..page, paintTo=function() end}
end
current = chooser(1)
local UI = {_repaint=function()
    if fail_repaint then error("test repaint failed") end
    if draw and current then current:paintTo() end
end}
local function resolve() return current end
local function signature(w) return w.signature end
local observer = Observer.install(UI, resolve, signature, function() return clock end)
observer:begin()
clock=5; UI:_repaint()
current.page=2; current.signature="page2"
clock=20; UI:_repaint()
assert(observer:first()==20, "old page paint cannot borrow later target identity")
observer:begin()
local old = current
current = chooser(3)
clock=30; UI:_repaint()
assert(observer:first()==30, "replacement chooser paint must be observed")
assert(rawget(old, "paintTo") ~= nil)
observer:begin()
draw=false; UI:_repaint()
assert(observer:first()==nil, "no-op repaint is not evidence")
fail_repaint=true
local ok=pcall(function() UI:_repaint() end)
assert(not ok and observer:first()==nil, "failed repaint is not evidence")
current=chooser(4)
assert(Observer.effectiveMode({_leanui_view="cover_grid"}, {mode="compact_list"})=="cover_grid")
observer:restore()
assert(current.paintTo ~= nil)
print("PASS content identity, replacement, failed repaint, active mode")
'''
        result = subprocess.run([str(KOREADER_DIR/'luajit'), '-e', lua, str(module)],
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__': unittest.main()
