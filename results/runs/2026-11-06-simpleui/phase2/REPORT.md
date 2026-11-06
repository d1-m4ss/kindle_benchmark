# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 162; PASS=162; FAILED=0; UNSUPPORTED=0; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.076 | 29.077 | 6.257 | 32.505 | 12.565 | 30.308 | 9.866 | 42.510 |
| R2_simpleui | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 15.316 | 28.042 | 7.987 | 32.714 | 13.481 | 28.139 | 11.082 | 30.783 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 15.582 | 28.898 | 8.406 | 29.632 | 13.390 | 28.042 | 11.157 | 30.561 |
| R9_simpleui_vos | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.061 | 29.025 | 8.328 | 33.909 | 12.819 | 29.878 | 9.664 | 40.700 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 148.417 | 184.108 | 126.826 | 220.629 | 134.443 | 148.648 | 121.316 | 228.489 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 17.660 | 22.576 | 10.342 | 95.468 | 17.535 | 23.036 | 8.865 | 95.974 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 132.933 | 157.457 | 127.275 | 234.335 | 132.685 | 132.939 | 112.161 | 203.329 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 20.760 | 32.184 | 10.130 | 107.387 | 16.889 | 24.616 | 9.825 | 94.570 |

## Comparative Findings

- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 13.390 ms vs 13.481 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.316 ms vs 15.582 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 12.819 ms vs 13.481 ms (4.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.316 ms vs 16.061 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 12.565 ms vs 12.819 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.061 ms vs 16.076 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 14.156 | 14.156 | 14.156 | 14.156–14.156 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 45.061 | 45.061 | 45.061 | 45.061–45.061 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 16.817 | 16.075 | 20.120 | 15.889–20.946 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 51.245 | 47.639 | 51.713 | 46.738–51.830 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 134.443 | 132.035 | 148.648 | 121.316–228.489 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 17.535 | 9.309 | 23.036 | 8.865–95.974 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 29.311 | 25.126 | 110.325 | 21.187–134.641 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 148.417 | 131.982 | 184.108 | 126.826–220.629 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 17.660 | 14.736 | 22.576 | 10.342–95.468 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 147.304 | 133.833 | 173.286 | 132.384–178.440 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 247.637 | 113.278 | 260.899 | 65.985–261.615 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 35.251 | 32.327 | 42.291 | 29.855–44.374 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 33.251 | 16.668 | 33.349 | 16.634–33.352 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.657 | 13.300 | 30.364 | 12.975–31.064 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.565 | 10.231 | 30.308 | 9.866–42.510 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 49.395 | 43.199 | 56.457 | 42.203–56.925 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 76.663 | 74.833 | 106.546 | 73.829–111.068 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 23.767 | 13.719 | 28.354 | 12.604–46.385 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.076 | 7.995 | 29.077 | 6.257–32.505 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 106.728 | 100.081 | 121.262 | 88.827–126.247 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 129.495 | 80.696 | 144.704 | 64.596–170.261 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 48.260 | 44.661 | 54.738 | 44.405–55.687 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.668 | 16.663 | 33.300 | 16.644–33.332 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1440.427 | 1440.427 | 1440.427 | 1440.427–1440.427 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.655 | 8.756 | 16.692 | 6.953–16.703 |
| R2_simpleui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 16.139 | 16.139 | 16.139 | 16.139–16.139 |
| R2_simpleui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 48.552 | 48.552 | 48.552 | 48.552–48.552 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 19.298 | 16.695 | 19.363 | 16.044–19.379 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 48.262 | 46.768 | 50.892 | 46.395–51.549 |
| R2_simpleui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 131.659 | 119.346 | 151.304 | 115.733–152.115 |
| R2_simpleui | warm | real_2692 | 2692 | close_book | PASS | 10 | 219.101 | 184.474 | 239.196 | 109.031–268.349 |
| R2_simpleui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.673 | 16.628 | 16.676 | 16.623–16.677 |
| R2_simpleui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.657 | 12.795 | 30.023 | 12.737–30.142 |
| R2_simpleui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.481 | 11.708 | 28.139 | 11.082–30.783 |
| R2_simpleui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 50.023 | 43.837 | 65.635 | 43.770–70.056 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 66.389 | 65.624 | 90.152 | 64.149–91.225 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 19.360 | 16.011 | 20.223 | 13.997–21.094 |
| R2_simpleui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.316 | 9.543 | 28.042 | 7.987–32.714 |
| R2_simpleui | warm | real_2692 | 2692 | open_book | PASS | 10 | 104.133 | 77.530 | 151.559 | 76.912–157.086 |
| R2_simpleui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 119.329 | 87.617 | 132.829 | 62.913–169.133 |
| R2_simpleui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.686 | 16.661 | 16.709 | 16.610–16.733 |
| R2_simpleui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1161.871 | 1161.871 | 1161.871 | 1161.871–1161.871 |
| R2_simpleui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.658 | 13.937 | 16.689 | 6.378–16.720 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 16.869 | 16.869 | 16.869 | 16.869–16.869 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 52.949 | 52.949 | 52.949 | 52.949–52.949 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 18.564 | 15.686 | 20.625 | 14.967–21.140 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 47.311 | 46.443 | 49.980 | 46.226–50.647 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 132.685 | 132.394 | 132.939 | 112.161–203.329 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.889 | 10.309 | 24.616 | 9.825–94.570 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 29.686 | 25.947 | 103.439 | 24.251–103.540 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 132.933 | 132.102 | 157.457 | 127.275–234.335 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 20.760 | 12.092 | 32.184 | 10.130–107.387 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 131.585 | 116.785 | 142.025 | 116.461–151.814 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 231.334 | 208.535 | 241.472 | 198.271–264.613 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 40.495 | 37.481 | 43.199 | 36.899–47.639 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.642 | 16.630 | 16.674 | 16.580–16.679 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.663 | 12.948 | 30.184 | 12.413–31.466 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.390 | 11.418 | 28.042 | 11.157–30.561 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 52.642 | 45.633 | 59.887 | 44.794–67.080 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 68.835 | 65.034 | 90.333 | 64.181–110.830 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 19.070 | 17.790 | 21.775 | 16.408–32.814 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.582 | 9.888 | 28.898 | 8.406–29.632 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 108.052 | 81.445 | 140.157 | 78.068–146.471 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 123.864 | 69.829 | 146.788 | 60.813–184.485 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 49.068 | 40.650 | 50.912 | 40.263–53.987 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.665 | 16.620 | 16.688 | 16.612–16.710 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1301.036 | 1301.036 | 1301.036 | 1301.036–1301.036 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.664 | 12.877 | 16.722 | 7.025–16.729 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 14.426 | 14.426 | 14.426 | 14.426–14.426 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 55.750 | 55.750 | 55.750 | 55.750–55.750 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 18.247 | 16.729 | 19.778 | 16.349–20.161 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 41.399 | 39.913 | 46.900 | 39.542–48.275 |
| R9_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 150.003 | 137.451 | 173.339 | 130.479–175.064 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 249.216 | 109.244 | 261.176 | 72.304–264.163 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.636 | 16.611 | 16.693 | 16.555–16.728 |
| R9_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.662 | 14.649 | 30.091 | 13.646–30.212 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.819 | 11.231 | 29.878 | 9.664–40.700 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 49.483 | 42.739 | 56.354 | 41.911–58.432 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 77.882 | 76.392 | 107.903 | 75.763–114.797 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 23.596 | 16.252 | 27.561 | 14.695–50.270 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.061 | 8.944 | 29.025 | 8.328–33.909 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 116.747 | 109.280 | 132.176 | 106.115–132.546 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 129.225 | 85.018 | 152.320 | 65.740–171.354 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.657 | 16.611 | 16.687 | 16.593–16.712 |
| R9_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1130.762 | 1130.762 | 1130.762 | 1130.762–1130.762 |
| R9_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.655 | 13.116 | 16.669 | 5.908–16.691 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 417.825 | 417.825 | 417.825 | 417.825–417.825 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 494.461 | 494.461 | 494.461 | 494.461–494.461 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 508.733 | 508.733 | 508.733 | 508.733–508.733 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 675.449 | 675.449 | 675.449 | 675.449–675.449 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 349.720 | 346.309 | 377.939 | 345.456–384.993 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 425.128 | 424.107 | 464.844 | 423.852–474.773 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 434.891 | 434.012 | 474.953 | 433.792–484.968 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 446.879 | 445.988 | 487.259 | 445.765–497.355 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 349.531 | 349.531 | 349.531 | 349.531–349.531 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1740.275 | 1740.275 | 1740.275 | 1740.275–1740.275 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 34838.777 | 34838.777 | 34838.777 | 34838.777–34838.777 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 34886.727 | 34886.727 | 34886.727 | 34886.727–34886.727 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 394.336 | 394.336 | 394.336 | 394.336–394.336 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 473.324 | 473.324 | 473.324 | 473.324–473.324 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 485.246 | 485.246 | 485.246 | 485.246–485.246 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 623.157 | 623.157 | 623.157 | 623.157–623.157 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 331.527 | 330.079 | 356.903 | 329.718–363.247 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 413.313 | 407.986 | 437.915 | 406.654–444.065 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 422.848 | 417.560 | 448.319 | 416.238–454.687 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 434.524 | 429.109 | 460.275 | 427.755–466.713 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 326.480 | 326.480 | 326.480 | 326.480–326.480 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1761.487 | 1761.487 | 1761.487 | 1761.487–1761.487 |
| R2_simpleui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 19465.751 | 19465.751 | 19465.751 | 19465.751–19465.751 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 20361.152 | 20361.152 | 20361.152 | 20361.152–20361.152 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 558.554 | 558.554 | 558.554 | 558.554–558.554 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 635.697 | 635.697 | 635.697 | 635.697–635.697 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 648.084 | 648.084 | 648.084 | 648.084–648.084 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 786.170 | 786.170 | 786.170 | 786.170–786.170 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 384.349 | 373.158 | 393.564 | 370.360–395.868 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 454.162 | 450.874 | 478.210 | 450.052–484.223 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 463.893 | 460.428 | 488.127 | 459.562–494.185 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 475.279 | 472.079 | 499.925 | 471.279–506.086 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 357.359 | 357.359 | 357.359 | 357.359–357.359 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1804.763 | 1804.763 | 1804.763 | 1804.763–1804.763 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 33203.420 | 33203.420 | 33203.420 | 33203.420–33203.420 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 49267.185 | 49267.185 | 49267.185 | 49267.185–49267.185 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 533.070 | 533.070 | 533.070 | 533.070–533.070 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 615.497 | 615.497 | 615.497 | 615.497–615.497 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 628.264 | 628.264 | 628.264 | 628.264–628.264 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 775.727 | 775.727 | 775.727 | 775.727–775.727 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 340.303 | 339.856 | 364.244 | 339.744–370.230 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 409.491 | 408.633 | 445.962 | 408.419–455.080 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 418.715 | 417.952 | 456.748 | 417.762–466.256 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 430.164 | 429.286 | 468.847 | 429.067–478.518 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 347.113 | 347.113 | 347.113 | 347.113–347.113 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1723.917 | 1723.917 | 1723.917 | 1723.917–1723.917 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 21043.821 | 21043.821 | 21043.821 | 21043.821–21043.821 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 23085.931 | 23085.931 | 23085.931 | 23085.931–23085.931 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 17332.040 | 17332.040 | 17332.040–17332.040 | 31717.532 | 106224.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18309.524 | 18309.524 | 18309.524–18309.524 | 21981.148 | 108512.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16710.850 | 17041.356 | 16702.619–17123.982 | 27659.351 | 99536.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17755.080 | 18190.127 | 17745.971–18298.889 | 21609.481 | 103088.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16694.494 | 16694.494 | 16694.494–16694.494 | 26264.200 | 97936.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17901.791 | 17901.791 | 17901.791–17901.791 | 28717.157 | 119376.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 87967.673 | 87967.673 | 87967.673–87967.673 | 89505.096 | 407136.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15542.203 | 15542.203 | 15542.203–15542.203 | 28336.617 | 103024.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16338.465 | 16338.465 | 16338.465–16338.465 | 20120.449 | 105392.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 15495.355 | 15519.599 | 15490.348–15525.660 | 21517.033 | 97408.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16393.340 | 16402.065 | 15651.062–16404.246 | 20456.947 | 100976.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15570.559 | 15570.559 | 15570.559–15570.559 | 21660.394 | 97152.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15834.793 | 15834.793 | 15834.793–15834.793 | 20030.543 | 110752.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 67621.469 | 67621.469 | 67621.469–67621.469 | 70204.334 | 321792.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16624.945 | 16624.945 | 16624.945–16624.945 | 17737.297 | 105584.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17325.902 | 17325.902 | 17325.902–17325.902 | 21237.061 | 107968.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16001.122 | 16004.560 | 15926.763–16005.419 | 22853.044 | 101648.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16800.649 | 16846.565 | 16119.130–16858.044 | 20924.102 | 104336.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15928.821 | 15928.821 | 15928.821–15928.821 | 25028.664 | 97536.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16234.743 | 16234.743 | 16234.743–16234.743 | 20408.154 | 108016.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 75915.367 | 75915.367 | 75915.367–75915.367 | 76768.423 | 391712.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16758.974 | 16758.974 | 16758.974–16758.974 | 29135.452 | 106016.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17764.833 | 17764.833 | 17764.833–17764.833 | 21329.271 | 108432.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16221.931 | 16575.528 | 16165.185–16663.927 | 27012.071 | 98816.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17323.610 | 17784.382 | 17229.071–17899.575 | 21047.106 | 102304.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16162.681 | 16162.681 | 16162.681–16162.681 | 24821.378 | 97648.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17354.739 | 17354.739 | 17354.739–17354.739 | 28304.049 | 116160.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 79803.708 | 79803.708 | 79803.708–79803.708 | 83078.522 | 338752.000 |

## Data-derived comparisons

- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 13.390 ms vs 13.481 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.316 ms vs 15.582 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 12.819 ms vs 13.481 ms (4.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.316 ms vs 16.061 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 12.565 ms vs 12.819 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.061 ms vs 16.076 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
