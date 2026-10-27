# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `71c62562577d75d79b6dab0405876eeae7ea19ad7d5db59667c6c9cf1bd57e06`
Reader flash setting: `unset`

Aggregated rows: 553; PASS=545; FAILED=0; UNSUPPORTED=8; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R0_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.520 | 26.372 | 12.634 | 28.187 | 15.675 | 24.272 | 9.520 | 27.657 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.088 | 28.742 | 7.341 | 30.886 | 13.441 | 30.194 | 9.425 | 33.666 |
| R11_project_title_vos | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 16.044 | 16.132 | 13.143 | 16.254 | 16.094 | 16.161 | 15.755 | 16.629 |
| R12_leanui | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 15.966 | 18.408 | 12.723 | 20.913 | 16.106 | 16.191 | 15.648 | 16.629 |
| R13_m1n1mal | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.380 | 25.312 | 13.615 | 27.453 | 15.684 | 23.742 | 10.629 | 26.066 |
| R1_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.699 | 25.144 | 9.929 | 27.546 | 14.495 | 27.079 | 9.357 | 27.955 |
| R2_simpleui | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 15.937 | 30.327 | 7.417 | 35.230 | 12.801 | 28.548 | 10.354 | 31.870 |
| R3_zenos | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 16.100 | 27.400 | 5.455 | 29.395 | 16.133 | 27.447 | 6.586 | 29.820 |
| R4_project_title | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 16.085 | 16.121 | 8.030 | 16.173 | 16.088 | 16.156 | 15.828 | 16.679 |
| R5_vos | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.650 | 22.519 | 12.857 | 26.617 | 15.283 | 25.983 | 8.452 | 27.889 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.084 | 28.390 | 7.491 | 31.528 | 13.129 | 29.262 | 11.048 | 35.832 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 16.102 | 26.503 | 6.357 | 27.281 | 16.132 | 26.903 | 6.536 | 27.335 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 17.244 | 27.043 | 11.765 | 32.070 | 14.992 | 26.360 | 10.002 | 28.765 |
| R9_simpleui_vos | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 15.128 | 30.224 | 8.200 | 43.277 | 14.913 | 29.812 | 10.632 | 33.788 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 133.322 | 186.127 | 129.809 | 219.762 | 133.870 | 148.485 | 116.760 | 228.836 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 17.851 | 24.690 | 14.793 | 108.936 | 16.311 | 22.659 | 8.624 | 98.786 |
| R1_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 133.023 | 149.959 | 130.734 | 184.794 | 132.969 | 148.828 | 126.886 | 170.863 |
| R1_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 37.531 | 49.302 | 21.590 | 65.536 | 37.703 | 54.308 | 30.457 | 70.630 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 148.855 | 172.734 | 129.976 | 251.142 | 134.483 | 148.661 | 127.010 | 226.544 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 17.369 | 20.848 | 9.489 | 95.837 | 16.096 | 21.494 | 8.374 | 96.248 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 133.035 | 158.805 | 123.937 | 224.254 | 132.514 | 149.102 | 118.900 | 182.573 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 28.984 | 43.584 | 13.984 | 49.187 | 16.241 | 18.611 | 9.958 | 46.158 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 145.489 | 149.702 | 130.817 | 230.751 | 148.008 | 169.337 | 124.547 | 190.512 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 44.526 | 60.935 | 27.068 | 95.464 | 40.239 | 51.127 | 25.326 | 83.281 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R0_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R11_project_title_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R12_leanui | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R13_m1n1mal | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R1_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R4_project_title | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R5_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R8_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 14.495 ms vs 15.675 ms (7.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.699 ms vs 17.520 ms (10.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 12.801 ms vs 15.675 ms (18.3% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.937 ms vs 17.520 ms (9.0% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 15.675 ms vs 16.133 ms (2.8% lower) (UX-level comparison: books/page differs, 10.000 vs 5.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.100 ms vs 17.520 ms (8.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (warm, real_2692, 2692 books): 15.675 ms vs 16.088 ms (2.6% lower) (UX-level comparison: books/page differs, 10.000 vs 14.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.085 ms vs 17.520 ms (8.2% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 15.283 ms vs 15.675 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.650 ms vs 17.520 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 12.801 ms vs 13.129 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.937 ms vs 16.084 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 16.132 ms vs 16.133 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.100 ms vs 16.102 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R8_vos_bookshelf` has a lower descriptive median than `R5_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 14.992 ms vs 15.283 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.650 ms vs 17.244 ms (9.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 12.801 ms vs 14.913 ms (14.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.128 ms vs 15.937 ms (5.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 13.441 ms vs 14.913 ms (9.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.128 ms vs 16.088 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R11_project_title_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 16.088 ms vs 16.094 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.044 ms vs 16.085 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R0_stock | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 41.081 | 41.081 | 41.081 | 41.081–41.081 |
| R0_stock | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 36.394 | 36.394 | 36.394 | 36.394–36.394 |
| R0_stock | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 27.243 | 26.277 | 27.418 | 26.035–27.462 |
| R0_stock | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 27.247 | 26.804 | 27.295 | 26.693–27.307 |
| R0_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 61.694 | 44.548 | 84.064 | 43.312–85.609 |
| R0_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 28.520 | 24.366 | 36.956 | 22.171–48.531 |
| R0_stock | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.656 | 16.641 | 16.681 | 16.635–16.682 |
| R0_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.773 | 26.594 | 37.009 | 26.346–37.019 |
| R0_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.675 | 13.023 | 24.272 | 9.520–27.657 |
| R0_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 26.818 | 25.764 | 36.883 | 25.064–37.167 |
| R0_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 82.999 | 44.868 | 167.161 | 43.180–172.507 |
| R0_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 24.114 | 15.203 | 36.368 | 13.906–37.380 |
| R0_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.520 | 15.442 | 26.372 | 12.634–28.187 |
| R0_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 62.132 | 47.294 | 76.712 | 43.569–83.070 |
| R0_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 105.470 | 58.626 | 121.938 | 57.591–179.930 |
| R0_stock | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.648 | 16.297 | 16.679 | 13.557–16.684 |
| R0_stock | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 664.320 | 664.320 | 664.320 | 664.320–664.320 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 14.627 | 14.627 | 14.627 | 14.627–14.627 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 55.574 | 55.574 | 55.574 | 55.574–55.574 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 15.405 | 14.632 | 17.490 | 14.439–18.011 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 50.116 | 48.258 | 54.660 | 47.794–55.796 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 133.870 | 132.337 | 148.485 | 116.760–228.836 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.311 | 9.890 | 22.659 | 8.624–98.786 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 28.945 | 24.470 | 100.162 | 24.293–119.643 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 133.322 | 132.246 | 186.127 | 129.809–219.762 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 17.851 | 15.474 | 24.690 | 14.793–108.936 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 166.831 | 139.115 | 192.055 | 136.282–236.608 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 246.017 | 219.212 | 265.974 | 177.472–267.145 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 26.630 | 24.572 | 28.765 | 24.190–30.568 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.639 | 16.624 | 16.667 | 16.616–16.680 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.645 | 13.309 | 31.267 | 11.970–31.703 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.441 | 10.329 | 30.194 | 9.425–33.666 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 57.495 | 49.405 | 66.245 | 49.245–70.856 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 172.500 | 142.626 | 187.524 | 141.763–192.547 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 27.828 | 18.472 | 54.126 | 17.297–57.425 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.088 | 8.533 | 28.742 | 7.341–30.886 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 115.528 | 106.988 | 130.719 | 102.117–141.932 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 119.980 | 83.760 | 150.205 | 77.842–202.809 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 47.520 | 45.218 | 50.768 | 43.158–51.030 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 21.513 | 19.556 | 57.422 | 18.770–329.065 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1386.388 | 1386.388 | 1386.388 | 1386.388–1386.388 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.642 | 12.259 | 16.680 | 6.097–16.694 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 39.586 | 39.586 | 39.586 | 39.586–39.586 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 33.038 | 33.038 | 33.038 | 33.038–33.038 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 42.457 | 39.942 | 42.879 | 39.313–42.985 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 36.740 | 33.959 | 37.202 | 33.264–37.317 |
| R11_project_title_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 32.492 | 30.826 | 37.041 | 30.771–40.592 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 40.281 | 35.359 | 53.055 | 28.514–53.502 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.655 | 16.628 | 16.692 | 16.594–16.697 |
| R11_project_title_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 36.802 | 32.817 | 46.936 | 32.399–47.033 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.094 | 16.036 | 16.161 | 15.755–16.629 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 35.497 | 32.656 | 47.345 | 31.777–49.543 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 47.264 | 41.846 | 49.927 | 38.550–50.011 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 19.276 | 16.952 | 26.472 | 16.659–29.183 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.044 | 15.969 | 16.132 | 13.143–16.254 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 61.430 | 56.254 | 67.292 | 50.586–81.582 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 103.587 | 60.212 | 122.197 | 58.984–174.327 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.658 | 16.635 | 16.674 | 16.624–16.680 |
| R11_project_title_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 500.000 | 500.000 | 500.000 | 500.000–500.000 |
| R12_leanui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 30.847 | 30.847 | 30.847 | 30.847–30.847 |
| R12_leanui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 28.649 | 28.649 | 28.649 | 28.649–28.649 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 30.574 | 29.176 | 30.740 | 28.826–30.781 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 29.926 | 29.586 | 30.799 | 29.501–31.017 |
| R12_leanui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 46.683 | 45.054 | 53.429 | 44.879–55.960 |
| R12_leanui | warm | real_2692 | 2692 | close_book | PASS | 10 | 34.189 | 30.097 | 37.752 | 27.986–42.881 |
| R12_leanui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.662 | 16.353 | 16.664 | 13.720–16.668 |
| R12_leanui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 31.928 | 29.281 | 37.491 | 27.731–41.546 |
| R12_leanui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.106 | 16.010 | 16.191 | 15.648–16.629 |
| R12_leanui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 31.664 | 29.776 | 36.734 | 28.583–37.093 |
| R12_leanui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 55.852 | 51.078 | 60.742 | 49.654–78.065 |
| R12_leanui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.523 | 19.333 | 25.961 | 17.403–34.997 |
| R12_leanui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.966 | 14.043 | 18.408 | 12.723–20.913 |
| R12_leanui | warm | real_2692 | 2692 | open_book | PASS | 10 | 55.592 | 49.551 | 62.382 | 43.444–86.120 |
| R12_leanui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 99.322 | 58.829 | 110.693 | 57.938–161.135 |
| R12_leanui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.671 | 16.659 | 16.702 | 16.620–16.703 |
| R12_leanui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 500.011 | 500.011 | 500.011 | 500.011–500.011 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 31.928 | 31.928 | 31.928 | 31.928–31.928 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 35.648 | 35.648 | 35.648 | 35.648–35.648 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 27.983 | 27.370 | 28.617 | 27.217–28.776 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 26.699 | 25.979 | 27.721 | 25.799–27.976 |
| R13_m1n1mal | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 55.699 | 42.874 | 76.453 | 42.562–78.079 |
| R13_m1n1mal | warm | real_2692 | 2692 | close_book | PASS | 10 | 28.898 | 22.850 | 42.246 | 21.106–48.686 |
| R13_m1n1mal | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.669 | 16.634 | 16.678 | 16.614–16.704 |
| R13_m1n1mal | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 26.805 | 25.747 | 36.949 | 25.328–38.277 |
| R13_m1n1mal | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.684 | 11.789 | 23.742 | 10.629–26.066 |
| R13_m1n1mal | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 26.288 | 25.195 | 36.334 | 25.185–37.779 |
| R13_m1n1mal | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 81.741 | 45.817 | 145.405 | 45.532–176.083 |
| R13_m1n1mal | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 21.622 | 14.819 | 37.586 | 14.246–38.024 |
| R13_m1n1mal | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.380 | 15.640 | 25.312 | 13.615–27.453 |
| R13_m1n1mal | warm | real_2692 | 2692 | open_book | PASS | 10 | 63.115 | 55.856 | 71.378 | 53.820–84.990 |
| R13_m1n1mal | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 110.808 | 60.628 | 131.206 | 59.618–182.889 |
| R13_m1n1mal | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.660 | 15.546 | 16.686 | 6.079–16.755 |
| R13_m1n1mal | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 668.337 | 668.337 | 668.337 | 668.337–668.337 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 33.386 | 33.386 | 33.386 | 33.386–33.386 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 34.965 | 34.965 | 34.965 | 34.965–34.965 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 26.926 | 26.332 | 27.231 | 26.184–27.307 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 26.175 | 25.155 | 26.645 | 24.900–26.762 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 132.969 | 131.933 | 148.828 | 126.886–170.863 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 37.703 | 32.835 | 54.308 | 30.457–70.630 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 24.819 | 23.047 | 69.972 | 22.518–87.087 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 133.023 | 131.915 | 149.959 | 130.734–184.794 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 37.531 | 30.980 | 49.302 | 21.590–65.536 |
| R1_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 57.454 | 51.356 | 74.538 | 50.515–75.939 |
| R1_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 29.798 | 24.285 | 104.482 | 23.679–117.577 |
| R1_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 9.575 | 6.390 | 13.270 | 6.338–14.481 |
| R1_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.669 | 16.634 | 16.688 | 16.633–16.711 |
| R1_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 26.498 | 24.266 | 33.516 | 24.003–34.133 |
| R1_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.495 | 11.031 | 27.079 | 9.357–27.955 |
| R1_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 25.549 | 24.143 | 34.745 | 22.061–37.026 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 87.779 | 60.736 | 144.956 | 53.923–164.434 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.219 | 18.443 | 48.590 | 16.350–114.243 |
| R1_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.699 | 13.575 | 25.144 | 9.929–27.546 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 69.593 | 64.068 | 83.089 | 62.017–89.241 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 110.652 | 66.282 | 132.431 | 59.249–187.242 |
| R1_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 26.852 | 25.000 | 28.680 | 23.532–29.392 |
| R1_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.659 | 16.641 | 16.665 | 16.626–16.696 |
| R1_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 742.391 | 742.391 | 742.391 | 742.391–742.391 |
| R2_simpleui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 13.977 | 13.977 | 13.977 | 13.977–13.977 |
| R2_simpleui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 54.170 | 54.170 | 54.170 | 54.170–54.170 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 19.475 | 15.718 | 20.066 | 14.779–20.214 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 52.019 | 49.690 | 52.266 | 49.108–52.328 |
| R2_simpleui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 143.254 | 121.457 | 161.659 | 117.333–166.042 |
| R2_simpleui | warm | real_2692 | 2692 | close_book | PASS | 10 | 231.974 | 184.232 | 252.002 | 115.631–258.065 |
| R2_simpleui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.632 | 16.020 | 35.711 | 11.759–146.104 |
| R2_simpleui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.641 | 13.031 | 30.864 | 12.757–32.593 |
| R2_simpleui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.801 | 11.390 | 28.548 | 10.354–31.870 |
| R2_simpleui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 65.733 | 54.134 | 75.545 | 53.596–84.474 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 158.810 | 130.959 | 169.616 | 125.933–176.480 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 23.778 | 19.365 | 24.422 | 19.140–24.559 |
| R2_simpleui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.937 | 8.958 | 30.327 | 7.417–35.230 |
| R2_simpleui | warm | real_2692 | 2692 | open_book | PASS | 10 | 98.051 | 85.235 | 149.918 | 79.326–188.324 |
| R2_simpleui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 123.967 | 79.717 | 143.757 | 67.777–170.654 |
| R2_simpleui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 18.029 | 16.675 | 119.764 | 16.674–123.273 |
| R2_simpleui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1217.143 | 1217.143 | 1217.143 | 1217.143–1217.143 |
| R2_simpleui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.640 | 14.702 | 16.701 | 6.481–16.716 |
| R3_zenos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 102.009 | 102.009 | 102.009 | 102.009–102.009 |
| R3_zenos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 32.477 | 32.477 | 32.477 | 32.477–32.477 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 79.240 | 77.334 | 82.935 | 76.857–83.859 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 32.552 | 32.448 | 33.072 | 32.422–33.202 |
| R3_zenos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 56.573 | 47.526 | 66.051 | 35.294–67.703 |
| R3_zenos | warm | real_2692 | 2692 | close_book | PASS | 10 | 59.759 | 51.721 | 66.463 | 34.720–70.128 |
| R3_zenos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 33.282 | 26.608 | 33.342 | 19.554–33.349 |
| R3_zenos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 41.782 | 41.311 | 56.691 | 40.841–59.073 |
| R3_zenos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.133 | 8.782 | 27.447 | 6.586–29.820 |
| R3_zenos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 33.120 | 28.571 | 40.523 | 26.270–41.200 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 35.337 | 33.130 | 45.294 | 32.026–52.652 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 33.287 | 20.886 | 47.553 | 19.988–48.880 |
| R3_zenos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.100 | 6.524 | 27.400 | 5.455–29.395 |
| R3_zenos | warm | real_2692 | 2692 | open_book | PASS | 10 | 65.992 | 51.366 | 76.078 | 49.987–87.027 |
| R3_zenos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 130.416 | 82.196 | 144.775 | 70.235–189.501 |
| R3_zenos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 33.197 | 33.172 | 39.303 | 33.149–42.161 |
| R3_zenos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 519.000 | 519.000 | 519.000 | 519.000–519.000 |
| R3_zenos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 25.325 | 10.905 | 25.663 | 7.927–25.684 |
| R4_project_title | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 26.573 | 26.573 | 26.573 | 26.573–26.573 |
| R4_project_title | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 25.895 | 25.895 | 25.895 | 25.895–25.895 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 26.768 | 26.199 | 27.669 | 26.057–27.894 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 27.532 | 27.090 | 27.696 | 26.979–27.737 |
| R4_project_title | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 39.078 | 37.577 | 44.325 | 36.567–48.403 |
| R4_project_title | warm | real_2692 | 2692 | close_book | PASS | 10 | 23.753 | 20.621 | 27.842 | 19.758–30.896 |
| R4_project_title | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.660 | 16.635 | 16.669 | 16.616–16.673 |
| R4_project_title | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.728 | 24.410 | 33.104 | 23.517–33.552 |
| R4_project_title | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.088 | 16.039 | 16.156 | 15.828–16.679 |
| R4_project_title | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 27.398 | 26.709 | 31.975 | 26.528–34.263 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 43.098 | 40.395 | 50.938 | 40.394–50.948 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 19.361 | 14.267 | 26.115 | 13.257–26.466 |
| R4_project_title | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.085 | 15.953 | 16.121 | 8.030–16.173 |
| R4_project_title | warm | real_2692 | 2692 | open_book | PASS | 10 | 50.949 | 45.731 | 55.137 | 40.561–64.799 |
| R4_project_title | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 89.898 | 51.780 | 110.528 | 44.752–156.306 |
| R4_project_title | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.657 | 16.610 | 16.682 | 16.608–16.720 |
| R4_project_title | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 499.989 | 499.989 | 499.989 | 499.989–499.989 |
| R5_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 41.831 | 41.831 | 41.831 | 41.831–41.831 |
| R5_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 43.337 | 43.337 | 43.337 | 43.337–43.337 |
| R5_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 35.635 | 34.204 | 43.914 | 33.846–45.984 |
| R5_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 32.924 | 32.636 | 35.278 | 32.564–35.867 |
| R5_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 64.435 | 41.849 | 90.639 | 37.021–99.141 |
| R5_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 50.275 | 38.718 | 63.190 | 34.079–65.965 |
| R5_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.642 | 16.624 | 16.666 | 16.613–16.681 |
| R5_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 35.078 | 32.892 | 45.959 | 31.907–46.749 |
| R5_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.283 | 10.760 | 25.983 | 8.452–27.889 |
| R5_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 34.338 | 32.489 | 47.952 | 32.107–49.503 |
| R5_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 57.787 | 48.673 | 83.366 | 37.173–85.768 |
| R5_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 24.550 | 17.393 | 26.314 | 16.937–27.875 |
| R5_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.650 | 14.309 | 22.519 | 12.857–26.617 |
| R5_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 51.629 | 48.898 | 75.664 | 45.077–76.598 |
| R5_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 113.867 | 64.586 | 132.813 | 60.288–186.422 |
| R5_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.669 | 16.246 | 16.699 | 13.475–16.700 |
| R5_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 732.405 | 732.405 | 732.405 | 732.405–732.405 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 13.142 | 13.142 | 13.142 | 13.142–13.142 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 55.350 | 55.350 | 55.350 | 55.350–55.350 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 15.644 | 13.714 | 21.621 | 13.232–23.115 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 50.978 | 49.029 | 52.156 | 48.542–52.451 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 134.483 | 131.866 | 148.661 | 127.010–226.544 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.096 | 9.336 | 21.494 | 8.374–96.248 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 22.912 | 19.687 | 83.093 | 19.313–112.314 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 148.855 | 132.121 | 172.734 | 129.976–251.142 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 17.369 | 13.180 | 20.848 | 9.489–95.837 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 152.074 | 122.664 | 156.656 | 122.058–157.863 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 209.979 | 103.022 | 242.623 | 77.852–270.855 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 34.430 | 32.184 | 42.089 | 30.041–48.030 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.660 | 15.787 | 28.958 | 7.984–139.486 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.654 | 12.828 | 30.663 | 11.949–31.798 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.129 | 11.345 | 29.262 | 11.048–35.832 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 60.139 | 50.879 | 62.859 | 47.160–63.923 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 146.498 | 127.536 | 159.488 | 126.466–160.742 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.276 | 17.456 | 22.904 | 17.320–23.202 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.084 | 9.280 | 28.390 | 7.491–31.528 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 97.629 | 77.025 | 150.075 | 76.677–161.639 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 118.644 | 86.412 | 144.554 | 59.646–163.952 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 41.544 | 38.335 | 44.100 | 37.466–44.408 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 17.075 | 16.624 | 32.515 | 16.219–165.075 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1035.792 | 1035.792 | 1035.792 | 1035.792–1035.792 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.654 | 10.588 | 16.676 | 6.998–16.726 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 102.850 | 102.850 | 102.850 | 102.850–102.850 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 32.065 | 32.065 | 32.065 | 32.065–32.065 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 74.602 | 71.083 | 75.679 | 70.203–75.948 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 32.080 | 31.843 | 32.720 | 31.784–32.880 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 132.514 | 130.958 | 149.102 | 118.900–182.573 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.241 | 13.320 | 18.611 | 9.958–46.158 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 24.899 | 22.404 | 69.990 | 21.402–75.197 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 133.035 | 131.995 | 158.805 | 123.937–224.254 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 28.984 | 21.833 | 43.584 | 13.984–49.187 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 65.431 | 48.276 | 68.624 | 47.063–69.464 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 36.352 | 33.917 | 42.230 | 33.279–42.885 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 9.863 | 8.748 | 11.131 | 8.642–13.484 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 33.304 | 19.908 | 33.349 | 19.085–33.383 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 41.159 | 40.820 | 53.738 | 40.692–53.791 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.132 | 9.308 | 26.903 | 6.536–27.335 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 39.757 | 32.260 | 43.755 | 31.914–43.959 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 36.543 | 33.313 | 45.860 | 33.302–45.997 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 33.349 | 24.898 | 48.861 | 20.391–63.635 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.102 | 7.156 | 26.503 | 6.357–27.281 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 120.637 | 76.858 | 137.939 | 73.263–140.193 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 123.731 | 80.363 | 154.828 | 76.334–194.307 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 27.517 | 25.832 | 38.596 | 25.773–79.580 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 33.169 | 33.097 | 45.343 | 33.068–54.955 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 563.236 | 563.236 | 563.236 | 563.236–563.236 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 25.025 | 7.938 | 25.549 | 7.558–26.030 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 44.071 | 44.071 | 44.071 | 44.071–44.071 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 47.676 | 47.676 | 47.676 | 47.676–47.676 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 41.901 | 41.045 | 42.725 | 40.831–42.931 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 32.898 | 32.805 | 34.637 | 32.782–35.072 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 148.008 | 131.533 | 169.337 | 124.547–190.512 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 40.239 | 28.298 | 51.127 | 25.326–83.281 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 28.190 | 24.320 | 107.482 | 23.202–242.181 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 145.489 | 131.863 | 149.702 | 130.817–230.751 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 44.526 | 36.938 | 60.935 | 27.068–95.464 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 71.706 | 42.612 | 84.539 | 41.408–95.007 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 44.954 | 36.859 | 131.234 | 32.700–139.793 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 9.988 | 7.266 | 12.206 | 7.187–15.177 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.660 | 16.625 | 16.696 | 16.587–16.705 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 35.618 | 32.844 | 44.557 | 32.702–45.144 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.992 | 11.548 | 26.360 | 10.002–28.765 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 34.592 | 31.924 | 44.787 | 31.257–46.695 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 52.657 | 43.758 | 60.198 | 39.828–62.273 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 23.233 | 17.556 | 26.522 | 16.031–37.693 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 17.244 | 15.154 | 27.043 | 11.765–32.070 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 132.879 | 117.109 | 153.650 | 115.106–173.702 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 125.725 | 98.117 | 158.538 | 74.126–196.477 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 26.929 | 25.004 | 30.264 | 23.114–32.510 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.656 | 16.555 | 16.683 | 15.897–16.697 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1042.055 | 1042.055 | 1042.055 | 1042.055–1042.055 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 13.964 | 13.964 | 13.964 | 13.964–13.964 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 51.657 | 51.657 | 51.657 | 51.657–51.657 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 15.660 | 15.186 | 18.918 | 15.068–19.732 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 46.671 | 46.033 | 50.049 | 45.874–50.893 |
| R9_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 160.608 | 138.717 | 172.615 | 136.794–178.094 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 238.117 | 221.545 | 246.336 | 188.402–250.394 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.584 | 11.448 | 17.136 | 7.902–21.460 |
| R9_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.665 | 12.546 | 30.600 | 11.962–31.151 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.913 | 11.548 | 29.812 | 10.632–33.788 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 57.217 | 44.191 | 72.066 | 43.255–78.046 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 160.368 | 144.174 | 183.557 | 140.679–187.640 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 29.016 | 19.603 | 56.791 | 18.918–58.247 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.128 | 8.884 | 30.224 | 8.200–43.277 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 117.053 | 103.837 | 134.851 | 100.721–135.154 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 132.864 | 78.674 | 141.885 | 60.057–165.559 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 19.368 | 18.366 | 44.309 | 16.967–143.356 |
| R9_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1244.173 | 1244.173 | 1244.173 | 1244.173–1244.173 |
| R9_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.648 | 7.446 | 16.694 | 6.927–16.698 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 260.615 | 260.615 | 260.615 | 260.615–260.615 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 342.104 | 342.104 | 342.104 | 342.104–342.104 |
| R0_stock | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 350.655 | 350.655 | 350.655 | 350.655–350.655 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 425.455 | 425.455 | 425.455 | 425.455–425.455 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 211.129 | 202.528 | 224.198 | 200.377–227.465 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 268.663 | 262.477 | 283.307 | 260.931–286.968 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 274.570 | 268.345 | 289.088 | 266.789–292.718 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 283.672 | 277.671 | 298.444 | 276.170–302.137 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 200.420 | 200.420 | 200.420 | 200.420–200.420 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1274.143 | 1274.143 | 1274.143 | 1274.143–1274.143 |
| R0_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11601.095 | 11601.095 | 11601.095 | 11601.095–11601.095 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11617.329 | 11617.329 | 11617.329 | 11617.329–11617.329 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 592.539 | 592.539 | 592.539 | 592.539–592.539 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 674.046 | 674.046 | 674.046 | 674.046–674.046 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 687.193 | 687.193 | 687.193 | 687.193–687.193 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 857.336 | 857.336 | 857.336 | 857.336–857.336 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 356.411 | 353.720 | 393.496 | 353.048–402.767 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 430.655 | 430.551 | 482.772 | 430.525–495.802 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 440.716 | 440.487 | 493.245 | 440.430–506.377 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 453.976 | 453.200 | 507.042 | 453.006–520.308 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 369.412 | 369.412 | 369.412 | 369.412–369.412 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1861.981 | 1861.981 | 1861.981 | 1861.981–1861.981 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 36799.773 | 36799.773 | 36799.773 | 36799.773–36799.773 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 61907.907 | 61907.907 | 61907.907 | 61907.907–61907.907 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 254.389 | 254.389 | 254.389 | 254.389–254.389 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 333.346 | 333.346 | 333.346 | 333.346–333.346 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 340.620 | 340.620 | 340.620 | 340.620–340.620 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 350.379 | 350.379 | 350.379 | 350.379–350.379 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 240.294 | 235.772 | 243.865 | 234.641–244.757 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 323.291 | 320.905 | 325.525 | 320.308–326.084 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 333.897 | 329.697 | 334.083 | 328.647–334.130 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 343.904 | 339.725 | 344.945 | 338.681–345.206 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 289.540 | 289.540 | 289.540 | 289.540–289.540 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1716.424 | 1716.424 | 1716.424 | 1716.424–1716.424 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 10370.922 | 10370.922 | 10370.922 | 10370.922–10370.922 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 10388.084 | 10388.084 | 10388.084 | 10388.084–10388.084 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 422.315 | 422.315 | 422.315 | 422.315–422.315 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 489.019 | 489.019 | 489.019 | 489.019–489.019 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 497.106 | 497.106 | 497.106 | 497.106–497.106 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 508.614 | 508.614 | 508.614 | 508.614–508.614 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 257.583 | 246.318 | 293.144 | 243.501–302.035 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 323.030 | 314.797 | 362.286 | 312.738–372.100 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 330.887 | 324.375 | 370.806 | 322.747–380.786 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 342.249 | 335.298 | 381.834 | 333.560–391.730 |
| R12_leanui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 253.885 | 253.885 | 253.885 | 253.885–253.885 |
| R12_leanui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1416.491 | 1416.491 | 1416.491 | 1416.491–1416.491 |
| R12_leanui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 10245.041 | 10245.041 | 10245.041 | 10245.041–10245.041 |
| R12_leanui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 10261.506 | 10261.506 | 10261.506 | 10261.506–10261.506 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 395.399 | 395.399 | 395.399 | 395.399–395.399 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 470.414 | 470.414 | 470.414 | 470.414–470.414 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 478.986 | 478.986 | 478.986 | 478.986–478.986 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 550.371 | 550.371 | 550.371 | 550.371–550.371 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 210.878 | 208.726 | 227.061 | 208.187–231.107 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 273.974 | 267.263 | 287.724 | 265.586–291.161 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 280.468 | 273.389 | 293.926 | 271.619–297.290 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 290.183 | 282.974 | 303.996 | 281.172–307.449 |
| R13_m1n1mal | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 207.089 | 207.089 | 207.089 | 207.089–207.089 |
| R13_m1n1mal | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1249.882 | 1249.882 | 1249.882 | 1249.882–1249.882 |
| R13_m1n1mal | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11638.471 | 11638.471 | 11638.471 | 11638.471–11638.471 |
| R13_m1n1mal | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11656.087 | 11656.087 | 11656.087 | 11656.087–11656.087 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 263.829 | 263.829 | 263.829 | 263.829–263.829 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 340.545 | 340.545 | 340.545 | 340.545–340.545 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 349.280 | 349.280 | 349.280 | 349.280–349.280 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 407.424 | 407.424 | 407.424 | 407.424–407.424 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 214.060 | 209.692 | 226.273 | 208.599–229.326 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 273.185 | 266.196 | 285.010 | 264.448–287.966 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 279.355 | 272.308 | 290.977 | 270.547–293.883 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 288.722 | 281.815 | 300.159 | 280.088–303.019 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 203.163 | 203.163 | 203.163 | 203.163–203.163 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1218.790 | 1218.790 | 1218.790 | 1218.790–1218.790 |
| R1_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 25896.985 | 25896.985 | 25896.985 | 25896.985–25896.985 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 25938.755 | 25938.755 | 25938.755 | 25938.755–25938.755 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 574.126 | 574.126 | 574.126 | 574.126–574.126 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 655.758 | 655.758 | 655.758 | 655.758–655.758 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 667.713 | 667.713 | 667.713 | 667.713–667.713 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 815.845 | 815.845 | 815.845 | 815.845–815.845 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 377.154 | 362.799 | 394.514 | 359.210–398.855 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 466.016 | 442.650 | 481.555 | 436.808–485.440 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 476.324 | 452.665 | 492.079 | 446.751–496.018 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 488.668 | 464.661 | 505.093 | 458.660–509.199 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 357.172 | 357.172 | 357.172 | 357.172–357.172 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1933.586 | 1933.586 | 1933.586 | 1933.586–1933.586 |
| R2_simpleui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 22557.156 | 22557.156 | 22557.156 | 22557.156–22557.156 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 22999.863 | 22999.863 | 22999.863 | 22999.863–22999.863 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 504.266 | 504.266 | 504.266 | 504.266–504.266 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 674.364 | 674.364 | 674.364 | 674.364–674.364 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 688.311 | 688.311 | 688.311 | 688.311–688.311 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 701.854 | 701.854 | 701.854 | 701.854–701.854 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 333.997 | 320.178 | 342.554 | 316.724–344.694 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 460.897 | 441.482 | 465.505 | 436.628–466.656 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 471.332 | 453.207 | 476.759 | 448.675–478.115 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 482.997 | 466.159 | 489.390 | 461.949–490.988 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 308.381 | 308.381 | 308.381 | 308.381–308.381 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2332.163 | 2332.163 | 2332.163 | 2332.163–2332.163 |
| R3_zenos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13164.481 | 13164.481 | 13164.481 | 13164.481–13164.481 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13184.009 | 13184.009 | 13184.009 | 13184.009–13184.009 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 231.437 | 231.437 | 231.437 | 231.437–231.437 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 288.878 | 288.878 | 288.878 | 288.878–288.878 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 296.252 | 296.252 | 296.252 | 296.252–296.252 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 307.208 | 307.208 | 307.208 | 307.208–307.208 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 212.063 | 211.940 | 237.174 | 211.909–243.452 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 273.331 | 272.166 | 297.326 | 271.874–303.325 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 279.744 | 278.594 | 304.263 | 278.306–310.392 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 289.887 | 288.231 | 314.791 | 287.817–321.017 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 225.623 | 225.623 | 225.623 | 225.623–225.623 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1269.864 | 1269.864 | 1269.864 | 1269.864–1269.864 |
| R4_project_title | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 9027.281 | 9027.281 | 9027.281 | 9027.281–9027.281 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 9042.256 | 9042.256 | 9042.256 | 9042.256–9042.256 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 311.375 | 311.375 | 311.375 | 311.375–311.375 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 405.734 | 405.734 | 405.734 | 405.734–405.734 |
| R5_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 415.255 | 415.255 | 415.255 | 415.255–415.255 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 460.628 | 460.628 | 460.628 | 460.628–460.628 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 223.657 | 221.813 | 238.808 | 221.352–242.596 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 295.687 | 295.002 | 323.298 | 294.831–330.200 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 302.924 | 302.277 | 330.201 | 302.116–337.020 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 312.817 | 312.137 | 339.795 | 311.967–346.539 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 231.718 | 231.718 | 231.718 | 231.718–231.718 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1610.689 | 1610.689 | 1610.689 | 1610.689–1610.689 |
| R5_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12337.558 | 12337.558 | 12337.558 | 12337.558–12337.558 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12364.253 | 12364.253 | 12364.253 | 12364.253–12364.253 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 566.562 | 566.562 | 566.562 | 566.562–566.562 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 643.316 | 643.316 | 643.316 | 643.316–643.316 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 655.849 | 655.849 | 655.849 | 655.849–655.849 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 808.480 | 808.480 | 808.480 | 808.480–808.480 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 350.508 | 340.457 | 374.332 | 337.945–380.288 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 445.634 | 417.484 | 458.215 | 410.447–461.360 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 456.462 | 427.623 | 468.404 | 420.413–471.389 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 469.358 | 439.747 | 481.055 | 432.344–483.980 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 352.700 | 352.700 | 352.700 | 352.700–352.700 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1823.265 | 1823.265 | 1823.265 | 1823.265–1823.265 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 34354.838 | 34354.838 | 34354.838 | 34354.838–34354.838 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 34634.674 | 34634.674 | 34634.674 | 34634.674–34634.674 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 527.542 | 527.542 | 527.542 | 527.542–527.542 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 705.151 | 705.151 | 705.151 | 705.151–705.151 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 721.856 | 721.856 | 721.856 | 721.856–721.856 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 736.293 | 736.293 | 736.293 | 736.293–736.293 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 289.737 | 285.043 | 317.679 | 283.869–324.664 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 401.294 | 401.063 | 432.186 | 401.005–439.909 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 411.264 | 411.065 | 442.122 | 411.015–449.836 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 422.822 | 422.598 | 453.788 | 422.543–461.530 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 289.255 | 289.255 | 289.255 | 289.255–289.255 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2366.641 | 2366.641 | 2366.641 | 2366.641–2366.641 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 26058.297 | 26058.297 | 26058.297 | 26058.297–26058.297 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 26085.729 | 26085.729 | 26085.729 | 26085.729–26085.729 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 435.411 | 435.411 | 435.411 | 435.411–435.411 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 539.319 | 539.319 | 539.319 | 539.319–539.319 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 549.998 | 549.998 | 549.998 | 549.998–549.998 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 604.244 | 604.244 | 604.244 | 604.244–604.244 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 243.513 | 231.357 | 263.654 | 228.319–268.689 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 323.153 | 312.632 | 346.387 | 310.002–352.196 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 331.669 | 319.953 | 355.496 | 317.024–361.452 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 342.298 | 331.680 | 368.345 | 329.025–374.857 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 232.486 | 232.486 | 232.486 | 232.486–232.486 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1614.187 | 1614.187 | 1614.187 | 1614.187–1614.187 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 28656.628 | 28656.628 | 28656.628 | 28656.628–28656.628 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 28712.989 | 28712.989 | 28712.989 | 28712.989–28712.989 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 609.865 | 609.865 | 609.865 | 609.865–609.865 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 687.503 | 687.503 | 687.503 | 687.503–687.503 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 700.398 | 700.398 | 700.398 | 700.398–700.398 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 919.617 | 919.617 | 919.617 | 919.617–919.617 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 358.240 | 342.304 | 396.076 | 338.320–405.535 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 431.371 | 414.963 | 480.621 | 410.861–492.933 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 441.182 | 424.517 | 490.880 | 420.350–503.304 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 452.904 | 436.416 | 504.026 | 432.294–516.807 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 342.464 | 342.464 | 342.464 | 342.464–342.464 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1828.199 | 1828.199 | 1828.199 | 1828.199–1828.199 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 23406.838 | 23406.838 | 23406.838 | 23406.838–23406.838 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 23898.344 | 23898.344 | 23898.344 | 23898.344–23898.344 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R0_stock | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 8918.718 | 8918.718 | 8918.718–8918.718 | 11042.607 | 87072.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10217.218 | 10217.218 | 10217.218–10217.218 | 14769.426 | 87744.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9219.370 | 9249.161 | 9102.737–9256.608 | 13889.824 | 82880.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9256.534 | 9292.003 | 9094.921–9300.870 | 15176.053 | 84096.000 |
| R0_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9266.077 | 9266.077 | 9266.077–9266.077 | 16421.436 | 82544.000 |
| R0_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9255.351 | 9255.351 | 9255.351–9255.351 | 9266.202 | 96688.000 |
| R0_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14488.601 | 14488.601 | 14488.601–14488.601 | 16806.533 | 256144.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 17191.778 | 17191.778 | 17191.778–17191.778 | 19313.348 | 105712.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18001.626 | 18001.626 | 18001.626–18001.626 | 22006.356 | 108416.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16565.932 | 16962.163 | 16488.736–17061.221 | 28276.848 | 98544.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17526.436 | 17917.695 | 17467.029–18015.510 | 21812.700 | 102528.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16553.354 | 16553.354 | 16553.354–16553.354 | 27758.838 | 98496.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18204.865 | 18204.865 | 18204.865–18204.865 | 22433.919 | 111936.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 82645.364 | 82645.364 | 82645.364–82645.364 | 84550.637 | 395520.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10307.017 | 10307.017 | 10307.017–10307.017 | 14681.165 | 85872.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10391.267 | 10391.267 | 10391.267–10391.267 | 17019.415 | 88096.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10268.942 | 10346.421 | 10267.220–10365.790 | 12079.457 | 85088.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10393.728 | 10395.143 | 10277.450–10395.497 | 17001.716 | 85312.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10352.431 | 10352.431 | 10352.431–10352.431 | 12173.688 | 85552.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10455.462 | 10455.462 | 10455.462–10455.462 | 19443.958 | 96768.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15149.182 | 15149.182 | 15149.182–15149.182 | 41071.167 | 236960.000 |
| R12_leanui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 11349.062 | 11349.062 | 11349.062–11349.062 | 15448.700 | 86688.000 |
| R12_leanui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11383.238 | 11383.238 | 11383.238–11383.238 | 17902.117 | 87536.000 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 11306.566 | 11441.923 | 11270.973–11475.762 | 15558.587 | 83008.000 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 11445.231 | 11543.103 | 11338.712–11567.571 | 17810.467 | 83936.000 |
| R12_leanui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 11359.008 | 11359.008 | 11359.008–11359.008 | 15470.765 | 82256.000 |
| R12_leanui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11503.153 | 11503.153 | 11503.153–11503.153 | 19851.315 | 97760.000 |
| R12_leanui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15384.548 | 15384.548 | 15384.548–15384.548 | 41325.877 | 241760.000 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9236.310 | 9236.310 | 9236.310–9236.310 | 12039.657 | 86096.000 |
| R13_m1n1mal | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10470.247 | 10470.247 | 10470.247–10470.247 | 15039.405 | 86688.000 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9314.927 | 9333.611 | 9100.872–9338.282 | 11925.232 | 83040.000 |
| R13_m1n1mal | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9316.794 | 9347.231 | 9122.923–9354.841 | 15178.568 | 84800.000 |
| R13_m1n1mal | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9293.380 | 9293.380 | 9293.380–9293.380 | 15285.607 | 81344.000 |
| R13_m1n1mal | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9388.821 | 9388.821 | 9388.821–9388.821 | 9399.673 | 96592.000 |
| R13_m1n1mal | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14412.622 | 14412.622 | 14412.622–14412.622 | 15631.594 | 266352.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9964.526 | 9964.526 | 9964.526–9964.526 | 14825.097 | 84736.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11201.687 | 11201.687 | 11201.687–11201.687 | 16033.868 | 88048.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9643.402 | 9695.321 | 9628.598–9708.301 | 13360.835 | 84432.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9684.777 | 9712.434 | 9633.012–9719.348 | 15588.265 | 86080.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9856.297 | 9856.297 | 9856.297–9856.297 | 17159.879 | 83344.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9933.008 | 9933.008 | 9933.008–9933.008 | 9943.512 | 97616.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 20767.827 | 20767.827 | 20767.827–20767.827 | 21508.813 | 322208.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15447.934 | 15447.934 | 15447.934–15447.934 | 25071.799 | 99312.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16166.191 | 16166.191 | 16166.191–16166.191 | 20395.908 | 101696.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 15478.938 | 15483.031 | 15437.258–15484.055 | 23658.057 | 96480.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16323.656 | 16328.169 | 16312.562–16329.297 | 20882.873 | 100384.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15462.770 | 15462.770 | 15462.770–15462.770 | 21197.786 | 96560.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16354.496 | 16354.496 | 16354.496–16354.496 | 16836.367 | 107040.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 67537.691 | 67537.691 | 67537.691–67537.691 | 67600.914 | 299120.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15313.520 | 15313.520 | 15313.520–15313.520 | 20292.377 | 92768.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18153.501 | 18153.501 | 18153.501–18153.501 | 29998.515 | 111200.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14399.298 | 14416.254 | 14343.829–14420.493 | 23668.026 | 95168.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 15835.642 | 15911.732 | 15803.376–15930.755 | 22921.019 | 98880.000 |
| R3_zenos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14392.177 | 14392.177 | 14392.177–14392.177 | 23602.532 | 94400.000 |
| R3_zenos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16010.643 | 16010.643 | 16010.643–16010.643 | 17532.723 | 107792.000 |
| R3_zenos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 22804.460 | 22804.460 | 22804.460–22804.460 | 22848.597 | 251184.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9073.587 | 9073.587 | 9073.587–9073.587 | 11105.977 | 85216.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9169.442 | 9169.442 | 9169.442–9169.442 | 15224.285 | 85232.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9419.317 | 9422.052 | 9396.907–9422.735 | 15826.588 | 82192.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9425.872 | 9444.991 | 9370.103–9449.771 | 15379.131 | 82272.000 |
| R4_project_title | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9374.333 | 9374.333 | 9374.333–9374.333 | 9997.560 | 82656.000 |
| R4_project_title | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9446.450 | 9446.450 | 9446.450–9446.450 | 17088.475 | 90944.000 |
| R4_project_title | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 13838.111 | 13838.111 | 13838.111–13838.111 | 35142.044 | 235744.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10174.401 | 10174.401 | 10174.401–10174.401 | 13986.519 | 86416.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11523.339 | 11523.339 | 11523.339–11523.339 | 16749.920 | 88608.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10111.644 | 10156.031 | 10107.210–10167.128 | 12043.184 | 86896.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10172.718 | 10180.715 | 10119.698–10182.714 | 16736.612 | 88528.000 |
| R5_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10307.624 | 10307.624 | 10307.624–10307.624 | 11336.468 | 85488.000 |
| R5_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10265.308 | 10265.308 | 10265.308–10265.308 | 17007.589 | 99024.000 |
| R5_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15700.640 | 15700.640 | 15700.640–15700.640 | 17961.667 | 261360.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16579.074 | 16579.074 | 16579.074–16579.074 | 17638.378 | 104368.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17224.266 | 17224.266 | 17224.266–17224.266 | 21455.847 | 106784.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 15959.528 | 15974.988 | 15846.392–15978.853 | 24759.744 | 96000.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16732.114 | 16851.111 | 16696.442–16880.860 | 21315.888 | 100352.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15895.384 | 15895.384 | 15895.384–15895.384 | 22446.872 | 96784.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16756.649 | 16756.649 | 16756.649–16756.649 | 17238.280 | 107696.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 76062.172 | 76062.172 | 76062.172–76062.172 | 76127.766 | 378496.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15730.418 | 15730.418 | 15730.418–15730.418 | 18471.634 | 95840.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18506.103 | 18506.103 | 18506.103–18506.103 | 30605.437 | 110080.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14668.951 | 14678.189 | 14660.178–14680.498 | 22473.453 | 93568.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16160.100 | 16755.853 | 16138.240–16904.791 | 23266.248 | 98944.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14750.854 | 14750.854 | 14750.854–14750.854 | 23991.749 | 93520.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16392.667 | 16392.667 | 16392.667–16392.667 | 17057.511 | 108416.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 30207.292 | 30207.292 | 30207.292–30207.292 | 30553.817 | 318960.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10759.698 | 10759.698 | 10759.698–10759.698 | 16210.159 | 87312.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 12109.499 | 12109.499 | 12109.499–12109.499 | 17441.562 | 89248.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10611.680 | 10637.973 | 10557.988–10644.547 | 13457.682 | 86736.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10582.152 | 10663.959 | 10561.695–10684.410 | 17277.659 | 89184.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10637.371 | 10637.371 | 10637.371–10637.371 | 13061.438 | 85200.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10702.273 | 10702.273 | 10702.273–10702.273 | 17307.967 | 100160.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 25211.601 | 25211.601 | 25211.601–25211.601 | 26164.379 | 323024.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16590.048 | 16590.048 | 16590.048–16590.048 | 26908.077 | 106336.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17430.044 | 17430.044 | 17430.044–17430.044 | 21336.856 | 110288.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16041.817 | 16115.458 | 16040.251–16133.868 | 26749.820 | 97344.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16990.681 | 17028.468 | 16940.435–17037.915 | 21317.632 | 101408.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16056.630 | 16056.630 | 16056.630–16056.630 | 24997.695 | 96080.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17714.017 | 17714.017 | 17714.017–17714.017 | 21901.122 | 112752.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 74038.263 | 74038.263 | 74038.263–74038.263 | 75207.679 | 316304.000 |

## Data-derived comparisons

- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 14.495 ms vs 15.675 ms (7.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.699 ms vs 17.520 ms (10.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 12.801 ms vs 15.675 ms (18.3% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.937 ms vs 17.520 ms (9.0% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 15.675 ms vs 16.133 ms (2.8% lower) (UX-level comparison: books/page differs, 10.000 vs 5.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.100 ms vs 17.520 ms (8.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (warm, real_2692, 2692 books): 15.675 ms vs 16.088 ms (2.6% lower) (UX-level comparison: books/page differs, 10.000 vs 14.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.085 ms vs 17.520 ms (8.2% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 15.283 ms vs 15.675 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.650 ms vs 17.520 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 12.801 ms vs 13.129 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.937 ms vs 16.084 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 16.132 ms vs 16.133 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.100 ms vs 16.102 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R8_vos_bookshelf` has a lower descriptive median than `R5_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 14.992 ms vs 15.283 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.650 ms vs 17.244 ms (9.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 12.801 ms vs 14.913 ms (14.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.128 ms vs 15.937 ms (5.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 13.441 ms vs 14.913 ms (9.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.128 ms vs 16.088 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R11_project_title_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 16.088 ms vs 16.094 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.044 ms vs 16.085 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
