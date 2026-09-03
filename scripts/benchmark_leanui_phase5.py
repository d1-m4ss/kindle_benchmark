#!/usr/bin/env python3
"""
Benchmark comparison for LeanUI Phase 5: Top Status Bar & Visual Polish.
Compares:
- Phase 4 baseline: Dense 14 rows + Bottom Navbar
- Phase 5: Dense 14 rows + Bottom Navbar + Unified Topbar + Visual Badges
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

RUN_BASE = ROOT / "env_benchmark_runs" / "leanui_phase5_validation"
LIB_DIR = ROOT / "libraries" / "flat" / "books_50"


def get_git_info(repo_path: Path):
    if not (repo_path / ".git").exists():
        return "not_a_git_repo", False
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_path, text=True).strip()
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path, text=True).strip()
    return sha, len(status) > 0


def setup_env(run_id: str, enable_topbar: bool, badges: str = "on"):
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
        f'        ["topbar_enabled"] = {"true" if enable_topbar else "false"},',
        f'        ["badges"] = "{badges}",',
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


def run_cell(run_id: str, enable_topbar: bool, badges: str = "on", profile: str = "synthetic", warmup: int = 1, measure: int = 2):
    home_dir, targets_file = setup_env(run_id, enable_topbar, badges)
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
    p = subprocess.run(cmd, cwd=str(KOREADER_DIR), env=env, capture_output=True, text=True)
    if p.returncode != 0:
        print(f"[{run_id}] FAILED (code {p.returncode})")
        print("STDERR tail:\n", p.stderr[-1000:])
        return None

    if not out_file.exists():
        print(f"[{run_id}] FAILED: output file {out_file} not found")
        return None

    return json.loads(out_file.read_text())


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
    print("LeanUI Phase 5: Top Status Bar & Polish Benchmark")
    print("==================================================")

    leanui_sha, leanui_dirty = get_git_info(LEANUI_SRC)
    print(f"LeanUI Source: {LEANUI_SRC}")
    print(f"LeanUI Commit: {leanui_sha} {'(DIRTY)' if leanui_dirty else '(CLEAN)'}")

    # 1. Phase 4 baseline (Topbar OFF)
    print("\n--- Running Phase 4 Baseline (Dense 14 rows, Bottom Nav, Topbar OFF) ---")
    p4_raw = run_cell("P4_baseline", enable_topbar=False, profile="synthetic")
    if not p4_raw:
        sys.exit(1)
    p4_m = extract_metrics(p4_raw)
    print(f"  Result: {p4_m['status']} | {p4_m['entries_per_page']} entries | render: {p4_m['render_ms']:.2f}ms | seq: {p4_m['seq_ms']:.2f}ms | cached: {p4_m['cached_ms']:.2f}ms | Lua: {p4_m['stress_lua_mib']:.2f}MiB")

    # 2. Phase 5 (Topbar ON + Badges ON)
    print("\n--- Running Phase 5 (Dense 14 rows, Bottom Nav, Topbar ON, Badges ON) ---")
    p5_raw = run_cell("P5_full_polish", enable_topbar=True, badges="on", profile="synthetic")
    if not p5_raw:
        sys.exit(1)
    p5_m = extract_metrics(p5_raw)
    print(f"  Result: {p5_m['status']} | {p5_m['entries_per_page']} entries | render: {p5_m['render_ms']:.2f}ms | seq: {p5_m['seq_ms']:.2f}ms | cached: {p5_m['cached_ms']:.2f}ms | Lua: {p5_m['stress_lua_mib']:.2f}MiB")

    # 3. Smoke validation profile for Phase 5
    print("\n--- Running Smoke Validation for Phase 5 ---")
    p5_smoke = run_cell("P5_full_polish", enable_topbar=True, badges="on", profile="smoke_validation")
    smoke_status = p5_smoke.get("run_status", "UNKNOWN") if p5_smoke else "FAILED"
    print(f"  Smoke Status: {smoke_status}")

    render_delta = p5_m["render_ms"] - p4_m["render_ms"]
    seq_delta = p5_m["seq_ms"] - p4_m["seq_ms"]
    cached_delta = p5_m["cached_ms"] - p4_m["cached_ms"]
    lua_delta = p5_m["stress_lua_mib"] - p4_m["stress_lua_mib"]

    print("\n================== PHASE 5 COMPARISON ==================")
    print("Metric                 | Phase 4 (Baseline)| Phase 5 (Full) | Delta         | Gate Budget")
    print("-----------------------+-------------------+----------------+---------------+------------")
    print(f"Entries per page       | {p4_m['entries_per_page']:17d} | {p5_m['entries_per_page']:14d} | {p5_m['entries_per_page']-p4_m['entries_per_page']:+13d} | Equal (14)")
    print(f"First Render ms        | {p4_m['render_ms']:17.2f} | {p5_m['render_ms']:14.2f} | {render_delta:+11.2f} ms | Near noise")
    print(f"Sequential Paging ms   | {p4_m['seq_ms']:17.2f} | {p5_m['seq_ms']:14.2f} | {seq_delta:+11.2f} ms | Near noise")
    print(f"Cached Paging ms       | {p4_m['cached_ms']:17.2f} | {p5_m['cached_ms']:14.2f} | {cached_delta:+11.2f} ms | Near noise")
    print(f"Stress Live Lua MiB    | {p4_m['stress_lua_mib']:17.2f} | {p5_m['stress_lua_mib']:14.2f} | {lua_delta:+11.2f} MiB| < +2.0 MiB")
    print("========================================================")

    failures = []
    if p5_m["entries_per_page"] != 14:
        failures.append(f"Entries per page changed: expected 14, got {p5_m['entries_per_page']}")
    if lua_delta >= 2.0:
        failures.append(f"Phase 5 added >= 2.0 MiB live Lua: {lua_delta:+.2f} MiB")
    if smoke_status != "PASS":
        failures.append(f"Smoke validation failed: status {smoke_status}")

    if failures:
        print("\n[ACCEPTANCE FAILED]:")
        for f in failures:
            print(" -", f)
        sys.exit(1)
    else:
        print("\n[ACCEPTANCE PASS]: Phase 5 top status bar & visual polish passed all acceptance criteria.")


if __name__ == "__main__":
    main()
