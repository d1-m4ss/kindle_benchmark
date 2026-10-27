#!/usr/bin/env python3
"""Build the README summary charts from the published campaign CSVs.

Each row comes from the newest campaign that measured it (see SOURCES); the
charts are written to docs/charts/*.svg as plain, self-contained SVG.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "results" / "runs"
OUT = ROOT / "docs" / "charts"
BASE = "2026-10-27-m1n1mal-v3"
PT = "2026-10-27-pt-covers"
VOS = "2026-10-27-vos-141"
SOURCES = {"R4_project_title": PT, **{k: VOS for k in (
    "R5_vos", "R8_vos_bookshelf", "R9_simpleui_vos", "R10_simpleui_vos_bookshelf", "R11_project_title_vos")}}
NAMES = {
    "R0_stock": "Stock", "R1_bookshelf": "Bookshelf", "R2_simpleui": "SimpleUI", "R3_zenos": "ZenOS",
    "R4_project_title": "Project:Title", "R5_vos": "VOS", "R6_simpleui_bookshelf": "SimpleUI + Bookshelf",
    "R7_zenos_bookshelf": "ZenOS + Bookshelf", "R8_vos_bookshelf": "VOS + Bookshelf",
    "R9_simpleui_vos": "SimpleUI + VOS", "R10_simpleui_vos_bookshelf": "SimpleUI + VOS + Bookshelf",
    "R11_project_title_vos": "Project:Title + VOS", "R13_m1n1mal": "m1n1mal + pagecount",
}
_cache: dict[str, list[dict]] = {}


def metric(stack: str, scenario: str, mode: str, column: str = "wall_time_ms_median") -> float:
    campaign = SOURCES.get(stack, BASE)
    if campaign not in _cache:
        _cache[campaign] = list(csv.DictReader(open(RUNS / campaign / "phase2" / "RESULTS.csv")))
    for row in _cache[campaign]:
        if (row["Stack"], row["Scenario"], row["Mode"], row["Status"]) == (stack, scenario, mode, "PASS") and row.get(column):
            return float(row[column])
    raise KeyError((stack, scenario, mode))


def bars(title: str, unit: str, values: list[tuple[str, float]], path: Path, decimals: int = 0) -> None:
    values = sorted(values, key=lambda kv: kv[1])
    row_h, left, width, top = 24, 200, 760, 44
    height = top + row_h * len(values) + 16
    peak = max(v for _, v in values)
    scale = (width - left - 90) / peak
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Helvetica, Arial, sans-serif" font-size="13">',
           f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
           f'<text x="12" y="26" font-size="15" font-weight="bold" fill="#1f2328">{title}</text>']
    for i, (name, value) in enumerate(values):
        y = top + i * row_h
        color = "#2da44e" if name.startswith("m1n1mal") else "#0969da" if name == "Stock" else "#8c959f"
        w = max(1.0, value * scale)
        out.append(f'<text x="{left - 8}" y="{y + 15}" text-anchor="end" fill="#1f2328">{name}</text>')
        out.append(f'<rect x="{left}" y="{y + 3}" width="{w:.1f}" height="16" rx="2" fill="{color}"/>')
        out.append(f'<text x="{left + w + 6:.1f}" y="{y + 15}" fill="#57606a">{value:.{decimals}f} {unit}</text>')
    out.append("</svg>")
    path.write_text("\n".join(out) + "\n")


def bookends_control(path: Path) -> None:
    """Stock vs Stock + Bookends: three metrics, each pair drawn on its own scale."""
    base = RUNS / "2026-10-27-bookends" / "phase2"
    rows = list(csv.DictReader(open(base / "BOOKENDS_RESULTS.csv")))
    pick = lambda stack, scenario: float(next(r["wall_time_ms_median"] for r in rows
                                              if r["Stack"] == stack and r["Scenario"] == scenario and r["wall_time_ms_median"]))
    heap = {m.group(1): float(m.group(2)) for m in re.finditer(
        r"^\| (A_stock|K_stock_bookends) \| \d+ \| \d+ \| ([\d.]+) \|", (base / "BOOKENDS_REPORT.md").read_text(), re.M)}
    groups = [("Reader page turn", "ms", pick("A_stock", "reader_page_turn"), pick("K_stock_bookends", "reader_page_turn"), 1),
              ("Closing a book", "ms", pick("A_stock", "close_book"), pick("K_stock_bookends", "close_book"), 1),
              ("Live Lua heap", "MiB", heap["A_stock"], heap["K_stock_bookends"], 1)]
    width, left, row_h = 760, 170, 22
    height = 44 + len(groups) * (2 * row_h + 14) + 8
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Helvetica, Arial, sans-serif" font-size="13">',
           f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
           '<text x="12" y="26" font-size="15" font-weight="bold" fill="#1f2328">Bookends v5.31.0 control (real library), lower is better</text>']
    y = 44
    for label, unit, stock, bk, dec in groups:
        scale = (width - left - 110) / max(stock, bk)
        out.append(f'<text x="{left - 8}" y="{y + 30}" text-anchor="end" font-weight="bold" fill="#1f2328">{label}</text>')
        for i, (name, value, color) in enumerate((("Stock", stock, "#0969da"), ("+ Bookends", bk, "#bf8700"))):
            yy = y + i * row_h
            out.append(f'<rect x="{left}" y="{yy + 3}" width="{value * scale:.1f}" height="16" rx="2" fill="{color}"/>')
            out.append(f'<text x="{left + value * scale + 6:.1f}" y="{yy + 15}" fill="#57606a">{name}: {value:.{dec}f} {unit}</text>')
        y += 2 * row_h + 14
    out.append("</svg>")
    path.write_text("\n".join(out) + "\n")


def before_after(path: Path) -> None:
    """Each plugin alone, previous vs current round, relative to Stock of the same campaign.

    Absolute times are not comparable between the rounds (the current runs are
    headless and Stock itself restarts about twice as fast), so times are shown
    as a multiple of that campaign's Stock and heap as MiB above Stock.
    """
    old_csv = list(csv.DictReader(open(RUNS / "2026-09-12-full" / "phase2" / "RESULTS.csv")))

    def get(rows, stack, scenario, mode, column="wall_time_ms_median"):
        for r in rows:
            if (r["Stack"], r["Scenario"], r["Mode"], r["Status"]) == (stack, scenario, mode, "PASS") and r.get(column):
                return float(r[column])
        raise KeyError((stack, scenario))

    plugins = [("R1_bookshelf", "Bookshelf 5.0.0→6.0.3"), ("R5_vos", "VOS 1.3.4→1.4.1"),
               ("R3_zenos", "ZenOS 3.2.2→4.2.0"), ("R2_simpleui", "SimpleUI 2.7.1→3.0.1"),
               ("R4_project_title", "Project:Title (no covers→covers)")]
    panels = [("Restart to library (× Stock)", "process:spawn_to_library_ready_ms", "real_steady_cold", "wall_time_ms_median", "x"),
              ("Open book (× Stock)", "open_book_minimal", "warm", "wall_time_ms_median", "x"),
              ("Close book (× Stock)", "close_book", "warm", "wall_time_ms_median", "x"),
              ("Live Lua heap (MiB above Stock)", "memory:post_stress_idle", "warm", "forced_gc_live_heap_kb_median", "mib")]

    def rel(rows_for, stack, scenario, mode, column, kind):
        a = metric_from(rows_for(stack), stack, scenario, mode, column)
        b = metric_from(rows_for("R0_stock"), "R0_stock", scenario, mode, column)
        return (a - b) / 1024 if kind == "mib" else a / b

    def metric_from(rows, stack, scenario, mode, column):
        return get(rows, stack, scenario, mode, column)

    def rows_old(_stack): return old_csv

    def rows_new(stack):
        campaign = SOURCES.get(stack, BASE)
        if campaign not in _cache:
            _cache[campaign] = list(csv.DictReader(open(RUNS / campaign / "phase2" / "RESULTS.csv")))
        return _cache[campaign]

    width, pw, ph, top, left = 900, 440, 214, 44, 12
    height = top + 2 * ph + 40
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Helvetica, Arial, sans-serif" font-size="12">',
           f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
           '<text x="12" y="24" font-size="15" font-weight="bold" fill="#1f2328">Each plugin alone: previous round (gray) vs current (color), relative to Stock of the same round</text>']
    for idx, (title, scenario, mode, column, kind) in enumerate(panels):
        ox, oy = left + (idx % 2) * (pw + 8), top + (idx // 2) * ph
        vals = [(label, rel(rows_old, k, scenario, mode, column, kind), rel(rows_new, k, scenario, mode, column, kind)) for k, label in plugins]
        peak = max(max(abs(o), abs(n)) for _, o, n in vals)
        scale = (pw - 200 - 70) / peak
        out.append(f'<text x="{ox}" y="{oy + 16}" font-weight="bold" fill="#1f2328">{title}</text>')
        for r, (label, o, n) in enumerate(vals):
            y = oy + 28 + r * 34
            out.append(f'<text x="{ox + 192}" y="{y + 20}" text-anchor="end" fill="#1f2328" font-size="11">{label}</text>')
            fmt = (lambda v: f"{v:+.0f} MiB") if kind == "mib" else (lambda v: f"{v:.2f}x")
            for j, (v, color) in enumerate(((o, "#afb8c1"), (n, "#0969da"))):
                w = max(1.0, abs(v) * scale)
                x0 = ox + 200 if v >= 0 else ox + 200 - w
                out.append(f'<rect x="{x0:.1f}" y="{y + 2 + j * 14}" width="{w:.1f}" height="12" rx="2" fill="{color}"/>')
                out.append(f'<text x="{ox + 200 + (w if v >= 0 else 0) + 5:.1f}" y="{y + 12 + j * 14}" fill="#57606a" font-size="10">{fmt(v)}</text>')
    out.append(f'<text x="12" y="{height - 12}" fill="#57606a" font-size="11">Different run setups: the current runs are headless and Stock itself restarts ~2x faster, so only ratios to Stock are compared.</text>')
    out.append("</svg>")
    path.write_text("\n".join(out) + "\n")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    restart = [(n, metric(k, "process:spawn_to_library_ready_ms", "real_steady_cold")) for k, n in NAMES.items()]
    heap = [(n, metric(k, "memory:post_stress_idle", "warm", "forced_gc_live_heap_kb_median") / 1024) for k, n in NAMES.items()]
    close = [(n, metric(k, "close_book", "warm")) for k, n in NAMES.items()]
    bars("Real library (2,692 EPUBs): restart to usable library, lower is better", "ms", restart, OUT / "real_restart.svg")
    bars("Live Lua heap after stress (forced GC), lower is better", "MiB", heap, OUT / "real_heap.svg", 1)
    bars("Closing a book, lower is better", "ms", close, OUT / "real_close_book.svg")
    bookends_control(OUT / "bookends_control.svg")
    before_after(OUT / "before_after.svg")


if __name__ == "__main__":
    main()
