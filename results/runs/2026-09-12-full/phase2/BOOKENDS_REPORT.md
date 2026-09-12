# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `bookends_control`

Versions lock SHA-256: `b7aa678f5eef72bc810dedd92ebabb1d9973e5a3d10230e9401af28e1a995ad4`
Reader flash setting: `unset`

Aggregated rows: 40; PASS=38; FAILED=0; UNSUPPORTED=2; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 22.191 | 36.365 | 17.865 | 39.881 | 22.084 | 35.978 | 16.516 | 42.148 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 22.103 | 40.279 | 14.679 | 45.344 | 23.456 | 40.969 | 16.862 | 43.997 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 14.625 | 13.669–14.937 | 8.572 | 144.777 |
| K_stock_bookends | 1 | 10 | 17.239 | 16.763–18.719 | 8.407 | 155.782 |

The observed median forced-GC heap difference in this control is **+2.614 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 87.126 | 83.465 | 111.975 | 82.385–113.399 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 47.868 | 28.943 | 71.307 | 28.291–73.475 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 65.221 | 46.587 | 89.248 | 44.922–97.656 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 22.084 | 18.452 | 35.978 | 16.516–42.148 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 46.581 | 43.570 | 63.515 | 43.497–67.746 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 103.172 | 76.770 | 134.846 | 74.218–153.374 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 36.392 | 32.467 | 88.072 | 25.214–136.518 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 22.191 | 19.407 | 36.365 | 17.865–39.881 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 71.223 | 55.796 | 87.621 | 51.373–104.497 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 144.777 | 76.393 | 175.915 | 75.060–254.360 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 8.572 | 8.054 | 9.156 | 5.650–9.211 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 89.483 | 86.463 | 118.041 | 82.853–119.199 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 43.721 | 35.986 | 60.768 | 32.253–70.889 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 77.571 | 49.855 | 94.069 | 47.781–95.009 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 23.456 | 19.026 | 40.969 | 16.862–43.997 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 48.780 | 46.210 | 72.766 | 45.868–82.293 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 129.727 | 82.733 | 152.222 | 80.962–163.850 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 37.194 | 34.620 | 97.314 | 24.911–110.608 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 22.103 | 20.503 | 40.279 | 14.679–45.344 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 100.305 | 88.756 | 123.626 | 83.550–139.352 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 155.782 | 114.720 | 186.043 | 88.600–275.712 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 8.407 | 7.851 | 8.961 | 7.630–9.364 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 528.691 | 528.691 | 528.691 | 528.691–528.691 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2722.199 | 2722.199 | 2722.199 | 2722.199–2722.199 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 17713.316 | 17713.316 | 17713.316 | 17713.316–17713.316 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 17933.112 | 17933.112 | 17933.112 | 17933.112–17933.112 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 674.106 | 674.106 | 674.106 | 674.106–674.106 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 3031.547 | 3031.547 | 3031.547 | 3031.547–3031.547 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 20603.556 | 20603.556 | 20603.556 | 20603.556–20603.556 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 20876.763 | 20876.763 | 20876.763 | 20876.763–20876.763 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 8974.962 | 8974.962 | 8974.962–8974.962 | 11403.257 | 166464.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 12770.985 | 12770.985 | 12770.985–12770.985 | 22583.378 | 214608.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 14976.312 | 15279.348 | 13997.353–15295.798 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 13975.950 | 13975.950 | 13975.950–13975.950 | 18078.610 | 336144.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9836.287 | 9836.287 | 9836.287–9836.287 | 13837.904 | 168544.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13634.174 | 13634.174 | 13634.174–13634.174 | 23661.832 | 218192.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 17652.768 | 18541.013 | 17165.010–19167.892 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 18426.540 | 18426.540 | 18426.540–18426.540 | 18440.325 | 342704.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
