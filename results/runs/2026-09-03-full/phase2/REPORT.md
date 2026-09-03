# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `26bb78442d6bed9f4933bc3c30a6209507dc0fecb152335c3fd708bd660db8d4`
Reader flash setting: `unset`

Aggregated rows: 617; PASS=611; FAILED=0; UNSUPPORTED=6; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R0_stock | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 14.260 | 21.759 | 8.586 | 28.518 | 16.811 | 23.935 | 8.654 | 34.623 |
| R0_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 28.045 | 38.936 | 14.605 | 54.044 | 16.328 | 28.769 | 11.724 | 32.363 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 17.593 | 32.405 | 11.900 | 35.609 | 32.198 | 44.076 | 8.542 | 55.092 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 18.524 | 52.837 | 11.397 | 77.031 | 16.988 | 51.526 | 9.262 | 59.648 |
| R11_project_title_vos | paging | real_2692 | 2692 | 14 | 37.000 | 3/3 | 90/90 | 8.719 | 9.951 | 7.090 | 13.787 | 8.478 | 9.838 | 7.335 | 13.583 |
| R11_project_title_vos | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 9.195 | 11.498 | 7.778 | 11.759 | 9.142 | 10.229 | 8.099 | 13.543 |
| R1_bookshelf | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 14.708 | 22.070 | 9.027 | 30.565 | 16.931 | 25.051 | 8.734 | 31.828 |
| R1_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.980 | 29.492 | 13.547 | 33.013 | 15.732 | 26.969 | 12.922 | 36.323 |
| R2_simpleui | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 16.415 | 29.980 | 9.931 | 36.249 | 28.634 | 46.607 | 4.602 | 61.168 |
| R2_simpleui | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 16.979 | 48.728 | 10.252 | 51.418 | 14.061 | 44.756 | 10.048 | 50.164 |
| R3_zenos | paging | real_2692 | 2692 | 5 | 101.000 | 3/3 | 90/90 | 8.605 | 12.192 | 6.438 | 32.048 | 12.864 | 26.956 | 7.094 | 32.931 |
| R3_zenos | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 8.111 | 21.317 | 3.029 | 23.499 | 8.009 | 23.044 | 3.311 | 24.586 |
| R4_project_title | paging | real_2692 | 2692 | 14 | 37.000 | 3/3 | 90/90 | 9.072 | 10.380 | 7.268 | 14.500 | 8.977 | 10.933 | 7.243 | 14.655 |
| R4_project_title | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 7.725 | 8.433 | 6.994 | 9.126 | 7.902 | 8.268 | 6.765 | 8.339 |
| R5_vos | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 15.973 | 26.660 | 11.252 | 31.510 | 18.178 | 31.051 | 13.816 | 33.318 |
| R5_vos | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 11.494 | 25.855 | 9.175 | 27.775 | 10.114 | 22.803 | 6.756 | 27.137 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 18.574 | 33.564 | 11.076 | 37.834 | 32.108 | 51.554 | 9.520 | 58.074 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 14.755 | 44.037 | 9.137 | 46.396 | 10.277 | 41.062 | 6.710 | 44.269 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | 5 | 101.000 | 3/3 | 90/90 | 8.500 | 11.811 | 5.739 | 29.351 | 12.789 | 26.812 | 6.758 | 30.853 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 8.607 | 23.173 | 6.833 | 28.749 | 13.553 | 28.425 | 7.880 | 30.538 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 16.767 | 28.573 | 13.076 | 46.135 | 19.297 | 34.119 | 14.431 | 118.385 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 16.288 | 28.003 | 14.686 | 31.253 | 14.852 | 26.793 | 11.459 | 30.580 |
| R9_simpleui_vos | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 16.493 | 31.474 | 8.820 | 35.865 | 28.995 | 48.130 | 4.783 | 54.851 |
| R9_simpleui_vos | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 20.297 | 52.137 | 12.924 | 69.772 | 16.416 | 46.887 | 9.110 | 50.782 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 173.196 | 200.064 | 164.806 | 204.305 | 170.566 | 188.977 | 160.053 | 204.032 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 31.349 | 42.588 | 8.653 | 51.597 | 15.951 | 19.567 | 8.089 | 25.155 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 162.618 | 173.494 | 158.393 | 179.476 | 161.476 | 168.254 | 158.126 | 176.525 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 21.401 | 31.850 | 15.573 | 41.324 | 28.068 | 55.916 | 14.920 | 85.331 |
| R1_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 171.226 | 175.623 | 162.690 | 184.039 | 170.120 | 178.771 | 158.338 | 189.915 |
| R1_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 29.076 | 35.319 | 9.186 | 46.843 | 12.992 | 18.907 | 7.998 | 26.189 |
| R1_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 177.332 | 189.716 | 173.388 | 264.315 | 160.897 | 164.978 | 158.430 | 169.250 |
| R1_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 24.678 | 33.487 | 9.193 | 44.314 | 9.473 | 14.796 | 7.937 | 19.908 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 173.165 | 199.804 | 167.997 | 204.321 | 171.526 | 195.331 | 160.071 | 214.378 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 31.087 | 41.167 | 9.271 | 55.452 | 16.249 | 19.655 | 8.228 | 30.145 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 191.111 | 203.764 | 173.662 | 251.016 | 176.623 | 185.496 | 164.539 | 191.046 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 40.679 | 60.036 | 21.898 | 79.131 | 18.680 | 24.198 | 9.705 | 24.981 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 178.183 | 190.347 | 166.883 | 265.498 | 166.561 | 170.258 | 159.349 | 178.062 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 22.776 | 28.302 | 8.869 | 39.043 | 15.373 | 19.322 | 8.804 | 28.236 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 164.680 | 174.013 | 159.060 | 192.860 | 160.563 | 166.065 | 158.228 | 168.561 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 9.947 | 23.100 | 7.813 | 34.063 | 9.460 | 14.017 | 7.923 | 15.267 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 176.147 | 190.420 | 168.027 | 196.752 | 175.250 | 188.818 | 161.302 | 212.644 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 31.675 | 44.525 | 9.570 | 130.545 | 16.304 | 22.570 | 7.991 | 37.671 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 160.638 | 166.341 | 158.346 | 245.314 | 162.712 | 181.325 | 157.479 | 187.967 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 22.438 | 29.945 | 9.317 | 45.032 | 10.306 | 15.244 | 7.896 | 18.493 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R0_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R11_project_title_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R1_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R4_project_title | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R5_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R8_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R0_stock` has a lower descriptive median than `R1_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 16.811 ms vs 16.931 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R1_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 14.260 ms vs 14.708 ms (3.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 15.732 ms vs 16.328 ms (3.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.980 ms vs 28.045 ms (39.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (paging, real_2692, 2692 books): 16.811 ms vs 28.634 ms (41.3% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 14.260 ms vs 16.415 ms (13.1% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 14.061 ms vs 16.328 ms (13.9% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.979 ms vs 28.045 ms (39.5% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 12.864 ms vs 16.811 ms (23.5% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 8.605 ms vs 14.260 ms (39.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 8.009 ms vs 16.328 ms (50.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 8.111 ms vs 28.045 ms (71.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 8.977 ms vs 16.811 ms (46.6% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 9.072 ms vs 14.260 ms (36.4% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 7.902 ms vs 16.328 ms (51.6% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 7.725 ms vs 28.045 ms (72.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R0_stock` has a lower descriptive median than `R5_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 16.811 ms vs 18.178 ms (7.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R5_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 14.260 ms vs 15.973 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 10.114 ms vs 16.328 ms (38.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.494 ms vs 28.045 ms (59.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 28.634 ms vs 32.108 ms (10.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 16.415 ms vs 18.574 ms (11.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 10.277 ms vs 14.061 ms (26.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 14.755 ms vs 16.979 ms (13.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (paging, real_2692, 2692 books): 12.789 ms vs 12.864 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_sequential_paging` (paging, real_2692, 2692 books): 8.500 ms vs 8.605 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 8.009 ms vs 13.553 ms (40.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 8.111 ms vs 8.607 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 18.178 ms vs 19.297 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 15.973 ms vs 16.767 ms (4.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 10.114 ms vs 14.852 ms (31.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.494 ms vs 16.288 ms (29.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 28.634 ms vs 28.995 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 16.415 ms vs 16.493 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 14.061 ms vs 16.416 ms (14.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.979 ms vs 20.297 ms (16.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 28.995 ms vs 32.198 ms (10.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 16.493 ms vs 17.593 ms (6.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 16.416 ms vs 16.988 ms (3.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 18.524 ms vs 20.297 ms (8.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (paging, real_2692, 2692 books): 8.478 ms vs 8.977 ms (5.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (paging, real_2692, 2692 books): 8.719 ms vs 9.072 ms (3.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R11_project_title_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 7.902 ms vs 9.142 ms (13.6% lower).
- `R4_project_title` has a lower descriptive median than `R11_project_title_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 7.725 ms vs 9.195 ms (16.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R0_stock | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 16.811 | 10.420 | 23.935 | 8.654–34.623 |
| R0_stock | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 14.260 | 9.415 | 21.759 | 8.586–28.518 |
| R0_stock | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 22.516 | 18.596 | 22.900 | 17.616–22.996 |
| R0_stock | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 35.909 | 35.909 | 35.909 | 35.909–35.909 |
| R0_stock | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 35.985 | 35.985 | 35.985 | 35.985–35.985 |
| R0_stock | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 31.099 | 30.867 | 31.176 | 30.809–31.195 |
| R0_stock | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 32.426 | 32.000 | 33.050 | 31.893–33.206 |
| R0_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 82.864 | 62.498 | 126.718 | 55.275–138.166 |
| R0_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 33.239 | 28.807 | 35.837 | 26.505–41.750 |
| R0_stock | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.380 | 7.878 | 8.627 | 7.459–8.824 |
| R0_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 31.334 | 29.592 | 45.384 | 28.662–49.014 |
| R0_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.328 | 14.598 | 28.769 | 11.724–32.363 |
| R0_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 31.516 | 30.419 | 44.457 | 28.687–45.685 |
| R0_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 85.734 | 74.045 | 130.042 | 69.483–135.774 |
| R0_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.102 | 16.211 | 36.442 | 14.726–44.672 |
| R0_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 28.045 | 16.705 | 38.936 | 14.605–54.044 |
| R0_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 97.847 | 74.275 | 108.968 | 72.137–114.210 |
| R0_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 147.924 | 118.954 | 184.388 | 110.761–208.412 |
| R0_stock | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.374 | 7.652 | 8.797 | 7.407–8.828 |
| R0_stock | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 2447.845 | 2447.845 | 2447.845 | 2447.845–2447.845 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 170.566 | 163.701 | 188.977 | 160.053–204.032 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 15.951 | 8.641 | 19.567 | 8.089–25.155 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 173.196 | 168.809 | 200.064 | 164.806–204.305 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 31.349 | 25.258 | 42.588 | 8.653–51.597 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 22.070 | 20.453 | 22.160 | 20.049–22.183 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 32.198 | 10.675 | 44.076 | 8.542–55.092 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 17.593 | 15.617 | 32.405 | 11.900–35.609 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 128.942 | 123.516 | 201.160 | 122.160–219.214 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 12.582 | 10.968 | 24.356 | 10.565–27.299 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 40.447 | 40.447 | 40.447 | 40.447–40.447 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 110.148 | 110.148 | 110.148 | 110.148–110.148 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 34.699 | 32.028 | 34.921 | 31.360–34.976 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 96.795 | 94.216 | 97.673 | 93.571–97.893 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 161.476 | 158.848 | 168.254 | 158.126–176.525 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 28.068 | 17.540 | 55.916 | 14.920–85.331 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 19.160 | 16.551 | 91.392 | 15.439–111.418 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 162.618 | 159.893 | 173.494 | 158.393–179.476 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 21.401 | 16.401 | 31.850 | 15.573–41.324 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 88.547 | 58.451 | 123.998 | 54.112–130.046 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 167.993 | 86.606 | 282.590 | 82.318–290.518 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 22.327 | 16.976 | 96.621 | 16.459–131.750 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.277 | 7.323 | 8.686 | 7.166–9.203 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 32.346 | 31.454 | 48.123 | 31.000–50.418 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.988 | 12.360 | 51.526 | 9.262–59.648 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 97.916 | 88.284 | 114.553 | 87.933–130.892 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 91.871 | 53.209 | 101.197 | 50.993–102.481 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 39.416 | 32.030 | 100.730 | 31.898–113.496 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 18.524 | 12.638 | 52.837 | 11.397–77.031 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 119.273 | 109.586 | 140.921 | 109.390–155.281 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 143.169 | 107.874 | 164.895 | 97.900–216.630 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 23.627 | 21.167 | 26.090 | 20.374–28.039 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 12.168 | 10.669 | 31.005 | 10.394–146.568 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1495.270 | 1495.270 | 1495.270 | 1495.270–1495.270 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 9.820 | 8.202 | 17.370 | 7.340–18.265 |
| R11_project_title_vos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 8.478 | 7.897 | 9.838 | 7.335–13.583 |
| R11_project_title_vos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 8.719 | 7.877 | 9.951 | 7.090–13.787 |
| R11_project_title_vos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 7.179 | 6.975 | 7.958 | 6.924–8.153 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 40.517 | 40.517 | 40.517 | 40.517–40.517 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 39.879 | 39.879 | 39.879 | 39.879–39.879 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 40.071 | 39.946 | 41.237 | 39.915–41.528 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 39.729 | 38.599 | 40.890 | 38.316–41.180 |
| R11_project_title_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 34.335 | 32.891 | 37.146 | 32.628–40.288 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 40.350 | 35.931 | 42.304 | 33.368–48.288 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 9.130 | 8.316 | 11.743 | 7.744–12.090 |
| R11_project_title_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 41.428 | 38.932 | 47.173 | 37.693–49.151 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 9.142 | 8.323 | 10.229 | 8.099–13.543 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 40.032 | 38.255 | 47.191 | 37.633–48.046 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 48.310 | 45.975 | 55.895 | 45.380–57.926 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.793 | 14.037 | 31.720 | 12.738–32.505 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 9.195 | 8.197 | 11.498 | 7.778–11.759 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 59.245 | 53.236 | 66.442 | 51.644–82.613 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 107.136 | 60.230 | 121.696 | 57.835–175.621 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.793 | 8.171 | 8.984 | 7.583–9.520 |
| R11_project_title_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 353.463 | 353.463 | 353.463 | 353.463–353.463 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 170.120 | 161.940 | 178.771 | 158.338–189.915 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 12.992 | 8.511 | 18.907 | 7.998–26.189 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 171.226 | 166.702 | 175.623 | 162.690–184.039 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 29.076 | 21.510 | 35.319 | 9.186–46.843 |
| R1_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 8.359 | 8.233 | 9.287 | 8.201–9.519 |
| R1_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 16.931 | 12.649 | 25.051 | 8.734–31.828 |
| R1_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 14.708 | 10.497 | 22.070 | 9.027–30.565 |
| R1_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 149.157 | 145.312 | 152.104 | 144.351–152.841 |
| R1_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 25.103 | 12.806 | 25.143 | 9.732–25.153 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 37.023 | 37.023 | 37.023 | 37.023–37.023 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 39.979 | 39.979 | 39.979 | 39.979–39.979 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 30.771 | 29.713 | 31.611 | 29.449–31.821 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 30.457 | 29.507 | 30.720 | 29.269–30.786 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 160.897 | 159.013 | 164.978 | 158.430–169.250 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 9.473 | 8.179 | 14.796 | 7.937–19.908 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 20.297 | 16.473 | 36.955 | 14.799–45.674 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 177.332 | 173.663 | 189.716 | 173.388–264.315 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 24.678 | 20.104 | 33.487 | 9.193–44.314 |
| R1_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 69.264 | 58.077 | 83.601 | 57.528–87.024 |
| R1_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 39.539 | 27.612 | 52.863 | 26.128–66.854 |
| R1_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 7.542 | 6.922 | 8.357 | 6.791–8.400 |
| R1_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.319 | 7.790 | 8.630 | 7.533–8.892 |
| R1_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 31.395 | 30.380 | 47.488 | 30.373–51.255 |
| R1_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.732 | 13.855 | 26.969 | 12.922–36.323 |
| R1_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 31.572 | 31.070 | 47.552 | 30.857–48.518 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 85.822 | 45.531 | 118.765 | 45.171–118.828 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 25.100 | 18.514 | 45.846 | 17.272–52.737 |
| R1_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.980 | 14.941 | 29.492 | 13.547–33.013 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 68.245 | 48.164 | 74.271 | 47.528–76.551 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 117.541 | 61.425 | 139.496 | 58.795–201.477 |
| R1_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 16.811 | 15.714 | 19.532 | 15.647–23.452 |
| R1_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.322 | 7.949 | 8.899 | 7.787–9.199 |
| R1_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 562.804 | 562.804 | 562.804 | 562.804–562.804 |
| R2_simpleui | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 28.634 | 8.175 | 46.607 | 4.602–61.168 |
| R2_simpleui | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 16.415 | 12.825 | 29.980 | 9.931–36.249 |
| R2_simpleui | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 27.120 | 24.163 | 33.936 | 23.424–35.640 |
| R2_simpleui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 44.500 | 44.500 | 44.500 | 44.500–44.500 |
| R2_simpleui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 133.776 | 133.776 | 133.776 | 133.776–133.776 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 33.348 | 32.191 | 33.366 | 31.902–33.371 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 115.264 | 114.544 | 115.974 | 114.364–116.151 |
| R2_simpleui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 107.792 | 75.367 | 132.536 | 74.941–147.505 |
| R2_simpleui | warm | real_2692 | 2692 | close_book | PASS | 10 | 219.028 | 202.976 | 237.607 | 100.237–240.542 |
| R2_simpleui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.694 | 8.149 | 9.210 | 7.670–9.693 |
| R2_simpleui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 32.294 | 31.464 | 48.817 | 30.830–53.635 |
| R2_simpleui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.061 | 11.244 | 44.756 | 10.048–50.164 |
| R2_simpleui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 128.874 | 75.121 | 143.600 | 48.359–164.133 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 97.529 | 69.036 | 108.261 | 68.283–110.005 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 34.252 | 27.534 | 74.906 | 25.241–78.039 |
| R2_simpleui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.979 | 14.023 | 48.728 | 10.252–51.418 |
| R2_simpleui | warm | real_2692 | 2692 | open_book | PASS | 10 | 112.244 | 105.532 | 131.476 | 100.626–203.744 |
| R2_simpleui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 142.297 | 94.570 | 173.866 | 82.082–207.219 |
| R2_simpleui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 19.418 | 17.102 | 33.795 | 16.239–144.353 |
| R2_simpleui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1369.156 | 1369.156 | 1369.156 | 1369.156–1369.156 |
| R2_simpleui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 11.178 | 8.177 | 17.543 | 8.112–19.454 |
| R3_zenos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 12.864 | 8.013 | 26.956 | 7.094–32.931 |
| R3_zenos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 8.605 | 7.624 | 12.192 | 6.438–32.048 |
| R3_zenos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 28.562 | 20.083 | 33.293 | 17.963–34.476 |
| R3_zenos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 114.844 | 114.844 | 114.844 | 114.844–114.844 |
| R3_zenos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 47.999 | 47.999 | 47.999 | 47.999–47.999 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 104.838 | 104.754 | 106.136 | 104.733–106.460 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 49.446 | 48.428 | 51.888 | 48.174–52.498 |
| R3_zenos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 48.154 | 33.480 | 61.261 | 32.733–65.419 |
| R3_zenos | warm | real_2692 | 2692 | close_book | PASS | 10 | 33.614 | 30.691 | 39.266 | 28.962–41.366 |
| R3_zenos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 17.014 | 16.231 | 22.406 | 12.332–64.783 |
| R3_zenos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 35.581 | 33.718 | 38.634 | 33.673–42.561 |
| R3_zenos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 8.009 | 6.242 | 23.044 | 3.311–24.586 |
| R3_zenos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 42.263 | 37.399 | 48.623 | 36.791–54.240 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 54.666 | 35.565 | 61.878 | 35.289–64.025 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 32.727 | 13.385 | 41.334 | 12.406–42.175 |
| R3_zenos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 8.111 | 6.726 | 21.317 | 3.029–23.499 |
| R3_zenos | warm | real_2692 | 2692 | open_book | PASS | 10 | 123.202 | 114.943 | 136.274 | 114.134–142.236 |
| R3_zenos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 137.733 | 110.022 | 163.113 | 96.008–212.428 |
| R3_zenos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 9.200 | 8.156 | 11.804 | 7.832–11.933 |
| R3_zenos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 516.548 | 516.548 | 516.548 | 516.548–516.548 |
| R3_zenos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 6.378 | 6.044 | 8.022 | 5.654–9.435 |
| R4_project_title | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 8.977 | 8.138 | 10.933 | 7.243–14.655 |
| R4_project_title | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 9.072 | 8.241 | 10.380 | 7.268–14.500 |
| R4_project_title | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 9.042 | 8.483 | 9.411 | 8.343–9.503 |
| R4_project_title | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 31.902 | 31.902 | 31.902 | 31.902–31.902 |
| R4_project_title | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 29.858 | 29.858 | 29.858 | 29.858–29.858 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 29.778 | 27.128 | 31.256 | 26.466–31.625 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 29.084 | 28.662 | 29.240 | 28.557–29.279 |
| R4_project_title | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 43.360 | 40.408 | 47.877 | 39.791–48.838 |
| R4_project_title | warm | real_2692 | 2692 | close_book | PASS | 10 | 22.838 | 20.222 | 28.327 | 16.609–30.434 |
| R4_project_title | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.197 | 8.018 | 8.422 | 7.951–8.782 |
| R4_project_title | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.278 | 22.862 | 29.681 | 22.484–33.730 |
| R4_project_title | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 7.902 | 7.058 | 8.268 | 6.765–8.339 |
| R4_project_title | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 25.716 | 23.967 | 28.523 | 23.253–31.677 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 46.791 | 43.630 | 53.975 | 43.596–54.765 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 17.495 | 9.332 | 19.593 | 8.967–20.147 |
| R4_project_title | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 7.725 | 7.207 | 8.433 | 6.994–9.126 |
| R4_project_title | warm | real_2692 | 2692 | open_book | PASS | 10 | 52.861 | 48.484 | 61.900 | 42.351–79.565 |
| R4_project_title | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 105.814 | 58.170 | 119.017 | 56.143–171.609 |
| R4_project_title | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.139 | 7.984 | 8.566 | 7.870–9.166 |
| R4_project_title | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 251.674 | 251.674 | 251.674 | 251.674–251.674 |
| R5_vos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 18.178 | 15.903 | 31.051 | 13.816–33.318 |
| R5_vos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 15.973 | 14.466 | 26.660 | 11.252–31.510 |
| R5_vos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 25.487 | 23.584 | 27.141 | 23.108–27.554 |
| R5_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 45.449 | 45.449 | 45.449 | 45.449–45.449 |
| R5_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 48.745 | 48.745 | 48.745 | 48.745–48.745 |
| R5_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 42.593 | 41.933 | 43.153 | 41.768–43.293 |
| R5_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 41.118 | 40.853 | 41.220 | 40.787–41.245 |
| R5_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 63.898 | 46.552 | 96.276 | 45.830–96.767 |
| R5_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 44.248 | 39.749 | 49.935 | 35.549–50.206 |
| R5_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.698 | 7.450 | 9.304 | 7.438–9.552 |
| R5_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 42.728 | 41.587 | 48.760 | 41.150–52.103 |
| R5_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 10.114 | 8.052 | 22.803 | 6.756–27.137 |
| R5_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 42.812 | 41.406 | 49.447 | 41.203–57.379 |
| R5_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 56.578 | 50.099 | 94.191 | 46.855–96.572 |
| R5_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 19.959 | 13.332 | 28.628 | 12.682–41.179 |
| R5_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 11.494 | 9.821 | 25.855 | 9.175–27.775 |
| R5_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 117.975 | 110.886 | 137.502 | 108.357–137.729 |
| R5_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 140.151 | 127.511 | 189.776 | 122.804–201.243 |
| R5_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.440 | 8.056 | 9.198 | 7.686–9.221 |
| R5_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 708.333 | 708.333 | 708.333 | 708.333–708.333 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 171.526 | 162.100 | 195.331 | 160.071–214.378 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 16.249 | 8.932 | 19.655 | 8.228–30.145 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 173.165 | 169.587 | 199.804 | 167.997–204.321 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 31.087 | 26.221 | 41.167 | 9.271–55.452 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 19.886 | 19.100 | 21.405 | 18.903–21.785 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 32.108 | 10.614 | 51.554 | 9.520–58.074 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 18.574 | 16.549 | 33.564 | 11.076–37.834 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 135.414 | 134.216 | 137.212 | 133.917–137.662 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 14.235 | 12.743 | 14.609 | 12.370–14.702 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 42.253 | 42.253 | 42.253 | 42.253–42.253 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 131.512 | 131.512 | 131.512 | 131.512–131.512 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 33.692 | 32.607 | 33.943 | 32.336–34.006 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 114.340 | 110.741 | 115.123 | 109.841–115.319 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 176.623 | 165.907 | 185.496 | 164.539–191.046 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 18.680 | 11.639 | 24.198 | 9.705–24.981 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 28.019 | 24.897 | 88.814 | 22.821–95.278 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 191.111 | 174.987 | 203.764 | 173.662–251.016 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 40.679 | 31.960 | 60.036 | 21.898–79.131 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 98.383 | 69.883 | 117.090 | 67.966–133.765 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 222.972 | 214.965 | 227.546 | 211.549–227.567 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 21.085 | 18.638 | 85.618 | 18.204–93.096 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 10.351 | 9.126 | 24.788 | 9.059–138.742 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 27.261 | 25.512 | 41.126 | 25.341–48.848 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 10.277 | 7.632 | 41.062 | 6.710–44.269 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 101.936 | 56.541 | 119.201 | 37.040–143.394 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 101.453 | 68.116 | 114.255 | 67.885–114.828 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 35.222 | 25.178 | 66.061 | 24.471–75.438 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 14.755 | 13.206 | 44.037 | 9.137–46.396 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 116.392 | 103.148 | 207.655 | 99.565–211.396 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 136.887 | 97.302 | 167.100 | 86.061–200.125 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 27.866 | 26.935 | 30.702 | 25.673–31.970 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 19.163 | 17.620 | 33.473 | 17.048–147.607 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1516.866 | 1516.866 | 1516.866 | 1516.866–1516.866 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 10.226 | 8.689 | 17.197 | 8.536–23.436 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 166.561 | 160.633 | 170.258 | 159.349–178.062 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 15.373 | 9.477 | 19.322 | 8.804–28.236 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 178.183 | 171.827 | 190.347 | 166.883–265.498 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 22.776 | 17.893 | 28.302 | 8.869–39.043 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 11.982 | 10.438 | 12.408 | 10.052–12.514 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 12.789 | 8.094 | 26.812 | 6.758–30.853 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 8.500 | 7.527 | 11.811 | 5.739–29.351 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 154.702 | 151.474 | 159.986 | 150.667–161.307 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 34.508 | 24.687 | 36.213 | 22.232–36.639 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 120.837 | 120.837 | 120.837 | 120.837–120.837 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 50.791 | 50.791 | 50.791 | 50.791–50.791 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 110.155 | 107.955 | 110.258 | 107.405–110.284 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 50.050 | 49.709 | 50.532 | 49.624–50.652 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 160.563 | 158.867 | 166.065 | 158.228–168.561 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 9.460 | 8.294 | 14.017 | 7.923–15.267 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 16.815 | 14.658 | 54.039 | 14.455–65.198 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 164.680 | 160.003 | 174.013 | 159.060–192.860 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 9.947 | 8.283 | 23.100 | 7.813–34.063 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 54.983 | 43.051 | 69.669 | 41.906–75.442 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 32.522 | 27.417 | 37.932 | 27.299–41.493 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 8.337 | 7.366 | 12.177 | 7.045–14.819 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 17.087 | 16.008 | 23.486 | 15.967–77.580 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 44.672 | 43.671 | 48.628 | 43.372–58.623 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 13.553 | 8.047 | 28.425 | 7.880–30.538 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 52.739 | 48.389 | 59.557 | 47.788–63.621 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 61.998 | 44.298 | 65.314 | 44.057–65.394 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 32.085 | 19.311 | 48.287 | 18.566–65.113 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 8.607 | 7.656 | 23.173 | 6.833–28.749 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 123.906 | 116.932 | 133.418 | 107.960–139.717 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 147.576 | 112.236 | 165.033 | 101.905–189.763 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 14.497 | 12.710 | 18.668 | 12.285–25.909 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 9.145 | 7.866 | 10.732 | 7.285–13.500 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 533.300 | 533.300 | 533.300 | 533.300–533.300 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 9.251 | 8.405 | 12.501 | 7.836–30.745 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 175.250 | 166.897 | 188.818 | 161.302–212.644 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 16.304 | 9.130 | 22.570 | 7.991–37.671 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 176.147 | 170.670 | 190.420 | 168.027–196.752 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 31.675 | 25.917 | 44.525 | 9.570–130.545 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 13.807 | 11.557 | 28.797 | 10.995–32.544 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 19.297 | 16.226 | 34.119 | 14.431–118.385 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 16.767 | 14.668 | 28.573 | 13.076–46.135 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 165.123 | 160.043 | 220.629 | 158.773–234.506 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 26.460 | 24.481 | 28.102 | 23.986–28.512 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 47.850 | 47.850 | 47.850 | 47.850–47.850 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 43.269 | 43.269 | 43.269 | 43.269–43.269 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 42.862 | 40.536 | 44.241 | 39.955–44.586 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 41.055 | 41.023 | 42.120 | 41.015–42.386 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 162.712 | 158.562 | 181.325 | 157.479–187.967 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 10.306 | 8.018 | 15.244 | 7.896–18.493 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 17.642 | 15.130 | 41.924 | 15.044–50.785 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 160.638 | 159.264 | 166.341 | 158.346–245.314 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 22.438 | 17.634 | 29.945 | 9.317–45.032 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 67.147 | 48.965 | 115.949 | 44.523–125.089 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 42.847 | 37.112 | 71.880 | 31.504–73.349 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 7.341 | 6.886 | 7.731 | 6.605–8.058 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.215 | 7.720 | 9.080 | 7.369–9.194 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 43.823 | 41.632 | 47.918 | 41.531–49.557 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.852 | 12.679 | 26.793 | 11.459–30.580 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 44.312 | 42.300 | 53.669 | 41.250–57.487 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 72.641 | 53.807 | 91.095 | 50.489–101.122 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 27.072 | 20.508 | 32.482 | 19.046–51.569 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.288 | 15.267 | 28.003 | 14.686–31.253 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 69.988 | 66.852 | 96.105 | 56.502–99.128 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 136.666 | 93.630 | 165.548 | 80.515–191.357 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 17.734 | 15.523 | 20.415 | 15.256–21.037 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.396 | 7.686 | 8.762 | 7.524–8.866 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 590.515 | 590.515 | 590.515 | 590.515–590.515 |
| R9_simpleui_vos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 28.995 | 8.360 | 48.130 | 4.783–54.851 |
| R9_simpleui_vos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 16.493 | 12.239 | 31.474 | 8.820–35.865 |
| R9_simpleui_vos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 23.763 | 14.829 | 32.727 | 12.595–34.968 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 43.764 | 43.764 | 43.764 | 43.764–43.764 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 110.916 | 110.916 | 110.916 | 110.916–110.916 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 34.758 | 32.784 | 35.664 | 32.290–35.891 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 95.990 | 94.785 | 97.500 | 94.484–97.877 |
| R9_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 89.598 | 53.918 | 107.250 | 53.211–123.595 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 221.656 | 212.527 | 232.821 | 202.109–241.496 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.561 | 8.305 | 9.166 | 8.215–9.476 |
| R9_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 30.763 | 27.966 | 34.554 | 25.942–49.014 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.416 | 10.912 | 46.887 | 9.110–50.782 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 94.364 | 85.319 | 114.080 | 84.447–147.009 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 89.341 | 54.117 | 104.340 | 50.107–104.839 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 36.799 | 31.631 | 76.036 | 25.488–87.251 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 20.297 | 16.033 | 52.137 | 12.924–69.772 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 121.081 | 110.551 | 136.604 | 110.336–172.383 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 147.964 | 104.033 | 178.276 | 82.068–200.733 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 12.393 | 10.490 | 30.043 | 10.256–139.229 |
| R9_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 970.915 | 970.915 | 970.915 | 970.915–970.915 |
| R9_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 9.809 | 8.737 | 18.980 | 8.726–22.544 |
| R0_stock | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 527.557 | 522.006 | 643.028 | 520.618–671.895 |
| R0_stock | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 544.504 | 540.557 | 661.621 | 539.571–690.901 |
| R0_stock | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1833.042 | 1561.077 | 1978.535 | 1493.086–2014.908 |
| R0_stock | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1881.315 | 1607.821 | 2042.976 | 1539.447–2083.391 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 666.025 | 666.025 | 666.025 | 666.025–666.025 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 745.724 | 745.724 | 745.724 | 745.724–745.724 |
| R0_stock | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 755.774 | 755.774 | 755.774 | 755.774–755.774 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 867.297 | 867.297 | 867.297 | 867.297–867.297 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 476.070 | 441.212 | 483.418 | 432.498–485.255 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 547.534 | 512.546 | 554.397 | 503.799–556.113 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 555.423 | 519.957 | 561.528 | 511.091–563.055 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 594.748 | 559.684 | 607.666 | 550.918–610.895 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 459.892 | 459.892 | 459.892 | 459.892–459.892 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1716.917 | 1716.917 | 1716.917 | 1716.917–1716.917 |
| R0_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 16231.944 | 16231.944 | 16231.944 | 16231.944–16231.944 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 17391.798 | 17391.798 | 17391.798 | 17391.798–17391.798 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 662.255 | 655.850 | 713.304 | 654.249–726.067 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 714.421 | 710.384 | 766.605 | 709.375–779.650 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 15192.610 | 15118.746 | 15230.241 | 15100.280–15239.649 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 15237.039 | 15179.322 | 15290.279 | 15164.893–15303.589 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 890.337 | 890.337 | 890.337 | 890.337–890.337 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1052.048 | 1052.048 | 1052.048 | 1052.048–1052.048 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1062.525 | 1062.525 | 1062.525 | 1062.525–1062.525 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1114.959 | 1114.959 | 1114.959 | 1114.959–1114.959 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 610.213 | 609.054 | 618.673 | 608.764–620.788 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 754.156 | 745.828 | 762.243 | 743.745–764.265 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 763.594 | 753.085 | 770.806 | 750.458–772.609 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 812.669 | 801.844 | 818.963 | 799.138–820.537 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 606.152 | 606.152 | 606.152 | 606.152–606.152 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2941.468 | 2941.468 | 2941.468 | 2941.468–2941.468 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 38460.618 | 38460.618 | 38460.618 | 38460.618–38460.618 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 38548.893 | 38548.893 | 38548.893 | 38548.893–38548.893 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 397.171 | 387.389 | 398.222 | 384.944–398.485 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 410.338 | 401.094 | 413.687 | 398.783–414.525 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1131.810 | 1118.160 | 1136.865 | 1114.748–1138.129 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1172.249 | 1158.071 | 1177.353 | 1154.527–1178.629 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 2019.679 | 2019.679 | 2019.679 | 2019.679–2019.679 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2108.275 | 2108.275 | 2108.275 | 2108.275–2108.275 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 2119.262 | 2119.262 | 2119.262 | 2119.262–2119.262 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 2182.260 | 2182.260 | 2182.260 | 2182.260–2182.260 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 674.805 | 672.105 | 719.025 | 671.430–730.080 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 761.894 | 756.954 | 809.339 | 755.719–821.200 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 772.065 | 765.143 | 818.391 | 763.413–829.973 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 814.046 | 809.922 | 859.994 | 808.891–871.481 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 728.874 | 728.874 | 728.874 | 728.874–728.874 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2260.863 | 2260.863 | 2260.863 | 2260.863–2260.863 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 10167.754 | 10167.754 | 10167.754 | 10167.754–10167.754 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 10218.879 | 10218.879 | 10218.879 | 10218.879–10218.879 |
| R1_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 624.017 | 562.062 | 695.653 | 546.573–713.562 |
| R1_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 642.132 | 580.874 | 715.579 | 565.559–733.941 |
| R1_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 14403.530 | 13812.318 | 14428.253 | 13664.515–14434.434 |
| R1_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 14451.072 | 13858.388 | 14474.271 | 13710.217–14480.071 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 654.281 | 654.281 | 654.281 | 654.281–654.281 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 740.587 | 740.587 | 740.587 | 740.587–740.587 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 755.389 | 755.389 | 755.389 | 755.389–755.389 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 858.502 | 858.502 | 858.502 | 858.502–858.502 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 500.097 | 450.147 | 532.270 | 437.659–540.313 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 568.850 | 516.696 | 598.805 | 503.657–606.293 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 576.335 | 524.956 | 605.412 | 512.111–612.681 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 619.891 | 570.005 | 650.701 | 557.534–658.404 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 525.363 | 525.363 | 525.363 | 525.363–525.363 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1789.443 | 1789.443 | 1789.443 | 1789.443–1789.443 |
| R1_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 25323.510 | 25323.510 | 25323.510 | 25323.510–25323.510 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 25406.687 | 25406.687 | 25406.687 | 25406.687–25406.687 |
| R2_simpleui | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 679.125 | 634.578 | 799.103 | 623.442–829.097 |
| R2_simpleui | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 733.711 | 690.014 | 853.744 | 679.090–883.752 |
| R2_simpleui | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 2411.238 | 2345.822 | 2536.248 | 2329.468–2567.500 |
| R2_simpleui | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 2455.764 | 2392.338 | 2581.629 | 2376.481–2613.095 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 787.647 | 787.647 | 787.647 | 787.647–787.647 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 977.835 | 977.835 | 977.835 | 977.835–977.835 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 988.486 | 988.486 | 988.486 | 988.486–988.486 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1036.887 | 1036.887 | 1036.887 | 1036.887–1036.887 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 589.915 | 568.174 | 597.653 | 562.739–599.588 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 746.375 | 727.257 | 758.167 | 722.478–761.115 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 757.457 | 737.799 | 768.501 | 732.885–771.263 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 798.503 | 780.724 | 812.279 | 776.279–815.723 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 683.917 | 683.917 | 683.917 | 683.917–683.917 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 3276.721 | 3276.721 | 3276.721 | 3276.721–3276.721 |
| R2_simpleui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 23759.612 | 23759.612 | 23759.612 | 23759.612–23759.612 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 23996.121 | 23996.121 | 23996.121 | 23996.121–23996.121 |
| R3_zenos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 675.326 | 629.722 | 824.422 | 618.320–861.696 |
| R3_zenos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 777.871 | 730.776 | 922.544 | 719.002–958.712 |
| R3_zenos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1737.489 | 1679.773 | 1878.920 | 1665.345–1914.277 |
| R3_zenos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1780.447 | 1721.663 | 1924.245 | 1706.968–1960.195 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 844.031 | 844.031 | 844.031 | 844.031–844.031 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1030.284 | 1030.284 | 1030.284 | 1030.284–1030.284 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1044.152 | 1044.152 | 1044.152 | 1044.152–1044.152 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1086.250 | 1086.250 | 1086.250 | 1086.250–1086.250 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 587.519 | 533.164 | 607.674 | 519.575–612.713 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 753.569 | 701.596 | 771.638 | 688.603–776.156 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 768.366 | 716.329 | 786.673 | 703.319–791.249 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 815.949 | 761.501 | 829.444 | 747.890–832.818 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 597.770 | 597.770 | 597.770 | 597.770–597.770 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2318.970 | 2318.970 | 2318.970 | 2318.970–2318.970 |
| R3_zenos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 13471.534 | 13471.534 | 13471.534 | 13471.534–13471.534 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 13530.676 | 13530.676 | 13530.676 | 13530.676–13530.676 |
| R4_project_title | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 539.472 | 508.792 | 539.801 | 501.122–539.883 |
| R4_project_title | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 552.900 | 520.961 | 553.326 | 512.976–553.432 |
| R4_project_title | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1310.977 | 1280.373 | 1313.689 | 1272.722–1314.367 |
| R4_project_title | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1355.980 | 1321.283 | 1357.574 | 1312.609–1357.973 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 494.603 | 494.603 | 494.603 | 494.603–494.603 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 562.689 | 562.689 | 562.689 | 562.689–562.689 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 570.756 | 570.756 | 570.756 | 570.756–570.756 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 611.738 | 611.738 | 611.738 | 611.738–611.738 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 436.439 | 431.969 | 446.421 | 430.851–448.916 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 504.177 | 495.414 | 512.132 | 493.224–514.121 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 512.408 | 503.367 | 519.659 | 501.107–521.472 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 550.671 | 545.988 | 558.495 | 544.817–560.451 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 433.531 | 433.531 | 433.531 | 433.531–433.531 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1416.001 | 1416.001 | 1416.001 | 1416.001–1416.001 |
| R4_project_title | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 8356.098 | 8356.098 | 8356.098 | 8356.098–8356.098 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 8403.611 | 8403.611 | 8403.611 | 8403.611–8403.611 |
| R5_vos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 545.564 | 544.089 | 648.960 | 543.720–674.809 |
| R5_vos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 566.045 | 564.346 | 672.012 | 563.922–698.503 |
| R5_vos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1954.840 | 1949.524 | 2093.048 | 1948.195–2127.600 |
| R5_vos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 2009.351 | 2007.849 | 2154.816 | 2007.473–2191.182 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 676.539 | 676.539 | 676.539 | 676.539–676.539 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 781.156 | 781.156 | 781.156 | 781.156–781.156 |
| R5_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 791.045 | 791.045 | 791.045 | 791.045–791.045 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 895.317 | 895.317 | 895.317 | 895.317–895.317 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 471.385 | 465.530 | 476.491 | 464.066–477.768 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 561.867 | 556.716 | 569.224 | 555.428–571.064 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 569.683 | 564.882 | 576.780 | 563.682–578.554 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 610.597 | 606.391 | 616.788 | 605.340–618.336 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 475.624 | 475.624 | 475.624 | 475.624–475.624 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2133.525 | 2133.525 | 2133.525 | 2133.525–2133.525 |
| R5_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 14233.680 | 14233.680 | 14233.680 | 14233.680–14233.680 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 14418.171 | 14418.171 | 14418.171 | 14418.171–14418.171 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 799.380 | 754.659 | 837.813 | 743.479–847.421 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 858.671 | 811.781 | 892.599 | 800.059–901.081 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 15393.245 | 15375.105 | 15475.727 | 15370.570–15496.347 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 15446.775 | 15436.345 | 15537.127 | 15433.737–15559.714 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 836.882 | 836.882 | 836.882 | 836.882–836.882 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1022.167 | 1022.167 | 1022.167 | 1022.167–1022.167 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1033.651 | 1033.651 | 1033.651 | 1033.651–1033.651 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1076.162 | 1076.162 | 1076.162 | 1076.162–1076.162 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 608.538 | 581.690 | 635.551 | 574.979–642.304 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 766.831 | 735.435 | 794.901 | 727.586–801.919 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 777.628 | 745.826 | 806.224 | 737.876–813.373 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 818.319 | 787.291 | 849.219 | 779.534–856.945 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 673.812 | 673.812 | 673.812 | 673.812–673.812 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2898.021 | 2898.021 | 2898.021 | 2898.021–2898.021 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 38709.499 | 38709.499 | 38709.499 | 38709.499–38709.499 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 38791.029 | 38791.029 | 38791.029 | 38791.029–38791.029 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 686.635 | 651.263 | 725.690 | 642.420–735.454 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 776.246 | 754.176 | 823.214 | 748.658–834.957 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 13982.169 | 13939.040 | 14140.528 | 13928.258–14180.118 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 14035.579 | 13989.630 | 14194.170 | 13978.143–14233.818 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 837.585 | 837.585 | 837.585 | 837.585–837.585 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1030.814 | 1030.814 | 1030.814 | 1030.814–1030.814 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1045.511 | 1045.511 | 1045.511 | 1045.511–1045.511 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1110.843 | 1110.843 | 1110.843 | 1110.843–1110.843 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 617.392 | 612.779 | 640.439 | 611.626–646.201 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 788.346 | 781.944 | 810.536 | 780.343–816.084 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 802.992 | 796.041 | 825.813 | 794.303–831.518 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 845.074 | 842.548 | 867.424 | 841.916–873.011 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 603.665 | 603.665 | 603.665 | 603.665–603.665 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2705.801 | 2705.801 | 2705.801 | 2705.801–2705.801 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 26406.062 | 26406.062 | 26406.062 | 26406.062–26406.062 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 26478.795 | 26478.795 | 26478.795 | 26478.795–26478.795 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 1090.718 | 808.209 | 1534.281 | 737.582–1645.171 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 1111.864 | 829.322 | 1565.404 | 758.687–1678.789 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 15824.380 | 15219.356 | 16465.150 | 15068.101–16625.342 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 16689.581 | 15428.851 | 17872.698 | 15113.669–18168.478 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 747.950 | 747.950 | 747.950 | 747.950–747.950 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 849.116 | 849.116 | 849.116 | 849.116–849.116 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 860.628 | 860.628 | 860.628 | 860.628–860.628 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 931.817 | 931.817 | 931.817 | 931.817–931.817 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 537.556 | 528.465 | 541.255 | 526.192–542.179 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 624.733 | 619.199 | 633.644 | 617.815–635.871 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 632.246 | 628.143 | 640.849 | 627.117–643.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 673.090 | 668.903 | 683.321 | 667.856–685.878 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 518.404 | 518.404 | 518.404 | 518.404–518.404 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2190.522 | 2190.522 | 2190.522 | 2190.522–2190.522 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 26408.033 | 26408.033 | 26408.033 | 26408.033–26408.033 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 26608.699 | 26608.699 | 26608.699 | 26608.699–26608.699 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 719.233 | 698.203 | 784.653 | 692.945–801.008 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 774.038 | 752.099 | 837.780 | 746.614–853.716 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 2520.064 | 2375.366 | 2529.265 | 2339.191–2531.565 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 2565.336 | 2422.353 | 2572.891 | 2386.608–2574.780 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 826.501 | 826.501 | 826.501 | 826.501–826.501 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 991.628 | 991.628 | 991.628 | 991.628–991.628 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1000.095 | 1000.095 | 1000.095 | 1000.095–1000.095 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1048.921 | 1048.921 | 1048.921 | 1048.921–1048.921 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 603.789 | 558.382 | 606.006 | 547.030–606.561 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 742.012 | 699.500 | 747.761 | 688.872–749.199 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 751.026 | 709.500 | 756.642 | 699.119–758.046 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 792.225 | 753.299 | 803.908 | 743.568–806.829 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 540.089 | 540.089 | 540.089 | 540.089–540.089 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2808.353 | 2808.353 | 2808.353 | 2808.353–2808.353 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 22935.633 | 22935.633 | 22935.633 | 22935.633–22935.633 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 23231.007 | 23231.007 | 23231.007 | 23231.007–23231.007 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R0_stock | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 8922.796 | 8995.777 | 8922.011–9014.022 | 11610.932 | 168880.000 |
| R0_stock | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 9584.737 | 10398.472 | 9573.272–10601.905 | 13816.674 | 195136.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 8939.765 | 8939.765 | 8939.765–8939.765 | 11287.496 | 165024.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10242.737 | 10242.737 | 10242.737–10242.737 | 14753.088 | 174016.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9241.132 | 9247.979 | 9197.804–9249.690 | 14646.275 | 161152.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9266.011 | 9287.748 | 9242.116–9293.183 | 15188.285 | 170640.000 |
| R0_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9285.022 | 9285.022 | 9285.022–9285.022 | 15866.401 | 165344.000 |
| R0_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9238.370 | 9238.370 | 9238.370–9238.370 | 12545.806 | 183472.000 |
| R0_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 27272.034 | 27272.034 | 27272.034–27272.034 | 29819.051 | 347584.000 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13994.024 | 13996.437 | 13937.524–13997.040 | 15699.188 | 178048.000 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 18890.587 | 18929.209 | 18871.489–18938.864 | 29503.503 | 246592.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14018.853 | 14018.853 | 14018.853–14018.853 | 18220.905 | 172272.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14690.739 | 14690.739 | 14690.739–14690.739 | 16036.681 | 184192.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13932.838 | 14208.444 | 13912.549–14277.346 | 22825.205 | 172320.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 14598.154 | 14851.914 | 14572.072–14915.354 | 15751.169 | 183216.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13916.936 | 13916.936 | 13916.936–13916.936 | 23290.830 | 172640.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 21989.333 | 21989.333 | 21989.333–21989.333 | 24702.218 | 202400.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 73525.225 | 73525.225 | 73525.225–73525.225 | 73601.221 | 362208.000 |
| R11_project_title_vos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10278.255 | 10305.030 | 10274.138–10311.724 | 14291.847 | 168160.000 |
| R11_project_title_vos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 11026.106 | 11031.244 | 11011.380–11032.528 | 22910.944 | 202752.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10352.368 | 10352.368 | 10352.368–10352.368 | 14376.783 | 166224.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10368.087 | 10368.087 | 10368.087–10368.087 | 17058.890 | 175824.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10329.380 | 10385.924 | 10257.950–10400.060 | 11757.215 | 167264.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10270.173 | 10355.942 | 10261.438–10377.384 | 17082.938 | 175344.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10362.255 | 10362.255 | 10362.255–10362.255 | 12166.518 | 165136.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10387.962 | 10387.962 | 10387.962–10387.962 | 19747.867 | 183616.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14981.693 | 14981.693 | 14981.693–14981.693 | 33668.445 | 318960.000 |
| R1_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9503.845 | 9583.870 | 9414.169–9603.876 | 13458.229 | 168032.000 |
| R1_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 14061.443 | 14351.796 | 14040.686–14424.385 | 22615.714 | 236384.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9443.985 | 9443.985 | 9443.985–9443.985 | 10927.195 | 167616.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10645.220 | 10645.220 | 10645.220–10645.220 | 15324.086 | 176352.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9341.177 | 9345.677 | 9165.817–9346.802 | 11401.897 | 164176.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9385.817 | 9418.380 | 9172.864–9426.521 | 15240.360 | 173984.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9299.978 | 9299.978 | 9299.978–9299.978 | 13275.183 | 166464.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9362.192 | 9362.192 | 9362.192–9362.192 | 12707.544 | 185792.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 18040.291 | 18040.291 | 18040.291–18040.291 | 20218.785 | 317008.000 |
| R2_simpleui | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13199.054 | 13202.122 | 13123.245–13202.890 | 16861.826 | 178368.000 |
| R2_simpleui | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 14500.140 | 15899.293 | 14411.233–16249.081 | 18437.380 | 200912.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13195.175 | 13195.175 | 13195.175–13195.175 | 17613.874 | 173936.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 13949.507 | 13949.507 | 13949.507–13949.507 | 17187.727 | 181760.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13190.492 | 13228.942 | 13188.812–13238.555 | 21821.878 | 174912.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 13995.504 | 14009.988 | 13949.027–14013.609 | 17181.392 | 182560.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13160.988 | 13160.988 | 13160.988–13160.988 | 22839.689 | 172480.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 19241.961 | 19241.961 | 19241.961–19241.961 | 19466.187 | 198528.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 62620.440 | 62620.440 | 62620.440–62620.440 | 62663.390 | 352592.000 |
| R3_zenos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14272.892 | 14294.307 | 14191.767–14299.661 | 15626.159 | 175216.000 |
| R3_zenos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 15745.181 | 15763.890 | 15734.821–15768.567 | 16492.566 | 208656.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14188.798 | 14188.798 | 14188.798–14188.798 | 15605.112 | 171648.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15779.399 | 15779.399 | 15779.399–15779.399 | 26458.126 | 189824.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14276.861 | 14294.543 | 14217.111–14298.963 | 21658.169 | 172000.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 15704.643 | 15768.343 | 15673.748–15784.268 | 26256.839 | 187408.000 |
| R3_zenos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14268.541 | 14268.541 | 14268.541–14268.541 | 21851.674 | 177680.000 |
| R3_zenos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16917.333 | 16917.333 | 16917.333–16917.333 | 17438.244 | 203584.000 |
| R3_zenos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 38051.056 | 38051.056 | 38051.056–38051.056 | 39346.734 | 349232.000 |
| R4_project_title | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9191.302 | 9202.477 | 9079.126–9205.271 | 11298.758 | 167392.000 |
| R4_project_title | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 9819.915 | 9837.324 | 9814.138–9841.677 | 23170.504 | 197840.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9167.985 | 9167.985 | 9167.985–9167.985 | 11482.909 | 167680.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9138.978 | 9138.978 | 9138.978–9138.978 | 15295.822 | 176192.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9351.478 | 9387.803 | 9322.208–9396.884 | 14918.543 | 165200.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9412.118 | 9443.746 | 9380.731–9451.653 | 15378.562 | 173680.000 |
| R4_project_title | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9645.853 | 9645.853 | 9645.853–9645.853 | 10108.199 | 166304.000 |
| R4_project_title | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9775.005 | 9775.005 | 9775.005–9775.005 | 24917.010 | 184880.000 |
| R4_project_title | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14848.162 | 14848.162 | 14848.162–14848.162 | 25211.920 | 315104.000 |
| R5_vos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10220.030 | 10249.124 | 10133.757–10256.397 | 14047.413 | 169232.000 |
| R5_vos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 10812.538 | 10827.197 | 10750.995–10830.862 | 15422.418 | 194832.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10134.503 | 10134.503 | 10134.503–10134.503 | 13826.523 | 166512.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11385.897 | 11385.897 | 11385.897–11385.897 | 16497.659 | 175840.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10119.081 | 10129.981 | 10111.054–10132.706 | 11897.995 | 167552.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10127.909 | 10155.584 | 10123.815–10162.503 | 16717.498 | 175408.000 |
| R5_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10163.593 | 10163.593 | 10163.593–10163.593 | 11663.608 | 166592.000 |
| R5_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10171.784 | 10171.784 | 10171.784–10171.784 | 16721.170 | 185184.000 |
| R5_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 29683.784 | 29683.784 | 29683.784–29683.784 | 30269.404 | 353424.000 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13343.239 | 13388.689 | 13328.235–13400.052 | 18078.247 | 177616.000 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 18232.126 | 18234.113 | 18225.919–18234.610 | 30123.017 | 243776.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13416.981 | 13416.981 | 13416.981–13416.981 | 18169.220 | 174704.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14211.919 | 14211.919 | 14211.919–14211.919 | 17512.825 | 182480.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13264.225 | 13326.621 | 13225.693–13342.221 | 22255.093 | 175744.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 14109.252 | 14736.821 | 14095.959–14893.713 | 17271.688 | 184400.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13252.432 | 13252.432 | 13252.432–13252.432 | 23040.913 | 176832.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 21145.161 | 21145.161 | 21145.161–21145.161 | 31103.542 | 204016.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 68729.127 | 68729.127 | 68729.127–68729.127 | 68775.264 | 479232.000 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14482.979 | 14531.476 | 14439.132–14543.601 | 16125.349 | 176320.000 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 19714.427 | 19754.858 | 19676.110–19764.966 | 25591.521 | 262336.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14454.792 | 14454.792 | 14454.792–14454.792 | 16994.466 | 171664.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15971.144 | 15971.144 | 15971.144–15971.144 | 26824.966 | 186416.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14362.078 | 14409.981 | 14359.887–14421.957 | 22078.861 | 175168.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 15884.457 | 16240.582 | 15817.980–16329.613 | 26595.076 | 187952.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14452.727 | 14452.727 | 14452.727–14452.727 | 22661.466 | 176368.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16511.158 | 16511.158 | 16511.158–16511.158 | 22524.421 | 204848.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 41713.188 | 41713.188 | 41713.188–41713.188 | 43196.257 | 385360.000 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10401.173 | 10486.592 | 10305.974–10507.946 | 15491.012 | 166592.000 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 15026.446 | 15034.640 | 15003.981–15036.688 | 33622.510 | 221456.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10358.849 | 10358.849 | 10358.849–10358.849 | 15424.932 | 166672.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11644.106 | 11644.106 | 11644.106–11644.106 | 16881.729 | 177056.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10312.470 | 10312.882 | 10265.349–10312.985 | 12257.277 | 166784.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10306.923 | 10339.788 | 10215.896–10348.005 | 16860.794 | 175712.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10271.181 | 10271.181 | 10271.181–10271.181 | 12090.925 | 169248.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10335.591 | 10335.591 | 10335.591–10335.591 | 19756.314 | 190672.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 27180.025 | 27180.025 | 27180.025–27180.025 | 32551.775 | 355168.000 |
| R9_simpleui_vos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13821.655 | 13833.115 | 13772.847–13835.979 | 16355.318 | 177280.000 |
| R9_simpleui_vos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 15097.362 | 15531.369 | 15088.687–15639.870 | 17887.175 | 198032.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13766.952 | 13766.952 | 13766.952–13766.952 | 17058.232 | 174112.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14567.073 | 14567.073 | 14567.073–14567.073 | 15903.477 | 185376.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13772.551 | 13786.820 | 13750.203–13790.387 | 22110.875 | 174768.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 14550.113 | 14551.501 | 14496.277–14551.848 | 15798.463 | 184720.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13809.859 | 13809.859 | 13809.859–13809.859 | 22656.853 | 174256.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 21810.051 | 21810.051 | 21810.051–21810.051 | 24469.038 | 201856.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 68998.491 | 68998.491 | 68998.491–68998.491 | 79361.656 | 365968.000 |

## Data-derived comparisons

- `R0_stock` has a lower descriptive median than `R1_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 16.811 ms vs 16.931 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R1_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 14.260 ms vs 14.708 ms (3.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 15.732 ms vs 16.328 ms (3.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.980 ms vs 28.045 ms (39.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (paging, real_2692, 2692 books): 16.811 ms vs 28.634 ms (41.3% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 14.260 ms vs 16.415 ms (13.1% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 14.061 ms vs 16.328 ms (13.9% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.979 ms vs 28.045 ms (39.5% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 12.864 ms vs 16.811 ms (23.5% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 8.605 ms vs 14.260 ms (39.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 8.009 ms vs 16.328 ms (50.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 8.111 ms vs 28.045 ms (71.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 8.977 ms vs 16.811 ms (46.6% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 9.072 ms vs 14.260 ms (36.4% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 7.902 ms vs 16.328 ms (51.6% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 7.725 ms vs 28.045 ms (72.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R0_stock` has a lower descriptive median than `R5_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 16.811 ms vs 18.178 ms (7.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R5_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 14.260 ms vs 15.973 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 10.114 ms vs 16.328 ms (38.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.494 ms vs 28.045 ms (59.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 28.634 ms vs 32.108 ms (10.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R6_simpleui_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 16.415 ms vs 18.574 ms (11.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 10.277 ms vs 14.061 ms (26.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 14.755 ms vs 16.979 ms (13.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (paging, real_2692, 2692 books): 12.789 ms vs 12.864 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_sequential_paging` (paging, real_2692, 2692 books): 8.500 ms vs 8.605 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 8.009 ms vs 13.553 ms (40.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 8.111 ms vs 8.607 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 18.178 ms vs 19.297 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 15.973 ms vs 16.767 ms (4.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 10.114 ms vs 14.852 ms (31.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.494 ms vs 16.288 ms (29.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 28.634 ms vs 28.995 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 16.415 ms vs 16.493 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 14.061 ms vs 16.416 ms (14.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 16.979 ms vs 20.297 ms (16.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 28.995 ms vs 32.198 ms (10.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 16.493 ms vs 17.593 ms (6.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 16.416 ms vs 16.988 ms (3.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 18.524 ms vs 20.297 ms (8.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (paging, real_2692, 2692 books): 8.478 ms vs 8.977 ms (5.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (paging, real_2692, 2692 books): 8.719 ms vs 9.072 ms (3.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R11_project_title_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 7.902 ms vs 9.142 ms (13.6% lower).
- `R4_project_title` has a lower descriptive median than `R11_project_title_vos` for `library_sequential_paging` (warm, real_2692, 2692 books): 7.725 ms vs 9.195 ms (16.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
