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
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.633 | 31.966 | 14.460 | 32.923 | 18.524 | 31.425 | 11.721 | 35.560 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 18.028 | 31.545 | 14.499 | 34.770 | 18.225 | 30.022 | 10.566 | 35.048 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 15.092 | 15.033–15.148 | 4.125 | 100.504 |
| K_stock_bookends | 1 | 10 | 19.410 | 17.929–22.357 | 12.090 | 107.708 |

The observed median forced-GC heap difference in this control is **+4.317 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 53.757 | 43.447 | 80.794 | 43.050–86.820 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 21.816 | 18.973 | 36.685 | 16.605–46.347 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 31.921 | 29.027 | 41.512 | 28.949–47.836 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 18.524 | 12.955 | 31.425 | 11.721–35.560 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 57.409 | 32.901 | 86.378 | 27.837–116.078 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 36.775 | 35.439 | 55.324 | 31.674–55.420 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.600 | 16.419 | 43.199 | 15.537–45.349 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.633 | 15.786 | 31.966 | 14.460–32.923 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 63.184 | 53.306 | 66.711 | 48.512–83.537 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 100.504 | 53.759 | 121.182 | 52.139–171.992 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 4.125 | 3.861 | 13.503 | 3.763–15.560 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 55.578 | 40.380 | 74.281 | 39.595–96.619 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 23.498 | 18.889 | 38.950 | 18.093–74.564 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 32.544 | 28.586 | 43.298 | 28.017–46.730 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 18.225 | 12.629 | 30.022 | 10.566–35.048 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 51.397 | 28.937 | 82.617 | 28.931–82.667 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 38.227 | 37.088 | 54.246 | 37.052–54.249 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 23.531 | 17.906 | 41.092 | 16.433–42.609 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 18.028 | 16.361 | 31.545 | 14.499–34.770 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 60.950 | 44.536 | 81.488 | 40.132–94.530 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 107.708 | 53.579 | 127.792 | 50.378–177.959 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 12.090 | 4.274 | 16.050 | 3.994–16.344 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 351.274 | 351.274 | 351.274 | 351.274–351.274 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1949.651 | 1949.651 | 1949.651 | 1949.651–1949.651 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12655.698 | 12655.698 | 12655.698 | 12655.698–12655.698 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12670.441 | 12670.441 | 12670.441 | 12670.441–12670.441 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 289.900 | 289.900 | 289.900 | 289.900–289.900 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1895.268 | 1895.268 | 1895.268 | 1895.268–1895.268 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13355.938 | 13355.938 | 13355.938 | 13355.938–13355.938 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13398.998 | 13398.998 | 13398.998 | 13398.998–13398.998 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9066.772 | 9066.772 | 9066.772–9066.772 | 11725.335 | 87104.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16498.175 | 16498.175 | 16498.175–16498.175 | 29903.697 | 135744.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 15454.368 | 15481.075 | 15393.792–15511.288 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 16325.288 | 16325.288 | 16325.288–16325.288 | 16338.839 | 270432.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9937.651 | 9937.651 | 9937.651–9937.651 | 14303.756 | 86176.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16538.120 | 16538.120 | 16538.120–16538.120 | 28360.594 | 136848.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 19875.394 | 22824.640 | 18358.929–22893.366 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 24804.704 | 24804.704 | 24804.704–24804.704 | 24818.028 | 271456.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
