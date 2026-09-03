#!/usr/bin/env python3
"""
Benchmark ablation runner for LeanUI Phase 2 (L0, L1, L2, L3).
Tests:
- L0: Stock KOReader baseline (Stock 10 items)
- L1: Dense layout only (14 items/page, cache OFF, scoped redraw OFF)
- L2: Dense layout + in-memory item cache (14 items/page, cache ON, scoped redraw OFF)
- L3: Dense layout + in-memory item cache + scoped redraw (14 items/page, cache ON, scoped redraw ON)
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

RUN_BASE = ROOT / "env_benchmark_runs" / "leanui_phase2_ablations"


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


def setup_env(run_id: str, library_dir: Path, leanui_config: dict | None, disable_coverbrowser: bool = False):
    home_dir = RUN_BASE / run_id
    if home_dir.exists():
        shutil.rmtree(home_dir)
    plugins_dir = home_dir / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)

    # Link benchmark plugin
    (plugins_dir / "benchmark.koplugin").symlink_to(BENCHMARK_PLUGIN)

    # If leanui_config is given, link LeanUI plugin
    if leanui_config is not None:
        (plugins_dir / "leanui.koplugin").symlink_to(LEANUI_SRC)

    plugins_disabled_clause = '    ["plugins_disabled"] = { ["coverbrowser"] = true },' if disable_coverbrowser else '    ["plugins_disabled"] = {},'

    settings_content = [
        'return {',
        f'    ["home_dir"] = "{library_dir}",',
        f'    ["lastdir"] = "{library_dir}",',
        plugins_disabled_clause,
    ]

    if leanui_config:
        settings_content.append('    ["leanui_settings"] = {')
        for k, v in leanui_config.items():
            if isinstance(v, bool):
                val_str = "true" if v else "false"
            elif isinstance(v, (int, float)):
                val_str = str(v)
            else:
                val_str = f'"{v}"'
            settings_content.append(f'        ["{k}"] = {val_str},')
        settings_content.append('    },')

    settings_content.append('}\n')

    settings_file = home_dir / "settings.reader.lua"
    settings_file.write_text("\n".join(settings_content))

    targets_file = home_dir / "benchmark_targets.json"
    write_targets(library_dir, targets_file)
    return home_dir, targets_file


def run_cell(run_id: str, library_dir: Path, leanui_config: dict | None, disable_coverbrowser: bool = False, profile: str = "synthetic", warmup: int = 1, measure: int = 2):
    home_dir, targets_file = setup_env(run_id, library_dir, leanui_config, disable_coverbrowser=disable_coverbrowser)
    out_file = home_dir / f"{run_id}_results.json"
    screenshot_dir = home_dir / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    is_darwin = sys.platform == "darwin"
    env = os.environ.copy()
    env.pop("EMULATE_READER_FLASH", None)
    expected_plugins = "leanui" if leanui_config is not None else ""

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
        "BENCHMARK_LIBRARY_DIR": str(library_dir),
        "BENCHMARK_OUTPUT_FILE": str(out_file),
        "BENCHMARK_WARMUP_COUNT": str(warmup),
        "BENCHMARK_MEASURE_COUNT": str(measure),
        "BENCHMARK_BOOK_COUNT": "50",
        "BENCHMARK_DATASET_MODE": "flat",
        "BENCHMARK_EXPECTED_PLUGINS": expected_plugins,
        "BENCHMARK_RUN_OVERHEAD": "1",
        "BENCHMARK_OVERHEAD_COUNT": "30",
        "BENCHMARK_TARGETS_FILE": str(targets_file),
        "BENCHMARK_SCREENSHOT_DIR": str(screenshot_dir),
    })

    cmd = ["./luajit", "reader.lua", str(library_dir)]
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

    # Inspect visible items count from cached paging or first render
    cached_iter = scenarios.get("library_cached_paging", {}).get("iterations", [])
    entries_per_page = 0
    if cached_iter and "visible_count_after" in cached_iter[0]:
        entries_per_page = cached_iter[0]["visible_count_after"]
    elif "library_first_render" in scenarios:
        entries_per_page = scenarios["library_first_render"].get("semantic_evidence", {}).get("visible_count_after", 0)

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
    print("LeanUI Phase 2: Ablation Benchmark (L0 -> L1 -> L2 -> L3)")
    print("==================================================")

    leanui_sha, leanui_dirty = get_git_info(LEANUI_SRC)
    print(f"LeanUI Source: {LEANUI_SRC}")
    print(f"LeanUI Commit: {leanui_sha} {'(DIRTY)' if leanui_dirty else '(CLEAN)'}")

    lib_flat50 = ROOT / "libraries" / "flat" / "books_50"

    modes = {
        "L0_stock_passthrough": {
            "config": None,
            "disable_cb": False,
            "desc": "Stock KOReader baseline (10 items/page)"
        },
        "L1_dense_layout_nocache": {
            "config": {
                "enabled": True,
                "library_mode": "dense",
                "items_per_page_portrait": 14,
                "cache_enabled": False,
                "scoped_redraw": False,
            },
            "disable_cb": True,
            "desc": "Dense layout only (14 items, cache OFF, full redraw)"
        },
        "L2_dense_layout_ramcache": {
            "config": {
                "enabled": True,
                "library_mode": "dense",
                "items_per_page_portrait": 14,
                "cache_enabled": True,
                "scoped_redraw": False,
            },
            "disable_cb": True,
            "desc": "Dense layout + RAM cache (14 items, cache ON, full redraw)"
        },
        "L3_dense_layout_scoped_redraw": {
            "config": {
                "enabled": True,
                "library_mode": "dense",
                "items_per_page_portrait": 14,
                "cache_enabled": True,
                "scoped_redraw": True,
            },
            "disable_cb": True,
            "desc": "Dense layout + RAM cache + Scoped redraw"
        },
    }

    results = {}

    for mode_key, mode_info in modes.items():
        print(f"\n--- Running {mode_key}: {mode_info['desc']} ---")
        raw = run_cell(mode_key, lib_flat50, mode_info["config"], disable_coverbrowser=mode_info["disable_cb"], profile="synthetic")
        if not raw:
            print(f"[FATAL] Mode {mode_key} failed to produce results!")
            sys.exit(1)
        m = extract_metrics(raw)
        results[mode_key] = m
        print(f"  Result: {m['status']} | {m['entries_per_page']} entries/page | render: {m['render_ms']:.2f}ms | seq: {m['seq_ms']:.2f}ms | cached: {m['cached_ms']:.2f}ms | Lua: {m['stress_lua_mib']:.2f}MiB")

    print("\n=================== ABLATION RESULTS ===================")
    print("Mode                          | Entries | Render ms | Seq ms  | Cached ms | Stress Lua | Status")
    print("------------------------------+---------+-----------+---------+-----------+------------+-------")
    for k, m in results.items():
        print(f"{k:29} | {m['entries_per_page']:7d} | {m['render_ms']:9.2f} | {m['seq_ms']:7.2f} | {m['cached_ms']:9.2f} | {m['stress_lua_mib']:9.2f}  | {m['status']}")
    print("========================================================")


if __name__ == "__main__":
    main()
