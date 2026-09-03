# Campaign runbook

Operational procedure for running a full benchmark campaign. Written to be followed
literally, by a person or an agent. For what the scenarios mean see
[`SCENARIOS.md`](SCENARIOS.md); for the design see [`README.md`](README.md).

## Ground rules

- Run every command from the repository root.
- Measurement runs use `--lanes 1`. Only `--validate` may use up to `--lanes 2`.
- One baseline campaign name for steps 1–4. A campaign is identified by its code hashes,
  `versions.lock.json` hash and flash setting; if any of those change, the campaign
  refuses to continue and a new name is required.
- A flash study is always a **separate campaign**, including its own validation gate.
- Runs are resumable. Re-running the same command skips results that already validate.
  Use `--no-resume` only to deliberately discard and redo.
- A block stops the campaign on its first failing job. Nothing is analyzed for a
  failed run, so a non-zero exit means "investigate", never "partial result".
- Never edit files under `results/` by hand. Regenerate with `analyze_results.py`.
- The real corpus is cloned per config and deleted after each block. Ordinary
  Phase 2 blocks use one working copy; the two-job Bookends block prepares and
  cleans both `bookends_A_stock` and `bookends_K_stock_bookends`. Do not remove
  `real_books/`; it is the master.

## Preflight

```bash
./setup.sh                       # checks out revisions from versions.lock.json
./build.sh                       # only needed if KOReader itself changed
./prepare_library.sh             # deterministic synthetic corpora
python3 -m pytest tests/ -q      # must be all green
```

`setup.sh` prints the pinned table and fails if any checkout drifted from the lock
file. Do not proceed past a drift.

For Phase 2 and the Bookends control, `real_books/` must contain exactly 2692 EPUB
files. The runner hard-fails on any other count.

Pick the campaign name once and export it:

```bash
export CAMPAIGN=$(date +%F)-full        # e.g. 2026-09-03-full
```

## Step 1 — validation gate (mandatory)

```bash
python3 scripts/run_benchmarks.py --validate --campaign "$CAMPAIGN" --lanes 1
```

15 jobs on FLAT 50. Every later phase refuses to start without a valid `smoke_gate`
checkpoint for the same campaign and the same flash setting.

Expected tail:

```
[AUDIT SUMMARY] samples=795 real_transitions=795 noops=0 wraps=0 empty_shelves=0 ...
[AUDIT PASS] Verified 795 paging transition samples across 15 runs with zero invariant violations.
```

Stop if `noops`, `wraps` or `empty_shelves` is non-zero, or if any run is not `PASS`.

## Step 2 — paging Phase 1 (synthetic)

```bash
python3 scripts/run_benchmarks.py --paging-phase1 --paging-runs 3 --campaign "$CAMPAIGN" --lanes 1
```

72 jobs: 12 configs x {FLAT 2000, HIERARCHICAL 2000} x 3 independent processes.
Paging only — no startup, memory or open-book work.

Check in the audit summary that:

- every `phase1:<config>:<dataset>:paging:paging` cell shows **3** process runs;
- `noops`, `wraps`, `empty_shelves` are all 0;
- `paging_roots` names `ComputerScience (165 of 2000 books)` for the hierarchical
  cells and is absent for the flat cells.

Each run also writes `paging_probe_page2_before.png` and
`paging_probe_page3_after.png` under `phase1/screenshots/<run_id>/`. Validation
already requires them to be valid PNGs at one exact emulator resolution with
differing hashes, so a run measured behind an overlay fails instead of passing.
Open a few and confirm they show a library page: that is the only check that
proves what was on screen.

## Step 3 — paging Phase 2 (real corpus)

```bash
python3 scripts/run_benchmarks.py --paging-phase2 --paging-runs 3 --campaign "$CAMPAIGN" --lanes 1
```

36 jobs: 12 configs x 3 processes. Requires a complete step 2.

`paging_roots` must be **empty** here: the working corpus keeps 500 books in its
root, so paging is never narrowed. A named paging root on the real corpus means the
corpus was not restructured and the run measured the wrong thing.

