# KOReader UI Plugin Performance Benchmark

This repository measures the performance and retained runtime cost of KOReader UI plugins and plugin stacks in a pinned macOS SDL emulator.

It answers a practical question: **which UI changes stay close to Stock KOReader, and which trade more startup time or retained Lua state for a richer shell?**

> This is a controlled emulator comparison, not a benchmark of physical Kindle latency. It is useful for relative work, memory, and redraw comparisons; it cannot turn a Mac millisecond value into a Kindle millisecond value.

## Quick links

- [Phase 1 synthetic report](results/runs/2026-09-03-full/phase1/REPORT.md)
- [Phase 2 real-library report](results/runs/2026-09-03-full/phase2/REPORT.md)
- [Bookends control](results/runs/2026-09-03-bookends10-fixed/phase2/BOOKENDS_REPORT.md)
- [100 ms flash-delay study](results/runs/2026-09-03-flash100/phase1/REPORT.md)
- [Campaign runbook](RUNBOOK.md)
- [Scenario definitions and contracts](SCENARIOS.md)

## Headline results

There is no universal winner: the stacks prioritize different UI behaviours. The
latest full baseline is `2026-09-03-full`; its campaign metadata records the
runner and benchmark-harness hashes used for that run. Current source includes
later harness changes, while the remeasured Bookends control is published
separately as `2026-09-03-bookends10-fixed`. Every dedicated paging cell has
three isolated process runs and passed the transition, framebuffer and screenshot
evidence gates.

- **Project:Title** had the best overall lightweight profile in this campaign:
  fastest steady restart to the real library, fastest first render, fastest
  minimally instrumented book open and the lowest post-stress live Lua heap.
- **Project:Title + VOS** retained excellent paging and open-book results, but its
  steady restart was much slower than Project:Title alone in this run.
- **Bookshelf** left the normal library close to Stock and showed a lower
  `open_book_minimal` median in this campaign (117.5 ms versus 147.9 ms for
  Stock). That is an observation, not evidence that Bookshelf causally speeds
  up the reader-open path. In its dedicated shelf, the default animation
  dominated page-turn latency; animation-off isolates a much smaller renderer
  cost.
- **SimpleUI** traded substantially more startup, first-render time and retained
  Lua state for its richer home/dashboard shell.

### Synthetic stress case: FLAT 2000

This table is the intentionally hostile case: 2,000 EPUBs in one folder. Values
are warm medians in milliseconds; every shown value has 10 measured samples after
two warmups. `Open book` is `open_book_minimal`, isolated from dirty-region
instrumentation.

| Stack | Library render | Open book |
|---|---:|---:|
| **Project:Title** | **40.6** | **48.2** |
| Project:Title + VOS | 47.5 | 52.7 |
| Stock | 54.7 | 104.9 |
| SimpleUI + VOS + Bookshelf | 59.2 | 94.7 |
| SimpleUI + VOS | 61.2 | 82.1 |
| VOS | 61.6 | 84.5 |
| SimpleUI + Bookshelf | 67.0 | 88.3 |
| ZenOS | 67.4 | 99.2 |
| ZenOS + Bookshelf | 70.5 | 108.4 |
| SimpleUI | 70.8 | 91.2 |
| VOS + Bookshelf | 77.1 | 90.6 |
| Bookshelf | 82.5 | 113.4 |

### Real library: 2,692 EPUBs

`Real 2692` is the total corpus size. Real paging traverses the library root,
which contains exactly **505 visible entries: 500 EPUBs + 5 folders**. The other
2,192 EPUBs remain inside those folders and still participate in indexing,
metadata/cache growth, folder navigation and the remaining Phase 2 scenarios.

The real corpus is the more practically useful result set. Restart values are the median of three isolated process runs; render/open values are warm medians of 10 samples. Memory is one forced-GC checkpoint per stack after the same stress sequence, so it is an observed state point, not a replicated statistical median.

