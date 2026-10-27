# Plan: benchmark on a real Kindle

Status: **planned, not scheduled.** One proof-of-concept run exists (2026-10-28); the full device queue is deferred until there is time for it.

## Why

The emulator on Apple Silicon is optimistic and uneven. The same Stock scenarios on a Kindle Paperwhite (2022, 11th gen, 1236 x 1648) were slower by roughly 10x (library paging) up to 39x (opening a book), so absolute emulator numbers do not carry over and the ranking of stacks may differ.

## Proof of concept (done, 2026-10-28)

The existing harness ran unchanged on the device: Stock, 250 synthetic books, warm profile, 2 warmups + 10 measured iterations, every scenario PASS. A separate KOReader copy (`KO_HOME=/mnt/us/koreader_bench/home`, same KOReader v2026.07.2 binary) was delivered over HTTP, started by a detached on-device script after the normal KOReader exited, and the normal KOReader was restored afterwards (about 4 minutes total).

| Scenario (Stock, flat 250) | Mac emulator | Paperwhite | Slower by |
|---|---:|---:|---:|
| Library paging (sequential) | 17.6 ms | 172.7 ms | 10x |
| Library paging (cached) | 19.5 ms | 264.3 ms | 14x |
| Library first render | 26.8 ms | 373.3 ms | 14x |
| Change sort mode | 32.5 ms | 620.9 ms | 19x |
| Close book | 36.6 ms | 1012.0 ms | 28x |
| Open book | 39.3 ms | 1512.8 ms | 39x |

Device process RSS after stress was about 60 MiB (emulator: about 179 MiB, not comparable: different process model).

## Design

1. **Delivery over HTTP.** The Mac serves a bundle (benchmark plugin, stack plugins, settings, a library subset); the device downloads it with `wget` and checks the checksum. The KOReader inspector (port 8080) is used to start the run.
2. **Autonomous queue, Wi-Fi off while measuring.** The inspector needs Wi-Fi, so the queue is started over HTTP with Wi-Fi on; the on-device script then turns Wi-Fi off, runs every configuration unattended (settings written per stack, KOReader restarted with exit code 85, so the framework is stopped only once), writes one result JSON per run to disk, and turns Wi-Fi back on at the end (a watchdog also restores Wi-Fi and the normal KOReader on timeout). Results are then fetched over HTTP. Wi-Fi stays off during the queue because background networking adds timing noise.
3. **Device-side markers.** Add process RSS and free memory (`/proc/self/status`, `/proc/meminfo`) and the process start time (`/proc/<pid>/stat` against `/proc/uptime`) so restart is measured on the device, not over Wi-Fi from the Mac. Add an "e-ink update complete" marker so paint and panel refresh can be told apart.
4. **Runner mode.** A `--target kindle` mode: deliver, run the queue, fetch results, then reuse the existing audit and report pipeline so the report is the same format as the emulator one.
5. **Stacks (deferred).** Queue the remaining stacks (SimpleUI, Project:Title, m1n1mal, Bookshelf, then ZenOS, VOS and the combinations) after the marker work. Not started.

## Estimated time for the full matrix on the device

Derived from the measured emulator campaign (`2026-10-27-m1n1mal-v3`) and the observed slowdowns above; an estimate, not a measurement. One device means one lane, no parallelism.

| Step | Jobs | Mac emulator | Assumed device slowdown | Estimated device time |
|---|---:|---:|---|---:|
| Validation gate (all stacks) | 17 | about 1 min | per-job overhead | 5-10 min |
| Phase 1 warm jobs (4 synthetic libraries x 14 stacks) | 56 | 11.9 min | 15-20x + about 10 s per job | 3.0-4.1 h |
| Phase 1 restarts (init, steady x3, first-run) | 77 | under 1 min | about 8-12 s each | 10-15 min |
| Phase 2 first run (index a real library subset) | 14 | 1.8 min | 30-50x | 55-90 min |
| Phase 2 warm (real library) | 14 | 5.1 min | 15-20x | 75-100 min |
| Phase 2 steady restarts | 42 | about 0.5 min | about 8-12 s each | 6-10 min |
| Bookends control | 2 | about 1 min | 15-20x | 15-20 min |
| **Total, one pass** | | about 20 min | | **about 6-8.5 h** |

Add 10-20 percent for cooldown pauses between runs and charging. A reduced matrix (7 key stacks: Stock, Bookshelf, Project:Title, SimpleUI, ZenOS, VOS, m1n1mal, no combinations) would be roughly 3-4 hours.

## Constraints and risks

- The whole 2,692-book library (about 3 GB) does not fit next to the existing install on the device (3.2 GB free), so Phase 2 would use a subset (for example 500 root books plus a few folders); numbers would not be directly comparable with the emulator's real-library table.
- Device state affects results: battery, temperature, free memory, other Kindle processes. Use warmups, cooldowns and 3+ repeats where the matrix says so.
- Results describe one Kindle model.
- The queue closes and restores the user's KOReader: run only with the owner's explicit go-ahead, behind a watchdog.
