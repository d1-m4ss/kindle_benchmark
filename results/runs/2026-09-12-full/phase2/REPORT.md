# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `b7aa678f5eef72bc810dedd92ebabb1d9973e5a3d10230e9401af28e1a995ad4`
Reader flash setting: `unset`

Aggregated rows: 663; PASS=656; FAILED=0; UNSUPPORTED=7; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R0_stock | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 20.370 | 31.572 | 16.505 | 34.625 | 23.902 | 35.871 | 19.151 | 39.670 |
| R0_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 21.489 | 35.328 | 17.605 | 38.332 | 21.023 | 33.398 | 16.510 | 40.060 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 21.083 | 39.260 | 15.891 | 43.980 | 42.026 | 66.535 | 13.086 | 70.047 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 22.769 | 57.449 | 15.152 | 89.765 | 19.111 | 44.395 | 13.352 | 48.875 |
| R11_project_title_vos | paging | real_2692 | 2692 | 14 | 37.000 | 3/3 | 90/90 | 11.857 | 14.311 | 8.782 | 19.742 | 11.960 | 14.401 | 9.210 | 19.865 |
| R11_project_title_vos | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 12.254 | 13.856 | 10.744 | 18.856 | 12.206 | 14.423 | 9.707 | 18.024 |
| R12_leanui | paging | real_2692 | 2692 | 14 | 37.000 | 3/3 | 90/90 | 12.630 | 15.245 | 9.452 | 19.789 | 13.006 | 15.452 | 8.321 | 20.546 |
| R12_leanui | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 12.921 | 14.097 | 10.251 | 20.180 | 12.739 | 15.203 | 9.523 | 17.153 |
| R1_bookshelf | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 20.334 | 31.796 | 16.586 | 34.086 | 23.256 | 35.075 | 18.056 | 39.119 |
| R1_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 20.679 | 31.729 | 12.680 | 38.034 | 10.990 | 23.013 | 9.147 | 28.773 |
| R2_simpleui | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 23.386 | 41.184 | 16.686 | 44.533 | 35.642 | 67.718 | 13.338 | 73.196 |
| R2_simpleui | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 27.109 | 58.344 | 18.581 | 69.657 | 22.848 | 51.788 | 13.128 | 60.914 |
| R3_zenos | paging | real_2692 | 2692 | 5 | 101.000 | 3/3 | 90/90 | 11.005 | 26.392 | 8.729 | 34.252 | 18.312 | 30.672 | 9.782 | 40.040 |
| R3_zenos | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 11.037 | 25.151 | 8.392 | 27.418 | 19.318 | 30.206 | 9.544 | 37.854 |
| R4_project_title | paging | real_2692 | 2692 | 14 | 37.000 | 3/3 | 90/90 | 12.465 | 14.620 | 9.190 | 19.794 | 12.691 | 15.322 | 9.601 | 19.612 |
| R4_project_title | warm | real_2692 | 2692 | 14 | 37.000 | 1/1 | 30/30 | 13.005 | 15.421 | 9.547 | 17.682 | 12.448 | 15.237 | 10.007 | 17.583 |
| R5_vos | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 20.558 | 32.381 | 17.254 | 35.479 | 23.668 | 36.284 | 17.077 | 41.027 |
| R5_vos | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 13.941 | 25.960 | 10.623 | 35.145 | 20.383 | 34.003 | 10.475 | 35.894 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 22.314 | 39.694 | 16.317 | 43.923 | 34.627 | 68.463 | 13.811 | 82.852 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 24.218 | 50.443 | 17.684 | 55.543 | 20.842 | 47.705 | 12.969 | 54.432 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | 5 | 101.000 | 3/3 | 90/90 | 11.375 | 27.678 | 8.933 | 38.590 | 17.830 | 31.832 | 9.740 | 39.790 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | 5 | 101.000 | 1/1 | 30/30 | 11.186 | 25.772 | 9.205 | 30.574 | 17.985 | 29.458 | 10.214 | 38.045 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | 10 | 51.000 | 3/3 | 90/90 | 21.001 | 34.147 | 14.955 | 37.883 | 24.057 | 37.296 | 18.291 | 41.922 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 21.351 | 34.563 | 14.472 | 36.832 | 12.440 | 26.694 | 9.510 | 28.244 |
| R9_simpleui_vos | paging | real_2692 | 2692 | 8 | 64.000 | 3/3 | 90/90 | 21.654 | 39.627 | 15.037 | 44.155 | 42.054 | 66.244 | 13.349 | 69.246 |
| R9_simpleui_vos | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 18.941 | 52.056 | 12.526 | 54.463 | 12.879 | 44.926 | 9.658 | 53.465 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 88.821 | 106.083 | 80.553 | 131.350 | 87.569 | 104.207 | 79.016 | 129.888 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 29.624 | 37.048 | 22.404 | 95.920 | 35.361 | 48.309 | 20.476 | 93.330 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 90.916 | 115.815 | 85.417 | 171.643 | 115.506 | 138.442 | 83.307 | 271.432 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 49.376 | 66.569 | 36.101 | 162.957 | 36.224 | 44.456 | 16.733 | 185.029 |
| R1_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 88.376 | 95.912 | 81.046 | 105.091 | 87.946 | 94.533 | 80.136 | 108.459 |
| R1_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 30.795 | 35.554 | 22.170 | 48.940 | 29.841 | 37.044 | 20.509 | 47.624 |
| R1_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 84.213 | 95.135 | 77.757 | 110.555 | 83.957 | 95.555 | 76.102 | 121.736 |
| R1_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 25.733 | 31.431 | 17.467 | 45.407 | 28.345 | 43.954 | 16.655 | 64.812 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 88.786 | 104.440 | 80.277 | 133.882 | 88.256 | 103.495 | 78.795 | 141.644 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 29.325 | 38.715 | 22.908 | 97.170 | 40.160 | 60.201 | 21.947 | 96.249 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 92.298 | 102.484 | 85.650 | 192.127 | 104.084 | 126.077 | 83.025 | 231.862 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 48.622 | 62.277 | 32.633 | 161.032 | 37.981 | 48.650 | 19.950 | 155.836 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 95.867 | 106.618 | 84.849 | 121.073 | 82.083 | 94.590 | 71.797 | 108.568 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 34.261 | 42.479 | 14.228 | 66.811 | 23.069 | 29.159 | 12.658 | 45.305 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 74.742 | 93.007 | 70.700 | 148.825 | 75.513 | 87.138 | 66.775 | 123.925 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 15.418 | 35.209 | 8.762 | 62.198 | 13.479 | 32.503 | 7.851 | 57.989 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | default (medium) | 8 | 64.000 | 3/3 | 90/90 | 87.927 | 96.253 | 82.760 | 103.915 | 87.115 | 94.768 | 79.391 | 104.538 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | off | 8 | 64.000 | 3/3 | 90/90 | 29.623 | 36.628 | 22.369 | 45.176 | 28.983 | 37.121 | 20.544 | 47.010 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | default (medium) | 8 | 64.000 | 1/1 | 30/30 | 72.484 | 85.309 | 69.561 | 164.741 | 74.648 | 82.784 | 67.333 | 97.407 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | off | 8 | 64.000 | 1/1 | 30/30 | 12.125 | 16.269 | 9.211 | 33.220 | 12.422 | 23.756 | 7.641 | 34.392 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R0_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R11_project_title_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R12_leanui | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R1_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R4_project_title | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R5_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R8_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 23.256 ms vs 23.902 ms (2.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.334 ms vs 20.370 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 10.990 ms vs 21.023 ms (47.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 20.679 ms vs 21.489 ms (3.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (paging, real_2692, 2692 books): 23.902 ms vs 35.642 ms (32.9% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.370 ms vs 23.386 ms (12.9% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 21.023 ms vs 22.848 ms (8.0% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 21.489 ms vs 27.109 ms (20.7% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 18.312 ms vs 23.902 ms (23.4% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 11.005 ms vs 20.370 ms (46.0% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 19.318 ms vs 21.023 ms (8.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.037 ms vs 21.489 ms (48.6% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 12.691 ms vs 23.902 ms (46.9% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 12.465 ms vs 20.370 ms (38.8% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 12.448 ms vs 21.023 ms (40.8% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 13.005 ms vs 21.489 ms (39.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 23.668 ms vs 23.902 ms (1.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R5_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.370 ms vs 20.558 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 20.383 ms vs 21.023 ms (3.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 13.941 ms vs 21.489 ms (35.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (paging, real_2692, 2692 books): 34.627 ms vs 35.642 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 22.314 ms vs 23.386 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 20.842 ms vs 22.848 ms (8.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 24.218 ms vs 27.109 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (paging, real_2692, 2692 books): 17.830 ms vs 18.312 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 11.005 ms vs 11.375 ms (3.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 17.985 ms vs 19.318 ms (6.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.037 ms vs 11.186 ms (1.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 23.668 ms vs 24.057 ms (1.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.558 ms vs 21.001 ms (2.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R8_vos_bookshelf` has a lower descriptive median than `R5_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 12.440 ms vs 20.383 ms (39.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 13.941 ms vs 21.351 ms (34.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 35.642 ms vs 42.054 ms (15.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 21.654 ms vs 23.386 ms (7.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 12.879 ms vs 22.848 ms (43.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 18.941 ms vs 27.109 ms (30.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 42.026 ms vs 42.054 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 21.083 ms vs 21.654 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 12.879 ms vs 19.111 ms (32.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 18.941 ms vs 22.769 ms (16.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (paging, real_2692, 2692 books): 11.960 ms vs 12.691 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (paging, real_2692, 2692 books): 11.857 ms vs 12.465 ms (4.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (warm, real_2692, 2692 books): 12.206 ms vs 12.448 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (warm, real_2692, 2692 books): 12.254 ms vs 13.005 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R0_stock | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 23.902 | 21.004 | 35.871 | 19.151–39.670 |
| R0_stock | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 20.370 | 17.973 | 31.572 | 16.505–34.625 |
| R0_stock | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 20.492 | 19.818 | 21.194 | 19.649–21.370 |
| R0_stock | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 44.823 | 44.823 | 44.823 | 44.823–44.823 |
| R0_stock | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 46.911 | 46.911 | 46.911 | 46.911–46.911 |
| R0_stock | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 43.667 | 43.071 | 45.266 | 42.922–45.666 |
| R0_stock | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 42.602 | 42.046 | 42.772 | 41.907–42.815 |
| R0_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 99.335 | 84.965 | 119.899 | 82.107–128.822 |
| R0_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 53.810 | 41.957 | 60.768 | 27.322–71.343 |
| R0_stock | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.228 | 7.882 | 8.713 | 7.878–8.917 |
| R0_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 46.225 | 44.620 | 63.575 | 43.543–65.572 |
| R0_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 21.023 | 18.149 | 33.398 | 16.510–40.060 |
| R0_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 46.742 | 45.136 | 61.832 | 44.321–61.956 |
| R0_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 105.312 | 77.027 | 128.659 | 75.807–140.674 |
| R0_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 36.370 | 32.062 | 80.892 | 25.391–121.348 |
| R0_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 21.489 | 19.372 | 35.328 | 17.605–38.332 |
| R0_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 66.237 | 58.855 | 80.023 | 50.342–100.009 |
| R0_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 152.173 | 75.755 | 179.642 | 66.174–268.961 |
| R0_stock | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.311 | 8.067 | 8.669 | 7.702–8.885 |
| R0_stock | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 526.738 | 526.738 | 526.738 | 526.738–526.738 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 87.569 | 81.257 | 104.207 | 79.016–129.888 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 35.361 | 24.864 | 48.309 | 20.476–93.330 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 88.821 | 83.134 | 106.083 | 80.553–131.350 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 29.624 | 25.169 | 37.048 | 22.404–95.920 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 36.618 | 34.390 | 37.440 | 33.833–37.646 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 42.026 | 15.190 | 66.535 | 13.086–70.047 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 21.083 | 17.496 | 39.260 | 15.891–43.980 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 126.196 | 124.161 | 129.967 | 123.652–130.910 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 17.550 | 16.452 | 18.817 | 16.177–19.134 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 64.723 | 64.723 | 64.723 | 64.723–64.723 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 153.014 | 153.014 | 153.014 | 153.014–153.014 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 48.595 | 46.685 | 52.232 | 46.208–53.141 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 131.159 | 129.497 | 134.580 | 129.081–135.435 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 115.506 | 86.122 | 138.442 | 83.307–271.432 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 36.224 | 21.993 | 44.456 | 16.733–185.029 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 37.910 | 34.413 | 140.915 | 33.985–141.353 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 90.916 | 86.629 | 115.815 | 85.417–171.643 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 49.376 | 39.282 | 66.569 | 36.101–162.957 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 100.250 | 79.105 | 122.152 | 76.605–136.959 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 145.870 | 137.112 | 230.581 | 107.562–236.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 33.745 | 31.673 | 148.843 | 31.641–157.402 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 12.250 | 8.924 | 14.719 | 8.605–14.818 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 46.321 | 45.073 | 63.361 | 44.650–63.992 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 19.111 | 13.835 | 44.395 | 13.352–48.875 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 138.657 | 117.430 | 180.944 | 112.202–203.736 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 91.582 | 74.350 | 123.386 | 74.165–124.584 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 49.022 | 37.134 | 90.853 | 29.817–120.937 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 22.769 | 18.684 | 57.449 | 15.152–89.765 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 189.773 | 166.650 | 213.808 | 157.570–226.463 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 181.972 | 126.980 | 213.872 | 107.086–309.309 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 41.330 | 39.439 | 45.739 | 39.245–56.391 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 45.111 | 38.828 | 244.263 | 37.815–249.682 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 2368.245 | 2368.245 | 2368.245 | 2368.245–2368.245 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 11.852 | 11.166 | 23.030 | 11.098–23.781 |
| R11_project_title_vos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 11.960 | 10.110 | 14.401 | 9.210–19.865 |
| R11_project_title_vos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 11.857 | 10.070 | 14.311 | 8.782–19.742 |
| R11_project_title_vos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 11.228 | 10.918 | 12.114 | 10.841–12.335 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 52.039 | 52.039 | 52.039 | 52.039–52.039 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 48.605 | 48.605 | 48.605 | 48.605–48.605 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 51.883 | 51.701 | 52.022 | 51.656–52.057 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 49.722 | 49.544 | 50.348 | 49.500–50.505 |
| R11_project_title_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 46.264 | 42.889 | 51.234 | 41.666–52.548 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 42.253 | 38.432 | 51.084 | 34.549–52.720 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 13.140 | 10.897 | 15.203 | 10.443–15.430 |
| R11_project_title_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 52.224 | 49.931 | 59.474 | 49.594–60.369 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.206 | 10.332 | 14.423 | 9.707–18.024 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 52.672 | 50.899 | 60.250 | 50.412–61.241 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 61.335 | 58.744 | 66.887 | 57.759–73.608 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 32.385 | 20.754 | 38.677 | 20.751–42.640 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 12.254 | 11.073 | 13.856 | 10.744–18.856 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 71.093 | 64.512 | 78.010 | 53.662–103.146 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 141.862 | 76.510 | 166.964 | 73.237–240.175 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.175 | 7.831 | 8.611 | 7.327–9.651 |
| R11_project_title_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 522.170 | 522.170 | 522.170 | 522.170–522.170 |
| R12_leanui | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 13.006 | 10.877 | 15.452 | 8.321–20.546 |
| R12_leanui | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 12.630 | 10.817 | 15.245 | 9.452–19.789 |
| R12_leanui | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 12.753 | 11.731 | 12.986 | 11.475–13.044 |
| R12_leanui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 41.664 | 41.664 | 41.664 | 41.664–41.664 |
| R12_leanui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 40.626 | 40.626 | 40.626 | 40.626–40.626 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 40.241 | 39.551 | 42.979 | 39.378–43.664 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 40.194 | 37.976 | 40.264 | 37.422–40.281 |
| R12_leanui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 63.687 | 62.050 | 71.524 | 61.083–72.069 |
| R12_leanui | warm | real_2692 | 2692 | close_book | PASS | 10 | 30.901 | 29.431 | 35.323 | 28.771–43.115 |
| R12_leanui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.472 | 7.883 | 9.349 | 7.200–9.363 |
| R12_leanui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 42.552 | 39.980 | 48.985 | 39.683–50.134 |
| R12_leanui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.739 | 11.054 | 15.203 | 9.523–17.153 |
| R12_leanui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 41.719 | 40.215 | 48.487 | 38.708–49.688 |
| R12_leanui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 70.376 | 67.578 | 79.994 | 65.901–81.117 |
| R12_leanui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 29.659 | 20.510 | 32.979 | 18.949–33.489 |
| R12_leanui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 12.921 | 10.747 | 14.097 | 10.251–20.180 |
| R12_leanui | warm | real_2692 | 2692 | open_book | PASS | 10 | 66.466 | 62.023 | 76.320 | 50.198–98.068 |
| R12_leanui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 140.161 | 74.289 | 168.590 | 70.085–245.352 |
| R12_leanui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.218 | 7.744 | 8.954 | 7.659–9.097 |
| R12_leanui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 261.883 | 261.883 | 261.883 | 261.883–261.883 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 87.946 | 82.198 | 94.533 | 80.136–108.459 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 29.841 | 23.425 | 37.044 | 20.509–47.624 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 88.376 | 85.568 | 95.912 | 81.046–105.091 |
| R1_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 30.795 | 25.655 | 35.554 | 22.170–48.940 |
| R1_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 14.642 | 13.368 | 14.666 | 13.049–14.672 |
| R1_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 23.256 | 19.903 | 35.075 | 18.056–39.119 |
| R1_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 20.334 | 18.078 | 31.796 | 16.586–34.086 |
| R1_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 164.096 | 163.735 | 178.243 | 163.645–181.780 |
| R1_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 19.057 | 17.831 | 22.020 | 17.524–22.761 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 49.704 | 49.704 | 49.704 | 49.704–49.704 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 47.751 | 47.751 | 47.751 | 47.751–47.751 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 44.223 | 44.140 | 46.494 | 44.119–47.062 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 43.436 | 42.101 | 43.794 | 41.767–43.884 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 83.957 | 78.601 | 95.555 | 76.102–121.736 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 28.345 | 18.416 | 43.954 | 16.655–64.812 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 33.317 | 27.634 | 66.605 | 27.442–111.956 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 84.213 | 79.145 | 95.135 | 77.757–110.555 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 25.733 | 20.766 | 31.431 | 17.467–45.407 |
| R1_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 93.002 | 75.739 | 119.688 | 70.964–122.830 |
| R1_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 46.184 | 41.553 | 63.672 | 37.088–82.496 |
| R1_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 9.090 | 8.394 | 10.184 | 7.808–10.401 |
| R1_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 9.395 | 8.706 | 12.604 | 8.442–12.903 |
| R1_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 43.037 | 39.873 | 53.475 | 39.067–59.282 |
| R1_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 10.990 | 9.966 | 23.013 | 9.147–28.773 |
| R1_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 43.322 | 41.144 | 53.872 | 40.853–55.206 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 106.195 | 91.801 | 124.493 | 66.856–140.185 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 26.169 | 22.239 | 30.071 | 19.119–31.586 |
| R1_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 20.679 | 16.810 | 31.729 | 12.680–38.034 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 80.698 | 72.881 | 104.542 | 60.471–114.904 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 163.606 | 105.755 | 210.930 | 94.230–279.167 |
| R1_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 33.708 | 28.338 | 36.128 | 27.737–37.868 |
| R1_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.496 | 8.058 | 8.884 | 7.560–9.259 |
| R1_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 825.893 | 825.893 | 825.893 | 825.893–825.893 |
| R2_simpleui | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 35.642 | 15.712 | 67.718 | 13.338–73.196 |
| R2_simpleui | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 23.386 | 19.269 | 41.184 | 16.686–44.533 |
| R2_simpleui | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 34.061 | 32.555 | 35.910 | 32.179–36.372 |
| R2_simpleui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 60.126 | 60.126 | 60.126 | 60.126–60.126 |
| R2_simpleui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 181.845 | 181.845 | 181.845 | 181.845–181.845 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 46.638 | 46.093 | 48.306 | 45.957–48.723 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 162.017 | 157.451 | 163.754 | 156.310–164.188 |
| R2_simpleui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 115.510 | 91.504 | 159.947 | 81.712–165.404 |
| R2_simpleui | warm | real_2692 | 2692 | close_book | PASS | 10 | 145.350 | 134.603 | 279.466 | 129.474–313.419 |
| R2_simpleui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 13.835 | 11.975 | 36.492 | 11.633–211.751 |
| R2_simpleui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 48.800 | 44.313 | 66.105 | 43.856–67.729 |
| R2_simpleui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 22.848 | 17.704 | 51.788 | 13.128–60.914 |
| R2_simpleui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 166.260 | 68.775 | 206.981 | 66.448–251.530 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 122.947 | 89.282 | 134.677 | 77.712–142.068 |
| R2_simpleui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 41.782 | 30.300 | 89.188 | 27.959–90.417 |
| R2_simpleui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 27.109 | 21.763 | 58.344 | 18.581–69.657 |
| R2_simpleui | warm | real_2692 | 2692 | open_book | PASS | 10 | 150.185 | 135.434 | 178.032 | 132.661–185.137 |
| R2_simpleui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 172.719 | 108.587 | 211.553 | 100.672–306.088 |
| R2_simpleui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 27.785 | 24.526 | 168.344 | 23.603–169.312 |
| R2_simpleui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1899.219 | 1899.219 | 1899.219 | 1899.219–1899.219 |
| R2_simpleui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 14.812 | 11.566 | 31.589 | 11.558–32.547 |
| R3_zenos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 18.312 | 10.636 | 30.672 | 9.782–40.040 |
| R3_zenos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 11.005 | 9.419 | 26.392 | 8.729–34.252 |
| R3_zenos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 26.694 | 25.693 | 26.877 | 25.443–26.923 |
| R3_zenos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 143.787 | 143.787 | 143.787 | 143.787–143.787 |
| R3_zenos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 64.625 | 64.625 | 64.625 | 64.625–64.625 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 141.642 | 138.832 | 146.004 | 138.129–147.094 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 64.956 | 63.399 | 65.759 | 63.010–65.960 |
| R3_zenos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 76.581 | 61.295 | 90.429 | 58.602–90.453 |
| R3_zenos | warm | real_2692 | 2692 | close_book | PASS | 10 | 54.114 | 44.660 | 96.393 | 43.697–118.638 |
| R3_zenos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 17.325 | 16.422 | 17.444 | 13.338–17.452 |
| R3_zenos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 58.517 | 56.245 | 67.795 | 55.369–71.629 |
| R3_zenos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 19.318 | 11.382 | 30.206 | 9.544–37.854 |
| R3_zenos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 66.513 | 64.376 | 79.661 | 64.207–83.691 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 82.812 | 60.264 | 92.263 | 59.937–122.634 |
| R3_zenos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 34.435 | 31.496 | 55.850 | 25.396–74.687 |
| R3_zenos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 11.037 | 9.794 | 25.151 | 8.392–27.418 |
| R3_zenos | warm | real_2692 | 2692 | open_book | PASS | 10 | 150.886 | 102.995 | 167.775 | 97.195–177.536 |
| R3_zenos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 168.069 | 99.153 | 201.094 | 95.419–291.666 |
| R3_zenos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 9.434 | 8.888 | 11.703 | 8.442–13.128 |
| R3_zenos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 598.337 | 598.337 | 598.337 | 598.337–598.337 |
| R3_zenos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 12.917 | 10.256 | 17.420 | 9.053–41.268 |
| R4_project_title | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 12.691 | 10.822 | 15.322 | 9.601–19.612 |
| R4_project_title | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 12.465 | 10.970 | 14.620 | 9.190–19.794 |
| R4_project_title | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 11.719 | 11.628 | 12.041 | 11.605–12.122 |
| R4_project_title | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 40.555 | 40.555 | 40.555 | 40.555–40.555 |
| R4_project_title | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 41.043 | 41.043 | 41.043 | 41.043–41.043 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 40.708 | 39.534 | 41.176 | 39.241–41.293 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 38.748 | 34.898 | 41.896 | 33.936–42.683 |
| R4_project_title | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 64.195 | 60.777 | 74.997 | 60.571–78.395 |
| R4_project_title | warm | real_2692 | 2692 | close_book | PASS | 10 | 30.912 | 24.686 | 40.839 | 20.627–40.847 |
| R4_project_title | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 12.041 | 10.974 | 13.943 | 10.850–13.993 |
| R4_project_title | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 41.368 | 39.856 | 45.247 | 36.756–47.319 |
| R4_project_title | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.448 | 10.478 | 15.237 | 10.007–17.583 |
| R4_project_title | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 40.743 | 37.654 | 45.249 | 37.508–46.973 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 70.736 | 66.232 | 78.351 | 66.201–79.572 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 29.785 | 19.761 | 38.837 | 18.988–41.933 |
| R4_project_title | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 13.005 | 10.830 | 15.421 | 9.547–17.682 |
| R4_project_title | warm | real_2692 | 2692 | open_book | PASS | 10 | 66.375 | 59.179 | 78.057 | 55.372–104.972 |
| R4_project_title | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 140.025 | 79.423 | 164.695 | 75.738–234.414 |
| R4_project_title | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.277 | 7.955 | 8.756 | 7.480–8.885 |
| R4_project_title | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 500.434 | 500.434 | 500.434 | 500.434–500.434 |
| R5_vos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 23.668 | 20.143 | 36.284 | 17.077–41.027 |
| R5_vos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 20.558 | 18.701 | 32.381 | 17.254–35.479 |
| R5_vos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 20.079 | 19.897 | 21.358 | 19.851–21.678 |
| R5_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 66.941 | 66.941 | 66.941 | 66.941–66.941 |
| R5_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 60.496 | 60.496 | 60.496 | 60.496–60.496 |
| R5_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 56.026 | 53.434 | 57.831 | 52.786–58.282 |
| R5_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 53.404 | 52.504 | 56.880 | 52.279–57.749 |
| R5_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 70.757 | 65.147 | 122.507 | 65.119–137.888 |
| R5_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 60.032 | 54.837 | 66.269 | 48.344–73.826 |
| R5_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 12.997 | 11.312 | 15.070 | 11.253–16.686 |
| R5_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 55.519 | 53.438 | 62.254 | 50.933–62.468 |
| R5_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 20.383 | 12.646 | 34.003 | 10.475–35.894 |
| R5_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 55.668 | 52.542 | 68.006 | 51.886–71.997 |
| R5_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 76.904 | 71.964 | 113.387 | 66.407–119.011 |
| R5_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 36.106 | 29.155 | 65.789 | 27.235–90.706 |
| R5_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 13.941 | 12.121 | 25.960 | 10.623–35.145 |
| R5_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 98.128 | 78.295 | 107.294 | 78.163–133.861 |
| R5_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 153.589 | 85.882 | 184.944 | 76.262–268.451 |
| R5_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 11.452 | 9.334 | 12.961 | 8.812–13.041 |
| R5_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1080.131 | 1080.131 | 1080.131 | 1080.131–1080.131 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 88.256 | 82.040 | 103.495 | 78.795–141.644 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 40.160 | 27.825 | 60.201 | 21.947–96.249 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 88.786 | 84.949 | 104.440 | 80.277–133.882 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 29.325 | 25.575 | 38.715 | 22.908–97.170 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 38.346 | 34.316 | 38.950 | 33.308–39.101 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 34.627 | 15.273 | 68.463 | 13.811–82.852 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 22.314 | 19.482 | 39.694 | 16.317–43.923 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 158.958 | 133.076 | 160.828 | 126.605–161.296 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 33.720 | 32.466 | 34.547 | 32.152–34.754 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 61.735 | 61.735 | 61.735 | 61.735–61.735 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 182.298 | 182.298 | 182.298 | 182.298–182.298 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 46.557 | 46.255 | 47.044 | 46.180–47.166 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 155.149 | 154.579 | 156.530 | 154.436–156.875 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 104.084 | 85.880 | 126.077 | 83.025–231.862 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 37.981 | 26.217 | 48.650 | 19.950–155.836 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 38.521 | 35.050 | 138.422 | 33.946–138.815 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 92.298 | 88.592 | 102.484 | 85.650–192.127 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 48.622 | 39.106 | 62.277 | 32.633–161.032 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 110.206 | 80.383 | 142.683 | 76.185–153.105 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 144.308 | 138.277 | 379.257 | 123.669–410.287 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 31.924 | 30.517 | 136.316 | 30.511–140.541 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 14.015 | 13.189 | 37.000 | 12.521–225.316 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 47.853 | 45.355 | 59.034 | 45.199–59.128 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 20.842 | 17.997 | 47.705 | 12.969–54.432 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 174.734 | 63.796 | 202.226 | 63.748–240.391 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 97.885 | 95.134 | 125.665 | 92.856–128.905 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 60.814 | 41.289 | 70.285 | 29.965–97.764 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 24.218 | 21.186 | 50.443 | 17.684–55.543 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 169.707 | 157.847 | 182.787 | 137.192–196.265 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 188.614 | 125.573 | 219.344 | 99.894–317.589 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 42.469 | 37.939 | 44.045 | 35.561–47.107 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 26.164 | 24.595 | 49.956 | 24.123–231.555 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 1958.409 | 1958.409 | 1958.409 | 1958.409–1958.409 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 12.053 | 11.271 | 20.740 | 10.756–21.597 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 82.083 | 72.948 | 94.590 | 71.797–108.568 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 23.069 | 14.206 | 29.159 | 12.658–45.305 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 95.867 | 88.230 | 106.618 | 84.849–121.073 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 34.261 | 26.551 | 42.479 | 14.228–66.811 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 18.336 | 18.110 | 20.364 | 18.054–20.871 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 17.830 | 11.193 | 31.832 | 9.740–39.790 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 11.375 | 9.526 | 27.678 | 8.933–38.590 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 181.098 | 166.869 | 182.515 | 163.312–182.869 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 28.420 | 24.822 | 28.630 | 23.922–28.683 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 147.512 | 147.512 | 147.512 | 147.512–147.512 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 66.948 | 66.948 | 66.948 | 66.948–66.948 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 138.999 | 137.871 | 139.462 | 137.589–139.578 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 64.513 | 64.439 | 65.247 | 64.420–65.430 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 75.513 | 68.341 | 87.138 | 66.775–123.925 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 13.479 | 8.020 | 32.503 | 7.851–57.989 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 22.989 | 19.017 | 65.413 | 17.592–75.726 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 74.742 | 71.791 | 93.007 | 70.700–148.825 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 15.418 | 11.932 | 35.209 | 8.762–62.198 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 74.656 | 58.061 | 86.906 | 57.398–91.143 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 62.531 | 45.188 | 116.386 | 39.963–138.164 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 11.188 | 10.066 | 12.224 | 10.052–15.639 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 17.296 | 16.671 | 17.576 | 14.667–17.713 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 58.342 | 56.299 | 60.267 | 55.930–60.607 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 17.985 | 10.957 | 29.458 | 10.214–38.045 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 65.782 | 62.557 | 78.837 | 61.967–80.679 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 82.585 | 63.411 | 86.581 | 62.128–90.801 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 33.911 | 30.823 | 56.602 | 25.868–75.427 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 11.186 | 10.127 | 25.772 | 9.205–30.574 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 145.356 | 108.992 | 178.304 | 107.426–187.864 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 168.748 | 105.219 | 201.164 | 98.317–290.153 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 20.556 | 18.531 | 29.088 | 18.346–29.626 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 10.544 | 9.320 | 39.830 | 9.298–141.123 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 748.293 | 748.293 | 748.293 | 748.293–748.293 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 12.282 | 10.251 | 15.342 | 10.100–15.909 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging | PASS | 90 | 87.115 | 82.035 | 94.768 | 79.391–104.538 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 90 | 28.983 | 24.523 | 37.121 | 20.544–47.010 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 90 | 87.927 | 85.067 | 96.253 | 82.760–103.915 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 90 | 29.623 | 25.696 | 36.628 | 22.369–45.176 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | close_bookshelf | PASS | 3 | 14.364 | 12.871 | 14.548 | 12.498–14.594 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 24.057 | 20.942 | 37.296 | 18.291–41.922 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 21.001 | 18.579 | 34.147 | 14.955–37.883 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | open_bookshelf | PASS | 3 | 176.520 | 172.266 | 185.369 | 171.203–187.581 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 20.140 | 18.898 | 21.230 | 18.587–21.503 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 63.537 | 63.537 | 63.537 | 63.537–63.537 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 59.779 | 59.779 | 59.779 | 59.779–59.779 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 55.395 | 55.168 | 57.226 | 55.111–57.684 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 51.515 | 50.354 | 54.248 | 50.064–54.931 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 74.648 | 69.325 | 82.784 | 67.333–97.407 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 12.422 | 8.714 | 23.756 | 7.641–34.392 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 20.367 | 18.642 | 37.259 | 17.793–44.806 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | PASS | 30 | 72.484 | 70.481 | 85.309 | 69.561–164.741 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | PASS | 30 | 12.125 | 10.085 | 16.269 | 9.211–33.220 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 84.641 | 66.551 | 126.047 | 65.742–134.607 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 52.212 | 49.724 | 62.337 | 47.160–67.570 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 7.529 | 6.952 | 8.731 | 6.828–8.861 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.434 | 7.983 | 9.156 | 7.519–9.164 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 53.674 | 52.678 | 72.024 | 52.170–74.558 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.440 | 10.569 | 26.694 | 9.510–28.244 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 54.916 | 53.482 | 71.755 | 49.934–72.183 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 84.766 | 74.287 | 118.416 | 73.684–128.519 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 40.276 | 26.794 | 69.386 | 24.519–96.542 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 21.351 | 18.599 | 34.563 | 14.472–36.832 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 76.620 | 72.315 | 98.091 | 68.915–131.855 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 149.209 | 99.646 | 184.958 | 93.233–266.792 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 24.708 | 23.185 | 30.016 | 22.389–33.092 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.797 | 7.772 | 10.103 | 7.395–10.844 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 590.051 | 590.051 | 590.051 | 590.051–590.051 |
| R9_simpleui_vos | paging | real_2692 | 2692 | library_cached_paging | PASS | 90 | 42.054 | 15.243 | 66.244 | 13.349–69.246 |
| R9_simpleui_vos | paging | real_2692 | 2692 | library_sequential_paging | PASS | 90 | 21.654 | 18.580 | 39.627 | 15.037–44.155 |
| R9_simpleui_vos | paging | real_2692 | 2692 | paging_probe_step_2_to_3 | PASS | 3 | 16.651 | 16.170 | 32.123 | 16.050–35.991 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 59.417 | 59.417 | 59.417 | 59.417–59.417 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 142.524 | 142.524 | 142.524 | 142.524–142.524 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 47.691 | 45.885 | 47.998 | 45.434–48.075 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 127.220 | 126.976 | 127.252 | 126.915–127.260 |
| R9_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 93.511 | 67.205 | 119.072 | 58.064–123.527 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 146.086 | 137.278 | 229.009 | 113.209–235.913 |
| R9_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 13.058 | 11.898 | 14.061 | 11.634–14.838 |
| R9_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 37.605 | 36.114 | 44.215 | 36.009–57.620 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 12.879 | 11.002 | 44.926 | 9.658–53.465 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 116.261 | 101.230 | 161.290 | 100.116–198.231 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 99.165 | 62.589 | 115.474 | 59.281–117.905 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 56.761 | 30.208 | 89.563 | 24.924–128.256 |
| R9_simpleui_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 18.941 | 15.844 | 52.056 | 12.526–54.463 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 193.135 | 152.093 | 225.040 | 147.693–229.167 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 186.328 | 135.186 | 304.693 | 103.447–319.933 |
| R9_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 52.543 | 47.465 | 213.549 | 46.488–245.495 |
| R9_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 2474.601 | 2474.601 | 2474.601 | 2474.601–2474.601 |
| R9_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 11.776 | 9.261 | 23.079 | 8.831–24.620 |
| R0_stock | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 543.028 | 529.954 | 543.489 | 526.686–543.605 |
| R0_stock | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 566.572 | 553.730 | 569.876 | 550.519–570.701 |
| R0_stock | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 2341.715 | 2340.121 | 2372.272 | 2339.722–2379.911 |
| R0_stock | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 2414.359 | 2409.512 | 2447.966 | 2408.301–2456.367 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 564.891 | 564.891 | 564.891 | 564.891–564.891 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 665.960 | 665.960 | 665.960 | 665.960–665.960 |
| R0_stock | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 676.619 | 676.619 | 676.619 | 676.619–676.619 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 795.861 | 795.861 | 795.861 | 795.861–795.861 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 512.365 | 502.862 | 524.423 | 500.486–527.438 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 609.515 | 595.763 | 620.718 | 592.326–623.518 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 618.656 | 604.671 | 629.354 | 601.174–632.029 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 662.695 | 649.388 | 673.634 | 646.061–676.368 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 520.596 | 520.596 | 520.596 | 520.596–520.596 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2337.238 | 2337.238 | 2337.238 | 2337.238–2337.238 |
| R0_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 15681.212 | 15681.212 | 15681.212 | 15681.212–15681.212 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 15784.824 | 15784.824 | 15784.824 | 15784.824–15784.824 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 701.764 | 699.572 | 702.323 | 699.024–702.463 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 770.906 | 770.064 | 773.571 | 769.853–774.237 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 11496.261 | 11234.725 | 11502.352 | 11169.342–11503.874 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 11563.913 | 11344.647 | 11566.132 | 11289.831–11566.687 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 918.122 | 918.122 | 918.122 | 918.122–918.122 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1148.514 | 1148.514 | 1148.514 | 1148.514–1148.514 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1159.134 | 1159.134 | 1159.134 | 1159.134–1159.134 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1211.028 | 1211.028 | 1211.028 | 1211.028–1211.028 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 651.785 | 637.876 | 669.811 | 634.398–674.317 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 857.260 | 832.994 | 861.370 | 826.927–862.398 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 869.193 | 844.436 | 871.765 | 838.247–872.409 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 923.587 | 892.969 | 925.610 | 885.314–926.116 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 654.989 | 654.989 | 654.989 | 654.989–654.989 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 3933.716 | 3933.716 | 3933.716 | 3933.716–3933.716 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 45921.015 | 45921.015 | 45921.015 | 45921.015–45921.015 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 46212.062 | 46212.062 | 46212.062 | 46212.062–46212.062 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 530.984 | 528.610 | 534.394 | 528.016–535.246 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 552.175 | 549.423 | 556.726 | 548.735–557.864 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1563.507 | 1544.472 | 1585.787 | 1539.713–1591.358 |
| R11_project_title_vos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1610.607 | 1591.235 | 1633.604 | 1586.392–1639.353 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 548.154 | 548.154 | 548.154 | 548.154–548.154 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 657.838 | 657.838 | 657.838 | 657.838–657.838 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 667.465 | 667.465 | 667.465 | 667.465–667.465 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 710.769 | 710.769 | 710.769 | 710.769–710.769 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 517.156 | 509.543 | 523.302 | 507.640–524.839 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 628.330 | 619.720 | 632.969 | 617.567–634.129 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 638.030 | 629.129 | 641.923 | 626.904–642.896 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 685.257 | 673.909 | 687.318 | 671.072–687.833 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 533.778 | 533.778 | 533.778 | 533.778–533.778 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2515.783 | 2515.783 | 2515.783 | 2515.783–2515.783 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12441.838 | 12441.838 | 12441.838 | 12441.838–12441.838 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12493.824 | 12493.824 | 12493.824 | 12493.824–12493.824 |
| R12_leanui | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 511.586 | 511.345 | 512.266 | 511.285–512.436 |
| R12_leanui | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 531.077 | 530.336 | 531.493 | 530.150–531.597 |
| R12_leanui | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1600.176 | 1574.443 | 1616.269 | 1568.010–1620.292 |
| R12_leanui | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1646.378 | 1620.972 | 1662.388 | 1614.621–1666.391 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 549.656 | 549.656 | 549.656 | 549.656–549.656 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 639.843 | 639.843 | 639.843 | 639.843–639.843 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 647.917 | 647.917 | 647.917 | 647.917–647.917 |
| R12_leanui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 691.269 | 691.269 | 691.269 | 691.269–691.269 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 485.883 | 477.864 | 502.417 | 475.859–506.550 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 572.770 | 566.034 | 592.852 | 564.350–597.873 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 581.183 | 574.363 | 601.141 | 572.658–606.130 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 624.188 | 617.433 | 647.531 | 615.744–653.366 |
| R12_leanui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 477.821 | 477.821 | 477.821 | 477.821–477.821 |
| R12_leanui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2054.935 | 2054.935 | 2054.935 | 2054.935–2054.935 |
| R12_leanui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11647.114 | 11647.114 | 11647.114 | 11647.114–11647.114 |
| R12_leanui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11702.064 | 11702.064 | 11702.064 | 11702.064–11702.064 |
| R1_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 547.049 | 539.809 | 560.171 | 537.999–563.452 |
| R1_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 572.281 | 564.434 | 586.074 | 562.472–589.522 |
| R1_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 10231.679 | 10162.547 | 10357.430 | 10145.264–10388.868 |
| R1_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 10280.902 | 10213.742 | 10406.830 | 10196.953–10438.312 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 578.450 | 578.450 | 578.450 | 578.450–578.450 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 686.703 | 686.703 | 686.703 | 686.703–686.703 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 698.986 | 698.986 | 698.986 | 698.986–698.986 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 845.733 | 845.733 | 845.733 | 845.733–845.733 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 496.898 | 495.073 | 523.217 | 494.617–529.797 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 592.796 | 590.492 | 620.987 | 589.916–628.035 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 601.868 | 599.212 | 630.685 | 598.547–637.889 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 645.280 | 642.865 | 674.138 | 642.261–681.352 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 497.537 | 497.537 | 497.537 | 497.537–497.537 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2153.199 | 2153.199 | 2153.199 | 2153.199–2153.199 |
| R1_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 24638.418 | 24638.418 | 24638.418 | 24638.418–24638.418 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 24718.687 | 24718.687 | 24718.687 | 24718.687–24718.687 |
| R2_simpleui | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 780.258 | 761.483 | 793.763 | 756.789–797.139 |
| R2_simpleui | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 850.607 | 832.801 | 869.760 | 828.349–874.548 |
| R2_simpleui | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 3281.558 | 3204.547 | 3296.587 | 3185.294–3300.345 |
| R2_simpleui | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 3331.933 | 3253.099 | 3346.853 | 3233.391–3350.583 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 817.298 | 817.298 | 817.298 | 817.298–817.298 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1071.095 | 1071.095 | 1071.095 | 1071.095–1071.095 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1083.552 | 1083.552 | 1083.552 | 1083.552–1083.552 |
| R2_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1131.393 | 1131.393 | 1131.393 | 1131.393–1131.393 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 658.669 | 655.019 | 693.805 | 654.107–702.589 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 878.846 | 877.326 | 913.416 | 876.946–922.059 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 889.874 | 889.379 | 924.425 | 889.256–933.063 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 937.200 | 935.683 | 970.787 | 935.304–979.184 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 699.031 | 699.031 | 699.031 | 699.031–699.031 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 4226.688 | 4226.688 | 4226.688 | 4226.688–4226.688 |
| R2_simpleui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 31122.313 | 31122.313 | 31122.313 | 31122.313–31122.313 |
| R2_simpleui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 31217.983 | 31217.983 | 31217.983 | 31217.983–31217.983 |
| R3_zenos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 690.763 | 683.027 | 729.821 | 681.093–739.585 |
| R3_zenos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 821.083 | 816.098 | 855.416 | 814.852–863.999 |
| R3_zenos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 2128.076 | 2100.498 | 2140.268 | 2093.604–2143.316 |
| R3_zenos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 2192.177 | 2153.322 | 2194.802 | 2143.608–2195.459 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 818.150 | 818.150 | 818.150 | 818.150–818.150 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1055.578 | 1055.578 | 1055.578 | 1055.578–1055.578 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1073.254 | 1073.254 | 1073.254 | 1073.254–1073.254 |
| R3_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1121.014 | 1121.014 | 1121.014 | 1121.014–1121.014 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 645.418 | 629.344 | 668.638 | 625.325–674.443 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 859.418 | 851.755 | 884.928 | 849.840–891.306 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 876.148 | 868.701 | 900.187 | 866.839–906.196 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 924.986 | 919.217 | 948.711 | 917.774–954.642 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 637.907 | 637.907 | 637.907 | 637.907–637.907 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 3356.397 | 3356.397 | 3356.397 | 3356.397–3356.397 |
| R3_zenos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 18386.233 | 18386.233 | 18386.233 | 18386.233–18386.233 |
| R3_zenos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 18540.284 | 18540.284 | 18540.284 | 18540.284–18540.284 |
| R4_project_title | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 513.975 | 510.163 | 515.921 | 509.210–516.408 |
| R4_project_title | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 533.899 | 530.775 | 534.980 | 529.994–535.250 |
| R4_project_title | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 1587.035 | 1578.425 | 1605.949 | 1576.272–1610.678 |
| R4_project_title | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 1634.587 | 1626.809 | 1655.284 | 1624.865–1660.459 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 520.323 | 520.323 | 520.323 | 520.323–520.323 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 609.416 | 609.416 | 609.416 | 609.416–609.416 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 618.070 | 618.070 | 618.070 | 618.070–618.070 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 661.339 | 661.339 | 661.339 | 661.339–661.339 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 488.363 | 481.179 | 490.355 | 479.383–490.854 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 570.647 | 568.549 | 579.846 | 568.025–582.146 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 579.614 | 577.275 | 588.649 | 576.691–590.908 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 624.658 | 622.733 | 632.450 | 622.252–634.398 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 489.590 | 489.590 | 489.590 | 489.590–489.590 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2047.190 | 2047.190 | 2047.190 | 2047.190–2047.190 |
| R4_project_title | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11879.071 | 11879.071 | 11879.071 | 11879.071–11879.071 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11930.550 | 11930.550 | 11930.550 | 11930.550–11930.550 |
| R5_vos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 574.332 | 574.144 | 586.224 | 574.097–589.197 |
| R5_vos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 601.028 | 598.269 | 611.929 | 597.580–614.654 |
| R5_vos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 2399.781 | 2374.816 | 2410.418 | 2368.574–2413.077 |
| R5_vos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 2445.846 | 2423.445 | 2460.069 | 2417.845–2463.625 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 596.018 | 596.018 | 596.018 | 596.018–596.018 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 735.716 | 735.716 | 735.716 | 735.716–735.716 |
| R5_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 748.191 | 748.191 | 748.191 | 748.191–748.191 |
| R5_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 853.879 | 853.879 | 853.879 | 853.879–853.879 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 547.128 | 535.593 | 572.842 | 532.710–579.270 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 671.521 | 650.752 | 692.628 | 645.560–697.904 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 680.815 | 660.021 | 701.848 | 654.822–707.106 |
| R5_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 729.506 | 705.068 | 750.606 | 698.959–755.881 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 541.548 | 541.548 | 541.548 | 541.548–541.548 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2690.395 | 2690.395 | 2690.395 | 2690.395–2690.395 |
| R5_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 16946.172 | 16946.172 | 16946.172 | 16946.172–16946.172 |
| R5_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 17022.564 | 17022.564 | 17022.564 | 17022.564–17022.564 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 770.618 | 768.027 | 778.948 | 767.380–781.030 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 841.182 | 840.098 | 851.777 | 839.827–854.426 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 11761.026 | 11653.486 | 11902.901 | 11626.601–11938.369 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 11820.261 | 11714.034 | 11965.482 | 11687.477–12001.787 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 876.141 | 876.141 | 876.141 | 876.141–876.141 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1132.717 | 1132.717 | 1132.717 | 1132.717–1132.717 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1145.146 | 1145.146 | 1145.146 | 1145.146–1145.146 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1192.387 | 1192.387 | 1192.387 | 1192.387–1192.387 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 656.124 | 655.943 | 690.671 | 655.898–699.307 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 873.499 | 870.854 | 905.755 | 870.192–913.820 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 884.440 | 881.671 | 916.898 | 880.978–925.012 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 931.667 | 928.204 | 966.290 | 927.338–974.946 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 651.894 | 651.894 | 651.894 | 651.894–651.894 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 4054.926 | 4054.926 | 4054.926 | 4054.926–4054.926 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 44265.553 | 44265.553 | 44265.553 | 44265.553–44265.553 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 44354.790 | 44354.790 | 44354.790 | 44354.790–44354.790 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 696.872 | 691.528 | 700.271 | 690.192–701.121 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 823.774 | 822.129 | 834.410 | 821.718–837.069 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 10008.341 | 9958.999 | 10030.032 | 9946.663–10035.455 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 10064.821 | 10016.403 | 10088.629 | 10004.299–10094.582 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 846.547 | 846.547 | 846.547 | 846.547–846.547 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1090.652 | 1090.652 | 1090.652 | 1090.652–1090.652 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 1105.828 | 1105.828 | 1105.828 | 1105.828–1105.828 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1153.596 | 1153.596 | 1153.596 | 1153.596–1153.596 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 632.976 | 632.757 | 661.646 | 632.702–668.813 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 848.906 | 848.398 | 875.171 | 848.271–881.738 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 866.288 | 866.020 | 892.283 | 865.953–898.782 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 917.453 | 916.885 | 941.668 | 916.743–947.721 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 635.168 | 635.168 | 635.168 | 635.168–635.168 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 3357.924 | 3357.924 | 3357.924 | 3357.924–3357.924 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 26644.722 | 26644.722 | 26644.722 | 26644.722–26644.722 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 26716.164 | 26716.164 | 26716.164 | 26716.164–26716.164 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 566.203 | 564.550 | 571.561 | 564.136–572.901 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 593.517 | 592.297 | 597.600 | 591.992–598.621 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 10304.326 | 10231.053 | 10340.481 | 10212.734–10349.519 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 10355.890 | 10281.997 | 10393.060 | 10263.523–10402.353 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 590.804 | 590.804 | 590.804 | 590.804–590.804 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 726.184 | 726.184 | 726.184 | 726.184–726.184 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 738.863 | 738.863 | 738.863 | 738.863–738.863 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 838.173 | 838.173 | 838.173 | 838.173–838.173 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 527.604 | 522.184 | 547.327 | 520.829–552.258 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 641.011 | 636.942 | 667.945 | 635.925–674.678 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 650.929 | 646.581 | 677.081 | 645.494–683.620 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 697.919 | 691.574 | 721.640 | 689.988–727.570 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 517.895 | 517.895 | 517.895 | 517.895–517.895 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 2628.157 | 2628.157 | 2628.157 | 2628.157–2628.157 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 23035.488 | 23035.488 | 23035.488 | 23035.488–23035.488 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 23193.550 | 23193.550 | 23193.550 | 23193.550–23193.550 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 692.461 | 685.606 | 693.156 | 683.892–693.330 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 760.278 | 759.644 | 763.037 | 759.486–763.726 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 3089.704 | 3067.816 | 3099.826 | 3062.344–3102.356 |
| R9_simpleui_vos | paging | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 3137.866 | 3126.304 | 3159.002 | 3123.414–3164.286 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 756.607 | 756.607 | 756.607 | 756.607–756.607 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 974.178 | 974.178 | 974.178 | 974.178–974.178 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 984.708 | 984.708 | 984.708 | 984.708–984.708 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 1032.104 | 1032.104 | 1032.104 | 1032.104–1032.104 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 658.491 | 650.932 | 675.567 | 649.042–679.836 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 847.468 | 838.053 | 861.452 | 835.699–864.948 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 858.170 | 848.686 | 872.071 | 846.314–875.547 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 905.654 | 895.837 | 918.644 | 893.383–921.891 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 647.487 | 647.487 | 647.487 | 647.487–647.487 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 3513.329 | 3513.329 | 3513.329 | 3513.329–3513.329 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 31829.310 | 31829.310 | 31829.310 | 31829.310–31829.310 |
| R9_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 31919.153 | 31919.153 | 31919.153 | 31919.153–31919.153 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R0_stock | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 8958.501 | 9012.210 | 8943.235–9025.638 | 11963.858 | 166128.000 |
| R0_stock | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 9575.884 | 9608.728 | 9538.509–9616.938 | 11690.613 | 189648.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9047.345 | 9047.345 | 9047.345–9047.345 | 11876.547 | 166512.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10293.446 | 10293.446 | 10293.446–10293.446 | 14879.609 | 175280.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9249.243 | 9274.403 | 9224.474–9280.692 | 11108.020 | 167264.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9275.802 | 9308.692 | 9269.278–9316.915 | 15223.545 | 173840.000 |
| R0_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9259.239 | 9259.239 | 9259.239–9259.239 | 15360.285 | 164640.000 |
| R0_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9263.282 | 9263.282 | 9263.282–9263.282 | 17920.349 | 182832.000 |
| R0_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15244.110 | 15244.110 | 15244.110–15244.110 | 17061.266 | 341072.000 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14066.451 | 14097.557 | 14036.498–14105.334 | 18397.099 | 174992.000 |
| R10_simpleui_vos_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 19339.292 | 19351.601 | 19291.257–19354.679 | 20407.657 | 218592.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14108.135 | 14108.135 | 14108.135–14108.135 | 18641.271 | 175232.000 |
| R10_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14744.443 | 14744.443 | 14744.443–14744.443 | 16072.870 | 185536.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14002.151 | 14006.195 | 13905.784–14007.206 | 22983.154 | 173024.000 |
| R10_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 14717.628 | 14943.972 | 14631.452–15000.558 | 15785.202 | 183728.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13961.866 | 13961.866 | 13961.866–13961.866 | 23009.677 | 174320.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 19455.687 | 19455.687 | 19455.687–19455.687 | 28661.645 | 205328.000 |
| R10_simpleui_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 76771.185 | 76771.185 | 76771.185–76771.185 | 83370.422 | 425264.000 |
| R11_project_title_vos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10315.765 | 10371.205 | 10271.120–10385.065 | 14055.354 | 166496.000 |
| R11_project_title_vos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 10986.655 | 11042.299 | 10961.835–11056.210 | 22754.165 | 197984.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10384.003 | 10384.003 | 10384.003–10384.003 | 14359.145 | 168784.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10361.030 | 10361.030 | 10361.030–10361.030 | 17112.708 | 178400.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10252.839 | 10308.429 | 10234.788–10322.327 | 11886.121 | 166960.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10307.472 | 10314.965 | 10281.632–10316.839 | 16924.276 | 174768.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10273.339 | 10273.339 | 10273.339–10273.339 | 11818.488 | 167760.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10365.651 | 10365.651 | 10365.651–10365.651 | 20777.879 | 186160.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15054.992 | 15054.992 | 15054.992–15054.992 | 36060.072 | 325376.000 |
| R12_leanui | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9101.012 | 9137.668 | 9009.949–9146.832 | 11590.549 | 165632.000 |
| R12_leanui | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 9697.738 | 9710.570 | 9670.312–9713.777 | 24277.396 | 194880.000 |
| R12_leanui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9002.609 | 9002.609 | 9002.609–9002.609 | 11829.666 | 165504.000 |
| R12_leanui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9061.137 | 9061.137 | 9061.137–9061.137 | 14996.735 | 174000.000 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9354.543 | 9364.071 | 9218.969–9366.453 | 15031.516 | 163232.000 |
| R12_leanui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9276.555 | 9549.242 | 9264.375–9617.414 | 15261.073 | 171968.000 |
| R12_leanui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9224.398 | 9224.398 | 9224.398–9224.398 | 14874.727 | 161472.000 |
| R12_leanui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9299.578 | 9299.578 | 9299.578–9299.578 | 18199.700 | 180016.000 |
| R12_leanui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14735.504 | 14735.504 | 14735.504–14735.504 | 24091.781 | 323376.000 |
| R1_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9461.759 | 9544.190 | 9444.353–9564.798 | 13568.868 | 165408.000 |
| R1_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 14518.008 | 14571.805 | 14423.574–14585.254 | 15173.620 | 202272.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9493.712 | 9493.712 | 9493.712–9493.712 | 13619.981 | 166352.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10739.892 | 10739.892 | 10739.892–10739.892 | 15389.409 | 176336.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9433.294 | 9472.378 | 9111.384–9482.149 | 12049.929 | 164464.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9404.321 | 9459.856 | 9197.521–9473.739 | 15310.066 | 173888.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9398.946 | 9398.946 | 9398.946–9398.946 | 10156.165 | 167008.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9442.169 | 9442.169 | 9442.169–9442.169 | 15337.147 | 187776.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 20528.235 | 20528.235 | 20528.235–20528.235 | 21961.966 | 367824.000 |
| R2_simpleui | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13185.076 | 13197.504 | 13148.107–13200.611 | 17082.209 | 175808.000 |
| R2_simpleui | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 14417.154 | 14450.326 | 14376.150–14458.619 | 14430.354 | 194480.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13169.201 | 13169.201 | 13169.201–13169.201 | 16299.928 | 175168.000 |
| R2_simpleui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14030.123 | 14030.123 | 14030.123–14030.123 | 17325.490 | 182096.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13178.616 | 13182.666 | 13110.136–13183.679 | 21619.646 | 174624.000 |
| R2_simpleui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 13965.491 | 14014.979 | 13903.304–14027.351 | 16994.870 | 183744.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13163.808 | 13163.808 | 13163.808–13163.808 | 22148.287 | 174368.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 17977.793 | 17977.793 | 17977.793–17977.793 | 29159.136 | 197968.000 |
| R2_simpleui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 72404.071 | 72404.071 | 72404.071–72404.071 | 73377.242 | 408864.000 |
| R3_zenos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14217.331 | 14300.615 | 14215.331–14321.437 | 15857.264 | 172208.000 |
| R3_zenos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 15724.581 | 15745.194 | 15721.104–15750.347 | 16444.986 | 204352.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14318.749 | 14318.749 | 14318.749–14318.749 | 23699.218 | 171968.000 |
| R3_zenos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15808.120 | 15808.120 | 15808.120–15808.120 | 26507.153 | 191712.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14227.238 | 14275.254 | 14213.598–14287.258 | 21783.492 | 176896.000 |
| R3_zenos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 15746.277 | 15771.490 | 15698.855–15777.793 | 26180.436 | 190176.000 |
| R3_zenos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14217.023 | 14217.023 | 14217.023–14217.023 | 22468.646 | 183568.000 |
| R3_zenos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 15872.718 | 15872.718 | 15872.718–15872.718 | 19833.743 | 201152.000 |
| R3_zenos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 39158.976 | 39158.976 | 39158.976–39158.976 | 42646.800 | 353344.000 |
| R4_project_title | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9201.077 | 9205.640 | 9104.933–9206.780 | 11620.903 | 165616.000 |
| R4_project_title | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 9768.007 | 9801.757 | 9735.913–9810.194 | 23065.747 | 195136.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9172.937 | 9172.937 | 9172.937–9172.937 | 11839.994 | 167888.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9186.616 | 9186.616 | 9186.616–9186.616 | 15243.045 | 176400.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9409.073 | 9642.342 | 9354.050–9700.659 | 15022.518 | 164560.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9377.429 | 9627.507 | 9364.499–9690.026 | 15444.515 | 173088.000 |
| R4_project_title | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9325.636 | 9325.636 | 9325.636–9325.636 | 14821.254 | 161552.000 |
| R4_project_title | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9421.647 | 9421.647 | 9421.647–9421.647 | 17227.174 | 180416.000 |
| R4_project_title | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 13757.434 | 13757.434 | 13757.434–13757.434 | 34208.131 | 319856.000 |
| R5_vos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10122.841 | 10150.231 | 10081.556–10157.079 | 14037.623 | 166960.000 |
| R5_vos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 10790.032 | 10811.135 | 10762.790–10816.411 | 11803.393 | 189856.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10152.438 | 10152.438 | 10152.438–10152.438 | 13804.450 | 165872.000 |
| R5_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11454.579 | 11454.579 | 11454.579–11454.579 | 16741.596 | 175680.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10168.532 | 10194.104 | 10165.829–10200.497 | 12186.590 | 168096.000 |
| R5_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10153.884 | 10199.531 | 10116.231–10210.942 | 16727.730 | 177584.000 |
| R5_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10176.458 | 10176.458 | 10176.458–10176.458 | 11249.354 | 168560.000 |
| R5_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10198.114 | 10198.114 | 10198.114–10198.114 | 19764.249 | 187072.000 |
| R5_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15639.759 | 15639.759 | 15639.759–15639.759 | 18590.979 | 331808.000 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13405.654 | 13419.479 | 13368.186–13422.936 | 14897.106 | 178032.000 |
| R6_simpleui_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 18598.421 | 18641.940 | 18106.089–18652.819 | 19661.961 | 211872.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13401.533 | 13401.533 | 13401.533–13401.533 | 15618.143 | 175936.000 |
| R6_simpleui_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14112.979 | 14112.979 | 14112.979–14112.979 | 17415.431 | 183632.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13343.030 | 13344.565 | 13278.827–13344.948 | 22404.820 | 175168.000 |
| R6_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 14079.312 | 14153.808 | 14041.159–14172.433 | 17211.584 | 184304.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13323.558 | 13323.558 | 13323.558–13323.558 | 23086.109 | 173728.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 18193.179 | 18193.179 | 18193.179–18193.179 | 29109.195 | 197888.000 |
| R6_simpleui_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 76090.438 | 76090.438 | 76090.438–76090.438 | 77128.319 | 437856.000 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14530.733 | 14545.208 | 14512.358–14548.827 | 17341.934 | 174672.000 |
| R7_zenos_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 20169.358 | 20179.668 | 20121.636–20182.245 | 20663.146 | 229552.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14599.534 | 14599.534 | 14599.534–14599.534 | 17346.198 | 173744.000 |
| R7_zenos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16076.323 | 16076.323 | 16076.323–16076.323 | 26995.968 | 193632.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 14448.707 | 14458.451 | 14387.773–14460.887 | 22101.623 | 180416.000 |
| R7_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 15958.324 | 15966.471 | 15879.227–15968.508 | 26479.834 | 186080.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 14390.797 | 14390.797 | 14390.797–14390.797 | 22546.399 | 171968.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 16045.217 | 16045.217 | 16045.217–16045.217 | 19945.178 | 204544.000 |
| R7_zenos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 42586.929 | 42586.929 | 42586.929–42586.929 | 45287.354 | 389632.000 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10414.411 | 10442.096 | 10379.759–10449.017 | 15413.398 | 166800.000 |
| R8_vos_bookshelf | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 15367.784 | 15399.794 | 15366.538–15407.796 | 16001.026 | 199824.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10409.095 | 10409.095 | 10409.095–10409.095 | 15421.527 | 167312.000 |
| R8_vos_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11632.013 | 11632.013 | 11632.013–11632.013 | 17070.612 | 178112.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10349.126 | 10353.342 | 10314.017–10354.396 | 12130.106 | 167072.000 |
| R8_vos_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10342.743 | 10346.562 | 10252.946–10347.517 | 17003.567 | 175856.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10313.661 | 10313.661 | 10313.661–10313.661 | 12364.712 | 166096.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10405.516 | 10405.516 | 10405.516–10405.516 | 19906.274 | 185312.000 |
| R8_vos_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 20578.892 | 20578.892 | 20578.892–20578.892 | 23340.124 | 347568.000 |
| R9_simpleui_vos | paging | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13791.740 | 13801.978 | 13785.545–13804.537 | 16479.108 | 175184.000 |
| R9_simpleui_vos | paging | real_2692 | 2692 | post_stress_idle | PASS | 3 | 3 | 15106.389 | 15179.911 | 15094.725–15198.291 | 19802.453 | 196128.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13832.322 | 13832.322 | 13832.322–13832.322 | 23510.321 | 177296.000 |
| R9_simpleui_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 14519.900 | 14519.900 | 14519.900–14519.900 | 15808.395 | 188816.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 13773.663 | 13820.579 | 13751.800–13832.308 | 22509.256 | 173840.000 |
| R9_simpleui_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 14518.952 | 14527.249 | 14478.511–14529.323 | 15961.711 | 183824.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 13789.952 | 13789.952 | 13789.952–13789.952 | 22401.989 | 171488.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 20756.589 | 20756.589 | 20756.589–20756.589 | 29233.375 | 204080.000 |
| R9_simpleui_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 75839.204 | 75839.204 | 75839.204–75839.204 | 78572.390 | 401888.000 |

## Data-derived comparisons

- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 23.256 ms vs 23.902 ms (2.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.334 ms vs 20.370 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 10.990 ms vs 21.023 ms (47.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 20.679 ms vs 21.489 ms (3.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (paging, real_2692, 2692 books): 23.902 ms vs 35.642 ms (32.9% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.370 ms vs 23.386 ms (12.9% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 21.023 ms vs 22.848 ms (8.0% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 21.489 ms vs 27.109 ms (20.7% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 18.312 ms vs 23.902 ms (23.4% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 11.005 ms vs 20.370 ms (46.0% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 19.318 ms vs 21.023 ms (8.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.037 ms vs 21.489 ms (48.6% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 12.691 ms vs 23.902 ms (46.9% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (paging, real_2692, 2692 books): 12.465 ms vs 20.370 ms (38.8% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 12.448 ms vs 21.023 ms (40.8% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R4_project_title` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 13.005 ms vs 21.489 ms (39.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (paging, real_2692, 2692 books): 23.668 ms vs 23.902 ms (1.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R0_stock` has a lower descriptive median than `R5_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.370 ms vs 20.558 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 20.383 ms vs 21.023 ms (3.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 13.941 ms vs 21.489 ms (35.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (paging, real_2692, 2692 books): 34.627 ms vs 35.642 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 22.314 ms vs 23.386 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 20.842 ms vs 22.848 ms (8.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R6_simpleui_bookshelf` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 24.218 ms vs 27.109 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (paging, real_2692, 2692 books): 17.830 ms vs 18.312 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 11.005 ms vs 11.375 ms (3.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R7_zenos_bookshelf` has a lower descriptive median than `R3_zenos` for `library_cached_paging` (warm, real_2692, 2692 books): 17.985 ms vs 19.318 ms (6.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R3_zenos` has a lower descriptive median than `R7_zenos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 11.037 ms vs 11.186 ms (1.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_cached_paging` (paging, real_2692, 2692 books): 23.668 ms vs 24.057 ms (1.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (paging, real_2692, 2692 books): 20.558 ms vs 21.001 ms (2.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R8_vos_bookshelf` has a lower descriptive median than `R5_vos` for `library_cached_paging` (warm, real_2692, 2692 books): 12.440 ms vs 20.383 ms (39.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R5_vos` has a lower descriptive median than `R8_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 13.941 ms vs 21.351 ms (34.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R2_simpleui` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 35.642 ms vs 42.054 ms (15.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (paging, real_2692, 2692 books): 21.654 ms vs 23.386 ms (7.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_cached_paging` (warm, real_2692, 2692 books): 12.879 ms vs 22.848 ms (43.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R2_simpleui` for `library_sequential_paging` (warm, real_2692, 2692 books): 18.941 ms vs 27.109 ms (30.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_cached_paging` (paging, real_2692, 2692 books): 42.026 ms vs 42.054 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R10_simpleui_vos_bookshelf` has a lower descriptive median than `R9_simpleui_vos` for `library_sequential_paging` (paging, real_2692, 2692 books): 21.083 ms vs 21.654 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_cached_paging` (warm, real_2692, 2692 books): 12.879 ms vs 19.111 ms (32.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R9_simpleui_vos` has a lower descriptive median than `R10_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, real_2692, 2692 books): 18.941 ms vs 22.769 ms (16.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (paging, real_2692, 2692 books): 11.960 ms vs 12.691 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (paging, real_2692, 2692 books): 11.857 ms vs 12.465 ms (4.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (warm, real_2692, 2692 books): 12.206 ms vs 12.448 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (warm, real_2692, 2692 books): 12.254 ms vs 13.005 ms (5.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
