# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `c792a7f6cfd87cad3e4f4f44f45eae9070b409392d420b44dc24bb4639bd823d`
Reader flash setting: `unset`

Aggregated rows: 199; PASS=196; FAILED=0; UNSUPPORTED=3; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.093 | 28.772 | 7.346 | 33.527 | 14.271 | 28.579 | 9.116 | 29.647 |
| R11_project_title_vos | warm | real_2692 | 2692 | 7 | 73.000 | 1/1 | 30/30 | 15.139 | 25.046 | 12.726 | 27.651 | 18.619 | 28.043 | 8.987 | 28.817 |
| R5_vos | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.448 | 24.174 | 13.310 | 27.184 | 14.662 | 26.920 | 9.052 | 27.601 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.128 | 25.120 | 13.304 | 26.495 | 15.090 | 25.532 | 8.801 | 27.482 |
| R9_simpleui_vos | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.125 | 27.668 | 7.317 | 30.591 | 14.651 | 29.046 | 9.790 | 31.996 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 148.310 | 169.029 | 129.436 | 218.605 | 134.200 | 148.004 | 115.317 | 231.290 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 16.170 | 19.458 | 10.976 | 97.457 | 18.727 | 23.886 | 7.956 | 119.180 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 148.526 | 150.797 | 128.725 | 187.132 | 148.520 | 164.303 | 131.569 | 197.884 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 41.767 | 56.877 | 30.364 | 79.816 | 37.428 | 55.089 | 26.821 | 78.548 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R11_project_title_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R5_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R8_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 14.662 ms vs 15.090 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.448 ms vs 16.128 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 14.271 ms vs 14.651 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.093 ms vs 16.125 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 13.066 | 13.066 | 13.066 | 13.066–13.066 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 48.237 | 48.237 | 48.237 | 48.237–48.237 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 15.119 | 14.155 | 18.471 | 13.914–19.309 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 46.795 | 45.846 | 48.442 | 45.609–48.854 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 134.200 | 132.378 | 148.004 | 115.317–231.290 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 18.727 | 9.124 | 23.886 | 7.956–119.180 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 24.742 | 22.788 | 97.996 | 21.401–116.851 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 148.310 | 132.065 | 169.029 | 129.436–218.605 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.170 | 14.113 | 19.458 | 10.976–97.457 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 156.924 | 128.426 | 174.982 | 124.597–177.588 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 252.127 | 109.770 | 263.725 | 73.041–270.354 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 38.588 | 35.016 | 41.469 | 34.332–43.079 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.638 | 16.095 | 17.371 | 14.389–23.577 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.663 | 13.376 | 30.694 | 11.854–30.815 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.271 | 10.154 | 28.579 | 9.116–29.647 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 52.313 | 44.447 | 60.753 | 44.313–65.809 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 170.392 | 143.412 | 182.743 | 141.906–184.596 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 27.564 | 18.413 | 42.175 | 17.950–44.379 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.093 | 8.478 | 28.772 | 7.346–33.527 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 108.600 | 88.931 | 122.930 | 84.984–137.028 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 130.574 | 80.802 | 142.147 | 65.965–172.256 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 46.486 | 43.219 | 49.162 | 43.096–49.184 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 17.257 | 16.920 | 46.210 | 16.915–285.821 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1400.699 | 1400.699 | 1400.699 | 1400.699–1400.699 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.660 | 13.895 | 16.683 | 6.131–16.695 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 45.154 | 45.154 | 45.154 | 45.154–45.154 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 42.805 | 42.805 | 42.805 | 42.805–42.805 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 45.933 | 44.187 | 46.250 | 43.750–46.329 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 46.724 | 45.144 | 51.887 | 44.749–53.178 |
| R11_project_title_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 62.837 | 48.778 | 68.153 | 47.837–84.592 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 56.662 | 51.088 | 66.729 | 50.441–67.159 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.661 | 16.610 | 16.670 | 16.314–16.679 |
| R11_project_title_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 46.032 | 44.465 | 52.239 | 43.377–53.958 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 18.619 | 11.491 | 28.043 | 8.987–28.817 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 45.882 | 44.548 | 54.453 | 44.207–55.978 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 78.878 | 70.046 | 90.547 | 68.474–91.005 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 25.177 | 21.712 | 51.730 | 15.606–119.075 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.139 | 13.198 | 25.046 | 12.726–27.651 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 50.037 | 45.121 | 61.372 | 41.188–72.411 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 104.553 | 55.773 | 122.021 | 54.604–177.735 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.663 | 16.649 | 16.670 | 16.612–16.672 |
| R11_project_title_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 839.517 | 839.517 | 839.517 | 839.517–839.517 |
| R5_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 46.306 | 46.306 | 46.306 | 46.306–46.306 |
| R5_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 44.320 | 44.320 | 44.320 | 44.320–44.320 |
| R5_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 35.999 | 34.265 | 38.529 | 33.832–39.162 |
| R5_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 33.135 | 32.540 | 33.671 | 32.391–33.805 |
| R5_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 56.227 | 48.503 | 70.833 | 43.990–71.232 |
| R5_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 45.805 | 39.011 | 56.602 | 37.222–62.237 |
| R5_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.671 | 16.645 | 16.686 | 16.640–16.704 |
| R5_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 34.621 | 32.671 | 47.360 | 32.211–49.460 |
| R5_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.662 | 11.344 | 26.920 | 9.052–27.601 |
| R5_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 34.477 | 33.271 | 46.541 | 32.894–49.469 |
| R5_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 52.200 | 43.108 | 64.893 | 42.284–66.723 |
| R5_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 23.895 | 21.648 | 38.418 | 17.882–41.219 |
| R5_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.448 | 14.439 | 24.174 | 13.310–27.184 |
| R5_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 63.174 | 44.967 | 69.850 | 34.880–74.538 |
| R5_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 112.498 | 61.085 | 130.187 | 52.998–173.326 |
| R5_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.651 | 16.639 | 16.666 | 16.637–16.680 |
| R5_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 688.140 | 688.140 | 688.140 | 688.140–688.140 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 47.474 | 47.474 | 47.474 | 47.474–47.474 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 49.136 | 49.136 | 49.136 | 49.136–49.136 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 32.941 | 32.761 | 40.505 | 32.716–42.396 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 33.732 | 33.411 | 42.143 | 33.331–44.246 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 148.520 | 132.031 | 164.303 | 131.569–197.884 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 37.428 | 30.300 | 55.089 | 26.821–78.548 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 26.087 | 22.245 | 74.113 | 21.246–94.989 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 148.526 | 132.280 | 150.797 | 128.725–187.132 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 41.767 | 36.014 | 56.877 | 30.364–79.816 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 69.899 | 45.508 | 86.982 | 41.663–113.612 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 40.576 | 34.872 | 119.870 | 34.769–129.982 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 12.451 | 7.812 | 14.070 | 6.503–15.239 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.659 | 16.651 | 16.666 | 16.640–16.676 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 36.701 | 33.173 | 45.297 | 32.836–45.959 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.090 | 11.136 | 25.532 | 8.801–27.482 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 34.505 | 32.770 | 48.913 | 32.185–49.531 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 53.847 | 41.771 | 64.846 | 41.080–66.409 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 24.250 | 18.080 | 28.256 | 15.995–37.493 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.128 | 14.573 | 25.120 | 13.304–26.495 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 119.380 | 106.534 | 134.024 | 104.349–136.180 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 127.280 | 105.379 | 151.782 | 82.822–195.779 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 25.424 | 24.088 | 27.007 | 23.618–28.677 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.659 | 16.637 | 16.677 | 16.615–16.683 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 850.790 | 850.790 | 850.790 | 850.790–850.790 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 13.070 | 13.070 | 13.070 | 13.070–13.070 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 48.001 | 48.001 | 48.001 | 48.001–48.001 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 15.366 | 15.116 | 16.563 | 15.054–16.862 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 48.362 | 45.659 | 55.408 | 44.983–57.169 |
| R9_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 158.002 | 128.554 | 171.427 | 124.804–177.842 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 247.406 | 108.183 | 259.025 | 72.278–260.710 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.657 | 16.626 | 16.695 | 16.622–16.696 |
| R9_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.662 | 13.357 | 30.148 | 12.762–30.374 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.651 | 10.488 | 29.046 | 9.790–31.996 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 51.176 | 43.008 | 60.697 | 42.209–66.164 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 169.967 | 140.906 | 181.490 | 139.199–183.306 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 28.377 | 18.969 | 47.474 | 18.115–57.360 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.125 | 8.176 | 27.668 | 7.317–30.591 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 111.058 | 97.308 | 133.407 | 94.282–138.767 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 123.583 | 81.988 | 145.129 | 55.366–171.254 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 17.683 | 16.810 | 146.120 | 15.863–152.256 |
| R9_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1177.733 | 1177.733 | 1177.733 | 1177.733–1177.733 |
| R9_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.651 | 13.861 | 16.694 | 6.826–16.701 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 540.254 | 540.254 | 540.254 | 540.254–540.254 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 617.007 | 617.007 | 617.007 | 617.007–617.007 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 628.199 | 628.199 | 628.199 | 628.199–628.199 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 785.059 | 785.059 | 785.059 | 785.059–785.059 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 353.207 | 351.074 | 371.843 | 350.540–376.501 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 426.301 | 425.668 | 451.297 | 425.510–457.547 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 436.248 | 435.235 | 461.513 | 434.982–467.829 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 448.172 | 447.967 | 473.824 | 447.916–480.237 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 351.925 | 351.925 | 351.925 | 351.925–351.925 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1779.076 | 1779.076 | 1779.076 | 1779.076–1779.076 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 36405.500 | 36405.500 | 36405.500 | 36405.500–36405.500 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 37297.585 | 37297.585 | 37297.585 | 37297.585–37297.585 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 245.712 | 245.712 | 245.712 | 245.712–245.712 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 339.813 | 339.813 | 339.813 | 339.813–339.813 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 346.676 | 346.676 | 346.676 | 346.676–346.676 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 355.949 | 355.949 | 355.949 | 355.949–355.949 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 228.422 | 227.526 | 235.583 | 227.302–237.373 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 333.114 | 325.307 | 333.384 | 323.355–333.452 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 340.261 | 332.520 | 340.721 | 330.585–340.836 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 349.275 | 342.194 | 350.100 | 340.423–350.306 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 230.820 | 230.820 | 230.820 | 230.820–230.820 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2005.789 | 2005.789 | 2005.789 | 2005.789–2005.789 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13236.109 | 13236.109 | 13236.109 | 13236.109–13236.109 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13253.958 | 13253.958 | 13253.958 | 13253.958–13253.958 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 257.832 | 257.832 | 257.832 | 257.832–257.832 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 356.340 | 356.340 | 356.340 | 356.340–356.340 |
| R5_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 365.756 | 365.756 | 365.756 | 365.756–365.756 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 394.858 | 394.858 | 394.858 | 394.858–394.858 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 215.927 | 213.526 | 234.757 | 212.926–239.465 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 290.868 | 289.962 | 307.347 | 289.735–311.467 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 297.713 | 296.529 | 313.671 | 296.233–317.661 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 307.361 | 305.994 | 323.347 | 305.652–327.344 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 215.602 | 215.602 | 215.602 | 215.602–215.602 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1607.509 | 1607.509 | 1607.509 | 1607.509–1607.509 |
| R5_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11907.892 | 11907.892 | 11907.892 | 11907.892–11907.892 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11933.329 | 11933.329 | 11933.329 | 11933.329–11933.329 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 415.022 | 415.022 | 415.022 | 415.022–415.022 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 519.910 | 519.910 | 519.910 | 519.910–519.910 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 528.890 | 528.890 | 528.890 | 528.890–528.890 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 570.157 | 570.157 | 570.157 | 570.157–570.157 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 222.861 | 219.704 | 237.605 | 218.915–241.291 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 305.677 | 293.733 | 319.778 | 290.747–323.303 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 312.473 | 300.556 | 326.614 | 297.577–330.149 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 321.689 | 310.112 | 335.858 | 307.217–339.400 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 220.152 | 220.152 | 220.152 | 220.152–220.152 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1623.181 | 1623.181 | 1623.181 | 1623.181–1623.181 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 27571.230 | 27571.230 | 27571.230 | 27571.230–27571.230 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 27615.555 | 27615.555 | 27615.555 | 27615.555–27615.555 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 547.867 | 547.867 | 547.867 | 547.867–547.867 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 620.587 | 620.587 | 620.587 | 620.587–620.587 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 633.175 | 633.175 | 633.175 | 633.175–633.175 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 778.788 | 778.788 | 778.788 | 778.788–778.788 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 337.769 | 333.505 | 364.553 | 332.439–371.248 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 408.574 | 406.963 | 450.012 | 406.560–460.371 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 417.796 | 416.471 | 459.433 | 416.139–469.842 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 429.778 | 428.374 | 472.323 | 428.023–482.959 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 330.759 | 330.759 | 330.759 | 330.759–330.759 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1755.319 | 1755.319 | 1755.319 | 1755.319–1755.319 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 23023.613 | 23023.613 | 23023.613 | 23023.613–23023.613 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 25672.515 | 25672.515 | 25672.515 | 25672.515–25672.515 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 17238.506 | 17238.506 | 17238.506–17238.506 | 31010.125 | 104496.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18165.678 | 18165.678 | 18165.678–18165.678 | 22273.697 | 106832.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16648.851 | 17140.866 | 16625.511–17263.870 | 27854.925 | 98336.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17719.085 | 18095.935 | 17646.792–18190.147 | 22089.833 | 102080.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16618.054 | 16618.054 | 16618.054–16618.054 | 28083.890 | 98576.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18402.651 | 18402.651 | 18402.651–18402.651 | 18580.394 | 109088.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 88439.451 | 88439.451 | 88439.451–88439.451 | 90413.836 | 411296.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10402.316 | 10402.316 | 10402.316–10402.316 | 14934.796 | 86752.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10466.262 | 10466.262 | 10466.262–10466.262 | 17881.019 | 90624.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10376.348 | 10400.654 | 10360.902–10406.730 | 12921.914 | 85472.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10491.801 | 10509.401 | 10431.031–10513.801 | 17685.418 | 87328.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10408.441 | 10408.441 | 10408.441–10408.441 | 13065.044 | 85040.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10573.609 | 10573.609 | 10573.609–10573.609 | 11814.366 | 97520.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15713.450 | 15713.450 | 15713.450–15713.450 | 16584.751 | 266304.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10213.000 | 10213.000 | 10213.000–10213.000 | 12243.479 | 88480.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11785.613 | 11785.613 | 11785.613–11785.613 | 17015.378 | 89008.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10292.734 | 10312.344 | 10258.336–10317.246 | 12291.725 | 85280.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10289.434 | 10325.559 | 10202.457–10334.590 | 17025.037 | 87216.000 |
| R5_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10289.453 | 10289.453 | 10289.453–10289.453 | 11830.904 | 85088.000 |
| R5_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10353.668 | 10353.668 | 10353.668–10353.668 | 14327.885 | 99824.000 |
| R5_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 16011.660 | 16011.660 | 16011.660–16011.660 | 18467.543 | 260944.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10862.172 | 10862.172 | 10862.172–10862.172 | 14968.084 | 87232.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 12382.344 | 12382.344 | 12382.344–12382.344 | 17825.910 | 89456.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10695.665 | 10698.662 | 10684.485–10699.411 | 13727.235 | 85360.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10739.196 | 10756.221 | 10728.919–10760.478 | 17546.087 | 86656.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10653.845 | 10653.845 | 10653.845–10653.845 | 13017.642 | 85152.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10729.220 | 10729.220 | 10729.220–10729.220 | 14726.792 | 101184.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 22243.258 | 22243.258 | 22243.258–22243.258 | 23867.488 | 347248.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16651.334 | 16651.334 | 16651.334–16651.334 | 27135.234 | 104368.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17607.170 | 17607.170 | 17607.170–17607.170 | 21528.614 | 106880.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16203.178 | 16207.018 | 16128.662–16207.979 | 25655.416 | 96480.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17210.979 | 17230.650 | 17183.947–17235.568 | 21392.646 | 100160.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16150.377 | 16150.377 | 16150.377–16150.377 | 25276.849 | 95760.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17967.115 | 17967.115 | 17967.115–17967.115 | 18146.639 | 108640.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 80265.682 | 80265.682 | 80265.682–80265.682 | 81943.460 | 321472.000 |

## Data-derived comparisons

- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 14.662 ms vs 15.090 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.448 ms vs 16.128 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 14.271 ms vs 14.651 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.093 ms vs 16.125 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
