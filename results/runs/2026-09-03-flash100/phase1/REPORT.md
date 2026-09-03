# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `26bb78442d6bed9f4933bc3c30a6209507dc0fecb152335c3fd708bd660db8d4`
Reader flash setting: `100`

Aggregated rows: 276; PASS=276; FAILED=0; UNSUPPORTED=0; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | paging | flat | 2000 | 10 | 201.000 | 3/3 | 90/90 | 121.325 | 134.407 | 114.579 | 143.138 | 115.809 | 125.296 | 113.070 | 129.635 |
| A_stock | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 120.375 | 129.594 | 117.072 | 132.700 | 115.959 | 123.139 | 112.126 | 127.026 |
| B_bookshelf | paging | flat | 2000 | 10 | 201.000 | 3/3 | 90/90 | 121.620 | 136.542 | 113.613 | 141.105 | 115.894 | 126.741 | 113.104 | 131.069 |
| B_bookshelf | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 120.988 | 131.003 | 116.325 | 135.375 | 115.799 | 123.190 | 112.360 | 125.501 |
| C_simpleui | paging | flat | 2000 | 8 | 251.000 | 3/3 | 90/90 | 122.516 | 143.924 | 114.642 | 235.062 | 114.986 | 131.265 | 111.014 | 222.651 |
| C_simpleui | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 121.733 | 138.018 | 116.513 | 139.953 | 115.153 | 127.247 | 111.165 | 129.636 |
| D_zenos | paging | flat | 2000 | 5 | 400.000 | 3/3 | 90/90 | 111.534 | 134.094 | 109.512 | 139.499 | 110.959 | 131.030 | 109.364 | 231.951 |
| D_zenos | paging | hierarchical | 2000 | 5 | 33.000 | 3/3 | 90/90 | 111.150 | 124.286 | 108.920 | 128.140 | 111.031 | 124.832 | 108.913 | 133.638 |
| E_project_title | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 112.589 | 114.570 | 110.092 | 118.601 | 112.344 | 114.029 | 109.554 | 118.485 |
| E_project_title | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 112.283 | 113.822 | 110.650 | 114.564 | 112.087 | 114.054 | 110.247 | 117.876 |
| F_vos | paging | flat | 2000 | 10 | 200.000 | 3/3 | 90/90 | 121.009 | 135.034 | 115.487 | 137.510 | 116.274 | 126.441 | 112.202 | 130.812 |
| F_vos | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 120.478 | 130.419 | 115.572 | 134.348 | 115.790 | 124.460 | 113.265 | 129.628 |
| G_simpleui_bookshelf | paging | flat | 2000 | 8 | 251.000 | 3/3 | 90/90 | 121.447 | 141.472 | 114.535 | 228.764 | 115.130 | 130.655 | 111.376 | 222.867 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 121.512 | 138.845 | 117.169 | 148.052 | 114.753 | 127.432 | 111.316 | 222.968 |
| H_zenos_bookshelf | paging | flat | 2000 | 5 | 400.000 | 3/3 | 90/90 | 111.219 | 135.358 | 108.927 | 139.996 | 110.758 | 131.088 | 109.491 | 139.778 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | 5 | 33.000 | 3/3 | 90/90 | 112.008 | 125.900 | 109.000 | 145.528 | 112.198 | 126.373 | 109.210 | 155.570 |
| I_vos_bookshelf | paging | flat | 2000 | 10 | 200.000 | 3/3 | 90/90 | 121.665 | 136.548 | 116.907 | 141.722 | 115.914 | 128.368 | 112.923 | 131.427 |
| I_vos_bookshelf | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 117.165 | 124.925 | 112.145 | 133.451 | 114.433 | 123.591 | 107.403 | 219.791 |
| J_simpleui_vos | paging | flat | 2000 | 8 | 250.000 | 3/3 | 90/90 | 122.134 | 146.845 | 114.654 | 235.484 | 114.764 | 130.927 | 111.963 | 133.821 |
| J_simpleui_vos | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 121.766 | 141.348 | 115.264 | 148.813 | 114.590 | 129.457 | 111.224 | 224.488 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | 8 | 250.000 | 3/3 | 90/90 | 122.719 | 144.472 | 114.601 | 268.887 | 114.819 | 130.697 | 112.677 | 137.930 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 120.648 | 139.243 | 114.243 | 141.271 | 115.133 | 128.382 | 111.300 | 130.908 |
| L_project_title_vos | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 111.971 | 114.287 | 109.707 | 221.803 | 111.679 | 113.559 | 109.898 | 120.388 |
| L_project_title_vos | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 112.388 | 113.335 | 109.918 | 115.566 | 111.607 | 113.864 | 109.245 | 117.519 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| B_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 1121.492 | 1133.268 | 982.662 | 1145.054 | 975.109 | 978.366 | 971.043 | 986.577 |
| B_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 119.190 | 121.204 | 111.503 | 131.771 | 112.648 | 114.859 | 109.895 | 121.580 |
| B_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 1108.506 | 1120.423 | 981.816 | 1136.539 | 974.769 | 977.206 | 969.256 | 982.295 |
| B_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 118.638 | 120.679 | 109.872 | 128.642 | 112.197 | 114.109 | 110.321 | 120.649 |
| G_simpleui_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 1123.420 | 1136.218 | 979.974 | 1148.921 | 975.185 | 978.095 | 971.420 | 1094.798 |
| G_simpleui_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 119.459 | 121.885 | 112.050 | 129.209 | 112.897 | 114.995 | 110.626 | 123.685 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 1111.464 | 1117.415 | 980.505 | 1122.936 | 974.466 | 976.645 | 968.959 | 981.818 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 118.901 | 122.813 | 110.744 | 128.047 | 111.946 | 113.808 | 110.125 | 222.500 |
| H_zenos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 1126.295 | 1145.914 | 1115.629 | 1166.213 | 975.375 | 978.696 | 971.497 | 986.517 |
| H_zenos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 119.608 | 122.113 | 111.324 | 130.391 | 112.610 | 114.435 | 110.071 | 122.270 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 1132.903 | 1169.868 | 1110.449 | 1184.231 | 975.619 | 996.145 | 970.927 | 1023.773 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 119.659 | 126.833 | 111.709 | 130.414 | 112.531 | 123.023 | 110.035 | 132.701 |
| I_vos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 1121.681 | 1150.746 | 983.626 | 1232.072 | 974.691 | 978.447 | 971.086 | 1084.910 |
| I_vos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 119.139 | 122.506 | 110.427 | 227.545 | 112.602 | 114.243 | 110.318 | 121.242 |
| I_vos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 1102.367 | 1130.850 | 974.440 | 1147.554 | 972.101 | 976.378 | 968.474 | 1084.707 |
| I_vos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 114.472 | 119.040 | 108.881 | 126.609 | 112.275 | 115.094 | 109.248 | 220.298 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 1123.513 | 1141.077 | 979.147 | 1164.666 | 975.207 | 979.703 | 971.884 | 1087.324 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 119.206 | 122.144 | 111.581 | 130.343 | 112.642 | 114.392 | 110.469 | 122.709 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 1112.624 | 1123.878 | 977.759 | 1134.801 | 974.501 | 976.947 | 969.042 | 1083.870 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 118.340 | 126.420 | 111.017 | 138.976 | 111.901 | 113.463 | 110.030 | 121.013 |

