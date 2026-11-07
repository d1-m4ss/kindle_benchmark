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
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.727 | 28.680 | 14.766 | 29.234 | 18.157 | 30.735 | 11.910 | 32.184 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.872 | 30.235 | 13.346 | 32.137 | 18.037 | 29.299 | 11.450 | 34.140 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 14.382 | 14.313–14.405 | 4.133 | 95.657 |
| K_stock_bookends | 1 | 10 | 18.419 | 17.780–21.142 | 11.700 | 104.297 |

The observed median forced-GC heap difference in this control is **+4.037 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 56.600 | 43.312 | 77.777 | 39.432–96.889 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 27.657 | 25.794 | 40.855 | 23.134–44.354 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 29.002 | 27.800 | 33.179 | 27.035–46.576 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 18.157 | 12.634 | 30.735 | 11.910–32.184 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 42.184 | 30.271 | 93.857 | 27.913–99.363 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 38.718 | 35.423 | 52.941 | 33.558–60.002 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.521 | 18.557 | 38.848 | 15.944–45.488 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.727 | 15.675 | 28.680 | 14.766–29.234 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 51.630 | 46.506 | 62.063 | 45.069–82.392 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 95.657 | 52.780 | 117.420 | 52.528–165.958 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 4.133 | 3.738 | 6.308 | 3.730–12.712 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 64.968 | 50.330 | 82.217 | 46.914–84.103 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 34.083 | 23.291 | 63.036 | 22.846–65.974 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 28.215 | 27.116 | 31.248 | 26.941–48.128 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 18.037 | 13.365 | 29.299 | 11.450–34.140 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 41.441 | 28.111 | 93.166 | 27.861–99.377 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 38.160 | 34.931 | 54.480 | 34.571–55.497 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 24.316 | 18.487 | 42.246 | 14.706–45.067 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.872 | 14.963 | 30.235 | 13.346–32.137 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 64.529 | 57.305 | 79.865 | 56.689–87.465 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 104.297 | 60.977 | 129.759 | 58.831–175.550 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 11.700 | 6.017 | 14.300 | 4.512–16.149 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 233.521 | 233.521 | 233.521 | 233.521–233.521 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1703.833 | 1703.833 | 1703.833 | 1703.833–1703.833 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12363.825 | 12363.825 | 12363.825 | 12363.825–12363.825 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12378.600 | 12378.600 | 12378.600 | 12378.600–12378.600 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 242.826 | 242.826 | 242.826 | 242.826–242.826 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1704.070 | 1704.070 | 1704.070 | 1704.070–1704.070 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13438.210 | 13438.210 | 13438.210 | 13438.210–13438.210 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13510.868 | 13510.868 | 13510.868 | 13510.868–13510.868 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9031.175 | 9031.175 | 9031.175–9031.175 | 11980.890 | 86704.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13574.741 | 13574.741 | 13574.741–13574.741 | 29143.938 | 127696.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 14727.003 | 14748.222 | 14656.058–14750.757 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14799.136 | 14799.136 | 14799.136–14799.136 | 18027.826 | 269040.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9921.425 | 9921.425 | 9921.425–9921.425 | 14197.464 | 86384.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15206.468 | 15206.468 | 15206.468–15206.468 | 30628.864 | 136176.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 18860.911 | 21217.760 | 18206.804–21649.519 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 23105.057 | 23105.057 | 23105.057–23105.057 | 27031.127 | 255280.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
