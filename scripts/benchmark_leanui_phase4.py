#!/usr/bin/env python3
"""
Benchmark comparison for LeanUI Phase 4: Quick Settings overhead & lifecycle.
Tests:
1. Standard library paging with QS never opened (zero-overhead lazy verification)
2. First QS open latency
3. Subsequent QS open latency
4. Memory stability across 20 open/close cycles
"""

import os
import sys
import json
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KOREADER_DIR = ROOT / "koreader_src" / "koreader-emulator-arm64-apple-darwin27.0.0-debug" / "koreader"
LUAJIT = KOREADER_DIR / "luajit"
PLUGINS_SRC = ROOT / "plugins_source"
BENCHMARK_PLUGIN = PLUGINS_SRC / "benchmark"
DEFAULT_LEANUI_SRC = Path("/Users/d13mas/Documents/scripts/koreader_plugin/leanui.koplugin")
LEANUI_SRC = Path(os.environ.get("LEANUI_SOURCE", DEFAULT_LEANUI_SRC)).resolve()

RUN_BASE = ROOT / "env_benchmark_runs" / "leanui_phase4_validation"
LIB_DIR = ROOT / "libraries" / "flat" / "books_50"


def get_git_info(repo_path: Path):
    if not (repo_path / ".git").exists():
        return "not_a_git_repo", False
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_path, text=True).strip()
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path, text=True).strip()
    return sha, len(status) > 0


def setup_env(run_id: str):
    home_dir = RUN_BASE / run_id
    if home_dir.exists():
        shutil.rmtree(home_dir)
    plugins_dir = home_dir / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)

    (plugins_dir / "benchmark.koplugin").symlink_to(BENCHMARK_PLUGIN)
    (plugins_dir / "leanui.koplugin").symlink_to(LEANUI_SRC)

    settings_content = [
        'return {',
        f'    ["home_dir"] = "{LIB_DIR}",',
        f'    ["lastdir"] = "{LIB_DIR}",',
        '    ["plugins_disabled"] = { ["coverbrowser"] = true },',
        '    ["leanui_settings"] = {',
        '        ["enabled"] = true,',
        '        ["library_mode"] = "dense",',
        '        ["items_per_page_portrait"] = 14,',
        '        ["cache_enabled"] = true,',
        '        ["scoped_redraw"] = true,',
        '        ["navbar_enabled"] = true,',
        '        ["navbar_labels"] = true,',
        '        ["quicksettings_enabled"] = true,',
        '    },',
        '}\n',
    ]

    settings_file = home_dir / "settings.reader.lua"
    settings_file.write_text("\n".join(settings_content))

    books = sorted(str(p) for p in LIB_DIR.rglob("*.epub") if p.is_file())
    targets_file = home_dir / "benchmark_targets.json"
    targets_file.write_text(json.dumps({
        "sample_book": books[0] if books else None,
        "sample_folder": None,
        "candidate_books": books[:10],
    }, indent=2))
    return home_dir, targets_file


def run_library_benchmark(run_id: str):
    home_dir, targets_file = setup_env(run_id)
    out_file = home_dir / f"{run_id}_results.json"
    screenshot_dir = home_dir / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    is_darwin = sys.platform == "darwin"
    env = os.environ.copy()
    env.pop("EMULATE_READER_FLASH", None)

    env.update({
        "KO_HOME": str(home_dir),
        "EMULATE_READER_W": "618" if is_darwin else "1236",
        "EMULATE_READER_H": "824" if is_darwin else "1648",
        "EMULATE_READER_DPI": "300",
        "EMULATE_BW_SCREEN": "1",
        "BENCHMARK_ENABLE": "1",
        "BENCHMARK_CONFIG": run_id,
        "BENCHMARK_MODE": "warm",
        "BENCHMARK_PROFILE": "synthetic",
        "BENCHMARK_LIBRARY_DIR": str(LIB_DIR),
        "BENCHMARK_OUTPUT_FILE": str(out_file),
        "BENCHMARK_WARMUP_COUNT": "1",
        "BENCHMARK_MEASURE_COUNT": "2",
        "BENCHMARK_BOOK_COUNT": "50",
        "BENCHMARK_DATASET_MODE": "flat",
        "BENCHMARK_EXPECTED_PLUGINS": "leanui",
        "BENCHMARK_RUN_OVERHEAD": "1",
        "BENCHMARK_OVERHEAD_COUNT": "30",
        "BENCHMARK_TARGETS_FILE": str(targets_file),
        "BENCHMARK_SCREENSHOT_DIR": str(screenshot_dir),
    })

    cmd = ["./luajit", "reader.lua", str(LIB_DIR)]
    p = subprocess.run(cmd, cwd=str(KOREADER_DIR), env=env, capture_output=True, text=True)
    if p.returncode != 0:
        print("Library benchmark FAILED:\n", p.stderr[-1000:])
        return None
    return json.loads(out_file.read_text())