| Stack | Restart → library | Library render | Open book | Live Lua after stress |
|---|---:|---:|---:|---:|
| **Project:Title** | **504 ms** | **25.7 ms** | **105.8 ms** | **14.5 MiB** |
| Stock | 548 ms | 31.5 ms | 147.9 ms | 26.6 MiB |
| VOS | 562 ms | 42.8 ms | 140.2 ms | 29.0 MiB |
| Bookshelf | 569 ms | 31.6 ms | 117.5 ms | 17.6 MiB |
| VOS + Bookshelf | 625 ms | 44.3 ms | 136.7 ms | 26.5 MiB |
| SimpleUI + VOS | 742 ms | 94.4 ms | 148.0 ms | 67.4 MiB |
| SimpleUI | 746 ms | 128.9 ms | 142.3 ms | 61.2 MiB |
| ZenOS | 754 ms | 42.3 ms | 137.7 ms | 37.2 MiB |
| SimpleUI + VOS + Bookshelf | 754 ms | 97.9 ms | 143.2 ms | 71.8 MiB |
| Project:Title + VOS | 762 ms | 40.0 ms | 107.1 ms | 14.6 MiB |
| SimpleUI + Bookshelf | 767 ms | 101.9 ms | 136.9 ms | 67.1 MiB |
| ZenOS + Bookshelf | 788 ms | 52.7 ms | 147.6 ms | 40.7 MiB |

`RSS` is recorded too, but it is the whole macOS emulator process. It includes native libraries, mappings, allocator behaviour, and cached allocations, so forced-GC live Lua heap is the cleaner plugin-side signal.

### Dedicated real-library paging

These medians come from three isolated process runs per stack. `Entries/page`
always reports the visible page size. It must be read together with the 505-entry
root above; `Real 2692` does not mean that paging traverses one flat list of 2,692
books. Entries per page differ by UI, so comparisons across different layouts are
UX-level comparisons, not equal-render-work claims.

| Stack | Entries/page | Sequential | Cached |
|---|---:|---:|---:|
| Stock | 10 | 14.26 ms | 16.81 ms |
| Bookshelf | 10 | 14.71 ms | 16.93 ms |
| SimpleUI | 8 | 16.41 ms | 28.63 ms |
| ZenOS | 5 | 8.61 ms | 12.86 ms |
| Project:Title | 14 | 9.07 ms | 8.98 ms |
| VOS | 10 | 15.97 ms | 18.18 ms |
| SimpleUI + Bookshelf | 8 | 18.57 ms | 32.11 ms |
| ZenOS + Bookshelf | 5 | 8.50 ms | 12.79 ms |
| VOS + Bookshelf | 10 | 16.77 ms | 19.30 ms |
| SimpleUI + VOS | 8 | 16.49 ms | 28.99 ms |
| SimpleUI + VOS + Bookshelf | 8 | 17.59 ms | 32.20 ms |
| Project:Title + VOS | 14 | 8.72 ms | 8.48 ms |

The separate `2026-09-03-flash100` sensitivity study added approximately
97–106 ms to the median library transition. It is an injected SDL delay, not a
physical Kindle model.

### Bookends control

Bookends was measured separately as Stock versus Stock + Bookends, rather than
multiplying every stack by another on/off factor. No reader page-turn penalty
was observed with Bookends in this control. Across 10 full reader cycles in one
process, its median forced-GC live Lua heap was about 5 MiB higher than Stock
(18.99 versus 13.99 MiB). Minimally instrumented book opening was about 7% slower
(133.0 versus 124.5 ms).

The 10 memory samples are repeated cycles within one process, not independent
process replicates.

The control has one process per variant. The lower observed library-paging medians
with Bookends are therefore not evidence that the plugin improves paging performance.

## What was tested

The harness uses a backend-specific adapter for each UI stack. A scenario is `PASS` only when its semantic postcondition succeeds; unsupported UI actions remain `UNSUPPORTED` and are never converted into zero-latency samples.

Core scenarios include:

