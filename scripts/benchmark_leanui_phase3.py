#!/usr/bin/env python3
"""
Benchmark comparison for LeanUI Phase 3: Bottom Navbar overhead.
Compares:
- Phase 2 baseline: Dense 14 rows + scoped redraw, navbar disabled
- Phase 3: Dense 14 rows + scoped redraw, navbar enabled
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
PLUGINS_SRC = ROOT / "plugins_source"
BENCHMARK_PLUGIN = PLUGINS_SRC / "benchmark"
DEFAULT_LEANUI_SRC = Path("/Users/d13mas/Documents/scripts/koreader_plugin/leanui.koplugin")
LEANUI_SRC = Path(os.environ.get("LEANUI_SOURCE", DEFAULT_LEANUI_SRC)).resolve()

RUN_BASE = ROOT / "env_benchmark_runs" / "leanui_phase3_validation"
LIB_DIR = ROOT / "libraries" / "flat" / "books_50"


def get_git_info(repo_path: Path):
    if not (repo_path / ".git").exists():
        return "not_a_git_repo", False
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_path, text=True).strip()
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path, text=True).strip()
    return sha, len(status) > 0


def write_targets(library: Path, output_file: Path):
    books = sorted(str(p) for p in library.rglob("*.epub") if p.is_file())
    targets = {
        "sample_book": books[0] if books else None,
        "sample_folder": None,
        "candidate_books": books[:10],
    }
    output_file.write_text(json.dumps(targets, indent=2))


def setup_env(run_id: str, enable_navbar: bool):
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
        f'        ["navbar_enabled"] = {"true" if enable_navbar else "false"},',
        '        ["navbar_labels"] = true,',
        '    },',
        '}\n',
    ]

    settings_file = home_dir / "settings.reader.lua"
    settings_file.write_text("\n".join(settings_content))

    targets_file = home_dir / "benchmark_targets.json"
    write_targets(LIB_DIR, targets_file)
    return home_dir, targets_file


def run_cell(run_id: str, enable_navbar: bool, profile: str = "synthetic", warmup: int = 1, measure: int = 2):
    home_dir, targets_file = setup_env(run_id, enable_navbar)
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
        "BENCHMARK_PROFILE": profile,
        "BENCHMARK_LIBRARY_DIR": str(LIB_DIR),
        "BENCHMARK_OUTPUT_FILE": str(out_file),
        "BENCHMARK_WARMUP_COUNT": str(warmup),
        "BENCHMARK_MEASURE_COUNT": str(measure),
        "BENCHMARK_BOOK_COUNT": "50",
        "BENCHMARK_DATASET_MODE": "flat",
        "BENCHMARK_EXPECTED_PLUGINS": "leanui",
        "BENCHMARK_RUN_OVERHEAD": "1",
        "BENCHMARK_OVERHEAD_COUNT": "30",
        "BENCHMARK_TARGETS_FILE": str(targets_file),
        "BENCHMARK_SCREENSHOT_DIR": str(screenshot_dir),
    })

    cmd = ["./luajit", "reader.lua", str(LIB_DIR)]
    t0 = time.monotonic()
    p = subprocess.run(cmd, cwd=str(KOREADER_DIR), env=env, capture_output=True, text=True)
    dur = time.monotonic() - t0

    if p.returncode != 0:
        print(f"[{run_id}] FAILED (code {p.returncode})")
        print("STDERR tail:\n", p.stderr[-1000:])
        return None

    if not out_file.exists():
        print(f"[{run_id}] FAILED: output file {out_file} not found")
        return None

    data = json.loads(out_file.read_text())
    return data


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
    print("LeanUI Phase 3: Bottom Navbar Overhead Benchmark")
    print("==================================================")

    leanui_sha, leanui_dirty = get_git_info(LEANUI_SRC)
    print(f"LeanUI Source: {LEANUI_SRC}")
    print(f"LeanUI Commit: {leanui_sha} {'(DIRTY)' if leanui_dirty else '(CLEAN)'}")

    # 1. Phase 2 baseline (Navbar OFF)
    print("\n--- Running Phase 2 Baseline (Dense 14 rows, Navbar OFF) ---")
    p2_raw = run_cell("P2_dense_no_navbar", enable_navbar=False, profile="synthetic")
    if not p2_raw:
        sys.exit(1)
    p2_m = extract_metrics(p2_raw)
    print(f"  Result: {p2_m['status']} | {p2_m['entries_per_page']} entries | render: {p2_m['render_ms']:.2f}ms | seq: {p2_m['seq_ms']:.2f}ms | cached: {p2_m['cached_ms']:.2f}ms | Lua: {p2_m['stress_lua_mib']:.2f}MiB")

    # 2. Phase 3 (Navbar ON)
    print("\n--- Running Phase 3 (Dense 14 rows, Navbar ON) ---")
    p3_raw = run_cell("P3_dense_with_navbar", enable_navbar=True, profile="synthetic")
    if not p3_raw:
        sys.exit(1)
    p3_m = extract_metrics(p3_raw)
    print(f"  Result: {p3_m['status']} | {p3_m['entries_per_page']} entries | render: {p3_m['render_ms']:.2f}ms | seq: {p3_m['seq_ms']:.2f}ms | cached: {p3_m['cached_ms']:.2f}ms | Lua: {p3_m['stress_lua_mib']:.2f}MiB")

    # 3. Smoke validation profile for Phase 3
    print("\n--- Running Smoke Validation for Phase 3 ---")
    p3_smoke = run_cell("P3_dense_with_navbar", enable_navbar=True, profile="smoke_validation")
    smoke_status = p3_smoke.get("run_status", "UNKNOWN") if p3_smoke else "FAILED"
    print(f"  Smoke Status: {smoke_status}")

    # Deltas
    render_delta = p3_m["render_ms"] - p2_m["render_ms"]
    seq_delta = p3_m["seq_ms"] - p2_m["seq_ms"]
    cached_delta = p3_m["cached_ms"] - p2_m["cached_ms"]
    lua_delta = p3_m["stress_lua_mib"] - p2_m["stress_lua_mib"]

    print("\n================== PHASE 3 COMPARISON ==================")
    print("Metric                 | Phase 2 (No Nav) | Phase 3 (+Nav) | Delta         | Gate Budget")
    print("-----------------------+------------------+----------------+---------------+------------")
    print(f"Entries per page       | {p2_m['entries_per_page']:16d} | {p3_m['entries_per_page']:14d} | {p3_m['entries_per_page']-p2_m['entries_per_page']:+13d} | Equal (14)")
    print(f"First Render ms        | {p2_m['render_ms']:16.2f} | {p3_m['render_ms']:14.2f} | {render_delta:+11.2f} ms | Near noise")
    print(f"Sequential Paging ms   | {p2_m['seq_ms']:16.2f} | {p3_m['seq_ms']:14.2f} | {seq_delta:+11.2f} ms | Near noise")
    print(f"Cached Paging ms       | {p2_m['cached_ms']:16.2f} | {p3_m['cached_ms']:14.2f} | {cached_delta:+11.2f} ms | Near noise")
    print(f"Stress Live Lua MiB    | {p2_m['stress_lua_mib']:16.2f} | {p3_m['stress_lua_mib']:14.2f} | {lua_delta:+11.2f} MiB| < +2.0 MiB")
    print("========================================================")

    # Acceptance check
    failures = []
    if p3_m["entries_per_page"] != 14:
        failures.append(f"Entries per page changed: expected 14, got {p3_m['entries_per_page']}")
    if lua_delta >= 2.0:
        failures.append(f"Navbar added >= 2.0 MiB live Lua: {lua_delta:+.2f} MiB")
    if smoke_status != "PASS":
        failures.append(f"Smoke validation failed: status {smoke_status}")

    if failures:
        print("\n[ACCEPTANCE FAILED]:")
        for f in failures:
            print(" -", f)
        sys.exit(1)
    else:
        print("\n[ACCEPTANCE PASS]: Phase 3 bottom navbar overhead passed all acceptance criteria.")


if __name__ == "__main__":
    main()
