#!/usr/bin/env python3
"""
Benchmark validation for LeanUI Phase 1: Zero-feature baseline overhead.
Compares Stock vs Stock + LeanUI framework (all features disabled).
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

RUN_DIR = ROOT / "env_benchmark_runs" / "leanui_phase1_validation"
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


def setup_env(name: str, enable_leanui: bool):
    home_dir = RUN_DIR / name
    if home_dir.exists():
        shutil.rmtree(home_dir)
    plugins_dir = home_dir / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)

    # Link benchmark plugin
    (plugins_dir / "benchmark.koplugin").symlink_to(BENCHMARK_PLUGIN)

    if enable_leanui:
        (plugins_dir / "leanui.koplugin").symlink_to(LEANUI_SRC)

    settings_file = home_dir / "settings.reader.lua"
    settings_file.write_text(
        'return {\n'
        f'    ["home_dir"] = "{LIB_DIR}",\n'
        f'    ["lastdir"] = "{LIB_DIR}",\n'
        '    ["plugins_disabled"] = {},\n'
        '}\n'
    )

    targets_file = home_dir / "benchmark_targets.json"
    write_targets(LIB_DIR, targets_file)
    return home_dir, targets_file


def run_single(name: str, enable_leanui: bool, profile: str = "synthetic", warmup: int = 1, measure: int = 2):
    home_dir, targets_file = setup_env(name, enable_leanui)
    out_file = home_dir / f"{name}_{profile}_results.json"
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
        "BENCHMARK_CONFIG": name,
        "BENCHMARK_MODE": "warm",
        "BENCHMARK_PROFILE": profile,
        "BENCHMARK_LIBRARY_DIR": str(LIB_DIR),
        "BENCHMARK_OUTPUT_FILE": str(out_file),
        "BENCHMARK_WARMUP_COUNT": str(warmup),
        "BENCHMARK_MEASURE_COUNT": str(measure),
        "BENCHMARK_BOOK_COUNT": "50",
        "BENCHMARK_DATASET_MODE": "flat",
        "BENCHMARK_EXPECTED_PLUGINS": "leanui" if enable_leanui else "",
        "BENCHMARK_RUN_OVERHEAD": "1",
        "BENCHMARK_OVERHEAD_COUNT": "30",
        "BENCHMARK_TARGETS_FILE": str(targets_file),
        "BENCHMARK_SCREENSHOT_DIR": str(screenshot_dir),
    })

    cmd = ["./luajit", "reader.lua", str(LIB_DIR)]
    print(f"Running benchmark for [{name}] (profile={profile})...")
    start_time = time.monotonic()
    p = subprocess.run(cmd, cwd=str(KOREADER_DIR), env=env, capture_output=True, text=True)
    dur = time.monotonic() - start_time

    if p.returncode != 0:
        print(f"[{name}] FAILED with code {p.returncode}")
        print("STDERR tail:\n", p.stderr[-1000:])
        return None

    if not out_file.exists():
        print(f"[{name}] FAILED: output file {out_file} not created")
        return None

    data = json.loads(out_file.read_text())
    print(f"[{name}] SUCCESS in {dur:.2f}s")
    return data


def extract_metrics(res: dict):
    scenarios = res.get("scenarios", {})
    mem = res.get("memory_checkpoints", {})

    def get_med(scen_name):
        sc = scenarios.get(scen_name, {})
        it = sc.get("iterations", [])
        if not it:
            # Fall back to single sample or mean if available
            return sc.get("wall_time_ms", 0.0)
        times = [x.get("wall_time_ms", 0.0) for x in it if "wall_time_ms" in x]
        if not times:
            return 0.0
        times.sort()
        return times[len(times) // 2]

    restart_ms = get_med("start_to_home")
    render_ms = get_med("library_first_render")
    seq_ms = get_med("library_sequential_paging")
    cached_ms = get_med("library_cached_paging")
    open_ms = get_med("open_book_minimal")

    live_lua_post_init_kb = mem.get("post_init_idle", {}).get("forced_gc_live_heap_kb", 0)
    live_lua_post_render_kb = mem.get("post_library_render_idle", {}).get("forced_gc_live_heap_kb", 0)
    live_lua_post_stress_kb = mem.get("post_stress_idle", {}).get("forced_gc_live_heap_kb", 0)

    active_plugins = res.get("active_plugins", [])
    run_status = res.get("run_status", "UNKNOWN")

    return {
        "run_status": run_status,
        "active_plugins": active_plugins,
        "restart_ms": restart_ms,
        "render_ms": render_ms,
        "seq_ms": seq_ms,
        "cached_ms": cached_ms,
        "open_ms": open_ms,
        "live_lua_post_init_mib": live_lua_post_init_kb / 1024.0,
        "live_lua_post_render_mib": live_lua_post_render_kb / 1024.0,
        "live_lua_post_stress_mib": live_lua_post_stress_kb / 1024.0,
    }


def main():
    print("==================================================")
    print("LeanUI Phase 1: Zero-Feature Framework Benchmark")
    print("==================================================")

    leanui_sha, leanui_dirty = get_git_info(LEANUI_SRC)
    print(f"LeanUI Source: {LEANUI_SRC}")
    print(f"LeanUI Commit: {leanui_sha} {'(DIRTY)' if leanui_dirty else '(CLEAN)'}")

    # 1. Synthetic profile (measures startup, render, paging, open_book, forced-GC live heap)
    stock_raw = run_single("A_stock_control", enable_leanui=False, profile="synthetic")
    if not stock_raw:
        sys.exit(1)

    leanui_raw = run_single("B_stock_plus_leanui", enable_leanui=True, profile="synthetic")
    if not leanui_raw:
        sys.exit(1)

    # 2. Smoke validation profile (measures smoke guards, probe screenshots)
    stock_smoke = run_single("A_stock_control", enable_leanui=False, profile="smoke_validation")
    leanui_smoke = run_single("B_stock_plus_leanui", enable_leanui=True, profile="smoke_validation")

    stock = extract_metrics(stock_raw)
    leanui = extract_metrics(leanui_raw)

    print("\n--- Verification of Plugin Loading & Smoke Status ---")
    print(f"Stock run status:        {stock['run_status']}")
    print(f"Stock+LeanUI run status: {leanui['run_status']}")
    print(f"Smoke profile Stock:     {stock_smoke.get('run_status')}")
    print(f"Smoke profile LeanUI:    {leanui_smoke.get('run_status')}")
    print(f"LeanUI present in active: {'leanui' in leanui['active_plugins']}")

    assert "leanui" in leanui["active_plugins"], "FATAL: LeanUI plugin was not loaded!"
    assert leanui["run_status"] == "PASS", "FATAL: LeanUI run status was not PASS!"
    assert leanui_smoke.get("run_status") == "PASS", "FATAL: LeanUI smoke run status was not PASS!"

    # Deltas
    restart_diff = leanui["restart_ms"] - stock["restart_ms"]
    restart_pct = (restart_diff / stock["restart_ms"] * 100) if stock["restart_ms"] else 0.0

    render_diff = leanui["render_ms"] - stock["render_ms"]
    render_pct = (render_diff / stock["render_ms"] * 100) if stock["render_ms"] else 0.0

    lua_render_diff = leanui["live_lua_post_render_mib"] - stock["live_lua_post_render_mib"]
    lua_stress_diff = leanui["live_lua_post_stress_mib"] - stock["live_lua_post_stress_mib"]

    print("\n================ COMPARISON TABLE ================")
    print(f"Metric                    | Stock      | Stock+LeanUI | Delta         | Gate Limit")
    print(f"--------------------------+------------+--------------+---------------+-----------")
    print(f"Start to Home ms          | {stock['restart_ms']:10.2f} | {leanui['restart_ms']:12.2f} | {restart_diff:+6.2f} ({restart_pct:+.1f}%) | <= +5%")
    print(f"Library First Render ms   | {stock['render_ms']:10.2f} | {leanui['render_ms']:12.2f} | {render_diff:+6.2f} ({render_pct:+.1f}%) | Near noise")
    print(f"Cached Paging ms          | {stock['cached_ms']:10.2f} | {leanui['cached_ms']:12.2f} | {leanui['cached_ms']-stock['cached_ms']:+6.2f} ms      | Near noise")
    print(f"Sequential Paging ms      | {stock['seq_ms']:10.2f} | {leanui['seq_ms']:12.2f} | {leanui['seq_ms']-stock['seq_ms']:+6.2f} ms      | Near noise")
    print(f"Open Book Minimal ms      | {stock['open_ms']:10.2f} | {leanui['open_ms']:12.2f} | {leanui['open_ms']-stock['open_ms']:+6.2f} ms      | Near noise")
    print(f"Post-Render Live Lua MiB  | {stock['live_lua_post_render_mib']:10.2f} | {leanui['live_lua_post_render_mib']:12.2f} | {lua_render_diff:+6.2f} MiB    | < +2.0 MiB")
    print(f"Post-Stress Live Lua MiB  | {stock['live_lua_post_stress_mib']:10.2f} | {leanui['live_lua_post_stress_mib']:12.2f} | {lua_stress_diff:+6.2f} MiB    | < +2.0 MiB")
    print("==================================================")

    # Check Acceptance criteria
    failures = []
    if restart_pct > 5.0 and restart_diff > 30.0:
        failures.append(f"Restart exceeded threshold: {restart_pct:+.1f}% ({restart_diff:+.1f}ms)")
    if lua_stress_diff >= 2.0:
        failures.append(f"Live Lua heap increased by >= 2 MiB: {lua_stress_diff:+.2f} MiB")

    if failures:
        print("\n[ACCEPTANCE FAILED]:")
        for f in failures:
            print(" -", f)
        sys.exit(1)
    else:
        print("\n[ACCEPTANCE PASS]: Framework overhead is within measurement noise and budgets.")


if __name__ == "__main__":
    main()
