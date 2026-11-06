# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 464; PASS=424; FAILED=0; UNSUPPORTED=40; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| C_simpleui | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 16.176 | 33.117 | 8.389 | 37.219 | 13.452 | 35.258 | 10.295 | 43.521 |
| C_simpleui | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 12.986 | 16.540 | 9.953 | 16.812 | 14.070 | 30.713 | 10.029 | 36.540 |
| C_simpleui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 12.172 | 38.217 | 7.925 | 50.354 | 13.941 | 42.018 | 11.016 | 45.417 |
| G_simpleui_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 9.919 | 24.406 | 7.534 | 31.730 | 16.070 | 40.187 | 7.098 | 52.049 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | flat | 2000 | 9 | 222.000 | 1/1 | 30/30 | 16.073 | 49.249 | 4.900 | 66.310 | 15.913 | 44.044 | 6.653 | 45.838 |
| J_simpleui_vos | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 13.717 | 28.238 | 12.454 | 33.170 | 13.360 | 29.327 | 10.881 | 29.867 |
| J_simpleui_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | 9 | 222.000 | 1/1 | 30/30 | 16.139 | 49.483 | 7.392 | 66.028 | 14.133 | 42.269 | 10.835 | 45.856 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 16.068 | 16.461 | 13.638 | 16.666 | 13.845 | 28.189 | 10.234 | 29.619 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| G_simpleui_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 132.689 | 167.018 | 129.234 | 265.162 | 132.775 | 134.346 | 115.450 | 231.910 |
| G_simpleui_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 16.143 | 17.429 | 8.495 | 125.604 | 16.148 | 16.351 | 4.300 | 110.334 |
| G_simpleui_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 148.625 | 149.887 | 132.207 | 149.888 | 132.017 | 133.981 | 112.408 | 190.692 |
| G_simpleui_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 15.724 | 22.811 | 12.042 | 27.025 | 16.169 | 16.419 | 10.651 | 58.744 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 148.895 | 181.475 | 131.585 | 262.113 | 131.881 | 135.481 | 116.441 | 269.155 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 24.200 | 27.662 | 11.285 | 150.190 | 16.142 | 16.277 | 8.679 | 126.293 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 141.843 | 156.720 | 132.058 | 158.378 | 132.694 | 145.594 | 112.913 | 202.498 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 13.268 | 16.464 | 12.647 | 17.090 | 16.153 | 16.463 | 9.971 | 60.093 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| C_simpleui | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| J_simpleui_vos | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| J_simpleui_vos | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| J_simpleui_vos | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| J_simpleui_vos | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| J_simpleui_vos | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| J_simpleui_vos | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |

## Comparative Findings

- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.452 ms vs 13.941 ms (3.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 12.172 ms vs 16.176 ms (24.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 14.070 ms vs 16.070 ms (12.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 9.919 ms vs 12.986 ms (23.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 13.452 ms vs 15.913 ms (15.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 16.073 ms vs 16.176 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 13.360 ms vs 14.070 ms (5.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 12.986 ms vs 13.717 ms (5.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 14.133 ms vs 15.913 ms (11.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 16.073 ms vs 16.139 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 13.360 ms vs 13.845 ms (3.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 13.717 ms vs 16.068 ms (14.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| C_simpleui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.487 | 8.419 | 8.765 | 8.402–8.835 |
| C_simpleui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 28.291 | 23.611 | 29.611 | 22.441–29.941 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.038 | 7.549 | 8.084 | 7.427–8.096 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 21.879 | 21.604 | 22.590 | 21.535–22.768 |
| C_simpleui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 71.297 | 65.937 | 96.156 | 61.646–98.248 |
| C_simpleui | warm | flat | 2000 | close_book | PASS | 10 | 93.901 | 85.418 | 229.536 | 84.805–249.140 |
| C_simpleui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.654 | 16.626 | 16.692 | 16.592–16.697 |
| C_simpleui | warm | flat | 2000 | home_to_library | PASS | 10 | 16.649 | 12.616 | 30.446 | 12.001–30.802 |
| C_simpleui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.452 | 11.656 | 35.258 | 10.295–43.521 |
| C_simpleui | warm | flat | 2000 | library_first_render | PASS | 10 | 59.250 | 55.369 | 82.584 | 54.661–82.920 |
| C_simpleui | warm | flat | 2000 | library_folder_back | PASS | 10 | 41.186 | 38.273 | 63.698 | 36.903–70.027 |
| C_simpleui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 7.048 | 5.743 | 10.908 | 5.617–29.286 |
| C_simpleui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.176 | 10.698 | 33.117 | 8.389–37.219 |
| C_simpleui | warm | flat | 2000 | open_book | PASS | 10 | 152.197 | 128.330 | 190.480 | 114.903–191.849 |
| C_simpleui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 95.212 | 67.818 | 111.912 | 51.309–120.071 |
| C_simpleui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.632 | 16.585 | 16.710 | 16.572–16.728 |
| C_simpleui | warm | flat | 2000 | repeated_nav | PASS | 2 | 512.805 | 227.139 | 798.471 | 155.723–869.887 |
| C_simpleui | warm | flat | 2000 | start_to_home | PASS | 10 | 16.657 | 15.535 | 16.676 | 6.572–16.708 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 10 | 15.816 | 14.667 | 27.559 | 14.424–29.404 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 10 | 72.362 | 47.942 | 144.333 | 40.036–167.056 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.638 | 16.558 | 16.671 | 16.397–16.675 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 10 | 16.660 | 14.175 | 28.663 | 13.224–28.745 |
| C_simpleui | warm | flat | 50 | library_cached_paging | PASS | 30 | 14.070 | 10.781 | 30.713 | 10.029–36.540 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 10 | 31.848 | 27.975 | 44.040 | 26.004–46.974 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 10 | 16.388 | 13.350 | 18.092 | 11.757–30.656 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.694 | 7.100 | 29.840 | 5.987–37.655 |
| C_simpleui | warm | flat | 50 | library_sequential_paging | PASS | 5 | 12.986 | 10.266 | 16.540 | 9.953–16.812 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 10 | 106.120 | 87.790 | 117.195 | 69.130–124.953 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 10 | 51.127 | 38.044 | 91.719 | 31.529–95.149 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.669 | 16.631 | 16.706 | 16.616–16.713 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 2 | 347.332 | 330.388 | 364.275 | 326.152–368.511 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 10 | 16.657 | 11.655 | 16.855 | 7.247–18.255 |
| C_simpleui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 26.562 | 21.347 | 41.758 | 20.033–45.291 |
| C_simpleui | warm | hierarchical | 2000 | close_book | PASS | 10 | 49.364 | 47.052 | 50.779 | 46.322–52.736 |
| C_simpleui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.657 | 16.635 | 16.710 | 16.614–16.780 |
| C_simpleui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.616 | 8.293 | 29.176 | 8.262–33.645 |
| C_simpleui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.754 | 21.426 | 44.214 | 20.903–44.748 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.183 | 14.318 | 28.745 | 14.090–29.012 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.725 | 13.589 | 30.152 | 12.137–30.839 |
| C_simpleui | warm | hierarchical | 2000 | open_book | PASS | 10 | 95.921 | 53.952 | 108.590 | 53.702–110.037 |
| C_simpleui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 44.824 | 40.238 | 57.763 | 37.911–61.609 |
| C_simpleui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.661 | 16.635 | 16.671 | 16.620–16.739 |
| C_simpleui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.652 | 14.426 | 16.697 | 8.532–16.708 |
| C_simpleui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.133 | 9.544 | 26.354 | 9.484–26.822 |
| C_simpleui | warm | hierarchical | 50 | close_book | PASS | 10 | 36.629 | 33.411 | 43.000 | 32.471–82.619 |
| C_simpleui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.663 | 16.624 | 16.688 | 16.619–16.695 |
| C_simpleui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.659 | 14.217 | 27.725 | 13.724–28.258 |
| C_simpleui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.817 | 22.206 | 43.327 | 21.005–44.501 |
| C_simpleui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.617 | 8.326 | 26.192 | 8.189–26.655 |
| C_simpleui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.939 | 11.689 | 26.662 | 11.262–26.781 |
| C_simpleui | warm | hierarchical | 50 | open_book | PASS | 10 | 50.132 | 46.663 | 74.021 | 45.716–89.777 |
| C_simpleui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 44.914 | 35.794 | 60.828 | 33.855–63.059 |
| C_simpleui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.641 | 16.610 | 16.680 | 16.589–16.706 |
| C_simpleui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.685 | 15.722 | 16.736 | 7.548–16.742 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.188 | 7.783 | 8.670 | 7.682–8.791 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 20.937 | 20.309 | 21.543 | 20.152–21.695 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.775 | 132.348 | 134.346 | 115.450–231.910 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.148 | 14.360 | 16.351 | 4.300–110.334 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 15.760 | 7.597 | 112.126 | 6.388–133.525 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 132.689 | 132.079 | 167.018 | 129.234–265.162 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.143 | 14.860 | 17.429 | 8.495–125.604 |
| G_simpleui_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 71.492 | 63.789 | 98.039 | 63.247–99.686 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 153.142 | 81.641 | 254.404 | 81.600–259.592 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 33.117 | 32.740 | 33.224 | 31.695–33.256 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.663 | 16.616 | 16.729 | 16.607–16.762 |
| G_simpleui_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.642 | 13.503 | 31.081 | 12.395–31.117 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.941 | 12.066 | 42.018 | 11.016–45.417 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 70.553 | 60.821 | 103.375 | 58.644–105.362 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 40.040 | 38.016 | 61.200 | 37.030–61.309 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.768 | 6.076 | 17.877 | 5.195–30.962 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 12.172 | 8.579 | 38.217 | 7.925–50.354 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 135.095 | 106.770 | 168.636 | 100.823–191.627 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 89.892 | 82.374 | 126.320 | 75.100–126.943 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.879 | 16.808 | 17.207 | 16.764–19.903 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.662 | 16.610 | 16.672 | 16.589–16.677 |
| G_simpleui_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 725.056 | 691.726 | 758.386 | 683.394–766.718 |
| G_simpleui_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.660 | 14.085 | 16.669 | 7.313–16.670 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.017 | 130.159 | 133.981 | 112.408–190.692 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.169 | 15.991 | 16.419 | 10.651–58.744 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 21.325 | 16.052 | 65.894 | 15.132–73.473 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 148.625 | 132.930 | 149.887 | 132.207–149.888 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 15.724 | 13.369 | 22.811 | 12.042–27.025 |
| G_simpleui_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 17.206 | 16.136 | 29.552 | 16.114–38.949 |
| G_simpleui_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 56.267 | 46.999 | 149.329 | 38.873–150.325 |
| G_simpleui_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 33.170 | 33.064 | 33.215 | 32.990–33.222 |
| G_simpleui_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.662 | 16.636 | 16.680 | 16.631–16.694 |
| G_simpleui_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.703 | 13.350 | 35.606 | 12.935–36.136 |
| G_simpleui_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.070 | 10.697 | 40.187 | 7.098–52.049 |
| G_simpleui_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 42.100 | 34.938 | 57.741 | 34.815–61.112 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 16.053 | 11.073 | 17.862 | 10.495–28.145 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.337 | 5.830 | 31.585 | 5.266–33.459 |
| G_simpleui_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 9.919 | 8.226 | 24.406 | 7.534–31.730 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 105.215 | 93.110 | 112.145 | 57.534–114.309 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 45.248 | 40.215 | 87.618 | 36.152–90.053 |
| G_simpleui_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 17.082 | 16.742 | 33.521 | 16.611–33.579 |
| G_simpleui_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.660 | 16.644 | 16.681 | 16.611–16.682 |
| G_simpleui_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 425.042 | 405.056 | 445.028 | 400.059–450.024 |
| G_simpleui_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.645 | 15.367 | 16.679 | 5.609–16.711 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.294 | 13.258 | 56.820 | 12.745–65.907 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 25.145 | 20.245 | 41.775 | 19.766–46.993 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 51.704 | 48.449 | 73.733 | 48.401–154.224 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 31.689 | 25.947 | 32.890 | 20.900–35.780 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.657 | 16.404 | 16.684 | 14.872–16.688 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.667 | 14.027 | 28.358 | 12.458–28.628 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.797 | 31.543 | 34.002 | 21.990–43.570 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.531 | 13.467 | 28.091 | 13.229–28.488 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 14.380 | 11.256 | 28.906 | 5.900–30.209 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 102.567 | 91.162 | 112.473 | 57.599–115.899 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 48.991 | 37.451 | 65.777 | 34.797–75.142 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.996 | 16.780 | 19.275 | 16.656–19.451 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.663 | 16.598 | 16.684 | 16.419–16.688 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.658 | 15.657 | 16.685 | 7.107–16.707 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 15.623 | 13.172 | 54.343 | 12.757–56.343 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.135 | 11.085 | 27.374 | 9.226–29.484 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 36.038 | 33.407 | 39.545 | 32.798–41.460 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 32.704 | 31.374 | 33.117 | 30.823–33.509 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.672 | 16.657 | 17.194 | 16.647–21.324 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.652 | 13.657 | 28.078 | 13.045–29.398 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.773 | 31.564 | 34.045 | 21.909–43.651 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.603 | 7.923 | 27.359 | 7.360–27.940 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.134 | 11.337 | 27.239 | 11.030–27.443 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 69.004 | 61.642 | 99.189 | 47.424–105.292 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 46.612 | 41.369 | 49.564 | 38.101–49.644 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.779 | 16.633 | 17.191 | 16.549–19.600 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.682 | 16.657 | 16.758 | 16.621–16.770 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.685 | 15.638 | 16.713 | 6.404–16.723 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.604 | 7.284 | 7.958 | 7.204–8.046 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 29.231 | 28.433 | 29.584 | 28.233–29.672 |
| J_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 90.284 | 85.100 | 133.586 | 80.721–133.880 |
| J_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 143.251 | 126.885 | 252.004 | 124.659–267.086 |
| J_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.654 | 16.621 | 16.691 | 16.595–16.781 |
| J_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 16.628 | 12.368 | 32.078 | 11.733–32.228 |
| J_simpleui_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.913 | 8.188 | 44.044 | 6.653–45.838 |
| J_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 67.994 | 65.785 | 87.771 | 63.561–101.998 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 52.608 | 47.269 | 83.166 | 46.831–85.900 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 5.716 | 4.982 | 15.377 | 4.681–15.763 |
| J_simpleui_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.073 | 6.808 | 49.249 | 4.900–66.310 |
| J_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 128.802 | 119.273 | 144.021 | 114.499–160.124 |
| J_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 87.124 | 63.625 | 113.459 | 60.622–120.691 |
| J_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.638 | 16.599 | 16.708 | 16.503–16.711 |
| J_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 800.070 | 760.061 | 840.078 | 750.059–850.080 |
| J_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 16.651 | 11.833 | 16.724 | 6.258–16.746 |
| J_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 19.870 | 18.262 | 32.327 | 17.194–33.481 |
| J_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 46.620 | 44.344 | 55.904 | 42.293–59.654 |
| J_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.654 | 16.629 | 16.682 | 16.619–16.703 |
| J_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 16.657 | 13.285 | 30.468 | 12.906–30.540 |
| J_simpleui_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.360 | 11.555 | 29.327 | 10.881–29.867 |
| J_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 32.838 | 32.754 | 43.700 | 32.750–44.849 |
| J_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 16.196 | 13.484 | 33.120 | 13.072–35.388 |
| J_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 12.286 | 5.883 | 29.036 | 5.647–32.628 |
| J_simpleui_vos | warm | flat | 50 | library_sequential_paging | PASS | 5 | 13.717 | 12.612 | 28.238 | 12.454–33.170 |
| J_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 131.397 | 98.535 | 152.532 | 72.393–154.820 |
| J_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 78.353 | 44.521 | 104.996 | 40.657–120.056 |
| J_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.669 | 16.643 | 16.727 | 16.638–16.993 |
| J_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 389.486 | 371.284 | 407.689 | 366.733–412.240 |
| J_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 16.675 | 9.566 | 16.729 | 7.158–16.820 |
| J_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.033 | 14.423 | 27.076 | 13.424–28.440 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 52.120 | 49.015 | 70.693 | 48.784–156.577 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.657 | 16.634 | 16.688 | 16.620–16.695 |
| J_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.687 | 13.986 | 28.288 | 13.782–28.427 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.744 | 32.688 | 32.790 | 32.660–32.875 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.401 | 9.734 | 26.631 | 6.244–27.701 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.802 | 5.179 | 18.378 | 4.716–29.359 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 108.742 | 99.375 | 125.219 | 95.665–134.250 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 57.446 | 47.160 | 91.858 | 40.747–109.747 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.629 | 16.612 | 16.668 | 16.602–16.683 |
| J_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.662 | 15.642 | 16.709 | 6.906–16.711 |
| J_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.117 | 10.238 | 27.092 | 8.435–27.237 |
| J_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 39.010 | 35.542 | 46.300 | 35.171–84.068 |
| J_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.669 | 16.634 | 16.698 | 16.630–16.703 |
| J_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.669 | 13.914 | 28.285 | 13.084–28.680 |
| J_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.772 | 32.602 | 32.838 | 32.554–32.990 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.112 | 6.803 | 17.809 | 6.314–27.714 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.635 | 11.688 | 17.698 | 5.514–26.930 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 104.606 | 63.724 | 129.618 | 54.784–142.222 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 45.514 | 42.100 | 64.070 | 37.523–68.260 |
| J_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.665 | 16.616 | 16.689 | 16.606–16.703 |
| J_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.656 | 15.740 | 16.685 | 7.630–16.686 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.129 | 8.092 | 8.487 | 8.083–8.577 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 19.358 | 18.816 | 20.599 | 18.680–20.909 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 131.881 | 130.617 | 135.481 | 116.441–269.155 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.142 | 15.853 | 16.277 | 8.679–126.293 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 20.334 | 15.738 | 125.084 | 14.776–146.383 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 148.895 | 132.635 | 181.475 | 131.585–262.113 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 24.200 | 16.131 | 27.662 | 11.285–150.190 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 100.860 | 94.364 | 136.933 | 92.842–141.931 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 199.038 | 127.440 | 284.762 | 127.436–294.187 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 33.106 | 28.772 | 34.774 | 23.806–35.835 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.652 | 16.634 | 16.696 | 16.632–16.732 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.659 | 12.679 | 31.481 | 11.221–31.546 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 14.133 | 11.422 | 42.269 | 10.835–45.856 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 66.144 | 61.753 | 78.962 | 61.500–91.728 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 53.719 | 52.444 | 84.473 | 52.346–88.214 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.996 | 5.486 | 14.609 | 4.526–16.593 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.139 | 9.404 | 49.483 | 7.392–66.028 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 138.697 | 127.226 | 151.402 | 110.933–159.028 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 82.450 | 69.247 | 102.694 | 56.513–105.388 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 17.984 | 16.843 | 19.281 | 15.804–20.333 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.657 | 16.628 | 16.695 | 16.602–16.718 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 825.050 | 778.402 | 871.698 | 766.740–883.360 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.675 | 13.399 | 16.690 | 7.003–16.693 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.694 | 129.609 | 145.594 | 112.913–202.498 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.153 | 15.954 | 16.463 | 9.971–60.093 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 14.169 | 12.728 | 53.594 | 12.030–63.886 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 141.843 | 132.426 | 156.720 | 132.058–158.378 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 13.268 | 12.791 | 16.464 | 12.647–17.090 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 17.776 | 16.312 | 28.308 | 16.113–30.826 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 44.474 | 39.352 | 63.933 | 37.973–114.250 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 33.187 | 33.125 | 33.230 | 33.089–33.246 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.672 | 16.654 | 16.694 | 16.613–16.699 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.645 | 13.958 | 31.081 | 11.886–33.504 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.845 | 11.044 | 28.189 | 10.234–29.619 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 32.854 | 27.474 | 38.153 | 27.369–38.251 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 15.476 | 13.376 | 32.317 | 13.196–32.737 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.671 | 5.229 | 28.006 | 4.964–28.168 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 16.068 | 14.039 | 16.461 | 13.638–16.666 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 110.050 | 99.384 | 127.766 | 91.142–132.642 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 45.069 | 39.612 | 85.765 | 38.665–93.355 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.825 | 16.598 | 16.936 | 16.464–16.967 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.662 | 16.621 | 16.678 | 16.572–16.684 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 401.510 | 387.204 | 415.816 | 383.628–419.392 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.654 | 14.666 | 16.674 | 7.027–16.717 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.477 | 14.181 | 59.863 | 13.590–69.955 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 13.787 | 13.296 | 27.185 | 12.879–27.949 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 56.713 | 52.861 | 151.141 | 48.325–154.125 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 32.484 | 30.731 | 33.621 | 30.701–37.637 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.651 | 16.146 | 16.701 | 11.988–16.720 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.654 | 13.280 | 28.784 | 12.565–29.419 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.757 | 32.629 | 32.833 | 32.587–32.912 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.401 | 12.461 | 28.978 | 6.205–29.926 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.654 | 5.816 | 18.248 | 5.127–29.949 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 116.617 | 101.571 | 127.297 | 93.983–133.125 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 65.526 | 40.400 | 89.182 | 37.811–89.946 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 17.434 | 16.788 | 18.161 | 16.459–18.757 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.656 | 16.647 | 16.673 | 16.612–16.681 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.659 | 15.668 | 16.706 | 7.096–16.734 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 13.632 | 11.965 | 52.600 | 11.753–58.250 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.084 | 8.396 | 26.716 | 7.986–27.451 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 39.325 | 36.063 | 44.053 | 34.512–51.259 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 33.050 | 32.918 | 33.255 | 32.862–33.297 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.646 | 16.069 | 16.679 | 12.210–16.693 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.645 | 13.179 | 28.900 | 12.977–29.533 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.751 | 32.715 | 32.824 | 32.705–32.826 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.345 | 6.131 | 17.797 | 6.032–27.859 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.549 | 10.497 | 17.762 | 5.205–27.789 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 101.996 | 62.677 | 115.916 | 60.891–133.507 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 55.111 | 44.547 | 87.334 | 35.131–109.943 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.769 | 16.363 | 16.848 | 15.960–17.066 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.681 | 16.647 | 16.710 | 16.505–16.712 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.670 | 15.655 | 16.683 | 6.953–16.702 |
| C_simpleui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 9.041 | 9.041 | 9.041 | 9.041–9.041 |
| C_simpleui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 29.105 | 29.105 | 29.105 | 29.105–29.105 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 7.530 | 7.530 | 7.530 | 7.530–7.530 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 30.560 | 30.560 | 30.560 | 30.560–30.560 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.662 | 8.662 | 8.662 | 8.662–8.662 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.676 | 32.676 | 32.676 | 32.676–32.676 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 7.120 | 7.120 | 7.120 | 7.120–7.120 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 21.144 | 21.144 | 21.144 | 21.144–21.144 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 295.450 | 291.888 | 300.486 | 290.997–301.745 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 339.155 | 338.293 | 340.200 | 338.078–340.461 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 346.048 | 345.344 | 347.314 | 345.168–347.631 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 356.051 | 355.538 | 357.478 | 355.410–357.835 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 252.877 | 250.116 | 265.884 | 249.425–269.135 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 291.253 | 289.213 | 303.104 | 288.702–306.066 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 298.394 | 296.264 | 310.098 | 295.732–313.023 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 308.530 | 305.997 | 319.979 | 305.364–322.842 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 370.533 | 370.533 | 370.533 | 370.533–370.533 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1948.896 | 1948.896 | 1948.896 | 1948.896–1948.896 |
| C_simpleui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 19964.597 | 19964.597 | 19964.597 | 19964.597–19964.597 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 23137.110 | 23137.110 | 23137.110 | 23137.110–23137.110 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 318.183 | 318.183 | 318.183 | 318.183–318.183 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1539.751 | 1539.751 | 1539.751 | 1539.751–1539.751 |
| C_simpleui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11581.002 | 11581.002 | 11581.002 | 11581.002–11581.002 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11613.754 | 11613.754 | 11613.754 | 11613.754–11613.754 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 350.006 | 350.006 | 350.006 | 350.006–350.006 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1532.084 | 1532.084 | 1532.084 | 1532.084–1532.084 |
| C_simpleui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9324.416 | 9324.416 | 9324.416 | 9324.416–9324.416 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9350.776 | 9350.776 | 9350.776 | 9350.776–9350.776 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 432.311 | 432.311 | 432.311 | 432.311–432.311 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1600.682 | 1600.682 | 1600.682 | 1600.682–1600.682 |
| C_simpleui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8490.868 | 8490.868 | 8490.868 | 8490.868–8490.868 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8516.321 | 8516.321 | 8516.321 | 8516.321–8516.321 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 290.443 | 289.923 | 306.894 | 289.793–311.007 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 328.256 | 325.504 | 346.663 | 324.816–351.264 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 336.651 | 333.032 | 354.896 | 332.128–359.458 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 347.547 | 343.749 | 366.891 | 342.799–371.727 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 372.019 | 372.019 | 372.019 | 372.019–372.019 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2074.075 | 2074.075 | 2074.075 | 2074.075–2074.075 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 31666.468 | 31666.468 | 31666.468 | 31666.468–31666.468 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 45591.485 | 45591.485 | 45591.485 | 45591.485–45591.485 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 325.014 | 325.014 | 325.014 | 325.014–325.014 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1660.672 | 1660.672 | 1660.672 | 1660.672–1660.672 |
| G_simpleui_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 19438.337 | 19438.337 | 19438.337 | 19438.337–19438.337 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 19470.636 | 19470.636 | 19470.636 | 19470.636–19470.636 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 306.296 | 306.296 | 306.296 | 306.296–306.296 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1474.551 | 1474.551 | 1474.551 | 1474.551–1474.551 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11035.487 | 11035.487 | 11035.487 | 11035.487–11035.487 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11110.721 | 11110.721 | 11110.721 | 11110.721–11110.721 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 444.711 | 444.711 | 444.711 | 444.711–444.711 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1618.753 | 1618.753 | 1618.753 | 1618.753–1618.753 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10247.062 | 10247.062 | 10247.062 | 10247.062–10247.062 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10277.324 | 10277.324 | 10277.324 | 10277.324–10277.324 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 260.353 | 259.827 | 273.665 | 259.696–276.993 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 305.563 | 304.868 | 317.998 | 304.694–321.106 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 313.161 | 311.951 | 325.741 | 311.648–328.886 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 324.071 | 322.520 | 336.458 | 322.132–339.555 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 465.440 | 465.440 | 465.440 | 465.440–465.440 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2144.474 | 2144.474 | 2144.474 | 2144.474–2144.474 |
| J_simpleui_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 23031.353 | 23031.353 | 23031.353 | 23031.353–23031.353 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 23667.037 | 23667.037 | 23667.037 | 23667.037–23667.037 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 351.821 | 351.821 | 351.821 | 351.821–351.821 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1643.282 | 1643.282 | 1643.282 | 1643.282–1643.282 |
| J_simpleui_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11857.083 | 11857.083 | 11857.083 | 11857.083–11857.083 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11890.515 | 11890.515 | 11890.515 | 11890.515–11890.515 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 306.913 | 306.913 | 306.913 | 306.913–306.913 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1490.202 | 1490.202 | 1490.202 | 1490.202–1490.202 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9654.251 | 9654.251 | 9654.251 | 9654.251–9654.251 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9682.847 | 9682.847 | 9682.847 | 9682.847–9682.847 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 441.192 | 441.192 | 441.192 | 441.192–441.192 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1616.651 | 1616.651 | 1616.651 | 1616.651–1616.651 |
| J_simpleui_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8890.724 | 8890.724 | 8890.724 | 8890.724–8890.724 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8916.581 | 8916.581 | 8916.581 | 8916.581–8916.581 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 269.952 | 269.574 | 296.906 | 269.479–303.645 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 305.950 | 305.858 | 334.609 | 305.835–341.774 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 313.671 | 313.320 | 342.115 | 313.232–349.226 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 325.245 | 323.990 | 352.800 | 323.676–359.689 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 506.310 | 506.310 | 506.310 | 506.310–506.310 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2149.404 | 2149.404 | 2149.404 | 2149.404–2149.404 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 36156.876 | 36156.876 | 36156.876 | 36156.876–36156.876 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 78854.844 | 78854.844 | 78854.844 | 78854.844–78854.844 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 328.018 | 328.018 | 328.018 | 328.018–328.018 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1509.181 | 1509.181 | 1509.181 | 1509.181–1509.181 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18475.279 | 18475.279 | 18475.279 | 18475.279–18475.279 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18508.257 | 18508.257 | 18508.257 | 18508.257–18508.257 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 319.327 | 319.327 | 319.327 | 319.327–319.327 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1490.702 | 1490.702 | 1490.702 | 1490.702–1490.702 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11319.921 | 11319.921 | 11319.921 | 11319.921–11319.921 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11525.471 | 11525.471 | 11525.471 | 11525.471–11525.471 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 450.601 | 450.601 | 450.601 | 450.601–450.601 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1634.202 | 1634.202 | 1634.202 | 1634.202–1634.202 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10500.446 | 10500.446 | 10500.446 | 10500.446–10500.446 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10605.865 | 10605.865 | 10605.865 | 10605.865–10605.865 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 293.918 | 293.918 | 293.918 | 293.918–293.918 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 338.599 | 338.599 | 338.599 | 338.599–338.599 |
| C_simpleui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 345.592 | 345.592 | 345.592 | 345.592–345.592 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 355.558 | 355.558 | 355.558 | 355.558–355.558 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 473.216 | 473.216 | 473.216 | 473.216–473.216 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 518.771 | 518.771 | 518.771 | 518.771–518.771 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 525.950 | 525.950 | 525.950 | 525.950–525.950 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 536.234 | 536.234 | 536.234 | 536.234–536.234 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 310.490 | 310.490 | 310.490 | 310.490–310.490 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 358.926 | 358.926 | 358.926 | 358.926–358.926 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 366.149 | 366.149 | 366.149 | 366.149–366.149 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 376.398 | 376.398 | 376.398 | 376.398–376.398 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 321.644 | 321.644 | 321.644 | 321.644–321.644 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 357.984 | 357.984 | 357.984 | 357.984–357.984 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 365.369 | 365.369 | 365.369 | 365.369–365.369 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 375.696 | 375.696 | 375.696 | 375.696–375.696 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| C_simpleui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14085.621 | 14100.212 | 14051.441–14103.859 | 22460.891 | 95856.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14329.738 | 14334.723 | 14281.586–14335.969 | 15535.216 | 96112.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14063.656 | 14066.981 | 14049.402–14067.812 | 21378.985 | 90960.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14109.098 | 14135.116 | 14099.289–14141.621 | 15396.561 | 91360.000 |
| C_simpleui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16510.508 | 16510.508 | 16510.508–16510.508 | 25148.613 | 98192.000 |
| C_simpleui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 25975.090 | 25975.090 | 25975.090–25975.090 | 34382.117 | 123632.000 |
| C_simpleui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 106273.133 | 106273.133 | 106273.133–106273.133 | 110152.944 | 246048.000 |
| C_simpleui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14387.387 | 14387.387 | 14387.387–14387.387 | 17143.120 | 95168.000 |
| C_simpleui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 18761.117 | 18761.117 | 18761.117–18761.117 | 23593.300 | 110432.000 |
| C_simpleui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 55381.598 | 55381.598 | 55381.598–55381.598 | 59660.075 | 198032.000 |
| C_simpleui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14098.340 | 14098.340 | 14098.340–14098.340 | 22517.349 | 95520.000 |
| C_simpleui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14256.582 | 14256.582 | 14256.582–14256.582 | 15510.488 | 96048.000 |
| C_simpleui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 51619.457 | 51619.457 | 51619.457–51619.457 | 62235.862 | 177312.000 |
| C_simpleui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14120.301 | 14120.301 | 14120.301–14120.301 | 21964.071 | 98944.000 |
| C_simpleui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14169.098 | 14169.098 | 14169.098–14169.098 | 15576.103 | 100160.000 |
| C_simpleui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 50527.133 | 50527.133 | 50527.133–50527.133 | 61609.866 | 178608.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14464.665 | 14472.084 | 14404.700–14473.938 | 21589.527 | 92656.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14581.747 | 14609.088 | 14558.341–14615.923 | 15859.546 | 93104.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17095.828 | 17095.828 | 17095.828–17095.828 | 28033.189 | 101232.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 26514.551 | 26514.551 | 26514.551–26514.551 | 40514.262 | 125424.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 111483.255 | 111483.255 | 111483.255–111483.255 | 113120.494 | 283120.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15069.648 | 15069.648 | 15069.648–15069.648 | 19826.066 | 95520.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 18774.453 | 18774.453 | 18774.453–18774.453 | 19997.479 | 108592.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 59370.930 | 59370.930 | 59370.930–59370.930 | 63052.683 | 233360.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14751.863 | 14751.863 | 14751.863–14751.863 | 17804.548 | 95648.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14678.828 | 14678.828 | 14678.828–14678.828 | 15952.093 | 95728.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 58417.780 | 58417.780 | 58417.780–58417.780 | 86272.516 | 210592.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14763.457 | 14763.457 | 14763.457–14763.457 | 17336.870 | 96112.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14699.844 | 14699.844 | 14699.844–14699.844 | 16032.510 | 98016.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 54404.390 | 54404.390 | 54404.390–54404.390 | 76083.292 | 202928.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14526.786 | 14541.180 | 14489.103–14544.778 | 22503.425 | 91824.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14735.493 | 14788.140 | 14673.876–14801.302 | 15670.447 | 92208.000 |
| J_simpleui_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17447.513 | 17447.513 | 17447.513–17447.513 | 26027.812 | 99040.000 |
| J_simpleui_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 30960.692 | 30960.692 | 30960.692–30960.692 | 55978.943 | 143488.000 |
| J_simpleui_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 124739.118 | 124739.118 | 124739.118–124739.118 | 126977.343 | 280144.000 |
| J_simpleui_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14842.177 | 14842.177 | 14842.177–14842.177 | 16077.753 | 96448.000 |
| J_simpleui_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 15661.364 | 15661.364 | 15661.364–15661.364 | 17442.825 | 108800.000 |
| J_simpleui_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 58525.243 | 58525.243 | 58525.243–58525.243 | 61732.481 | 202272.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14537.806 | 14537.806 | 14537.806–14537.806 | 16858.849 | 95664.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14892.091 | 14892.091 | 14892.091–14892.091 | 15745.598 | 96096.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 58291.024 | 58291.024 | 58291.024–58291.024 | 74309.355 | 189936.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14616.278 | 14616.278 | 14616.278–14616.278 | 15649.102 | 96560.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14797.540 | 14797.540 | 14797.540–14797.540 | 15702.201 | 97136.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 52963.864 | 52963.864 | 52963.864–52963.864 | 67589.142 | 182208.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14990.037 | 15000.931 | 14973.002–15003.654 | 23385.457 | 92880.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15150.943 | 15213.443 | 15121.365–15229.068 | 16132.918 | 93088.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 18066.349 | 18066.349 | 18066.349–18066.349 | 28778.919 | 101824.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 31152.396 | 31152.396 | 31152.396–31152.396 | 56655.920 | 142304.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 130655.596 | 130655.596 | 130655.596–130655.596 | 132897.158 | 311792.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15512.841 | 15512.841 | 15512.841–15512.841 | 18829.066 | 94832.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16132.376 | 16132.376 | 16132.376–16132.376 | 17663.546 | 108496.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 62487.083 | 62487.083 | 62487.083–62487.083 | 64983.355 | 240112.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15313.927 | 15313.927 | 15313.927–15313.927 | 18964.739 | 96000.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15439.380 | 15439.380 | 15439.380–15439.380 | 16447.715 | 96416.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 65053.156 | 65053.156 | 65053.156–65053.156 | 94920.579 | 225600.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 15319.646 | 15319.646 | 15319.646–15319.646 | 18418.146 | 95776.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15395.681 | 15395.681 | 15395.681–15395.681 | 16378.367 | 97632.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 56948.062 | 56948.062 | 56948.062–56948.062 | 83999.153 | 207344.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14106.383 | 14106.383 | 14106.383–14106.383 | 16069.069 | 95712.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14306.676 | 14306.676 | 14306.676–14306.676 | 15610.854 | 96064.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14649.426 | 14649.426 | 14649.426–14649.426 | 17665.389 | 95472.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14808.359 | 14808.359 | 14808.359–14808.359 | 16087.087 | 95584.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14520.759 | 14520.759 | 14520.759–14520.759 | 16727.979 | 96128.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14719.938 | 14719.938 | 14719.938–14719.938 | 15764.973 | 96496.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15210.349 | 15210.349 | 15210.349–15210.349 | 18879.607 | 96352.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15322.712 | 15322.712 | 15322.712–15322.712 | 16460.633 | 96688.000 |

## Data-derived comparisons

- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.452 ms vs 13.941 ms (3.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 12.172 ms vs 16.176 ms (24.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 14.070 ms vs 16.070 ms (12.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 9.919 ms vs 12.986 ms (23.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 13.452 ms vs 15.913 ms (15.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 16.073 ms vs 16.176 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 13.360 ms vs 14.070 ms (5.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 12.986 ms vs 13.717 ms (5.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 14.133 ms vs 15.913 ms (11.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 16.073 ms vs 16.139 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 13.360 ms vs 13.845 ms (3.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 13.717 ms vs 16.068 ms (14.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
