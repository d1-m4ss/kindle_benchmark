"""Energy profile: real idle, outermost refresh counting, artifact and session rules."""
import copy
import dataclasses
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import analyze_energy as analyze
from scripts import run_benchmarks as runner
from scripts.run_benchmarks import KOREADER_DIR, ROOT


def window(wall, cpu=100.0, actions=0, refreshes=0, pixels=0, flashing=0, tasks=None):
    return {"status": "PASS", "wall_s": wall, "actions": actions, "cpu_total_ms": cpu,
            "voluntary_switches": 1, "wakeups": 2, "tasks_fired": sum((tasks or {}).values()),
            "tasks_by_source": tasks or {}, "set_dirty_calls": 0, "refreshes": refreshes,
            "refresh_pixels": pixels, "disk_writes": 0,
            "refresh_by_type": {"full": {"count": flashing, "pixels": 0}} if flashing else {}}


def artifact():
    return {"reader_book": {"path": "/b.epub"}, "source_verified": True, "run_status": "PASS",
            "plugin_files_sha256": "a" * 64, "energy": {"windows": {
        "library_startup_tail": window(30), "library_idle": window(120),
        "library_paging": window(70, actions=30, refreshes=30),
        "book_cycles": window(60, actions=10, refreshes=10), "library_navigation": window(40, actions=10, refreshes=10),
        "reader_open_tail": window(30), "reader_idle": window(120),
        "reader_turns_short": window(21, actions=10, refreshes=10),
        "reader_turns_long": window(210, actions=100, refreshes=100),
        "reader_after_turns_tail": window(30), "library_after_close_tail": window(30),
    }}}


JOB = runner.Job("energy_R0_stock_r01", "energy", "energy", "R0_stock", (), "/l", "/h", "warm",
                 "energy", "real_2692", 2692, 0, 1, False, energy_idle_s=120, energy_tail_s=30,
                 energy_pace_s=2, energy_cycles=10, energy_nav_cycles=10)


JOB_FRESH = dataclasses.replace(JOB, run_id="energy_R0_stock_r00", fresh_home=True)


class ArtifactRules(unittest.TestCase):
    def test_complete_artifact_passes(self):
        self.assertEqual(runner.energy_errors(JOB, artifact()), [])

    def test_short_idle_is_rejected(self):
        data = artifact()
        data["energy"]["windows"]["reader_idle"]["wall_s"] = 119.0
        self.assertIn("energy window reader_idle ran 119.0s, expected 120s", runner.energy_errors(JOB, data))

    def test_stall_inside_a_short_tail_is_rejected(self):
        job = dataclasses.replace(JOB, energy_tail_s=5)
        data = artifact()
        data["energy"]["windows"]["reader_open_tail"]["wall_s"] = 11.0
        self.assertIn("energy window reader_open_tail ran 11.0s, expected 5s", runner.energy_errors(job, data))

    def test_stalled_idle_is_rejected(self):
        data = artifact()
        data["energy"]["windows"]["library_idle"]["wall_s"] = 200.0
        self.assertIn("energy window library_idle ran 200.0s, expected 120s", runner.energy_errors(JOB, data))

    def test_incomplete_actions_are_rejected(self):
        data = artifact()
        data["energy"]["windows"]["reader_turns_long"]["actions"] = 99
        self.assertIn("energy window reader_turns_long ran 99 actions, expected 100", runner.energy_errors(JOB, data))

    def test_missing_window_is_rejected(self):
        data = artifact()
        del data["energy"]["windows"]["book_cycles"]
        self.assertIn("energy window missing: book_cycles", runner.energy_errors(JOB, data))

    def test_negative_counter_is_rejected(self):
        data = artifact()
        data["energy"]["windows"]["library_idle"]["cpu_total_ms"] = -1
        self.assertIn("energy counter library_idle.cpu_total_ms invalid: -1", runner.energy_errors(JOB, data))

    def test_action_that_paints_nothing_is_rejected(self):
        data = artifact()
        data["energy"]["windows"]["library_paging"]["refreshes"] = 0
        self.assertIn("energy window library_paging made 0 refreshes for 30 actions", runner.energy_errors(JOB, data))

    def test_plugin_change_during_the_run_is_rejected(self):
        data = artifact()
        data["source_verified"] = False
        self.assertIn("energy plugin tree changed during the run", runner.energy_errors(JOB, data))

    def test_later_round_must_measure_the_first_rounds_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            layout = runner.make_layout("c", "energy")
            layout = dataclasses.replace(layout, raw=Path(tmp))
            (Path(tmp) / "energy_R0_stock_r00.json").write_text(json.dumps({"plugin_files_sha256": "a" * 64}))
            self.assertEqual(runner.energy_round_errors(JOB, layout, artifact()), [])
            changed = artifact()
            changed["plugin_files_sha256"] = "b" * 64
            self.assertEqual(runner.energy_round_errors(JOB, layout, changed),
                             ["energy plugin code differs from energy_R0_stock_r00.json"])

    def test_later_round_needs_the_first_round(self):
        with tempfile.TemporaryDirectory() as tmp:
            layout = dataclasses.replace(runner.make_layout("c", "energy"), raw=Path(tmp))
            self.assertEqual(runner.energy_round_errors(JOB, layout, artifact()),
                             ["energy first round missing: energy_R0_stock_r00.json"])

    def test_energy_declares_no_latency_scenarios(self):
        self.assertEqual(runner.expected_scenarios(JOB), set())


