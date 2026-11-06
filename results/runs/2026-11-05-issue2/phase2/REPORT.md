# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 280; PASS=279; FAILED=0; UNSUPPORTED=1; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R0_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.614 | 25.901 | 9.847 | 27.745 | 16.817 | 25.226 | 9.149 | 27.170 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 15.175 | 29.243 | 8.758 | 32.113 | 14.060 | 29.897 | 10.841 | 35.772 |
| R2_simpleui | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.039 | 27.870 | 7.388 | 34.978 | 13.408 | 28.787 | 11.117 | 28.944 |
| R3_zenos | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 16.071 | 26.531 | 5.605 | 27.058 | 16.105 | 26.855 | 6.585 | 27.447 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 15.740 | 29.671 | 8.808 | 32.948 | 15.732 | 29.275 | 11.474 | 30.601 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 16.093 | 27.049 | 6.675 | 27.802 | 16.012 | 27.448 | 7.505 | 46.498 |
| R9_simpleui_vos | warm | real_2692 | 2692 | 9 | 57.000 | 1/1 | 30/30 | 16.078 | 28.482 | 6.515 | 31.616 | 13.652 | 28.060 | 10.763 | 33.855 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 148.074 | 167.339 | 130.573 | 223.113 | 133.869 | 148.954 | 125.387 | 232.058 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 18.033 | 28.987 | 10.044 | 103.812 | 19.023 | 28.201 | 10.618 | 111.058 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 133.158 | 162.589 | 126.550 | 222.248 | 132.648 | 132.868 | 110.445 | 205.061 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 20.484 | 30.257 | 11.991 | 103.563 | 18.413 | 26.938 | 9.172 | 94.658 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 136.506 | 161.105 | 129.795 | 207.702 | 132.251 | 143.855 | 123.087 | 170.967 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 29.394 | 41.664 | 12.875 | 73.586 | 17.609 | 22.014 | 11.988 | 44.995 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R0_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 13.408 ms vs 16.817 ms (20.3% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.039 ms vs 16.614 ms (3.5% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 16.105 ms vs 16.817 ms (4.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.071 ms vs 16.614 ms (3.3% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 13.408 ms vs 15.732 ms (14.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.740 ms vs 16.039 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 16.012 ms vs 16.105 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.071 ms vs 16.093 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 13.408 ms vs 13.652 ms (1.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.039 ms vs 16.078 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 13.652 ms vs 14.060 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.175 ms vs 16.078 ms (5.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R0_stock | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 34.579 | 34.579 | 34.579 | 34.579–34.579 |
| R0_stock | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 37.207 | 37.207 | 37.207 | 37.207–37.207 |
| R0_stock | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 29.621 | 26.828 | 29.992 | 26.130–30.085 |
| R0_stock | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 29.129 | 27.285 | 29.666 | 26.824–29.800 |
| R0_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 54.742 | 45.328 | 74.360 | 43.700–101.036 |
| R0_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 33.912 | 27.496 | 47.650 | 27.341–49.585 |
| R0_stock | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.645 | 16.619 | 16.664 | 16.613–16.664 |
| R0_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 28.472 | 26.977 | 33.773 | 26.159–42.192 |
| R0_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.817 | 11.855 | 25.226 | 9.149–27.170 |
| R0_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 29.076 | 27.193 | 37.173 | 26.427–41.179 |
| R0_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 37.436 | 34.561 | 48.126 | 31.876–51.513 |
| R0_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.300 | 17.818 | 39.208 | 15.298–44.856 |
| R0_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.614 | 14.142 | 25.901 | 9.847–27.745 |
| R0_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 61.047 | 55.415 | 68.981 | 52.683–83.020 |
| R0_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 103.885 | 54.634 | 120.935 | 52.880–170.908 |
| R0_stock | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.659 | 16.320 | 16.682 | 13.428–16.723 |
| R0_stock | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 657.270 | 657.270 | 657.270 | 657.270–657.270 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 11.943 | 11.943 | 11.943 | 11.943–11.943 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 58.605 | 58.605 | 58.605 | 58.605–58.605 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 16.560 | 14.259 | 17.950 | 13.684–18.298 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 53.502 | 52.952 | 59.386 | 52.815–60.857 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 133.869 | 132.140 | 148.954 | 125.387–232.058 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 19.023 | 11.265 | 28.201 | 10.618–111.058 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 29.285 | 25.827 | 105.883 | 24.224–123.958 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 148.074 | 132.492 | 167.339 | 130.573–223.113 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 18.033 | 15.746 | 28.987 | 10.044–103.812 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 178.221 | 144.370 | 200.671 | 142.126–248.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 265.443 | 244.336 | 278.408 | 184.230–281.277 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 41.661 | 37.292 | 48.069 | 36.878–49.274 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.672 | 16.635 | 16.700 | 16.633–16.707 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.669 | 13.127 | 30.782 | 11.953–30.877 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.060 | 11.234 | 29.897 | 10.841–35.772 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 55.061 | 49.492 | 62.979 | 49.476–63.830 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 91.681 | 80.249 | 110.934 | 79.506–112.141 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 30.392 | 21.026 | 55.278 | 20.145–57.775 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.175 | 9.533 | 29.243 | 8.758–32.113 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 127.963 | 117.072 | 140.192 | 100.147–150.070 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 138.807 | 96.532 | 168.496 | 65.572–187.426 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 49.099 | 45.554 | 52.200 | 45.538–52.537 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 22.851 | 19.968 | 48.192 | 19.946–212.725 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1421.335 | 1421.335 | 1421.335 | 1421.335–1421.335 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.651 | 12.516 | 16.681 | 7.122–16.685 |
| R2_simpleui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 18.735 | 18.735 | 18.735 | 18.735–18.735 |
| R2_simpleui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 53.118 | 53.118 | 53.118 | 53.118–53.118 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 16.637 | 16.281 | 22.493 | 16.192–23.957 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 54.963 | 50.712 | 57.397 | 49.649–58.005 |
| R2_simpleui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 144.307 | 128.407 | 160.332 | 123.561–167.195 |
| R2_simpleui | warm | real_2692 | 2692 | close_book | PASS | 10 | 233.770 | 118.919 | 238.242 | 99.227–241.361 |
| R2_simpleui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.655 | 16.444 | 27.790 | 14.895–127.886 |
| R2_simpleui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.675 | 13.795 | 30.023 | 13.481–31.117 |
| R2_simpleui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.408 | 12.026 | 28.787 | 11.117–28.944 |
| R2_simpleui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 63.212 | 53.418 | 68.712 | 49.653–69.291 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 66.118 | 65.157 | 85.959 | 63.920–91.794 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 32.401 | 18.554 | 47.566 | 17.075–49.946 |
| R2_simpleui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.039 | 9.615 | 27.870 | 7.388–34.978 |
| R2_simpleui | warm | real_2692 | 2692 | open_book | PASS | 10 | 102.834 | 88.951 | 117.228 | 82.077–170.381 |
| R2_simpleui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 125.993 | 80.217 | 143.722 | 72.867–189.741 |
| R2_simpleui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 18.295 | 17.052 | 39.820 | 16.577–126.721 |
| R2_simpleui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1102.977 | 1102.977 | 1102.977 | 1102.977–1102.977 |
| R2_simpleui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.654 | 13.822 | 16.690 | 7.347–16.695 |
| R3_zenos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 84.918 | 84.918 | 84.918 | 84.918–84.918 |
| R3_zenos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 16.570 | 16.570 | 16.570 | 16.570–16.570 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 69.518 | 63.419 | 71.844 | 61.894–72.426 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 18.678 | 16.611 | 18.892 | 16.094–18.945 |
| R3_zenos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 36.276 | 31.392 | 48.888 | 30.779–51.422 |
| R3_zenos | warm | real_2692 | 2692 | close_book | PASS | 10 | 58.853 | 54.815 | 60.538 | 34.658–63.837 |
| R3_zenos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 33.297 | 30.909 | 33.325 | 30.382–33.325 |
| R3_zenos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 33.371 | 33.357 | 33.403 | 33.352–33.482 |
| R3_zenos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.105 | 8.893 | 26.855 | 6.585–27.447 |
| R3_zenos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 17.343 | 16.209 | 20.313 | 16.042–21.981 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 15.988 | 13.382 | 30.043 | 12.483–30.796 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 21.800 | 11.452 | 29.784 | 10.926–33.957 |
| R3_zenos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.071 | 7.636 | 26.531 | 5.605–27.058 |
| R3_zenos | warm | real_2692 | 2692 | open_book | PASS | 10 | 58.822 | 52.077 | 72.482 | 43.684–90.676 |
| R3_zenos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 126.143 | 83.311 | 151.434 | 67.432–195.175 |
| R3_zenos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.672 | 16.562 | 17.967 | 15.923–20.472 |
| R3_zenos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 513.731 | 513.731 | 513.731 | 513.731–513.731 |
| R3_zenos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 33.300 | 33.275 | 33.443 | 33.252–34.275 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 14.608 | 14.608 | 14.608 | 14.608–14.608 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 54.742 | 54.742 | 54.742 | 54.742–54.742 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 18.640 | 15.563 | 21.163 | 14.794–21.794 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 53.802 | 53.230 | 56.408 | 53.087–57.060 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 132.648 | 132.448 | 132.868 | 110.445–205.061 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 18.413 | 10.394 | 26.938 | 9.172–94.658 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 30.623 | 27.278 | 101.202 | 26.046–132.496 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 133.158 | 132.406 | 162.589 | 126.550–222.248 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 20.484 | 14.779 | 30.257 | 11.991–103.563 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 147.920 | 123.513 | 159.832 | 122.622–159.895 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 236.214 | 225.559 | 253.427 | 217.364–276.511 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 38.450 | 37.662 | 44.484 | 37.544–46.911 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.648 | 16.324 | 29.535 | 13.689–144.972 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.667 | 13.047 | 30.399 | 12.866–31.285 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.732 | 12.557 | 29.275 | 11.474–30.601 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 67.174 | 53.651 | 70.303 | 52.777–76.489 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 67.428 | 63.513 | 89.876 | 63.464–91.528 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 33.556 | 18.537 | 46.050 | 16.230–46.508 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.740 | 9.821 | 29.671 | 8.808–32.948 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 98.222 | 83.908 | 152.171 | 80.191–157.485 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 129.823 | 86.228 | 148.523 | 59.235–190.803 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 50.053 | 47.334 | 60.845 | 46.845–73.379 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 20.404 | 19.449 | 49.419 | 18.931–300.276 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1038.180 | 1038.180 | 1038.180 | 1038.180–1038.180 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.520 | 7.917 | 16.670 | 7.651–16.690 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 85.668 | 85.668 | 85.668 | 85.668–85.668 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 19.079 | 19.079 | 19.079 | 19.079–19.079 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 66.122 | 62.160 | 66.219 | 61.169–66.243 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 17.982 | 16.919 | 19.465 | 16.653–19.836 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 132.251 | 131.285 | 143.855 | 123.087–170.967 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 17.609 | 12.823 | 22.014 | 11.988–44.995 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 27.191 | 22.113 | 69.120 | 19.650–81.729 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 136.506 | 132.427 | 161.105 | 129.795–207.702 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 29.394 | 24.819 | 41.664 | 12.875–73.586 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 34.427 | 31.330 | 48.172 | 30.853–48.402 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 38.737 | 36.465 | 39.403 | 36.029–39.670 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 10.399 | 9.436 | 11.539 | 8.730–11.544 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 33.311 | 32.239 | 33.332 | 23.381–33.374 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 33.359 | 33.329 | 33.394 | 33.304–33.418 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.012 | 8.364 | 27.448 | 7.505–46.498 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 17.659 | 15.969 | 19.544 | 15.782–20.152 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 16.290 | 13.380 | 30.946 | 13.377–31.352 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 19.727 | 10.284 | 31.724 | 9.652–31.942 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.093 | 7.663 | 27.049 | 6.675–27.802 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 103.239 | 74.711 | 113.176 | 63.077–116.381 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 124.009 | 83.860 | 147.728 | 74.060–193.868 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 28.575 | 27.269 | 34.925 | 25.813–48.298 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.648 | 16.106 | 17.840 | 11.417–21.431 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 578.502 | 578.502 | 578.502 | 578.502–578.502 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 33.285 | 33.238 | 33.442 | 33.234–34.338 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 13.349 | 13.349 | 13.349 | 13.349–13.349 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 48.376 | 48.376 | 48.376 | 48.376–48.376 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 16.471 | 15.621 | 19.354 | 15.409–20.075 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 57.276 | 53.118 | 57.798 | 52.079–57.929 |
| R9_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 172.269 | 144.081 | 186.921 | 141.671–191.322 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 261.286 | 241.765 | 273.847 | 193.938–288.058 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.667 | 16.625 | 16.677 | 16.618–16.681 |
| R9_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.656 | 14.324 | 30.680 | 14.301–32.348 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.652 | 11.327 | 28.060 | 10.763–33.855 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 51.220 | 49.515 | 65.440 | 48.392–65.758 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 80.185 | 79.640 | 107.410 | 79.237–111.960 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 30.560 | 22.874 | 51.446 | 20.835–54.270 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.078 | 8.832 | 28.482 | 6.515–31.616 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 119.994 | 108.800 | 132.385 | 106.914–142.672 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 130.872 | 92.848 | 150.128 | 63.597–202.373 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 20.623 | 19.785 | 149.231 | 18.728–157.301 |
| R9_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1296.678 | 1296.678 | 1296.678 | 1296.678–1296.678 |
| R9_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.648 | 13.521 | 16.676 | 6.478–16.680 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 253.943 | 253.943 | 253.943 | 253.943–253.943 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 333.146 | 333.146 | 333.146 | 333.146–333.146 |
| R0_stock | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 341.847 | 341.847 | 341.847 | 341.847–341.847 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 402.390 | 402.390 | 402.390 | 402.390–402.390 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 207.032 | 206.586 | 228.665 | 206.475–234.073 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 270.860 | 266.867 | 293.017 | 265.869–298.557 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 277.466 | 272.966 | 299.195 | 271.841–304.628 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 286.930 | 282.888 | 308.609 | 281.878–314.029 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 214.573 | 214.573 | 214.573 | 214.573–214.573 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1341.887 | 1341.887 | 1341.887 | 1341.887–1341.887 |
| R0_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 10425.166 | 10425.166 | 10425.166 | 10425.166–10425.166 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 10444.797 | 10444.797 | 10444.797 | 10444.797–10444.797 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 563.866 | 563.866 | 563.866 | 563.866–563.866 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 651.747 | 651.747 | 651.747 | 651.747–651.747 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 664.760 | 664.760 | 664.760 | 664.760–664.760 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 825.934 | 825.934 | 825.934 | 825.934–825.934 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 369.639 | 369.476 | 393.237 | 369.435–399.137 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 450.962 | 449.206 | 486.764 | 448.767–495.714 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 461.313 | 460.927 | 497.939 | 460.830–507.096 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 474.550 | 473.851 | 510.834 | 473.677–519.905 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 360.074 | 360.074 | 360.074 | 360.074–360.074 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1830.123 | 1830.123 | 1830.123 | 1830.123–1830.123 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 37008.071 | 37008.071 | 37008.071 | 37008.071–37008.071 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 38170.659 | 38170.659 | 38170.659 | 38170.659–38170.659 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 471.340 | 471.340 | 471.340 | 471.340–471.340 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 557.807 | 557.807 | 557.807 | 557.807–557.807 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 569.704 | 569.704 | 569.704 | 569.704–569.704 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 718.808 | 718.808 | 718.808 | 718.808–718.808 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 360.550 | 355.043 | 379.807 | 353.666–384.621 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 460.793 | 440.895 | 464.565 | 435.920–465.508 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 471.179 | 451.180 | 474.743 | 446.180–475.634 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 484.125 | 463.224 | 488.047 | 457.999–489.028 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 362.770 | 362.770 | 362.770 | 362.770–362.770 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1890.419 | 1890.419 | 1890.419 | 1890.419–1890.419 |
| R2_simpleui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 20789.385 | 20789.385 | 20789.385 | 20789.385–20789.385 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 22117.550 | 22117.550 | 22117.550 | 22117.550–22117.550 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 466.174 | 466.174 | 466.174 | 466.174–466.174 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 595.736 | 595.736 | 595.736 | 595.736–595.736 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 612.986 | 612.986 | 612.986 | 612.986–612.986 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 627.016 | 627.016 | 627.016 | 627.016–627.016 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 307.021 | 293.348 | 313.574 | 289.930–315.212 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 402.502 | 393.545 | 403.817 | 391.306–404.146 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 412.540 | 403.440 | 413.743 | 401.165–414.043 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 424.453 | 415.158 | 425.677 | 412.834–425.982 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 303.466 | 303.466 | 303.466 | 303.466–303.466 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2139.920 | 2139.920 | 2139.920 | 2139.920–2139.920 |
| R3_zenos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11484.318 | 11484.318 | 11484.318 | 11484.318–11484.318 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11516.806 | 11516.806 | 11516.806 | 11516.806–11516.806 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 414.299 | 414.299 | 414.299 | 414.299–414.299 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 498.469 | 498.469 | 498.469 | 498.469–498.469 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 510.830 | 510.830 | 510.830 | 510.830–510.830 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 660.295 | 660.295 | 660.295 | 660.295–660.295 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 366.628 | 351.600 | 387.826 | 347.843–393.125 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 465.108 | 435.363 | 476.564 | 427.927–479.428 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 475.404 | 445.431 | 487.103 | 437.937–490.027 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 487.568 | 457.266 | 499.479 | 449.690–502.457 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 383.788 | 383.788 | 383.788 | 383.788–383.788 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1927.601 | 1927.601 | 1927.601 | 1927.601–1927.601 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 34103.298 | 34103.298 | 34103.298 | 34103.298–34103.298 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 49720.836 | 49720.836 | 49720.836 | 49720.836–49720.836 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 475.281 | 475.281 | 475.281 | 475.281–475.281 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 618.487 | 618.487 | 618.487 | 618.487–618.487 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 631.972 | 631.972 | 631.972 | 631.972–631.972 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 644.637 | 644.637 | 644.637 | 644.637–644.637 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 295.767 | 293.752 | 311.970 | 293.248–316.021 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 390.917 | 386.372 | 401.774 | 385.235–404.488 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 401.567 | 396.556 | 412.378 | 395.304–415.081 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 413.350 | 408.069 | 424.299 | 406.749–427.036 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 289.913 | 289.913 | 289.913 | 289.913–289.913 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2122.238 | 2122.238 | 2122.238 | 2122.238–2122.238 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 24245.354 | 24245.354 | 24245.354 | 24245.354–24245.354 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 24292.128 | 24292.128 | 24292.128 | 24292.128–24292.128 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 547.553 | 547.553 | 547.553 | 547.553–547.553 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 621.598 | 621.598 | 621.598 | 621.598–621.598 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 634.944 | 634.944 | 634.944 | 634.944–634.944 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 791.971 | 791.971 | 791.971 | 791.971–791.971 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 346.975 | 342.096 | 377.010 | 340.876–384.519 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 426.304 | 425.794 | 467.740 | 425.667–478.099 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 436.244 | 435.886 | 478.086 | 435.796–488.546 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 448.017 | 447.533 | 490.420 | 447.412–501.020 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 347.995 | 347.995 | 347.995 | 347.995–347.995 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1811.038 | 1811.038 | 1811.038 | 1811.038–1811.038 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 22932.414 | 22932.414 | 22932.414 | 22932.414–22932.414 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 24794.594 | 24794.594 | 24794.594 | 24794.594–24794.594 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R0_stock | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9027.493 | 9027.493 | 9027.493–9027.493 | 11844.266 | 88592.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10323.157 | 10323.157 | 10323.157–10323.157 | 15041.715 | 90016.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9326.696 | 9449.178 | 9067.606–9479.798 | 13110.969 | 85152.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9307.220 | 9337.973 | 9077.380–9345.661 | 15205.572 | 86752.000 |
| R0_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9311.017 | 9311.017 | 9311.017–9311.017 | 9704.697 | 84960.000 |
| R0_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9416.079 | 9416.079 | 9416.079–9416.079 | 9427.985 | 98608.000 |
| R0_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14356.712 | 14356.712 | 14356.712–14356.712 | 14402.747 | 239184.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 17297.937 | 17297.937 | 17297.937–17297.937 | 31196.657 | 105712.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18354.218 | 18354.218 | 18354.218–18354.218 | 22140.579 | 108112.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16667.328 | 17048.388 | 16614.961–17143.652 | 27563.778 | 99280.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17687.441 | 18100.329 | 17644.723–18203.551 | 22050.571 | 103024.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16676.992 | 16676.992 | 16676.992–16676.992 | 26189.249 | 97984.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18512.969 | 18512.969 | 18512.969–18512.969 | 22787.480 | 110256.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 87926.147 | 87926.147 | 87926.147–87926.147 | 89949.607 | 392256.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15467.412 | 15467.412 | 15467.412–15467.412 | 27677.288 | 102112.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16201.826 | 16201.826 | 16201.826–16201.826 | 20262.599 | 104544.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 15495.248 | 15509.354 | 15491.311–15512.881 | 23017.394 | 97328.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16284.268 | 16305.939 | 16283.494–16311.357 | 20842.563 | 100576.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15537.381 | 15537.381 | 15537.381–15537.381 | 22691.889 | 96752.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16379.252 | 16379.252 | 16379.252–16379.252 | 16882.150 | 106880.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 67622.529 | 67622.529 | 67622.529–67622.529 | 67683.670 | 306000.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15352.756 | 15352.756 | 15352.756–15352.756 | 20415.872 | 94080.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18226.116 | 18226.116 | 18226.116–18226.116 | 29115.800 | 109984.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14439.312 | 14487.555 | 14401.866–14499.616 | 23268.728 | 94496.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 15929.940 | 15937.450 | 15924.323–15939.327 | 22250.281 | 98320.000 |
| R3_zenos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14434.319 | 14434.319 | 14434.319–14434.319 | 23901.100 | 94944.000 |
| R3_zenos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15917.680 | 15917.680 | 15917.680–15917.680 | 20513.098 | 121712.000 |
| R3_zenos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 22763.017 | 22763.017 | 22763.017–22763.017 | 24115.297 | 262800.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16039.732 | 16039.732 | 16039.732–16039.732 | 28751.705 | 103584.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16776.080 | 16776.080 | 16776.080–16776.080 | 20882.747 | 105808.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 15944.038 | 15959.016 | 15932.386–15962.761 | 24549.011 | 97392.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16823.151 | 16833.448 | 16760.339–16836.022 | 21460.045 | 101168.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15977.601 | 15977.601 | 15977.601–15977.601 | 25427.958 | 99168.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16826.046 | 16826.046 | 16826.046–16826.046 | 21491.320 | 109056.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 75373.697 | 75373.697 | 75373.697–75373.697 | 75437.576 | 388976.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 15828.338 | 15828.338 | 15828.338–15828.338 | 21976.135 | 95184.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18659.878 | 18659.878 | 18659.878–18659.878 | 29940.400 | 110608.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14736.805 | 14762.586 | 14719.707–14769.031 | 24540.856 | 95488.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 16289.664 | 16296.242 | 16279.305–16297.887 | 22666.278 | 99712.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14766.586 | 14766.586 | 14766.586–14766.586 | 24236.905 | 94848.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16286.571 | 16286.571 | 16286.571–16286.571 | 29700.616 | 122064.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 30186.204 | 30186.204 | 30186.204–30186.204 | 32371.780 | 323616.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16766.976 | 16766.976 | 16766.976–16766.976 | 27809.137 | 105856.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17645.542 | 17645.542 | 17645.542–17645.542 | 21587.132 | 108352.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 16206.921 | 16622.687 | 16182.198–16726.628 | 25723.254 | 97440.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 17185.612 | 17666.081 | 17179.093–17786.198 | 21634.730 | 101136.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 16242.425 | 16242.425 | 16242.425–16242.425 | 25081.588 | 97376.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18063.937 | 18063.937 | 18063.937–18063.937 | 22326.972 | 111024.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 79917.073 | 79917.073 | 79917.073–79917.073 | 82152.920 | 333936.000 |

## Data-derived comparisons

- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 13.408 ms vs 16.817 ms (20.3% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.039 ms vs 16.614 ms (3.5% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 16.105 ms vs 16.817 ms (4.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.071 ms vs 16.614 ms (3.3% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 13.408 ms vs 15.732 ms (14.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.740 ms vs 16.039 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 16.012 ms vs 16.105 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.071 ms vs 16.093 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 13.408 ms vs 13.652 ms (1.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.039 ms vs 16.078 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 13.652 ms vs 14.060 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.175 ms vs 16.078 ms (5.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
