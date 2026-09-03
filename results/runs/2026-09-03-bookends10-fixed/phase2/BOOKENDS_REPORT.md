# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `bookends_control`

Versions lock SHA-256: `26bb78442d6bed9f4933bc3c30a6209507dc0fecb152335c3fd708bd660db8d4`
Reader flash setting: `unset`

Aggregated rows: 40; PASS=38; FAILED=0; UNSUPPORTED=2; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.341 | 34.137 | 13.339 | 37.061 | 17.592 | 35.103 | 12.059 | 37.264 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 18.425 | 34.929 | 12.601 | 37.342 | 16.634 | 34.743 | 11.287 | 39.028 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 13.992 | 12.986–14.451 | 8.729 | 124.454 |
| K_stock_bookends | 1 | 10 | 18.985 | 18.054–20.045 | 8.149 | 133.049 |

The observed median forced-GC heap difference in this control is **+4.993 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 69.514 | 53.815 | 98.155 | 53.726–102.649 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 34.576 | 22.539 | 53.681 | 21.508–66.791 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 33.770 | 32.558 | 65.649 | 32.158–94.847 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 17.592 | 14.368 | 35.103 | 12.059–37.264 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 44.135 | 34.449 | 61.589 | 31.694–86.051 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 85.555 | 61.526 | 112.769 | 60.758–120.350 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 25.285 | 17.992 | 53.370 | 17.105–86.903 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.341 | 14.534 | 34.137 | 13.339–37.061 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 67.953 | 52.558 | 77.184 | 52.285–84.456 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 124.454 | 87.224 | 151.888 | 67.940–203.856 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 8.729 | 7.835 | 10.302 | 4.083–19.164 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 69.092 | 63.559 | 97.919 | 63.547–132.905 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 29.584 | 26.357 | 36.196 | 25.477–76.739 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 37.948 | 33.275 | 71.792 | 32.248–101.986 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.634 | 13.812 | 34.743 | 11.287–39.028 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 46.760 | 32.700 | 61.448 | 32.379–75.377 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 92.544 | 68.521 | 122.961 | 57.952–128.507 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 26.057 | 22.790 | 44.716 | 20.042–48.888 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 18.425 | 15.996 | 34.929 | 12.601–37.342 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 64.353 | 58.805 | 75.322 | 58.426–85.974 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 133.049 | 85.998 | 152.849 | 77.587–205.648 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 8.149 | 7.312 | 9.023 | 7.307–9.169 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 660.699 | 660.699 | 660.699 | 660.699–660.699 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2344.222 | 2344.222 | 2344.222 | 2344.222–2344.222 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 14901.956 | 14901.956 | 14901.956 | 14901.956–14901.956 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 15045.158 | 15045.158 | 15045.158 | 15045.158–15045.158 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 579.431 | 579.431 | 579.431 | 579.431–579.431 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2370.837 | 2370.837 | 2370.837 | 2370.837–2370.837 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 16629.091 | 16629.091 | 16629.091 | 16629.091–16629.091 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 16910.345 | 16910.345 | 16910.345 | 16910.345–16910.345 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 8961.165 | 8961.165 | 8961.165–8961.165 | 11023.462 | 166784.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13528.970 | 13528.970 | 13528.970–13528.970 | 20261.198 | 218720.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 14327.298 | 14679.292 | 13297.403–14797.505 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14621.220 | 14621.220 | 14621.220–14621.220 | 14630.618 | 329104.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9827.374 | 9827.374 | 9827.374–9827.374 | 14127.919 | 168240.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13646.894 | 13646.894 | 13646.894–13646.894 | 24403.279 | 222512.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 19440.177 | 20492.402 | 18487.148–20526.216 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 21349.729 | 21349.729 | 21349.729–21349.729 | 24363.636 | 354656.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