class Blocks(unittest.TestCase):
    def test_default_campaign_stays_within_fifteen_minutes(self):
        jobs = runner.energy_blocks("c")["energy"]
        j = jobs[0]
        # sleeps only; action work added at most 10 s per run in the smoke run, 20 s allows for it
        sleeps = (2 * j.energy_idle_s + 4 * j.energy_tail_s + j.energy_pace_s * (
            j.energy_turns + 2 * j.energy_cycles + 2 * j.energy_nav_cycles
            + j.energy_reader_short_turns + j.energy_reader_long_turns))
        self.assertLessEqual(len(jobs) * (sleeps + 20), 15 * 60)

    def test_one_interleaved_block_with_only_round_zero_fresh(self):
        blocks = runner.energy_blocks("c", 2)
        self.assertEqual(list(blocks), ["energy"])
        jobs = blocks["energy"]
        self.assertEqual([j.run_id for j in jobs[:6]], [
            "energy_R0_stock_r00", "energy_R13_m1n1mal_r00", "energy_R14_cyberui_r00",
            "energy_R13_m1n1mal_r01", "energy_R14_cyberui_r01", "energy_R0_stock_r01"])
        self.assertEqual({j.run_id for j in jobs if j.fresh_home},
                         {f"energy_{c}_r00" for c in runner.ENERGY_CONFIGS})
        self.assertEqual({j.ko_home for j in jobs if j.config == "R14_cyberui"},
                         {str(runner.ENV_BASE / "c" / "energy" / "R14_cyberui")})

    def test_only_an_incomplete_first_round_resets_its_corpus(self):
        jobs = runner.energy_blocks("c", 1)["energy"]
        layout = runner.make_layout("no-such-campaign", "energy")
        done = {"energy_R0_stock_r00"}
        with patch.object(runner, "valid_completed_result", lambda job, _: job.run_id in done):
            reset = runner.energy_corpora_to_reset(jobs, layout, resume=True)
            self.assertEqual({p.parent.name for p in reset}, {"R13_m1n1mal", "R14_cyberui"})
            everything = runner.energy_corpora_to_reset(jobs, layout, resume=False)
            self.assertEqual({p.parent.name for p in everything}, set(runner.ENERGY_CONFIGS))

    def test_later_rounds_keep_the_targets_of_the_first(self):
        first, later = JOB_FRESH, JOB
        with tempfile.TemporaryDirectory() as tmp:
            targets = Path(tmp) / "benchmark_targets.json"
            self.assertFalse(runner.energy_keeps_targets(later, targets))  # none yet
            targets.write_text("{}")
            self.assertTrue(runner.energy_keeps_targets(later, targets))
            self.assertFalse(runner.energy_keeps_targets(first, targets))
            other = dataclasses.replace(later, profile="real")
            self.assertFalse(runner.energy_keeps_targets(other, targets))

    def test_failed_energy_block_keeps_its_corpus_and_other_phases_do_not(self):
        self.assertFalse(runner.removes_corpus_after_block(False, True))
        self.assertTrue(runner.removes_corpus_after_block(True, True))
        self.assertTrue(runner.removes_corpus_after_block(False, False))

    def test_fractional_pace_reaches_the_harness_and_defaults_match_it(self):
        job = runner.energy_blocks("c")["energy"][0]
        env = runner.energy_environment(job)
        self.assertEqual(env["BENCHMARK_ENERGY_PACE_S"], "0.25")
        lua = (ROOT / "plugins_source/benchmark/main.lua").read_text()
        for name, value in env.items():
            found = re.search(rf'env_number\("{name}", ([\d.]+)\)', lua)
            self.assertIsNotNone(found, name)
            self.assertEqual(float(found[1]), float(value), name)

    def test_unknown_unpinned_plugin_is_refused(self):
        with self.assertRaisesRegex(RuntimeError, "unknown plugins"):
            runner.verify_pinned_revisions(["no_such_plugin"])


