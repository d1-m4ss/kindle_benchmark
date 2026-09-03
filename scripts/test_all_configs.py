#!/usr/bin/env python3
"""
Test runner to verify all 10 configurations start and run properly with the benchmark plugin.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KOREADER_DIR = ROOT / "koreader_src" / "koreader-emulator-arm64-apple-darwin27.0.0-debug" / "koreader"
PLUGINS_SRC = ROOT / "plugins_source"
ENV_DIR = ROOT / "env_test_configs"

CONFIGS = {
    "A_stock": [],
    "B_bookshelf": ["bookshelf"],
    "C_simpleui": ["simpleui"],
    "D_zenos": ["zenos"],
    "E_project_title": ["project_title"],
    "F_bookshelf_bookends": ["bookshelf", "bookends"],
    "G_simpleui_bookshelf_bookends": ["simpleui", "bookshelf", "bookends"],
    "H_zenos_bookshelf_bookends": ["zenos", "bookshelf", "bookends"],
    "I_simpleui_vos": ["simpleui", "vos"],
    "J_project_title_vos": ["project_title", "vos"],
}

PLUGIN_DIRS = {
    "bookshelf": "bookshelf.koplugin",
    "simpleui": "simpleui.koplugin",
    "zenos": "zenos.koplugin",
    "bookends": "bookends.koplugin",
    "project_title": "projecttitle.koplugin",
    "vos": "vos.koplugin",
}


def setup_config_env(cfg_name: str, plugins: list) -> Path:
    cfg_dir = ENV_DIR / cfg_name
    plugins_dir = cfg_dir / "plugins"
    if cfg_dir.exists():
        shutil.rmtree(cfg_dir)
    plugins_dir.mkdir(parents=True, exist_ok=True)

    # Always link benchmark plugin
    (plugins_dir / "benchmark.koplugin").symlink_to(PLUGINS_SRC / "benchmark")

    for p in plugins:
        target_name = PLUGIN_DIRS[p]
        src_path = PLUGINS_SRC / p
        (plugins_dir / target_name).symlink_to(src_path)

    return cfg_dir


def test_config(cfg_name: str, plugins: list):
    print(f"\n==========================================")
    print(f"Testing Config: {cfg_name} (Plugins: {plugins})")
    print(f"==========================================")

    cfg_dir = setup_config_env(cfg_name, plugins)
    out_file = cfg_dir / "test_result.json"
    lib_path = ROOT / "libraries" / "books_50"

    is_darwin = sys.platform == "darwin"
    env = os.environ.copy()
    env["KO_HOME"] = str(cfg_dir)
    env["EMULATE_READER_W"] = "618" if is_darwin else "1236"
    env["EMULATE_READER_H"] = "824" if is_darwin else "1648"
    env["EMULATE_READER_DPI"] = "300"
    env["EMULATE_BW_SCREEN"] = "1"
    env["BENCHMARK_ENABLE"] = "1"
    env["BENCHMARK_CONFIG"] = cfg_name
    env["BENCHMARK_MODE"] = "warm"
    env["BENCHMARK_LIBRARY_DIR"] = str(lib_path)
    env["BENCHMARK_OUTPUT_FILE"] = str(out_file)
    env["BENCHMARK_WARMUP_COUNT"] = "1"
    env["BENCHMARK_MEASURE_COUNT"] = "2"
    env["BENCHMARK_BOOK_COUNT"] = "50"

    cmd = ["./luajit", "reader.lua", str(lib_path)]
    p = subprocess.run(cmd, cwd=str(KOREADER_DIR), env=env, capture_output=True, text=True)

    if p.returncode != 0:
        print(f"FAILED (code {p.returncode})")
        print("STDERR:")
        print(p.stderr[-1000:] if len(p.stderr) > 1000 else p.stderr)
        return False
    else:
        print("SUCCESS! Output JSON exists:", out_file.exists())
        return True


if __name__ == "__main__":
    results = {}
    for name, plugins in CONFIGS.items():
        ok = test_config(name, plugins)
        results[name] = ok

    print("\n\n================ SUMMARY ================")
    for k, v in results.items():
        print(f"Config {k}: {'PASS' if v else 'FAIL'}")
