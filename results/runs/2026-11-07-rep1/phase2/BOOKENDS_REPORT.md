# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `bookends_control`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 40; PASS=38; FAILED=0; UNSUPPORTED=2; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 18.280 | 32.195 | 15.502 | 35.334 | 17.791 | 30.607 | 11.102 | 34.512 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.337 | 28.889 | 12.654 | 33.341 | 15.242 | 29.359 | 9.783 | 31.429 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 14.412 | 14.355–14.462 | 4.096 | 97.764 |
| K_stock_bookends | 1 | 10 | 18.692 | 17.801–21.226 | 12.587 | 103.422 |

The observed median forced-GC heap difference in this control is **+4.280 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 51.016 | 40.786 | 79.092 | 39.472–121.571 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 28.086 | 25.055 | 40.874 | 22.213–44.139 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 31.107 | 27.096 | 41.994 | 26.930–46.705 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 17.791 | 13.023 | 30.607 | 11.102–34.512 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 50.879 | 36.483 | 99.237 | 35.765–99.345 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 38.611 | 35.598 | 53.410 | 33.997–56.065 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 24.112 | 17.687 | 41.465 | 17.419–44.723 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 18.280 | 16.377 | 32.195 | 15.502–35.334 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 52.562 | 46.909 | 60.508 | 45.519–81.689 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 97.764 | 49.477 | 116.149 | 47.957–166.110 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 4.096 | 3.802 | 7.713 | 3.591–13.608 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 53.704 | 48.023 | 77.479 | 41.564–111.515 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 29.696 | 27.005 | 44.370 | 26.460–51.860 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.584 | 27.118 | 31.692 | 26.782–47.357 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.242 | 10.465 | 29.359 | 9.783–31.429 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 35.502 | 27.338 | 91.606 | 26.780–99.335 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 35.428 | 32.720 | 50.891 | 32.688–55.784 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 20.793 | 15.353 | 36.655 | 15.320–37.249 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.337 | 13.544 | 28.889 | 12.654–33.341 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 68.987 | 53.447 | 76.722 | 46.178–76.933 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 103.422 | 62.826 | 125.030 | 57.836–171.069 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 12.587 | 7.461 | 14.496 | 4.154–16.404 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 399.155 | 399.155 | 399.155 | 399.155–399.155 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2052.374 | 2052.374 | 2052.374 | 2052.374–2052.374 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12705.159 | 12705.159 | 12705.159 | 12705.159–12705.159 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12719.637 | 12719.637 | 12719.637 | 12719.637–12719.637 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 298.079 | 298.079 | 298.079 | 298.079–298.079 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1700.860 | 1700.860 | 1700.860 | 1700.860–1700.860 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13029.222 | 13029.222 | 13029.222 | 13029.222–13029.222 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13099.672 | 13099.672 | 13099.672 | 13099.672–13099.672 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9095.093 | 9095.093 | 9095.093–9095.093 | 12105.720 | 86784.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14411.800 | 14411.800 | 14411.800–14411.800 | 27408.950 | 142560.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 14757.413 | 14802.712 | 14699.839–14808.956 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14915.577 | 14915.577 | 14915.577–14915.577 | 18273.413 | 262624.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9935.550 | 9935.550 | 9935.550–9935.550 | 13730.661 | 87152.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16560.339 | 16560.339 | 16560.339–16560.339 | 35496.206 | 137200.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 19140.485 | 21698.911 | 18228.526–21734.925 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 24113.309 | 24113.309 | 24113.309–24113.309 | 27980.570 | 273344.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
