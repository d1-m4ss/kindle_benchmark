# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `71c62562577d75d79b6dab0405876eeae7ea19ad7d5db59667c6c9cf1bd57e06`
Reader flash setting: `unset`

Aggregated rows: 1596; PASS=1440; FAILED=0; UNSUPPORTED=156; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 20.488 | 61.649 | 10.419 | 65.260 | 24.032 | 55.956 | 12.227 | 67.119 |
| A_stock | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 17.149 | 101.001 | 14.601 | 115.961 | 16.130 | 101.111 | 10.916 | 116.674 |
| A_stock | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| A_stock | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 20.148 | 59.118 | 12.005 | 63.059 | 23.637 | 60.618 | 10.425 | 67.578 |
| B_bookshelf | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 99.214 | 174.936 | 16.818 | 215.823 | 17.782 | 65.530 | 10.074 | 150.024 |
| B_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 16.123 | 34.594 | 7.859 | 40.213 | 13.053 | 31.822 | 11.113 | 34.664 |
| C_simpleui | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 15.820 | 26.616 | 9.529 | 28.796 | 16.173 | 32.850 | 7.832 | 50.242 |
| C_simpleui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 16.100 | 30.556 | 6.536 | 31.484 | 16.085 | 29.410 | 5.790 | 30.545 |
| D_zenos | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 16.007 | 18.778 | 7.513 | 28.480 | 16.131 | 27.049 | 5.757 | 28.370 |
| D_zenos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 16.102 | 16.150 | 16.028 | 16.680 | 16.087 | 16.151 | 15.971 | 16.654 |
| E_project_title | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 16.212 | 16.488 | 16.050 | 16.557 | 16.081 | 16.109 | 16.018 | 16.646 |
| E_project_title | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 21.357 | 45.556 | 11.488 | 52.296 | 20.129 | 45.383 | 11.189 | 51.717 |
| F_vos | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 99.036 | 151.321 | 61.217 | 166.669 | 16.181 | 33.181 | 11.211 | 64.075 |
| F_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 16.148 | 37.342 | 8.305 | 47.395 | 14.022 | 36.093 | 10.485 | 38.511 |
| G_simpleui_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 16.149 | 23.469 | 9.754 | 28.319 | 16.145 | 32.811 | 8.547 | 33.305 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 16.095 | 31.043 | 6.340 | 32.601 | 15.831 | 30.500 | 6.313 | 33.175 |
| H_zenos_bookshelf | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 15.907 | 19.115 | 5.371 | 30.077 | 16.103 | 27.046 | 7.454 | 29.023 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 19.729 | 43.902 | 12.300 | 47.156 | 21.423 | 39.952 | 10.340 | 49.573 |
| I_vos_bookshelf | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 111.184 | 141.989 | 82.405 | 149.975 | 16.119 | 35.027 | 9.421 | 51.119 |
| I_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 16.098 | 30.645 | 8.345 | 38.088 | 13.886 | 30.821 | 9.653 | 33.749 |
| J_simpleui_vos | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 16.137 | 33.410 | 14.463 | 34.848 | 16.130 | 27.397 | 6.793 | 28.445 |
| J_simpleui_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 16.044 | 31.406 | 7.300 | 37.045 | 13.165 | 31.567 | 9.671 | 47.792 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 12.768 | 28.020 | 7.516 | 34.138 | 13.431 | 28.995 | 11.308 | 32.995 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 16.090 | 16.139 | 11.701 | 16.215 | 16.073 | 16.115 | 15.840 | 16.657 |
| L_project_title_vos | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 16.023 | 16.073 | 10.936 | 16.085 | 16.110 | 16.249 | 15.982 | 16.505 |
| L_project_title_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| M_leanui | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 16.161 | 16.241 | 14.461 | 19.255 | 16.091 | 16.150 | 15.938 | 16.633 |
| M_leanui | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 15.871 | 15.982 | 15.532 | 16.010 | 16.111 | 16.178 | 15.766 | 16.523 |
| M_leanui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| M_leanui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| N_m1n1mal | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 21.692 | 60.724 | 11.059 | 67.986 | 21.684 | 63.366 | 11.651 | 70.661 |
| N_m1n1mal | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 81.763 | 105.200 | 17.956 | 120.248 | 16.180 | 92.277 | 10.427 | 115.902 |
| N_m1n1mal | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| N_m1n1mal | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| B_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 132.964 | 154.835 | 127.806 | 243.275 | 148.384 | 154.310 | 127.490 | 159.179 |
| B_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 20.996 | 29.699 | 18.762 | 35.229 | 19.478 | 28.350 | 16.810 | 37.394 |
| B_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 148.389 | 149.522 | 132.738 | 150.121 | 132.800 | 149.209 | 121.369 | 183.315 |
| B_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 18.824 | 27.998 | 14.573 | 33.889 | 18.582 | 27.051 | 10.969 | 33.661 |
| B_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 132.658 | 161.819 | 123.712 | 241.914 | 131.935 | 133.666 | 106.140 | 240.412 |
| G_simpleui_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 16.144 | 16.314 | 9.472 | 111.286 | 16.034 | 16.785 | 7.009 | 102.446 |
| G_simpleui_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 132.851 | 149.096 | 128.977 | 149.231 | 132.606 | 138.845 | 113.135 | 184.835 |
| G_simpleui_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 13.948 | 18.671 | 10.902 | 22.015 | 16.138 | 16.366 | 9.500 | 60.392 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 133.036 | 141.237 | 118.610 | 179.801 | 133.925 | 144.094 | 116.232 | 161.596 |
| H_zenos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 16.165 | 21.225 | 7.520 | 27.097 | 16.129 | 17.182 | 8.833 | 45.475 |
| H_zenos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 133.682 | 139.865 | 132.202 | 140.372 | 133.009 | 144.368 | 122.354 | 179.163 |
| H_zenos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 19.682 | 24.506 | 8.369 | 25.235 | 16.032 | 18.970 | 6.464 | 27.324 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 133.587 | 158.064 | 126.270 | 242.956 | 132.436 | 153.509 | 122.404 | 181.045 |
| I_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 41.260 | 56.574 | 11.949 | 75.291 | 16.133 | 16.883 | 9.969 | 29.570 |
| I_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 147.564 | 153.243 | 132.688 | 157.182 | 133.355 | 151.411 | 125.000 | 208.191 |
| I_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 35.242 | 40.082 | 17.961 | 40.749 | 23.485 | 35.030 | 18.260 | 51.634 |
| I_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 132.351 | 163.108 | 119.955 | 244.388 | 132.096 | 134.221 | 114.974 | 239.417 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 16.159 | 17.301 | 4.773 | 124.777 | 16.117 | 17.060 | 5.057 | 124.942 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 140.821 | 149.349 | 129.239 | 149.466 | 132.258 | 138.379 | 111.560 | 202.624 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 15.034 | 20.072 | 10.298 | 23.257 | 16.127 | 16.388 | 9.465 | 65.849 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| A_stock | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| A_stock | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| A_stock | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
| B_bookshelf | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| B_bookshelf | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| B_bookshelf | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| C_simpleui | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| D_zenos | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| D_zenos | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| D_zenos | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| D_zenos | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| D_zenos | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| D_zenos | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| E_project_title | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| E_project_title | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| E_project_title | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
| F_vos | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| F_vos | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| F_vos | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
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
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| I_vos_bookshelf | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| I_vos_bookshelf | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_cached_paging_anim_off | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| I_vos_bookshelf | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
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
| L_project_title_vos | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| L_project_title_vos | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| L_project_title_vos | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
| M_leanui | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| M_leanui | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| M_leanui | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |
| N_m1n1mal | warm | flat | 2000 | start_to_home | UNSUPPORTED | — |
| N_m1n1mal | warm | flat | 50 | start_to_home | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 2000 | start_to_home | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |
| N_m1n1mal | warm | hierarchical | 50 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 23.637 ms vs 24.032 ms (1.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 20.148 ms vs 20.488 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 17.782 ms (9.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 17.149 ms vs 99.214 ms (82.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 13.053 ms vs 24.032 ms (45.7% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.123 ms vs 20.488 ms (21.3% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.173 ms (0.3% lower) (UX-level comparison: books/page differs, 10.000 vs 9.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 15.820 ms vs 17.149 ms (7.7% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 16.085 ms vs 24.032 ms (33.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.100 ms vs 20.488 ms (21.4% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.131 ms (0.0% lower) (UX-level comparison: books/page differs, 10.000 vs 5.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 16.007 ms vs 17.149 ms (6.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 16.087 ms vs 24.032 ms (33.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.102 ms vs 20.488 ms (21.4% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 16.081 ms vs 16.130 ms (0.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 16.212 ms vs 17.149 ms (5.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 20.129 ms vs 24.032 ms (16.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 20.488 ms vs 21.357 ms (4.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.181 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 17.149 ms vs 99.036 ms (82.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.053 ms vs 14.022 ms (6.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 16.123 ms vs 16.148 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 16.145 ms vs 16.173 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 15.820 ms vs 16.149 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 2000 books): 15.831 ms vs 16.085 ms (1.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 2000 books): 16.095 ms vs 16.100 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 16.103 ms vs 16.131 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 50 books): 15.907 ms vs 16.007 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 20.129 ms vs 21.423 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 19.729 ms vs 21.357 ms (7.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 16.119 ms vs 16.181 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 99.036 ms vs 111.184 ms (10.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 13.053 ms vs 13.886 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 16.098 ms vs 16.123 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.173 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 15.820 ms vs 16.137 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 13.165 ms vs 13.886 ms (5.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 16.044 ms vs 16.098 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 13.431 ms vs 16.130 ms (16.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 12.768 ms vs 16.137 ms (20.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 2000 books): 16.073 ms vs 16.087 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 2000 books): 16.090 ms vs 16.102 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 50 books): 16.081 ms vs 16.110 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 50 books): 16.023 ms vs 16.212 ms (1.2% lower).

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.757 | 7.382 | 10.128 | 7.288–10.721 |
| A_stock | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 12.100 | 10.794 | 15.111 | 10.467–15.864 |
| A_stock | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 6.998 | 6.196 | 11.873 | 5.996–13.092 |
| A_stock | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 14.496 | 13.356 | 15.789 | 13.071–16.112 |
| A_stock | warm | flat | 2000 | change_sort_mode | PASS | 10 | 89.349 | 83.445 | 137.177 | 82.505–139.216 |
| A_stock | warm | flat | 2000 | close_book | PASS | 10 | 66.702 | 64.532 | 68.269 | 64.127–71.943 |
| A_stock | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.661 | 16.640 | 16.672 | 16.627–16.681 |
| A_stock | warm | flat | 2000 | home_to_library | PASS | 10 | 92.061 | 53.121 | 204.351 | 40.301–233.393 |
| A_stock | warm | flat | 2000 | library_cached_paging | PASS | 30 | 24.032 | 14.447 | 55.956 | 12.227–67.119 |
| A_stock | warm | flat | 2000 | library_first_render | PASS | 10 | 38.930 | 37.905 | 70.603 | 37.474–89.336 |
| A_stock | warm | flat | 2000 | library_folder_back | PASS | 10 | 72.168 | 70.403 | 100.641 | 68.562–102.254 |
| A_stock | warm | flat | 2000 | library_folder_enter | PASS | 10 | 5.533 | 3.596 | 18.598 | 3.465–38.721 |
| A_stock | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 20.488 | 16.765 | 61.649 | 10.419–65.260 |
| A_stock | warm | flat | 2000 | open_book | PASS | 10 | 52.801 | 51.783 | 57.745 | 51.539–59.486 |
| A_stock | warm | flat | 2000 | open_book_minimal | PASS | 10 | 59.309 | 56.408 | 65.228 | 56.350–65.657 |
| A_stock | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.657 | 15.492 | 16.664 | 5.173–16.665 |
| A_stock | warm | flat | 2000 | repeated_nav | PASS | 2 | 309.757 | 298.773 | 320.742 | 296.027–323.488 |
| A_stock | warm | flat | 50 | change_sort_mode | PASS | 10 | 37.465 | 27.203 | 51.993 | 24.167–53.528 |
| A_stock | warm | flat | 50 | close_book | PASS | 10 | 17.201 | 13.284 | 22.369 | 12.929–27.684 |
| A_stock | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.665 | 16.609 | 16.688 | 16.567–16.707 |
| A_stock | warm | flat | 50 | home_to_library | PASS | 10 | 23.008 | 20.681 | 34.966 | 20.189–35.233 |
| A_stock | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.130 | 12.656 | 101.111 | 10.916–116.674 |
| A_stock | warm | flat | 50 | library_first_render | PASS | 10 | 24.864 | 21.288 | 48.677 | 20.230–49.579 |
| A_stock | warm | flat | 50 | library_folder_back | PASS | 10 | 27.635 | 23.025 | 34.207 | 22.411–35.240 |
| A_stock | warm | flat | 50 | library_folder_enter | PASS | 10 | 5.010 | 3.668 | 24.829 | 3.375–25.239 |
| A_stock | warm | flat | 50 | library_sequential_paging | PASS | 5 | 17.149 | 15.163 | 101.001 | 14.601–115.961 |
| A_stock | warm | flat | 50 | open_book | PASS | 10 | 27.318 | 22.610 | 40.123 | 22.194–44.255 |
| A_stock | warm | flat | 50 | open_book_minimal | PASS | 10 | 34.439 | 31.414 | 43.080 | 25.100–48.200 |
| A_stock | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.654 | 15.616 | 17.667 | 6.632–26.366 |
| A_stock | warm | flat | 50 | repeated_nav | PASS | 2 | 187.857 | 165.541 | 210.174 | 159.962–215.753 |
| A_stock | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.151 | 6.716 | 26.271 | 6.257–30.658 |
| A_stock | warm | hierarchical | 2000 | close_book | PASS | 10 | 16.157 | 12.524 | 24.559 | 12.330–39.263 |
| A_stock | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.669 | 16.553 | 16.842 | 16.382–16.946 |
| A_stock | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.085 | 10.435 | 21.716 | 8.921–23.232 |
| A_stock | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.105 | 10.555 | 21.690 | 10.356–21.842 |
| A_stock | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.284 | 10.350 | 25.949 | 8.952–28.642 |
| A_stock | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.537 | 4.882 | 25.363 | 4.283–25.968 |
| A_stock | warm | hierarchical | 2000 | open_book | PASS | 10 | 44.815 | 41.226 | 50.991 | 40.222–51.502 |
| A_stock | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 44.510 | 32.008 | 67.285 | 31.265–116.907 |
| A_stock | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.643 | 4.548 | 16.737 | 3.876–16.762 |
| A_stock | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 15.965 | 9.160 | 23.749 | 8.749–24.220 |
| A_stock | warm | hierarchical | 50 | close_book | PASS | 10 | 13.821 | 10.308 | 20.249 | 9.600–23.665 |
| A_stock | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.661 | 16.619 | 26.666 | 16.579–116.633 |
| A_stock | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.100 | 10.556 | 21.699 | 8.796–23.272 |
| A_stock | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.092 | 10.100 | 22.000 | 10.057–22.028 |
| A_stock | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.617 | 10.216 | 23.168 | 10.201–23.492 |
| A_stock | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.104 | 9.468 | 25.447 | 9.256–26.137 |
| A_stock | warm | hierarchical | 50 | open_book | PASS | 10 | 32.304 | 25.965 | 36.659 | 24.919–38.017 |
| A_stock | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 41.825 | 37.868 | 46.473 | 32.330–50.010 |
| A_stock | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.660 | 9.562 | 17.524 | 9.549–24.810 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.821 | 7.479 | 10.305 | 7.394–10.926 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 15.504 | 15.384 | 16.012 | 15.354–16.139 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 6.080 | 5.821 | 11.498 | 5.756–12.852 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 13.519 | 9.684 | 15.581 | 8.725–16.096 |
| B_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 148.384 | 131.752 | 154.310 | 127.490–159.179 |
| B_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 19.478 | 17.926 | 28.350 | 16.810–37.394 |
| B_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 26.157 | 22.562 | 121.189 | 22.115–122.765 |
| B_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 132.964 | 132.453 | 154.835 | 127.806–243.275 |
| B_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 20.996 | 19.030 | 29.699 | 18.762–35.229 |
| B_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 88.332 | 79.025 | 128.469 | 70.665–129.251 |
| B_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 45.223 | 42.956 | 227.335 | 42.403–346.109 |
| B_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 12.712 | 11.658 | 13.726 | 11.254–14.892 |
| B_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.657 | 16.616 | 16.669 | 16.593–16.677 |
| B_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 106.228 | 51.575 | 161.086 | 51.029–260.268 |
| B_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 23.637 | 14.398 | 60.618 | 10.425–67.578 |
| B_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 38.583 | 37.547 | 75.079 | 37.320–90.243 |
| B_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 82.409 | 68.062 | 98.634 | 67.661–99.260 |
| B_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 5.393 | 3.810 | 17.023 | 3.630–34.824 |
| B_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 20.148 | 17.812 | 59.118 | 12.005–63.059 |
| B_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 157.633 | 106.048 | 216.549 | 96.921–233.001 |
| B_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 122.329 | 67.107 | 140.358 | 62.462–148.890 |
| B_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 22.950 | 22.039 | 24.477 | 21.602–25.890 |
| B_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.666 | 16.650 | 16.688 | 16.647–16.725 |
| B_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 322.582 | 300.852 | 344.313 | 295.419–349.746 |
| B_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.800 | 131.891 | 149.209 | 121.369–183.315 |
| B_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 18.582 | 11.397 | 27.051 | 10.969–33.661 |
| B_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 23.119 | 21.187 | 56.161 | 21.038–62.016 |
| B_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 148.389 | 132.877 | 149.522 | 132.738–150.121 |
| B_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 18.824 | 14.627 | 27.998 | 14.573–33.889 |
| B_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 39.105 | 28.078 | 54.326 | 25.049–56.545 |
| B_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 61.947 | 21.866 | 66.732 | 20.275–67.259 |
| B_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 9.134 | 7.539 | 10.380 | 6.112–10.823 |
| B_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.667 | 16.633 | 16.685 | 16.624–16.697 |
| B_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 22.731 | 20.176 | 35.707 | 19.530–36.100 |
| B_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 17.782 | 13.189 | 65.530 | 10.074–150.024 |
| B_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 25.029 | 22.649 | 44.711 | 21.519–46.104 |
| B_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 34.142 | 24.724 | 37.389 | 23.857–37.403 |
| B_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 4.170 | 3.522 | 13.017 | 3.321–16.968 |
| B_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 99.214 | 17.778 | 174.936 | 16.818–215.823 |
| B_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 75.199 | 63.290 | 83.118 | 62.614–83.883 |
| B_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 42.317 | 35.025 | 65.514 | 32.945–67.428 |
| B_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 20.585 | 19.699 | 22.545 | 19.372–23.913 |
| B_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.663 | 16.637 | 16.716 | 16.559–16.739 |
| B_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 189.755 | 174.930 | 204.580 | 171.224–208.286 |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.151 | 12.682 | 48.846 | 12.115–52.892 |
| B_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.096 | 6.311 | 26.193 | 5.817–26.626 |
| B_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 21.037 | 20.239 | 84.410 | 20.141–88.162 |
| B_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 16.140 | 15.858 | 16.374 | 15.272–16.452 |
| B_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.660 | 16.636 | 16.777 | 16.623–16.891 |
| B_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.107 | 9.858 | 22.341 | 8.107–24.273 |
| B_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.110 | 10.360 | 22.083 | 10.260–22.384 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.555 | 10.181 | 24.673 | 9.485–28.956 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.372 | 7.131 | 25.459 | 3.962–27.837 |
| B_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 77.747 | 62.980 | 82.681 | 51.326–94.337 |
| B_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 48.948 | 40.753 | 65.087 | 39.048–68.067 |
| B_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.901 | 16.742 | 17.010 | 16.739–17.139 |
| B_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.654 | 16.601 | 16.754 | 16.512–16.792 |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 16.172 | 14.930 | 38.734 | 14.148–46.190 |
| B_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.053 | 9.442 | 22.682 | 9.028–23.127 |
| B_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 18.151 | 15.260 | 52.268 | 15.025–72.371 |
| B_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 10.675 | 7.591 | 14.024 | 6.660–16.431 |
| B_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.659 | 16.628 | 16.685 | 16.595–16.690 |
| B_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.103 | 10.052 | 22.175 | 8.238–23.954 |
| B_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.088 | 9.777 | 22.287 | 9.637–22.489 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.643 | 10.852 | 23.287 | 10.585–23.314 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.761 | 10.314 | 25.244 | 9.093–26.663 |
| B_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 63.075 | 49.584 | 70.547 | 33.109–72.014 |
| B_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 45.393 | 31.169 | 48.875 | 30.517–51.817 |
| B_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 19.906 | 17.431 | 22.859 | 17.235–26.625 |
| B_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.662 | 16.651 | 16.679 | 16.651–16.684 |
| C_simpleui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.596 | 9.158 | 10.412 | 9.049–10.616 |
| C_simpleui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 25.008 | 19.966 | 31.273 | 18.706–32.839 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.623 | 7.196 | 8.162 | 7.089–8.297 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 25.965 | 20.063 | 31.297 | 18.587–32.630 |
| C_simpleui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 75.320 | 64.145 | 81.818 | 63.978–90.730 |
| C_simpleui | warm | flat | 2000 | close_book | PASS | 10 | 214.121 | 91.897 | 246.953 | 83.080–269.021 |
| C_simpleui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.654 | 16.595 | 32.408 | 16.248–173.855 |
| C_simpleui | warm | flat | 2000 | home_to_library | PASS | 10 | 16.652 | 12.925 | 30.575 | 12.864–30.659 |
| C_simpleui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.053 | 11.435 | 31.822 | 11.113–34.664 |
| C_simpleui | warm | flat | 2000 | library_first_render | PASS | 10 | 78.130 | 59.583 | 83.813 | 57.267–92.248 |
| C_simpleui | warm | flat | 2000 | library_folder_back | PASS | 10 | 89.000 | 70.617 | 95.370 | 69.318–98.814 |
| C_simpleui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.115 | 8.992 | 12.811 | 8.055–13.238 |
| C_simpleui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.123 | 8.664 | 34.594 | 7.859–40.213 |
| C_simpleui | warm | flat | 2000 | open_book | PASS | 10 | 128.351 | 94.367 | 168.605 | 83.664–177.668 |
| C_simpleui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 90.478 | 76.102 | 116.177 | 65.340–136.356 |
| C_simpleui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.650 | 15.785 | 50.894 | 8.130–358.627 |
| C_simpleui | warm | flat | 2000 | repeated_nav | PASS | 2 | 701.207 | 662.121 | 740.293 | 652.350–750.064 |
| C_simpleui | warm | flat | 2000 | start_to_home | PASS | 10 | 16.657 | 13.791 | 16.679 | 6.568–16.697 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 10 | 31.930 | 18.941 | 41.750 | 18.350–45.561 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 10 | 57.989 | 39.035 | 130.334 | 36.943–136.667 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.647 | 15.762 | 23.983 | 7.951–89.680 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 10 | 16.673 | 13.729 | 29.632 | 13.009–29.698 |
| C_simpleui | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.173 | 9.793 | 32.850 | 7.832–50.242 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 10 | 41.045 | 32.000 | 50.466 | 30.675–56.941 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 10 | 20.626 | 15.181 | 27.544 | 15.137–28.517 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.917 | 10.221 | 25.122 | 9.329–27.049 |
| C_simpleui | warm | flat | 50 | library_sequential_paging | PASS | 5 | 15.820 | 9.771 | 26.616 | 9.529–28.796 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 10 | 118.820 | 90.553 | 129.620 | 73.233–131.048 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 10 | 44.668 | 39.829 | 73.512 | 36.019–78.198 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 10 | 17.388 | 16.588 | 18.358 | 16.482–18.698 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 2 | 412.791 | 369.399 | 456.183 | 358.551–467.031 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 10 | 16.656 | 14.615 | 16.712 | 6.170–16.717 |
| C_simpleui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 31.256 | 23.600 | 39.527 | 23.027–41.631 |
| C_simpleui | warm | hierarchical | 2000 | close_book | PASS | 10 | 43.410 | 41.450 | 51.055 | 41.080–101.839 |
| C_simpleui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.659 | 15.706 | 22.639 | 7.521–76.140 |
| C_simpleui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.660 | 15.201 | 28.064 | 14.090–28.094 |
| C_simpleui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.818 | 23.602 | 41.837 | 20.837–44.684 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 22.989 | 21.552 | 33.484 | 21.008–34.324 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 14.353 | 12.393 | 23.687 | 11.779–28.282 |
| C_simpleui | warm | hierarchical | 2000 | open_book | PASS | 10 | 58.674 | 55.068 | 103.909 | 53.093–105.673 |
| C_simpleui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 41.060 | 37.450 | 47.868 | 37.347–51.311 |
| C_simpleui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.649 | 14.136 | 83.631 | 12.496–96.886 |
| C_simpleui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.663 | 15.706 | 16.711 | 7.258–16.713 |
| C_simpleui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 14.742 | 9.739 | 25.216 | 9.489–25.510 |
| C_simpleui | warm | hierarchical | 50 | close_book | PASS | 10 | 36.119 | 32.838 | 45.920 | 32.048–82.003 |
| C_simpleui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.651 | 15.545 | 22.229 | 5.923–72.233 |
| C_simpleui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.659 | 15.977 | 27.599 | 12.911–27.892 |
| C_simpleui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.826 | 23.939 | 41.495 | 20.971–44.559 |
| C_simpleui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.997 | 10.179 | 25.095 | 8.354–26.181 |
| C_simpleui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.945 | 8.157 | 24.180 | 6.596–25.970 |
| C_simpleui | warm | hierarchical | 50 | open_book | PASS | 10 | 53.291 | 48.441 | 61.510 | 45.131–67.962 |
| C_simpleui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 43.037 | 36.583 | 64.757 | 32.494–65.552 |
| C_simpleui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.651 | 15.973 | 73.640 | 10.221–75.301 |
| C_simpleui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.664 | 15.674 | 16.680 | 6.995–16.705 |
| D_zenos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 31.833 | 31.831 | 31.967 | 31.831–32.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 33.544 | 33.379 | 33.546 | 33.338–33.547 |
| D_zenos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 29.452 | 29.127 | 34.795 | 29.046–36.131 |
| D_zenos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.015 | 31.986 | 32.108 | 31.979–32.131 |
| D_zenos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 79.142 | 64.691 | 84.986 | 63.476–85.433 |
| D_zenos | warm | flat | 2000 | close_book | PASS | 10 | 27.516 | 23.447 | 33.697 | 22.308–49.396 |
| D_zenos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 33.311 | 27.152 | 33.324 | 25.371–33.328 |
| D_zenos | warm | flat | 2000 | home_to_library | PASS | 10 | 37.502 | 37.231 | 54.447 | 36.035–55.288 |
| D_zenos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 16.085 | 6.968 | 29.410 | 5.790–30.545 |
| D_zenos | warm | flat | 2000 | library_first_render | PASS | 10 | 49.080 | 32.363 | 65.444 | 30.800–69.083 |
| D_zenos | warm | flat | 2000 | library_folder_back | PASS | 10 | 52.405 | 49.996 | 63.635 | 49.932–64.076 |
| D_zenos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 40.251 | 31.943 | 47.910 | 19.674–47.923 |
| D_zenos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.100 | 7.124 | 30.556 | 6.536–31.484 |
| D_zenos | warm | flat | 2000 | open_book | PASS | 10 | 72.112 | 42.736 | 75.459 | 41.220–75.579 |
| D_zenos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 69.773 | 42.831 | 74.140 | 41.073–77.840 |
| D_zenos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 33.177 | 30.812 | 42.365 | 11.112–46.408 |
| D_zenos | warm | flat | 2000 | repeated_nav | PASS | 2 | 170.526 | 167.448 | 173.604 | 166.678–174.374 |
| D_zenos | warm | flat | 2000 | start_to_home | PASS | 10 | 29.197 | 27.372 | 30.382 | 26.972–32.500 |
| D_zenos | warm | flat | 50 | change_sort_mode | PASS | 10 | 32.813 | 21.674 | 43.840 | 21.270–44.205 |
| D_zenos | warm | flat | 50 | close_book | PASS | 10 | 30.088 | 25.178 | 31.788 | 23.625–32.065 |
| D_zenos | warm | flat | 50 | close_quick_settings | PASS | 10 | 33.321 | 29.040 | 33.349 | 28.458–33.363 |
| D_zenos | warm | flat | 50 | home_to_library | PASS | 10 | 33.604 | 32.205 | 45.722 | 19.951–48.060 |
| D_zenos | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.131 | 9.413 | 27.049 | 5.757–28.370 |
| D_zenos | warm | flat | 50 | library_first_render | PASS | 10 | 35.587 | 32.656 | 46.443 | 32.592–47.196 |
| D_zenos | warm | flat | 50 | library_folder_back | PASS | 10 | 33.335 | 32.210 | 43.576 | 22.345–43.577 |
| D_zenos | warm | flat | 50 | library_folder_enter | PASS | 10 | 33.292 | 22.602 | 44.882 | 22.042–44.896 |
| D_zenos | warm | flat | 50 | library_sequential_paging | PASS | 9 | 16.007 | 8.336 | 18.778 | 7.513–28.480 |
| D_zenos | warm | flat | 50 | open_book | PASS | 10 | 62.684 | 56.976 | 66.906 | 56.038–67.731 |
| D_zenos | warm | flat | 50 | open_book_minimal | PASS | 10 | 60.120 | 37.383 | 64.899 | 34.210–65.664 |
| D_zenos | warm | flat | 50 | open_quick_settings | PASS | 10 | 33.191 | 32.688 | 37.238 | 29.183–38.475 |
| D_zenos | warm | flat | 50 | repeated_nav | PASS | 2 | 166.837 | 166.727 | 166.946 | 166.700–166.973 |
| D_zenos | warm | flat | 50 | start_to_home | PASS | 10 | 33.074 | 15.097 | 33.339 | 12.048–35.044 |
| D_zenos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 32.772 | 20.594 | 45.067 | 20.466–45.508 |
| D_zenos | warm | hierarchical | 2000 | close_book | PASS | 10 | 33.715 | 32.306 | 35.658 | 31.875–36.760 |
| D_zenos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 33.307 | 31.129 | 33.335 | 30.310–33.337 |
| D_zenos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 33.619 | 33.562 | 47.562 | 33.557–47.838 |
| D_zenos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.777 | 19.689 | 45.748 | 18.094–47.252 |
| D_zenos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 33.319 | 32.002 | 34.591 | 20.655–45.286 |
| D_zenos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 33.353 | 20.708 | 44.882 | 20.554–45.509 |
| D_zenos | warm | hierarchical | 2000 | open_book | PASS | 10 | 61.936 | 39.353 | 69.446 | 38.231–72.370 |
| D_zenos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 55.805 | 37.976 | 65.125 | 34.659–68.251 |
| D_zenos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 33.346 | 33.118 | 36.055 | 31.199–36.677 |
| D_zenos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 32.948 | 18.100 | 33.096 | 17.470–33.178 |
| D_zenos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 32.747 | 22.694 | 42.792 | 22.283–43.300 |
| D_zenos | warm | hierarchical | 50 | close_book | PASS | 10 | 30.673 | 21.942 | 32.614 | 21.729–32.961 |
| D_zenos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 33.308 | 32.044 | 33.351 | 29.923–33.373 |
| D_zenos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 33.610 | 33.572 | 46.548 | 33.559–47.079 |
| D_zenos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.778 | 20.873 | 44.642 | 19.525–45.865 |
| D_zenos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.316 | 23.172 | 34.409 | 21.584–43.888 |
| D_zenos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 33.320 | 22.531 | 33.945 | 21.897–39.053 |
| D_zenos | warm | hierarchical | 50 | open_book | PASS | 10 | 61.834 | 56.068 | 67.226 | 55.265–69.933 |
| D_zenos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 55.797 | 39.622 | 63.224 | 37.501–64.638 |
| D_zenos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 33.335 | 33.199 | 38.346 | 32.424–39.143 |
| D_zenos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 33.064 | 19.770 | 33.104 | 18.542–33.202 |
| E_project_title | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 6.678 | 6.468 | 6.962 | 6.416–7.033 |
| E_project_title | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.927 | 10.635 | 12.789 | 10.312–13.005 |
| E_project_title | warm | flat | 2000 | change_sort_mode | PASS | 10 | 58.507 | 53.506 | 67.169 | 52.589–67.650 |
| E_project_title | warm | flat | 2000 | close_book | PASS | 10 | 40.391 | 39.800 | 42.467 | 39.778–42.614 |
| E_project_title | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.655 | 16.641 | 16.675 | 16.638–16.735 |
| E_project_title | warm | flat | 2000 | home_to_library | PASS | 10 | 34.421 | 33.269 | 40.265 | 32.259–40.856 |
| E_project_title | warm | flat | 2000 | library_cached_paging | PASS | 30 | 16.087 | 16.040 | 16.151 | 15.971–16.654 |
| E_project_title | warm | flat | 2000 | library_first_render | PASS | 10 | 34.306 | 32.572 | 41.316 | 32.536–42.447 |
| E_project_title | warm | flat | 2000 | library_folder_back | PASS | 10 | 65.129 | 59.033 | 67.661 | 58.446–69.862 |
| E_project_title | warm | flat | 2000 | library_folder_enter | PASS | 10 | 4.351 | 3.462 | 14.842 | 3.301–16.187 |
| E_project_title | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.102 | 16.068 | 16.150 | 16.028–16.680 |
| E_project_title | warm | flat | 2000 | open_book | PASS | 10 | 43.069 | 40.258 | 44.511 | 40.130–44.541 |
| E_project_title | warm | flat | 2000 | open_book_minimal | PASS | 10 | 43.683 | 40.332 | 44.615 | 38.755–45.021 |
| E_project_title | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.665 | 16.645 | 16.677 | 16.639–16.712 |
| E_project_title | warm | flat | 2000 | repeated_nav | PASS | 2 | 166.701 | 166.699 | 166.702 | 166.699–166.702 |
| E_project_title | warm | flat | 50 | change_sort_mode | PASS | 10 | 16.134 | 16.110 | 16.244 | 16.070–16.816 |
| E_project_title | warm | flat | 50 | close_book | PASS | 10 | 14.550 | 14.087 | 15.381 | 13.193–16.437 |
| E_project_title | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.656 | 16.599 | 16.667 | 16.575–16.669 |
| E_project_title | warm | flat | 50 | home_to_library | PASS | 10 | 16.130 | 16.087 | 16.162 | 16.068–16.198 |
| E_project_title | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.081 | 16.040 | 16.109 | 16.018–16.646 |
| E_project_title | warm | flat | 50 | library_first_render | PASS | 10 | 16.157 | 16.069 | 16.246 | 15.919–16.340 |
| E_project_title | warm | flat | 50 | library_folder_back | PASS | 10 | 16.664 | 16.643 | 17.008 | 16.618–19.769 |
| E_project_title | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.620 | 15.670 | 16.659 | 15.446–16.663 |
| E_project_title | warm | flat | 50 | library_sequential_paging | PASS | 3 | 16.212 | 16.082 | 16.488 | 16.050–16.557 |
| E_project_title | warm | flat | 50 | open_book | PASS | 10 | 34.429 | 33.254 | 35.066 | 31.042–35.782 |
| E_project_title | warm | flat | 50 | open_book_minimal | PASS | 10 | 34.418 | 32.348 | 36.763 | 29.415–36.794 |
| E_project_title | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.657 | 16.630 | 16.673 | 16.614–16.675 |
| E_project_title | warm | flat | 50 | repeated_nav | PASS | 2 | 166.722 | 166.704 | 166.740 | 166.700–166.745 |
| E_project_title | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.046 | 16.026 | 16.077 | 16.020–16.087 |
| E_project_title | warm | hierarchical | 2000 | close_book | PASS | 10 | 17.693 | 17.240 | 18.757 | 16.652–18.769 |
| E_project_title | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.660 | 16.648 | 16.675 | 16.647–16.682 |
| E_project_title | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.059 | 16.020 | 16.092 | 16.007–16.095 |
| E_project_title | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.035 | 16.002 | 16.071 | 15.962–16.094 |
| E_project_title | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.665 | 16.635 | 16.675 | 16.632–16.681 |
| E_project_title | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.675 | 16.662 | 16.702 | 16.650–16.707 |
| E_project_title | warm | hierarchical | 2000 | open_book | PASS | 10 | 32.127 | 30.890 | 34.045 | 30.706–34.430 |
| E_project_title | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 31.559 | 30.819 | 32.994 | 30.236–34.125 |
| E_project_title | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.652 | 16.643 | 16.693 | 16.621–16.699 |
| E_project_title | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 15.988 | 15.955 | 16.007 | 15.933–16.012 |
| E_project_title | warm | hierarchical | 50 | close_book | PASS | 10 | 12.287 | 11.364 | 14.478 | 11.157–15.113 |
| E_project_title | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.660 | 16.645 | 16.668 | 16.633–16.672 |
| E_project_title | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.051 | 16.030 | 16.074 | 16.003–16.074 |
| E_project_title | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.038 | 16.017 | 16.070 | 15.969–16.081 |
| E_project_title | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.665 | 16.647 | 16.676 | 16.605–16.680 |
| E_project_title | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.651 | 16.638 | 16.666 | 16.630–16.679 |
| E_project_title | warm | hierarchical | 50 | open_book | PASS | 10 | 36.709 | 35.514 | 37.676 | 35.488–38.334 |
| E_project_title | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 36.486 | 34.615 | 38.518 | 32.236–40.497 |
| E_project_title | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.651 | 16.637 | 16.669 | 16.617–16.709 |
| F_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 20.876 | 19.944 | 24.536 | 19.711–25.451 |
| F_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.778 | 32.770 | 32.792 | 32.768–32.795 |
| F_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 86.627 | 76.792 | 126.657 | 73.900–137.236 |
| F_vos | warm | flat | 2000 | close_book | PASS | 10 | 75.101 | 72.969 | 85.936 | 72.638–87.425 |
| F_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.661 | 16.642 | 16.673 | 16.632–16.685 |
| F_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 50.522 | 49.334 | 88.205 | 48.800–95.094 |
| F_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 20.129 | 13.762 | 45.383 | 11.189–51.717 |
| F_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 49.490 | 46.577 | 72.935 | 45.211–78.457 |
| F_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 84.200 | 81.620 | 97.235 | 80.199–99.733 |
| F_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 15.748 | 3.514 | 32.126 | 2.923–32.133 |
| F_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 21.357 | 16.604 | 45.556 | 11.488–52.296 |
| F_vos | warm | flat | 2000 | open_book | PASS | 10 | 47.672 | 44.295 | 55.689 | 41.711–57.340 |
| F_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 45.873 | 43.130 | 51.660 | 40.929–53.392 |
| F_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.651 | 13.870 | 16.683 | 7.484–16.698 |
| F_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 263.947 | 254.136 | 273.759 | 251.683–276.212 |
| F_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 27.000 | 23.887 | 49.520 | 22.103–49.972 |
| F_vos | warm | flat | 50 | close_book | PASS | 10 | 34.678 | 31.407 | 39.035 | 27.949–44.622 |
| F_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.663 | 16.640 | 16.674 | 16.639–16.731 |
| F_vos | warm | flat | 50 | home_to_library | PASS | 10 | 31.948 | 27.581 | 43.138 | 27.190–43.637 |
| F_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.181 | 12.621 | 33.181 | 11.211–64.075 |
| F_vos | warm | flat | 50 | library_first_render | PASS | 10 | 39.909 | 31.837 | 63.841 | 30.169–72.351 |
| F_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 33.356 | 28.057 | 37.747 | 27.521–39.447 |
| F_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 12.919 | 9.909 | 26.081 | 9.543–26.323 |
| F_vos | warm | flat | 50 | library_sequential_paging | PASS | 4 | 99.036 | 67.621 | 151.321 | 61.217–166.669 |
| F_vos | warm | flat | 50 | open_book | PASS | 10 | 37.461 | 29.870 | 41.444 | 27.809–41.668 |
| F_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 48.209 | 40.142 | 52.876 | 37.842–53.958 |
| F_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.671 | 8.642 | 16.694 | 6.996–16.721 |
| F_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 174.401 | 173.925 | 174.876 | 173.806–174.995 |
| F_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.119 | 8.520 | 62.975 | 5.798–182.804 |
| F_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 32.731 | 30.088 | 41.562 | 29.709–42.490 |
| F_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.666 | 16.640 | 16.797 | 16.629–16.821 |
| F_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.629 | 32.571 | 32.702 | 32.365–32.823 |
| F_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.669 | 32.622 | 32.732 | 32.612–32.791 |
| F_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 33.010 | 21.648 | 35.040 | 19.357–37.907 |
| F_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.248 | 15.390 | 19.011 | 5.621–28.210 |
| F_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 50.447 | 42.227 | 51.601 | 41.923–52.310 |
| F_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 41.299 | 35.834 | 58.102 | 31.277–106.078 |
| F_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.672 | 16.651 | 17.650 | 16.637–26.331 |
| F_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.049 | 10.705 | 104.349 | 8.568–149.204 |
| F_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 22.045 | 21.069 | 27.671 | 20.738–28.058 |
| F_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.652 | 16.640 | 16.679 | 16.629–16.693 |
| F_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.665 | 32.642 | 32.675 | 32.583–32.697 |
| F_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.654 | 32.611 | 32.680 | 32.605–32.707 |
| F_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.312 | 31.255 | 33.355 | 26.435–33.379 |
| F_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 17.241 | 15.807 | 18.833 | 8.551–24.221 |
| F_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 44.878 | 40.421 | 45.742 | 27.743–46.086 |
| F_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 42.182 | 36.533 | 46.262 | 30.889–49.132 |
| F_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.648 | 9.677 | 16.659 | 9.007–16.662 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.699 | 7.293 | 7.918 | 7.191–7.973 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 27.503 | 22.041 | 27.572 | 20.676–27.589 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 131.935 | 131.124 | 133.666 | 106.140–240.412 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.034 | 15.840 | 16.785 | 7.009–102.446 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 13.319 | 5.885 | 109.165 | 5.796–129.942 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 132.658 | 131.773 | 161.819 | 123.712–241.914 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.144 | 15.957 | 16.314 | 9.472–111.286 |
| G_simpleui_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 85.468 | 70.035 | 92.582 | 69.832–104.651 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 221.994 | 91.074 | 249.751 | 89.297–250.573 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 33.114 | 32.535 | 33.205 | 28.888–33.309 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.654 | 15.836 | 35.183 | 9.216–201.373 |
| G_simpleui_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.644 | 12.636 | 31.036 | 12.284–31.114 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 14.022 | 10.918 | 36.093 | 10.485–38.511 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 75.359 | 56.370 | 82.392 | 55.616–86.753 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 90.821 | 72.115 | 94.038 | 68.967–96.653 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.392 | 8.960 | 31.660 | 8.630–33.744 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.148 | 9.201 | 37.342 | 8.305–47.395 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 142.921 | 103.232 | 158.532 | 85.376–173.525 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 89.321 | 72.131 | 103.291 | 62.966–122.254 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.821 | 16.748 | 17.246 | 16.689–20.361 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.690 | 16.616 | 53.537 | 16.588–347.231 |
| G_simpleui_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 703.235 | 639.100 | 767.369 | 623.066–783.403 |
| G_simpleui_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.664 | 14.180 | 16.677 | 5.625–16.682 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.606 | 131.302 | 138.845 | 113.135–184.835 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.138 | 15.935 | 16.366 | 9.500–60.392 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 14.714 | 11.789 | 54.295 | 11.711–60.835 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 132.851 | 130.623 | 149.096 | 128.977–149.231 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 13.948 | 11.518 | 18.671 | 10.902–22.015 |
| G_simpleui_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 28.466 | 22.175 | 42.287 | 18.324–48.001 |
| G_simpleui_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 55.020 | 43.676 | 133.391 | 37.677–148.610 |
| G_simpleui_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 33.181 | 33.134 | 33.243 | 33.107–33.285 |
| G_simpleui_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.668 | 15.683 | 24.047 | 7.125–90.316 |
| G_simpleui_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.666 | 14.286 | 29.245 | 13.959–29.398 |
| G_simpleui_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.145 | 9.576 | 32.811 | 8.547–33.305 |
| G_simpleui_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 41.989 | 32.528 | 49.739 | 30.624–50.625 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 16.474 | 15.393 | 27.689 | 15.229–27.943 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 14.018 | 9.897 | 28.769 | 9.719–33.130 |
| G_simpleui_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 16.149 | 10.215 | 23.469 | 9.754–28.319 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 99.663 | 61.527 | 113.680 | 60.947–113.927 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 46.934 | 40.443 | 76.627 | 38.460–91.094 |
| G_simpleui_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.752 | 16.361 | 16.818 | 13.677–16.856 |
| G_simpleui_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 17.549 | 16.666 | 88.957 | 16.656–101.392 |
| G_simpleui_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 383.409 | 367.186 | 399.632 | 363.130–403.688 |
| G_simpleui_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.649 | 15.591 | 16.688 | 6.274–16.725 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.087 | 13.324 | 52.270 | 12.678–60.809 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 40.000 | 25.146 | 41.520 | 24.250–43.629 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 43.296 | 41.903 | 51.044 | 40.962–108.160 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 32.965 | 32.423 | 33.215 | 32.272–33.228 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.656 | 15.726 | 26.536 | 7.600–115.322 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.657 | 14.550 | 28.883 | 14.394–28.943 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.783 | 22.189 | 43.205 | 20.634–45.155 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 22.313 | 21.359 | 34.645 | 21.349–34.649 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 13.927 | 11.214 | 23.897 | 6.450–23.926 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 82.016 | 56.419 | 107.631 | 55.934–117.897 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 40.870 | 37.936 | 47.215 | 36.031–49.338 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.975 | 16.777 | 18.239 | 16.685–18.530 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.637 | 11.072 | 24.460 | 10.546–92.937 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.677 | 15.668 | 16.717 | 7.180–16.728 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 14.005 | 13.084 | 50.504 | 12.757–59.639 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.160 | 9.861 | 25.575 | 9.592–25.685 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 34.831 | 33.326 | 44.368 | 31.218–83.156 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 33.084 | 30.029 | 33.549 | 20.241–36.658 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.631 | 13.844 | 17.110 | 6.568–21.071 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.655 | 14.173 | 28.845 | 14.127–28.945 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.767 | 31.603 | 33.968 | 23.583–42.023 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.675 | 10.040 | 26.020 | 9.316–26.670 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.052 | 7.799 | 21.756 | 6.535–22.341 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 62.980 | 51.354 | 78.325 | 50.669–84.022 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 48.314 | 37.107 | 57.323 | 33.721–61.743 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 17.104 | 16.841 | 33.596 | 16.789–33.612 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.662 | 11.488 | 24.034 | 10.550–90.261 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.655 | 15.638 | 16.674 | 6.646–16.680 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 29.116 | 26.442 | 35.475 | 25.773–37.065 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.032 | 31.850 | 32.075 | 31.805–32.086 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 133.925 | 131.099 | 144.094 | 116.232–161.596 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.129 | 15.554 | 17.182 | 8.833–45.475 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 15.387 | 9.165 | 57.437 | 7.480–64.777 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 133.036 | 131.108 | 141.237 | 118.610–179.801 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.165 | 12.704 | 21.225 | 7.520–27.097 |
| H_zenos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 80.376 | 64.116 | 85.015 | 63.766–85.199 |
| H_zenos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 29.426 | 24.598 | 32.811 | 24.206–33.801 |
| H_zenos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 16.251 | 14.813 | 16.367 | 8.648–16.437 |
| H_zenos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 33.303 | 32.158 | 33.336 | 31.544–33.340 |
| H_zenos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 37.590 | 36.946 | 49.081 | 35.691–54.966 |
| H_zenos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.831 | 7.752 | 30.500 | 6.313–33.175 |
| H_zenos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 48.222 | 32.286 | 53.015 | 30.785–69.848 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 51.778 | 50.007 | 63.392 | 49.981–64.124 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 33.478 | 19.794 | 48.289 | 19.178–49.454 |
| H_zenos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.095 | 6.925 | 31.043 | 6.340–32.601 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 56.696 | 52.006 | 57.751 | 48.276–65.459 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 48.447 | 45.375 | 78.651 | 44.420–80.485 |
| H_zenos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.883 | 16.155 | 17.181 | 11.416–18.845 |
| H_zenos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 33.275 | 33.071 | 75.739 | 33.065–88.213 |
| H_zenos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 175.014 | 168.340 | 181.688 | 166.671–183.357 |
| H_zenos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 28.858 | 26.270 | 29.500 | 20.947–32.108 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 133.009 | 125.131 | 144.368 | 122.354–179.163 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.032 | 13.318 | 18.970 | 6.464–27.324 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 11.989 | 5.979 | 43.510 | 5.893–50.567 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 133.682 | 132.504 | 139.865 | 132.202–140.372 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 19.682 | 12.491 | 24.506 | 8.369–25.235 |
| H_zenos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 32.862 | 19.725 | 44.851 | 19.329–46.167 |
| H_zenos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 30.424 | 27.626 | 66.564 | 25.602–67.796 |
| H_zenos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 16.399 | 15.972 | 16.469 | 13.671–16.481 |
| H_zenos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 33.314 | 27.871 | 33.325 | 27.598–33.336 |
| H_zenos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 33.611 | 32.147 | 48.717 | 19.525–50.180 |
| H_zenos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.103 | 9.609 | 27.046 | 7.454–29.023 |
| H_zenos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 33.587 | 28.613 | 45.780 | 20.064–48.107 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 33.381 | 22.237 | 34.780 | 21.608–44.684 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 33.309 | 22.719 | 34.507 | 21.043–44.915 |
| H_zenos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 9 | 15.907 | 7.442 | 19.115 | 5.371–30.077 |
| H_zenos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 69.041 | 42.291 | 83.531 | 39.212–90.484 |
| H_zenos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 60.644 | 51.195 | 65.804 | 33.296–72.604 |
| H_zenos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.918 | 16.304 | 19.417 | 11.609–20.622 |
| H_zenos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 33.338 | 33.157 | 41.004 | 32.888–44.228 |
| H_zenos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 169.870 | 167.324 | 172.416 | 166.687–173.052 |
| H_zenos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 33.056 | 25.070 | 33.132 | 22.620–33.140 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 13.995 | 9.425 | 48.362 | 8.656–61.686 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 32.748 | 19.636 | 45.711 | 19.408–45.862 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 66.671 | 64.126 | 74.160 | 58.877–76.106 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 16.276 | 16.110 | 16.409 | 16.067–16.442 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 33.308 | 25.129 | 33.348 | 24.849–33.379 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 33.608 | 33.557 | 48.259 | 33.553–48.324 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.782 | 19.139 | 46.333 | 17.239–48.122 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 33.329 | 19.919 | 34.637 | 19.581–46.201 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 33.316 | 31.949 | 45.348 | 19.950–46.343 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 68.487 | 46.654 | 80.390 | 43.990–91.525 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 63.171 | 38.799 | 69.065 | 35.469–69.637 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.946 | 15.845 | 18.224 | 13.951–18.645 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 33.330 | 33.302 | 75.544 | 33.243–82.003 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 33.007 | 16.522 | 33.104 | 15.152–33.139 |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 12.582 | 7.604 | 41.210 | 7.285–48.254 |
| H_zenos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 32.785 | 21.303 | 44.092 | 19.985–44.475 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 62.962 | 26.528 | 73.912 | 23.083–92.970 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 16.367 | 16.235 | 16.641 | 16.229–18.454 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 33.292 | 29.379 | 33.329 | 26.181–33.333 |
| H_zenos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 33.653 | 33.578 | 50.289 | 33.545–50.495 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.758 | 29.021 | 47.787 | 18.293–51.811 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.293 | 20.431 | 33.334 | 19.110–33.339 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 33.437 | 32.240 | 49.425 | 22.558–51.513 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 61.501 | 43.134 | 82.801 | 40.630–102.337 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 58.556 | 39.302 | 66.419 | 35.857–67.242 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.955 | 16.560 | 24.915 | 13.904–94.559 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 33.318 | 33.115 | 67.347 | 33.001–73.646 |
| H_zenos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 33.052 | 15.177 | 33.137 | 10.288–33.246 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 13.174 | 13.059 | 22.401 | 13.030–24.708 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.799 | 32.781 | 32.811 | 32.776–32.814 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.436 | 131.012 | 153.509 | 122.404–181.045 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.133 | 12.867 | 16.883 | 9.969–29.570 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 25.582 | 23.490 | 116.480 | 22.710–136.175 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 133.587 | 132.179 | 158.064 | 126.270–242.956 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 41.260 | 31.785 | 56.574 | 11.949–75.291 |
| I_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 90.057 | 74.922 | 123.319 | 73.126–133.155 |
| I_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 60.472 | 57.496 | 200.265 | 54.712–231.460 |
| I_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 16.288 | 15.422 | 16.316 | 8.214–16.321 |
| I_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.674 | 16.643 | 16.700 | 16.642–16.704 |
| I_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 53.332 | 48.510 | 93.205 | 47.245–102.062 |
| I_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 21.423 | 12.336 | 39.952 | 10.340–49.573 |
| I_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 49.524 | 47.840 | 70.440 | 46.982–76.327 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 92.647 | 83.350 | 103.273 | 83.328–103.809 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 13.346 | 4.133 | 16.499 | 3.729–16.700 |
| I_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 19.729 | 15.929 | 43.902 | 12.300–47.156 |
| I_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 139.463 | 102.703 | 190.478 | 90.702–209.360 |
| I_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 94.724 | 54.126 | 114.707 | 53.549–118.437 |
| I_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 22.996 | 22.218 | 23.637 | 20.972–25.425 |
| I_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.668 | 16.592 | 16.679 | 16.569–16.685 |
| I_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 317.059 | 312.357 | 321.761 | 311.182–322.936 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 133.355 | 130.714 | 151.411 | 125.000–208.191 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 23.485 | 20.665 | 35.030 | 18.260–51.634 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 19.623 | 18.944 | 55.387 | 17.580–59.409 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 147.564 | 132.882 | 153.243 | 132.688–157.182 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 35.242 | 23.639 | 40.082 | 17.961–40.749 |
| I_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 29.198 | 22.341 | 47.559 | 21.373–50.946 |
| I_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 32.961 | 27.050 | 38.039 | 26.184–42.112 |
| I_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 16.326 | 9.741 | 16.367 | 7.677–16.381 |
| I_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.663 | 16.629 | 16.699 | 16.623–16.702 |
| I_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 32.709 | 28.207 | 45.020 | 27.166–45.963 |
| I_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.119 | 11.110 | 35.027 | 9.421–51.119 |
| I_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 38.323 | 32.745 | 63.941 | 32.483–71.478 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 36.231 | 32.715 | 40.411 | 27.506–41.090 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.637 | 6.332 | 28.878 | 5.986–29.363 |
| I_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 4 | 111.184 | 87.387 | 141.989 | 82.405–149.975 |
| I_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 70.729 | 51.047 | 86.865 | 47.689–93.827 |
| I_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 60.181 | 38.880 | 69.478 | 30.981–75.199 |
| I_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 18.727 | 17.604 | 20.123 | 17.430–20.799 |
| I_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.663 | 16.646 | 16.677 | 16.640–16.690 |
| I_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 238.436 | 205.746 | 271.126 | 197.573–279.299 |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 14.272 | 11.528 | 53.330 | 11.056–57.842 |
| I_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 18.473 | 15.251 | 136.180 | 11.430–182.751 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 32.773 | 30.307 | 36.138 | 30.216–37.028 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 16.425 | 16.283 | 16.569 | 16.256–16.780 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.663 | 16.592 | 16.700 | 16.215–16.707 |
| I_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.664 | 32.634 | 32.714 | 32.614–32.715 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.678 | 32.646 | 32.724 | 32.589–32.729 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 31.637 | 21.398 | 35.579 | 19.661–38.539 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.838 | 16.486 | 20.050 | 14.849–28.351 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 64.760 | 49.667 | 86.231 | 46.632–88.878 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 66.788 | 57.883 | 70.764 | 42.205–74.033 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.803 | 16.207 | 16.905 | 12.979–16.910 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.651 | 16.585 | 16.693 | 16.422–16.859 |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 14.291 | 11.157 | 41.504 | 10.823–45.146 |
| I_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.044 | 10.641 | 104.398 | 8.544–149.122 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 33.749 | 25.591 | 57.302 | 18.457–59.499 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 16.442 | 16.247 | 16.563 | 16.176–16.567 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.651 | 16.640 | 16.679 | 16.632–16.705 |
| I_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.635 | 32.611 | 32.701 | 32.579–32.778 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.659 | 32.610 | 32.702 | 32.593–32.706 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.314 | 31.435 | 33.346 | 26.024–33.381 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 17.223 | 15.780 | 18.593 | 8.400–24.711 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 70.048 | 64.480 | 77.429 | 63.525–79.304 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 44.992 | 35.186 | 62.611 | 29.696–63.486 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.831 | 16.524 | 21.703 | 14.733–64.251 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.648 | 16.588 | 16.676 | 16.564–16.680 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 10.138 | 9.742 | 10.151 | 9.643–10.154 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 20.813 | 18.859 | 28.069 | 18.371–29.883 |
| J_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 98.945 | 78.092 | 105.904 | 71.994–105.935 |
| J_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 250.871 | 113.197 | 272.986 | 100.780–284.051 |
| J_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.673 | 16.629 | 16.707 | 16.625–16.710 |
| J_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 16.651 | 12.137 | 31.211 | 11.892–31.850 |
| J_simpleui_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.886 | 10.199 | 30.821 | 9.653–33.749 |
| J_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 60.535 | 53.220 | 80.628 | 51.953–82.827 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 115.872 | 87.563 | 124.125 | 85.618–126.885 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.734 | 9.223 | 12.427 | 9.106–12.992 |
| J_simpleui_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.098 | 8.536 | 30.645 | 8.345–38.088 |
| J_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 130.691 | 121.503 | 156.397 | 119.002–157.382 |
| J_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 105.005 | 79.118 | 111.799 | 69.958–122.134 |
| J_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 17.649 | 17.020 | 59.605 | 16.768–407.778 |
| J_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 768.356 | 739.706 | 797.006 | 732.543–804.169 |
| J_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 16.663 | 15.088 | 16.684 | 5.739–16.712 |
| J_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 20.386 | 14.835 | 26.492 | 14.021–27.840 |
| J_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 37.745 | 33.898 | 47.890 | 33.152–99.978 |
| J_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.657 | 16.645 | 16.678 | 16.644–16.714 |
| J_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 16.660 | 13.001 | 29.893 | 12.770–30.236 |
| J_simpleui_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.130 | 7.870 | 27.397 | 6.793–28.445 |
| J_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 32.790 | 29.144 | 36.470 | 27.623–38.050 |
| J_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 23.531 | 13.655 | 30.597 | 11.810–30.657 |
| J_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.194 | 6.426 | 19.930 | 5.793–23.820 |
| J_simpleui_vos | warm | flat | 50 | library_sequential_paging | PASS | 5 | 16.137 | 14.891 | 33.410 | 14.463–34.848 |
| J_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 82.359 | 46.093 | 113.187 | 45.996–118.961 |
| J_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 47.660 | 41.322 | 60.367 | 31.882–67.613 |
| J_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 17.905 | 16.728 | 27.855 | 16.652–87.458 |
| J_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 341.739 | 335.144 | 348.334 | 333.495–349.983 |
| J_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 16.661 | 15.535 | 16.673 | 5.745–16.673 |
| J_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 27.761 | 16.669 | 32.825 | 16.087–40.014 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 44.075 | 37.671 | 67.051 | 37.576–131.552 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.661 | 16.626 | 16.681 | 16.619–16.694 |
| J_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.646 | 14.012 | 28.584 | 13.236–28.877 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.759 | 32.613 | 32.806 | 31.753–32.819 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 19.800 | 9.231 | 27.106 | 8.788–28.132 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 14.663 | 7.687 | 25.175 | 6.508–26.213 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 122.102 | 64.003 | 141.320 | 61.782–145.852 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 39.773 | 37.684 | 64.375 | 34.709–85.415 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.651 | 16.223 | 26.240 | 14.035–111.066 |
| J_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.665 | 15.714 | 16.701 | 7.377–16.857 |
| J_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 12.581 | 9.638 | 26.607 | 9.502–28.664 |
| J_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 37.238 | 33.742 | 40.726 | 32.075–44.870 |
| J_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.654 | 16.642 | 16.671 | 16.624–16.696 |
| J_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.666 | 14.237 | 28.708 | 13.285–28.981 |
| J_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.769 | 32.482 | 32.820 | 32.382–32.872 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 15.647 | 8.693 | 25.959 | 8.308–28.161 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.262 | 6.799 | 26.894 | 6.570–27.203 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 122.074 | 102.669 | 132.212 | 79.304–135.345 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 48.618 | 40.866 | 65.322 | 34.892–75.494 |
| J_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.627 | 15.948 | 22.999 | 15.406–79.343 |
| J_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.653 | 15.699 | 16.689 | 7.360–16.691 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.967 | 7.586 | 8.676 | 7.491–8.853 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 23.679 | 20.650 | 25.070 | 19.893–25.418 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.096 | 130.110 | 134.221 | 114.974–239.417 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.117 | 15.070 | 17.060 | 5.057–124.942 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 16.032 | 6.945 | 117.260 | 6.521–138.396 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 132.351 | 131.525 | 163.108 | 119.955–244.388 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.159 | 12.701 | 17.301 | 4.773–124.777 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 102.383 | 76.391 | 109.788 | 72.266–110.702 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 252.612 | 99.925 | 282.630 | 89.635–294.941 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 33.114 | 33.050 | 33.167 | 33.031–33.171 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.675 | 16.605 | 16.790 | 16.580–16.816 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.636 | 12.437 | 32.692 | 10.826–33.542 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.165 | 10.575 | 31.567 | 9.671–47.792 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 67.058 | 60.192 | 85.117 | 59.989–89.060 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 106.650 | 80.243 | 116.339 | 79.667–144.239 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.985 | 10.041 | 16.206 | 9.751–34.242 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.044 | 8.429 | 31.406 | 7.300–37.045 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 141.928 | 130.340 | 157.810 | 128.337–172.785 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 108.559 | 85.842 | 123.938 | 70.290–135.049 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.852 | 16.825 | 16.962 | 16.809–16.996 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.658 | 16.581 | 62.932 | 16.563–400.303 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 800.014 | 759.981 | 840.047 | 749.973–850.055 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.651 | 7.021 | 16.694 | 6.802–16.724 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.258 | 130.650 | 138.379 | 111.560–202.624 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.127 | 13.992 | 16.388 | 9.465–65.849 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 14.119 | 13.147 | 65.314 | 12.797–74.202 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 140.821 | 130.899 | 149.349 | 129.239–149.466 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 15.034 | 11.982 | 20.072 | 10.298–23.257 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 35.478 | 22.644 | 37.122 | 22.213–37.427 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 42.990 | 37.097 | 110.552 | 36.296–115.424 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 33.137 | 31.774 | 33.178 | 27.359–33.264 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.656 | 16.638 | 16.668 | 16.636–16.675 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.657 | 13.021 | 30.536 | 12.759–35.612 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.431 | 11.803 | 28.995 | 11.308–32.995 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 34.364 | 32.425 | 42.746 | 29.184–45.276 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 20.530 | 18.818 | 35.492 | 17.840–37.072 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.973 | 9.802 | 29.490 | 9.431–32.360 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 12.768 | 9.350 | 28.020 | 7.516–34.138 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 133.466 | 102.351 | 141.922 | 91.197–152.561 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 52.945 | 45.225 | 92.357 | 44.236–92.643 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.752 | 16.710 | 16.816 | 16.641–16.827 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 21.184 | 17.724 | 112.905 | 17.476–123.861 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 317.947 | 230.060 | 405.832 | 208.089–427.804 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.646 | 10.202 | 16.691 | 7.854–16.714 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 13.643 | 13.043 | 56.707 | 12.462–66.366 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 21.216 | 14.852 | 32.399 | 14.820–38.104 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 47.596 | 45.316 | 53.659 | 45.062–98.501 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 32.930 | 31.870 | 33.175 | 31.546–33.177 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.665 | 16.437 | 16.713 | 14.698–16.716 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.644 | 13.206 | 29.216 | 12.730–29.970 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.746 | 32.694 | 32.821 | 32.533–32.825 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 14.499 | 8.259 | 26.585 | 8.226–28.015 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 14.494 | 6.262 | 26.734 | 5.525–29.106 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 116.111 | 86.398 | 123.976 | 70.473–127.945 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 56.200 | 40.671 | 80.409 | 40.624–88.386 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 17.029 | 16.788 | 18.061 | 16.761–18.405 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 17.060 | 16.346 | 91.763 | 13.735–98.454 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.679 | 15.764 | 16.692 | 7.588–16.739 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 14.743 | 11.737 | 55.759 | 11.703–61.476 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 15.873 | 9.042 | 26.440 | 8.673–26.783 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 35.166 | 32.372 | 39.821 | 31.792–40.263 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 33.080 | 31.708 | 34.046 | 30.302–37.011 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.660 | 16.300 | 16.707 | 13.473–16.717 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.620 | 13.109 | 29.775 | 11.204–30.750 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.764 | 32.632 | 32.809 | 32.579–32.819 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 12.978 | 8.509 | 27.497 | 8.060–27.854 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.078 | 6.883 | 27.272 | 6.647–28.313 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 78.611 | 57.622 | 110.712 | 52.410–113.851 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 51.132 | 43.883 | 69.399 | 40.345–89.845 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.767 | 16.382 | 17.039 | 15.590–17.801 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.652 | 16.283 | 23.943 | 13.378–89.327 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.675 | 15.569 | 16.700 | 6.280–16.724 |
| K_vos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 20.387 | 19.772 | 20.805 | 19.618–20.910 |
| K_vos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.756 | 32.734 | 32.785 | 32.728–32.792 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 17.261 | 15.163 | 17.841 | 14.639–17.986 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.788 | 32.750 | 32.835 | 32.741–32.847 |
| L_project_title_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 66.510 | 59.068 | 73.843 | 58.753–74.003 |
| L_project_title_vos | warm | flat | 2000 | close_book | PASS | 10 | 49.123 | 48.268 | 49.918 | 48.089–50.502 |
| L_project_title_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.658 | 16.615 | 16.667 | 16.611–16.678 |
| L_project_title_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 49.469 | 49.252 | 50.016 | 48.996–50.142 |
| L_project_title_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 16.073 | 16.038 | 16.115 | 15.840–16.657 |
| L_project_title_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 49.511 | 48.475 | 50.411 | 48.373–50.597 |
| L_project_title_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 83.350 | 71.170 | 83.366 | 70.422–83.406 |
| L_project_title_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 16.631 | 12.279 | 16.675 | 12.234–16.698 |
| L_project_title_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.090 | 16.061 | 16.139 | 11.701–16.215 |
| L_project_title_vos | warm | flat | 2000 | open_book | PASS | 10 | 50.061 | 47.671 | 52.522 | 47.431–53.090 |
| L_project_title_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 50.028 | 48.552 | 51.450 | 48.261–51.945 |
| L_project_title_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.663 | 16.660 | 16.683 | 16.648–16.717 |
| L_project_title_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 166.697 | 166.697 | 166.698 | 166.697–166.698 |
| L_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 16.071 | 15.700 | 16.389 | 13.796–18.428 |
| L_project_title_vos | warm | flat | 50 | close_book | PASS | 10 | 26.320 | 23.418 | 35.714 | 22.540–36.285 |
| L_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.650 | 16.630 | 16.666 | 16.623–16.685 |
| L_project_title_vos | warm | flat | 50 | home_to_library | PASS | 10 | 32.714 | 32.681 | 32.770 | 32.675–32.809 |
| L_project_title_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.110 | 16.008 | 16.249 | 15.982–16.505 |
| L_project_title_vos | warm | flat | 50 | library_first_render | PASS | 10 | 32.744 | 32.715 | 32.767 | 32.630–32.781 |
| L_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 33.335 | 33.208 | 33.356 | 32.947–33.398 |
| L_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.636 | 16.617 | 16.657 | 16.594–16.685 |
| L_project_title_vos | warm | flat | 50 | library_sequential_paging | PASS | 3 | 16.023 | 11.953 | 16.073 | 10.936–16.085 |
| L_project_title_vos | warm | flat | 50 | open_book | PASS | 10 | 49.507 | 42.655 | 54.916 | 40.321–80.636 |
| L_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 41.195 | 40.741 | 42.990 | 37.776–45.194 |
| L_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.661 | 16.630 | 16.692 | 16.608–16.697 |
| L_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 166.694 | 166.679 | 166.708 | 166.676–166.711 |
| L_project_title_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 15.994 | 15.927 | 16.013 | 15.904–16.018 |
| L_project_title_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 23.888 | 23.285 | 34.393 | 22.968–36.349 |
| L_project_title_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.652 | 16.633 | 16.676 | 16.619–16.685 |
| L_project_title_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.615 | 32.570 | 32.663 | 32.566–32.663 |
| L_project_title_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.644 | 32.582 | 32.711 | 32.537–32.717 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 33.296 | 33.158 | 33.333 | 32.355–33.373 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.652 | 16.636 | 17.030 | 16.626–19.370 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 42.535 | 41.231 | 43.439 | 38.277–43.704 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 42.545 | 40.327 | 42.993 | 39.079–43.817 |
| L_project_title_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.663 | 16.629 | 16.681 | 16.614–16.683 |
| L_project_title_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 15.970 | 15.923 | 15.998 | 15.909–16.003 |
| L_project_title_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 27.011 | 25.430 | 28.252 | 20.450–28.413 |
| L_project_title_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.666 | 16.634 | 16.690 | 16.621–16.706 |
| L_project_title_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.609 | 32.578 | 32.648 | 32.564–32.648 |
| L_project_title_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.615 | 32.558 | 32.677 | 32.508–32.678 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.317 | 33.298 | 33.360 | 33.283–33.368 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.646 | 16.619 | 16.670 | 16.595–16.699 |
| L_project_title_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 40.561 | 39.551 | 41.231 | 39.080–41.345 |
| L_project_title_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 40.969 | 39.068 | 42.060 | 37.964–42.415 |
| L_project_title_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.647 | 16.611 | 16.672 | 16.485–16.673 |
| M_leanui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 10.789 | 9.874 | 11.813 | 9.645–12.069 |
| M_leanui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.160 | 15.911 | 16.162 | 15.849–16.162 |
| M_leanui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.347 | 7.757 | 9.713 | 7.609–10.055 |
| M_leanui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 15.130 | 14.004 | 15.958 | 13.723–16.165 |
| M_leanui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 79.031 | 69.271 | 82.017 | 68.505–90.424 |
| M_leanui | warm | flat | 2000 | close_book | PASS | 10 | 53.199 | 51.232 | 55.587 | 49.717–56.899 |
| M_leanui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.651 | 16.345 | 16.682 | 14.173–16.712 |
| M_leanui | warm | flat | 2000 | home_to_library | PASS | 10 | 38.255 | 35.422 | 43.127 | 34.902–43.872 |
| M_leanui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 16.091 | 16.033 | 16.150 | 15.938–16.633 |
| M_leanui | warm | flat | 2000 | library_first_render | PASS | 10 | 36.623 | 35.873 | 44.324 | 35.787–44.621 |
| M_leanui | warm | flat | 2000 | library_folder_back | PASS | 10 | 79.489 | 75.553 | 83.617 | 75.043–84.099 |
| M_leanui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 7.288 | 4.052 | 10.950 | 3.245–16.442 |
| M_leanui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.161 | 15.943 | 16.241 | 14.461–19.255 |
| M_leanui | warm | flat | 2000 | open_book | PASS | 10 | 55.735 | 47.420 | 60.230 | 46.792–60.414 |
| M_leanui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 56.464 | 51.747 | 59.931 | 50.656–65.174 |
| M_leanui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.663 | 16.646 | 16.898 | 16.645–18.701 |
| M_leanui | warm | flat | 2000 | repeated_nav | PASS | 2 | 166.702 | 166.674 | 166.729 | 166.667–166.736 |
| M_leanui | warm | flat | 50 | change_sort_mode | PASS | 10 | 22.034 | 20.884 | 24.930 | 20.499–29.845 |
| M_leanui | warm | flat | 50 | close_book | PASS | 10 | 25.973 | 22.314 | 28.313 | 20.465–29.175 |
| M_leanui | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.649 | 16.440 | 16.678 | 14.724–16.682 |
| M_leanui | warm | flat | 50 | home_to_library | PASS | 10 | 16.136 | 15.930 | 16.188 | 15.860–16.320 |
| M_leanui | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.111 | 16.014 | 16.178 | 15.766–16.523 |
| M_leanui | warm | flat | 50 | library_first_render | PASS | 10 | 16.083 | 14.237 | 16.847 | 13.040–20.667 |
| M_leanui | warm | flat | 50 | library_folder_back | PASS | 10 | 27.454 | 26.006 | 29.900 | 25.907–32.154 |
| M_leanui | warm | flat | 50 | library_folder_enter | PASS | 10 | 3.899 | 3.648 | 4.951 | 3.356–5.408 |
| M_leanui | warm | flat | 50 | library_sequential_paging | PASS | 3 | 15.871 | 15.600 | 15.982 | 15.532–16.010 |
| M_leanui | warm | flat | 50 | open_book | PASS | 10 | 40.656 | 38.432 | 42.864 | 37.730–42.950 |
| M_leanui | warm | flat | 50 | open_book_minimal | PASS | 10 | 40.817 | 39.822 | 43.264 | 38.772–47.746 |
| M_leanui | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.659 | 16.630 | 16.679 | 16.583–16.681 |
| M_leanui | warm | flat | 50 | repeated_nav | PASS | 2 | 166.707 | 166.701 | 166.713 | 166.700–166.714 |
| M_leanui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.016 | 15.951 | 16.089 | 15.945–16.123 |
| M_leanui | warm | hierarchical | 2000 | close_book | PASS | 10 | 26.927 | 25.205 | 28.029 | 24.102–29.481 |
| M_leanui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.651 | 16.441 | 16.668 | 14.804–16.669 |
| M_leanui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.087 | 16.045 | 16.125 | 16.026–16.131 |
| M_leanui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.081 | 16.038 | 16.090 | 16.001–16.097 |
| M_leanui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.605 | 15.432 | 16.666 | 15.189–16.666 |
| M_leanui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.886 | 16.602 | 20.754 | 16.120–23.948 |
| M_leanui | warm | hierarchical | 2000 | open_book | PASS | 10 | 40.656 | 38.074 | 41.438 | 37.700–41.462 |
| M_leanui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 39.447 | 38.408 | 40.691 | 38.001–40.701 |
| M_leanui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.671 | 16.622 | 16.681 | 16.612–16.687 |
| M_leanui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.047 | 15.956 | 16.121 | 15.940–16.140 |
| M_leanui | warm | hierarchical | 50 | close_book | PASS | 10 | 17.760 | 16.764 | 20.661 | 16.332–21.002 |
| M_leanui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.659 | 16.432 | 16.694 | 14.641–16.732 |
| M_leanui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.077 | 16.048 | 16.105 | 16.021–16.120 |
| M_leanui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.046 | 16.031 | 16.147 | 16.027–16.162 |
| M_leanui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.678 | 16.653 | 16.716 | 16.611–16.720 |
| M_leanui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.660 | 16.627 | 16.677 | 16.603–16.698 |
| M_leanui | warm | hierarchical | 50 | open_book | PASS | 10 | 36.991 | 35.655 | 43.397 | 35.208–45.639 |
| M_leanui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 36.411 | 35.254 | 40.884 | 35.132–40.986 |
| M_leanui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.661 | 16.642 | 16.697 | 16.622–16.702 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 10.903 | 9.127 | 11.851 | 8.683–12.088 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 7.663 | 7.401 | 14.409 | 7.335–16.095 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.710 | 7.223 | 11.855 | 6.851–12.641 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 7.040 | 6.716 | 14.334 | 6.635–16.158 |
| N_m1n1mal | warm | flat | 2000 | change_sort_mode | PASS | 10 | 89.990 | 83.783 | 141.796 | 83.246–142.062 |
| N_m1n1mal | warm | flat | 2000 | close_book | PASS | 10 | 69.947 | 68.150 | 73.664 | 67.309–74.405 |
| N_m1n1mal | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.668 | 16.637 | 16.694 | 16.623–16.695 |
| N_m1n1mal | warm | flat | 2000 | home_to_library | PASS | 10 | 99.636 | 51.007 | 196.173 | 48.808–216.694 |
| N_m1n1mal | warm | flat | 2000 | library_cached_paging | PASS | 30 | 21.684 | 13.671 | 63.366 | 11.651–70.661 |
| N_m1n1mal | warm | flat | 2000 | library_first_render | PASS | 10 | 37.957 | 36.720 | 70.213 | 36.262–85.570 |
| N_m1n1mal | warm | flat | 2000 | library_folder_back | PASS | 10 | 83.249 | 68.560 | 102.864 | 67.941–106.109 |
| N_m1n1mal | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.059 | 3.932 | 16.448 | 3.866–42.530 |
| N_m1n1mal | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 21.692 | 16.352 | 60.724 | 11.059–67.986 |
| N_m1n1mal | warm | flat | 2000 | open_book | PASS | 10 | 63.080 | 60.284 | 98.076 | 57.774–98.730 |
| N_m1n1mal | warm | flat | 2000 | open_book_minimal | PASS | 10 | 59.744 | 57.593 | 62.587 | 57.425–63.914 |
| N_m1n1mal | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.657 | 15.774 | 20.329 | 8.236–52.999 |
| N_m1n1mal | warm | flat | 2000 | repeated_nav | PASS | 2 | 308.690 | 288.218 | 329.161 | 283.100–334.279 |
| N_m1n1mal | warm | flat | 50 | change_sort_mode | PASS | 10 | 34.522 | 24.191 | 45.580 | 21.405–45.584 |
| N_m1n1mal | warm | flat | 50 | close_book | PASS | 10 | 20.726 | 19.839 | 23.537 | 19.006–28.239 |
| N_m1n1mal | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.660 | 16.645 | 16.679 | 16.640–16.696 |
| N_m1n1mal | warm | flat | 50 | home_to_library | PASS | 10 | 22.977 | 21.328 | 38.500 | 20.798–42.499 |
| N_m1n1mal | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.180 | 12.104 | 92.277 | 10.427–115.902 |
| N_m1n1mal | warm | flat | 50 | library_first_render | PASS | 10 | 23.428 | 21.578 | 43.018 | 20.097–46.389 |
| N_m1n1mal | warm | flat | 50 | library_folder_back | PASS | 10 | 24.636 | 19.861 | 30.137 | 19.456–30.213 |
| N_m1n1mal | warm | flat | 50 | library_folder_enter | PASS | 10 | 7.045 | 3.824 | 12.118 | 3.687–19.496 |
| N_m1n1mal | warm | flat | 50 | library_sequential_paging | PASS | 5 | 81.763 | 42.011 | 105.200 | 17.956–120.248 |
| N_m1n1mal | warm | flat | 50 | open_book | PASS | 10 | 39.344 | 29.219 | 48.535 | 27.610–49.750 |
| N_m1n1mal | warm | flat | 50 | open_book_minimal | PASS | 10 | 44.212 | 31.869 | 48.480 | 29.468–49.529 |
| N_m1n1mal | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.664 | 16.592 | 25.254 | 16.390–26.086 |
| N_m1n1mal | warm | flat | 50 | repeated_nav | PASS | 2 | 175.894 | 158.221 | 193.568 | 153.803–197.986 |
| N_m1n1mal | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 15.162 | 7.075 | 149.013 | 5.751–149.444 |
| N_m1n1mal | warm | hierarchical | 2000 | close_book | PASS | 10 | 34.968 | 20.109 | 40.890 | 20.032–43.655 |
| N_m1n1mal | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.660 | 16.644 | 16.702 | 16.629–16.807 |
| N_m1n1mal | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.073 | 10.141 | 22.247 | 8.877–23.410 |
| N_m1n1mal | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.114 | 9.896 | 23.182 | 9.163–23.537 |
| N_m1n1mal | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 26.844 | 15.025 | 34.622 | 12.985–37.706 |
| N_m1n1mal | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.433 | 4.211 | 24.649 | 3.724–26.840 |
| N_m1n1mal | warm | hierarchical | 2000 | open_book | PASS | 10 | 38.570 | 36.239 | 41.469 | 35.236–41.906 |
| N_m1n1mal | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 42.258 | 39.718 | 46.672 | 37.794–53.205 |
| N_m1n1mal | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.657 | 15.096 | 23.394 | 5.484–83.293 |
| N_m1n1mal | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.105 | 8.986 | 23.146 | 8.955–23.194 |
| N_m1n1mal | warm | hierarchical | 50 | close_book | PASS | 10 | 18.392 | 15.461 | 25.445 | 15.130–25.445 |
| N_m1n1mal | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.662 | 16.646 | 26.693 | 16.644–116.673 |
| N_m1n1mal | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.105 | 10.030 | 22.165 | 8.903–23.335 |
| N_m1n1mal | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.095 | 10.602 | 22.056 | 10.122–22.065 |
| N_m1n1mal | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.526 | 10.537 | 22.924 | 10.443–23.946 |
| N_m1n1mal | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.556 | 9.916 | 24.731 | 9.573–25.047 |
| N_m1n1mal | warm | hierarchical | 50 | open_book | PASS | 10 | 29.357 | 28.127 | 33.693 | 26.556–34.023 |
| N_m1n1mal | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 40.897 | 29.838 | 46.824 | 28.009–47.026 |
| N_m1n1mal | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.640 | 9.331 | 16.694 | 7.491–16.702 |
| A_stock | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.486 | 8.486 | 8.486 | 8.486–8.486 |
| A_stock | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 15.009 | 15.009 | 15.009 | 15.009–15.009 |
| B_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 9.126 | 9.126 | 9.126 | 9.126–9.126 |
| B_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.118 | 16.118 | 16.118 | 16.118–16.118 |
| C_simpleui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 7.271 | 7.271 | 7.271 | 7.271–7.271 |
| C_simpleui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 25.912 | 25.912 | 25.912 | 25.912–25.912 |
| D_zenos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 31.984 | 31.984 | 31.984 | 31.984–31.984 |
| D_zenos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 33.556 | 33.556 | 33.556 | 33.556–33.556 |
| E_project_title | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 6.552 | 6.552 | 6.552 | 6.552–6.552 |
| E_project_title | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 6.947 | 6.947 | 6.947 | 6.947–6.947 |
| F_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 22.910 | 22.910 | 22.910 | 22.910–22.910 |
| F_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.786 | 32.786 | 32.786 | 32.786–32.786 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 7.993 | 7.993 | 7.993 | 7.993–7.993 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 27.849 | 27.849 | 27.849 | 27.849–27.849 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 32.076 | 32.076 | 32.076 | 32.076–32.076 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 33.511 | 33.511 | 33.511 | 33.511–33.511 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 30.168 | 30.168 | 30.168 | 30.168–30.168 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.638 | 32.638 | 32.638 | 32.638–32.638 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.525 | 8.525 | 8.525 | 8.525–8.525 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.604 | 32.604 | 32.604 | 32.604–32.604 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.496 | 8.496 | 8.496 | 8.496–8.496 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.173 | 32.173 | 32.173 | 32.173–32.173 |
| L_project_title_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 27.784 | 27.784 | 27.784 | 27.784–27.784 |
| L_project_title_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.751 | 32.751 | 32.751 | 32.751–32.751 |
| M_leanui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.700 | 8.700 | 8.700 | 8.700–8.700 |
| M_leanui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 9.018 | 9.018 | 9.018 | 9.018–9.018 |
| N_m1n1mal | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 12.322 | 12.322 | 12.322 | 12.322–12.322 |
| N_m1n1mal | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.126 | 16.126 | 16.126 | 16.126–16.126 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 203.277 | 199.889 | 213.451 | 199.042–215.994 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 225.682 | 223.882 | 243.173 | 223.432–247.545 |
| A_stock | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 229.154 | 227.433 | 246.991 | 227.003–251.450 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 237.591 | 236.073 | 255.673 | 235.694–260.193 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 166.516 | 165.611 | 185.203 | 165.385–189.875 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 190.833 | 190.306 | 217.082 | 190.174–223.644 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 194.242 | 193.539 | 220.408 | 193.363–226.949 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 202.504 | 201.743 | 228.998 | 201.552–235.622 |
| A_stock | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 247.274 | 247.274 | 247.274 | 247.274–247.274 |
| A_stock | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3130.712 | 3130.712 | 3130.712 | 3130.712–3130.712 |
| A_stock | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 14947.295 | 14947.295 | 14947.295 | 14947.295–14947.295 |
| A_stock | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 14996.787 | 14996.787 | 14996.787 | 14996.787–14996.787 |
| A_stock | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 209.597 | 209.597 | 209.597 | 209.597–209.597 |
| A_stock | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1111.867 | 1111.867 | 1111.867 | 1111.867–1111.867 |
| A_stock | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 7763.706 | 7763.706 | 7763.706 | 7763.706–7763.706 |
| A_stock | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7776.677 | 7776.677 | 7776.677 | 7776.677–7776.677 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 206.117 | 206.117 | 206.117 | 206.117–206.117 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 800.918 | 800.918 | 800.918 | 800.918–800.918 |
| A_stock | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 5497.038 | 5497.038 | 5497.038 | 5497.038–5497.038 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 5512.786 | 5512.786 | 5512.786 | 5512.786–5512.786 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 207.241 | 207.241 | 207.241 | 207.241–207.241 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 813.331 | 813.331 | 813.331 | 813.331–813.331 |
| A_stock | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5044.022 | 5044.022 | 5044.022 | 5044.022–5044.022 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5059.052 | 5059.052 | 5059.052 | 5059.052–5059.052 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 212.366 | 211.468 | 212.766 | 211.243–212.866 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 240.364 | 239.062 | 242.939 | 238.736–243.583 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 244.513 | 243.195 | 246.642 | 242.866–247.174 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 253.266 | 251.565 | 255.280 | 251.140–255.784 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 172.983 | 171.963 | 192.856 | 171.708–197.825 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 206.594 | 193.848 | 219.090 | 190.661–222.213 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 210.421 | 197.276 | 222.714 | 193.990–225.787 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 218.728 | 205.477 | 230.950 | 202.164–234.006 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 378.842 | 378.842 | 378.842 | 378.842–378.842 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3254.984 | 3254.984 | 3254.984 | 3254.984–3254.984 |
| B_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 31377.791 | 31377.791 | 31377.791 | 31377.791–31377.791 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 31477.090 | 31477.090 | 31477.090 | 31477.090–31477.090 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 218.556 | 218.556 | 218.556 | 218.556–218.556 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1126.580 | 1126.580 | 1126.580 | 1126.580–1126.580 |
| B_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 16861.486 | 16861.486 | 16861.486 | 16861.486–16861.486 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 16881.069 | 16881.069 | 16881.069 | 16881.069–16881.069 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 208.777 | 208.777 | 208.777 | 208.777–208.777 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 813.276 | 813.276 | 813.276 | 813.276–813.276 |
| B_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 8312.082 | 8312.082 | 8312.082 | 8312.082–8312.082 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 8573.568 | 8573.568 | 8573.568 | 8573.568–8573.568 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 334.901 | 334.901 | 334.901 | 334.901–334.901 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 927.238 | 927.238 | 927.238 | 927.238–927.238 |
| B_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 7047.868 | 7047.868 | 7047.868 | 7047.868–7047.868 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7256.641 | 7256.641 | 7256.641 | 7256.641–7256.641 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 305.702 | 298.960 | 306.822 | 297.275–307.103 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 340.357 | 339.978 | 353.879 | 339.884–357.260 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 347.323 | 346.854 | 361.961 | 346.737–365.620 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 357.973 | 357.117 | 373.311 | 356.904–377.145 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 259.089 | 255.896 | 277.170 | 255.098–281.691 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 308.580 | 293.250 | 319.976 | 289.418–322.826 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 315.683 | 299.935 | 326.624 | 295.998–329.359 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 326.351 | 310.335 | 337.022 | 306.331–339.690 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 371.227 | 371.227 | 371.227 | 371.227–371.227 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2028.715 | 2028.715 | 2028.715 | 2028.715–2028.715 |
| C_simpleui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 20535.978 | 20535.978 | 20535.978 | 20535.978–20535.978 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 21508.679 | 21508.679 | 21508.679 | 21508.679–21508.679 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 344.413 | 344.413 | 344.413 | 344.413–344.413 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1620.870 | 1620.870 | 1620.870 | 1620.870–1620.870 |
| C_simpleui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11922.832 | 11922.832 | 11922.832 | 11922.832–11922.832 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11952.208 | 11952.208 | 11952.208 | 11952.208–11952.208 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 309.915 | 309.915 | 309.915 | 309.915–309.915 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1493.554 | 1493.554 | 1493.554 | 1493.554–1493.554 |
| C_simpleui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9316.992 | 9316.992 | 9316.992 | 9316.992–9316.992 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9343.270 | 9343.270 | 9343.270 | 9343.270–9343.270 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 426.286 | 426.286 | 426.286 | 426.286–426.286 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1601.650 | 1601.650 | 1601.650 | 1601.650–1601.650 |
| C_simpleui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8489.955 | 8489.955 | 8489.955 | 8489.955–8489.955 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8515.322 | 8515.322 | 8515.322 | 8515.322–8515.322 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 310.861 | 309.585 | 315.625 | 309.265–316.816 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 408.180 | 408.030 | 409.187 | 407.993–409.439 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 416.607 | 416.546 | 419.060 | 416.531–419.673 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 428.345 | 428.165 | 437.446 | 428.120–439.721 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 270.357 | 270.355 | 291.199 | 270.355–296.409 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 340.625 | 340.305 | 367.112 | 340.225–373.733 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 348.341 | 348.232 | 375.198 | 348.205–381.912 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 359.983 | 359.693 | 386.815 | 359.621–393.523 |
| D_zenos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 341.377 | 341.377 | 341.377 | 341.377–341.377 |
| D_zenos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2665.087 | 2665.087 | 2665.087 | 2665.087–2665.087 |
| D_zenos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 12548.035 | 12548.035 | 12548.035 | 12548.035–12548.035 |
| D_zenos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12564.480 | 12564.480 | 12564.480 | 12564.480–12564.480 |
| D_zenos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 317.834 | 317.834 | 317.834 | 317.834–317.834 |
| D_zenos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2420.709 | 2420.709 | 2420.709 | 2420.709–2420.709 |
| D_zenos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 10626.525 | 10626.525 | 10626.525 | 10626.525–10626.525 |
| D_zenos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10653.995 | 10653.995 | 10653.995 | 10653.995–10653.995 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 317.979 | 317.979 | 317.979 | 317.979–317.979 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2309.490 | 2309.490 | 2309.490 | 2309.490–2309.490 |
| D_zenos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9458.959 | 9458.959 | 9458.959 | 9458.959–9458.959 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9474.417 | 9474.417 | 9474.417 | 9474.417–9474.417 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 316.618 | 316.618 | 316.618 | 316.618–316.618 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2290.270 | 2290.270 | 2290.270 | 2290.270–2290.270 |
| D_zenos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9240.060 | 9240.060 | 9240.060 | 9240.060–9240.060 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9256.418 | 9256.418 | 9256.418 | 9256.418–9256.418 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 166.066 | 165.438 | 170.356 | 165.281–171.429 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 189.198 | 188.913 | 192.221 | 188.841–192.976 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 192.464 | 192.142 | 195.436 | 192.061–196.179 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 200.538 | 200.208 | 204.145 | 200.126–205.047 |
| E_project_title | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 227.217 | 227.217 | 227.217 | 227.217–227.217 |
| E_project_title | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1539.036 | 1539.036 | 1539.036 | 1539.036–1539.036 |
| E_project_title | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 9408.717 | 9408.717 | 9408.717 | 9408.717–9408.717 |
| E_project_title | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9422.238 | 9422.238 | 9422.238 | 9422.238–9422.238 |
| E_project_title | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 197.271 | 197.271 | 197.271 | 197.271–197.271 |
| E_project_title | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 792.288 | 792.288 | 792.288 | 792.288–792.288 |
| E_project_title | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 5546.237 | 5546.237 | 5546.237 | 5546.237–5546.237 |
| E_project_title | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5558.153 | 5558.153 | 5558.153 | 5558.153–5558.153 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 186.889 | 186.889 | 186.889 | 186.889–186.889 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 772.358 | 772.358 | 772.358 | 772.358–772.358 |
| E_project_title | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 4454.792 | 4454.792 | 4454.792 | 4454.792–4454.792 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 4467.240 | 4467.240 | 4467.240 | 4467.240–4467.240 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 196.914 | 196.914 | 196.914 | 196.914–196.914 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 795.323 | 795.323 | 795.323 | 795.323–795.323 |
| E_project_title | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4477.920 | 4477.920 | 4477.920 | 4477.920–4477.920 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4490.153 | 4490.153 | 4490.153 | 4490.153–4490.153 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 181.357 | 180.581 | 205.054 | 180.388–210.979 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 238.927 | 238.878 | 266.933 | 238.866–273.935 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 243.602 | 243.192 | 271.437 | 243.089–278.396 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 252.967 | 252.347 | 280.975 | 252.192–287.977 |
| F_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 267.667 | 267.667 | 267.667 | 267.667–267.667 |
| F_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2460.387 | 2460.387 | 2460.387 | 2460.387–2460.387 |
| F_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 13719.066 | 13719.066 | 13719.066 | 13719.066–13719.066 |
| F_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 13739.392 | 13739.392 | 13739.392 | 13739.392–13739.392 |
| F_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 226.205 | 226.205 | 226.205 | 226.205–226.205 |
| F_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1572.801 | 1572.801 | 1572.801 | 1572.801–1572.801 |
| F_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 8851.868 | 8851.868 | 8851.868 | 8851.868–8851.868 |
| F_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8871.644 | 8871.644 | 8871.644 | 8871.644–8871.644 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 216.610 | 216.610 | 216.610 | 216.610–216.610 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1408.079 | 1408.079 | 1408.079 | 1408.079–1408.079 |
| F_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 6990.209 | 6990.209 | 6990.209 | 6990.209–6990.209 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7002.903 | 7002.903 | 7002.903 | 7002.903–7002.903 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 214.612 | 214.612 | 214.612 | 214.612–214.612 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1409.272 | 1409.272 | 1409.272 | 1409.272–1409.272 |
| F_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6306.276 | 6306.276 | 6306.276 | 6306.276–6306.276 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6317.981 | 6317.981 | 6317.981 | 6317.981–6317.981 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 264.928 | 262.277 | 283.885 | 261.614–288.624 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 308.095 | 305.882 | 322.105 | 305.328–325.607 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 315.205 | 312.691 | 328.908 | 312.062–332.334 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 325.933 | 323.268 | 339.886 | 322.602–343.375 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 495.743 | 495.743 | 495.743 | 495.743–495.743 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2135.117 | 2135.117 | 2135.117 | 2135.117–2135.117 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 33006.774 | 33006.774 | 33006.774 | 33006.774–33006.774 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 34533.502 | 34533.502 | 34533.502 | 34533.502–34533.502 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 326.041 | 326.041 | 326.041 | 326.041–326.041 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1606.705 | 1606.705 | 1606.705 | 1606.705–1606.705 |
| G_simpleui_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18884.519 | 18884.519 | 18884.519 | 18884.519–18884.519 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18916.916 | 18916.916 | 18916.916 | 18916.916–18916.916 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 311.931 | 311.931 | 311.931 | 311.931–311.931 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1491.349 | 1491.349 | 1491.349 | 1491.349–1491.349 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11042.831 | 11042.831 | 11042.831 | 11042.831–11042.831 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11073.044 | 11073.044 | 11073.044 | 11073.044–11073.044 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 434.409 | 434.409 | 434.409 | 434.409–434.409 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1617.351 | 1617.351 | 1617.351 | 1617.351–1617.351 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10142.568 | 10142.568 | 10142.568 | 10142.568–10142.568 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10172.130 | 10172.130 | 10172.130 | 10172.130–10172.130 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 279.249 | 276.164 | 296.634 | 275.393–300.980 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 356.002 | 343.479 | 368.750 | 340.349–371.937 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 364.551 | 351.919 | 377.265 | 348.761–380.443 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 376.691 | 364.060 | 389.219 | 360.902–392.351 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 462.891 | 462.891 | 462.891 | 462.891–462.891 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2770.149 | 2770.149 | 2770.149 | 2770.149–2770.149 |
| H_zenos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 24510.899 | 24510.899 | 24510.899 | 24510.899–24510.899 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 24553.229 | 24553.229 | 24553.229 | 24553.229–24553.229 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 330.117 | 330.117 | 330.117 | 330.117–330.117 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2386.918 | 2386.918 | 2386.918 | 2386.918–2386.918 |
| H_zenos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18089.157 | 18089.157 | 18089.157 | 18089.157–18089.157 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18109.243 | 18109.243 | 18109.243 | 18109.243–18109.243 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 322.060 | 322.060 | 322.060 | 322.060–322.060 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2291.732 | 2291.732 | 2291.732 | 2291.732–2291.732 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11279.832 | 11279.832 | 11279.832 | 11279.832–11279.832 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11308.101 | 11308.101 | 11308.101 | 11308.101–11308.101 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 492.679 | 492.679 | 492.679 | 492.679–492.679 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2485.776 | 2485.776 | 2485.776 | 2485.776–2485.776 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 11239.726 | 11239.726 | 11239.726 | 11239.726–11239.726 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11265.686 | 11265.686 | 11265.686 | 11265.686–11265.686 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 202.005 | 191.399 | 213.344 | 188.748–216.179 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 252.852 | 242.335 | 272.993 | 239.706–278.028 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 257.414 | 246.931 | 277.262 | 244.310–282.224 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 266.783 | 256.371 | 286.583 | 253.768–291.533 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 291.207 | 291.207 | 291.207 | 291.207–291.207 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2625.802 | 2625.802 | 2625.802 | 2625.802–2625.802 |
| I_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 30453.136 | 30453.136 | 30453.136 | 30453.136–30453.136 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 30505.751 | 30505.751 | 30505.751 | 30505.751–30505.751 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 235.574 | 235.574 | 235.574 | 235.574–235.574 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1590.765 | 1590.765 | 1590.765 | 1590.765–1590.765 |
| I_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18436.019 | 18436.019 | 18436.019 | 18436.019–18436.019 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18453.355 | 18453.355 | 18453.355 | 18453.355–18453.355 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 226.667 | 226.667 | 226.667 | 226.667–226.667 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1426.391 | 1426.391 | 1426.391 | 1426.391–1426.391 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9639.675 | 9639.675 | 9639.675 | 9639.675–9639.675 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9666.675 | 9666.675 | 9666.675 | 9666.675–9666.675 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 355.704 | 355.704 | 355.704 | 355.704–355.704 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1551.475 | 1551.475 | 1551.475 | 1551.475–1551.475 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8791.143 | 8791.143 | 8791.143 | 8791.143–8791.143 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8813.870 | 8813.870 | 8813.870 | 8813.870–8813.870 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 326.126 | 313.184 | 329.837 | 309.948–330.765 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 368.027 | 363.138 | 368.783 | 361.916–368.972 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 377.597 | 373.194 | 378.899 | 372.094–379.224 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 391.256 | 385.833 | 391.892 | 384.478–392.051 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 358.397 | 358.397 | 358.397 | 358.397–358.397 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1926.992 | 1926.992 | 1926.992 | 1926.992–1926.992 |
| J_simpleui_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 22429.285 | 22429.285 | 22429.285 | 22429.285–22429.285 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 24912.400 | 24912.400 | 24912.400 | 24912.400–24912.400 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 307.847 | 307.847 | 307.847 | 307.847–307.847 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1490.718 | 1490.718 | 1490.718 | 1490.718–1490.718 |
| J_simpleui_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 10442.838 | 10442.838 | 10442.838 | 10442.838–10442.838 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10471.639 | 10471.639 | 10471.639 | 10471.639–10471.639 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 321.493 | 321.493 | 321.493 | 321.493–321.493 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1494.893 | 1494.893 | 1494.893 | 1494.893–1494.893 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9894.526 | 9894.526 | 9894.526 | 9894.526–9894.526 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9927.326 | 9927.326 | 9927.326 | 9927.326–9927.326 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 441.110 | 441.110 | 441.110 | 441.110–441.110 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1618.434 | 1618.434 | 1618.434 | 1618.434–1618.434 |
| J_simpleui_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9175.321 | 9175.321 | 9175.321 | 9175.321–9175.321 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9201.885 | 9201.885 | 9201.885 | 9201.885–9201.885 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 285.467 | 275.340 | 302.016 | 272.808–306.153 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 329.154 | 313.911 | 342.034 | 310.101–345.255 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 336.680 | 321.559 | 349.838 | 317.779–353.127 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 348.080 | 332.488 | 360.911 | 328.589–364.119 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 542.439 | 542.439 | 542.439 | 542.439–542.439 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2194.395 | 2194.395 | 2194.395 | 2194.395–2194.395 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 35135.586 | 35135.586 | 35135.586 | 35135.586–35135.586 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 46692.497 | 46692.497 | 46692.497 | 46692.497–46692.497 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 345.758 | 345.758 | 345.758 | 345.758–345.758 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1584.410 | 1584.410 | 1584.410 | 1584.410–1584.410 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 19517.632 | 19517.632 | 19517.632 | 19517.632–19517.632 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 19553.581 | 19553.581 | 19553.581 | 19553.581–19553.581 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 334.636 | 334.636 | 334.636 | 334.636–334.636 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1516.244 | 1516.244 | 1516.244 | 1516.244–1516.244 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11153.051 | 11153.051 | 11153.051 | 11153.051–11153.051 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11187.258 | 11187.258 | 11187.258 | 11187.258–11187.258 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 451.435 | 451.435 | 451.435 | 451.435–451.435 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1620.473 | 1620.473 | 1620.473 | 1620.473–1620.473 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10297.984 | 10297.984 | 10297.984 | 10297.984–10297.984 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10374.939 | 10374.939 | 10374.939 | 10374.939–10374.939 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 217.741 | 215.808 | 217.842 | 215.325–217.867 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 273.358 | 273.305 | 274.138 | 273.291–274.333 |
| K_vos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 277.897 | 277.664 | 278.636 | 277.606–278.821 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 287.486 | 287.011 | 287.952 | 286.892–288.068 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 187.437 | 186.658 | 189.292 | 186.463–189.756 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 242.306 | 242.189 | 242.380 | 242.159–242.398 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 246.654 | 246.532 | 246.971 | 246.502–247.050 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 256.113 | 255.696 | 256.837 | 255.591–257.018 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 250.172 | 250.172 | 250.172 | 250.172–250.172 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2056.845 | 2056.845 | 2056.845 | 2056.845–2056.845 |
| L_project_title_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 11174.566 | 11174.566 | 11174.566 | 11174.566–11174.566 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11188.557 | 11188.557 | 11188.557 | 11188.557–11188.557 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 219.113 | 219.113 | 219.113 | 219.113–219.113 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1412.150 | 1412.150 | 1412.150 | 1412.150–1412.150 |
| L_project_title_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 7403.138 | 7403.138 | 7403.138 | 7403.138–7403.138 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7415.459 | 7415.459 | 7415.459 | 7415.459–7415.459 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 209.100 | 209.100 | 209.100 | 209.100–209.100 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1408.650 | 1408.650 | 1408.650 | 1408.650–1408.650 |
| L_project_title_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 6138.077 | 6138.077 | 6138.077 | 6138.077–6138.077 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 6151.190 | 6151.190 | 6151.190 | 6151.190–6151.190 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 216.341 | 216.341 | 216.341 | 216.341–216.341 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1414.985 | 1414.985 | 1414.985 | 1414.985–1414.985 |
| L_project_title_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6097.344 | 6097.344 | 6097.344 | 6097.344–6097.344 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6111.038 | 6111.038 | 6111.038 | 6111.038–6111.038 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 230.813 | 230.142 | 231.871 | 229.974–232.136 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 262.740 | 262.717 | 263.306 | 262.711–263.448 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 267.779 | 267.545 | 268.036 | 267.486–268.100 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 276.881 | 276.780 | 277.202 | 276.755–277.282 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 199.918 | 196.535 | 212.454 | 195.690–215.588 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 228.812 | 227.646 | 240.267 | 227.354–243.131 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 233.484 | 232.113 | 244.988 | 231.770–247.864 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 242.942 | 241.272 | 254.165 | 240.855–256.971 |
| M_leanui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 291.472 | 291.472 | 291.472 | 291.472–291.472 |
| M_leanui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1725.527 | 1725.527 | 1725.527 | 1725.527–1725.527 |
| M_leanui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 11116.473 | 11116.473 | 11116.473 | 11116.473–11116.473 |
| M_leanui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11131.959 | 11131.959 | 11131.959 | 11131.959–11131.959 |
| M_leanui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 248.498 | 248.498 | 248.498 | 248.498–248.498 |
| M_leanui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 846.495 | 846.495 | 846.495 | 846.495–846.495 |
| M_leanui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 6335.235 | 6335.235 | 6335.235 | 6335.235–6335.235 |
| M_leanui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6348.192 | 6348.192 | 6348.192 | 6348.192–6348.192 |
| M_leanui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 227.920 | 227.920 | 227.920 | 227.920–227.920 |
| M_leanui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 828.992 | 828.992 | 828.992 | 828.992–828.992 |
| M_leanui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 5095.274 | 5095.274 | 5095.274 | 5095.274–5095.274 |
| M_leanui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 5109.114 | 5109.114 | 5109.114 | 5109.114–5109.114 |
| M_leanui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 232.014 | 232.014 | 232.014 | 232.014–232.014 |
| M_leanui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 830.911 | 830.911 | 830.911 | 830.911–830.911 |
| M_leanui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4745.329 | 4745.329 | 4745.329 | 4745.329–4745.329 |
| M_leanui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4759.248 | 4759.248 | 4759.248 | 4759.248–4759.248 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 222.861 | 214.447 | 241.168 | 212.343–245.745 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 248.115 | 244.721 | 263.970 | 243.873–267.934 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 252.505 | 248.655 | 268.671 | 247.693–272.713 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 262.504 | 257.554 | 278.571 | 256.316–282.587 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 179.114 | 177.014 | 213.831 | 176.489–222.510 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 212.425 | 197.966 | 236.879 | 194.352–242.992 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 216.471 | 201.512 | 240.505 | 197.772–246.513 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 225.722 | 210.445 | 249.539 | 206.626–255.494 |
| N_m1n1mal | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 263.897 | 263.897 | 263.897 | 263.897–263.897 |
| N_m1n1mal | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3149.870 | 3149.870 | 3149.870 | 3149.870–3149.870 |
| N_m1n1mal | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 15171.246 | 15171.246 | 15171.246 | 15171.246–15171.246 |
| N_m1n1mal | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 15211.544 | 15211.544 | 15211.544 | 15211.544–15211.544 |
| N_m1n1mal | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 223.818 | 223.818 | 223.818 | 223.818–223.818 |
| N_m1n1mal | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1170.840 | 1170.840 | 1170.840 | 1170.840–1170.840 |
| N_m1n1mal | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 8147.414 | 8147.414 | 8147.414 | 8147.414–8147.414 |
| N_m1n1mal | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8166.488 | 8166.488 | 8166.488 | 8166.488–8166.488 |
| N_m1n1mal | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 216.859 | 216.859 | 216.859 | 216.859–216.859 |
| N_m1n1mal | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 822.459 | 822.459 | 822.459 | 822.459–822.459 |
| N_m1n1mal | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 6135.745 | 6135.745 | 6135.745 | 6135.745–6135.745 |
| N_m1n1mal | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 6155.871 | 6155.871 | 6155.871 | 6155.871–6155.871 |
| N_m1n1mal | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 268.516 | 268.516 | 268.516 | 268.516–268.516 |
| N_m1n1mal | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 864.451 | 864.451 | 864.451 | 864.451–864.451 |
| N_m1n1mal | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5139.765 | 5139.765 | 5139.765 | 5139.765–5139.765 |
| N_m1n1mal | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5158.071 | 5158.071 | 5158.071 | 5158.071–5158.071 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 196.367 | 196.367 | 196.367 | 196.367–196.367 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 224.279 | 224.279 | 224.279 | 224.279–224.279 |
| A_stock | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 227.884 | 227.884 | 227.884 | 227.884–227.884 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 236.660 | 236.660 | 236.660 | 236.660–236.660 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 211.065 | 211.065 | 211.065 | 211.065–211.065 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 240.607 | 240.607 | 240.607 | 240.607–240.607 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 244.321 | 244.321 | 244.321 | 244.321–244.321 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 252.806 | 252.806 | 252.806 | 252.806–252.806 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 302.910 | 302.910 | 302.910 | 302.910–302.910 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 342.630 | 342.630 | 342.630 | 342.630–342.630 |
| C_simpleui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 349.630 | 349.630 | 349.630 | 349.630–349.630 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 360.331 | 360.331 | 360.331 | 360.331–360.331 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 310.763 | 310.763 | 310.763 | 310.763–310.763 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 407.615 | 407.615 | 407.615 | 407.615–407.615 |
| D_zenos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 416.240 | 416.240 | 416.240 | 416.240–416.240 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 427.688 | 427.688 | 427.688 | 427.688–427.688 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 189.381 | 189.381 | 189.381 | 189.381–189.381 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 207.138 | 207.138 | 207.138 | 207.138–207.138 |
| E_project_title | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 210.382 | 210.382 | 210.382 | 210.382–210.382 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 218.903 | 218.903 | 218.903 | 218.903–218.903 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 211.713 | 211.713 | 211.713 | 211.713–211.713 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 272.442 | 272.442 | 272.442 | 272.442–272.442 |
| F_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 277.101 | 277.101 | 277.101 | 277.101–277.101 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 286.410 | 286.410 | 286.410 | 286.410–286.410 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 313.506 | 313.506 | 313.506 | 313.506–313.506 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 356.096 | 356.096 | 356.096 | 356.096–356.096 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 363.316 | 363.316 | 363.316 | 363.316–363.316 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 374.054 | 374.054 | 374.054 | 374.054–374.054 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 317.036 | 317.036 | 317.036 | 317.036–317.036 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 409.674 | 409.674 | 409.674 | 409.674–409.674 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 418.470 | 418.470 | 418.470 | 418.470–418.470 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 430.366 | 430.366 | 430.366 | 430.366–430.366 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 223.268 | 223.268 | 223.268 | 223.268–223.268 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 290.323 | 290.323 | 290.323 | 290.323–290.323 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 295.339 | 295.339 | 295.339 | 295.339–295.339 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 305.037 | 305.037 | 305.037 | 305.037–305.037 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 385.173 | 385.173 | 385.173 | 385.173–385.173 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 434.919 | 434.919 | 434.919 | 434.919–434.919 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 442.995 | 442.995 | 442.995 | 442.995–442.995 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 454.042 | 454.042 | 454.042 | 454.042–454.042 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 330.373 | 330.373 | 330.373 | 330.373–330.373 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 380.111 | 380.111 | 380.111 | 380.111–380.111 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 387.854 | 387.854 | 387.854 | 387.854–387.854 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 398.719 | 398.719 | 398.719 | 398.719–398.719 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 210.289 | 210.289 | 210.289 | 210.289–210.289 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 275.775 | 275.775 | 275.775 | 275.775–275.775 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 280.342 | 280.342 | 280.342 | 280.342–280.342 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 289.899 | 289.899 | 289.899 | 289.899–289.899 |
| M_leanui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 222.077 | 222.077 | 222.077 | 222.077–222.077 |
| M_leanui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 244.833 | 244.833 | 244.833 | 244.833–244.833 |
| M_leanui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 249.597 | 249.597 | 249.597 | 249.597–249.597 |
| M_leanui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 258.881 | 258.881 | 258.881 | 258.881–258.881 |
| N_m1n1mal | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 213.785 | 213.785 | 213.785 | 213.785–213.785 |
| N_m1n1mal | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 247.364 | 247.364 | 247.364 | 247.364–247.364 |
| N_m1n1mal | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 251.993 | 251.993 | 251.993 | 251.993–251.993 |
| N_m1n1mal | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 261.963 | 261.963 | 261.963 | 261.963–261.963 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8363.679 | 8441.901 | 8263.729–8461.456 | 14694.915 | 84096.000 |
| A_stock | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8506.237 | 8516.544 | 8432.897–8519.120 | 9103.341 | 84096.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8219.007 | 8323.732 | 8197.460–8349.913 | 12253.756 | 78528.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8211.573 | 8274.504 | 8196.472–8290.237 | 8905.211 | 79168.000 |
| A_stock | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 10855.741 | 10855.741 | 10855.741–10855.741 | 17063.654 | 86848.000 |
| A_stock | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 29555.472 | 29555.472 | 29555.472–29555.472 | 45341.113 | 213344.000 |
| A_stock | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 26519.229 | 26519.229 | 26519.229–26519.229 | 30264.454 | 226336.000 |
| A_stock | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8594.167 | 8594.167 | 8594.167–8594.167 | 15202.598 | 83984.000 |
| A_stock | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 26248.675 | 26248.675 | 26248.675–26248.675 | 26262.331 | 127712.000 |
| A_stock | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 15865.904 | 15865.904 | 15865.904–15865.904 | 19319.696 | 184016.000 |
| A_stock | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8335.479 | 8335.479 | 8335.479–8335.479 | 13066.467 | 82608.000 |
| A_stock | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8330.784 | 8330.784 | 8330.784–8330.784 | 8341.261 | 86768.000 |
| A_stock | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 20310.128 | 20310.128 | 20310.128–20310.128 | 24980.333 | 132128.000 |
| A_stock | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8294.218 | 8294.218 | 8294.218–8294.218 | 14755.995 | 84080.000 |
| A_stock | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8307.386 | 8307.386 | 8307.386–8307.386 | 8317.862 | 88976.000 |
| A_stock | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12702.979 | 12702.979 | 12702.979–12702.979 | 19645.158 | 121072.000 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8906.280 | 8912.680 | 8905.647–8914.280 | 10191.897 | 84032.000 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8992.733 | 8995.146 | 8989.909–8995.749 | 9715.442 | 84032.000 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8657.309 | 8769.805 | 8655.605–8797.930 | 14129.277 | 79408.000 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8710.324 | 8776.143 | 8624.344–8792.598 | 9353.506 | 79440.000 |
| B_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11456.323 | 11456.323 | 11456.323–11456.323 | 19436.403 | 88928.000 |
| B_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 30003.319 | 30003.319 | 30003.319–30003.319 | 40587.976 | 207584.000 |
| B_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 30578.308 | 30578.308 | 30578.308–30578.308 | 35055.900 | 288688.000 |
| B_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9270.956 | 9270.956 | 9270.956–9270.956 | 10836.613 | 83664.000 |
| B_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 27181.780 | 27181.780 | 27181.780–27181.780 | 27192.284 | 130288.000 |
| B_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 21098.076 | 21098.076 | 21098.076–21098.076 | 21118.771 | 229552.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8857.589 | 8857.589 | 8857.589–8857.589 | 9866.998 | 85200.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8774.038 | 8774.038 | 8774.038–8774.038 | 8784.515 | 88160.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 53831.360 | 53831.360 | 53831.360–53831.360 | 66679.460 | 210288.000 |
| B_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8956.362 | 8956.362 | 8956.362–8956.362 | 10139.663 | 84752.000 |
| B_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8822.308 | 8822.308 | 8822.308–8822.308 | 8832.784 | 87776.000 |
| B_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 42143.172 | 42143.172 | 42143.172–42143.172 | 67936.592 | 181456.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14043.402 | 14058.374 | 13996.090–14062.117 | 15514.698 | 94672.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14200.777 | 14238.824 | 14192.773–14248.336 | 15510.173 | 95040.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 13989.406 | 13990.134 | 13968.137–13990.316 | 20922.339 | 89248.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14208.684 | 14262.596 | 14196.457–14276.074 | 15416.505 | 89680.000 |
| C_simpleui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16381.535 | 16381.535 | 16381.535–16381.535 | 24747.191 | 98704.000 |
| C_simpleui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 25366.457 | 25366.457 | 25366.457–25366.457 | 26006.797 | 120432.000 |
| C_simpleui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 106254.969 | 106254.969 | 106254.969–106254.969 | 107061.965 | 235872.000 |
| C_simpleui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14320.629 | 14320.629 | 14320.629–14320.629 | 17174.907 | 94000.000 |
| C_simpleui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 17838.836 | 17838.836 | 17838.836–17838.836 | 20262.525 | 108000.000 |
| C_simpleui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 55380.004 | 55380.004 | 55380.004–55380.004 | 55409.516 | 188704.000 |
| C_simpleui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14146.613 | 14146.613 | 14146.613–14146.613 | 15223.754 | 95792.000 |
| C_simpleui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14358.258 | 14358.258 | 14358.258–14358.258 | 15594.444 | 96144.000 |
| C_simpleui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 51436.176 | 51436.176 | 51436.176–51436.176 | 55191.890 | 171408.000 |
| C_simpleui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 13979.680 | 13979.680 | 13979.680–13979.680 | 14917.528 | 95072.000 |
| C_simpleui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14315.543 | 14315.543 | 14315.543–14315.543 | 15572.311 | 95488.000 |
| C_simpleui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 50553.109 | 50553.109 | 50553.109–50553.109 | 54617.375 | 168592.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14402.246 | 14422.715 | 14394.105–14427.832 | 18975.592 | 93264.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15571.676 | 15592.320 | 15555.621–15597.480 | 17522.007 | 99584.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14405.278 | 14454.613 | 14377.126–14466.946 | 23136.975 | 92928.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15226.677 | 15259.680 | 15208.700–15267.931 | 17060.930 | 95904.000 |
| D_zenos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16026.915 | 16026.915 | 16026.915–16026.915 | 25683.812 | 98320.000 |
| D_zenos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 22721.841 | 22721.841 | 22721.841–22721.841 | 24178.826 | 135424.000 |
| D_zenos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 22919.822 | 22919.822 | 22919.822–22919.822 | 23406.160 | 159824.000 |
| D_zenos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14356.618 | 14356.618 | 14356.618–14356.618 | 19391.839 | 93088.000 |
| D_zenos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 17381.595 | 17381.595 | 17381.595–17381.595 | 17604.466 | 113472.000 |
| D_zenos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 18092.846 | 18092.846 | 18092.846–18092.846 | 18557.117 | 149648.000 |
| D_zenos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14428.520 | 14428.520 | 14428.520–14428.520 | 19639.252 | 92528.000 |
| D_zenos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 16548.243 | 16548.243 | 16548.243–16548.243 | 17360.336 | 112624.000 |
| D_zenos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 20482.123 | 20482.123 | 20482.123–20482.123 | 23107.225 | 143424.000 |
| D_zenos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14378.117 | 14378.117 | 14378.117–14378.117 | 19377.041 | 92640.000 |
| D_zenos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14871.001 | 14871.001 | 14871.001–14871.001 | 15669.004 | 105968.000 |
| D_zenos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 18422.225 | 18422.225 | 18422.225–18422.225 | 20027.798 | 140416.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8323.896 | 8329.621 | 8308.794–8331.052 | 13359.751 | 78528.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8271.860 | 8296.032 | 8265.989–8302.075 | 8986.098 | 78528.000 |
| E_project_title | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11025.599 | 11025.599 | 11025.599–11025.599 | 16730.531 | 85584.000 |
| E_project_title | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 11141.544 | 11141.544 | 11141.544–11141.544 | 19007.373 | 101920.000 |
| E_project_title | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 16158.854 | 16158.854 | 16158.854–16158.854 | 40936.923 | 137056.000 |
| E_project_title | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8898.997 | 8898.997 | 8898.997–8898.997 | 15331.688 | 84016.000 |
| E_project_title | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 8913.458 | 8913.458 | 8913.458–8913.458 | 18799.510 | 94208.000 |
| E_project_title | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 12245.705 | 12245.705 | 12245.705–12245.705 | 15992.458 | 123264.000 |
| E_project_title | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8342.177 | 8342.177 | 8342.177–8342.177 | 14449.188 | 83504.000 |
| E_project_title | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8412.188 | 8412.188 | 8412.188–8412.188 | 11272.370 | 89664.000 |
| E_project_title | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 12039.190 | 12039.190 | 12039.190–12039.190 | 26570.700 | 122848.000 |
| E_project_title | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8368.993 | 8368.993 | 8368.993–8368.993 | 14617.901 | 83776.000 |
| E_project_title | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8362.583 | 8362.583 | 8362.583–8362.583 | 14813.341 | 89744.000 |
| E_project_title | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 11376.030 | 11376.030 | 11376.030–11376.030 | 25030.067 | 114640.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8944.065 | 8998.178 | 8917.190–9011.706 | 14550.855 | 81392.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8946.347 | 9022.237 | 8903.522–9041.210 | 9895.092 | 81520.000 |
| F_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11686.835 | 11686.835 | 11686.835–11686.835 | 19724.443 | 90768.000 |
| F_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 20924.140 | 20924.140 | 20924.140–20924.140 | 37768.879 | 160560.000 |
| F_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 16494.646 | 16494.646 | 16494.646–16494.646 | 18174.589 | 183520.000 |
| F_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9461.519 | 9461.519 | 9461.519–9461.519 | 10623.966 | 85872.000 |
| F_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 27250.019 | 27250.019 | 27250.019–27250.019 | 35104.086 | 141984.000 |
| F_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 14088.158 | 14088.158 | 14088.158–14088.158 | 18959.590 | 165648.000 |
| F_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8925.237 | 8925.237 | 8925.237–8925.237 | 9712.629 | 86256.000 |
| F_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8965.038 | 8965.038 | 8965.038–8965.038 | 9515.197 | 86448.000 |
| F_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 15439.838 | 15439.838 | 15439.838–15439.838 | 26642.870 | 133744.000 |
| F_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9044.511 | 9044.511 | 9044.511–9044.511 | 15993.993 | 86656.000 |
| F_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9010.655 | 9010.655 | 9010.655–9010.655 | 9478.279 | 88048.000 |
| F_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12558.650 | 12558.650 | 12558.650–12558.650 | 23866.126 | 117024.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14395.942 | 14429.686 | 14391.438–14438.122 | 22559.122 | 90992.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14593.325 | 14644.003 | 14585.548–14656.673 | 15874.105 | 91376.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16937.184 | 16937.184 | 16937.184–16937.184 | 25851.395 | 97888.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 27650.434 | 27650.434 | 27650.434–27650.434 | 34108.083 | 119424.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 111108.474 | 111108.474 | 111108.474–111108.474 | 111974.226 | 271904.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15025.547 | 15025.547 | 15025.547–15025.547 | 19356.322 | 94528.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 18411.508 | 18411.508 | 18411.508–18411.508 | 19101.358 | 110064.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 59694.551 | 59694.551 | 59694.551–59694.551 | 60445.819 | 219504.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14690.152 | 14690.152 | 14690.152–14690.152 | 18072.126 | 94624.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14774.484 | 14774.484 | 14774.484–14774.484 | 16040.632 | 96352.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 57852.065 | 57852.065 | 57852.065–57852.065 | 61666.599 | 207904.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14657.836 | 14657.836 | 14657.836–14657.836 | 17555.574 | 94224.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14802.086 | 14802.086 | 14802.086–14802.086 | 16170.219 | 96160.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 54577.358 | 54577.358 | 54577.358–54577.358 | 58123.300 | 202704.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14843.170 | 14907.198 | 14842.393–14923.205 | 16384.560 | 95616.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15728.771 | 15734.450 | 15702.182–15735.869 | 17435.941 | 99008.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16719.856 | 16719.856 | 16719.856–16719.856 | 27575.481 | 100528.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 23339.177 | 23339.177 | 23339.177–23339.177 | 25292.485 | 137248.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 29885.870 | 29885.870 | 29885.870–29885.870 | 30597.310 | 209392.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15132.360 | 15132.360 | 15132.360–15132.360 | 21835.224 | 94096.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 18152.802 | 18152.802 | 18152.802–18152.802 | 18285.282 | 115920.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 23389.498 | 23389.498 | 23389.498–23389.498 | 23990.215 | 197696.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15120.816 | 15120.816 | 15120.816–15120.816 | 21383.330 | 93408.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 17044.317 | 17044.317 | 17044.317–17044.317 | 17912.144 | 113120.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 49269.801 | 49269.801 | 49269.801–49269.801 | 50752.353 | 204128.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 15109.520 | 15109.520 | 15109.520–15109.520 | 21141.526 | 95136.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15402.376 | 15402.376 | 15402.376–15402.376 | 16215.875 | 107856.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 44907.719 | 44907.719 | 44907.719–44907.719 | 46654.241 | 185936.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9350.609 | 9415.391 | 9343.734–9431.586 | 15913.858 | 82848.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9359.340 | 9379.902 | 9353.602–9385.043 | 10314.594 | 83008.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 12280.577 | 12280.577 | 12280.577–12280.577 | 15512.058 | 93120.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 19826.448 | 19826.448 | 19826.448–19826.448 | 37266.480 | 167040.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 22522.437 | 22522.437 | 22522.437–22522.437 | 25302.567 | 275456.000 |
| I_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9915.163 | 9915.163 | 9915.163–9915.163 | 12201.726 | 85776.000 |
| I_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 30354.296 | 30354.296 | 30354.296–30354.296 | 37203.288 | 144352.000 |
| I_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 19419.123 | 19419.123 | 19419.123–19419.123 | 19450.506 | 223664.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9556.870 | 9556.870 | 9556.870–9556.870 | 11403.412 | 86112.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9513.347 | 9513.347 | 9513.347–9513.347 | 10048.403 | 86112.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 56367.586 | 56367.586 | 56367.586–56367.586 | 71267.173 | 202096.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9604.979 | 9604.979 | 9604.979–9604.979 | 11344.192 | 85968.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9484.077 | 9484.077 | 9484.077–9484.077 | 10046.038 | 85968.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 45653.957 | 45653.957 | 45653.957–45653.957 | 64164.442 | 171088.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14448.989 | 14476.761 | 14442.329–14483.704 | 22126.265 | 91168.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14666.966 | 14692.641 | 14662.798–14699.060 | 15719.687 | 93792.000 |
| J_simpleui_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16955.724 | 16955.724 | 16955.724–16955.724 | 24710.839 | 96432.000 |
| J_simpleui_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 20672.653 | 20672.653 | 20672.653–20672.653 | 27792.510 | 121968.000 |
| J_simpleui_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 109065.196 | 109065.196 | 109065.196–109065.196 | 112251.812 | 247472.000 |
| J_simpleui_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15045.114 | 15045.114 | 15045.114–15045.114 | 22802.467 | 94304.000 |
| J_simpleui_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16069.485 | 16069.485 | 16069.485–16069.485 | 18117.419 | 108304.000 |
| J_simpleui_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 58262.673 | 58262.673 | 58262.673–58262.673 | 60280.980 | 190704.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14542.610 | 14542.610 | 14542.610–14542.610 | 16847.646 | 94800.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14888.505 | 14888.505 | 14888.505–14888.505 | 15993.238 | 100160.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 57245.860 | 57245.860 | 57245.860–57245.860 | 66530.417 | 188480.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14466.505 | 14466.505 | 14466.505–14466.505 | 15912.192 | 94624.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14876.899 | 14876.899 | 14876.899–14876.899 | 15966.481 | 99808.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 52919.704 | 52919.704 | 52919.704–52919.704 | 61110.964 | 179072.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14892.186 | 14936.014 | 14850.166–14946.971 | 22696.222 | 91600.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15110.701 | 15160.039 | 15033.049–15172.373 | 16152.848 | 93760.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17545.935 | 17545.935 | 17545.935–17545.935 | 28070.263 | 100176.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 21204.724 | 21204.724 | 21204.724–21204.724 | 34269.019 | 123296.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 115606.115 | 115606.115 | 115606.115–115606.115 | 117554.055 | 282608.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15414.892 | 15414.892 | 15414.892–15414.892 | 18474.995 | 95280.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16348.005 | 16348.005 | 16348.005–16348.005 | 20449.589 | 112160.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 62325.419 | 62325.419 | 62325.419–62325.419 | 65892.819 | 222064.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15230.325 | 15230.325 | 15230.325–15230.325 | 18944.273 | 95072.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15434.372 | 15434.372 | 15434.372–15434.372 | 16478.649 | 100976.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 63536.652 | 63536.652 | 63536.652–63536.652 | 72171.473 | 224032.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 15156.212 | 15156.212 | 15156.212–15156.212 | 18001.768 | 94736.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15395.813 | 15395.813 | 15395.813–15395.813 | 16438.592 | 100560.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 56613.387 | 56613.387 | 56613.387–56613.387 | 65303.274 | 206544.000 |
| K_vos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8946.093 | 8974.546 | 8921.468–8981.659 | 9533.679 | 87328.000 |
| K_vos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8937.698 | 8962.367 | 8917.323–8968.534 | 10051.295 | 87472.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9000.083 | 9044.705 | 8975.911–9055.860 | 14875.756 | 81584.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9079.978 | 9091.646 | 9033.024–9094.563 | 9990.371 | 81600.000 |
| L_project_title_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11974.239 | 11974.239 | 11974.239–11974.239 | 20382.821 | 91136.000 |
| L_project_title_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 12015.974 | 12015.974 | 12015.974–12015.974 | 29262.432 | 107504.000 |
| L_project_title_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17328.416 | 17328.416 | 17328.416–17328.416 | 46912.024 | 146096.000 |
| L_project_title_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9581.446 | 9581.446 | 9581.446–9581.446 | 10151.451 | 86448.000 |
| L_project_title_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 9679.778 | 9679.778 | 9679.778–9679.778 | 26909.142 | 98768.000 |
| L_project_title_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13224.592 | 13224.592 | 13224.592–13224.592 | 21303.674 | 136224.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9061.239 | 9061.239 | 9061.239–9061.239 | 9557.432 | 87456.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9061.646 | 9061.646 | 9061.646–9061.646 | 14809.667 | 94096.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 12724.506 | 12724.506 | 12724.506–12724.506 | 16871.618 | 127728.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9083.899 | 9083.899 | 9083.899–9083.899 | 9551.973 | 86192.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9064.806 | 9064.806 | 9064.806–9064.806 | 14543.210 | 92896.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 13422.447 | 13422.447 | 13422.447–13422.447 | 25212.851 | 119344.000 |
| M_leanui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 10111.104 | 10257.095 | 10105.913–10293.593 | 12401.395 | 84512.000 |
| M_leanui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 10213.000 | 10288.119 | 10185.148–10306.898 | 11182.472 | 84512.000 |
| M_leanui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 10144.223 | 10155.188 | 10135.652–10157.930 | 14796.836 | 79792.000 |
| M_leanui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 10179.146 | 10204.899 | 10135.563–10211.337 | 11127.134 | 79808.000 |
| M_leanui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 13092.554 | 13092.554 | 13092.554–13092.554 | 13750.998 | 91920.000 |
| M_leanui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 13237.508 | 13237.508 | 13237.508–13237.508 | 33616.696 | 109072.000 |
| M_leanui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17389.473 | 17389.473 | 17389.473–17389.473 | 46978.371 | 158080.000 |
| M_leanui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 11006.327 | 11006.327 | 11006.327–11006.327 | 16799.377 | 85616.000 |
| M_leanui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 11135.473 | 11135.473 | 11135.473–11135.473 | 21649.859 | 100816.000 |
| M_leanui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13733.676 | 13733.676 | 13733.676–13733.676 | 21424.623 | 148352.000 |
| M_leanui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 10165.886 | 10165.886 | 10165.886–10165.886 | 12181.264 | 84896.000 |
| M_leanui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 10281.086 | 10281.086 | 10281.086–10281.086 | 14117.285 | 93872.000 |
| M_leanui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 13384.083 | 13384.083 | 13384.083–13384.083 | 19450.161 | 130704.000 |
| M_leanui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 10185.694 | 10185.694 | 10185.694–10185.694 | 12436.902 | 84512.000 |
| M_leanui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 10269.953 | 10269.953 | 10269.953–10269.953 | 14249.411 | 94224.000 |
| M_leanui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12681.298 | 12681.298 | 12681.298–12681.298 | 18951.646 | 137264.000 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8480.899 | 8536.512 | 8393.200–8550.415 | 14964.443 | 84896.000 |
| N_m1n1mal | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8612.700 | 8623.063 | 8569.849–8625.653 | 9242.437 | 85360.000 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8389.610 | 8442.185 | 8317.802–8455.329 | 10522.134 | 80048.000 |
| N_m1n1mal | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8399.528 | 8426.269 | 8356.290–8432.954 | 9059.656 | 80544.000 |
| N_m1n1mal | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 10952.688 | 10952.688 | 10952.688–10952.688 | 17410.190 | 87312.000 |
| N_m1n1mal | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 29324.821 | 29324.821 | 29324.821–29324.821 | 44078.896 | 211968.000 |
| N_m1n1mal | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 22861.672 | 22861.672 | 22861.672–22861.672 | 24273.767 | 227504.000 |
| N_m1n1mal | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8789.794 | 8789.794 | 8789.794–8789.794 | 15435.922 | 84432.000 |
| N_m1n1mal | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 25745.892 | 25745.892 | 25745.892–25745.892 | 25756.396 | 128000.000 |
| N_m1n1mal | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13996.922 | 13996.922 | 13996.922–13996.922 | 17539.793 | 178832.000 |
| N_m1n1mal | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8408.169 | 8408.169 | 8408.169–8408.169 | 15010.951 | 84592.000 |
| N_m1n1mal | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8430.462 | 8430.462 | 8430.462–8430.462 | 8440.591 | 88016.000 |
| N_m1n1mal | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 18939.988 | 18939.988 | 18939.988–18939.988 | 28737.854 | 146800.000 |
| N_m1n1mal | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8377.739 | 8377.739 | 8377.739–8377.739 | 13149.667 | 82688.000 |
| N_m1n1mal | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8433.028 | 8433.028 | 8433.028–8433.028 | 8443.505 | 86560.000 |
| N_m1n1mal | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 11426.414 | 11426.414 | 11426.414–11426.414 | 21446.813 | 122704.000 |
| A_stock | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8306.690 | 8306.690 | 8306.690–8306.690 | 14619.756 | 83856.000 |
| A_stock | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8480.218 | 8480.218 | 8480.218–8480.218 | 9161.882 | 83888.000 |
| B_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8857.304 | 8857.304 | 8857.304–8857.304 | 9924.520 | 85136.000 |
| B_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8932.831 | 8932.831 | 8932.831–8932.831 | 9720.016 | 85136.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14027.461 | 14027.461 | 14027.461–14027.461 | 15690.171 | 94672.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14251.953 | 14251.953 | 14251.953–14251.953 | 15582.091 | 95024.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14407.223 | 14407.223 | 14407.223–14407.223 | 19446.813 | 92720.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15588.031 | 15588.031 | 15588.031–15588.031 | 17597.515 | 99024.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8388.751 | 8388.751 | 8388.751–8388.751 | 14288.411 | 83344.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8365.731 | 8365.731 | 8365.731–8365.731 | 9072.073 | 83344.000 |
| F_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8995.077 | 8995.077 | 8995.077–8995.077 | 15085.014 | 85664.000 |
| F_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8971.757 | 8971.757 | 8971.757–8971.757 | 9999.658 | 85776.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14681.797 | 14681.797 | 14681.797–14681.797 | 16316.240 | 96096.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14793.293 | 14793.293 | 14793.293–14793.293 | 16203.271 | 96320.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15032.035 | 15032.035 | 15032.035–15032.035 | 20741.929 | 94768.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 16174.984 | 16174.984 | 16174.984–16174.984 | 18136.944 | 101056.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9593.272 | 9593.272 | 9593.272–9593.272 | 10257.788 | 87344.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9571.671 | 9571.671 | 9571.671–9571.671 | 10561.348 | 87344.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14542.771 | 14542.771 | 14542.771–14542.771 | 17220.001 | 94928.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14681.165 | 14681.165 | 14681.165–14681.165 | 15857.395 | 97680.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15147.634 | 15147.634 | 15147.634–15147.634 | 18896.596 | 94736.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15283.153 | 15283.153 | 15283.153–15283.153 | 16663.356 | 96656.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9078.298 | 9078.298 | 9078.298–9078.298 | 16066.752 | 86544.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9066.290 | 9066.290 | 9066.290–9066.290 | 10113.907 | 86704.000 |
| M_leanui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 10187.624 | 10187.624 | 10187.624–10187.624 | 12481.026 | 84512.000 |
| M_leanui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 10222.242 | 10222.242 | 10222.242–10222.242 | 11286.923 | 84512.000 |
| N_m1n1mal | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8474.380 | 8474.380 | 8474.380–8474.380 | 15009.416 | 84416.000 |
| N_m1n1mal | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8551.188 | 8551.188 | 8551.188–8551.188 | 9294.505 | 84448.000 |

## Data-derived comparisons

- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 23.637 ms vs 24.032 ms (1.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 20.148 ms vs 20.488 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 17.782 ms (9.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 17.149 ms vs 99.214 ms (82.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 13.053 ms vs 24.032 ms (45.7% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.123 ms vs 20.488 ms (21.3% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.173 ms (0.3% lower) (UX-level comparison: books/page differs, 10.000 vs 9.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 15.820 ms vs 17.149 ms (7.7% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 16.085 ms vs 24.032 ms (33.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.100 ms vs 20.488 ms (21.4% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.131 ms (0.0% lower) (UX-level comparison: books/page differs, 10.000 vs 5.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 16.007 ms vs 17.149 ms (6.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 16.087 ms vs 24.032 ms (33.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.102 ms vs 20.488 ms (21.4% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 16.081 ms vs 16.130 ms (0.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 16.212 ms vs 17.149 ms (5.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 20.129 ms vs 24.032 ms (16.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 20.488 ms vs 21.357 ms (4.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.181 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 17.149 ms vs 99.036 ms (82.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.053 ms vs 14.022 ms (6.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 16.123 ms vs 16.148 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 16.145 ms vs 16.173 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 15.820 ms vs 16.149 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 2000 books): 15.831 ms vs 16.085 ms (1.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 2000 books): 16.095 ms vs 16.100 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 16.103 ms vs 16.131 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 50 books): 15.907 ms vs 16.007 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 20.129 ms vs 21.423 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 19.729 ms vs 21.357 ms (7.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 16.119 ms vs 16.181 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 99.036 ms vs 111.184 ms (10.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 13.053 ms vs 13.886 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 16.098 ms vs 16.123 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 16.130 ms vs 16.173 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 15.820 ms vs 16.137 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 13.165 ms vs 13.886 ms (5.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 16.044 ms vs 16.098 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 13.431 ms vs 16.130 ms (16.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 12.768 ms vs 16.137 ms (20.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 2000 books): 16.073 ms vs 16.087 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 2000 books): 16.090 ms vs 16.102 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 50 books): 16.081 ms vs 16.110 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 50 books): 16.023 ms vs 16.212 ms (1.2% lower).

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