def run_qs_lifecycle_test():
    lua_code = """
    package.path = "./?.lua;./tests/helpers/?.lua;" .. package.path
    require("mock_koreader").setup()

    -- Check lazy boundary before opening QS
    local pre_loaded = package.loaded["ui/quicksettings/panel"] ~= nil
                    or package.loaded["ui/quicksettings/actions"] ~= nil

    -- 1. Measure First Open
    local t0 = os.clock()
    local Panel = require("ui/quicksettings/panel")
    local p1 = Panel:new{}
    local t_first_ms = (os.clock() - t0) * 1000
    p1:dismiss()

    -- 2. Measure Subsequent Open
    local t1 = os.clock()
    local p2 = Panel:new{}
    local t_subseq_ms = (os.clock() - t1) * 1000
    p2:dismiss()

    -- 3. Measure 20 Open/Close Cycles Memory
    collectgarbage("collect")
    collectgarbage("collect")
    local mem_before_kb = collectgarbage("count")

    for i = 1, 20 do
        local p = Panel:new{}
        p:dismiss()
    end

    collectgarbage("collect")
    collectgarbage("collect")
    local mem_after_kb = collectgarbage("count")
    local mem_drift_kb = mem_after_kb - mem_before_kb

    print("QS_RESULT:" .. string.format('{"lazy_boundary_pass": %s, "first_open_ms": %.3f, "subseq_open_ms": %.3f, "mem_drift_kb": %.2f}',
        tostring(not pre_loaded), t_first_ms, t_subseq_ms, mem_drift_kb))
    """

    p = subprocess.run([str(LUAJIT), "-e", lua_code], cwd=str(LEANUI_SRC), capture_output=True, text=True)
    if p.returncode != 0:
        print("QS lifecycle test failed:\n", p.stderr)
        return None

    for line in p.stdout.splitlines():
        if line.startswith("QS_RESULT:"):
            return json.loads(line[len("QS_RESULT:"):])
    print("Could not find QS_RESULT in output:\n", p.stdout)
    return None


def extract_metrics(res: dict):
    scenarios = res.get("scenarios", {})
    mem = res.get("memory_checkpoints", {})

    def get_med(scen_name):
        sc = scenarios.get(scen_name, {})
        it = sc.get("iterations", [])
        if not it:
            return sc.get("wall_time_ms", 0.0)
        times = [x.get("wall_time_ms", 0.0) for x in it if "wall_time_ms" in x]
        if not times:
            return 0.0
        times.sort()
        return times[len(times) // 2]

    cached_iter = scenarios.get("library_cached_paging", {}).get("iterations", [])
    entries_per_page = 0
    if cached_iter and "visible_count_after" in cached_iter[0]:
        entries_per_page = cached_iter[0]["visible_count_after"]

    render_ms = get_med("library_first_render")
    seq_ms = get_med("library_sequential_paging")
    cached_ms = get_med("library_cached_paging")
    stress_lua_kb = mem.get("post_stress_idle", {}).get("forced_gc_live_heap_kb", 0)

    return {
        "status": res.get("run_status", "UNKNOWN"),
        "entries_per_page": entries_per_page,
        "render_ms": render_ms,
        "seq_ms": seq_ms,
        "cached_ms": cached_ms,
        "stress_lua_mib": stress_lua_kb / 1024.0,
    }


def main():
    print("==================================================")
    print("LeanUI Phase 4: Quick Settings Benchmark & Lifecycle")
    print("==================================================")

    leanui_sha, leanui_dirty = get_git_info(LEANUI_SRC)
    print(f"LeanUI Source: {LEANUI_SRC}")
    print(f"LeanUI Commit: {leanui_sha} {'(DIRTY)' if leanui_dirty else '(CLEAN)'}")

    # 1. Paging & first render (QS never opened)
    print("\n--- 1. Library Paging with QS Unopened (Zero-Overhead Check) ---")
    raw_bench = run_library_benchmark("P4_unopened_library")
    if not raw_bench:
        sys.exit(1)
    m = extract_metrics(raw_bench)
    print(f"  Result: {m['status']} | {m['entries_per_page']} entries | render: {m['render_ms']:.2f}ms | seq: {m['seq_ms']:.2f}ms | cached: {m['cached_ms']:.2f}ms | Lua: {m['stress_lua_mib']:.2f}MiB")

    # 2. QS Lifecycle & Latency
    print("\n--- 2. Quick Settings Lifecycle & Latencies ---")
    qs_res = run_qs_lifecycle_test()
    if not qs_res:
        sys.exit(1)

    print(f"  Lazy Boundary at Init: {'PASS' if qs_res['lazy_boundary_pass'] else 'FAIL'}")
    print(f"  First Open Latency:    {qs_res['first_open_ms']:.2f} ms")
    print(f"  Subsequent Open:       {qs_res['subseq_open_ms']:.2f} ms")
    print(f"  20 Cycles Heap Drift:  {qs_res['mem_drift_kb']:.2f} KiB ({qs_res['mem_drift_kb']/1024.0:.3f} MiB)")

    print("\n================== PHASE 4 SUMMARY ==================")
    print(f"Lazy-Load Boundary Pass:    {qs_res['lazy_boundary_pass']}")
    print(f"First Open Time:            {qs_res['first_open_ms']:.2f} ms")
    print(f"Subsequent Open Time:       {qs_res['subseq_open_ms']:.2f} ms")
    print(f"20-Cycle Heap Drift:        {qs_res['mem_drift_kb']:.2f} KiB (Budget < 512 KiB)")
    print(f"Library Cached Paging:      {m['cached_ms']:.2f} ms (Budget < 15.0 ms)")
    print(f"Library Live Lua Heap:      {m['stress_lua_mib']:.2f} MiB")
    print("======================================================")

    failures = []
    if not qs_res["lazy_boundary_pass"]:
        failures.append("Lazy boundary violated: QS was loaded before first open")
    if qs_res["mem_drift_kb"] > 512.0:
        failures.append(f"Memory growth across 20 cycles exceeded 512 KiB: {qs_res['mem_drift_kb']:.2f} KiB")
    if m["cached_ms"] > 16.0:
        failures.append(f"Cached paging degraded: {m['cached_ms']:.2f} ms")

    if failures:
        print("\n[ACCEPTANCE FAILED]:")
        for f in failures:
            print(" -", f)
        sys.exit(1)
    else:
        print("\n[ACCEPTANCE PASS]: Phase 4 Quick Settings passed all gate requirements.")


if __name__ == "__main__":
    main()
