#!/usr/bin/env python3
"""Summarise an --energy run: work per window and for one hypothetical session.

The numbers say how much work each stack makes the emulator do, relative to Stock.
They are not battery figures: the energy cost of a wake-up or a refresh on a device
is not known here, and CPU time on this host does not transfer to a Kindle.
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path

SCREEN_PIXELS = 1236 * 1648
READER_MIN, LIBRARY_MIN, READER_TURNS, LIBRARY_TURNS, BOOK_CYCLES, NAV_CYCLES = 30, 5, 60, 10, 1, 3
SESSION_TEXT = (f"{READER_MIN} min reading, {READER_TURNS} page turns; {LIBRARY_MIN} min in the library, "
                f"{LIBRARY_TURNS} library pages, {NAV_CYCLES} folder visits; {BOOK_CYCLES} book open and close")
SESSION_S = (READER_MIN + LIBRARY_MIN) * 60
METRICS = ("cpu_total_ms", "wakeups", "tasks_fired", "refreshes", "flashing_refreshes", "screens")
WINDOW_ORDER = ("library_startup_tail", "library_idle", "library_paging", "book_cycles", "library_navigation",
                "reader_open_tail", "reader_idle", "reader_turns_short", "reader_turns_long",
                "reader_after_turns_tail", "library_after_close_tail")
IDLE_WINDOWS = ("library_idle", "reader_idle")
MIN_IDLE_S_FOR_RATES = 60   # a one-minute timer is only seen reliably from here up
MIN_STEADY_RUNS = 3
NEGATIVE_TERM_MS = 20       # smaller terms are noise
ACTION_WINDOWS = ("library_paging", "book_cycles", "library_navigation", "reader_turns_short", "reader_turns_long")
RUN_ID = re.compile(r"^energy_(?P<config>.+)_r(?P<round>\d+)$")


def window_metrics(window: dict, name: str = "") -> dict:
    flashing = (window.get("refresh_by_type") or {}).get("full") or {}
    # A quiet window ends with the harness's own wake-up, which is no work of the stack.
    harness_wakeups = 1 if name in IDLE_WINDOWS and window["wakeups"] > 0 else 0
    return {
        "wall_s": window["wall_s"], "actions": window.get("actions", 0),
        "cpu_total_ms": window["cpu_total_ms"], "wakeups": window["wakeups"] - harness_wakeups,
        "tasks_fired": window["tasks_fired"], "refreshes": window["refreshes"],
        "flashing_refreshes": flashing.get("count", 0),
        "screens": window["refresh_pixels"] / SCREEN_PIXELS,
        "cpu_children_ms": window.get("cpu_children_ms", 0),
    }


def session_for_run(windows: dict) -> dict:
    """Idle rate times minutes, plus each action's cost above the idle it overlaps.

    Each total is split into `idle` and `actions`. An action term below zero means the
    idle sample held work the action window did not, and is listed rather than clamped.
    """
    m = {name: window_metrics(w, name) for name, w in windows.items()}
    result = {}
    for key in METRICS:
        reader_rate = m["reader_idle"][key] / m["reader_idle"]["wall_s"]
        library_rate = m["library_idle"][key] / m["library_idle"]["wall_s"]

        def above(name: str, rate: float, count: float | None = None) -> float:
            w = m[name]
            extra = w[key] - rate * w["wall_s"]
            return extra / w["actions"] * count if count is not None else extra

        idle = reader_rate * READER_MIN * 60 + library_rate * LIBRARY_MIN * 60
        terms = {
            "reader_turns_long": above("reader_turns_long", reader_rate, READER_TURNS),
            "library_paging": above("library_paging", library_rate, LIBRARY_TURNS),
            "library_navigation": above("library_navigation", library_rate, NAV_CYCLES),
            "book_cycles": above("book_cycles", library_rate, BOOK_CYCLES),
            "reader_open_tail": above("reader_open_tail", reader_rate),
            "reader_after_turns_tail": above("reader_after_turns_tail", reader_rate),
            "library_after_close_tail": above("library_after_close_tail", library_rate),
        }
        result[key] = idle + sum(terms.values())
        result[f"{key}_idle"] = idle
        result[f"{key}_actions"] = sum(terms.values())
        if key == "cpu_total_ms":
            result["negative_cpu_terms"] = {k: v for k, v in terms.items() if v < -NEGATIVE_TERM_MS}
    return result


def spread(values: list[float]) -> dict:
    return {"median": statistics.median(values), "min": min(values), "max": max(values), "n": len(values)}


def summarize(runs: list[dict]) -> dict:
    """runs: raw artifacts. Round 0 is first-run work and stays out of the steady figures."""
    grouped: dict[str, dict] = {}
    for run in runs:
        match = RUN_ID.match(run["run_id"])
        if not match or run.get("run_status") != "PASS":
            continue
        slot = grouped.setdefault(match["config"], {"steady": [], "first": None})
        if int(match["round"]) == 0:
            slot["first"] = run
        else:
            slot["steady"].append(run)
    summary = {}
    for config, slot in grouped.items():
        steady = [r["energy"]["windows"] for r in slot["steady"]]
        entry = {"steady_runs": len(steady), "windows": {}, "session": {}, "idle_tasks": {}}
        if steady:
            for name in [n for n in WINDOW_ORDER if n in steady[0]]:
                rows = [window_metrics(w[name], name) for w in steady]
                entry["windows"][name] = {k: spread([r[k] for r in rows]) for k in rows[0]}
            sessions = [session_for_run(w) for w in steady]
            entry["session"] = {k: spread([s[k] for s in sessions])
                                for k in [f"{m}{part}" for m in METRICS for part in ("", "_idle", "_actions")]}
            entry["negative_cpu_terms"] = [s["negative_cpu_terms"] for s in sessions if s["negative_cpu_terms"]]
            entry["child_cpu"] = {
                name: spread([window_metrics(w[name])["cpu_children_ms"] for w in steady])
                for name in ACTION_WINDOWS + IDLE_WINDOWS if name in steady[0]}
            for name in ("library_idle", "reader_idle"):
                labels = {label for w in steady for label in w[name].get("tasks_by_source", {})}
                entry["idle_tasks"][name] = dict(sorted(
                    ((label, statistics.median(w[name].get("tasks_by_source", {}).get(label, 0) for w in steady))
                     for label in labels), key=lambda item: (-item[1], item[0])))
        if slot["first"]:
            entry["first_run"] = {name: window_metrics(w, name)
                                  for name, w in slot["first"]["energy"]["windows"].items()}
        summary[config] = entry
    return summary


def ratio(value: float, base: float) -> str:
    return f"×{value / base:.2f}" if base > 0 else "n/a"


def page_cost_lines(summary: dict) -> list[str]:
    """CPU per page above reader idle: a long run costing more per page means the plugin accumulates work."""
    lines = ["", "## Cost per page turn above reader idle", "",
             "| Config | 10 pages, CPU ms/page | 100 pages, CPU ms/page | Tail after 100 pages, CPU ms above idle |",
             "|---|---:|---:|---:|"]
    for config, e in summary.items():
        w = e["windows"]
        if not w:
            continue
        rate = w["reader_idle"]["cpu_total_ms"]["median"] / w["reader_idle"]["wall_s"]["median"]

        def above(name: str) -> float:
            return w[name]["cpu_total_ms"]["median"] - rate * w[name]["wall_s"]["median"]

        lines.append(
            f"| {config} | {above('reader_turns_short') / w['reader_turns_short']['actions']['median']:.1f} "
            f"| {above('reader_turns_long') / w['reader_turns_long']['actions']['median']:.1f} "
            f"| {above('reader_after_turns_tail'):.0f} |")
    return lines


def idle_rows(summary: dict) -> list[str]:
    lines = ["", "## Idle samples, as measured", "",
             "Few events, and a sample shorter than a one-minute timer: read these as counts, not as rates.", "",
             "| Config | Window | Wall s | CPU ms | Child CPU ms | Wake-ups, harness excluded | Timers | Refreshes |",
             "|---|---|---:|---:|---:|---:|---:|---:|"]
    for config, e in summary.items():
        for name in IDLE_WINDOWS:
            w = e["windows"].get(name)
            if w:
                lines.append(
                    f"| {config} | {name} | {w['wall_s']['median']:.0f} | {w['cpu_total_ms']['median']:.0f} "
                    f"| {w['cpu_children_ms']['median']:.0f} | {w['wakeups']['median']:.0f} "
                    f"| {w['tasks_fired']['median']:.0f} | {w['refreshes']['median']:.0f} |")
    return lines


def warnings(summary: dict) -> list[str]:
    lines = []
    for config, e in summary.items():
        if e["session"] and e["steady_runs"] < MIN_STEADY_RUNS:
            lines.append(f"- {config}: {e['steady_runs']} steady run(s), so no spread is known and ratios are indicative.")
        idle_walls = [e["windows"][n]["wall_s"]["median"] for n in IDLE_WINDOWS if n in e["windows"]]
        if idle_walls and min(idle_walls) < MIN_IDLE_S_FOR_RATES:
            s = e["session"]
            parts = ", ".join(
                f"{label} {s[f'{key}_idle']['median']:.0f} of {s[key]['median']:.0f}"
                for label, key in (("CPU ms", "cpu_total_ms"), ("timers", "tasks_fired"),
                                   ("wake-ups", "wakeups"), ("refreshes", "refreshes")))
            lines.append(f"- {config}: idle sample of {min(idle_walls):.0f} s, under {MIN_IDLE_S_FOR_RATES} s. "
                         f"Extrapolated from it: {parts}. Transient work in the sample is scored as sustained.")
        for name, c in e.get("child_cpu", {}).items():
            if c["max"] > 0:
                note = "Multiplied up in the extrapolated session." if name in IDLE_WINDOWS else ""
                lines.append(f"- {config}, {name}: child-process CPU in steady rounds, median {c['median']:.0f} ms, "
                             f"range {c['min']:.0f}–{c['max']:.0f}. Background extraction may not have finished. {note}".rstrip())
        for terms in e.get("negative_cpu_terms", []):
            shown = ", ".join(f"{k} {v:.0f} ms" for k, v in terms.items())
            lines.append(f"- {config}: action terms below zero, so the idle sample held extra work: {shown}.")
    return lines


def render(summary: dict, baseline: str = "R0_stock", unpinned: list | None = None) -> str:
    lines = ["# Energy proxies (emulator)", "",
             "Work relative to Stock, not battery. Median of steady runs.",
             "Actions are direct harness calls: gesture handling is not measured. Disk and network are not measured."]
    for state in unpinned or []:
        lines.append(f"Measured off its pin: {state['plugin']} at {state['head'][:7]}, pinned {state['pinned'][:7]}, "
                     f"{state['uncommitted_entries']} uncommitted entries.")
    lines += ["", f"## Hypothetical session: {SESSION_TEXT}", "",
              "### Actions, measured above idle and scaled by count", "",
              "| Config | Runs | CPU s | vs Stock | Wake-ups | vs Stock | Timers | vs Stock | Refreshes | vs Stock "
              "| Flashing | Screens | vs Stock |",
              "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    base_entry = summary.get(baseline, {})
    base = base_entry.get("session", {})

    def versus(s: dict, key: str) -> str:
        return ratio(s[key]["median"], base[key]["median"]) if base else "n/a"

    for config, e in summary.items():
        s = e["session"]
        if not s:
            continue
        lines.append(
            f"| {config} | {e['steady_runs']} | {s['cpu_total_ms_actions']['median'] / 1000:.2f} "
            f"| {versus(s, 'cpu_total_ms_actions')} "
            f"| {s['wakeups_actions']['median']:.0f} | {versus(s, 'wakeups_actions')} "
            f"| {s['tasks_fired_actions']['median']:.0f} | {versus(s, 'tasks_fired_actions')} "
            f"| {s['refreshes_actions']['median']:.0f} | {versus(s, 'refreshes_actions')} "
            f"| {s['flashing_refreshes_actions']['median']:.0f} "
            f"| {s['screens_actions']['median']:.1f} | {versus(s, 'screens_actions')} |")
    idle_window = base_entry.get("windows", {}).get("reader_idle")
    floor = idle_window["cpu_total_ms"]["median"] / idle_window["wall_s"]["median"] * SESSION_S if idle_window else 0
    base_above = base["cpu_total_ms"]["median"] - floor if base else 0
    lines += ["", "### Whole session, extrapolated from the idle sample", "",
              "Idle CPU is mostly the emulator's own floor, which a Kindle does not share. "
              "`Above floor` subtracts Stock's reader idle rate for the whole session. "
              "See the warnings before using these.", "",
              "| Config | CPU above floor, s | vs Stock | Idle part, s | Wake-ups | Timers | Refreshes |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for config, e in summary.items():
        s = e["session"]
        if not s:
            continue
        above_floor = s["cpu_total_ms"]["median"] - floor
        lines.append(
            f"| {config} | {above_floor / 1000:.2f} | {ratio(above_floor, base_above)} "
            f"| {s['cpu_total_ms_idle']['median'] / 1000:.1f} | {s['wakeups']['median']:.0f} "
            f"| {s['tasks_fired']['median']:.0f} | {s['refreshes']['median']:.0f} |")
    lines += idle_rows(summary)
    lines += ["", "## Warnings", ""] + (warnings(summary) or ["None."])
    first = {c: e["first_run"] for c, e in summary.items() if e.get("first_run")}
    if first:
        lines += ["", "## First run on a fresh home, all windows", "",
                  "| Config | CPU ms | Child CPU ms |", "|---|---:|---:|"]
        for config, windows in first.items():
            lines.append(f"| {config} | {sum(w['cpu_total_ms'] for w in windows.values()):.0f} "
                         f"| {sum(w['cpu_children_ms'] for w in windows.values()):.0f} |")
    lines += page_cost_lines(summary)
    lines += ["", "## Windows", "",
              "| Config | Window | Wall s | CPU ms [min–max] | Child CPU ms | CPU ms/min | Wake-ups | Timers | Refreshes | Flashing | Screens |",
              "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for config, e in summary.items():
        for name, w in e["windows"].items():
            c = w["cpu_total_ms"]
            per_min = c["median"] / w["wall_s"]["median"] * 60
            lines.append(
                f"| {config} | {name} | {w['wall_s']['median']:.0f} | {c['median']:.0f} [{c['min']:.0f}–{c['max']:.0f}] "
                f"| {w['cpu_children_ms']['median']:.0f} | {per_min:.0f} | {w['wakeups']['median']:.0f} "
                f"| {w['tasks_fired']['median']:.0f} | {w['refreshes']['median']:.0f} "
                f"| {w['flashing_refreshes']['median']:.0f} | {w['screens']['median']:.2f} |")
    lines += ["", "## Timers firing in idle", ""]
    for config, e in summary.items():
        for name, tasks in e["idle_tasks"].items():
            top = ", ".join(f"`{label}` {count:g}" for label, count in list(tasks.items())[:6]) or "none"
            lines.append(f"- {config}, {name}: {top}")
    return "\n".join(lines) + "\n"


def main() -> int:
    root = Path(sys.argv[1])
    runs = [json.loads(p.read_text()) for p in sorted((root / "raw").glob("energy_*.json"))]
    summary = summarize(runs)
    (root / "energy_summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    unpinned = next((r["campaign_environment"].get("unpinned_plugins") for r in runs
                     if r.get("campaign_environment", {}).get("unpinned_plugins")), None)
    text = render(summary, unpinned=unpinned)
    (root / "energy_summary.md").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
