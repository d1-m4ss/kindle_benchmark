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


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    restart = [(n, metric(k, "process:spawn_to_library_ready_ms", "real_steady_cold")) for k, n in NAMES.items()]
    heap = [(n, metric(k, "memory:post_stress_idle", "warm", "forced_gc_live_heap_kb_median") / 1024) for k, n in NAMES.items()]
    close = [(n, metric(k, "close_book", "warm")) for k, n in NAMES.items()]
    bars("Real library (2,692 EPUBs): restart to usable library, lower is better", "ms", restart, OUT / "real_restart.svg")
    bars("Live Lua heap after stress (forced GC), lower is better", "MiB", heap, OUT / "real_heap.svg", 1)
    bars("Closing a book, lower is better", "ms", close, OUT / "real_close_book.svg")
    bookends_control(OUT / "bookends_control.svg")


if __name__ == "__main__":
    main()