- process spawn to usable UI and usable library;
- library first render, page navigation, folder navigation, and sort change;
- open and close book;
- quick/settings panel transitions;
- short navigation stress and memory checkpoints;
- dedicated Bookshelf open/render/page/close scenarios;
- a separate Bookends reader control;
- refresh and dirty-region accounting.

The primary open-book number is `open_book_minimal`, which avoids distorting the latency with full dirty-region instrumentation. The report retains the full-instrumented scenario separately.

## Published campaign status

Campaigns [`2026-09-03-full`](results/runs/2026-09-03-full/campaign.json),
[`2026-09-03-bookends10-fixed`](results/runs/2026-09-03-bookends10-fixed/campaign.json)
and [`2026-09-03-flash100`](results/runs/2026-09-03-flash100/campaign.json) were
generated by the code and dependency revisions recorded in their metadata. These
are aggregated report rows, not a count of individual warm iterations:

| Scope | PASS | FAILED | UNSUPPORTED |
|---|---:|---:|---:|
| Baseline Phase 1 | 1,520 | 0 | 136 |
| Baseline Phase 2 | 611 | 0 | 6 |
| Bookends control | 38 | 0 | 2 |
| Flash100 paging study | 276 | 0 | 0 |

`UNSUPPORTED` entries describe actions that do not exist for the relevant stack or corpus shape, such as next-page navigation in a single-page library. They are reported explicitly rather than treated as success or as `0 ms`.

## Test environment

### Host and emulator target

- Apple MacBook Pro with M4 Pro, arm64
- macOS / Darwin 27
- Python 3.14.7
- KOReader SDL emulator hard-gated to 1236 × 1648, 300 DPI, grayscale
- Kindle Paperwhite 11th-generation / PW5-style framebuffer

SDL logical window size and actual render-output size can differ on Retina macOS. The runner aborts unless the actual framebuffer is 1236 × 1648.

### Pinned software

Only tagged stable releases are pinned. Pre-release tags are deliberately excluded: ZenOS stays on `v3.2.2` while `v3.3.0-betaN` exists upstream, and Project:Title is pinned to the `2026.07-v3.8.3` tag rather than a commit after it.