## Step 4 — full Phase 1 and Phase 2 (only if startup/memory/open-book are needed)

Skip this step for a paging-only campaign.

```bash
# 111 jobs: startup, first-run, memory checkpoints, open-book, folders, sort, paging
python3 scripts/run_benchmarks.py --phase1 --batch all --campaign "$CAMPAIGN" --lanes 1

# 60 jobs on the real corpus; requires a complete --phase1
python3 scripts/run_benchmarks.py --phase2 --campaign "$CAMPAIGN" --lanes 1

# 2 jobs: Bookends control; requires complete --phase1 and --phase2
python3 scripts/run_benchmarks.py --phase2 --batch 3 --campaign "$CAMPAIGN" --lanes 1
```

`--batch 1` / `--batch 2` split Phase 1 and Phase 2 into resumable halves.
`--batch 3` is the Bookends control and is valid for Phase 2 only.

The Bookends control is the only consumer of `reader_page_turn`. It is now pinned to
a single document, so its previously published page-turn figures were withdrawn and
have to be re-measured here before any page-turn number is quoted again.

The runner prepares separate disposable real corpora for both Bookends jobs. Do not
pre-create either corpus manually; a missing or empty corpus is a runner failure.

## Step 5 — flash study (separate campaign)

```bash
export FLASH_CAMPAIGN=$(date +%F)-flash100

python3 scripts/run_benchmarks.py --validate \
  --campaign "$FLASH_CAMPAIGN" --emulate-reader-flash-ms 100 --lanes 1

python3 scripts/run_benchmarks.py --paging-phase1 --paging-runs 3 \
  --campaign "$FLASH_CAMPAIGN" --emulate-reader-flash-ms 100 --lanes 1
```

`EMULATE_READER_FLASH=100` is a supported SDL flash-delay approximation in the pinned
KOReader source. It does **not** model persistent e-ink ghosting: the shadow buffer is
resynchronized after each refresh. Label the result a synthetic flash-delay sensitivity
experiment, never a physical Kindle latency measurement, and never merge it into the
baseline campaign.

## Step 6 — reports

Reports are generated automatically at the end of each successful phase. To regenerate
without re-measuring:

```bash
python3 analyze_results.py --run-dir results/runs/"$CAMPAIGN"/phase1 --scope phase1
python3 analyze_results.py --run-dir results/runs/"$CAMPAIGN"/phase2 --scope phase2
python3 analyze_results.py --run-dir results/runs/"$CAMPAIGN"/phase2 --scope bookends_control
python3 analyze_results.py --run-dir results/runs/"$FLASH_CAMPAIGN"/phase1 --scope phase1
```

A non-zero exit means the audit rejected the raw data. Fix the cause and re-measure;
do not publish a campaign whose audit fails.

## Step 7 — publication

1. Sanitize raw evidence if raw measurements are to be published:

   ```bash
   python3 scripts/sanitize_published_results.py --run-dir results/runs/"$CAMPAIGN"
   python3 scripts/sanitize_published_results.py --run-dir results/runs/"$CAMPAIGN" --check
   ```

   This hashes every value exposing a local path, which is where EPUB filenames live.
   `--check` must print `PASS`.

2. Add one line per published campaign to `.gitignore`:

   ```gitignore
   !results/runs/<baseline-campaign>/
   !results/runs/<flash-campaign>/
   ```

   Only aggregates travel: `campaign.json`, `environment.json`, `*.csv`, `charts/`,
   `REPORT.md`, `VALIDATION.md`. `raw/`, `logs/`, `checkpoints/` and `screenshots/`
   stay local unless explicitly unignored after sanitizing.

3. Update the README headline tables and the campaign links to the new campaign, and
   remove any claim the new data does not support.

## Reporting the outcome

Report, per step: command, exit code, job count with PASS/FAILED split, and the
`[AUDIT SUMMARY]` line. On failure, name the first failing `run_id`, quote its
validation errors, and point at `results/runs/<campaign>/<phase>/logs/<run_id>.log`.
Do not summarize a failed campaign as partially successful, and do not compare medians
across campaigns with different `versions_lock_sha256` or flash settings.