class Summary(unittest.TestCase):
    def test_session_is_idle_rate_plus_cost_above_idle(self):
        windows = artifact()["energy"]["windows"]
        windows["reader_idle"]["cpu_total_ms"] = 120.0      # 1 ms/s
        windows["library_idle"]["cpu_total_ms"] = 240.0     # 2 ms/s
        windows["reader_turns_long"].update(cpu_total_ms=310.0)  # 100 above idle, 1 per page
        windows["library_paging"].update(cpu_total_ms=170.0)     # 30 above idle, 1 per page
        windows["library_navigation"].update(cpu_total_ms=100.0)  # 20 above idle, 2 per visit
        windows["book_cycles"].update(cpu_total_ms=130.0)        # 10 above idle, 1 per cycle
        windows["reader_open_tail"].update(cpu_total_ms=33.0)         # 3 above idle
        windows["reader_after_turns_tail"].update(cpu_total_ms=35.0)  # 5 above idle
        windows["library_after_close_tail"].update(cpu_total_ms=64.0)  # 4 above idle
        expected = 1800 + 600 + 60 + 10 + 6 + 1 + 3 + 5 + 4
        self.assertAlmostEqual(analyze.session_for_run(windows)["cpu_total_ms"], expected)

    def test_session_splits_idle_from_actions_and_lists_negative_terms(self):
        windows = artifact()["energy"]["windows"]
        windows["reader_idle"]["cpu_total_ms"] = 120.0
        windows["library_idle"]["cpu_total_ms"] = 240.0
        windows["reader_turns_long"]["cpu_total_ms"] = 110.0  # 100 below idle
        session = analyze.session_for_run(windows)
        self.assertAlmostEqual(session["cpu_total_ms_idle"], 1800 + 600)
        self.assertAlmostEqual(session["cpu_total_ms"], session["cpu_total_ms_idle"] + session["cpu_total_ms_actions"])
        self.assertAlmostEqual(session["negative_cpu_terms"]["reader_turns_long"], -60.0)

    def test_child_cpu_in_steady_action_window_is_warned(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        run["energy"]["windows"]["library_paging"]["cpu_children_ms"] = 900.0
        text = analyze.render(analyze.summarize([run]))
        self.assertIn("R0_stock, library_paging: child-process CPU in steady rounds, median 900 ms", text)

    def test_child_cpu_in_idle_window_is_warned_as_multiplied(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        run["energy"]["windows"]["library_idle"]["cpu_children_ms"] = 42.0
        self.assertIn("Multiplied up in the extrapolated session.", analyze.render(analyze.summarize([run])))

    def test_harness_end_of_window_wakeup_is_not_the_stacks(self):
        windows = artifact()["energy"]["windows"]
        windows["reader_idle"]["wakeups"] = 1
        windows["library_idle"]["wakeups"] = 1
        self.assertEqual(analyze.session_for_run(windows)["wakeups_idle"], 0)

    def test_short_idle_sample_and_single_round_are_warned(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        for name in ("library_idle", "reader_idle"):
            run["energy"]["windows"][name].update(wall_s=30, tasks_fired=2)
        text = analyze.render(analyze.summarize([run]))
        self.assertIn("R0_stock: 1 steady run(s), so no spread is known", text)
        self.assertIn("R0_stock: idle sample of 30 s, under 60 s.", text)
        self.assertIn("Transient work in the sample is scored as sustained.", text)

    def test_short_idle_sample_is_warned_even_with_no_events_in_it(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        for name in ("library_idle", "reader_idle"):
            run["energy"]["windows"][name].update(wall_s=30, wakeups=1, tasks_fired=0)
        self.assertIn("R0_stock: idle sample of 30 s, under 60 s.", analyze.render(analyze.summarize([run])))

    def test_small_negative_terms_are_noise(self):
        windows = artifact()["energy"]["windows"]
        windows["reader_idle"]["cpu_total_ms"] = 120.0
        windows["library_idle"]["cpu_total_ms"] = 120.0
        windows["library_after_close_tail"]["cpu_total_ms"] = 25.0  # 5 below idle
        self.assertEqual(analyze.session_for_run(windows)["negative_cpu_terms"].get("library_after_close_tail"), None)

    def test_unpinned_state_is_stated(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        text = analyze.render(analyze.summarize([run]), unpinned=[
            {"plugin": "m1n1mal", "head": "c71bd44d2", "pinned": "44ea3f53b", "uncommitted_entries": 10}])
        self.assertIn("Measured off its pin: m1n1mal at c71bd44, pinned 44ea3f5, 10 uncommitted entries.", text)

    def test_floor_is_stocks_reader_idle_rate_over_the_session(self):
        stock = {"run_id": "energy_R0_stock_r01", **artifact()}
        other = {"run_id": "energy_X_r01", **copy.deepcopy(artifact())}
        for run, reader_idle in ((stock, 120.0), (other, 240.0)):
            windows = run["energy"]["windows"]
            for name, w in windows.items():
                w["cpu_total_ms"] = reader_idle / 120 * w["wall_s"]
        text = analyze.render(analyze.summarize([stock, other]))
        self.assertIn("| R0_stock | 0.00 | n/a |", text)   # no work above the floor
        self.assertIn("| X | 2.10 | n/a |", text)          # 1 ms/s more for 35 min

    def test_failed_runs_are_ignored(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact(), "run_status": "FAILED"}
        self.assertEqual(analyze.summarize([run]), {})

    def test_first_run_stays_out_of_steady_figures(self):
        steady = {"run_id": "energy_R0_stock_r01", **artifact()}
        first = copy.deepcopy(steady)
        first["run_id"] = "energy_R0_stock_r00"
        first["energy"]["windows"]["library_idle"]["cpu_total_ms"] = 99999.0
        entry = analyze.summarize([first, steady])["R0_stock"]
        self.assertEqual(entry["steady_runs"], 1)
        self.assertEqual(entry["windows"]["library_idle"]["cpu_total_ms"]["median"], 100.0)
        self.assertEqual(entry["first_run"]["library_idle"]["cpu_total_ms"], 99999.0)

    def test_page_cost_shows_growth_between_short_and_long_runs(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        w = run["energy"]["windows"]
        w["reader_idle"]["cpu_total_ms"] = 120.0                # 1 ms/s
        w["reader_turns_short"]["cpu_total_ms"] = 41.0          # 20 above idle over 10 pages
        w["reader_turns_long"]["cpu_total_ms"] = 610.0          # 400 above idle over 100 pages
        w["reader_after_turns_tail"]["cpu_total_ms"] = 80.0     # 50 above idle
        self.assertIn("| R0_stock | 2.0 | 4.0 | 50 |", analyze.render(analyze.summarize([run])))

    def test_flashing_refreshes_and_idle_timers_are_reported(self):
        run = {"run_id": "energy_R0_stock_r01", **artifact()}
        run["energy"]["windows"]["reader_turns_long"].update(
            refreshes=100, refresh_by_type={"full": {"count": 16, "pixels": 0}})
        run["energy"]["windows"]["reader_idle"]["tasks_by_source"] = {"plugins/x.koplugin/main.lua:7": 4}
        entry = analyze.summarize([run])["R0_stock"]
        self.assertEqual(entry["windows"]["reader_turns_long"]["flashing_refreshes"]["median"], 16)
        self.assertEqual(entry["idle_tasks"]["reader_idle"], {"plugins/x.koplugin/main.lua:7": 4})
        self.assertIn("plugins/x.koplugin/main.lua:7", analyze.render(analyze.summarize([run])))


LUA = r'''
local ffi = require("ffi")
ffi.cdef[[
struct rusage {
  struct { long tv_sec; int tv_usec; } ru_utime; struct { long tv_sec; int tv_usec; } ru_stime;
  long ru_maxrss; long ru_ixrss; long ru_idrss; long ru_isrss; long ru_minflt; long ru_majflt;
  long ru_nswap; long ru_inblock; long ru_oublock; long ru_msgsnd; long ru_msgrcv; long ru_nsignals;
  long ru_nvcsw; long ru_nivcsw; };
int getrusage(int who, struct rusage *usage);
]]
table.pack = table.pack or function(...) return {n=select("#", ...), ...} end
table.unpack = table.unpack or unpack
local clock = 0
package.preload["ui/time"] = function() return {
    now = function() return clock end, monotonic = function() return clock end,
    to_s = function(v) return v end } end
local Energy = dofile(arg[1])
local function plugin_task() end
local function harness_task() end
local info = debug.getinfo
debug.getinfo = function(f, what)
    if f == harness_task then return {source="@/x/plugins/benchmark.koplugin/main.lua", linedefined=9} end
    if f == plugin_task then return {source="@/x/plugins/foo.koplugin/main.lua", linedefined=3} end
    return info(f, what)
end
local UI = {_task_queue = {}, _checkTasks = function() return "checked" end,
            setDirty = function() return "dirty" end}
local Screen = {getWidth = function() return 100 end, getHeight = function() return 10 end,
    bb = {getBoundedRect = function(_, x, y, w, h) return x, y, w, h end}}
function Screen:refreshFullImp() return "drawn" end
function Screen:refreshPartialImp(x, y, w, h) return self:refreshFullImp(x, y, w, h) end
function Screen:refreshUIImp(x, y, w, h) return self:refreshPartialImp(x, y, w, h) end
function Screen:refreshFlashUIImp(x, y, w, h) return self:refreshFullImp(x, y, w, h) end
function Screen:refreshNoMergePartialImp() end
function Screen:refreshFlashPartialImp() end
function Screen:refreshNoMergeUIImp() end
function Screen:refreshFastImp() end
function Screen:refreshA2Imp() end
local original_full = Screen.refreshFullImp
local input = {waitEvent = function() return "event" end}
local meter = Energy.install({UIManager = UI, Screen = Screen, input = input})

assert(Screen:refreshUIImp(0, 0, 5, 5) == "drawn")  -- outside a window: not counted
local rec = meter.window("w", function()
    assert(input.waitEvent() == "event")
    UI._task_queue = {{time = 9, action = plugin_task}, {time = 0, action = harness_task}, {time = 0, action = plugin_task}}
    assert(UI._checkTasks(UI) == "checked")
    assert(UI.setDirty() == "dirty")
    Screen:refreshUIImp(0, 0, 2, 3)        -- ui -> partial -> full: one request
    Screen:refreshFlashUIImp(0, 0, 4, 5)   -- flashing
    Screen:refreshFullImp()                -- no rectangle: the whole screen
    return 7
end)
assert(rec.status == "PASS" and rec.actions == 7)
assert(rec.wakeups == 1)
assert(rec.tasks_fired == 1, "harness and future tasks are excluded: " .. rec.tasks_fired)
assert(rec.tasks_by_source["plugins/foo.koplugin/main.lua:3"] == 1)
assert(rec.set_dirty_calls == 1)
assert(rec.refreshes == 3, "only the outermost Imp counts: " .. rec.refreshes)
assert(rec.refresh_pixels == 6 + 20 + 1000, rec.refresh_pixels)
assert(rec.refresh_by_type.ui.count == 1 and rec.refresh_by_type.full.count == 2)
assert(rec.cpu_total_ms >= 0)

local failed = meter.window("f", function() error("boom") end)
assert(failed.status == "FAILED" and failed.reason:find("boom"))
local short = meter.window("s", function() return 2, "reason" end)
assert(short.status == "FAILED" and short.actions == 2 and short.reason == "reason")

-- a failing action stops the run, names the window and leaves later ones out
local sleeps = {}
local adapter = {ensure_filemanager = function() end, goto_page = function() end,
    library_next_page_transition = function() return {success = false, reason = "no page"} end}
local windows, failure = Energy.run({adapter = adapter, meter = meter,
    sleep = function(s) sleeps[#sleeps + 1] = s end, settle = function() end, settle_ticks = 1,
    emit_ready = function() end, select_next_book = function() end, select_next_folder = function() end,
    select_reader_book = function() return true end,
    idle_s = 120, tail_s = 30, pace_s = 2, turns = 3, cycles = 1, nav_cycles = 1,
    reader_short_turns = 1, reader_long_turns = 2})
assert(failure == "library_paging: no page", failure)
assert(sleeps[1] == 30 and sleeps[2] == 120 and #sleeps == 2)
assert(windows.library_idle and not windows.book_cycles and not windows.reader_idle)

meter.restore()
assert(Screen.refreshFullImp == original_full and rawget(Screen, "refreshFullImp") == original_full)
assert(UI.setDirty() == "dirty" and input.waitEvent() == "event")
print("LUA_OK")
'''


class Counters(unittest.TestCase):
    def test_counters_with_a_stubbed_ui(self):
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "energy_test.lua"
            script.write_text(LUA)
            done = subprocess.run(["./luajit", str(script), str(ROOT / "plugins_source/benchmark/energy.lua")],
                                  cwd=KOREADER_DIR, capture_output=True, text=True, timeout=60)
        self.assertEqual(done.returncode, 0, done.stderr + done.stdout)
        self.assertIn("LUA_OK", done.stdout)


if __name__ == "__main__":
    unittest.main()