## Comparative Findings

- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 115.809 ms vs 115.894 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 121.325 ms vs 121.620 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 115.799 ms vs 115.959 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.375 ms vs 120.988 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 114.986 ms vs 115.809 ms (0.7% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 121.325 ms vs 122.516 ms (1.0% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 115.153 ms vs 115.959 ms (0.7% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.375 ms vs 121.733 ms (1.1% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 110.959 ms vs 115.809 ms (4.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 111.534 ms vs 121.325 ms (8.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 111.031 ms vs 115.959 ms (4.3% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 111.150 ms vs 120.375 ms (7.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 112.344 ms vs 115.809 ms (3.0% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 112.589 ms vs 121.325 ms (7.2% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 112.087 ms vs 115.959 ms (3.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 112.283 ms vs 120.375 ms (6.7% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 115.809 ms vs 116.274 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 121.009 ms vs 121.325 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 115.790 ms vs 115.959 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.375 ms vs 120.478 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 114.986 ms vs 115.130 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 121.447 ms vs 122.516 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.753 ms vs 115.153 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 121.512 ms vs 121.733 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (paging, flat, 2000 books): 110.758 ms vs 110.959 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, flat, 2000 books): 111.219 ms vs 111.534 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 111.031 ms vs 112.198 ms (1.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 111.150 ms vs 112.008 ms (0.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 115.914 ms vs 116.274 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 121.009 ms vs 121.665 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.433 ms vs 115.790 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 117.165 ms vs 120.478 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, flat, 2000 books): 114.764 ms vs 114.986 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 122.134 ms vs 122.516 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.590 ms vs 115.153 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 121.733 ms vs 121.766 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 114.764 ms vs 114.819 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 122.134 ms vs 122.719 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.590 ms vs 115.133 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.648 ms vs 121.766 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, flat, 2000 books): 111.679 ms vs 112.344 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (paging, flat, 2000 books): 111.971 ms vs 112.589 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, hierarchical, 2000 books): 111.607 ms vs 112.087 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 112.283 ms vs 112.388 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | paging | flat | 2000 | library_cached_paging | PASS | 90 | 115.809 | 114.265 | 125.296 | 113.070–129.635 |
| A_stock | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 121.325 | 117.975 | 134.407 | 114.579–143.138 |
| A_stock | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 122.557 | 122.522 | 125.196 | 122.513–125.856 |
| A_stock | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 115.959 | 114.378 | 123.139 | 112.126–127.026 |
| A_stock | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 120.375 | 118.248 | 129.594 | 117.072–132.700 |
| A_stock | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 117.188 | 116.174 | 118.510 | 115.921–118.840 |
| B_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 975.109 | 972.802 | 978.366 | 971.043–986.577 |
| B_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.648 | 111.385 | 114.859 | 109.895–121.580 |
| B_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 1121.492 | 1114.758 | 1133.268 | 982.662–1145.054 |
| B_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 119.190 | 117.737 | 121.204 | 111.503–131.771 |
| B_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 110.956 | 110.465 | 111.642 | 110.342–111.814 |
| B_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 115.894 | 113.874 | 126.741 | 113.104–131.069 |
| B_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 121.620 | 118.361 | 136.542 | 113.613–141.105 |
| B_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 240.448 | 240.112 | 242.299 | 240.028–242.762 |
| B_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 121.533 | 121.007 | 122.983 | 120.875–123.345 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 974.769 | 972.191 | 977.206 | 969.256–982.295 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.197 | 110.850 | 114.109 | 110.321–120.649 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 1108.506 | 983.263 | 1120.423 | 981.816–1136.539 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 118.638 | 116.011 | 120.679 | 109.872–128.642 |
| B_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 111.683 | 109.691 | 112.029 | 109.193–112.116 |
| B_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 115.799 | 114.062 | 123.190 | 112.360–125.501 |
| B_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 120.988 | 118.962 | 131.003 | 116.325–135.375 |
| B_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 193.854 | 193.778 | 194.876 | 193.759–195.131 |
| B_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 117.956 | 115.887 | 124.668 | 115.370–126.346 |
| C_simpleui | paging | flat | 2000 | library_cached_paging | PASS | 90 | 114.986 | 113.268 | 131.265 | 111.014–222.651 |
| C_simpleui | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 122.516 | 117.429 | 143.924 | 114.642–235.062 |
| C_simpleui | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 140.741 | 139.695 | 141.715 | 139.434–141.959 |
| C_simpleui | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 115.153 | 113.120 | 127.247 | 111.165–129.636 |
| C_simpleui | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 121.733 | 118.191 | 138.018 | 116.513–139.953 |
| C_simpleui | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 113.184 | 113.023 | 113.459 | 112.983–113.528 |
| D_zenos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 110.959 | 109.818 | 131.030 | 109.364–231.951 |
| D_zenos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 111.534 | 109.944 | 134.094 | 109.512–139.499 |
| D_zenos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 131.247 | 127.945 | 133.696 | 127.119–134.308 |
| D_zenos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 111.031 | 109.825 | 124.832 | 108.913–133.638 |
| D_zenos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 90 | 111.150 | 110.000 | 124.286 | 108.920–128.140 |
| D_zenos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 125.174 | 123.134 | 130.684 | 122.624–132.061 |
| E_project_title | paging | flat | 2000 | library_cached_paging | PASS | 90 | 112.344 | 110.770 | 114.029 | 109.554–118.485 |
| E_project_title | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 112.589 | 111.376 | 114.570 | 110.092–118.601 |
| E_project_title | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 112.178 | 110.511 | 113.524 | 110.094–113.861 |
| E_project_title | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 112.087 | 110.698 | 114.054 | 110.247–117.876 |
| E_project_title | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 112.283 | 111.138 | 113.822 | 110.650–114.564 |
| E_project_title | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 112.801 | 112.235 | 113.211 | 112.094–113.314 |
| F_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 116.274 | 114.235 | 126.441 | 112.202–130.812 |
| F_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 121.009 | 118.717 | 135.034 | 115.487–137.510 |
| F_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 125.419 | 123.301 | 125.585 | 122.771–125.627 |
| F_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 115.790 | 114.264 | 124.460 | 113.265–129.628 |
| F_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 120.478 | 117.654 | 130.419 | 115.572–134.348 |
| F_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 116.094 | 115.427 | 116.893 | 115.260–117.093 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 975.185 | 973.367 | 978.095 | 971.420–1094.798 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.897 | 111.644 | 114.995 | 110.626–123.685 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 1123.420 | 1112.115 | 1136.218 | 979.974–1148.921 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 119.459 | 116.867 | 121.885 | 112.050–129.209 |
| G_simpleui_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 225.525 | 224.881 | 225.758 | 224.720–225.816 |
| G_simpleui_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 115.130 | 113.244 | 130.655 | 111.376–222.867 |
| G_simpleui_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 121.447 | 117.455 | 141.472 | 114.535–228.764 |
| G_simpleui_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 250.923 | 247.877 | 252.777 | 247.115–253.241 |
| G_simpleui_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 144.039 | 142.822 | 146.669 | 142.518–147.326 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 974.466 | 972.603 | 976.645 | 968.959–981.818 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 111.946 | 110.764 | 113.808 | 110.125–222.500 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 1111.464 | 982.566 | 1117.415 | 980.505–1122.936 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 118.901 | 115.345 | 122.813 | 110.744–128.047 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 111.115 | 110.993 | 111.580 | 110.962–111.696 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 114.753 | 113.126 | 127.432 | 111.316–222.968 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 121.512 | 118.917 | 138.845 | 117.169–148.052 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 180.233 | 178.461 | 180.492 | 178.018–180.557 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 112.147 | 112.109 | 114.986 | 112.100–115.696 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 975.375 | 973.319 | 978.696 | 971.497–986.517 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.610 | 111.528 | 114.435 | 110.071–122.270 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 1126.295 | 1119.210 | 1145.914 | 1115.629–1166.213 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 119.608 | 117.799 | 122.113 | 111.324–130.391 |
| H_zenos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 118.516 | 118.029 | 119.285 | 117.907–119.477 |
| H_zenos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 110.758 | 109.896 | 131.088 | 109.491–139.778 |
| H_zenos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 111.219 | 109.867 | 135.358 | 108.927–139.996 |
| H_zenos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 263.006 | 257.983 | 266.178 | 256.727–266.971 |
| H_zenos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 131.536 | 129.155 | 131.821 | 128.560–131.892 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 975.619 | 973.300 | 996.145 | 970.927–1023.773 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.531 | 111.041 | 123.023 | 110.035–132.701 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 1132.903 | 1119.990 | 1169.868 | 1110.449–1184.231 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 119.659 | 117.645 | 126.833 | 111.709–130.414 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 118.871 | 118.313 | 121.309 | 118.173–121.919 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 112.198 | 110.207 | 126.373 | 109.210–155.570 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 90 | 112.008 | 110.292 | 125.900 | 109.000–145.528 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 220.332 | 217.290 | 221.386 | 216.529–221.650 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 124.297 | 123.222 | 126.408 | 122.953–126.936 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 974.691 | 972.768 | 978.447 | 971.086–1084.910 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.602 | 111.203 | 114.243 | 110.318–121.242 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 1121.681 | 1113.328 | 1150.746 | 983.626–1232.072 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 119.139 | 116.949 | 122.506 | 110.427–227.545 |
| I_vos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 111.564 | 110.944 | 112.174 | 110.789–112.326 |
| I_vos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 115.914 | 114.336 | 128.368 | 112.923–131.427 |
| I_vos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 121.665 | 119.255 | 136.548 | 116.907–141.722 |
| I_vos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 238.933 | 236.499 | 240.031 | 235.890–240.305 |
| I_vos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 124.497 | 124.108 | 126.181 | 124.011–126.602 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 972.101 | 969.438 | 976.378 | 968.474–1084.707 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.275 | 109.724 | 115.094 | 109.248–220.298 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 1102.367 | 984.452 | 1130.850 | 974.440–1147.554 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 114.472 | 112.600 | 119.040 | 108.881–126.609 |
| I_vos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 113.373 | 110.578 | 113.433 | 109.879–113.448 |
| I_vos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 114.433 | 109.679 | 123.591 | 107.403–219.791 |
| I_vos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 117.165 | 113.502 | 124.925 | 112.145–133.451 |
| I_vos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 194.569 | 190.911 | 197.117 | 189.996–197.754 |
| I_vos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 109.751 | 108.665 | 115.625 | 108.393–117.094 |
| J_simpleui_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 114.764 | 112.864 | 130.927 | 111.963–133.821 |
| J_simpleui_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 122.134 | 118.134 | 146.845 | 114.654–235.484 |
| J_simpleui_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 123.984 | 121.842 | 125.819 | 121.307–126.278 |
| J_simpleui_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 114.590 | 112.956 | 129.457 | 111.224–224.488 |
| J_simpleui_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 121.766 | 118.222 | 141.348 | 115.264–148.813 |
| J_simpleui_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 130.904 | 128.333 | 130.989 | 127.690–131.010 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 975.207 | 973.163 | 979.703 | 971.884–1087.324 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 112.642 | 110.966 | 114.392 | 110.469–122.709 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 1123.513 | 1113.230 | 1141.077 | 979.147–1164.666 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 119.206 | 117.645 | 122.144 | 111.581–130.343 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 227.069 | 226.455 | 228.714 | 226.301–229.125 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 114.819 | 113.463 | 130.697 | 112.677–137.930 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 122.719 | 117.921 | 144.472 | 114.601–268.887 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 224.736 | 223.866 | 227.683 | 223.648–228.420 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 120.852 | 119.786 | 121.448 | 119.520–121.597 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 974.501 | 972.343 | 976.947 | 969.042–1083.870 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 111.901 | 110.775 | 113.463 | 110.030–121.013 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 1112.624 | 983.629 | 1123.878 | 977.759–1134.801 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 118.340 | 115.053 | 126.420 | 111.017–138.976 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 112.229 | 111.290 | 113.331 | 111.055–113.606 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 115.133 | 113.376 | 128.382 | 111.300–130.908 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 120.648 | 117.664 | 139.243 | 114.243–141.271 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 198.715 | 196.841 | 198.875 | 196.373–198.915 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 130.590 | 126.669 | 130.864 | 125.689–130.933 |
| L_project_title_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 111.679 | 110.480 | 113.559 | 109.898–120.388 |
| L_project_title_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 111.971 | 110.641 | 114.287 | 109.707–221.803 |
| L_project_title_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 111.772 | 109.226 | 112.342 | 108.590–112.485 |
| L_project_title_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 111.607 | 110.561 | 113.864 | 109.245–117.519 |
| L_project_title_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 112.388 | 110.681 | 113.335 | 109.918–115.566 |
| L_project_title_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 111.789 | 111.464 | 112.623 | 111.383–112.831 |
| A_stock | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 797.072 | 786.578 | 916.279 | 783.955–946.081 |
| A_stock | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 926.746 | 914.918 | 1047.162 | 911.961–1077.266 |
| A_stock | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 9117.949 | 9112.956 | 9260.266 | 9111.707–9295.845 |
| A_stock | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9158.328 | 9155.879 | 9307.437 | 9155.266–9344.714 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 741.125 | 690.344 | 756.048 | 677.649–759.779 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 878.188 | 828.460 | 890.052 | 816.028–893.017 |
| A_stock | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 7317.031 | 7252.723 | 7321.067 | 7236.646–7322.076 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 7359.580 | 7297.017 | 7365.413 | 7281.376–7366.872 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 802.417 | 798.934 | 897.998 | 798.063–921.893 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 928.884 | 927.462 | 1027.382 | 927.107–1052.006 |
| B_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 81940.078 | 81915.750 | 82037.652 | 81909.668–82062.045 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 81990.308 | 81966.445 | 82085.894 | 81960.479–82109.790 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 829.313 | 790.879 | 916.883 | 781.271–938.775 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 963.069 | 925.116 | 1056.402 | 915.627–1079.736 |
| B_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 67104.490 | 67074.444 | 67365.383 | 67066.933–67430.606 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 67159.621 | 67122.795 | 67414.245 | 67113.588–67477.902 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 906.476 | 904.476 | 918.715 | 903.976–921.775 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1043.554 | 1040.534 | 1058.199 | 1039.779–1061.860 |
| C_simpleui | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 9458.514 | 9415.009 | 9521.571 | 9404.132–9537.335 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9503.322 | 9466.011 | 9571.213 | 9456.683–9588.186 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 797.679 | 743.176 | 807.981 | 729.550–810.557 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 938.001 | 882.413 | 947.706 | 868.516–950.133 |
| C_simpleui | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 7903.894 | 7863.963 | 7910.280 | 7853.980–7911.877 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 7952.305 | 7909.749 | 7957.447 | 7899.109–7958.733 |
| D_zenos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 861.615 | 828.420 | 917.303 | 820.122–931.225 |
| D_zenos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1082.162 | 1043.865 | 1135.794 | 1034.290–1149.202 |
| D_zenos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 8998.654 | 8899.496 | 9048.504 | 8874.707–9060.967 |
| D_zenos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9048.576 | 8944.876 | 9099.121 | 8918.951–9111.758 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 874.504 | 847.982 | 881.131 | 841.352–882.788 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1008.881 | 984.639 | 1016.546 | 978.579–1018.462 |
| D_zenos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 8734.283 | 8729.725 | 8743.613 | 8728.586–8745.946 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8782.956 | 8778.005 | 8791.343 | 8776.767–8793.440 |
| E_project_title | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 762.170 | 748.526 | 764.372 | 745.115–764.923 |
| E_project_title | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 880.041 | 869.412 | 884.206 | 866.755–885.248 |
| E_project_title | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 8577.267 | 8557.761 | 8580.549 | 8552.885–8581.369 |
| E_project_title | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8622.008 | 8602.281 | 8626.929 | 8597.349–8628.159 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 682.161 | 665.777 | 736.612 | 661.681–750.225 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 809.677 | 794.891 | 867.136 | 791.195–881.500 |
| E_project_title | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 6336.565 | 6327.395 | 6382.246 | 6325.103–6393.666 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 6380.312 | 6369.928 | 6423.906 | 6367.332–6434.804 |
| F_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 792.862 | 791.219 | 793.621 | 790.808–793.810 |
| F_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 922.169 | 919.051 | 926.361 | 918.272–927.409 |
| F_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 9168.217 | 9138.492 | 9168.964 | 9131.060–9169.151 |
| F_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9209.928 | 9183.139 | 9212.936 | 9176.442–9213.688 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 707.012 | 666.900 | 750.761 | 656.872–761.699 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 957.796 | 915.136 | 999.128 | 904.471–1009.461 |
| F_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 7400.653 | 7346.008 | 7428.509 | 7332.347–7435.474 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 7441.800 | 7390.308 | 7470.549 | 7377.435–7477.736 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 966.475 | 961.540 | 967.361 | 960.307–967.582 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1102.370 | 1098.935 | 1103.726 | 1098.076–1104.065 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 82520.483 | 82295.724 | 82543.953 | 82239.535–82549.821 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 82683.406 | 82460.338 | 82709.226 | 82404.572–82715.681 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 994.034 | 935.420 | 1056.394 | 920.766–1071.984 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1135.363 | 1074.773 | 1196.715 | 1059.626–1212.053 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 68052.583 | 67963.329 | 68199.613 | 67941.016–68236.370 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 68098.442 | 68013.482 | 68248.500 | 67992.242–68286.014 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 1097.681 | 1050.705 | 1112.216 | 1038.961–1115.850 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1308.481 | 1262.954 | 1326.226 | 1251.572–1330.662 |
| H_zenos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 82504.970 | 82469.748 | 82513.852 | 82460.943–82516.073 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 82561.100 | 82525.914 | 82566.949 | 82517.117–82568.411 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 987.644 | 931.586 | 993.287 | 917.571–994.697 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1125.677 | 1067.837 | 1131.705 | 1053.378–1133.212 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 70021.978 | 69647.808 | 70916.615 | 69554.265–71140.274 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 70068.089 | 69694.484 | 70967.839 | 69601.083–71192.777 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 990.811 | 940.660 | 1020.405 | 928.123–1027.803 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1119.090 | 1065.858 | 1147.733 | 1052.550–1154.894 |
| I_vos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 82353.361 | 82285.997 | 82548.089 | 82269.155–82596.771 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 82401.241 | 82333.907 | 82600.489 | 82317.073–82650.301 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 956.201 | 772.637 | 2508.545 | 726.746–2896.631 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1197.924 | 1019.985 | 2757.328 | 975.500–3147.180 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 67312.127 | 66971.639 | 69033.971 | 66886.517–69464.432 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 67362.898 | 67017.656 | 69082.309 | 66931.346–69512.161 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 1203.065 | 1050.559 | 1231.110 | 1012.432–1238.121 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1335.884 | 1186.484 | 1365.426 | 1149.134–1372.811 |
| J_simpleui_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 9734.442 | 9608.606 | 9734.660 | 9577.146–9734.714 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9780.945 | 9654.519 | 9802.152 | 9622.912–9807.454 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 1008.103 | 888.418 | 1226.275 | 858.497–1280.818 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1147.852 | 1031.003 | 1368.202 | 1001.790–1423.290 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 8209.143 | 8026.792 | 8385.297 | 7981.204–8429.336 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8254.295 | 8074.967 | 8434.178 | 8030.135–8479.149 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 1016.998 | 974.121 | 1106.862 | 963.401–1129.329 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1149.949 | 1107.724 | 1240.802 | 1097.167–1263.515 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 82804.129 | 82614.868 | 82878.357 | 82567.553–82896.914 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 82969.559 | 82775.009 | 83040.911 | 82726.372–83058.749 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 873.467 | 861.396 | 908.590 | 858.378–917.370 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 1013.713 | 1005.328 | 1049.211 | 1003.231–1058.085 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 67973.646 | 67934.754 | 68121.332 | 67925.031–68158.254 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 68026.656 | 67991.785 | 68168.456 | 67983.067–68203.906 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 701.591 | 693.590 | 760.011 | 691.590–774.616 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 823.062 | 815.887 | 880.615 | 814.093–895.004 |
| L_project_title_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 8472.012 | 8466.523 | 8637.082 | 8465.151–8678.349 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8515.322 | 8513.696 | 8683.356 | 8513.290–8725.365 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 658.589 | 623.493 | 676.202 | 614.719–680.605 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 897.507 | 864.208 | 916.529 | 855.883–921.285 |
| L_project_title_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 6419.827 | 6378.198 | 6422.624 | 6367.791–6423.323 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 6467.299 | 6424.424 | 6472.614 | 6413.705–6473.943 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|:--|--:|--:|
| A_stock | paging | flat | 2000 | post_init_idle | PASS | 3 | 10830.757 | 10883.947 | 10828.280–10897.245 | 16943.829 | 178880.000 |
| A_stock | paging | flat | 2000 | post_stress_idle | PASS | 3 | 11295.847 | 11316.656 | 11246.800–11321.858 | 13371.808 | 196640.000 |
| A_stock | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 9080.331 | 9088.400 | 8986.737–9090.417 | 9094.011 | 195136.000 |
| A_stock | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8259.604 | 8354.136 | 8257.706–8377.769 | 14604.751 | 180624.000 |
| B_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 16676.061 | 16685.107 | 16637.279–16687.369 | 33031.591 | 234144.000 |
| B_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 11119.614 | 11126.483 | 11071.567–11128.200 | 18222.540 | 180560.000 |
| B_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8593.825 | 8611.266 | 8505.247–8615.626 | 9447.491 | 183424.000 |
| B_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 13379.771 | 13388.618 | 13324.502–13390.830 | 27362.583 | 228704.000 |
| C_simpleui | paging | flat | 2000 | post_init_idle | PASS | 3 | 14778.456 | 14803.197 | 14740.187–14809.382 | 19170.043 | 188480.000 |
| C_simpleui | paging | flat | 2000 | post_stress_idle | PASS | 3 | 15175.009 | 15189.499 | 15157.997–15193.122 | 17559.038 | 203744.000 |
| C_simpleui | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 12476.378 | 12504.531 | 12458.397–12511.569 | 18861.358 | 187504.000 |
| C_simpleui | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 13228.552 | 13252.833 | 13167.751–13258.903 | 13242.251 | 198464.000 |
| D_zenos | paging | flat | 2000 | post_init_idle | PASS | 3 | 14205.243 | 14233.493 | 14122.923–14240.556 | 23207.642 | 186304.000 |
| D_zenos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 20315.224 | 20317.155 | 20218.208–20317.638 | 21746.196 | 211888.000 |
| D_zenos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 14286.438 | 14307.588 | 14251.653–14312.876 | 15840.145 | 190784.000 |
| D_zenos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 14943.462 | 14972.396 | 14929.060–14979.630 | 16445.795 | 202144.000 |
| E_project_title | paging | flat | 2000 | post_stress_idle | PASS | 3 | 11785.083 | 11841.399 | 11751.989–11855.478 | 25987.424 | 207600.000 |
| E_project_title | paging | flat | 2000 | post_init_idle | PASS | 3 | 11011.419 | 11049.631 | 10994.513–11059.185 | 16721.748 | 184288.000 |
| E_project_title | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 9227.368 | 9240.628 | 9211.786–9243.942 | 19824.568 | 201776.000 |
| E_project_title | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8340.950 | 8358.953 | 8337.454–8363.454 | 14578.688 | 175248.000 |
| F_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 12137.628 | 12163.250 | 12133.542–12169.655 | 14300.311 | 200176.000 |
| F_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 11740.511 | 11763.929 | 11681.370–11769.784 | 19879.675 | 185792.000 |
| F_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 9895.983 | 9916.493 | 9818.280–9921.620 | 9910.741 | 196400.000 |
| F_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 9005.761 | 9077.870 | 8965.397–9095.897 | 9592.252 | 182544.000 |
| G_simpleui_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 19515.341 | 19538.125 | 19501.251–19543.821 | 32919.953 | 247040.000 |
| G_simpleui_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 14917.466 | 14929.828 | 14916.571–14932.919 | 20136.986 | 190192.000 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 16216.001 | 16245.123 | 16191.938–16252.403 | 23458.994 | 244224.000 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 12742.603 | 12769.356 | 12703.739–12776.044 | 19862.546 | 181872.000 |
| H_zenos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 14464.964 | 14465.258 | 14446.362–14465.331 | 16732.659 | 191296.000 |
| H_zenos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 24286.528 | 24345.731 | 24253.173–24360.532 | 58088.561 | 261520.000 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 14521.421 | 14538.296 | 14483.636–14542.515 | 17094.901 | 190976.000 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 18212.341 | 18232.519 | 18181.220–18237.563 | 36646.556 | 234848.000 |
| I_vos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 17648.532 | 17648.688 | 17608.212–17648.728 | 41594.676 | 240128.000 |
| I_vos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 11931.583 | 11950.236 | 11867.278–11954.899 | 16822.732 | 190864.000 |
| I_vos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 15445.978 | 15497.440 | 14052.716–15510.306 | 33458.719 | 226736.000 |
| I_vos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 9369.427 | 9394.302 | 9135.599–9400.521 | 10740.036 | 184304.000 |
| J_simpleui_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 15835.583 | 15868.877 | 15807.868–15877.200 | 17611.710 | 206480.000 |
| J_simpleui_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 15389.050 | 15391.615 | 15314.511–15392.257 | 20604.623 | 186720.000 |
| J_simpleui_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 12952.464 | 12965.345 | 12918.503–12968.565 | 17958.394 | 187984.000 |
| J_simpleui_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 13805.103 | 13826.112 | 13743.810–13831.364 | 16204.094 | 202768.000 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 20231.478 | 20233.306 | 20230.435–20233.763 | 42754.352 | 253792.000 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 15579.771 | 15602.583 | 15530.310–15608.286 | 21070.216 | 192528.000 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 16843.665 | 16870.943 | 16813.372–16877.763 | 37436.107 | 230464.000 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 13216.493 | 13289.568 | 13194.856–13307.837 | 20281.362 | 182528.000 |
| L_project_title_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 11939.325 | 11959.731 | 11937.126–11964.833 | 19572.896 | 188464.000 |
| L_project_title_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 12731.591 | 12731.803 | 12663.310–12731.856 | 26685.066 | 213136.000 |
| L_project_title_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 10017.759 | 10021.593 | 9976.665–10022.552 | 20294.732 | 203008.000 |
| L_project_title_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8976.669 | 8983.053 | 8975.376–8984.649 | 14238.634 | 176848.000 |

## Data-derived comparisons

- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 115.809 ms vs 115.894 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 121.325 ms vs 121.620 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 115.799 ms vs 115.959 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.375 ms vs 120.988 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 114.986 ms vs 115.809 ms (0.7% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 121.325 ms vs 122.516 ms (1.0% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 115.153 ms vs 115.959 ms (0.7% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.375 ms vs 121.733 ms (1.1% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 110.959 ms vs 115.809 ms (4.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 111.534 ms vs 121.325 ms (8.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 111.031 ms vs 115.959 ms (4.3% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 111.150 ms vs 120.375 ms (7.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 112.344 ms vs 115.809 ms (3.0% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 112.589 ms vs 121.325 ms (7.2% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 112.087 ms vs 115.959 ms (3.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 112.283 ms vs 120.375 ms (6.7% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 115.809 ms vs 116.274 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 121.009 ms vs 121.325 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 115.790 ms vs 115.959 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.375 ms vs 120.478 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 114.986 ms vs 115.130 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 121.447 ms vs 122.516 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.753 ms vs 115.153 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 121.512 ms vs 121.733 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (paging, flat, 2000 books): 110.758 ms vs 110.959 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, flat, 2000 books): 111.219 ms vs 111.534 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 111.031 ms vs 112.198 ms (1.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 111.150 ms vs 112.008 ms (0.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 115.914 ms vs 116.274 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 121.009 ms vs 121.665 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.433 ms vs 115.790 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 117.165 ms vs 120.478 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, flat, 2000 books): 114.764 ms vs 114.986 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 122.134 ms vs 122.516 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.590 ms vs 115.153 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 121.733 ms vs 121.766 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 114.764 ms vs 114.819 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 122.134 ms vs 122.719 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 114.590 ms vs 115.133 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 120.648 ms vs 121.766 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, flat, 2000 books): 111.679 ms vs 112.344 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (paging, flat, 2000 books): 111.971 ms vs 112.589 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, hierarchical, 2000 books): 111.607 ms vs 112.087 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 112.283 ms vs 112.388 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
