#!/usr/bin/env python3
"""
Records exact system environment and git versions for KOReader and all plugins.
"""

import json
import os
import platform
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def get_git_info(repo_path: Path):
    if not repo_path.exists():
        return {"error": "path does not exist"}
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(repo_path), text=True
        ).strip()
        date = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=iso"], cwd=str(repo_path), text=True
        ).strip()
        try:
            tag = subprocess.check_output(
                ["git", "describe", "--tags", "--always"], cwd=str(repo_path), text=True
            ).strip()
        except Exception:
            tag = "unknown"
        return {"commit": commit, "date": date, "tag": tag}
    except Exception as e:
        return {"error": str(e)}


def record_metadata():
    # 1. Environment info
    env_info = {
        "os": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "target_emulation": {
            "device": "Amazon Kindle Paperwhite 11th Gen (PW5 - 2021)",
            "screen_width": 1236,
            "screen_height": 1648,
            "screen_dpi": 300,
            "screen_type": "Grayscale E-Ink (300 DPI Carta 1200)",
            "total_pixels": 1236 * 1648,
        }
    }

    # Host specific details (macOS sysctl)
    if platform.system() == "Darwin":
        try:
            cpu_brand = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], text=True).strip()
            ncpu = int(subprocess.check_output(["sysctl", "-n", "hw.ncpu"], text=True).strip())
            memsize = int(subprocess.check_output(["sysctl", "-n", "hw.memsize"], text=True).strip())
            env_info["host_hardware"] = {
                "cpu_model": cpu_brand,
                "cpu_cores": ncpu,
                "ram_bytes": memsize,
                "ram_gb": round(memsize / (1024**3), 2),
            }
        except Exception as e:
            env_info["host_hardware_error"] = str(e)

    # 2. Versions info
    versions_info = {
        "koreader": get_git_info(ROOT / "koreader_src"),
        "koreader_base": get_git_info(ROOT / "koreader_src" / "base"),
        "plugins": {
            "simpleui": get_git_info(ROOT / "plugins_source" / "simpleui"),
            "zenos": get_git_info(ROOT / "plugins_source" / "zenos"),
            "bookshelf": get_git_info(ROOT / "plugins_source" / "bookshelf"),
            "bookends": get_git_info(ROOT / "plugins_source" / "bookends"),
            "project_title": get_git_info(ROOT / "plugins_source" / "project_title"),
            "vos": get_git_info(ROOT / "plugins_source" / "vos"),
            "benchmark": get_git_info(ROOT),
        }
    }

    with open(RESULTS_DIR / "environment.json", "w") as f:
        json.dump(env_info, f, indent=2)
    print("Saved results/environment.json")

    with open(RESULTS_DIR / "versions.json", "w") as f:
        json.dump(versions_info, f, indent=2)
    print("Saved results/versions.json")


if __name__ == "__main__":
    record_metadata()