| Component | Release | Commit |
|---|---|---|
| KOReader | [`v2026.07.2`](https://github.com/koreader/koreader/releases/tag/v2026.07.2) | `9192014d8bd82a91dc1012473be0f238dedfdb54` |
| KOReader base | v2013.03-3987-g6e4bc81 | `6e4bc81af4e04f78d81677a323a780a71b29702a` |
| SimpleUI | [`2.7.0`](https://github.com/doctorhetfield-cmd/simpleui.koplugin/releases/tag/2.7.0) | `29dbfdea3298f8d4485faec38fd1691f76e35328` |
| ZenOS | [`v3.2.2`](https://github.com/xZenLabs/zen-os/releases/tag/v3.2.2) | `6bf289431bd7eeac88e424f77ecbba6cfab9ab61` |
| Bookshelf | [`v4.4.1`](https://github.com/AndyHazz/bookshelf.koplugin/releases/tag/v4.4.1) | `c20ffdec5170ba9595a9f1e534863e1b36474efc` |
| Bookends | [`v5.24.0`](https://github.com/AndyHazz/bookends.koplugin/releases/tag/v5.24.0) | `7ae55d263ef2dcf4090f07cb25fd864c3958bd04` |
| Project:Title | [`2026.07-v3.8.3`](https://github.com/joshuacant/ProjectTitle/releases/tag/2026.07-v3.8.3) | `f29b5328f408362a95282ed8786a5b691536260c` |
| VOS | [`v1.3.4`](https://github.com/SeriousHornet/vos.koplugin/releases/tag/v1.3.4) | `a8c661997b36165b5e75965c5903dbc9ffecebea` |

`versions.lock.json` is the single source of truth. `setup.sh` and `scripts/run_benchmarks.py` both read it, so bumping a dependency is a one-file edit:

1. Change `tag`, `commit`, `date`, `release_url` and `tree_url` for that entry.
2. Run `./setup.sh`. It checks out the pinned revisions and fails if any checkout drifts from the lock file.
3. Run `./build.sh` if KOReader itself changed.
4. Start a **new campaign**. The lock file's SHA-256 is part of the campaign identity, so a running campaign refuses to mix revisions and results from different locks are not comparable.

#### Baseline change

The pinned revisions above changed after the `2026-08-31-fixed` campaign was published: KOReader `1e2fa5f1` → `9192014d`, KOReader base `6232b260` → `6e4bc81a`, Bookshelf `643bc21f` (v4.4.0) → `c20ffdec` (v4.4.1), Project:Title `4dc97e62` → `f29b5328`. The published `2026-08-31-fixed` campaign predates this bump and also predates the paging-instrumentation and hierarchical-dataset fixes below — its paging/cached-paging numbers are not comparable to a campaign run against the current pinned revisions. See the deprecation banner in that campaign's phase1/phase2 reports.

## Corpus and design

### Phase 1: deterministic synthetic libraries

The synthetic corpus generator produces four shapes:

- FLAT 50
- FLAT 2000
- HIERARCHICAL 50
- HIERARCHICAL 2000

The FLAT 2000 directory is deliberately hostile: it concentrates listing, sorting, pagination, and widget construction in one folder. The hierarchical layouts better resemble ordinary libraries.

Phase 1 stacks:

| ID | Stack |
|---|---|
| A | Stock KOReader |
| B | Bookshelf |
| C | SimpleUI |
| D | ZenOS |
| E | Project:Title |
| F | VOS |
| G | SimpleUI + Bookshelf |
| H | ZenOS + Bookshelf |
| I | VOS + Bookshelf |
| J | SimpleUI + VOS |
| K | SimpleUI + VOS + Bookshelf |
| L | Project:Title + VOS |

### Phase 2: your real library

The published run used 2,692 EPUB files in a hierarchical personal library. The books are not and must not be included in this repository.

Place your own EPUB collection under exactly this path before Phase 2:

```text
real_books/
```

For example, the directory may look like this:

```text
real_books/
├── Fiction/
│   ├── Author A/
│   │   └── Title.epub
│   └── Author B/
│       └── Another title.epub
└── Non-fiction/
    └── Topic/
        └── Book.epub
```

The runner creates isolated working state per stack so one stack does not intentionally reuse another stack's KOReader/plugin cache.

#### Working-corpus layout

`real_books/` is never modified. For each stack the runner clones it into a disposable working corpus under `work_real/<campaign>/<config>/corpus`, restructured so the library is measurable:

```text
corpus/
├── <500 EPUBs in the root>   # sequential and cached library paging
├── folder1/                  # 500 books
├── folder2/                  # 500 books
├── folder3/                  # 500 books
├── folder4/                  # 500 books
└── folder5/                  # remaining books
```

Every book is preserved, so the corpus still totals 2,692 files; duplicate filenames across the master tree are disambiguated deterministically. Two reasons for the restructure:

- A personal library keeps no books in its root, so a paged library view there has a single page and cannot be measured at all. 500 books in the root give at least 30 sequential page transitions for every UI, including the densest measured layout at 14 entries per page.
- `folderN` names replace personal folder names, so the corpus structure itself carries nothing private. Book filenames stay real locally, because sorting and metadata parsing are part of what is measured. Published manifests retain aggregate corpus metadata only; raw evidence may be published only after `scripts/sanitize_published_results.py` hashes values exposing local paths.

Every paging metric — library and Bookshelf alike — therefore measures the same 505-entry root listing on every stack: 500 EPUBs plus 5 folders. The Bookshelf `all` shelf is not recursive: it lists the current folder, so it shows those 500 books plus the five folder entries, and no book from `folderN` appears in a shelf page turn. The remaining books are not decoration; they are what the rest of Phase 2 needs: first-run metadata and cover cache growth, `cache_database_bytes`, RSS and forced-GC live-heap checkpoints after real stress, folder navigation, and library first render. The exact mapping is recorded in `real_corpus_manifest.json` under `working_corpus_layout`.

#### Reader page turns

`reader_page_turn` is measured inside one pinned document, chosen deterministically from the books nearest the corpus median size. Page-turn latency tracks document size and complexity, and this corpus spans 59 KB to 29 MB, so rotating books would blend unrelated documents into one median. `open_book` deliberately keeps rotating through ten deterministic books, because opening the same file repeatedly would measure a warm document cache instead of a cold open.

Phase 2 uses the same 12 stacks: Stock, Bookshelf, SimpleUI, ZenOS,
Project:Title, VOS, SimpleUI + Bookshelf, ZenOS + Bookshelf, VOS + Bookshelf,
SimpleUI + VOS, SimpleUI + VOS + Bookshelf, and Project:Title + VOS. Bookends
is the separate controlled Stock comparison described above.

## Run it

Run all commands from the repository root. Full runs are expensive and create generated environments/results; use a new campaign name when you need a clean rerun. Measurement phases require `--lanes 1`; only `--validate` accepts up to `--lanes 2`.

[`RUNBOOK.md`](RUNBOOK.md) is the step-by-step operational procedure for a full campaign, including what each audit line must show, how to run the flash study, and how to publish. Follow it rather than assembling commands ad hoc.

### 1. Set up dependencies and pinned sources

```bash
./setup.sh
```

The script fetches KOReader and the plugin repositories at the revisions in `versions.lock.json`.

### 2. Build the KOReader emulator

```bash
./build.sh
```

### 3. Generate deterministic synthetic libraries

```bash
./prepare_library.sh
```

### 4. Run the validation gate

```bash
python3 scripts/run_benchmarks.py \
  --validate \
  --campaign local-run \
  --lanes 1
```

Validation checks framebuffer geometry, sub-millisecond timing, plugin loading, semantic postconditions, no fake zero-latency transition, dirty-region invariants, and instrumentation overhead.

### 5. Run the paging phases

Paging is measured on its own, isolated from startup, memory and open-book work, with three independent processes per cell:

```bash
# 72 jobs: 12 configs x {FLAT 2000, HIERARCHICAL 2000} x 3 processes
python3 scripts/run_benchmarks.py \
  --paging-phase1 \
  --paging-runs 3 \
  --campaign local-run \
  --lanes 1

# 36 jobs on the real corpus; requires a complete --paging-phase1
python3 scripts/run_benchmarks.py \
  --paging-phase2 \
  --paging-runs 3 \
  --campaign local-run \
  --lanes 1
```

### 6. Run full synthetic Phase 1

Only needed for startup, memory and open-book measurements; skip it for a paging-only campaign.

```bash
python3 scripts/run_benchmarks.py \
  --phase1 \
  --batch all \
  --campaign local-run \
  --lanes 1
```

Use `--batch 1` or `--batch 2` for a resumable half. Phase 1 refuses to proceed without a valid validation gate for that campaign.

### 7. Add your books and run real-library Phase 2

After placing exactly 2,692 EPUBs in `real_books/`, run:

```bash
python3 scripts/run_benchmarks.py \
  --phase2 \
  --campaign local-run \
  --lanes 1
```

Do not commit copyrighted books, generated KOReader homes, caches, emulator build output, or transient logs.

### 8. Run the Bookends control

This is Phase 2 batch 3 and requires a complete Phase 1 and Phase 2:

```bash
python3 scripts/run_benchmarks.py \
  --phase2 \
  --batch 3 \
  --campaign local-run \
  --lanes 1
```

For a focused Bookends-only repair/control, use a new standalone campaign. This
does not rerun or claim completion of the other phases:

```bash
python3 scripts/run_benchmarks.py \
  --bookends-control \
  --campaign local-bookends-control \
  --lanes 1
```

### 9. Run the flash study as its own campaign

`EMULATE_READER_FLASH` is part of the campaign identity, so a flash run never shares a campaign with the baseline and needs its own validation gate:

```bash
python3 scripts/run_benchmarks.py --validate \
  --campaign local-flash100 --emulate-reader-flash-ms 100 --lanes 1

python3 scripts/run_benchmarks.py --paging-phase1 --paging-runs 3 \
  --campaign local-flash100 --emulate-reader-flash-ms 100 --lanes 1
```

This is a synthetic SDL flash-delay sensitivity experiment. It does not model persistent e-ink ghosting and is not a physical-Kindle latency measurement.

### 10. Regenerate reports from existing raw data

This is read/compute-only with respect to a completed run; it does not rerun the emulator scenarios:

```bash
python3 analyze_results.py \
  --run-dir results/runs/local-run/phase1 \
  --scope phase1

python3 analyze_results.py \
  --run-dir results/runs/local-run/phase2 \
  --scope phase2

python3 analyze_results.py \
  --run-dir results/runs/local-run/phase2 \
  --scope bookends_control

python3 analyze_results.py \
  --run-dir results/runs/local-flash100/phase1 \
  --scope phase1
```

## Result layout

Each campaign is stored under `results/runs/<campaign>/`:

```text
results/runs/<campaign>/
├── campaign.json
├── phase1/
│   ├── raw/                  # source-of-truth schema-v2 measurements
│   ├── charts/
│   ├── RESULTS.csv
│   ├── VALIDATION.md
│   └── REPORT.md
└── phase2/
    ├── raw/
    ├── charts/
    ├── real_corpus_manifest.json
    ├── RESULTS.csv
    ├── BOOKENDS_RESULTS.csv
    ├── BOOKENDS_REPORT.md
    └── REPORT.md
```

Local runs also maintain `logs/` and `checkpoints/` for diagnostics and resume safety.

Publication is opt-in per campaign. `.gitignore` tracks only campaigns listed there explicitly, and only their aggregates: `campaign.json`, `environment.json`, `*.csv`, `charts/`, `REPORT.md`, `VALIDATION.md`. `raw/`, `logs/`, `checkpoints/` and `screenshots/` stay local — they are large, and on the real corpus raw evidence carries EPUB filenames. To publish a campaign, add one `!results/runs/<campaign>/` line. To publish its raw measurements too, first run `scripts/sanitize_published_results.py --run-dir <campaign>`, which hashes every value exposing a local path, then confirm with `--check`.

## Reading the measurements

Internal UI timings use KOReader's monotonic clock with microsecond representation:

```lua
time.to_us(time.monotonic() - t0) / 1000.0
```

External process timing uses Python's monotonic high-resolution clock. Warm scenarios use two warmups and 10 measured iterations. Startup/restart measurements use independent emulator processes; the published real-library steady restart median has three runs, and first-run initialization is descriptive rather than extensively replicated.

Memory checkpoints record natural Lua heap, forced-GC live Lua heap, RSS, KO_HOME/cache/database size, and related dirty-region metrics. `RSS` is supporting evidence rather than a clean measure of plugin memory on macOS.

Dirty-region output records refresh calls, full/partial refresh counts, cumulative dirty screen-equivalents, geometric union of dirty area, and largest dirty region. It measures redraw requests in the emulator, not physical Kindle waveform timing or ghosting.

## Limits

- The M4 Pro host does not reproduce Kindle CPU, storage I/O, memory-pressure, or E-Ink waveform behaviour.
- Results are descriptive local-emulator comparisons. They are not significance claims and do not select a universal winner.
- Exact rankings for close results can change on real hardware.
- A real Kindle follow-up is required for on-device latency or power conclusions.
- Published values apply to the pinned versions and corpus shape above, not to all plugin versions or libraries.

## License

Copyright (C) 2026 Dmytro Stadnik. The original code in this repository is
licensed under the GNU Affero General Public License, version 3 or later
([AGPL-3.0-or-later](LICENSE)).

## Attribution

This project benchmarks KOReader and independent third-party plugins. Those projects retain their own licences and copyrights; see their upstream repositories and licence files.
