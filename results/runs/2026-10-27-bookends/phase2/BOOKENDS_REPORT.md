# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `bookends_control`

Versions lock SHA-256: `c792a7f6cfd87cad3e4f4f44f45eae9070b409392d420b44dc24bb4639bd823d`
Reader flash setting: `unset`

Aggregated rows: 40; PASS=38; FAILED=0; UNSUPPORTED=2; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.741 | 31.501 | 10.766 | 33.272 | 16.936 | 31.784 | 10.811 | 34.863 |
| K_stock_bookends | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.947 | 31.043 | 14.510 | 32.310 | 18.330 | 29.887 | 11.940 | 35.465 |

## Bookends reader control

Each GC sample follows one complete `open → 10 page turns → close → forced GC → heap` cycle. There is one process per variant, so these are 10 within-process cycle samples, not 10 process replicates.

| Stack | Processes | GC samples | Forced-GC heap median MiB | Min–max MiB | Reader turn median ms | Open-book minimal median ms |
|:--|--:|--:|--:|:--|--:|--:|
| A_stock | 1 | 10 | 14.277 | 14.233–14.379 | 4.655 | 99.453 |
| K_stock_bookends | 1 | 10 | 18.020 | 17.163–20.826 | 16.663 | 103.548 |

The observed median forced-GC heap difference in this control is **+3.743 MiB**. This is a descriptive within-process comparison, not a causal or cross-device estimate.

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| K_stock_bookends | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 59.306 | 53.421 | 77.157 | 52.833–87.521 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 26.607 | 22.190 | 28.497 | 21.870–33.356 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.889 | 27.049 | 29.516 | 26.289–30.219 |
| A_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.936 | 13.013 | 31.784 | 10.811–34.863 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 42.227 | 27.881 | 95.606 | 27.658–115.959 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 61.318 | 47.739 | 151.238 | 47.518–162.927 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.163 | 17.401 | 24.473 | 15.379–25.712 |
| A_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.741 | 15.504 | 31.501 | 10.766–33.272 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 52.998 | 48.177 | 65.046 | 46.746–83.004 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 99.453 | 52.169 | 119.590 | 51.697–168.951 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 4.655 | 3.966 | 6.051 | 3.892–14.261 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 49.627 | 41.057 | 85.907 | 40.614–115.835 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 49.070 | 41.321 | 61.253 | 30.374–63.384 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 28.604 | 26.637 | 33.040 | 25.467–53.867 |
| K_stock_bookends | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 18.330 | 12.326 | 29.887 | 11.940–35.465 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 46.302 | 28.433 | 86.373 | 28.300–90.564 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 60.617 | 47.514 | 124.618 | 46.830–166.706 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.533 | 17.569 | 25.002 | 16.034–26.406 |
| K_stock_bookends | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.947 | 15.219 | 31.043 | 14.510–32.310 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 70.808 | 53.287 | 76.317 | 49.970–76.825 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 103.548 | 58.569 | 133.079 | 58.402–178.017 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 16.663 | 16.415 | 16.777 | 14.529–17.610 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 419.691 | 419.691 | 419.691 | 419.691–419.691 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1882.439 | 1882.439 | 1882.439 | 1882.439–1882.439 |
| A_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13810.244 | 13810.244 | 13810.244 | 13810.244–13810.244 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13933.165 | 13933.165 | 13933.165 | 13933.165–13933.165 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 243.688 | 243.688 | 243.688 | 243.688–243.688 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1736.553 | 1736.553 | 1736.553 | 1736.553–1736.553 |
| K_stock_bookends | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 14933.835 | 14933.835 | 14933.835 | 14933.835–14933.835 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 15117.162 | 15117.162 | 15117.162 | 15117.162–15117.162 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 8958.152 | 8958.152 | 8958.152–8958.152 | 11948.974 | 85712.000 |
| A_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13560.977 | 13560.977 | 13560.977–13560.977 | 35198.361 | 134256.000 |
| A_stock | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 14620.152 | 14675.787 | 14575.082–14724.492 | — | — |
| A_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14640.324 | 14640.324 | 14640.324–14640.324 | 17517.529 | 261856.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9953.195 | 9953.195 | 9953.195–9953.195 | 11601.653 | 88096.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13746.172 | 13746.172 | 13746.172–13746.172 | 26126.326 | 129008.000 |
| K_stock_bookends | warm | real_2692 | 2692 | post_reader_cycles_forced_gc | PASS | 1 | 10 | 18452.925 | 20981.719 | 17574.573–21325.910 | — | — |
| K_stock_bookends | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 22672.757 | 22672.757 | 22672.757–22672.757 | 25696.383 | 266304.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
