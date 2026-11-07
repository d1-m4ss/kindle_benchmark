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
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.219 | 30.597 | 15.033 | 44.655 | 17.015 | 29.437 | 12.096 | 32.773 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.471 | 27.367 | 13.178 | 28.942 | 15.936 | 29.570 | 9.901 | 29.946 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 16.040 | 15.310–16.451 | 5.501 | 95.672 |
| K_stock_bookends | 1 | 10 | 18.467 | 17.830–21.102 | 12.741 | 101.081 |

The observed median forced-GC heap difference in this control is **+2.427 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 56.909 | 48.169 | 71.274 | 46.329–84.482 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 27.517 | 22.096 | 36.217 | 21.084–50.238 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 29.372 | 27.214 | 42.389 | 26.712–42.774 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 17.015 | 13.726 | 29.437 | 12.096–32.773 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 49.456 | 28.390 | 91.658 | 27.756–99.321 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 35.764 | 33.140 | 53.943 | 31.100–54.986 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.032 | 16.301 | 41.271 | 15.157–42.334 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.219 | 15.758 | 30.597 | 15.033–44.655 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 42.456 | 40.048 | 50.026 | 32.684–63.169 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 95.672 | 58.828 | 117.607 | 46.478–164.186 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 5.501 | 3.200 | 7.100 | 3.182–7.423 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 53.006 | 37.955 | 71.355 | 37.833–108.347 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 33.290 | 23.398 | 64.480 | 23.040–66.272 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.409 | 26.611 | 42.264 | 26.522–43.592 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.936 | 11.924 | 29.570 | 9.901–29.946 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 35.403 | 26.668 | 84.090 | 26.289–97.500 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 35.111 | 34.198 | 37.392 | 33.071–49.047 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.101 | 14.710 | 37.537 | 14.607–38.820 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.471 | 14.438 | 27.367 | 13.178–28.942 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 69.768 | 51.841 | 78.921 | 42.886–93.893 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 101.081 | 58.073 | 127.116 | 56.703–168.401 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 12.741 | 8.810 | 14.329 | 4.422–16.089 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 296.682 | 296.682 | 296.682 | 296.682–296.682 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1880.046 | 1880.046 | 1880.046 | 1880.046–1880.046 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12290.063 | 12290.063 | 12290.063 | 12290.063–12290.063 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12305.159 | 12305.159 | 12305.159 | 12305.159–12305.159 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 226.405 | 226.405 | 226.405 | 226.405–226.405 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1572.930 | 1572.930 | 1572.930 | 1572.930–1572.930 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12939.053 | 12939.053 | 12939.053 | 12939.053–12939.053 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12989.484 | 12989.484 | 12989.484 | 12989.484–12989.484 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9040.522 | 9040.522 | 9040.522–9040.522 | 11755.845 | 86944.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16560.046 | 16560.046 | 16560.046–16560.046 | 36416.060 | 144432.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 16424.702 | 16827.753 | 15677.632–16845.581 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15570.976 | 15570.976 | 15570.976–15570.976 | 18798.182 | 274096.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10027.827 | 10027.827 | 10027.827–10027.827 | 13932.758 | 86736.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13726.831 | 13726.831 | 13726.831–13726.831 | 27669.956 | 126336.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 18910.077 | 21244.970 | 18258.202–21608.800 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 23522.562 | 23522.562 | 23522.562–23522.562 | 27588.198 | 267232.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
