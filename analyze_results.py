#!/usr/bin/env python3
"""Schema-v2, status-aware analyzer for the KOReader benchmark.

The analyzer never substitutes zero for missing, failed, or unsupported values
and never contains prose performance conclusions. All report statements are
derived from the loaded raw records.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
import struct
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RAW = RESULTS / "raw"

DEPRECATED_SCENARIOS = {
    "library_next_page",
    "library_prev_page",
    "bookshelf_page_turn",
}


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


def percentile(values: list[float], q: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def describe(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {key: None for key in ("count", "median", "p10", "p90", "mean", "stdev", "min", "max")}
    return {
        "count": len(values),
        "median": statistics.median(values),
        "p10": percentile(values, 0.10),
        "p90": percentile(values, 0.90),
        "mean": statistics.fmean(values),
        "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
        "min": min(values),
        "max": max(values),
    }


def load_records(scope: str) -> list[dict[str, Any]]:
    records = []
    for path in sorted(RAW.glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            print(f"SKIP {path}: {exc}")
            continue
        if data.get("schema_version") != 2:
            continue
        phase = data.get("phase", "validation")
        if scope != "all" and phase != scope and not (scope == "phase1" and phase == "phase1_setup") \
                and not (scope == "phase2" and phase == "phase2_setup"):
            continue
        data["_path"] = str(path)
        records.append(data)
    return records


def numeric(value: Any) -> float | None:
    return float(value) if isinstance(value, (int, float)) and math.isfinite(value) else None


def aggregate_scenarios(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], dict[str, Any]] = defaultdict(lambda: {
        "statuses": Counter(), "values": defaultdict(list), "files": set(),
    })
    metrics = (
        "wall_time_ms", "natural_lua_heap_kb", "lua_heap_delta_kb", "rss_kb",
        "set_dirty_calls", "refresh_count", "full_refreshes", "partial_refreshes",
        "unique_dirty_pct", "cumulative_dirty_screen_equivalents", "largest_single_dirty_pct",
        "visible_count_before", "visible_count_after", "total_pages",
    )
    for record in records:
        key_base = (
            record.get("phase", "validation"), record.get("config"), record.get("mode"),
            record.get("profile"), record.get("dataset_mode"), record.get("book_count"),
        )
        for scenario, scenario_data in record.get("scenarios", {}).items():
            group = groups[key_base + (scenario,)]
            group["files"].add(record["_path"])
            iterations = scenario_data.get("iterations") or []
            if not iterations:
                iterations = [scenario_data]
            for iteration in iterations:
                status = iteration.get("status", scenario_data.get("status", "FAILED"))
                group["statuses"][status] += 1
                if status != "PASS":
                    continue
                for metric in metrics:
                    value = numeric(iteration.get(metric))
                    if value is not None:
                        group["values"][metric].append(value)

    rows = []
    for key, group in sorted(groups.items(), key=lambda item: tuple(str(v) for v in item[0])):
        phase, config, mode, profile, dataset, books, scenario = key
        statuses: Counter = group["statuses"]
        if scenario in DEPRECATED_SCENARIOS:
            status = "DEPRECATED_INVALID_FOR_RANKING"
        elif statuses["PASS"]:
            status = "PASS"
        elif statuses["FAILED"]:
            status = "FAILED"
        else:
            status = "UNSUPPORTED"
        row: dict[str, Any] = {
            "Phase": phase,
            "Stack": config,
            "Mode": mode,
            "Profile": profile,
            "Dataset": dataset,
            "BookCount": books,
            "Scenario": scenario,
            "Status": status,
            "ProcessRuns": len(group["files"]),
            "PassSamples": statuses["PASS"],
            "FailedSamples": statuses["FAILED"],
            "UnsupportedSamples": statuses["UNSUPPORTED"],
        }
        for metric, values in group["values"].items():
            stats = describe(values)
            prefix = metric
            for stat_name, stat_value in stats.items():
                row[f"{prefix}_{stat_name}"] = stat_value
        rows.append(row)
    return rows


def add_external_timing_rows(records: Iterable[dict[str, Any]], rows: list[dict[str, Any]]) -> None:
    groups: dict[tuple[Any, ...], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        key = (
            record.get("phase", "validation"), record.get("config"), record.get("mode"),
            record.get("profile"), record.get("dataset_mode"), record.get("book_count"),
        )
        timing = record.get("external_process_timing", {})
        for metric, value in timing.items():
            val = numeric(value)
            if val is not None:
                groups[key][metric].append(val)
    for key, metrics in sorted(groups.items(), key=lambda item: tuple(str(v) for v in item[0])):
        phase, config, mode, profile, dataset, books = key
        for metric, values in metrics.items():
            stats = describe(values)
            row = {
                "Phase": phase, "Stack": config, "Mode": mode, "Profile": profile,
                "Dataset": dataset, "BookCount": books, "Scenario": f"process:{metric}",
                "Status": "PASS" if values else "FAILED", "ProcessRuns": len(values),
                "PassSamples": len(values), "FailedSamples": 0, "UnsupportedSamples": 0,
            }
            for stat_name, stat_value in stats.items():
                row[f"wall_time_ms_{stat_name}"] = stat_value
            rows.append(row)


def add_memory_rows(records: Iterable[dict[str, Any]], rows: list[dict[str, Any]]) -> None:
    groups: dict[tuple[Any, ...], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    process_files: dict[tuple[Any, ...], set[str]] = defaultdict(set)
    for record in records:
        key_base = (
            record.get("phase", "validation"), record.get("config"), record.get("mode"),
            record.get("profile"), record.get("dataset_mode"), record.get("book_count"),
        )
        checkpoints = record.get("memory_checkpoints", {})
        for name, snap in checkpoints.items():
            if not isinstance(snap, dict):
                continue
            key = key_base + (name,)
            process_files[key].add(str(record.get("_path", record.get("run_id", "unknown"))))
            for metric in ("natural_lua_heap_kb", "forced_gc_live_heap_kb", "rss_kb"):
                val = numeric(snap.get(metric))
                if val is not None:
                    groups[key][metric].append(val)
        reader_cycles = record.get("bookends_reader_cycles_live_heap_kb")
        if isinstance(reader_cycles, list):
            key = key_base + ("post_reader_cycles_forced_gc",)
            process_files[key].add(str(record.get("_path", record.get("run_id", "unknown"))))
            for value in reader_cycles:
                val = numeric(value)
                if val is not None:
                    groups[key]["forced_gc_live_heap_kb"].append(val)
    for key, metrics in sorted(groups.items(), key=lambda item: tuple(str(v) for v in item[0])):
        phase, config, mode, profile, dataset, books, name = key
        row = {
            "Phase": phase, "Stack": config, "Mode": mode, "Profile": profile,
            "Dataset": dataset, "BookCount": books, "Scenario": f"memory:{name}",
            "Status": "PASS", "ProcessRuns": len(process_files[key]),
            "PassSamples": max((len(v) for v in metrics.values()), default=0),
            "FailedSamples": 0, "UnsupportedSamples": 0,
        }
        for metric, values in metrics.items():
            for stat_name, stat_value in describe(values).items():
                row[f"{metric}_{stat_name}"] = stat_value
        rows.append(row)


def add_disk_rows(records: Iterable[dict[str, Any]], rows: list[dict[str, Any]]) -> None:
    groups: dict[tuple[Any, ...], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        key = (
            record.get("phase", "validation"), record.get("config"), record.get("mode"),
            record.get("profile"), record.get("dataset_mode"), record.get("book_count"),
        )
        disk = record.get("disk_usage", {})
        for metric, value in disk.items():
            val = numeric(value)
            if val is not None:
                groups[key][metric].append(val)
    for key, metrics in sorted(groups.items(), key=lambda item: tuple(str(v) for v in item[0])):
        phase, config, mode, profile, dataset, books = key
        for metric, values in metrics.items():
            stats = describe(values)
            row = {
                "Phase": phase, "Stack": config, "Mode": mode, "Profile": profile,
                "Dataset": dataset, "BookCount": books, "Scenario": f"disk:{metric}",
                "Status": "PASS" if values else "FAILED", "ProcessRuns": len(values),
                "PassSamples": len(values), "FailedSamples": 0, "UnsupportedSamples": 0,
            }
            for stat_name, stat_value in stats.items():
                row[f"bytes_{stat_name}"] = stat_value
            rows.append(row)


def write_csv(rows: list[dict[str, Any]], scope: str) -> Path:
    output = RESULTS / ("BOOKENDS_RESULTS.csv" if scope == "bookends_control" else "RESULTS.csv")
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return output


def fmt(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def validation_report(records: list[dict[str, Any]]) -> Path:
    output = RESULTS / "VALIDATION.md"
    lines = ["# Benchmark validation", "", "Generated only from schema-v2 raw results.", ""]
    precision_targets = {
        "precision_zenos_page": "library_cached_paging",
        "precision_simpleui_page": "library_cached_paging",
        "precision_stock_page": "library_cached_paging",
    }
    by_run = {record.get("run_id"): record for record in records}
    for run_id, scenario in precision_targets.items():
        record = by_run.get(run_id)
        lines += [f"## `{run_id}` / `{scenario}`", ""]
        if not record:
            lines += ["NOT RUN", ""]
            continue
        samples = [it.get("wall_time_ms") for it in record.get("scenarios", {}).get(scenario, {}).get("iterations", [])
                   if it.get("status") == "PASS" and numeric(it.get("wall_time_ms")) is not None]
        lines += [f"Timer: `{record.get('timing', {})}`", "", f"Raw samples ({len(samples)}):", "",
                  "```json", json.dumps(samples, separators=(",", ":")), "```", ""]
    overhead_records = [r for r in records if r.get("instrumentation_overhead_validation")]
    lines += ["## Instrumentation overhead", ""]
    if not overhead_records:
        lines += ["NOT RUN", ""]
    else:
        for record in overhead_records:
            for scenario, result in sorted(record["instrumentation_overhead_validation"].items()):
                lines.append(
                    f"- `{scenario}`: n={result.get('sample_count')}, "
                    f"minimal median={fmt((result.get('minimal') or {}).get('median'))} ms, "
                    f"full median={fmt((result.get('full') or {}).get('median'))} ms, "
                    f"delta={fmt(result.get('median_delta_ms'))} ms, "
                    f"relative={fmt(result.get('relative_overhead_pct'))}%"
                )
        lines.append("")
    output.write_text("\n".join(lines))
    return output


def comparison_findings(rows: list[dict[str, Any]]) -> list[str]:
    pairs = [
        ("A_stock", "B_bookshelf"), ("A_stock", "C_simpleui"),
        ("A_stock", "D_zenos"), ("A_stock", "E_project_title"), ("A_stock", "F_vos"),
        ("C_simpleui", "G_simpleui_bookshelf"),
        ("D_zenos", "H_zenos_bookshelf"),
        ("F_vos", "I_vos_bookshelf"),
        ("C_simpleui", "J_simpleui_vos"),
        ("J_simpleui_vos", "K_simpleui_vos_bookshelf"),
        ("E_project_title", "L_project_title_vos"),
        ("R0_stock", "R1_bookshelf"),
        ("R0_stock", "R2_simpleui"), ("R0_stock", "R3_zenos"),
        ("R0_stock", "R4_project_title"), ("R0_stock", "R5_vos"),
        ("R2_simpleui", "R6_simpleui_bookshelf"),
        ("R3_zenos", "R7_zenos_bookshelf"),
        ("R5_vos", "R8_vos_bookshelf"),
        ("R2_simpleui", "R9_simpleui_vos"),
        ("R9_simpleui_vos", "R10_simpleui_vos_bookshelf"),
        ("R4_project_title", "R11_project_title_vos"),
    ]
    primary = {
        "library_sequential_paging", "library_cached_paging",
        "bookshelf_sequential_paging", "bookshelf_cached_paging",
        "bookshelf_sequential_paging_anim_off", "bookshelf_cached_paging_anim_off",
    }
    index = {}
    for row in rows:
        if row.get("Status") != "PASS" or row.get("Scenario") not in primary:
            continue
        med = row.get("wall_time_ms_median")
        p10 = row.get("wall_time_ms_p10")
        p90 = row.get("wall_time_ms_p90")
        bpp = row.get("visible_count_before_median")
        if not isinstance(med, (int, float)):
            continue
        key = (row.get("Mode"), row.get("Dataset"), row.get("BookCount"), row.get("Scenario"), row.get("Stack"))
        index[key] = (med, p10, p90, bpp)

    findings = []
    for left, right in pairs:
        contexts = sorted({key[:4] for key in index if key[4] == left}, key=lambda values: tuple(str(v) for v in values))
        for context in contexts:
            left_entry = index.get(context + (left,))
            right_entry = index.get(context + (right,))
            if left_entry is None or right_entry is None:
                continue
            left_med, left_p10, left_p90, left_bpp = left_entry
            right_med, right_p10, right_p90, right_bpp = right_entry
            if left_med == right_med:
                continue
            lower_name, lower_med, lower_p10, lower_p90, lower_bpp, higher_name, higher_med, higher_p10, higher_p90, higher_bpp = (
                (left, left_med, left_p10, left_p90, left_bpp, right, right_med, right_p10, right_p90, right_bpp)
                if left_med < right_med else (right, right_med, right_p10, right_p90, right_bpp, left, left_med, left_p10, left_p90, left_bpp)
            )
            relative = (higher_med - lower_med) / higher_med * 100 if higher_med else 0.0
            mode, dataset, books, scenario = context

            overlap = (lower_p10 is not None and higher_p90 is not None and lower_p90 is not None and higher_p10 is not None) and (lower_p10 <= higher_p90 and higher_p10 <= lower_p90)
            ux_note = ""
            if lower_bpp is not None and higher_bpp is not None and lower_bpp != higher_bpp:
                ux_note = f" (UX-level comparison: books/page differs, {fmt(lower_bpp)} vs {fmt(higher_bpp)})"

            if overlap:
                findings.append(
                    f"- `{lower_name}` has a lower descriptive median than `{higher_name}` "
                    f"for `{scenario}` ({mode}, {dataset}, {books} books): "
                    f"{lower_med:.3f} ms vs {higher_med:.3f} ms ({relative:.1f}% lower){ux_note}. "
                    f"Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload."
                )
            else:
                findings.append(
                    f"- `{lower_name}` has a lower descriptive median than `{higher_name}` "
                    f"for `{scenario}` ({mode}, {dataset}, {books} books): "
                    f"{lower_med:.3f} ms vs {higher_med:.3f} ms ({relative:.1f}% lower){ux_note}."
                )
    return findings


def data_report(rows: list[dict[str, Any]], scope: str, records: list[dict[str, Any]]) -> Path:
    output = RESULTS / ("BOOKENDS_REPORT.md" if scope == "bookends_control" else "REPORT.md")
    status_counts = Counter(row["Status"] for row in rows)
    lock_hashes = sorted({
        str(record.get("campaign_environment", {}).get("versions_lock_sha256"))
        for record in records
        if record.get("campaign_environment", {}).get("versions_lock_sha256")
    })
    flash_settings = sorted(
        {record.get("emulate_reader_flash_ms") for record in records},
        key=lambda value: (value is not None, str(value)),
    )
    flash_text = ", ".join("unset" if value is None else str(value) for value in flash_settings)
    lines = [
        "# KOReader UI Benchmark Report", "",
        "> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.", "",
        f"Scope: `{scope}`", "",
        f"Versions lock SHA-256: `{', '.join(lock_hashes) if lock_hashes else 'unknown'}`",
        f"Reader flash setting: `{flash_text or 'unknown'}`", "",
        f"Aggregated rows: {len(rows)}; PASS={status_counts['PASS']}; "
        f"FAILED={status_counts['FAILED']}; UNSUPPORTED={status_counts['UNSUPPORTED']}; "
        f"DEPRECATED={status_counts['DEPRECATED_INVALID_FOR_RANKING']}.", "",
    ]
    manifest_path = RESULTS / "real_corpus_manifest.json"
    if any(row.get("Dataset") == "real_2692" for row in rows) and manifest_path.is_file():
        try:
            layout = json.loads(manifest_path.read_text()).get("working_corpus_layout", {})
        except (OSError, json.JSONDecodeError):
            layout = {}
        root_books = layout.get("root_books")
        folders = layout.get("folders")
        if isinstance(root_books, int) and isinstance(folders, dict):
            root_entries = root_books + len(folders)
            lines += [
                f"`Real 2692` names the complete corpus. Paging traverses its root with "
                f"**{root_entries} visible entries ({root_books} books + {len(folders)} folders)**; "
                "the remaining EPUBs are inside those folders. `Books/page` always reports "
                "the visible page size, not `2692 / page size`.", "",
            ]
    lines += [
        "## Default UI paging", "",
        "| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |",
        "|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|",
    ]

    default_contexts = sorted({
        (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"])
        for r in rows if r["Scenario"] in {"library_sequential_paging", "library_cached_paging"}
    }, key=lambda t: tuple(str(v) for v in t))

    for stack, mode, dataset, books in default_contexts:
        seq_row = next((r for r in rows if (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"], r["Scenario"]) == (stack, mode, dataset, books, "library_sequential_paging")), None)
        cached_row = next((r for r in rows if (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"], r["Scenario"]) == (stack, mode, dataset, books, "library_cached_paging")), None)

        vis_med = (seq_row and seq_row.get("visible_count_before_median")) or (cached_row and cached_row.get("visible_count_before_median"))
        vis_min = (seq_row and seq_row.get("visible_count_before_min")) or (cached_row and cached_row.get("visible_count_before_min"))
        vis_max = (seq_row and seq_row.get("visible_count_before_max")) or (cached_row and cached_row.get("visible_count_before_max"))
        total_p = (seq_row and seq_row.get("total_pages_median")) or (cached_row and cached_row.get("total_pages_median"))

        if vis_med is not None:
            if vis_min == vis_max:
                bpp_str = f"{int(vis_med)}" if vis_med == int(vis_med) else f"{vis_med:.1f}"
            else:
                bpp_str = f"{fmt(vis_med)} ({int(vis_min)}–{int(vis_max)})"
        else:
            bpp_str = "—"

        seq_runs = seq_row.get("ProcessRuns", 0) if seq_row else 0
        cac_runs = cached_row.get("ProcessRuns", 0) if cached_row else 0
        seq_n = seq_row.get("PassSamples", 0) if seq_row else 0
        cac_n = cached_row.get("PassSamples", 0) if cached_row else 0
        runs_str = f"{seq_runs}/{cac_runs}"
        samples_str = f"{seq_n}/{cac_n}"

        seq_med = fmt(seq_row.get("wall_time_ms_median")) if seq_row else "—"
        seq_p90 = fmt(seq_row.get("wall_time_ms_p90")) if seq_row else "—"
        seq_min = fmt(seq_row.get("wall_time_ms_min")) if seq_row else "—"
        seq_max = fmt(seq_row.get("wall_time_ms_max")) if seq_row else "—"

        cached_med = fmt(cached_row.get("wall_time_ms_median")) if cached_row else "—"
        cached_p90 = fmt(cached_row.get("wall_time_ms_p90")) if cached_row else "—"
        cached_min = fmt(cached_row.get("wall_time_ms_min")) if cached_row else "—"
        cached_max = fmt(cached_row.get("wall_time_ms_max")) if cached_row else "—"

        lines.append(
            f"| {stack} | {mode} | {dataset} | {books} | {bpp_str} | {fmt(total_p)} | {runs_str} | {samples_str} | "
            f"{seq_med} | {seq_p90} | {seq_min} | {seq_max} | "
            f"{cached_med} | {cached_p90} | {cached_min} | {cached_max} |"
        )

    if scope == "bookends_control":
        control_stacks = sorted({
            row["Stack"] for row in rows
            if row["Scenario"] == "memory:post_reader_cycles_forced_gc"
        })
        if control_stacks:
            lines += [
                "", "## Bookends reader control", "",
                "Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. "
                "There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.", "",
                "| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |",
                "|:--|--:|--:|--:|:--|--:|--:|",
            ]
            memory_by_stack: dict[str, dict[str, Any]] = {}
            for stack in control_stacks:
                memory = next(row for row in rows if
                              row["Stack"] == stack and
                              row["Scenario"] == "memory:post_reader_cycles_forced_gc")
                memory_by_stack[stack] = memory
                reader_turn = next((row for row in rows if
                                    row["Stack"] == stack and row["Scenario"] == "reader_page_turn"), None)
                open_minimal = next((row for row in rows if
                                     row["Stack"] == stack and row["Scenario"] == "open_book_minimal"), None)
                heap_median = numeric(memory.get("forced_gc_live_heap_kb_median"))
                heap_min = numeric(memory.get("forced_gc_live_heap_kb_min"))
                heap_max = numeric(memory.get("forced_gc_live_heap_kb_max"))
                heap_spread = "—" if heap_min is None or heap_max is None else \
                    f"{fmt(heap_min / 1024)}–{fmt(heap_max / 1024)}"
                lines.append(
                    f"| {stack} | {memory['ProcessRuns']} | {memory['PassSamples']} | "
                    f"{fmt(heap_median / 1024 if heap_median is not None else None)} | {heap_spread} | "
                    f"{fmt(reader_turn.get('wall_time_ms_median') if reader_turn else None)} | "
                    f"{fmt(open_minimal.get('wall_time_ms_median') if open_minimal else None)} |"
                )
            stock = memory_by_stack.get("A_stock")
            bookends = memory_by_stack.get("K_stock_bookends")
            stock_median = numeric(stock.get("forced_gc_live_heap_kb_median")) if stock else None
            bookends_median = numeric(bookends.get("forced_gc_live_heap_kb_median")) if bookends else None
            if stock_median is not None and bookends_median is not None:
                lines += [
                    "",
                    f"The observed median forced-GC heap difference in this control is "
                    f"**{(bookends_median - stock_median) / 1024:+.3f} MiB**. This is a descriptive "
                    "within-process comparison, not a causal or cross-device estimate.",
                ]

    bs_contexts = sorted({
        (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"])
        for r in rows if r["Scenario"].startswith("bookshelf_") and "paging" in r["Scenario"]
    }, key=lambda t: tuple(str(v) for v in t))

    if bs_contexts:
        lines += [
            "", "## Bookshelf paging", "",
            "| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |",
            "|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|",
        ]
        for stack, mode, dataset, books in bs_contexts:
            # Mode 1: animation_on_default
            seq_def = next((r for r in rows if (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"], r["Scenario"]) == (stack, mode, dataset, books, "bookshelf_sequential_paging")), None)
            cac_def = next((r for r in rows if (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"], r["Scenario"]) == (stack, mode, dataset, books, "bookshelf_cached_paging")), None)
            vis_def = (seq_def and seq_def.get("visible_count_before_median")) or (cac_def and cac_def.get("visible_count_before_median"))
            vis_def_min = (seq_def and seq_def.get("visible_count_before_min")) or (cac_def and cac_def.get("visible_count_before_min"))
            vis_def_max = (seq_def and seq_def.get("visible_count_before_max")) or (cac_def and cac_def.get("visible_count_before_max"))
            total_p_def = (seq_def and seq_def.get("total_pages_median")) or (cac_def and cac_def.get("total_pages_median"))
            if vis_def is not None:
                bpp_def = f"{int(vis_def)}" if vis_def_min == vis_def_max else f"{fmt(vis_def)} ({int(vis_def_min)}–{int(vis_def_max)})"
            else:
                bpp_def = "—"

            if seq_def or cac_def:
                seq_runs = seq_def.get("ProcessRuns", 0) if seq_def else 0
                cac_runs = cac_def.get("ProcessRuns", 0) if cac_def else 0
                seq_n = seq_def.get("PassSamples", 0) if seq_def else 0
                cac_n = cac_def.get("PassSamples", 0) if cac_def else 0
                lines.append(
                    f"| {stack} | {mode} | {dataset} | {books} | default (medium) | {bpp_def} | {fmt(total_p_def)} | {seq_runs}/{cac_runs} | {seq_n}/{cac_n} | "
                    f"{fmt(seq_def.get('wall_time_ms_median') if seq_def else None)} | {fmt(seq_def.get('wall_time_ms_p90') if seq_def else None)} | "
                    f"{fmt(seq_def.get('wall_time_ms_min') if seq_def else None)} | {fmt(seq_def.get('wall_time_ms_max') if seq_def else None)} | "
                    f"{fmt(cac_def.get('wall_time_ms_median') if cac_def else None)} | {fmt(cac_def.get('wall_time_ms_p90') if cac_def else None)} | "
                    f"{fmt(cac_def.get('wall_time_ms_min') if cac_def else None)} | {fmt(cac_def.get('wall_time_ms_max') if cac_def else None)} |"
                )

            # Mode 2: animation_off
            seq_off = next((r for r in rows if (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"], r["Scenario"]) == (stack, mode, dataset, books, "bookshelf_sequential_paging_anim_off")), None)
            cac_off = next((r for r in rows if (r["Stack"], r["Mode"], r["Dataset"], r["BookCount"], r["Scenario"]) == (stack, mode, dataset, books, "bookshelf_cached_paging_anim_off")), None)
            vis_off = (seq_off and seq_off.get("visible_count_before_median")) or (cac_off and cac_off.get("visible_count_before_median"))
            vis_off_min = (seq_off and seq_off.get("visible_count_before_min")) or (cac_off and cac_off.get("visible_count_before_min"))
            vis_off_max = (seq_off and seq_off.get("visible_count_before_max")) or (cac_off and cac_off.get("visible_count_before_max"))
            total_p_off = (seq_off and seq_off.get("total_pages_median")) or (cac_off and cac_off.get("total_pages_median"))
            if vis_off is not None:
                bpp_off = f"{int(vis_off)}" if vis_off_min == vis_off_max else f"{fmt(vis_off)} ({int(vis_off_min)}–{int(vis_off_max)})"
            else:
                bpp_off = "—"

            if seq_off or cac_off:
                seq_runs = seq_off.get("ProcessRuns", 0) if seq_off else 0
                cac_runs = cac_off.get("ProcessRuns", 0) if cac_off else 0
                seq_n = seq_off.get("PassSamples", 0) if seq_off else 0
                cac_n = cac_off.get("PassSamples", 0) if cac_off else 0
                lines.append(
                    f"| {stack} | {mode} | {dataset} | {books} | off | {bpp_off} | {fmt(total_p_off)} | {seq_runs}/{cac_runs} | {seq_n}/{cac_n} | "
                    f"{fmt(seq_off.get('wall_time_ms_median') if seq_off else None)} | {fmt(seq_off.get('wall_time_ms_p90') if seq_off else None)} | "
                    f"{fmt(seq_off.get('wall_time_ms_min') if seq_off else None)} | {fmt(seq_off.get('wall_time_ms_max') if seq_off else None)} | "
                    f"{fmt(cac_off.get('wall_time_ms_median') if cac_off else None)} | {fmt(cac_off.get('wall_time_ms_p90') if cac_off else None)} | "
                    f"{fmt(cac_off.get('wall_time_ms_min') if cac_off else None)} | {fmt(cac_off.get('wall_time_ms_max') if cac_off else None)} |"
                )

    unsupported_rows = [r for r in rows if r.get("Status") == "UNSUPPORTED"]
    if unsupported_rows:
        lines += [
            "", "## Unsupported Configurations", "",
            "| Stack | Mode | Dataset | Books | Scenario | Status | Reason |",
            "|:--|:--|:--|--:|:--|:--|:--|",
        ]
        for r in unsupported_rows:
            lines.append(f"| {r['Stack']} | {r['Mode']} | {r['Dataset']} | {r['BookCount']} | {r['Scenario']} | UNSUPPORTED | {r.get('FailureReason', '—')} |")

    findings = comparison_findings(rows)
    if findings:
        lines += ["", "## Comparative Findings", ""] + findings

    lines += [
        "", "## All Scenario Results", "",
        "| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |",
        "|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|",
    ]
    for row in rows:
        if not (row["Scenario"].startswith("process:") or "wall_time_ms_median" in row):
            continue
        spread = f"{fmt(row.get('wall_time_ms_min'))}–{fmt(row.get('wall_time_ms_max'))}"
        lines.append(
            f"| {row['Stack']} | {row['Mode']} | {row['Dataset']} | {row['BookCount']} | "
            f"{row['Scenario']} | {row['Status']} | {row['PassSamples']} | "
            f"{fmt(row.get('wall_time_ms_median'))} | {fmt(row.get('wall_time_ms_p10'))} | {fmt(row.get('wall_time_ms_p90'))} | {spread} |"
        )
    memory_rows = [r for r in rows if r["Scenario"].startswith("memory:")]
    if memory_rows:
        lines += [
            "", "## Memory Checkpoints", "",
            "| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |",
            "|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|",
        ]
        for row in memory_rows:
            heap_spread = f"{fmt(row.get('forced_gc_live_heap_kb_min'))}–{fmt(row.get('forced_gc_live_heap_kb_max'))}"
            lines.append(
                f"| {row['Stack']} | {row['Mode']} | {row['Dataset']} | {row['BookCount']} | "
                f"{row['Scenario'].replace('memory:', '')} | {row['Status']} | {row['ProcessRuns']} | {row['PassSamples']} | "
                f"{fmt(row.get('forced_gc_live_heap_kb_median'))} | {fmt(row.get('forced_gc_live_heap_kb_p90'))} | {heap_spread} | "
                f"{fmt(row.get('natural_lua_heap_kb_median'))} | {fmt(row.get('rss_kb_median'))} |"
            )
    findings = comparison_findings(rows)
    lines += ["", "## Data-derived comparisons", ""]
    lines += findings or ["No complete paired comparisons are available yet."]
    lines += ["", "## Interpretation limits", "",
              "These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.", ""]
    output.write_text("\n".join(lines))
    return output


def _write_svg_bar(path: Path, title: str, ylabel: str,
                   labels: list[str], values: list[float]) -> None:
    from html import escape
    width = max(800, len(labels) * 70)
    height, left, top, bottom = 520, 70, 55, 150
    plot_h = height - top - bottom
    maximum = max(values) if values else 1.0
    maximum = maximum if maximum > 0 else 1.0
    bar_w = max(8, (width - left - 20) / max(1, len(values)) * 0.7)
    step = (width - left - 20) / max(1, len(values))
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="28" text-anchor="middle" font-family="sans-serif" font-size="18">{escape(title)}</text>',
        f'<text x="18" y="{top + plot_h/2}" transform="rotate(-90 18 {top + plot_h/2})" text-anchor="middle" font-family="sans-serif" font-size="12">{escape(ylabel)}</text>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="black"/>',
        f'<line x1="{left}" y1="{top+plot_h}" x2="{width-20}" y2="{top+plot_h}" stroke="black"/>',
    ]
    for index, (label, value) in enumerate(zip(labels, values)):
        x = left + index * step + (step - bar_w) / 2
        bar_h = value / maximum * plot_h
        y = top + plot_h - bar_h
        parts.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{bar_w:.2f}" height="{bar_h:.2f}" fill="#3978b5"/>')
        parts.append(f'<text x="{x + bar_w/2:.2f}" y="{y-4:.2f}" text-anchor="middle" font-family="sans-serif" font-size="9">{value:.2f}</text>')
        parts.append(f'<text x="{x + bar_w/2:.2f}" y="{top+plot_h+12}" transform="rotate(55 {x + bar_w/2:.2f} {top+plot_h+12})" text-anchor="start" font-family="sans-serif" font-size="9">{escape(label)}</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts))


def _generate_svg_charts(rows: list[dict[str, Any]], charts_dir: Path) -> list[Path]:
    specs = [
        ("warm_library_navigation.svg", "Warm library navigation", "Median latency (ms)",
         [r for r in rows if r.get("Mode") == "warm" and r.get("Scenario") in {"library_first_render", "library_sequential_paging", "library_cached_paging"}],
         "wall_time_ms_median"),
        ("steady_restart.svg", "Steady-state restart to usable library", "Median latency (ms)",
         [r for r in rows if r.get("Mode") in {"steady_state_cold", "real_steady_cold"} and r.get("Scenario") == "process:spawn_to_library_ready_ms"],
         "wall_time_ms_median"),
        ("live_lua_heap.svg", "Forced-GC live Lua heap", "KiB",
         [r for r in rows if r.get("Scenario") == "memory:post_library_render_idle"],
         "forced_gc_live_heap_kb_median"),
    ]
    outputs = []
    for filename, title, ylabel, selected, key in specs:
        selected = [r for r in selected if r.get("Status") == "PASS" and isinstance(r.get(key), (int, float))]
        if selected:
            path = charts_dir / filename
            _write_svg_bar(path, title, ylabel, [f"{r['Stack']} {r['Scenario']}" for r in selected], [r[key] for r in selected])
            outputs.append(path)
    refresh = [r for r in rows if r.get("Mode") == "warm" and r.get("Scenario") == "library_sequential_paging"
               and r.get("Status") == "PASS" and isinstance(r.get("unique_dirty_pct_median"), (int, float))
               and isinstance(r.get("cumulative_dirty_screen_equivalents_median"), (int, float))]
    if refresh:
        labels, values = [], []
        for row in refresh:
            labels.extend([f"{row['Stack']} unique", f"{row['Stack']} cumulative"])
            values.extend([row["unique_dirty_pct_median"], row["cumulative_dirty_screen_equivalents_median"] * 100])
        path = charts_dir / "refresh_dirty_work.svg"
        _write_svg_bar(path, "Refresh and dirty work: sequential paging", "Percent / screen-equivalent percent", labels, values)
        outputs.append(path)
    return outputs


def generate_charts(rows: list[dict[str, Any]]) -> list[Path]:
    charts_dir = RESULTS / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib unavailable; generating dependency-free SVG charts")
        return _generate_svg_charts(rows, charts_dir)

    outputs = []

    def bar_chart(selected: list[dict[str, Any]], value_key: str, title: str, ylabel: str, filename: str) -> None:
        selected = [row for row in selected if isinstance(row.get(value_key), (int, float)) and row.get("Status") == "PASS"]
        if not selected:
            return
        labels = [f"{row['Stack']}\n{row['Scenario'].replace('process:', '')}" for row in selected]
        values = [row[value_key] for row in selected]
        width = max(8, min(22, len(labels) * 0.65))
        fig, ax = plt.subplots(figsize=(width, 6))
        ax.bar(range(len(values)), values)
        ax.set_xticks(range(len(labels)), labels, rotation=55, ha="right", fontsize=8)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        fig.tight_layout()
        output = charts_dir / filename
        fig.savefig(output, dpi=180)
        plt.close(fig)
        outputs.append(output)

    bar_chart(
        [r for r in rows if r.get("Mode") == "warm" and r.get("Scenario") in
         {"library_first_render", "library_sequential_paging", "library_cached_paging"}],
        "wall_time_ms_median", "Warm library navigation", "Median latency (ms)",
        "warm_library_navigation.png",
    )
    bar_chart(
        [r for r in rows if r.get("Mode") in {"steady_state_cold", "real_steady_cold"}
         and r.get("Scenario") == "process:spawn_to_library_ready_ms"],
        "wall_time_ms_median", "Steady-state restart to usable library", "Median latency (ms)",
        "steady_restart.png",
    )
    bar_chart(
        [r for r in rows if r.get("Scenario") == "memory:post_library_render_idle"],
        "forced_gc_live_heap_kb_median", "Forced-GC live Lua heap", "KiB",
        "live_lua_heap.png",
    )
    refresh_rows = [r for r in rows if r.get("Mode") == "warm"
                    and r.get("Scenario") == "library_sequential_paging"
                    and r.get("Status") == "PASS"
                    and isinstance(r.get("unique_dirty_pct_median"), (int, float))
                    and isinstance(r.get("cumulative_dirty_screen_equivalents_median"), (int, float))]
    if refresh_rows:
        labels = [str(r["Stack"]) for r in refresh_rows]
        unique = [r["unique_dirty_pct_median"] for r in refresh_rows]
        cumulative = [r["cumulative_dirty_screen_equivalents_median"] * 100 for r in refresh_rows]
        fig, ax = plt.subplots(figsize=(max(8, len(labels) * 0.65), 6))
        positions = list(range(len(labels)))
        ax.bar([p - 0.2 for p in positions], unique, width=0.4, label="Unique dirty %")
        ax.bar([p + 0.2 for p in positions], cumulative, width=0.4, label="Cumulative screen-equivalent %")
        ax.set_xticks(positions, labels, rotation=55, ha="right", fontsize=8)
        ax.set_ylabel("Percent / screen-equivalent percent")
        ax.set_title("Refresh and dirty work: sequential paging")
        ax.legend()
        fig.tight_layout()
        output = charts_dir / "refresh_dirty_work.png"
        fig.savefig(output, dpi=180)
        plt.close(fig)
        outputs.append(output)
    return outputs


def audit_records(records: list[dict[str, Any]], scope: str, strict: bool = True) -> tuple[int, list[str]]:
    PAGING_SCENARIOS = {
        "library_sequential_paging", "library_cached_paging",
        "bookshelf_sequential_paging", "bookshelf_cached_paging",
        "bookshelf_sequential_paging_anim_off", "bookshelf_cached_paging_anim_off",
    }
    PROBE_SCENARIOS = {
        "smoke_probe_step_2_to_3", "bookshelf_probe_step_2_to_3",
        "paging_probe_step_2_to_3",
    }
    ALL_MEASURED_PAGING = PAGING_SCENARIOS | PROBE_SCENARIOS
    violations = []
    total_verified_transitions = 0

    for record in records:
        path = record.get("_path", record.get("run_id", "unknown"))
        scenarios = record.get("scenarios", {})
        deprecated_found = DEPRECATED_SCENARIOS & set(scenarios)
        if deprecated_found:
            msg = f"{path}: contains deprecated scenarios {sorted(deprecated_found)}"
            if strict:
                violations.append(msg)

        for sc_name, sc_data in scenarios.items():
            if not isinstance(sc_data, dict):
                continue
            status = sc_data.get("status")
            if sc_name == "smoke_noop_guard":
                if status != "PASS" or sc_data.get("attempted_status") != "FAILED":
                    violations.append(f"{path}: smoke no-op guard did not reject transition")
                continue
            if status == "UNSUPPORTED":
                if not sc_data.get("reason"):
                    violations.append(f"{path}: UNSUPPORTED scenario {sc_name} missing reason")
                if sc_name in PAGING_SCENARIOS and record.get("profile") in {"paging", "smoke_validation"}:
                    violations.append(
                        f"{path}: measured paging scenario {sc_name} is UNSUPPORTED (zero pages available) — "
                        "the dataset must yield real paging data, not a silent skip"
                    )
                continue

            iterations = sc_data.get("iterations", [])
            if sc_name in ALL_MEASURED_PAGING:
                if status != "PASS":
                    violations.append(f"{path}: measured paging scenario {sc_name} has status {status}")
                req = sc_data.get("requested_transitions")
                act = sc_data.get("actual_transitions")
                if req is None or act is None:
                    violations.append(f"{path}: {sc_name} missing transition count metadata")
                else:
                    if act != req:
                        violations.append(f"{path}: {sc_name} transition count mismatch (actual={act} != requested={req})")
                    if len(iterations) != act:
                        violations.append(f"{path}: {sc_name} iteration count mismatch (len={len(iterations)} != actual={act})")

                if sc_name.startswith("bookshelf_"):
                    strict_bookshelf_paging = record.get("profile") in {"paging", "smoke_validation", "real"}
                    if strict_bookshelf_paging:
                        min_pages = 3 if sc_name in PROBE_SCENARIOS else 2
                        if sc_data.get("total_pages", 0) < min_pages:
                            violations.append(f"{path}: {sc_name} bookshelf total_pages < {min_pages} ({sc_data.get('total_pages')})")
                        if not sc_data.get("animation_verified"):
                            violations.append(f"{path}: {sc_name} bookshelf animation unverified")

                if sc_name.endswith("_sequential_paging") or sc_name.endswith("_sequential_paging_anim_off"):
                    for idx, it in enumerate(iterations):
                        expected_before, expected_after = idx + 1, idx + 2
                        if it.get("page_before") != expected_before or it.get("page_after") != expected_after:
                            violations.append(
                                f"{path}: {sc_name}[{idx}] broken sequential chain "
                                f"(expected {expected_before}->{expected_after}, got "
                                f"{it.get('page_before')}->{it.get('page_after')})"
                            )

                if sc_name.endswith("_cached_paging") or sc_name.endswith("_cached_paging_anim_off"):
                    if not sc_data.get("warmup_verified"):
                        violations.append(f"{path}: {sc_name} unverified cached warmup")
                    for idx, it in enumerate(iterations):
                        expected_before, expected_after = (1, 2) if idx % 2 == 0 else (2, 1)
                        if it.get("page_before") != expected_before or it.get("page_after") != expected_after:
                            violations.append(
                                f"{path}: {sc_name}[{idx}] broken cached alternation "
                                f"(expected {expected_before}->{expected_after}, got "
                                f"{it.get('page_before')}->{it.get('page_after')})"
                            )

                if sc_name in ALL_MEASURED_PAGING and status == "PASS":
                    previous_hash, previous_idx = None, None
                    for idx, it in enumerate(iterations):
                        if it.get("status") != "PASS":
                            continue
                        current = it.get("framebuffer_hash")
                        if current and previous_hash and current == previous_hash:
                            violations.append(
                                f"{path}: {sc_name} screen did not change between [{previous_idx}] "
                                f"and [{idx}] (identical framebuffer {current})"
                            )
                        if current:
                            previous_hash, previous_idx = current, idx

                if sc_name in PROBE_SCENARIOS and status == "PASS":
                    shot_b = sc_data.get("screenshot_before")
                    shot_a = sc_data.get("screenshot_after")
                    if not shot_b or not shot_a:
                        violations.append(f"{path}: {sc_name} missing mandatory probe screenshots")
                    else:
                        hash_b_raw = sc_data.get("screenshot_before_sha256")
                        hash_a_raw = sc_data.get("screenshot_after_sha256")
                        if not hash_b_raw or not hash_a_raw:
                            violations.append(f"{path}: {sc_name} missing mandatory screenshot SHA256 hashes in raw JSON")
                        raw_p = Path(path) if path != "unknown" else None
                        if raw_p and raw_p.exists():
                            shot_dir = raw_p.parent.parent / "screenshots" / record.get("run_id", raw_p.stem)
                            path_b = shot_dir / shot_b
                            path_a = shot_dir / shot_a
                            ok_b, err_b, _, _ = verify_png_file(path_b)
                            ok_a, err_a, _, _ = verify_png_file(path_a)
                            if not ok_b:
                                violations.append(f"{path}: {sc_name} screenshot_before invalid ({err_b})")
                            if not ok_a:
                                violations.append(f"{path}: {sc_name} screenshot_after invalid ({err_a})")
                            if ok_b and ok_a:
                                hb = hashlib.sha256(path_b.read_bytes()).hexdigest()
                                ha = hashlib.sha256(path_a.read_bytes()).hexdigest()
                                if hash_b_raw and hash_b_raw != hb:
                                    violations.append(f"{path}: {sc_name} screenshot_before_sha256 mismatch ({hash_b_raw} != {hb})")
                                if hash_a_raw and hash_a_raw != ha:
                                    violations.append(f"{path}: {sc_name} screenshot_after_sha256 mismatch ({hash_a_raw} != {ha})")
                                if hb == ha:
                                    violations.append(f"{path}: {sc_name} probe screenshots identical (no visual change)")

                for idx, it in enumerate(iterations):
                    if it.get("status") != "PASS":
                        continue
                    total_verified_transitions += 1
                    pb = it.get("page_before")
                    pa = it.get("page_after")
                    vb = it.get("visible_count_before")
                    va = it.get("visible_count_after")
                    ib = it.get("visible_items_before")
                    ia = it.get("visible_items_after")
                    sb = it.get("visible_signature_before")
                    sa = it.get("visible_signature_after")
                    tp = it.get("total_pages")

                    if pb is None or pa is None:
                        violations.append(f"{path}: {sc_name}[{idx}] missing page numbers")
                    elif pb == pa:
                        violations.append(f"{path}: {sc_name}[{idx}] no-op transition ({pb} -> {pa})")

                    if sc_name in PROBE_SCENARIOS:
                        if pb != 2 or pa != 3:
                            violations.append(f"{path}: {sc_name}[{idx}] invalid probe transition ({pb} -> {pa}, expected 2 -> 3)")

                    if sc_name.endswith("_sequential_paging") or sc_name.endswith("_sequential_paging_anim_off"):
                        if pb is not None and pa is not None and pa != pb + 1:
                            violations.append(f"{path}: {sc_name}[{idx}] non-sequential page transition ({pb} -> {pa})")

                    if vb is None or va is None or tp is None:
                        violations.append(f"{path}: {sc_name}[{idx}] missing page metadata")
                    else:
                        if vb <= 0 or va <= 0:
                            violations.append(f"{path}: {sc_name}[{idx}] zero visible items ({vb}, {va})")

                    if not isinstance(ib, list) or len(ib) == 0 or not isinstance(ia, list) or len(ia) == 0:
                        violations.append(f"{path}: {sc_name}[{idx}] missing/empty visible_items list")
                    elif vb is not None and len(ib) != vb:
                        violations.append(f"{path}: {sc_name}[{idx}] visible_count_before ({vb}) != len(visible_items_before) ({len(ib)})")
                    elif va is not None and len(ia) != va:
                        violations.append(f"{path}: {sc_name}[{idx}] visible_count_after ({va}) != len(visible_items_after) ({len(ia)})")

                    if sb is None or sa is None or sb == "" or sa == "":
                        violations.append(f"{path}: {sc_name}[{idx}] empty visible signature")
                    elif sb == sa:
                        violations.append(f"{path}: {sc_name}[{idx}] unchanged signature across page turn")

                    if sc_name.startswith("bookshelf_"):
                        refreshes = it.get("refresh_count", it.get("set_dirty_calls", 0))
                        if not isinstance(refreshes, (int, float)) or refreshes <= 0:
                            violations.append(f"{path}: {sc_name}[{idx}] no refresh/state-change evidence")
                    if it.get("measured_widget_on_stack") is not True:
                        violations.append(
                            f"{path}: {sc_name}[{idx}] measured widget was not on the window stack "
                            f"(top_widget={it.get('top_widget')})"
                        )
                    if not it.get("top_widget"):
                        violations.append(f"{path}: {sc_name}[{idx}] missing window-stack evidence")
                    if not it.get("framebuffer_hash"):
                        violations.append(f"{path}: {sc_name}[{idx}] missing framebuffer_hash evidence")

    return total_verified_transitions, violations


def audit_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    paging_scenarios = {
        "library_sequential_paging", "library_cached_paging",
        "bookshelf_sequential_paging", "bookshelf_cached_paging",
        "bookshelf_sequential_paging_anim_off", "bookshelf_cached_paging_anim_off",
        "smoke_probe_step_2_to_3", "bookshelf_probe_step_2_to_3",
        "paging_probe_step_2_to_3",
    }
    samples = 0
    real_transitions = 0
    noops = 0
    wraps = 0
    empty_shelves: set[tuple[str, str]] = set()
    books_per_page: dict[str, list[int]] = defaultdict(list)
    process_runs: dict[str, set[str]] = defaultdict(set)
    process_cell_samples: dict[str, int] = defaultdict(int)
    paging_roots: dict[str, str] = {}

    for record in records:
        path = record.get("_path", record.get("run_id", "unknown"))
        config = str(record.get("config", "unknown"))
        process_cell = ":".join(str(record.get(key, "unknown")) for key in ("phase", "config", "dataset_mode", "profile", "mode"))
        has_paging = False
        cell_samples = 0
        for scenario, data in record.get("scenarios", {}).items():
            if scenario not in paging_scenarios or not isinstance(data, dict):
                continue
            has_paging = True
            if scenario.startswith("bookshelf_") and record.get("profile") in {"paging", "smoke_validation", "real"}:
                if data.get("total_pages", 0) < 2:
                    empty_shelves.add((path, scenario))
            for iteration in data.get("iterations", []):
                if iteration.get("status") != "PASS":
                    continue
                samples += 1
                cell_samples += 1
                before = iteration.get("page_before")
                after = iteration.get("page_after")
                if before == after:
                    noops += 1
                if scenario.endswith("_sequential_paging") or scenario.endswith("_sequential_paging_anim_off"):
                    if isinstance(before, int) and isinstance(after, int) and after == 1 and before > 1:
                        wraps += 1
                if before != after and iteration.get("visible_signature_before") != iteration.get("visible_signature_after"):
                    real_transitions += 1
                for count in (iteration.get("visible_count_before"), iteration.get("visible_count_after")):
                    if isinstance(count, int) and count > 0:
                        books_per_page[config].append(count)
        if has_paging:
            process_runs[process_cell].add(path)
            if record.get("profile") in {"paging", "smoke_validation"}:
                process_cell_samples[process_cell] += cell_samples
            root = record.get("paging_root")
            if isinstance(root, dict) and root.get("path"):
                paging_roots[process_cell] = (
                    f"{Path(str(root['path'])).name} "
                    f"({root.get('book_count')} of {root.get('library_book_count')} books)"
                )

    zero_data_cells = sorted(cell for cell, count in process_cell_samples.items() if count == 0)

    return {
        "paging_roots": paging_roots,
        "paging_samples": samples,
        "real_transitions": real_transitions,
        "noops": noops,
        "wraps": wraps,
        "empty_shelves": len(empty_shelves),
        "process_runs": {key: len(value) for key, value in sorted(process_runs.items())},
        "books_per_page": {
            key: {"min": min(values), "max": max(values)}
            for key, values in sorted(books_per_page.items()) if values
        },
        "zero_data_cells": zero_data_cells,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("validation", "phase1", "phase2", "bookends_control", "all"), default="all")
    parser.add_argument("--run-dir", type=Path,
                        help="dated phase folder containing raw/, logs/, checkpoints/")
    args = parser.parse_args()
    global RESULTS, RAW
    if args.run_dir:
        RESULTS = args.run_dir.resolve()
        RAW = RESULTS / "raw"
    records = load_records(args.scope)

    # In active campaign runs (non-empty records and run-dir specified or scope given), audit strictly
    strict_audit = bool(args.run_dir)
    total_transitions, violations = audit_records(records, args.scope, strict=strict_audit)
    summary = audit_summary(records)
    print(
        "[AUDIT SUMMARY] "
        f"samples={summary['paging_samples']} "
        f"real_transitions={summary['real_transitions']} "
        f"noops={summary['noops']} "
        f"wraps={summary['wraps']} "
        f"empty_shelves={summary['empty_shelves']} "
        f"process_runs={json.dumps(summary['process_runs'], sort_keys=True)} "
        f"books_per_page_range={json.dumps(summary['books_per_page'], sort_keys=True)} "
        f"paging_roots={json.dumps(summary['paging_roots'], sort_keys=True, ensure_ascii=False)}"
    )
    if violations:
        print(f"AUDIT FAILED: {len(violations)} raw invariant violations found:")
        for v in violations:
            print(f"  - {v}")
        return 1

    if summary["zero_data_cells"]:
        print(f"AUDIT FAILED: {len(summary['zero_data_cells'])} paging process-cells produced zero measured transitions:")
        for cell in summary["zero_data_cells"]:
            print(f"  - {cell}")
        return 1

    if total_transitions > 0:
        print(f"[AUDIT PASS] Verified {total_transitions} paging transition samples across {len(records)} runs with zero invariant violations.")

    rows = aggregate_scenarios(records)
    add_external_timing_rows(records, rows)
    add_memory_rows(records, rows)
    add_disk_rows(records, rows)
    csv_path = write_csv(rows, args.scope)
    extra_csv_paths = []
    if args.scope == "all":
        phase1_rows = [row for row in rows if row.get("Phase") in {"phase1", "phase1_setup"}]
        phase2_rows = [row for row in rows if row.get("Phase") == "phase2"]
        extra_csv_paths = [write_csv(phase1_rows, "phase1"), write_csv(phase2_rows, "phase2")]
    report_path = validation_report(records) if args.scope == "validation" else data_report(rows, args.scope, records)
    chart_paths = [] if args.scope == "validation" else generate_charts(rows)
    print(f"Loaded {len(records)} schema-v2 records")
    print(f"Wrote {csv_path}")
    for extra_path in extra_csv_paths:
        print(f"Wrote {extra_path}")
    print(f"Wrote {report_path}")
    if chart_paths:
        print(f"Wrote {len(chart_paths)} charts to {chart_paths[0].parent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
