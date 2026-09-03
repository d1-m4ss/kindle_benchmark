#!/usr/bin/env python3
"""Checkpointed orchestrator for the compact KOReader benchmark.

Long measurements are always explicit and sequential. A campaign is stored at
results/runs/<YYYY-MM-DD>/<phase>/ and can be resumed on another day by passing
the same --campaign value.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import queue
import re
import shutil
import statistics
import struct
import subprocess
import sys
import threading
import time
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, replace
from datetime import date, datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
KOREADER_DIR = ROOT / "koreader_src" / "koreader-emulator-arm64-apple-darwin27.0.0-debug" / "koreader"
PLUGINS_SRC = ROOT / "plugins_source"
ENV_BASE = ROOT / "env_benchmark_runs"
WORK_REAL = ROOT / "work_real"
RUNS_ROOT = ROOT / "results" / "runs"
SEED = 20260831
# A library root must supply at least this many books before the paging harness
# will page through it directly. 30 sequential transitions need 31 pages, and
# the coarsest layout (Project:Title) shows 13 books plus ".." per page.
PAGING_MIN_ROOT_BOOKS = 403
SCHEMA_VERSION = 2

# versions.lock.json is the single source of truth for pinned revisions and
# plugin naming. setup.sh reads the same file, so a version bump is a one-file
# edit and nothing here has to be kept in sync by hand.
VERSIONS_LOCK = ROOT / "versions.lock.json"


def load_versions_lock() -> dict:
    try:
        lock = json.loads(VERSIONS_LOCK.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"HARD FAIL: cannot read {VERSIONS_LOCK}: {exc}") from exc
    if "koreader" not in lock or not lock.get("plugins"):
        raise RuntimeError(f"HARD FAIL: {VERSIONS_LOCK} is missing 'koreader' or 'plugins'")
    required = ("checkout_path", "commit", "tag", "plugin_dir", "loaded_name")
    for name, info in lock["plugins"].items():
        missing = [key for key in required if not info.get(key)]
        if missing:
            raise RuntimeError(f"HARD FAIL: plugin {name} in {VERSIONS_LOCK} is missing {missing}")
    if not lock["koreader"].get("checkout_path") or not lock["koreader"].get("commit"):
        raise RuntimeError(f"HARD FAIL: koreader entry in {VERSIONS_LOCK} is incomplete")
    return lock


VERSIONS = load_versions_lock()
PINNED_REVISIONS = {
    "koreader": (VERSIONS["koreader"]["checkout_path"], VERSIONS["koreader"]["commit"]),
    **{
        name: (info["checkout_path"], info["commit"])
        for name, info in VERSIONS["plugins"].items()
    },
}
PINNED_TAGS = {
    "koreader": VERSIONS["koreader"]["tag"],
    **{name: info["tag"] for name, info in VERSIONS["plugins"].items()},
}


def verify_pinned_revisions() -> None:
    for name, (rel_path, expected_sha) in PINNED_REVISIONS.items():
        repo_path = ROOT / rel_path
        if not repo_path.exists():
            raise RuntimeError(f"HARD FAIL: Repo path not found for {name}: {repo_path}")
        actual_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(repo_path), text=True
        ).strip()
        if actual_sha != expected_sha:
            raise RuntimeError(
                f"HARD FAIL: Revision mismatch for {name} (pinned {PINNED_TAGS.get(name, '?')})! "
                f"Expected SHA: {expected_sha}, Actual: {actual_sha}. "
                f"Run ./setup.sh to check out the revisions from versions.lock.json."
            )


PHASE1_CONFIGS = OrderedDict({
    "A_stock": [],
    "B_bookshelf": ["bookshelf"],
    "C_simpleui": ["simpleui"],
    "D_zenos": ["zenos"],
    "E_project_title": ["project_title"],
    "F_vos": ["vos"],
    "G_simpleui_bookshelf": ["simpleui", "bookshelf"],
    "H_zenos_bookshelf": ["zenos", "bookshelf"],
    "I_vos_bookshelf": ["vos", "bookshelf"],
    "J_simpleui_vos": ["simpleui", "vos"],
    "K_simpleui_vos_bookshelf": ["simpleui", "vos", "bookshelf"],
    "L_project_title_vos": ["project_title", "vos"],
})
PHASE2_CONFIGS = OrderedDict({
    "R0_stock": [],
    "R1_bookshelf": ["bookshelf"],
    "R2_simpleui": ["simpleui"],
    "R3_zenos": ["zenos"],
    "R4_project_title": ["project_title"],
    "R5_vos": ["vos"],
    "R6_simpleui_bookshelf": ["simpleui", "bookshelf"],
    "R7_zenos_bookshelf": ["zenos", "bookshelf"],
    "R8_vos_bookshelf": ["vos", "bookshelf"],
    "R9_simpleui_vos": ["simpleui", "vos"],
    "R10_simpleui_vos_bookshelf": ["simpleui", "vos", "bookshelf"],
    "R11_project_title_vos": ["project_title", "vos"],
})
PLUGIN_DIRS = {name: info["plugin_dir"] for name, info in VERSIONS["plugins"].items()}
LOADED_PLUGIN_NAMES = {name: info["loaded_name"] for name, info in VERSIONS["plugins"].items()}

BASE_SCENARIOS = {
    "start_to_home", "home_to_library", "library_first_render",
    "library_sequential_paging", "library_cached_paging", "change_sort_mode",
    "open_book_minimal", "open_book", "close_book",
}
NORMAL_EXTRA_SCENARIOS = {"open_quick_settings", "close_quick_settings", "repeated_nav"}
FOLDER_SCENARIOS = {"library_folder_enter", "library_folder_back"}
BOOKSHELF_SCENARIOS = {
    "open_bookshelf", "bookshelf_first_render",
    "bookshelf_sequential_paging", "bookshelf_cached_paging",
    "bookshelf_sequential_paging_anim_off", "bookshelf_cached_paging_anim_off",
    "close_bookshelf",
}
ALLOWED_SCENARIO_STATUSES = {"PASS", "FAILED", "UNSUPPORTED"}


@dataclass(frozen=True)
class RunLayout:
    campaign: str
    phase: str
    root: Path
    raw: Path
    logs: Path
    checkpoints: Path
    charts: Path
    screenshots: Path
    environment: Path


@dataclass(frozen=True)
class Job:
    run_id: str
    block: str
    phase: str
    config: str
    plugins: tuple[str, ...]
    library_dir: str
    ko_home: str
    mode: str
    profile: str
    dataset_mode: str
    book_count: int
    warmup: int
    measure: int
    fresh_home: bool
    overhead: bool = False
    timeout_s: int = 600
    emulate_reader_flash_ms: int | None = None


def make_layout(campaign: str, phase: str) -> RunLayout:
    root = RUNS_ROOT / campaign / phase
    return RunLayout(
        campaign=campaign,
        phase=phase,
        root=root,
        raw=root / "raw",
        logs=root / "logs",
        checkpoints=root / "checkpoints",
        charts=root / "charts",
        screenshots=root / "screenshots",
        environment=root / "environment.json",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_png_file(path: Path) -> tuple[bool, str | None, int, int]:
    if not path.is_file():
        return False, f"file not found: {path}", 0, 0
    data = path.read_bytes()
    if len(data) < 24:
        return False, f"file too short for PNG ({len(data)} bytes)", 0, 0
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return False, "invalid PNG signature magic bytes", 0, 0
    chunk_type = data[12:16]
    if chunk_type != b"IHDR":
        return False, f"expected IHDR chunk first, got {chunk_type}", 0, 0
    width, height = struct.unpack(">II", data[16:24])
    if width <= 0 or height <= 0:
        return False, f"invalid dimensions ({width}x{height})", width, height
    if (width, height) not in {(618, 824), (1236, 1648)}:
        return False, f"unexpected resolution {width}x{height} (expected 618x824 or 1236x1648)", width, height
    return True, None, width, height


def benchmark_harness_sha256() -> str:
    digest = hashlib.sha256()
    for path in sorted((ROOT / "plugins_source" / "benchmark").glob("*.lua")):
        digest.update(path.name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def atomic_json_write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
    temporary.replace(path)


def ensure_layout(layout: RunLayout, emulate_reader_flash_ms: int | None = None) -> dict:
    for path in (layout.raw, layout.logs, layout.checkpoints, layout.charts, layout.screenshots):
        path.mkdir(parents=True, exist_ok=True)
    lock = ROOT / "versions.lock.json"
    metadata = {
        "campaign": layout.campaign,
        "phase": layout.phase,
        "created_or_verified_utc": datetime.now(timezone.utc).isoformat(),
        "host": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "target": {"width": 1236, "height": 1648, "dpi": 300, "grayscale": True},
        "emulate_reader_flash_ms": emulate_reader_flash_ms,
        "versions_lock_sha256": sha256_file(lock) if lock.exists() else None,
        "runner_sha256": sha256_file(Path(__file__)),
        "benchmark_harness_sha256": benchmark_harness_sha256(),
    }
    campaign_file = layout.root.parent / "campaign.json"
    campaign_identity = {
        "campaign": layout.campaign,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "emulate_reader_flash_ms": emulate_reader_flash_ms,
        "versions_lock_sha256": metadata["versions_lock_sha256"],
        "runner_sha256": metadata["runner_sha256"],
        "benchmark_harness_sha256": metadata["benchmark_harness_sha256"],
    }
    if campaign_file.exists():
        existing_campaign = json.loads(campaign_file.read_text())
        for key in ("campaign", "emulate_reader_flash_ms", "versions_lock_sha256", "runner_sha256", "benchmark_harness_sha256"):
            if existing_campaign.get(key) != campaign_identity.get(key):
                raise RuntimeError(f"campaign identity changed for {key}; start a new campaign")
        campaign_identity = existing_campaign
    atomic_json_write(campaign_file, campaign_identity)

    if layout.environment.exists():
        existing = json.loads(layout.environment.read_text())
        if existing.get("campaign") != layout.campaign or existing.get("phase") != layout.phase:
            raise RuntimeError(f"environment metadata mismatch in {layout.environment}")
        for key in ("emulate_reader_flash_ms", "versions_lock_sha256", "runner_sha256", "benchmark_harness_sha256"):
            if existing.get(key) != metadata.get(key):
                raise RuntimeError(f"campaign code/version changed for {key}; start a new campaign")
        metadata = existing
    atomic_json_write(layout.environment, metadata)
    return metadata


def _safe_remove(path: Path) -> None:
    if path.exists() or path.is_symlink():
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()


def sanitize_working_corpus(path: Path) -> None:
    """Remove KOReader state only from a disposable working clone."""
    if not path.is_dir():
        return
    for candidate in sorted(path.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if candidate.name.endswith(".sdr") or candidate.name.startswith(".koreader"):
            _safe_remove(candidate)


@lru_cache(maxsize=1)
def zenos_plugin_version() -> str:
    """Version string ZenOS compares its quickstart state against."""
    meta = PLUGINS_SRC / "zenos" / "_meta.lua"
    match = re.search(r'version\s*=\s*"([^"]+)"', meta.read_text())
    if not match:
        raise RuntimeError(f"HARD FAIL: cannot read plugin version from {meta}")
    return match.group(1)


def setup_isolated_home(job: Job) -> Path:
    home = Path(job.ko_home)
    if job.fresh_home:
        _safe_remove(home)
    plugins_dir = home / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)
    links = {"benchmark.koplugin": PLUGINS_SRC / "benchmark"}
    links.update({PLUGIN_DIRS[name]: PLUGINS_SRC / name for name in job.plugins})
    for link_name, source in links.items():
        link = plugins_dir / link_name
        if link.is_symlink() and link.resolve() == source.resolve():
            continue
        _safe_remove(link)
        link.symlink_to(source)
    settings_file = home / "settings.reader.lua"
    if not settings_file.exists():
        plugins_disabled_str = '        ["coverbrowser"] = true,\n' if "project_title" in job.plugins else ''
        pt_setup_str = '    ["aaaProjectTitle_initial_default_setup_done2"] = true,\n' if "project_title" in job.plugins else ''
        settings_file.write_text(
            'return {\n'
            f'    ["home_dir"] = "{job.library_dir}",\n'
            f'    ["lastdir"] = "{job.library_dir}",\n'
            '    ["plugins_disabled"] = {\n'
            f'{plugins_disabled_str}'
            '    },\n'
            f'{pt_setup_str}'
            '}\n'
        )
    if "project_title" in job.plugins:
        settings_dir = home / "settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        pt_settings = settings_dir / "project_title.lua"
        if not pt_settings.exists():
            pt_settings.write_text(
                'return {\n'
                '    ["config_version"] = "6",\n'
                '    ["use_custom_sorts"] = true,\n'
                '    ["use_custom_bookstatus"] = true,\n'
                '}\n'
            )
        pt_fonts_src = PLUGINS_SRC / "project_title" / "fonts" / "source"
        pt_fonts_dst = home / "fonts" / "source"
        if pt_fonts_src.exists() and not pt_fonts_dst.exists():
            pt_fonts_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(pt_fonts_src, pt_fonts_dst)
        pt_icons_src = PLUGINS_SRC / "project_title" / "icons"
        pt_icons_dst = home / "icons"
        if pt_icons_src.exists() and not pt_icons_dst.exists():
            shutil.copytree(pt_icons_src, pt_icons_dst)
    if "zenos" in job.plugins:
        # ZenOS shows a full-screen quickstart wizard on a fresh profile, which
        # covers the library and silently occludes every measured page turn.
        # Declare the wizard already shown for the pinned version: a real
        # version string keeps is_incomplete_fresh_config() from resetting it,
        # and matching _meta.lua suppresses the update screen too.
        settings_dir = home / "settings" / "ZenOS"
        settings_dir.mkdir(parents=True, exist_ok=True)
        zen_config = settings_dir / "config.lua"
        if not zen_config.exists():
            zen_config.write_text(
                'return {\n'
                '    ["_meta"] = {\n'
                f'        ["quickstart_shown_for_version"] = "{zenos_plugin_version()}",\n'
                '        ["quickstart_completed"] = true,\n'
                '        ["quickstart_menu_tour_pending"] = false,\n'
                '    },\n'
                '}\n'
            )
    if "bookshelf" in job.plugins or "bookshelf" in job.config.lower():
        settings_dir = home / "settings"
        settings_dir.mkdir(parents=True, exist_ok=True)
        bs_settings = settings_dir / "bookshelf.lua"
        if not bs_settings.exists():
            bs_settings.write_text(
                'return {\n'
                '    ["active_chip"] = "all",\n'
                '    ["active_page"] = 1,\n'
                '    ["active_cursor"] = 1,\n'
                '    ["shelf_page_animation"] = "medium",\n'
                '}\n'
            )
    if "simpleui" in job.plugins or "simpleui" in job.config.lower():
        sui_dir = home / "settings" / "simpleui"
        sui_dir.mkdir(parents=True, exist_ok=True)
        sui_settings = sui_dir / "sui_settings.lua"
        if not sui_settings.exists():
            sui_settings.write_text(
                'return {\n'
                '    ["simpleui_onboarding_done"] = true,\n'
                '    ["simpleui_updater_auto_check"] = false,\n'
                '}\n'
            )
    return home


def write_deterministic_targets(library: Path, output: Path, limit: int = 10) -> None:
    books = sorted(path for path in library.rglob("*") if path.is_file() and path.suffix.lower() == ".epub")
    folders = sorted(
        path for path in library.rglob("*")
        if path.is_dir() and path != library
        and not any(part.startswith(".") for part in path.relative_to(library).parts)
    )

    def choose(paths: list[Path]) -> list[str]:
        ranked = sorted(paths, key=lambda path: hashlib.sha256(
            f"{SEED}:{path.relative_to(library)}".encode()).digest())
        return [str(path) for path in ranked[:limit]]

    # The paging harness needs a listing it can actually page through. Descend
    # into the fullest leaf folder only when the library root cannot supply
    # PAGING_MIN_ROOT_BOOKS, so a root that already paginates (flat synthetic
    # corpora, the restructured real working corpus) is never narrowed.
    leaf_counts: dict[Path, int] = {}
    for book in books:
        leaf_counts[book.parent] = leaf_counts.get(book.parent, 0) + 1
    root_book_count = leaf_counts.get(library, 0)
    leaf_folder = None
    leaf_folder_book_count = 0
    if root_book_count < PAGING_MIN_ROOT_BOOKS:
        candidates = {path: count for path, count in leaf_counts.items() if path != library}
        if candidates:
            chosen = max(
                candidates,
                key=lambda p: (candidates[p], hashlib.sha256(f"{SEED}:{p.relative_to(library)}".encode()).digest()),
            )
            leaf_folder = str(chosen)
            leaf_folder_book_count = candidates[chosen]

    # One fixed document for reader page turns. Rotating books between
    # iterations mixes different documents into a single median, and the corpus
    # spans 59 KB to 29 MB. Pick a book near the median size so the pinned
    # document is representative rather than an outlier.
    reader_book = None
    reader_book_bytes = None
    if books:
        sized = sorted((path.stat().st_size, path) for path in books)
        median_size = sized[len(sized) // 2][0]
        reader_size, reader_path = min(
            sized,
            key=lambda item: (
                abs(item[0] - median_size),
                hashlib.sha256(f"{SEED}:{item[1].relative_to(library)}".encode()).digest(),
            ),
        )
        reader_book = str(reader_path)
        reader_book_bytes = reader_size

    output.write_text(json.dumps(
        {
            "seed": SEED, "books": choose(books), "folders": choose(folders),
            "root_book_count": root_book_count,
            "leaf_folder": leaf_folder, "leaf_folder_book_count": leaf_folder_book_count,
            "paging_min_root_books": PAGING_MIN_ROOT_BOOKS,
            "reader_book": reader_book, "reader_book_bytes": reader_book_bytes,
        },
        ensure_ascii=False, separators=(",", ":"),
    ))


def tree_disk_usage(path: Path) -> dict[str, int]:
    total = 0
    cache_db = 0
    if not path.exists():
        return {"total_bytes": 0, "cache_database_bytes": 0}
    for item in path.rglob("*"):
        if not item.is_file() or item.is_symlink():
            continue
        try:
            size = item.stat().st_size
        except OSError:
            continue
        total += size
        lowered = item.name.lower()
        if item.suffix.lower() in {".db", ".sqlite", ".sqlite3"} or "cache" in lowered:
            cache_db += size
    return {"total_bytes": total, "cache_database_bytes": cache_db}


def expected_scenarios(job: Job) -> set[str]:
    if job.profile == "startup":
        return {"home_to_library", "library_first_render"}
    if job.profile == "paging":
        scenarios = {"library_sequential_paging", "library_cached_paging", "paging_probe_step_2_to_3"}
        if "bookshelf" in job.config.lower():
            scenarios.update({
                "open_bookshelf", "bookshelf_sequential_paging", "bookshelf_cached_paging",
                "bookshelf_sequential_paging_anim_off", "bookshelf_cached_paging_anim_off",
                "close_bookshelf",
            })
        return scenarios
    if job.profile == "smoke_validation":
        scenarios = {"library_sequential_paging", "smoke_probe_step_2_to_3", "library_cached_paging", "smoke_noop_guard"}
        if "bookshelf" in job.config.lower():
            scenarios.update({
                "open_bookshelf", "bookshelf_sequential_paging", "bookshelf_probe_step_2_to_3",
                "bookshelf_cached_paging", "bookshelf_sequential_paging_anim_off",
                "bookshelf_cached_paging_anim_off", "close_bookshelf",
            })
        return scenarios
    scenarios = set(BASE_SCENARIOS)
    if job.profile != "bookends_control":
        scenarios.update(NORMAL_EXTRA_SCENARIOS)
    else:
        scenarios.add("reader_page_turn")
    if job.dataset_mode != "flat":
        scenarios.update(FOLDER_SCENARIOS)
    has_bookshelf = "bookshelf" in job.config.lower()
    if has_bookshelf and job.profile != "startup" and job.mode not in {"first_run_cold", "real_first_run"}:
        scenarios.update(BOOKSHELF_SCENARIOS)
    return scenarios


def expected_paging_root(job: Job) -> tuple[str | None, int]:
    """The leaf folder the runner named for this job, if any."""
    targets_file = Path(job.ko_home) / "benchmark_targets.json"
    if not targets_file.exists():
        return None, 0
    try:
        targets = json.loads(targets_file.read_text())
    except (OSError, json.JSONDecodeError):
        return None, 0
    leaf = targets.get("leaf_folder")
    return (leaf if isinstance(leaf, str) else None), int(targets.get("leaf_folder_book_count") or 0)


def paging_root_errors(job: Job, data: dict) -> list[str]:
    expected_path, expected_books = expected_paging_root(job)
    recorded = data.get("paging_root")
    errors: list[str] = []
    if expected_path is None:
        if isinstance(recorded, dict) and recorded.get("path"):
            errors.append(
                f"paging narrowed to {recorded.get('path')} although the library root paginates on its own"
            )
        return errors
    if not isinstance(recorded, dict):
        errors.append(
            f"paging_root metadata missing although the runner narrowed paging to {expected_path}"
        )
        return errors
    if recorded.get("path") != expected_path:
        errors.append(f"paging_root.path mismatch: raw={recorded.get('path')} expected={expected_path}")
    recorded_books = recorded.get("book_count")
    if not isinstance(recorded_books, (int, float)) or recorded_books <= 0:
        errors.append(f"paging_root.book_count must be > 0, got {recorded_books}")
    elif expected_books and recorded_books != expected_books:
        errors.append(
            f"paging_root.book_count mismatch: raw={recorded_books} expected={expected_books}"
        )
    return errors


def validate_result_artifact(job: Job, layout: RunLayout, *, require_success: bool) -> tuple[bool, list[str]]:
    raw_path = layout.raw / f"{job.run_id}.json"
    log_path = layout.logs / f"{job.run_id}.log"
    errors: list[str] = []
    if not raw_path.exists():
        return False, [f"missing raw JSON: {raw_path}"]
    if not log_path.exists() or log_path.stat().st_size == 0:
        errors.append(f"missing/empty log: {log_path}")
    try:
        data = json.loads(raw_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return False, [f"invalid raw JSON: {exc}"]

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append("wrong schema_version")
    if data.get("run_id") != job.run_id:
        errors.append("run_id mismatch")
    if data.get("process_returncode") != 0:
        errors.append("process did not exit cleanly")
    if job.emulate_reader_flash_ms is not None and data.get("emulate_reader_flash_ms") != job.emulate_reader_flash_ms:
        errors.append(
            f"emulate_reader_flash_ms mismatch: raw={data.get('emulate_reader_flash_ms')} "
            f"expected={job.emulate_reader_flash_ms}"
        )
    if data.get("campaign") != layout.campaign or data.get("output_phase") != layout.phase:
        errors.append("campaign/phase metadata mismatch")
    screen_size = data.get("screen_size")
    if not isinstance(screen_size, dict) or screen_size.get("w") != 1236 or screen_size.get("h") != 1648:
        errors.append(f"framebuffer size mismatch: {screen_size}")
    if data.get("framebuffer_resolution") != "1236x1648":
        errors.append("framebuffer_resolution mismatch")
    if log_path.exists():
        log_text = log_path.read_text(errors="replace")
        if "framebuffer resolution:" in log_text and not ("1236" in log_text and "1648" in log_text):
            errors.append("framebuffer resolution log line mismatch")
    env_meta = data.get("campaign_environment")
    if not isinstance(env_meta, dict) or not env_meta.get("runner_sha256"):
        errors.append("campaign environment metadata missing")
    timing = data.get("external_process_timing", {})
    if not isinstance(timing.get("spawn_to_ui_ready_ms"), (int, float)):
        errors.append("UI READY timing missing")
    if not isinstance(timing.get("spawn_to_library_ready_ms"), (int, float)):
        errors.append("LIBRARY READY timing missing")
    if not isinstance(timing.get("complete_marker_ms"), (int, float)):
        errors.append("COMPLETE marker missing")

    if job.profile in {"paging", "smoke_validation"}:
        # Narrowing paging into a leaf folder measures less than the whole
        # library, so the artifact must agree with what the runner asked for:
        # declared with a positive book count when a leaf was named, and absent
        # when the library root paginates on its own. Neither a silent narrowing
        # nor a silently ignored narrowing may pass.
        errors.extend(paging_root_errors(job, data))

    if job.profile == "bookends_control":
        # Reader page turns are only comparable inside one document, so a
        # silent fallback to the rotating book selection must not pass.
        reader_book = data.get("reader_book")
        if not isinstance(reader_book, dict) or reader_book.get("pinned") is not True:
            errors.append(f"reader page turns were not pinned to one document: {reader_book}")
        elif not reader_book.get("path"):
            errors.append("reader_book.path missing")
        reader_cycles = data.get("bookends_reader_cycles_live_heap_kb")
        if not isinstance(reader_cycles, list) or len(reader_cycles) != 10:
            errors.append(
                "Bookends reader memory control requires exactly 10 forced-GC samples, "
                f"got {len(reader_cycles) if isinstance(reader_cycles, list) else reader_cycles}"
            )
        elif any(
            not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0
            for value in reader_cycles
        ):
            errors.append("Bookends reader memory control contains an invalid forced-GC sample")
        if data.get("bookends_reader_cycles_completed") != 10:
            errors.append(
                "Bookends reader memory control did not complete 10 valid open/turn/close cycles"
            )
        if data.get("bookends_reader_cycle_failures") not in ([], None):
            errors.append(
                f"Bookends reader memory cycle failures: {data.get('bookends_reader_cycle_failures')}"
            )
        reader_stats = data.get("bookends_reader_cycles_stats")
        if not isinstance(reader_stats, dict) or reader_stats.get("count") != 10:
            errors.append("Bookends reader memory statistics are missing or not based on 10 samples")

    scenarios = data.get("scenarios")
    if not isinstance(scenarios, dict):
        errors.append("scenario object missing")
        scenarios = {}

    DEPRECATED_SCENARIOS = {"library_next_page", "library_prev_page", "bookshelf_page_turn"}
    found_deprecated = DEPRECATED_SCENARIOS & set(scenarios)
    if found_deprecated:
        errors.append(f"deprecated scenarios found in results: {sorted(found_deprecated)}")

    PAGING_SCENARIOS = {
        "library_sequential_paging", "library_cached_paging",
        "bookshelf_sequential_paging", "bookshelf_cached_paging",
        "bookshelf_sequential_paging_anim_off", "bookshelf_cached_paging_anim_off",
    }
    missing = sorted(expected_scenarios(job) - set(scenarios))
    if missing:
        errors.append(f"expected scenarios missing: {missing}")
    failed_scenarios = []
    for name, result in scenarios.items():
        status = result.get("status") if isinstance(result, dict) else None
        if status not in ALLOWED_SCENARIO_STATUSES:
            errors.append(f"invalid status for {name}: {status}")
            continue
        if status == "FAILED":
            if not result.get("reason"):
                errors.append(f"FAILED scenario lacks diagnosis: {name}")
            failed_scenarios.append(name)
        elif status == "UNSUPPORTED":
            if not result.get("reason"):
                errors.append(f"UNSUPPORTED scenario lacks reason: {name}")
            if name in PAGING_SCENARIOS and job.profile in {"paging", "smoke_validation"}:
                errors.append(
                    f"measured paging scenario {name} is UNSUPPORTED (zero pages available) — "
                    "the dataset must yield real paging data, not a silent skip"
                )
            continue
        if name == "smoke_noop_guard":
            if status != "PASS" or result.get("attempted_status") != "FAILED":
                errors.append(f"smoke no-op guard did not reject transition: {result}")
            continue

        iterations = result.get("iterations", [])
        if name in PAGING_SCENARIOS or name.endswith("_probe_step_2_to_3"):
            req_trans = result.get("requested_transitions")
            act_trans = result.get("actual_transitions")
            total_p = result.get("total_pages")
            if status == "PASS":
                if req_trans is None or act_trans is None:
                    errors.append(f"missing transition count metadata in {name}")
                elif act_trans != req_trans:
                    errors.append(f"count mismatch in {name}: actual={act_trans} != requested={req_trans}")
                if len(iterations) != act_trans:
                    errors.append(f"iterations count mismatch in {name}: len={len(iterations)} != actual={act_trans}")

            if name.endswith("_sequential_paging") or name.endswith("_sequential_paging_anim_off"):
                if status == "PASS" and iterations:
                    first_iter = iterations[0]
                    if first_iter.get("page_before") != 1 or first_iter.get("page_after") != 2:
                        errors.append(f"first sequential iteration in {name} is not 1->2 (found {first_iter.get('page_before')}->{first_iter.get('page_after')})")
                    for idx, it in enumerate(iterations):
                        exp_from = idx + 1
                        exp_to = idx + 2
                        if it.get("page_before") != exp_from or it.get("page_after") != exp_to:
                            errors.append(f"broken sequential chain in {name}[{idx}]: expected {exp_from}->{exp_to}, got {it.get('page_before')}->{it.get('page_after')}")

            if name.endswith("_cached_paging") or name.endswith("_cached_paging_anim_off"):
                if status == "PASS":
                    if not result.get("warmup_verified"):
                        errors.append(f"unverified warmup in {name}")
                    for idx, it in enumerate(iterations):
                        exp_from = 1 if idx % 2 == 0 else 2
                        exp_to = 2 if idx % 2 == 0 else 1
                        if it.get("page_before") != exp_from or it.get("page_after") != exp_to:
                            errors.append(f"broken cached alternation in {name}[{idx}]: expected {exp_from}->{exp_to}, got {it.get('page_before')}->{it.get('page_after')}")

            if name.endswith("_probe_step_2_to_3"):
                if status == "PASS":
                    if iterations:
                        first_iter = iterations[0]
                        if first_iter.get("page_before") != 2 or first_iter.get("page_after") != 3:
                            errors.append(f"probe 2->3 in {name} is not 2->3 (found {first_iter.get('page_before')}->{first_iter.get('page_after')})")
                    # Mandatory probe screenshots
                    shot_b = result.get("screenshot_before")
                    shot_a = result.get("screenshot_after")
                    if not shot_b or not shot_a:
                        errors.append(f"mandatory probe screenshots missing in {name}")
                    else:
                        shot_dir = layout.screenshots / data.get("run_id", "unknown")
                        path_b = shot_dir / shot_b
                        path_a = shot_dir / shot_a
                        ok_b, err_b, _, _ = verify_png_file(path_b)
                        ok_a, err_a, _, _ = verify_png_file(path_a)
                        if not ok_b:
                            errors.append(f"probe screenshot_before invalid ({err_b}) in {name}")
                        if not ok_a:
                            errors.append(f"probe screenshot_after invalid ({err_a}) in {name}")
                        if ok_b and ok_a:
                            hash_b = sha256_file(path_b)
                            hash_a = sha256_file(path_a)
                            raw_hb = result.get("screenshot_before_sha256")
                            raw_ha = result.get("screenshot_after_sha256")
                            if raw_hb is None or raw_ha is None:
                                errors.append(f"probe screenshot sha256 hashes missing in {name}")
                            else:
                                if raw_hb != hash_b:
                                    errors.append(f"probe screenshot_before_sha256 mismatch in {name} ({raw_hb} != {hash_b})")
                                if raw_ha != hash_a:
                                    errors.append(f"probe screenshot_after_sha256 mismatch in {name} ({raw_ha} != {hash_a})")
                            if hash_b == hash_a:
                                errors.append(f"probe screenshots identical (no visual change) in {name}: {hash_b}")

            if status == "PASS":
                previous_hash, previous_idx = None, None
                for idx, it in enumerate(iterations):
                    if it.get("status") != "PASS":
                        continue
                    current = it.get("framebuffer_hash")
                    if current and previous_hash and current == previous_hash:
                        errors.append(
                            f"screen did not change between {name}[{previous_idx}] and {name}[{idx}]: "
                            f"identical framebuffer {current}"
                        )
                    if current:
                        previous_hash, previous_idx = current, idx

            if name.startswith("bookshelf_"):
                strict_bookshelf_paging = job.profile in {"paging", "smoke_validation", "real"}
                if status == "PASS" and strict_bookshelf_paging:
                    if total_p is None or total_p < 2:
                        errors.append(f"bookshelf shelf has <2 pages ({total_p}) in {name}")
                    if "animation" not in result or not result.get("animation_verified"):
                        errors.append(f"bookshelf animation unverified in {name}")

        for index, iteration in enumerate(iterations):
            iteration_status = iteration.get("status")
            if iteration_status not in ALLOWED_SCENARIO_STATUSES:
                errors.append(f"invalid iteration status: {name}[{index}]={iteration_status}")
                continue
            if iteration_status == "FAILED":
                if not iteration.get("reason"):
                    errors.append(f"FAILED iteration lacks diagnosis: {name}[{index}]")
                if require_success:
                    errors.append(f"diagnosed failed iteration: {name}[{index}]")
                continue
            if iteration_status != "PASS":
                continue
            elapsed = iteration.get("wall_time_ms")
            if not isinstance(elapsed, (int, float)) or elapsed <= 0:
                errors.append(f"non-positive PASS timing: {name}[{index}]")
            if name == "repeated_nav":
                evidence = iteration.get("semantic_evidence", {})
                trans = evidence.get("transitions", 0)
                if not isinstance(trans, (int, float)) or trans <= 0:
                    errors.append(f"repeated_nav PASS with 0 transitions: {name}[{index}]")
            if name in PAGING_SCENARIOS or name.endswith("_probe_step_2_to_3"):
                page_before = iteration.get("page_before")
                page_after = iteration.get("page_after")
                vis_before = iteration.get("visible_count_before")
                vis_after = iteration.get("visible_count_after")
                items_before = iteration.get("visible_items_before")
                items_after = iteration.get("visible_items_after")
                total_pages = iteration.get("total_pages")
                sig_before = iteration.get("visible_signature_before")
                sig_after = iteration.get("visible_signature_after")
                refreshes = iteration.get("refresh_count", iteration.get("set_dirty_calls", 0))

                if page_before is None or page_after is None:
                    errors.append(f"missing page numbers in {name}[{index}]")
                elif page_before == page_after:
                    errors.append(f"no-op transition (page_before == page_after == {page_before}) in {name}[{index}]")

                if vis_before is None or vis_after is None or total_pages is None:
                    errors.append(f"missing page-size metadata in {name}[{index}]")
                else:
                    if vis_before <= 0 or vis_after <= 0:
                        errors.append(f"zero visible items in {name}[{index}]: before={vis_before}, after={vis_after}")

                if not isinstance(items_before, list) or len(items_before) == 0 or not isinstance(items_after, list) or len(items_after) == 0:
                    errors.append(f"missing or empty visible_items list in {name}[{index}]")
                elif vis_before is not None and len(items_before) != vis_before:
                    errors.append(f"visible_count_before ({vis_before}) != len(visible_items_before) ({len(items_before)}) in {name}[{index}]")
                elif vis_after is not None and len(items_after) != vis_after:
                    errors.append(f"visible_count_after ({vis_after}) != len(visible_items_after) ({len(items_after)}) in {name}[{index}]")

                if sig_before is None or sig_after is None or sig_before == "" or sig_after == "":
                    errors.append(f"empty visible signature in {name}[{index}]")
                elif sig_before == sig_after:
                    errors.append(f"unchanged visible signature across page turn in {name}[{index}]")

                if name.startswith("bookshelf_"):
                    if not isinstance(refreshes, (int, float)) or refreshes <= 0:
                        errors.append(f"no refresh/state-change evidence for Bookshelf page turn in {name}[{index}]")
                elif not isinstance(refreshes, (int, float)) or refreshes <= 0:
                    errors.append(f"no refresh observed for page turn in {name}[{index}]")

                # A page turn under a full-screen overlay satisfies every other
                # guard while the screen shows something else, so each measured
                # transition must prove nothing covered the measured widget.
                top_widget = iteration.get("top_widget")
                windows_above = iteration.get("windows_above_measured")
                on_stack = iteration.get("measured_widget_on_stack")
                if not isinstance(top_widget, str) or not top_widget:
                    errors.append(f"missing top_widget evidence in {name}[{index}]")
                if not isinstance(windows_above, int) or windows_above < 0:
                    errors.append(f"missing windows_above_measured evidence in {name}[{index}]")
                if on_stack is not True:
                    errors.append(
                        f"measured widget was not on the window stack in {name}[{index}]: "
                        f"top_widget={top_widget}"
                    )
                frame_hash = iteration.get("framebuffer_hash")
                if not isinstance(frame_hash, str) or not frame_hash:
                    errors.append(f"missing framebuffer_hash evidence in {name}[{index}]")
            unique = iteration.get("unique_dirty_pct")
            union = iteration.get("spatial_union_dirty_area_pixels")
            cumulative = iteration.get("cumulative_dirty_area_pixels")
            if not isinstance(unique, (int, float)) or not 0 <= unique <= 100:
                errors.append(f"dirty percentage invariant: {name}[{index}]")
            if not isinstance(union, (int, float)) or not isinstance(cumulative, (int, float)) or union > cumulative:
                errors.append(f"dirty union invariant: {name}[{index}]")
    if data.get("plugin_load_assertion", {}).get("status") != "PASS":
        errors.append("plugin-load assertion failed")
    if data.get("run_status") != "PASS":
        errors.append("run_status is not PASS")
    if require_success and failed_scenarios:
        errors.append(f"diagnosed scenario failures: {sorted(failed_scenarios)}")
    return not errors, errors


def valid_completed_result(job: Job, layout: RunLayout) -> bool:
    valid, _ = validate_result_artifact(job, layout, require_success=True)
    return valid


def run_job(job: Job, layout: RunLayout, environment: dict, *, resume: bool = True,
            _project_title_restart: bool = False) -> dict:
    out_file = layout.raw / f"{job.run_id}.json"
    log_file = layout.logs / f"{job.run_id}.log"
    if resume and valid_completed_result(job, layout):
        return {"run_id": job.run_id, "status": "SKIPPED", "reason": "validated completed result exists"}

    # Project:Title performs its supported first-run migration and requests one
    # restart (exit 85). Keep it outside the measured process instead of
    # fabricating the plugin's private SQLite cache.
    home = Path(job.ko_home) if _project_title_restart else setup_isolated_home(job)
    if job.mode == "real_first_run":
        sanitize_working_corpus(Path(job.library_dir))
    targets_file = home / "benchmark_targets.json"
    write_deterministic_targets(Path(job.library_dir), targets_file)
    is_darwin = sys.platform == "darwin"
    emu_w = "618" if is_darwin else "1236"
    emu_h = "824" if is_darwin else "1648"
    screenshot_dir = layout.screenshots / job.run_id
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    # Never inherit an ambient flash setting: campaign metadata must be the
    # sole source of this synthetic emulator condition.
    env.pop("EMULATE_READER_FLASH", None)
    if job.emulate_reader_flash_ms is not None:
        env["EMULATE_READER_FLASH"] = str(job.emulate_reader_flash_ms)
    env.update({
        "KO_HOME": job.ko_home,
        "EMULATE_READER_W": emu_w,
        "EMULATE_READER_H": emu_h,
        "EMULATE_READER_DPI": "300",
        "EMULATE_BW_SCREEN": "1",
        "BENCHMARK_ENABLE": "1",
        "BENCHMARK_CONFIG": job.config,
        "BENCHMARK_MODE": job.mode,
        "BENCHMARK_PROFILE": job.profile,
        "BENCHMARK_LIBRARY_DIR": job.library_dir,
        "BENCHMARK_OUTPUT_FILE": str(out_file),
        "BENCHMARK_WARMUP_COUNT": str(job.warmup),
        "BENCHMARK_MEASURE_COUNT": str(job.measure),
        "BENCHMARK_BOOK_COUNT": str(job.book_count),
        "BENCHMARK_DATASET_MODE": job.dataset_mode,
        "BENCHMARK_EXPECTED_PLUGINS": ",".join(LOADED_PLUGIN_NAMES[name] for name in job.plugins),
        "BENCHMARK_RUN_OVERHEAD": "1" if job.overhead else "0",
        "BENCHMARK_OVERHEAD_COUNT": "30",
        "BENCHMARK_TARGETS_FILE": str(targets_file),
        "BENCHMARK_SCREENSHOT_DIR": str(screenshot_dir),
    })

    cmd = ["./luajit", "reader.lua", job.library_dir]
    started_ns = time.monotonic_ns()
    process = subprocess.Popen(
        cmd, cwd=KOREADER_DIR, env=env,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1,
    )
    line_queue: queue.Queue[str | None] = queue.Queue()

    def read_output() -> None:
        assert process.stdout is not None
        for line in process.stdout:
            line_queue.put(line)
        line_queue.put(None)

    reader_thread = threading.Thread(target=read_output, daemon=True)
    reader_thread.start()
    markers: dict[str, float] = {}
    deadline = time.monotonic() + job.timeout_s
    with log_file.open("a" if _project_title_restart else "w") as log:
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                process.kill()
                process.wait()
                raise TimeoutError(f"{job.run_id} exceeded {job.timeout_s}s")
            try:
                line = line_queue.get(timeout=min(0.25, remaining))
            except queue.Empty:
                continue
            if line is None:
                break
            log.write(line)
            log.flush()
            stripped = line.strip()
            if stripped in {"[BENCHMARK_UI_READY]", "[BENCHMARK_LIBRARY_READY]", "[BENCHMARK_COMPLETE]"}:
                markers[stripped[1:-1].lower()] = (time.monotonic_ns() - started_ns) / 1_000_000.0
    returncode = process.wait()
    reader_thread.join(timeout=5)
    total_ms = (time.monotonic_ns() - started_ns) / 1_000_000.0

    if not out_file.exists():
        if returncode == 85 and "project_title" in job.plugins and not _project_title_restart:
            return run_job(job, layout, environment, resume=False, _project_title_restart=True)
        return {"run_id": job.run_id, "status": "FAILED", "returncode": returncode, "reason": "output JSON missing"}
    data = json.loads(out_file.read_text())
    data.update({
        "phase": job.phase,
        "output_phase": layout.phase,
        "campaign": layout.campaign,
        "run_id": job.run_id,
        "block": job.block,
        "process_returncode": returncode,
        "emulate_reader_flash_ms": job.emulate_reader_flash_ms,
        "campaign_environment": environment,
        "external_process_timing": {
            "clock": "python time.monotonic_ns",
            "spawn_to_ui_ready_ms": markers.get("benchmark_ui_ready"),
            "spawn_to_library_ready_ms": markers.get("benchmark_library_ready"),
            "complete_marker_ms": markers.get("benchmark_complete"),
            "spawn_to_process_exit_ms": total_ms,
        },
        "orchestrator_job": asdict(job),
        "ko_home_disk_usage": tree_disk_usage(Path(job.ko_home)),
    })
    if job.mode in {"first_run_cold", "real_first_run", "steady_init"}:
        data["indexing_measurement"] = {
            "status": "INCLUSIVE",
            "inclusive_spawn_to_usable_library_ms": markers.get("benchmark_library_ready"),
            "scope": "Includes synchronous discovery/indexing required before usable library; no backend-independent async indexing-complete signal is assumed.",
        }
    else:
        data["indexing_measurement"] = {
            "status": "REUSED",
            "scope": "Reuses the initialized KO_HOME/cache/DB for this block; no reindex is requested per measured operation.",
        }
    if returncode != 0:
        data["run_status"] = "FAILED"

    # Compute and persist SHA256 hashes for probe screenshots
    for sc_name, sc_data in data.get("scenarios", {}).items():
        if isinstance(sc_data, dict) and sc_name.endswith("_probe_step_2_to_3") and sc_data.get("status") == "PASS":
            shot_b = sc_data.get("screenshot_before")
            shot_a = sc_data.get("screenshot_after")
            if shot_b and shot_a:
                shot_dir = layout.screenshots / job.run_id
                path_b = shot_dir / shot_b
                path_a = shot_dir / shot_a
                if path_b.is_file():
                    sc_data["screenshot_before_sha256"] = sha256_file(path_b)
                if path_a.is_file():
                    sc_data["screenshot_after_sha256"] = sha256_file(path_a)

    out_file.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    valid, errors = validate_result_artifact(job, layout, require_success=True)
    return {
        "run_id": job.run_id,
        "status": "PASS" if valid else "FAILED",
        "returncode": returncode,
        "errors": errors,
    }


def validation_jobs(campaign: str) -> list[Job]:
    jobs: list[Job] = []
    precision = [
        ("precision_zenos_page", "D_zenos"),
        ("precision_simpleui_page", "C_simpleui"),
        ("precision_stock_page", "A_stock"),
    ]
    for run_id, config in precision:
        jobs.append(Job(
            run_id, "smoke_gate", "validation", config, tuple(PHASE1_CONFIGS[config]),
            str(ROOT / "libraries" / "flat" / "books_50"),
            str(ENV_BASE / campaign / "validation" / run_id),
            "warm", "smoke_validation", "flat", 50, 2, 20, True,
            overhead=config == "A_stock",
        ))
    for config, plugins in PHASE1_CONFIGS.items():
        run_id = f"smoke_flat_{config}"
        jobs.append(Job(
            run_id, "smoke_gate", "validation", config, tuple(plugins),
            str(ROOT / "libraries" / "flat" / "books_50"),
            str(ENV_BASE / campaign / "validation" / run_id),
            "warm", "smoke_validation", "flat", 50, 1, 1, True,
        ))
    return jobs


def phase1_blocks(campaign: str, first_runs: int = 3, steady_runs: int = 3) -> OrderedDict[str, list[Job]]:
    blocks: OrderedDict[str, list[Job]] = OrderedDict()
    corpora = (("flat", 50), ("flat", 2000), ("hierarchical", 50), ("hierarchical", 2000))
    primary_first = {"A_stock", "B_bookshelf", "C_simpleui", "D_zenos", "J_project_title_vos"}
    large_library = str(ROOT / "libraries" / "hierarchical" / "books_2000")

    for config, plugins in PHASE1_CONFIGS.items():
        jobs: list[Job] = []
        for dataset, size in corpora:
            cell = f"{dataset}_{size}_{config}"
            jobs.append(Job(
                f"phase1_warm_{cell}", config, "phase1", config, tuple(plugins),
                str(ROOT / "libraries" / dataset / f"books_{size}"),
                str(ENV_BASE / campaign / "phase1" / f"warm_{cell}"),
                "warm", "synthetic", dataset, size, 2, 10, True,
            ))
        steady_home = str(ENV_BASE / campaign / "phase1" / f"steady_{config}")
        jobs.append(Job(
            f"phase1_steady_init_{config}", config, "phase1_setup", config, tuple(plugins),
            large_library, steady_home, "steady_init", "startup", "hierarchical", 2000, 0, 1, True,
        ))
        for index in range(1, steady_runs + 1):
            jobs.append(Job(
                f"phase1_steady_{config}_r{index:02d}", config, "phase1", config, tuple(plugins),
                large_library, steady_home, "steady_state_cold", "startup",
                "hierarchical", 2000, 0, 1, False,
            ))
        if config in primary_first:
            for index in range(1, first_runs + 1):
                run_id = f"phase1_first_{config}_r{index:02d}"
                jobs.append(Job(
                    run_id, config, "phase1", config, tuple(plugins), large_library,
                    str(ENV_BASE / campaign / "phase1" / run_id),
                    "first_run_cold", "startup", "hierarchical", 2000, 0, 1, True,
                ))
        if config == "A_stock":
            for index in range(1, first_runs + 1):
                run_id = f"phase1_first_K_vos_r{index:02d}"
                jobs.append(Job(
                    run_id, config, "phase1", "K_vos", ("vos",), large_library,
                    str(ENV_BASE / campaign / "phase1" / run_id),
                    "first_run_cold", "startup", "hierarchical", 2000, 0, 1, True,
                ))
        blocks[config] = jobs
    return blocks


def phase1_jobs(campaign: str = "test", first_runs: int = 3, steady_runs: int = 3) -> list[Job]:
    return [job for jobs in phase1_blocks(campaign, first_runs, steady_runs).values() for job in jobs]


def paging_phase1_blocks(campaign: str, process_runs: int = 3) -> OrderedDict[str, list[Job]]:
    blocks: OrderedDict[str, list[Job]] = OrderedDict()
    for config, plugins in PHASE1_CONFIGS.items():
        jobs = []
        for dataset, size in (("flat", 2000), ("hierarchical", 2000)):
            library = str(ROOT / "libraries" / dataset / f"books_{size}")
            for index in range(1, process_runs + 1):
                jobs.append(Job(
                    f"paging_{dataset}_{size}_{config}_r{index:02d}", config, "phase1", config,
                    tuple(plugins), library,
                    str(ENV_BASE / campaign / "paging_phase1" / f"{dataset}_{size}_{config}_r{index:02d}"),
                    "paging", "paging", dataset, size, 0, 1, True,
                ))
        blocks[config] = jobs
    return blocks


def corpus_files(master: Path) -> list[Path]:
    return sorted(path for path in master.rglob("*") if path.is_file() and path.suffix.lower() == ".epub")


def percentile_value(values: list[int], q: float) -> float | None:
    if not values:
        return None
    position = (len(values) - 1) * q
    lower, upper = math.floor(position), math.ceil(position)
    if lower == upper:
        return float(values[lower])
    return values[lower] * (upper - position) + values[upper] * (position - lower)


def working_layout_summary(master: Path, books: list[Path]) -> dict:
    """Describe the flat working corpus the runner builds from this master tree."""
    layout = plan_real_corpus_layout(master, books)
    folders: dict[str, int] = {}
    root_books = 0
    for _, relative in layout:
        if relative.parent == Path("."):
            root_books += 1
        else:
            folders[relative.parts[0]] = folders.get(relative.parts[0], 0) + 1
    return {
        "root_books": root_books,
        "folders": dict(sorted(folders.items())),
        "total_books": len(layout),
        "maximum_folder_depth": 1,
        "note": (
            "The master tree keeps zero books at its root, so the disposable "
            "working clone is rebuilt as a flat root plus neutral folderN "
            "buckets. Master content is never modified."
        ),
    }


def write_corpus_manifest(master: Path, output: Path) -> Path:
    all_files = [path for path in master.rglob("*") if path.is_file()]
    all_dirs = [path for path in master.rglob("*") if path.is_dir()]
    books = corpus_files(master)
    if len(books) != 2692:
        raise RuntimeError(f"HARD FAIL: real_books/ must contain exactly 2692 EPUB files, found {len(books)}")
    suffixes: dict[str, int] = {}
    sizes = sorted(path.stat().st_size for path in all_files)
    state_count = 0
    for path in all_files:
        suffix = path.suffix.lower() or "<none>"
        suffixes[suffix] = suffixes.get(suffix, 0) + 1
        if any(part.endswith(".sdr") or part.startswith(".koreader") for part in path.relative_to(master).parts):
            state_count += 1
    manifest = {
        "schema_version": 1,
        "corpus_name": f"REAL_{len(books)}",
        "seed": SEED,
        "total_files": len(all_files),
        "book_count": len(books),
        "logical_bytes": sum(sizes),
        "median_file_bytes": statistics.median(sizes) if sizes else None,
        "p90_file_bytes": percentile_value(sizes, 0.90),
        "folder_count": len(all_dirs),
        "maximum_folder_depth": max((len(path.relative_to(master).parts) for path in all_dirs), default=0),
        "preexisting_koreader_state_count": state_count,
        "formats": suffixes,
        "working_corpus_layout": working_layout_summary(master, books),
    }
    atomic_json_write(output, manifest)
    return output


# Working-corpus layout for the real library. The master real_books/ tree keeps
# zero books at its root and up to five levels of personal folder names, so
# library paging there is unmeasurable and every path is sensitive. The
# disposable working clone is rebuilt as a flat root plus neutral folders:
#
#   corpus/<REAL_ROOT_BOOKS books>   sequential + cached paging
#   corpus/folder1..folderN          folder navigation, render inside a big folder
#
# REAL_ROOT_BOOKS is sized so the coarsest layout still yields the full 30
# sequential transitions: Project:Title shows 14 entries per page (13 books plus
# the ".." entry), so 30 transitions need 31 pages, i.e. 403 books.
REAL_ROOT_BOOKS = 500
REAL_FOLDER_BOOKS = 500


def plan_real_corpus_layout(master: Path, books: list[Path]) -> list[tuple[Path, Path]]:
    """Map each master book to its flat working-corpus path, deterministically."""
    ranked = sorted(books, key=lambda path: hashlib.sha256(
        f"{SEED}:{path.relative_to(master)}".encode()).digest())
    mapping: list[tuple[Path, Path]] = []
    for index, source in enumerate(ranked):
        if index < REAL_ROOT_BOOKS:
            relative = Path(source.name)
        else:
            folder_index = (index - REAL_ROOT_BOOKS) // REAL_FOLDER_BOOKS + 1
            relative = Path(f"folder{folder_index}") / source.name
        mapping.append((source, relative))
    # Real filenames are not unique across the master tree; keep every book by
    # disambiguating collisions deterministically instead of silently dropping.
    seen: dict[Path, int] = {}
    resolved: list[tuple[Path, Path]] = []
    for source, relative in mapping:
        count = seen.get(relative, 0)
        seen[relative] = count + 1
        if count:
            relative = relative.with_name(f"{relative.stem}_{count:03d}{relative.suffix}")
        resolved.append((source, relative))
    return resolved


def _clone_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["cp", "-c", str(source), str(target)], check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        shutil.copy2(source, target)


def clone_selected_corpus(master: Path, destination: Path, selected: Iterable[Path]) -> None:
    _safe_remove(destination)
    destination.mkdir(parents=True)
    for source in selected:
        _clone_file(source, destination / source.relative_to(master))


def clone_flat_real_corpus(master: Path, destination: Path, books: list[Path]) -> dict:
    _safe_remove(destination)
    destination.mkdir(parents=True)
    layout = plan_real_corpus_layout(master, books)
    for source, relative in layout:
        _clone_file(source, destination / relative)
    folders: dict[str, int] = {}
    root_books = 0
    for _, relative in layout:
        if relative.parent == Path("."):
            root_books += 1
        else:
            folders[relative.parts[0]] = folders.get(relative.parts[0], 0) + 1
    return {
        "root_books": root_books,
        "folders": dict(sorted(folders.items())),
        "total_books": len(layout),
    }


def prepare_real_corpora(campaign: str, configs: Iterable[str], lanes: int) -> None:
    master = ROOT / "real_books"
    if not master.is_dir():
        raise FileNotFoundError("real_books/ does not exist")
    books = corpus_files(master)
    if len(books) != 2692:
        raise RuntimeError(f"HARD FAIL: real_books/ must contain exactly 2692 EPUB files, found {len(books)}")
    def prepare(config: str) -> None:
        destination = WORK_REAL / campaign / config / "corpus"
        if not destination.exists():
            clone_flat_real_corpus(master, destination, books)

    with ThreadPoolExecutor(max_workers=max(1, lanes)) as executor:
        futures = [executor.submit(prepare, config) for config in configs]
        for future in as_completed(futures):
            future.result()


def real_corpora_for_jobs(jobs: Iterable[Job]) -> list[Path]:
    """Return every distinct disposable corpus required by a block."""
    return sorted({Path(job.library_dir) for job in jobs}, key=str)


def prepare_real_corpora_for_jobs(campaign: str, jobs: Iterable[Job], lanes: int) -> list[Path]:
    """Prepare and return every disposable corpus required by a block."""
    corpora = real_corpora_for_jobs(jobs)
    prepare_real_corpora(
        campaign,
        [corpus.parent.name for corpus in corpora],
        lanes=lanes,
    )
    return corpora


def phase2_blocks(campaign: str, steady_runs: int = 3) -> OrderedDict[str, list[Job]]:
    master = ROOT / "real_books"
    if not master.is_dir():
        raise FileNotFoundError("real_books/ does not exist")
    books = corpus_files(master)
    if len(books) != 2692:
        raise RuntimeError(f"HARD FAIL: real_books/ must contain exactly 2692 EPUB files, found {len(books)}")
    blocks: OrderedDict[str, list[Job]] = OrderedDict()
    for config, plugins in PHASE2_CONFIGS.items():
        library = WORK_REAL / campaign / config / "corpus"
        home = ENV_BASE / campaign / "phase2" / config
        jobs = [Job(
            f"phase2_first_{config}", config, "phase2", config, tuple(plugins),
            str(library), str(home), "real_first_run", "startup", "real_2692",
            len(books), 0, 1, True, timeout_s=3600,
        )]
        for index in range(1, steady_runs + 1):
            jobs.append(Job(
                f"phase2_steady_{config}_r{index:02d}", config, "phase2", config, tuple(plugins),
                str(library), str(home), "real_steady_cold", "startup", "real_2692",
                len(books), 0, 1, False, timeout_s=1800,
            ))
        jobs.append(Job(
            f"phase2_warm_{config}", config, "phase2", config, tuple(plugins),
            str(library), str(home), "warm", "real", "real_2692",
            len(books), 2, 10, False, timeout_s=3600,
        ))
        blocks[config] = jobs
    return blocks


def phase2_jobs(campaign: str = "test", steady_runs: int = 3) -> list[Job]:
    return [job for jobs in phase2_blocks(campaign, steady_runs).values() for job in jobs]


def paging_phase2_blocks(campaign: str, process_runs: int = 3) -> OrderedDict[str, list[Job]]:
    master = ROOT / "real_books"
    if not master.is_dir():
        raise FileNotFoundError("real_books/ does not exist")
    books = corpus_files(master)
    if len(books) != 2692:
        raise RuntimeError(f"HARD FAIL: real_books/ must contain exactly 2692 EPUB files, found {len(books)}")
    blocks: OrderedDict[str, list[Job]] = OrderedDict()
    for config, plugins in PHASE2_CONFIGS.items():
        library = WORK_REAL / campaign / config / "corpus"
        jobs = []
        for index in range(1, process_runs + 1):
            jobs.append(Job(
                f"paging_real_{config}_r{index:02d}", config, "phase2", config,
                tuple(plugins), str(library),
                str(ENV_BASE / campaign / "paging_phase2" / f"{config}_r{index:02d}"),
                "paging", "paging", "real_2692", len(books), 0, 1, True,
                timeout_s=3600,
            ))
        blocks[config] = jobs
    return blocks


def bookends_blocks(campaign: str) -> OrderedDict[str, list[Job]]:
    master = ROOT / "real_books"
    books = corpus_files(master)
    jobs = []
    for config, plugins in (("A_stock", []), ("K_stock_bookends", ["bookends"])):
        library = WORK_REAL / campaign / f"bookends_{config}" / "corpus"
        jobs.append(Job(
            f"bookends_control_{config}", "bookends_control", "bookends_control",
            config, tuple(plugins), str(library),
            str(ENV_BASE / campaign / "phase2" / f"bookends_{config}"),
            "warm", "bookends_control", "real_2692", len(books), 2, 10, True,
            timeout_s=3600,
        ))
    return OrderedDict({"bookends_control": jobs})


def bookends_jobs(campaign: str = "test") -> list[Job]:
    return list(bookends_blocks(campaign)["bookends_control"])


def checkpoint_path(layout: RunLayout, block: str) -> Path:
    return layout.checkpoints / f"{block}.json"


def write_block_checkpoint(layout: RunLayout, block: str, jobs: list[Job]) -> Path:
    failures = []
    artifacts = []
    for job in jobs:
        valid, errors = validate_result_artifact(job, layout, require_success=True)
        if not valid:
            failures.append({"run_id": job.run_id, "errors": errors})
            continue
        raw = layout.raw / f"{job.run_id}.json"
        log = layout.logs / f"{job.run_id}.log"
        artifacts.append({
            "run_id": job.run_id,
            "raw_sha256": sha256_file(raw),
            "log_sha256": sha256_file(log),
        })
    if failures:
        raise RuntimeError(f"block {block} cannot checkpoint: {failures[0]}")
    data = {
        "schema_version": 1,
        "status": "SUCCESS",
        "campaign": layout.campaign,
        "phase": layout.phase,
        "block": block,
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "jobs": artifacts,
    }
    path = checkpoint_path(layout, block)
    atomic_json_write(path, data)
    return path


def block_checkpoint_valid(layout: RunLayout, block: str, jobs: list[Job]) -> bool:
    path = checkpoint_path(layout, block)
    if not path.exists():
        return False
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return False
    if data.get("status") != "SUCCESS" or data.get("campaign") != layout.campaign \
            or data.get("phase") != layout.phase or data.get("block") != block:
        return False
    expected = {job.run_id for job in jobs}
    recorded_entries = {entry.get("run_id"): entry for entry in data.get("jobs", [])}
    if set(recorded_entries) != expected:
        return False
    for job in jobs:
        if not valid_completed_result(job, layout):
            return False
        entry = recorded_entries[job.run_id]
        raw = layout.raw / f"{job.run_id}.json"
        log = layout.logs / f"{job.run_id}.log"
        if entry.get("raw_sha256") != sha256_file(raw) or entry.get("log_sha256") != sha256_file(log):
            return False
    return True


def ensure_validation_passed(layout: RunLayout, jobs: list[Job]) -> None:
    for job in jobs:
        valid, errors = validate_result_artifact(job, layout, require_success=True)
        if not valid:
            raise RuntimeError(f"validation failed for {job.run_id}: {errors}")
    targets = {
        "precision_zenos_page": "library_cached_paging",
        "precision_simpleui_page": "library_cached_paging",
        "precision_stock_page": "library_cached_paging",
    }
    by_id = {job.run_id: job for job in jobs}
    for run_id, scenario in targets.items():
        data = json.loads((layout.raw / f"{run_id}.json").read_text())
        if data.get("timing", {}).get("integer_rounding") is not False:
            raise RuntimeError(f"{run_id} does not prove non-rounded raw timing")
        samples = [
            iteration.get("wall_time_ms")
            for iteration in data["scenarios"][scenario].get("iterations", [])
            if iteration.get("status") == "PASS"
        ]
        if len(samples) < 20 or not any(value != int(value) for value in samples):
            raise RuntimeError(f"{run_id}/{scenario} lacks 20 fractional-ms PASS samples")
        if run_id not in by_id:
            raise RuntimeError(f"validation job definition missing: {run_id}")
    overhead = json.loads((layout.raw / "precision_stock_page.json").read_text()).get(
        "instrumentation_overhead_validation", {}
    )
    required = {"library_sequential_paging"}
    if not set(overhead).issuperset(required):
        raise RuntimeError("instrumentation overhead control is incomplete")
    for scenario, result in overhead.items():
        if result.get("sample_count", 0) < 30:
            raise RuntimeError(f"instrumentation control {scenario} has fewer than 30 paired samples")
        delta = abs(result.get("median_delta_ms") or 0.0)
        relative = abs(result.get("relative_overhead_pct") or 0.0)
        if delta > 15.0 and relative > 25.0:
            raise RuntimeError(f"material instrumentation overhead in {scenario}: {delta:.3f} ms / {relative:.2f}%")


def ensure_paging_phase1_complete(campaign: str, process_runs: int,
                                  emulate_reader_flash_ms: int | None = None) -> None:
    layout = make_layout(campaign, "phase1")
    validation = validation_jobs(campaign)
    paging = paging_phase1_blocks(campaign, process_runs)
    if emulate_reader_flash_ms is not None:
        validation = [replace(job, emulate_reader_flash_ms=emulate_reader_flash_ms) for job in validation]
        paging = OrderedDict(
            (block, [replace(job, emulate_reader_flash_ms=emulate_reader_flash_ms) for job in jobs])
            for block, jobs in paging.items()
        )
    if not block_checkpoint_valid(layout, "smoke_gate", validation):
        raise RuntimeError("Paging Phase 1 smoke_gate checkpoint is missing or invalid")
    for block, jobs in paging.items():
        if not block_checkpoint_valid(layout, block, jobs):
            raise RuntimeError(f"Paging Phase 1 block checkpoint is missing or invalid: {block}")


def ensure_phase1_complete(campaign: str, first_runs: int, steady_runs: int,
                           emulate_reader_flash_ms: int | None = None) -> None:
    layout = make_layout(campaign, "phase1")
    validation = validation_jobs(campaign)
    phase1 = phase1_blocks(campaign, first_runs, steady_runs)
    if emulate_reader_flash_ms is not None:
        validation = [replace(job, emulate_reader_flash_ms=emulate_reader_flash_ms) for job in validation]
        phase1 = OrderedDict(
            (block, [replace(job, emulate_reader_flash_ms=emulate_reader_flash_ms) for job in jobs])
            for block, jobs in phase1.items()
        )
    if not block_checkpoint_valid(layout, "smoke_gate", validation):
        raise RuntimeError("Phase 1 smoke_gate checkpoint is missing or invalid")
    for block, jobs in phase1.items():
        if not block_checkpoint_valid(layout, block, jobs):
            raise RuntimeError(f"Phase 1 block checkpoint is missing or invalid: {block}")


def select_blocks(blocks: OrderedDict[str, list[Job]], phase: str, batch: str) -> OrderedDict[str, list[Job]]:
    keys = list(blocks)
    if batch == "all":
        return blocks
    if phase == "phase1":
        selected = keys[:5] if batch == "1" else keys[5:] if batch == "2" else []
    elif phase == "phase2":
        selected = keys[:6] if batch == "1" else keys[6:] if batch == "2" else []
    else:
        selected = keys if batch in {"3", "all"} else []
    if not selected:
        raise ValueError(f"batch {batch} is not valid for {phase}")
    return OrderedDict((key, blocks[key]) for key in selected)


def run_block(block: str, jobs: list[Job], layout: RunLayout, environment: dict,
              *, resume: bool) -> bool:
    if resume and block_checkpoint_valid(layout, block, jobs):
        print(f"BLOCK {block}: SKIPPED (validated SUCCESS checkpoint)", flush=True)
        return True
    print(f"BLOCK {block}: START ({len(jobs)} jobs; sequential)", flush=True)
    for index, job in enumerate(jobs, 1):
        print(f"  [{index}/{len(jobs)}] {job.run_id}", flush=True)
        try:
            result = run_job(job, layout, environment, resume=resume)
        except Exception as exc:
            result = {"run_id": job.run_id, "status": "FAILED", "reason": str(exc)}
        print("  " + json.dumps(result, ensure_ascii=False), flush=True)
        if result["status"] not in {"PASS", "SKIPPED"}:
            print(f"BLOCK {block}: FAILED; no checkpoint written", flush=True)
            return False
    path = write_block_checkpoint(layout, block, jobs)
    print(f"BLOCK {block}: SUCCESS checkpoint {path}", flush=True)
    return True


def run_validation_parallel(jobs: list[Job], layout: RunLayout, environment: dict,
                            *, resume: bool, lanes: int) -> bool:
    if lanes == 1:
        for job in jobs:
            result = run_job(job, layout, environment, resume=resume)
            print(json.dumps(result, ensure_ascii=False), flush=True)
            if result["status"] not in {"PASS", "SKIPPED"}:
                return False
    else:
        with ThreadPoolExecutor(max_workers=lanes) as executor:
            future_jobs = {
                executor.submit(run_job, job, layout, environment, resume=resume): job
                for job in jobs
            }
            for future in as_completed(future_jobs):
                job = future_jobs[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {"run_id": job.run_id, "status": "FAILED", "reason": str(exc)}
                print(json.dumps(result, ensure_ascii=False), flush=True)
                if result["status"] not in {"PASS", "SKIPPED"}:
                    return False
    ensure_validation_passed(layout, jobs)
    write_block_checkpoint(layout, "smoke_gate", jobs)
    return True


def analyze_layout(layout: RunLayout, scope: str) -> None:
    subprocess.run([
        sys.executable, str(ROOT / "analyze_results.py"),
        "--run-dir", str(layout.root), "--scope", scope,
    ], cwd=ROOT, check=True)


def print_plan(blocks: OrderedDict[str, list[Job]], layout: RunLayout) -> None:
    print(json.dumps({
        "campaign": layout.campaign,
        "phase": layout.phase,
        "output": str(layout.root),
        "blocks": {block: [job.run_id for job in jobs] for block, jobs in blocks.items()},
        "total_jobs": sum(len(jobs) for jobs in blocks.values()),
        "measurement_lanes": 1,
    }, indent=2))


def prepare_jobs(jobs: list[Job], lanes: int) -> None:
    def prepare(job: Job) -> None:
        home = setup_isolated_home(job)
        library = Path(job.library_dir)
        if library.exists():
            write_deterministic_targets(library, home / "benchmark_targets.json")

    unique_homes: dict[str, Job] = {}
    for job in jobs:
        current = unique_homes.get(job.ko_home)
        if current is None or (job.fresh_home and not current.fresh_home):
            unique_homes[job.ko_home] = job
    with ThreadPoolExecutor(max_workers=max(1, lanes)) as executor:
        futures = [executor.submit(prepare, job) for job in unique_homes.values()]
        for future in as_completed(futures):
            future.result()


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--validate", action="store_true")
    group.add_argument("--phase1", action="store_true")
    group.add_argument("--phase2", action="store_true")
    group.add_argument("--paging-phase1", action="store_true",
                       help="paging-only synthetic phase: flat/hierarchical 2000, three process runs")
    group.add_argument("--paging-phase2", action="store_true",
                       help="paging-only real phase: real_books/2692, three process runs")
    group.add_argument("--bookends-control", action="store_true")
    parser.add_argument("--campaign", default=date.today().isoformat(),
                        help="campaign folder name; reuse the same value tomorrow")
    parser.add_argument("--batch", choices=("1", "2", "3", "all"), default="all")
    parser.add_argument("--lanes", type=int, default=1)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--no-analyze", action="store_true")
    parser.add_argument("--first-runs", type=int, default=3)
    parser.add_argument("--steady-runs", type=int, default=3)
    parser.add_argument("--paging-runs", type=int, default=3,
                        help="independent process runs per paging cell (default: 3)")
    parser.add_argument("--emulate-reader-flash-ms", type=int,
                        help="explicit SDL flash delay in milliseconds; omit for baseline")
    args = parser.parse_args()

    if not args.campaign or "/" in args.campaign or args.campaign in {".", ".."}:
        parser.error("--campaign must be a single safe folder name, preferably YYYY-MM-DD")
    if args.lanes < 1:
        parser.error("--lanes must be >= 1")
    if args.paging_runs < 1:
        parser.error("--paging-runs must be >= 1")
    if args.emulate_reader_flash_ms is not None and args.emulate_reader_flash_ms <= 0:
        parser.error("--emulate-reader-flash-ms must be > 0; omit it for baseline")
    if args.validate and args.lanes > 2:
        parser.error("validation/diagnostics allow at most 2 lanes")
    if not args.validate and not args.prepare_only and args.lanes != 1:
        parser.error("final Phase 1/2 and Bookends measurements must use --lanes 1")

    phase_name = "phase1" if args.validate or args.phase1 or args.paging_phase1 else "phase2"
    layout = make_layout(args.campaign, phase_name)
    environment: dict = {}
    resume = not args.no_resume

    verify_pinned_revisions()

    if args.validate:
        if args.batch != "all":
            parser.error("validation uses one smoke_gate block; --batch must be all")
        jobs = validation_jobs(args.campaign)
        blocks = OrderedDict({"smoke_gate": jobs})
    elif args.paging_phase1:
        blocks = select_blocks(
            paging_phase1_blocks(args.campaign, args.paging_runs),
            "phase1", args.batch,
        )
        if not args.dry_run and not args.prepare_only:
            gate_jobs = validation_jobs(args.campaign)
            if args.emulate_reader_flash_ms is not None:
                gate_jobs = [replace(job, emulate_reader_flash_ms=args.emulate_reader_flash_ms) for job in gate_jobs]
            if not block_checkpoint_valid(layout, "smoke_gate", gate_jobs):
                raise RuntimeError("Paging Phase 1 cannot start: smoke_gate checkpoint is missing or invalid")
    elif args.phase1:
        blocks = select_blocks(
            phase1_blocks(args.campaign, args.first_runs, args.steady_runs),
            "phase1", args.batch,
        )
        if not args.dry_run and not args.prepare_only:
            gate_jobs = validation_jobs(args.campaign)
            if args.emulate_reader_flash_ms is not None:
                gate_jobs = [replace(job, emulate_reader_flash_ms=args.emulate_reader_flash_ms) for job in gate_jobs]
            if not block_checkpoint_valid(layout, "smoke_gate", gate_jobs):
                raise RuntimeError("Phase 1 cannot start: smoke_gate checkpoint is missing or invalid")
    elif args.paging_phase2:
        if not args.dry_run and not args.prepare_only:
            ensure_paging_phase1_complete(args.campaign, args.paging_runs, args.emulate_reader_flash_ms)
        blocks = select_blocks(paging_phase2_blocks(args.campaign, args.paging_runs), "phase2", args.batch)
    elif args.phase2:
        if args.batch == "3":
            blocks = bookends_blocks(args.campaign)
            if not args.dry_run and not args.prepare_only:
                ensure_phase1_complete(args.campaign, args.first_runs, args.steady_runs, args.emulate_reader_flash_ms)
                expected_phase2 = phase2_blocks(args.campaign, args.steady_runs)
                if args.emulate_reader_flash_ms is not None:
                    expected_phase2 = OrderedDict(
                        (block, [replace(job, emulate_reader_flash_ms=args.emulate_reader_flash_ms) for job in jobs])
                        for block, jobs in expected_phase2.items()
                    )
                for block, jobs in expected_phase2.items():
                    if not block_checkpoint_valid(layout, block, jobs):
                        raise RuntimeError(f"Phase 2 block checkpoint is missing or invalid: {block}")
        else:
            if not args.dry_run and not args.prepare_only:
                ensure_phase1_complete(args.campaign, args.first_runs, args.steady_runs, args.emulate_reader_flash_ms)
            blocks = select_blocks(phase2_blocks(args.campaign, args.steady_runs), "phase2", args.batch)
    else:
        if args.batch not in {"3", "all"}:
            parser.error("Bookends control is Phase 2 batch 3")
        blocks = bookends_blocks(args.campaign)
        # Explicit standalone control for a focused Bookends repair campaign.
        # The normal full-campaign spelling (--phase2 --batch 3) retains its
        # Phase 1/2 prerequisites above.

    if args.emulate_reader_flash_ms is not None:
        blocks = OrderedDict(
            (block, [replace(job, emulate_reader_flash_ms=args.emulate_reader_flash_ms) for job in jobs])
            for block, jobs in blocks.items()
        )

    if args.dry_run:
        print_plan(blocks, layout)
        return 0

    environment = ensure_layout(layout, args.emulate_reader_flash_ms)
    all_jobs = [job for jobs in blocks.values() for job in jobs]
    if args.prepare_only:
        if args.phase2 or args.paging_phase2 or args.bookends_control:
            configs = sorted({job.config if job.block != "bookends_control" else f"bookends_{job.config}" for job in all_jobs})
            prepare_real_corpora(args.campaign, configs, args.lanes)
            write_corpus_manifest(ROOT / "real_books", layout.root / "real_corpus_manifest.json")
        prepare_jobs(all_jobs, args.lanes)
        print(f"Preparation complete; no KOReader measurement process started. Output: {layout.root}")
        return 0

    if args.phase2 or args.paging_phase2 or args.bookends_control:
        write_corpus_manifest(ROOT / "real_books", layout.root / "real_corpus_manifest.json")

    success = True
    if args.validate:
        success = run_validation_parallel(all_jobs, layout, environment, resume=resume, lanes=args.lanes)
    else:
        for block, jobs in blocks.items():
            real_corpora = real_corpora_for_jobs(jobs) \
                if (args.phase2 or args.paging_phase2 or args.bookends_control) else []
            if real_corpora and not (resume and block_checkpoint_valid(layout, block, jobs)):
                real_corpora = prepare_real_corpora_for_jobs(args.campaign, jobs, lanes=1)
            try:
                if not run_block(block, jobs, layout, environment, resume=resume):
                    success = False
                    break
            finally:
                # The copies are disposable and must not accumulate across blocks.
                for corpus in real_corpora:
                    _safe_remove(corpus)

    if success and not args.no_analyze:
        scope = "validation" if args.validate else "phase1" if args.phase1 or args.paging_phase1 else \
            "bookends_control" if args.bookends_control or args.batch == "3" else "phase2"
        analyze_layout(layout, scope)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
