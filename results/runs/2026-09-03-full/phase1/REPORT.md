# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `26bb78442d6bed9f4933bc3c30a6209507dc0fecb152335c3fd708bd660db8d4`
Reader flash setting: `unset`

Aggregated rows: 1656; PASS=1520; FAILED=0; UNSUPPORTED=136; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | paging | flat | 2000 | 10 | 201.000 | 3/3 | 90/90 | 15.748 | 25.862 | 12.349 | 30.775 | 18.927 | 30.922 | 13.130 | 37.527 |
| A_stock | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 14.492 | 16.160 | 12.225 | 26.713 | 18.959 | 27.548 | 13.646 | 32.096 |
| A_stock | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 21.143 | 66.380 | 14.052 | 67.274 | 21.633 | 71.138 | 12.989 | 73.127 |
| A_stock | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 79.741 | 99.506 | 54.692 | 102.349 | 35.222 | 82.470 | 11.009 | 122.522 |
| A_stock | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| A_stock | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | paging | flat | 2000 | 10 | 201.000 | 3/3 | 90/90 | 14.169 | 22.729 | 9.091 | 29.139 | 18.064 | 29.931 | 8.746 | 37.750 |
| B_bookshelf | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 14.067 | 16.563 | 12.048 | 28.806 | 18.593 | 26.241 | 14.080 | 31.875 |
| B_bookshelf | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 24.841 | 151.934 | 14.904 | 262.452 | 30.880 | 132.287 | 15.951 | 152.853 |
| B_bookshelf | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 98.952 | 134.645 | 78.691 | 149.656 | 25.665 | 55.655 | 13.900 | 77.530 |
| B_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | paging | flat | 2000 | 8 | 251.000 | 3/3 | 90/90 | 17.450 | 31.074 | 11.851 | 40.598 | 18.293 | 33.737 | 10.912 | 40.509 |
| C_simpleui | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 17.019 | 27.739 | 11.989 | 37.081 | 17.672 | 30.697 | 10.451 | 40.354 |
| C_simpleui | warm | flat | 2000 | 8 | 251.000 | 1/1 | 30/30 | 13.997 | 37.999 | 9.088 | 40.405 | 10.802 | 34.463 | 5.589 | 35.936 |
| C_simpleui | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 20.793 | 32.690 | 8.798 | 34.064 | 10.247 | 18.999 | 5.546 | 30.653 |
| C_simpleui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | paging | flat | 2000 | 5 | 400.000 | 3/3 | 90/90 | 8.273 | 12.070 | 6.307 | 27.543 | 8.122 | 22.043 | 5.685 | 25.565 |
| D_zenos | paging | hierarchical | 2000 | 5 | 33.000 | 3/3 | 90/90 | 8.236 | 9.212 | 6.134 | 23.662 | 8.310 | 18.998 | 5.698 | 22.218 |
| D_zenos | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 8.425 | 27.708 | 6.606 | 32.518 | 12.081 | 35.986 | 7.245 | 38.948 |
| D_zenos | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 8.594 | 13.863 | 7.798 | 30.190 | 13.039 | 28.133 | 7.835 | 49.795 |
| D_zenos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 8.765 | 10.182 | 7.597 | 14.939 | 8.431 | 10.042 | 6.751 | 15.114 |
| E_project_title | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 8.793 | 9.594 | 7.452 | 10.577 | 8.575 | 9.594 | 6.635 | 13.703 |
| E_project_title | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 8.732 | 10.281 | 7.383 | 13.481 | 8.625 | 9.913 | 7.676 | 14.964 |
| E_project_title | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 9.492 | 9.798 | 8.331 | 9.874 | 9.171 | 10.760 | 7.785 | 12.662 |
| E_project_title | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | paging | flat | 2000 | 10 | 200.000 | 3/3 | 90/90 | 15.482 | 25.365 | 12.112 | 29.172 | 19.199 | 30.894 | 14.340 | 34.976 |
| F_vos | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 14.857 | 16.930 | 10.597 | 29.131 | 19.184 | 27.519 | 13.798 | 32.252 |
| F_vos | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 23.340 | 56.846 | 18.660 | 59.218 | 24.280 | 55.026 | 12.787 | 61.663 |
| F_vos | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 61.764 | 93.253 | 52.864 | 105.294 | 23.727 | 42.468 | 14.896 | 78.895 |
| F_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | paging | flat | 2000 | 8 | 251.000 | 3/3 | 90/90 | 17.413 | 30.773 | 11.869 | 40.242 | 19.569 | 34.613 | 11.508 | 45.404 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 18.109 | 33.665 | 14.251 | 41.404 | 20.925 | 37.380 | 12.276 | 44.603 |
| G_simpleui_bookshelf | warm | flat | 2000 | 8 | 251.000 | 1/1 | 30/30 | 13.405 | 33.082 | 9.950 | 41.922 | 13.093 | 34.216 | 6.536 | 38.852 |
| G_simpleui_bookshelf | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 22.508 | 30.460 | 8.199 | 31.559 | 10.758 | 27.846 | 5.935 | 29.270 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | paging | flat | 2000 | 5 | 400.000 | 3/3 | 90/90 | 8.239 | 11.654 | 3.291 | 33.740 | 8.367 | 27.321 | 3.108 | 31.417 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | 5 | 33.000 | 3/3 | 90/90 | 8.256 | 9.365 | 6.800 | 25.897 | 8.235 | 18.500 | 5.408 | 22.742 |
| H_zenos_bookshelf | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 8.601 | 31.671 | 6.870 | 36.587 | 12.019 | 34.900 | 7.955 | 39.846 |
| H_zenos_bookshelf | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 8.686 | 13.562 | 8.390 | 26.444 | 13.066 | 24.293 | 8.094 | 27.123 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | paging | flat | 2000 | 10 | 200.000 | 3/3 | 90/90 | 15.534 | 26.573 | 12.818 | 30.772 | 20.031 | 33.084 | 15.596 | 38.973 |
| I_vos_bookshelf | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 14.688 | 17.551 | 11.952 | 29.514 | 19.121 | 27.174 | 14.364 | 31.624 |
| I_vos_bookshelf | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 23.459 | 86.567 | 15.244 | 153.074 | 21.819 | 76.879 | 11.645 | 80.173 |
| I_vos_bookshelf | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 56.775 | 105.648 | 18.575 | 124.257 | 24.822 | 66.816 | 13.958 | 69.248 |
| I_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | paging | flat | 2000 | 8 | 250.000 | 3/3 | 90/90 | 16.986 | 30.901 | 11.528 | 39.609 | 17.776 | 33.575 | 10.252 | 43.494 |
| J_simpleui_vos | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 13.753 | 19.452 | 7.733 | 27.835 | 13.423 | 26.376 | 6.052 | 34.571 |
| J_simpleui_vos | warm | flat | 2000 | 8 | 250.000 | 1/1 | 30/30 | 16.782 | 37.407 | 12.880 | 46.842 | 15.191 | 36.764 | 9.895 | 39.673 |
| J_simpleui_vos | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 16.183 | 28.651 | 11.792 | 36.405 | 12.636 | 26.980 | 9.387 | 35.608 |
| J_simpleui_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | 8 | 250.000 | 3/3 | 90/90 | 16.355 | 31.726 | 10.288 | 45.701 | 15.396 | 34.231 | 9.070 | 42.745 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 16.754 | 28.427 | 9.214 | 37.492 | 19.500 | 36.106 | 10.075 | 41.513 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | 8 | 250.000 | 1/1 | 30/30 | 13.506 | 34.418 | 8.670 | 46.332 | 12.374 | 33.468 | 7.571 | 37.825 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 17.574 | 28.781 | 12.360 | 37.883 | 14.142 | 25.040 | 10.036 | 31.083 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 9.325 | 10.771 | 7.580 | 14.883 | 8.915 | 10.697 | 7.103 | 15.167 |
| L_project_title_vos | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 9.167 | 10.449 | 8.005 | 11.335 | 9.056 | 10.493 | 7.746 | 16.451 |
| L_project_title_vos | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 7.992 | 8.412 | 6.869 | 8.686 | 8.004 | 8.327 | 6.811 | 9.272 |
| L_project_title_vos | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 9.903 | 10.485 | 8.506 | 10.630 | 9.270 | 10.716 | 7.839 | 12.092 |
| L_project_title_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| B_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 173.245 | 185.493 | 163.996 | 238.778 | 175.636 | 181.899 | 161.710 | 192.381 |
| B_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 27.179 | 32.906 | 10.551 | 47.336 | 8.975 | 10.720 | 7.075 | 18.548 |
| B_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 183.865 | 194.213 | 174.733 | 220.424 | 185.151 | 193.056 | 165.461 | 208.381 |
| B_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 28.736 | 36.771 | 9.823 | 43.163 | 8.788 | 10.459 | 7.073 | 15.448 |
| B_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 160.712 | 186.028 | 157.832 | 244.332 | 159.233 | 166.218 | 158.362 | 171.546 |
| B_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 23.172 | 29.851 | 9.168 | 42.099 | 8.081 | 8.787 | 6.980 | 12.707 |
| B_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 162.764 | 167.605 | 159.559 | 170.708 | 159.940 | 164.937 | 158.001 | 183.744 |
| B_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 15.021 | 21.394 | 9.283 | 24.820 | 7.758 | 8.632 | 7.100 | 12.999 |
| B_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 183.621 | 194.469 | 167.643 | 204.029 | 172.175 | 188.227 | 161.783 | 201.851 |
| G_simpleui_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 30.889 | 38.792 | 13.810 | 59.539 | 12.282 | 15.938 | 8.709 | 23.590 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 173.918 | 184.442 | 164.699 | 192.800 | 168.466 | 183.652 | 160.664 | 197.173 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 30.694 | 40.191 | 11.395 | 52.438 | 10.127 | 14.634 | 8.007 | 26.257 |
| G_simpleui_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 182.762 | 188.207 | 171.466 | 232.116 | 161.438 | 176.972 | 157.588 | 180.681 |
| G_simpleui_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 15.992 | 25.179 | 8.566 | 32.761 | 9.404 | 20.155 | 7.262 | 29.508 |
| G_simpleui_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 177.166 | 193.447 | 169.345 | 194.997 | 159.744 | 167.483 | 157.855 | 175.038 |
| G_simpleui_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 15.946 | 25.636 | 8.481 | 33.428 | 8.067 | 11.536 | 7.066 | 20.164 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 176.480 | 190.033 | 160.617 | 207.897 | 161.557 | 174.398 | 157.410 | 211.969 |
| H_zenos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 17.002 | 24.359 | 7.200 | 49.760 | 9.341 | 11.918 | 6.709 | 21.051 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 184.878 | 196.188 | 170.457 | 203.794 | 179.838 | 185.323 | 159.366 | 201.713 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 18.444 | 23.098 | 11.073 | 27.036 | 9.445 | 13.481 | 7.563 | 19.592 |
| H_zenos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 164.277 | 175.646 | 158.941 | 178.744 | 160.060 | 166.291 | 157.473 | 181.895 |
| H_zenos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 11.671 | 19.741 | 7.743 | 30.069 | 7.856 | 8.244 | 6.967 | 10.339 |
| H_zenos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 167.176 | 175.656 | 162.243 | 182.322 | 159.858 | 164.072 | 157.240 | 183.728 |
| H_zenos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 14.018 | 20.691 | 8.095 | 23.015 | 8.027 | 9.078 | 6.954 | 12.431 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 187.206 | 194.104 | 170.578 | 215.384 | 181.464 | 193.675 | 158.978 | 202.705 |
| I_vos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 30.074 | 39.480 | 11.522 | 52.157 | 9.760 | 11.872 | 7.771 | 16.908 |
| I_vos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 187.037 | 196.055 | 172.666 | 223.219 | 184.535 | 193.153 | 164.279 | 198.906 |
| I_vos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 27.319 | 36.362 | 8.802 | 42.513 | 8.738 | 10.994 | 6.827 | 17.115 |
| I_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 160.200 | 189.369 | 157.418 | 246.202 | 159.536 | 171.789 | 157.594 | 176.345 |
| I_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 20.557 | 27.800 | 9.420 | 39.994 | 7.896 | 8.879 | 6.738 | 12.689 |
| I_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 163.986 | 176.270 | 159.241 | 186.525 | 158.899 | 160.912 | 157.042 | 171.506 |
| I_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 18.552 | 20.877 | 8.242 | 21.140 | 7.888 | 8.838 | 6.856 | 12.223 |
| I_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 172.026 | 187.046 | 158.149 | 232.453 | 180.086 | 189.099 | 157.452 | 197.577 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 25.666 | 33.430 | 8.168 | 51.635 | 11.233 | 14.074 | 6.903 | 21.230 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 171.608 | 181.005 | 158.247 | 197.373 | 168.535 | 174.120 | 156.748 | 201.621 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 28.923 | 35.378 | 7.234 | 47.516 | 10.168 | 15.523 | 6.841 | 25.194 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 185.882 | 201.765 | 166.061 | 225.455 | 163.125 | 180.635 | 158.714 | 184.758 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 16.962 | 19.136 | 8.550 | 26.813 | 9.793 | 19.980 | 8.401 | 25.986 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 190.177 | 203.206 | 176.690 | 206.319 | 188.470 | 192.559 | 174.157 | 200.953 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 26.706 | 37.668 | 17.888 | 40.917 | 17.998 | 22.257 | 15.445 | 35.565 |
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

## Comparative Findings

- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 18.064 ms vs 18.927 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 14.169 ms vs 15.748 ms (10.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 18.593 ms vs 18.959 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.067 ms vs 14.492 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 21.633 ms vs 30.880 ms (29.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 21.143 ms vs 24.841 ms (14.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 25.665 ms vs 35.222 ms (27.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 79.741 ms vs 98.952 ms (19.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 18.293 ms vs 18.927 ms (3.3% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 15.748 ms vs 17.450 ms (9.8% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 17.672 ms vs 18.959 ms (6.8% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.492 ms vs 17.019 ms (14.9% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 10.802 ms vs 21.633 ms (50.1% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 13.997 ms vs 21.143 ms (33.8% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 10.247 ms vs 35.222 ms (70.9% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 20.793 ms vs 79.741 ms (73.9% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 8.122 ms vs 18.927 ms (57.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 8.273 ms vs 15.748 ms (47.5% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.310 ms vs 18.959 ms (56.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.236 ms vs 14.492 ms (43.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 12.081 ms vs 21.633 ms (44.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 8.425 ms vs 21.143 ms (60.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 13.039 ms vs 35.222 ms (63.0% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 8.594 ms vs 79.741 ms (89.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 8.431 ms vs 18.927 ms (55.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 8.765 ms vs 15.748 ms (44.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.575 ms vs 18.959 ms (54.8% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.793 ms vs 14.492 ms (39.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 8.625 ms vs 21.633 ms (60.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 8.732 ms vs 21.143 ms (58.7% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 9.171 ms vs 35.222 ms (74.0% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 9.492 ms vs 79.741 ms (88.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 18.927 ms vs 19.199 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 15.482 ms vs 15.748 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 18.959 ms vs 19.184 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.492 ms vs 14.857 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 2000 books): 21.633 ms vs 24.280 ms (10.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 21.143 ms vs 23.340 ms (9.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 23.727 ms vs 35.222 ms (32.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 61.764 ms vs 79.741 ms (22.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 18.293 ms vs 19.569 ms (6.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 17.413 ms vs 17.450 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 17.672 ms vs 20.925 ms (15.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 17.019 ms vs 18.109 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 10.802 ms vs 13.093 ms (17.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 13.405 ms vs 13.997 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 10.247 ms vs 10.758 ms (4.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 20.793 ms vs 22.508 ms (7.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 8.122 ms vs 8.367 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, flat, 2000 books): 8.239 ms vs 8.273 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.235 ms vs 8.310 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.236 ms vs 8.256 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 2000 books): 12.019 ms vs 12.081 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 8.425 ms vs 8.601 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 13.039 ms vs 13.066 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 8.594 ms vs 8.686 ms (1.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 19.199 ms vs 20.031 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 15.482 ms vs 15.534 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 19.121 ms vs 19.184 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.688 ms vs 14.857 ms (1.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 2000 books): 21.819 ms vs 24.280 ms (10.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 23.340 ms vs 23.459 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 23.727 ms vs 24.822 ms (4.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 56.775 ms vs 61.764 ms (8.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, flat, 2000 books): 17.776 ms vs 18.293 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 16.986 ms vs 17.450 ms (2.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, hierarchical, 2000 books): 13.423 ms vs 17.672 ms (24.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.753 ms vs 17.019 ms (19.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 10.802 ms vs 15.191 ms (28.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 13.997 ms vs 16.782 ms (16.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 10.247 ms vs 12.636 ms (18.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 16.183 ms vs 20.793 ms (22.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, flat, 2000 books): 15.396 ms vs 17.776 ms (13.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (paging, flat, 2000 books): 16.355 ms vs 16.986 ms (3.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 13.423 ms vs 19.500 ms (31.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.753 ms vs 16.754 ms (17.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 12.374 ms vs 15.191 ms (18.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 13.506 ms vs 16.782 ms (19.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 12.636 ms vs 14.142 ms (10.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 16.183 ms vs 17.574 ms (7.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (paging, flat, 2000 books): 8.431 ms vs 8.915 ms (5.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (paging, flat, 2000 books): 8.765 ms vs 9.325 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.575 ms vs 9.056 ms (5.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.793 ms vs 9.167 ms (4.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 2000 books): 8.004 ms vs 8.625 ms (7.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 2000 books): 7.992 ms vs 8.732 ms (8.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 50 books): 9.171 ms vs 9.270 ms (1.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 50 books): 9.492 ms vs 9.903 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.822 | 8.948 | 9.989 | 8.730–10.031 |
| A_stock | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 8.324 | 7.938 | 8.561 | 7.841–8.620 |
| A_stock | paging | flat | 2000 | library_cached_paging | PASS | 90 | 18.927 | 15.623 | 30.922 | 13.130–37.527 |
| A_stock | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 15.748 | 13.143 | 25.862 | 12.349–30.775 |
| A_stock | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 24.784 | 23.974 | 25.070 | 23.772–25.141 |
| A_stock | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 18.959 | 15.786 | 27.548 | 13.646–32.096 |
| A_stock | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 14.492 | 12.739 | 16.160 | 12.225–26.713 |
| A_stock | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 23.573 | 21.331 | 24.272 | 20.771–24.447 |
| A_stock | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.467 | 7.979 | 8.831 | 7.857–8.922 |
| A_stock | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 8.312 | 7.893 | 8.645 | 7.788–8.728 |
| A_stock | warm | flat | 2000 | change_sort_mode | PASS | 10 | 97.716 | 91.934 | 149.681 | 87.602–152.012 |
| A_stock | warm | flat | 2000 | close_book | PASS | 10 | 74.787 | 64.784 | 85.000 | 47.179–87.278 |
| A_stock | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.270 | 7.948 | 8.569 | 7.329–8.639 |
| A_stock | warm | flat | 2000 | home_to_library | PASS | 10 | 101.891 | 69.042 | 175.419 | 57.250–203.199 |
| A_stock | warm | flat | 2000 | library_cached_paging | PASS | 30 | 21.633 | 15.717 | 71.138 | 12.989–73.127 |
| A_stock | warm | flat | 2000 | library_first_render | PASS | 10 | 54.674 | 44.822 | 109.345 | 43.432–151.269 |
| A_stock | warm | flat | 2000 | library_folder_back | PASS | 10 | 115.537 | 82.684 | 122.060 | 81.079–125.296 |
| A_stock | warm | flat | 2000 | library_folder_enter | PASS | 10 | 5.358 | 4.727 | 8.765 | 4.700–8.936 |
| A_stock | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 21.143 | 18.456 | 66.380 | 14.052–67.274 |
| A_stock | warm | flat | 2000 | open_book | PASS | 10 | 55.993 | 53.843 | 60.233 | 53.683–61.241 |
| A_stock | warm | flat | 2000 | open_book_minimal | PASS | 10 | 104.868 | 102.550 | 109.101 | 102.157–111.084 |
| A_stock | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.288 | 7.421 | 12.585 | 7.296–40.091 |
| A_stock | warm | flat | 2000 | repeated_nav | PASS | 2 | 250.401 | 196.645 | 304.156 | 183.206–317.595 |
| A_stock | warm | flat | 50 | change_sort_mode | PASS | 10 | 48.691 | 31.211 | 69.682 | 30.610–75.715 |
| A_stock | warm | flat | 50 | close_book | PASS | 10 | 24.110 | 19.524 | 45.503 | 17.459–51.312 |
| A_stock | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.415 | 7.598 | 8.897 | 7.539–9.192 |
| A_stock | warm | flat | 50 | home_to_library | PASS | 10 | 23.332 | 21.291 | 25.919 | 18.628–35.680 |
| A_stock | warm | flat | 50 | library_cached_paging | PASS | 30 | 35.222 | 12.525 | 82.470 | 11.009–122.522 |
| A_stock | warm | flat | 50 | library_first_render | PASS | 10 | 25.397 | 22.407 | 45.700 | 20.871–55.131 |
| A_stock | warm | flat | 50 | library_folder_back | PASS | 10 | 40.451 | 28.071 | 42.223 | 27.901–44.704 |
| A_stock | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.914 | 5.854 | 13.844 | 4.934–18.027 |
| A_stock | warm | flat | 50 | library_sequential_paging | PASS | 5 | 79.741 | 62.122 | 99.506 | 54.692–102.349 |
| A_stock | warm | flat | 50 | open_book | PASS | 10 | 38.740 | 32.441 | 55.061 | 32.237–56.861 |
| A_stock | warm | flat | 50 | open_book_minimal | PASS | 10 | 41.890 | 36.342 | 51.087 | 30.257–54.906 |
| A_stock | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.645 | 7.865 | 10.724 | 2.847–24.713 |
| A_stock | warm | flat | 50 | repeated_nav | PASS | 2 | 197.780 | 162.150 | 233.411 | 153.242–242.319 |
| A_stock | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 7.988 | 6.281 | 21.202 | 6.125–23.664 |
| A_stock | warm | hierarchical | 2000 | close_book | PASS | 10 | 20.574 | 18.006 | 40.649 | 17.607–41.678 |
| A_stock | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.390 | 7.776 | 12.402 | 7.726–41.164 |
| A_stock | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 9.089 | 8.512 | 9.531 | 8.274–10.743 |
| A_stock | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 8.931 | 8.482 | 14.853 | 7.766–14.857 |
| A_stock | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 14.015 | 11.093 | 30.560 | 10.332–32.406 |
| A_stock | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.711 | 4.705 | 22.612 | 4.167–26.851 |
| A_stock | warm | hierarchical | 2000 | open_book | PASS | 10 | 44.577 | 40.962 | 59.739 | 39.545–59.800 |
| A_stock | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 64.785 | 58.915 | 67.662 | 48.618–68.366 |
| A_stock | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.430 | 8.002 | 8.953 | 7.862–9.136 |
| A_stock | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 7.890 | 7.016 | 17.118 | 6.906–17.609 |
| A_stock | warm | hierarchical | 50 | close_book | PASS | 10 | 18.802 | 14.578 | 31.545 | 14.393–36.883 |
| A_stock | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.572 | 7.798 | 9.230 | 7.737–9.326 |
| A_stock | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.782 | 8.059 | 9.314 | 7.751–9.442 |
| A_stock | warm | hierarchical | 50 | library_first_render | PASS | 10 | 8.430 | 8.001 | 14.421 | 7.807–15.301 |
| A_stock | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 15.215 | 10.971 | 23.683 | 10.894–25.496 |
| A_stock | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 10.747 | 8.084 | 22.633 | 5.276–30.605 |
| A_stock | warm | hierarchical | 50 | open_book | PASS | 10 | 45.252 | 30.072 | 49.685 | 28.813–50.154 |
| A_stock | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 41.280 | 36.753 | 49.609 | 34.400–72.978 |
| A_stock | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.139 | 6.953 | 8.904 | 2.979–9.416 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.692 | 9.646 | 9.995 | 9.634–10.071 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 9.430 | 9.146 | 9.988 | 9.075–10.127 |
| B_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 175.636 | 167.158 | 181.899 | 161.710–192.381 |
| B_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 8.975 | 7.615 | 10.720 | 7.075–18.548 |
| B_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 173.245 | 167.526 | 185.493 | 163.996–238.778 |
| B_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 27.179 | 14.485 | 32.906 | 10.551–47.336 |
| B_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 7.861 | 6.880 | 8.345 | 6.635–8.466 |
| B_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 18.064 | 9.773 | 29.931 | 8.746–37.750 |
| B_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 14.169 | 10.210 | 22.729 | 9.091–29.139 |
| B_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 147.363 | 143.395 | 150.712 | 142.403–151.549 |
| B_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 21.776 | 20.739 | 23.080 | 20.480–23.406 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 185.151 | 175.796 | 193.056 | 165.461–208.381 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 8.788 | 7.882 | 10.459 | 7.073–15.448 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 183.865 | 176.667 | 194.213 | 174.733–220.424 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 28.736 | 22.939 | 36.771 | 9.823–43.163 |
| B_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 8.084 | 7.950 | 8.374 | 7.917–8.447 |
| B_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 18.593 | 15.271 | 26.241 | 14.080–31.875 |
| B_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 14.067 | 13.009 | 16.563 | 12.048–28.806 |
| B_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 105.568 | 102.119 | 105.904 | 101.257–105.988 |
| B_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 19.477 | 17.015 | 21.414 | 16.400–21.898 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.547 | 7.974 | 8.552 | 7.831–8.553 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 7.804 | 7.782 | 8.775 | 7.776–9.018 |
| B_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 159.233 | 158.676 | 166.218 | 158.362–171.546 |
| B_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 8.081 | 7.239 | 8.787 | 6.980–12.707 |
| B_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 12.340 | 8.723 | 37.538 | 8.628–38.448 |
| B_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 160.712 | 158.379 | 186.028 | 157.832–244.332 |
| B_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 23.172 | 17.668 | 29.851 | 9.168–42.099 |
| B_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 97.298 | 92.730 | 154.431 | 90.181–158.656 |
| B_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 74.833 | 48.330 | 79.599 | 47.665–82.921 |
| B_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 7.732 | 7.236 | 8.490 | 6.617–8.511 |
| B_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.541 | 7.534 | 8.836 | 7.512–9.163 |
| B_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 93.692 | 69.355 | 116.336 | 51.846–181.402 |
| B_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 30.880 | 17.766 | 132.287 | 15.951–152.853 |
| B_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 82.469 | 65.297 | 160.724 | 57.321–188.377 |
| B_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 123.755 | 85.908 | 131.947 | 84.542–134.619 |
| B_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.653 | 4.620 | 13.723 | 4.555–55.206 |
| B_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 24.841 | 20.208 | 151.934 | 14.904–262.452 |
| B_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 60.908 | 58.413 | 65.251 | 57.510–65.996 |
| B_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 113.439 | 107.575 | 117.582 | 104.425–118.264 |
| B_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 11.337 | 9.832 | 14.726 | 9.684–19.452 |
| B_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.312 | 8.073 | 8.700 | 8.014–8.944 |
| B_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 254.832 | 234.247 | 275.416 | 229.101–280.562 |
| B_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 159.940 | 158.974 | 164.937 | 158.001–183.744 |
| B_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 7.758 | 7.288 | 8.632 | 7.100–12.999 |
| B_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 13.220 | 10.942 | 30.356 | 10.763–43.134 |
| B_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 162.764 | 160.029 | 167.605 | 159.559–170.708 |
| B_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 15.021 | 11.066 | 21.394 | 9.283–24.820 |
| B_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 39.458 | 28.619 | 65.952 | 24.380–70.172 |
| B_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 35.181 | 21.943 | 43.252 | 20.276–44.840 |
| B_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.587 | 7.716 | 8.879 | 6.987–8.901 |
| B_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.431 | 7.541 | 8.801 | 7.416–9.180 |
| B_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 23.548 | 22.531 | 43.121 | 22.083–44.011 |
| B_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 25.665 | 20.456 | 55.655 | 13.900–77.530 |
| B_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 30.336 | 24.046 | 68.614 | 22.978–80.585 |
| B_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 44.061 | 28.775 | 47.376 | 28.298–50.744 |
| B_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.046 | 5.449 | 26.557 | 5.137–28.461 |
| B_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 98.952 | 83.938 | 134.645 | 78.691–149.656 |
| B_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 42.031 | 36.075 | 56.169 | 35.446–57.776 |
| B_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 65.839 | 59.218 | 68.641 | 48.677–68.760 |
| B_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 12.660 | 10.003 | 18.129 | 9.795–40.768 |
| B_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.384 | 7.972 | 8.873 | 7.480–9.147 |
| B_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 292.146 | 238.767 | 345.524 | 225.422–358.869 |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 8.244 | 7.370 | 24.279 | 7.241–28.310 |
| B_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 8.282 | 7.404 | 20.308 | 7.096–22.116 |
| B_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 20.064 | 18.362 | 25.688 | 17.570–44.593 |
| B_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.728 | 8.256 | 9.200 | 8.250–9.239 |
| B_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.930 | 7.825 | 12.685 | 7.774–42.518 |
| B_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.789 | 7.919 | 9.365 | 7.828–9.451 |
| B_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 9.564 | 8.178 | 13.875 | 8.101–14.106 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 13.816 | 11.404 | 30.408 | 11.203–30.602 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.521 | 5.617 | 18.134 | 5.051–28.480 |
| B_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 61.947 | 40.154 | 67.314 | 38.797–69.185 |
| B_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 64.891 | 59.844 | 67.287 | 50.422–68.254 |
| B_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 9.026 | 7.953 | 16.623 | 7.737–41.973 |
| B_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.393 | 7.938 | 8.720 | 7.899–9.005 |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 11.985 | 9.706 | 22.223 | 8.871–23.696 |
| B_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.029 | 7.024 | 18.598 | 6.846–20.529 |
| B_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 17.762 | 14.217 | 26.075 | 13.037–27.495 |
| B_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 8.678 | 8.149 | 9.109 | 8.119–9.110 |
| B_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.485 | 7.977 | 9.201 | 7.924–9.340 |
| B_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.893 | 8.273 | 9.301 | 8.195–9.607 |
| B_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 9.171 | 8.326 | 15.128 | 8.182–15.738 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 12.279 | 10.656 | 26.930 | 10.131–27.402 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 10.944 | 8.020 | 20.640 | 4.504–22.000 |
| B_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 46.600 | 42.048 | 51.773 | 30.908–57.755 |
| B_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 42.285 | 33.330 | 49.827 | 31.684–56.929 |
| B_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 9.692 | 8.859 | 10.910 | 8.610–13.319 |
| B_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.338 | 7.904 | 14.254 | 7.396–58.802 |
| C_simpleui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.453 | 8.127 | 9.651 | 7.796–9.700 |
| C_simpleui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 24.806 | 24.321 | 26.493 | 24.200–26.915 |
| C_simpleui | paging | flat | 2000 | library_cached_paging | PASS | 90 | 18.293 | 12.252 | 33.737 | 10.912–40.509 |
| C_simpleui | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 17.450 | 14.675 | 31.074 | 11.851–40.598 |
| C_simpleui | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 12.245 | 12.039 | 12.289 | 11.987–12.300 |
| C_simpleui | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 17.672 | 12.105 | 30.697 | 10.451–40.354 |
| C_simpleui | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 17.019 | 14.602 | 27.739 | 11.989–37.081 |
| C_simpleui | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 14.013 | 12.673 | 31.718 | 12.338–36.144 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.078 | 8.998 | 9.674 | 8.978–9.823 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 24.593 | 21.094 | 24.633 | 20.219–24.643 |
| C_simpleui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 90.216 | 73.511 | 121.123 | 62.274–121.695 |
| C_simpleui | warm | flat | 2000 | close_book | PASS | 10 | 175.627 | 102.458 | 249.587 | 99.655–256.431 |
| C_simpleui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.534 | 7.935 | 9.037 | 7.640–9.097 |
| C_simpleui | warm | flat | 2000 | home_to_library | PASS | 10 | 8.278 | 7.701 | 8.514 | 7.245–9.043 |
| C_simpleui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 10.802 | 7.857 | 34.463 | 5.589–35.936 |
| C_simpleui | warm | flat | 2000 | library_first_render | PASS | 10 | 70.769 | 51.976 | 78.476 | 50.923–81.482 |
| C_simpleui | warm | flat | 2000 | library_folder_back | PASS | 10 | 76.924 | 66.908 | 97.535 | 66.821–108.153 |
| C_simpleui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.747 | 7.485 | 11.784 | 7.416–28.869 |
| C_simpleui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 13.997 | 10.803 | 37.999 | 9.088–40.405 |
| C_simpleui | warm | flat | 2000 | open_book | PASS | 10 | 121.451 | 107.295 | 133.746 | 98.631–142.448 |
| C_simpleui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 91.230 | 80.159 | 124.111 | 68.582–141.171 |
| C_simpleui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 10.123 | 9.156 | 44.891 | 9.126–331.903 |
| C_simpleui | warm | flat | 2000 | repeated_nav | PASS | 2 | 653.028 | 634.863 | 671.193 | 630.322–675.734 |
| C_simpleui | warm | flat | 2000 | start_to_home | PASS | 10 | 12.662 | 10.579 | 25.033 | 8.720–29.177 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 10 | 36.335 | 22.152 | 43.038 | 21.707–58.145 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 10 | 44.584 | 38.996 | 64.131 | 32.605–104.900 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.703 | 8.367 | 15.659 | 8.179–76.153 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 10 | 7.952 | 7.132 | 21.118 | 6.922–21.500 |
| C_simpleui | warm | flat | 50 | library_cached_paging | PASS | 30 | 10.247 | 7.493 | 18.999 | 5.546–30.653 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 10 | 24.137 | 19.453 | 33.228 | 18.924–41.655 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 10 | 22.311 | 10.712 | 24.555 | 10.464–27.846 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 10 | 23.008 | 8.768 | 31.575 | 8.362–32.462 |
| C_simpleui | warm | flat | 50 | library_sequential_paging | PASS | 6 | 20.793 | 9.291 | 32.690 | 8.798–34.064 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 10 | 116.376 | 100.218 | 130.586 | 98.770–131.374 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 10 | 54.771 | 46.542 | 90.917 | 45.103–98.830 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 10 | 12.495 | 10.774 | 14.042 | 10.585–16.187 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 2 | 279.793 | 127.475 | 432.111 | 89.395–470.190 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 10 | 8.628 | 7.784 | 17.060 | 6.418–22.270 |
| C_simpleui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 8.369 | 7.378 | 31.480 | 6.496–32.437 |
| C_simpleui | warm | hierarchical | 2000 | close_book | PASS | 10 | 40.370 | 36.221 | 111.277 | 34.419–126.100 |
| C_simpleui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.329 | 7.445 | 8.726 | 5.643–9.487 |
| C_simpleui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.033 | 5.293 | 10.440 | 5.289–22.023 |
| C_simpleui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 19.099 | 17.049 | 30.527 | 16.742–32.579 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 10.893 | 7.946 | 32.389 | 7.430–35.535 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 13.896 | 11.561 | 38.738 | 5.327–49.250 |
| C_simpleui | warm | hierarchical | 2000 | open_book | PASS | 10 | 126.767 | 120.041 | 144.698 | 118.491–145.695 |
| C_simpleui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 77.261 | 58.182 | 101.505 | 56.714–107.234 |
| C_simpleui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.573 | 7.952 | 10.797 | 7.459–12.777 |
| C_simpleui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 8.989 | 7.975 | 16.674 | 7.526–17.045 |
| C_simpleui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 10.071 | 8.515 | 26.357 | 8.478–26.818 |
| C_simpleui | warm | hierarchical | 50 | close_book | PASS | 10 | 41.474 | 38.525 | 44.494 | 36.176–49.253 |
| C_simpleui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.621 | 8.294 | 9.224 | 8.056–9.813 |
| C_simpleui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.863 | 7.961 | 9.506 | 7.956–9.874 |
| C_simpleui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 26.501 | 22.264 | 37.189 | 20.869–37.923 |
| C_simpleui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.261 | 11.042 | 34.912 | 10.940–59.608 |
| C_simpleui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.587 | 9.049 | 34.994 | 9.005–35.002 |
| C_simpleui | warm | hierarchical | 50 | open_book | PASS | 10 | 137.269 | 117.864 | 148.157 | 116.866–148.675 |
| C_simpleui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 67.231 | 60.589 | 101.466 | 51.710–110.430 |
| C_simpleui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 13.267 | 12.313 | 14.126 | 12.225–14.168 |
| C_simpleui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 9.171 | 8.935 | 17.477 | 8.614–20.560 |
| D_zenos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 31.225 | 30.938 | 35.796 | 30.866–36.939 |
| D_zenos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 25.777 | 25.457 | 27.456 | 25.377–27.876 |
| D_zenos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 8.122 | 7.248 | 22.043 | 5.685–25.565 |
| D_zenos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 8.273 | 7.426 | 12.070 | 6.307–27.543 |
| D_zenos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 19.922 | 19.594 | 20.084 | 19.512–20.125 |
| D_zenos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 8.310 | 7.263 | 18.998 | 5.698–22.218 |
| D_zenos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 90 | 8.236 | 7.163 | 9.212 | 6.134–23.662 |
| D_zenos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 16.276 | 16.042 | 18.246 | 15.983–18.738 |
| D_zenos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 31.885 | 31.387 | 32.161 | 31.262–32.230 |
| D_zenos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 24.298 | 24.107 | 26.128 | 24.059–26.585 |
| D_zenos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 99.624 | 69.165 | 110.173 | 67.981–113.546 |
| D_zenos | warm | flat | 2000 | close_book | PASS | 10 | 33.517 | 30.086 | 38.326 | 30.074–40.880 |
| D_zenos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.929 | 15.229 | 22.361 | 11.564–67.824 |
| D_zenos | warm | flat | 2000 | home_to_library | PASS | 10 | 63.408 | 61.096 | 85.030 | 59.234–91.045 |
| D_zenos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 12.081 | 7.841 | 35.986 | 7.245–38.948 |
| D_zenos | warm | flat | 2000 | library_first_render | PASS | 10 | 67.353 | 65.395 | 86.618 | 65.107–93.526 |
| D_zenos | warm | flat | 2000 | library_folder_back | PASS | 10 | 107.013 | 89.909 | 112.170 | 89.284–112.227 |
| D_zenos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.428 | 10.123 | 11.839 | 9.993–12.126 |
| D_zenos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 8.425 | 7.616 | 27.708 | 6.606–32.518 |
| D_zenos | warm | flat | 2000 | open_book | PASS | 10 | 125.860 | 118.707 | 136.487 | 117.725–141.636 |
| D_zenos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 99.225 | 71.257 | 110.786 | 68.624–114.271 |
| D_zenos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.362 | 7.879 | 15.251 | 7.740–71.436 |
| D_zenos | warm | flat | 2000 | repeated_nav | PASS | 2 | 227.522 | 112.671 | 342.372 | 83.958–371.085 |
| D_zenos | warm | flat | 2000 | start_to_home | PASS | 10 | 8.550 | 7.548 | 12.225 | 7.517–15.629 |
| D_zenos | warm | flat | 50 | change_sort_mode | PASS | 10 | 25.442 | 18.707 | 34.159 | 18.159–35.670 |
| D_zenos | warm | flat | 50 | close_book | PASS | 10 | 33.477 | 30.169 | 60.566 | 28.352–79.060 |
| D_zenos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.962 | 11.852 | 17.164 | 11.779–17.266 |
| D_zenos | warm | flat | 50 | home_to_library | PASS | 10 | 30.345 | 28.182 | 50.799 | 27.658–75.115 |
| D_zenos | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.039 | 8.300 | 28.133 | 7.835–49.795 |
| D_zenos | warm | flat | 50 | library_first_render | PASS | 10 | 37.680 | 34.253 | 48.086 | 32.818–54.055 |
| D_zenos | warm | flat | 50 | library_folder_back | PASS | 10 | 25.117 | 22.910 | 43.728 | 21.860–44.287 |
| D_zenos | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.991 | 10.922 | 26.739 | 10.426–27.932 |
| D_zenos | warm | flat | 50 | library_sequential_paging | PASS | 9 | 8.594 | 8.082 | 13.863 | 7.798–30.190 |
| D_zenos | warm | flat | 50 | open_book | PASS | 10 | 64.865 | 60.673 | 75.472 | 58.444–103.215 |
| D_zenos | warm | flat | 50 | open_book_minimal | PASS | 10 | 59.941 | 50.103 | 89.048 | 46.311–90.740 |
| D_zenos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.954 | 8.298 | 12.148 | 7.988–13.791 |
| D_zenos | warm | flat | 50 | repeated_nav | PASS | 2 | 178.485 | 174.745 | 182.225 | 173.810–183.160 |
| D_zenos | warm | flat | 50 | start_to_home | PASS | 10 | 8.936 | 8.395 | 10.977 | 8.284–11.572 |
| D_zenos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 15.900 | 12.521 | 34.823 | 11.628–34.927 |
| D_zenos | warm | hierarchical | 2000 | close_book | PASS | 10 | 32.544 | 31.484 | 35.947 | 30.583–36.019 |
| D_zenos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.930 | 15.730 | 21.832 | 11.661–63.277 |
| D_zenos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 23.698 | 22.775 | 25.255 | 22.706–25.263 |
| D_zenos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 25.999 | 24.546 | 34.528 | 24.469–36.418 |
| D_zenos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 23.034 | 14.834 | 32.675 | 14.596–32.949 |
| D_zenos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 32.059 | 9.191 | 37.948 | 8.821–38.616 |
| D_zenos | warm | hierarchical | 2000 | open_book | PASS | 10 | 64.928 | 53.860 | 112.881 | 53.433–112.985 |
| D_zenos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 57.885 | 48.435 | 73.925 | 47.381–77.484 |
| D_zenos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.502 | 7.639 | 9.657 | 7.167–9.980 |
| D_zenos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 9.529 | 8.565 | 11.417 | 7.687–11.464 |
| D_zenos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 20.739 | 12.816 | 29.968 | 12.433–30.948 |
| D_zenos | warm | hierarchical | 50 | close_book | PASS | 10 | 34.751 | 29.894 | 39.984 | 29.832–45.796 |
| D_zenos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 17.111 | 15.742 | 22.115 | 11.652–61.902 |
| D_zenos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 23.714 | 22.809 | 23.994 | 21.829–24.037 |
| D_zenos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 26.965 | 24.753 | 37.508 | 24.663–40.199 |
| D_zenos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 15.381 | 13.791 | 27.513 | 13.292–28.678 |
| D_zenos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.007 | 9.065 | 23.751 | 8.095–25.554 |
| D_zenos | warm | hierarchical | 50 | open_book | PASS | 10 | 61.666 | 57.459 | 69.493 | 56.009–85.068 |
| D_zenos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 52.511 | 46.940 | 63.997 | 46.172–83.310 |
| D_zenos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.395 | 7.781 | 10.284 | 7.526–11.458 |
| D_zenos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 9.421 | 8.278 | 10.008 | 8.277–10.130 |
| E_project_title | paging | flat | 2000 | library_cached_paging | PASS | 90 | 8.431 | 7.714 | 10.042 | 6.751–15.114 |
| E_project_title | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 8.765 | 8.221 | 10.182 | 7.597–14.939 |
| E_project_title | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 7.761 | 7.564 | 7.915 | 7.515–7.953 |
| E_project_title | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 8.575 | 7.832 | 9.594 | 6.635–13.703 |
| E_project_title | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 8.793 | 7.942 | 9.594 | 7.452–10.577 |
| E_project_title | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 9.126 | 8.900 | 9.849 | 8.843–10.030 |
| E_project_title | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.193 | 7.059 | 7.779 | 7.026–7.926 |
| E_project_title | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 8.083 | 7.819 | 8.442 | 7.753–8.532 |
| E_project_title | warm | flat | 2000 | change_sort_mode | PASS | 10 | 69.895 | 64.333 | 73.086 | 57.695–74.637 |
| E_project_title | warm | flat | 2000 | close_book | PASS | 10 | 41.445 | 38.551 | 42.697 | 38.198–43.588 |
| E_project_title | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.198 | 7.685 | 8.706 | 7.455–8.935 |
| E_project_title | warm | flat | 2000 | home_to_library | PASS | 10 | 39.779 | 36.384 | 45.554 | 36.305–46.447 |
| E_project_title | warm | flat | 2000 | library_cached_paging | PASS | 30 | 8.625 | 7.934 | 9.913 | 7.676–14.964 |
| E_project_title | warm | flat | 2000 | library_first_render | PASS | 10 | 40.623 | 38.195 | 47.124 | 36.525–48.299 |
| E_project_title | warm | flat | 2000 | library_folder_back | PASS | 10 | 69.428 | 66.056 | 76.547 | 65.000–78.325 |
| E_project_title | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.742 | 8.551 | 9.263 | 8.262–9.474 |
| E_project_title | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 8.732 | 7.869 | 10.281 | 7.383–13.481 |
| E_project_title | warm | flat | 2000 | open_book | PASS | 10 | 51.299 | 47.638 | 59.468 | 43.305–59.771 |
| E_project_title | warm | flat | 2000 | open_book_minimal | PASS | 10 | 48.230 | 45.845 | 49.783 | 45.195–51.367 |
| E_project_title | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.207 | 7.928 | 8.668 | 7.922–9.110 |
| E_project_title | warm | flat | 2000 | repeated_nav | PASS | 2 | 84.749 | 84.185 | 85.313 | 84.044–85.454 |
| E_project_title | warm | flat | 50 | change_sort_mode | PASS | 10 | 13.392 | 11.272 | 14.736 | 10.467–15.008 |
| E_project_title | warm | flat | 50 | close_book | PASS | 10 | 13.826 | 11.897 | 15.858 | 11.609–16.042 |
| E_project_title | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.186 | 7.784 | 9.022 | 7.738–9.135 |
| E_project_title | warm | flat | 50 | home_to_library | PASS | 10 | 13.927 | 11.763 | 15.670 | 11.525–16.024 |
| E_project_title | warm | flat | 50 | library_cached_paging | PASS | 30 | 9.171 | 8.076 | 10.760 | 7.785–12.662 |
| E_project_title | warm | flat | 50 | library_first_render | PASS | 10 | 12.058 | 11.252 | 13.658 | 10.636–16.453 |
| E_project_title | warm | flat | 50 | library_folder_back | PASS | 10 | 15.949 | 13.886 | 18.232 | 13.145–19.288 |
| E_project_title | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.128 | 8.530 | 9.690 | 8.466–13.149 |
| E_project_title | warm | flat | 50 | library_sequential_paging | PASS | 3 | 9.492 | 8.563 | 9.798 | 8.331–9.874 |
| E_project_title | warm | flat | 50 | open_book | PASS | 10 | 35.265 | 33.168 | 35.810 | 32.894–36.203 |
| E_project_title | warm | flat | 50 | open_book_minimal | PASS | 10 | 33.580 | 32.105 | 37.822 | 31.631–38.299 |
| E_project_title | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.001 | 7.851 | 9.196 | 7.639–9.201 |
| E_project_title | warm | flat | 50 | repeated_nav | PASS | 2 | 83.806 | 82.970 | 84.642 | 82.761–84.851 |
| E_project_title | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 7.790 | 7.222 | 8.355 | 7.136–8.563 |
| E_project_title | warm | hierarchical | 2000 | close_book | PASS | 10 | 13.355 | 11.200 | 17.870 | 11.106–19.082 |
| E_project_title | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.337 | 7.886 | 8.717 | 7.850–9.149 |
| E_project_title | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.008 | 7.145 | 8.908 | 6.970–9.008 |
| E_project_title | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 8.767 | 7.848 | 9.602 | 7.136–9.636 |
| E_project_title | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 9.488 | 8.800 | 11.974 | 8.667–11.999 |
| E_project_title | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 11.527 | 8.532 | 15.772 | 8.356–17.320 |
| E_project_title | warm | hierarchical | 2000 | open_book | PASS | 10 | 34.462 | 32.670 | 36.259 | 32.124–37.406 |
| E_project_title | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 34.934 | 33.380 | 39.233 | 32.324–39.801 |
| E_project_title | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.138 | 7.642 | 8.922 | 7.221–8.963 |
| E_project_title | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.043 | 7.166 | 8.371 | 7.059–8.440 |
| E_project_title | warm | hierarchical | 50 | close_book | PASS | 10 | 11.526 | 10.056 | 14.875 | 9.436–15.646 |
| E_project_title | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.277 | 7.947 | 9.004 | 7.945–9.120 |
| E_project_title | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.021 | 7.058 | 8.338 | 7.048–8.448 |
| E_project_title | warm | hierarchical | 50 | library_first_render | PASS | 10 | 8.012 | 7.413 | 8.553 | 7.331–8.954 |
| E_project_title | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 8.396 | 7.685 | 9.546 | 7.468–10.254 |
| E_project_title | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 9.031 | 8.601 | 9.227 | 8.590–9.500 |
| E_project_title | warm | hierarchical | 50 | open_book | PASS | 10 | 31.661 | 30.448 | 35.046 | 30.259–36.314 |
| E_project_title | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 31.960 | 29.880 | 33.598 | 29.587–33.883 |
| E_project_title | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.293 | 7.938 | 8.535 | 7.669–8.884 |
| F_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 19.199 | 16.146 | 30.894 | 14.340–34.976 |
| F_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 15.482 | 13.629 | 25.365 | 12.112–29.172 |
| F_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 25.706 | 24.341 | 26.102 | 24.000–26.201 |
| F_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 19.184 | 16.079 | 27.519 | 13.798–32.252 |
| F_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 14.857 | 13.508 | 16.930 | 10.597–29.131 |
| F_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 21.323 | 15.273 | 22.377 | 13.761–22.641 |
| F_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 18.359 | 17.813 | 19.420 | 17.677–19.685 |
| F_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 18.111 | 16.696 | 18.755 | 16.342–18.916 |
| F_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 103.287 | 96.255 | 145.666 | 82.808–149.223 |
| F_vos | warm | flat | 2000 | close_book | PASS | 10 | 60.843 | 59.380 | 85.676 | 56.523–88.655 |
| F_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.431 | 7.950 | 8.974 | 7.794–9.065 |
| F_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 71.346 | 61.553 | 163.972 | 58.957–164.149 |
| F_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 24.280 | 14.575 | 55.026 | 12.787–61.663 |
| F_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 61.620 | 59.559 | 119.445 | 58.654–141.384 |
| F_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 103.804 | 97.696 | 133.869 | 96.748–133.919 |
| F_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.614 | 7.807 | 9.254 | 5.301–9.270 |
| F_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 23.340 | 20.780 | 56.846 | 18.660–59.218 |
| F_vos | warm | flat | 2000 | open_book | PASS | 10 | 83.855 | 60.149 | 90.175 | 59.087–92.663 |
| F_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 84.460 | 80.726 | 90.379 | 79.970–92.709 |
| F_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.672 | 7.314 | 9.007 | 5.725–9.075 |
| F_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 190.452 | 186.111 | 194.794 | 185.026–195.879 |
| F_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 53.039 | 28.915 | 106.648 | 27.137–261.438 |
| F_vos | warm | flat | 50 | close_book | PASS | 10 | 31.700 | 26.810 | 37.014 | 26.590–37.454 |
| F_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.024 | 7.651 | 9.026 | 7.646–9.223 |
| F_vos | warm | flat | 50 | home_to_library | PASS | 10 | 30.546 | 28.456 | 42.575 | 27.807–49.275 |
| F_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 23.727 | 16.894 | 42.468 | 14.896–78.895 |
| F_vos | warm | flat | 50 | library_first_render | PASS | 10 | 46.677 | 31.942 | 65.933 | 31.758–90.900 |
| F_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 39.108 | 36.686 | 48.298 | 34.080–50.310 |
| F_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.252 | 4.437 | 21.488 | 4.092–23.681 |
| F_vos | warm | flat | 50 | library_sequential_paging | PASS | 4 | 61.764 | 54.517 | 93.253 | 52.864–105.294 |
| F_vos | warm | flat | 50 | open_book | PASS | 10 | 59.650 | 53.957 | 64.797 | 46.108–65.209 |
| F_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 61.228 | 45.701 | 65.431 | 36.070–66.835 |
| F_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.517 | 7.533 | 10.628 | 7.375–26.513 |
| F_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 180.182 | 167.934 | 192.429 | 164.872–195.491 |
| F_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.329 | 7.606 | 50.368 | 7.183–57.521 |
| F_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 30.889 | 29.049 | 35.552 | 28.487–42.952 |
| F_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.172 | 7.940 | 9.055 | 7.533–9.328 |
| F_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 17.587 | 16.894 | 18.517 | 16.880–21.000 |
| F_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 18.379 | 16.698 | 20.311 | 16.603–21.922 |
| F_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 23.172 | 20.553 | 31.858 | 18.794–50.088 |
| F_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 18.156 | 8.364 | 28.573 | 4.165–30.919 |
| F_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 65.745 | 62.477 | 68.890 | 61.470–71.140 |
| F_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 65.261 | 56.749 | 79.558 | 49.145–128.239 |
| F_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.687 | 7.897 | 10.958 | 7.792–23.938 |
| F_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 7.896 | 3.777 | 16.014 | 3.664–16.808 |
| F_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 33.270 | 23.381 | 46.730 | 22.872–48.176 |
| F_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.348 | 8.027 | 9.142 | 7.978–9.210 |
| F_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.104 | 15.084 | 17.452 | 14.058–20.081 |
| F_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.220 | 15.418 | 21.871 | 15.164–21.900 |
| F_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 18.054 | 16.050 | 21.159 | 14.255–25.268 |
| F_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 8.974 | 4.689 | 12.709 | 4.063–22.640 |
| F_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 36.485 | 31.560 | 42.480 | 30.667–46.276 |
| F_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 43.320 | 31.746 | 77.182 | 30.565–186.286 |
| F_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.465 | 8.248 | 10.324 | 8.187–21.793 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 172.175 | 165.341 | 188.227 | 161.783–201.851 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 12.282 | 10.496 | 15.938 | 8.709–23.590 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 183.621 | 171.607 | 194.469 | 167.643–204.029 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 30.889 | 25.880 | 38.792 | 13.810–59.539 |
| G_simpleui_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 17.594 | 16.814 | 20.671 | 16.619–21.440 |
| G_simpleui_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 19.569 | 13.358 | 34.613 | 11.508–45.404 |
| G_simpleui_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 17.413 | 15.078 | 30.773 | 11.869–40.242 |
| G_simpleui_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 135.126 | 119.599 | 142.888 | 115.717–144.828 |
| G_simpleui_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 12.373 | 12.072 | 16.603 | 11.997–17.660 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 168.466 | 165.923 | 183.652 | 160.664–197.173 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 10.127 | 8.607 | 14.634 | 8.007–26.257 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 173.918 | 169.575 | 184.442 | 164.699–192.800 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 30.694 | 24.274 | 40.191 | 11.395–52.438 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 10.180 | 9.530 | 11.830 | 9.368–12.243 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 20.925 | 16.871 | 37.380 | 12.276–44.603 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 18.109 | 15.883 | 33.665 | 14.251–41.404 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 97.134 | 95.391 | 101.869 | 94.955–103.053 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 15.471 | 15.465 | 16.546 | 15.463–16.815 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 10.468 | 10.355 | 11.655 | 10.327–11.952 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 23.910 | 21.917 | 24.643 | 21.419–24.826 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 161.438 | 158.549 | 176.972 | 157.588–180.681 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 9.404 | 8.579 | 20.155 | 7.262–29.508 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 9.921 | 9.407 | 89.903 | 8.747–96.502 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 182.762 | 178.150 | 188.207 | 171.466–232.116 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 15.992 | 14.625 | 25.179 | 8.566–32.761 |
| G_simpleui_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 88.955 | 66.672 | 111.949 | 62.770–117.787 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 110.454 | 101.391 | 233.195 | 101.234–243.621 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 16.661 | 16.255 | 108.939 | 15.836–109.980 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.171 | 8.017 | 8.639 | 7.762–9.149 |
| G_simpleui_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 14.367 | 8.359 | 17.261 | 8.339–24.792 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.093 | 8.204 | 34.216 | 6.536–38.852 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 66.977 | 48.588 | 77.287 | 48.346–80.425 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 92.893 | 69.526 | 100.837 | 67.483–101.597 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 7.853 | 6.931 | 10.832 | 6.615–23.018 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 13.405 | 11.764 | 33.082 | 9.950–41.922 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 126.432 | 112.739 | 143.983 | 95.284–176.395 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 88.265 | 76.890 | 118.448 | 64.995–135.267 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 13.412 | 11.417 | 20.516 | 11.049–25.601 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.678 | 8.331 | 11.081 | 8.062–11.496 |
| G_simpleui_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 501.994 | 227.074 | 776.913 | 158.344–845.643 |
| G_simpleui_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 13.672 | 9.063 | 27.178 | 8.691–27.581 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 159.744 | 158.169 | 167.483 | 157.855–175.038 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 8.067 | 7.510 | 11.536 | 7.066–20.164 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 10.013 | 9.336 | 50.369 | 9.110–53.395 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 177.166 | 171.038 | 193.447 | 169.345–194.997 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 15.946 | 10.949 | 25.636 | 8.481–33.428 |
| G_simpleui_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 31.029 | 20.862 | 53.645 | 20.522–56.395 |
| G_simpleui_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 46.599 | 40.601 | 104.179 | 40.175–107.051 |
| G_simpleui_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 17.115 | 16.427 | 57.248 | 16.354–58.016 |
| G_simpleui_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.153 | 7.732 | 8.921 | 4.875–9.044 |
| G_simpleui_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 8.020 | 6.587 | 8.897 | 6.306–9.012 |
| G_simpleui_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 10.758 | 8.376 | 27.846 | 5.935–29.270 |
| G_simpleui_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 28.264 | 20.566 | 39.912 | 20.507–46.958 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 18.771 | 10.621 | 28.594 | 10.558–33.523 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.358 | 12.373 | 34.584 | 9.408–35.158 |
| G_simpleui_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 6 | 22.508 | 11.226 | 30.460 | 8.199–31.559 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 119.147 | 65.729 | 128.020 | 65.460–128.718 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 50.465 | 46.121 | 64.758 | 46.003–93.207 |
| G_simpleui_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 15.431 | 12.664 | 20.606 | 11.426–21.124 |
| G_simpleui_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 12.545 | 9.538 | 41.551 | 9.121–80.760 |
| G_simpleui_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 246.119 | 117.900 | 374.338 | 85.845–406.393 |
| G_simpleui_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 11.180 | 8.553 | 16.603 | 5.930–21.247 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 17.197 | 15.761 | 60.206 | 14.249–67.495 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.782 | 8.429 | 27.685 | 8.103–29.468 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 47.243 | 44.883 | 124.098 | 44.263–127.987 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 19.732 | 18.513 | 61.742 | 17.338–62.531 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.274 | 7.693 | 8.878 | 7.407–9.168 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.719 | 8.175 | 10.660 | 7.449–21.205 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 29.215 | 21.721 | 37.211 | 21.425–41.460 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.607 | 11.957 | 34.643 | 10.677–35.271 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 31.356 | 19.441 | 40.426 | 17.657–46.337 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 135.255 | 130.015 | 146.471 | 116.438–149.212 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 104.159 | 69.657 | 113.793 | 65.155–122.366 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 18.904 | 17.422 | 19.694 | 17.183–19.813 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 14.071 | 13.145 | 25.860 | 12.802–92.811 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 8.755 | 8.475 | 15.891 | 8.344–17.064 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 17.896 | 16.660 | 59.579 | 15.778–64.264 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 10.822 | 10.179 | 39.788 | 10.031–54.430 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 41.670 | 37.287 | 52.965 | 36.701–111.179 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 19.212 | 18.258 | 59.621 | 15.586–61.869 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.730 | 7.885 | 16.718 | 7.466–81.736 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 9.062 | 8.447 | 9.700 | 8.326–10.417 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 28.423 | 22.058 | 38.872 | 21.920–40.696 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 11.776 | 9.247 | 16.200 | 8.753–37.271 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 22.117 | 9.607 | 37.419 | 9.030–41.815 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 130.575 | 123.785 | 136.679 | 122.736–152.937 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 99.291 | 66.922 | 129.335 | 65.052–180.424 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 19.164 | 18.132 | 21.545 | 17.457–22.470 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 12.881 | 11.519 | 21.788 | 11.511–91.869 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 8.878 | 8.352 | 17.074 | 8.324–19.118 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 161.557 | 158.803 | 174.398 | 157.410–211.969 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 9.341 | 7.393 | 11.918 | 6.709–21.051 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 176.480 | 162.965 | 190.033 | 160.617–207.897 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 17.002 | 8.802 | 24.359 | 7.200–49.760 |
| H_zenos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 10.834 | 9.774 | 11.816 | 9.509–12.061 |
| H_zenos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 8.367 | 7.125 | 27.321 | 3.108–31.417 |
| H_zenos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 8.239 | 7.259 | 11.654 | 3.291–33.740 |
| H_zenos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 159.455 | 147.609 | 197.122 | 144.647–206.539 |
| H_zenos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 27.666 | 26.959 | 42.760 | 26.782–46.534 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 179.838 | 164.638 | 185.323 | 159.366–201.713 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 9.445 | 8.192 | 13.481 | 7.563–19.592 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 184.878 | 172.488 | 196.188 | 170.457–203.794 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 18.444 | 13.482 | 23.098 | 11.073–27.036 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 12.924 | 11.843 | 13.715 | 11.573–13.913 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 8.235 | 7.003 | 18.500 | 5.408–22.742 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 90 | 8.256 | 7.305 | 9.365 | 6.800–25.897 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 106.128 | 101.328 | 110.462 | 100.128–111.546 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 20.715 | 15.864 | 21.530 | 14.651–21.734 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 32.553 | 31.812 | 34.211 | 31.627–34.625 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 26.108 | 24.765 | 27.341 | 24.429–27.649 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 160.060 | 158.349 | 166.291 | 157.473–181.895 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 7.856 | 7.092 | 8.244 | 6.967–10.339 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 13.129 | 11.540 | 52.671 | 10.933–57.958 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 164.277 | 160.242 | 175.646 | 158.941–178.744 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 11.671 | 8.462 | 19.741 | 7.743–30.069 |
| H_zenos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 99.643 | 68.674 | 108.768 | 66.323–111.832 |
| H_zenos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 32.350 | 30.287 | 35.986 | 30.040–37.256 |
| H_zenos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 8.518 | 7.295 | 10.646 | 7.153–11.461 |
| H_zenos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 17.013 | 16.081 | 17.277 | 11.514–17.497 |
| H_zenos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 65.015 | 63.319 | 85.318 | 62.814–87.134 |
| H_zenos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 12.019 | 8.582 | 34.900 | 7.955–39.846 |
| H_zenos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 70.466 | 65.199 | 89.576 | 63.213–92.162 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 106.448 | 88.105 | 111.456 | 84.720–114.231 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 11.452 | 10.325 | 13.078 | 9.429–13.354 |
| H_zenos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 8.601 | 7.378 | 31.671 | 6.870–36.587 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 129.230 | 124.857 | 141.735 | 122.966–142.517 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 108.446 | 94.067 | 114.802 | 91.654–118.005 |
| H_zenos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.152 | 12.776 | 19.338 | 12.139–19.588 |
| H_zenos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.864 | 8.544 | 11.784 | 7.909–13.716 |
| H_zenos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 242.958 | 115.367 | 370.549 | 83.469–402.447 |
| H_zenos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 8.448 | 6.363 | 17.522 | 6.018–51.748 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 159.858 | 158.863 | 164.072 | 157.240–183.728 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 8.027 | 7.412 | 9.078 | 6.954–12.431 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 13.401 | 10.470 | 48.003 | 9.853–57.719 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 167.176 | 163.617 | 175.656 | 162.243–182.322 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 14.018 | 8.309 | 20.691 | 8.095–23.015 |
| H_zenos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 19.670 | 16.813 | 32.957 | 15.950–38.930 |
| H_zenos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 34.612 | 30.256 | 39.636 | 29.935–44.246 |
| H_zenos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.230 | 7.599 | 9.616 | 7.031–16.141 |
| H_zenos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 17.510 | 17.201 | 21.122 | 16.219–51.468 |
| H_zenos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 29.823 | 28.272 | 35.815 | 27.680–36.561 |
| H_zenos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.066 | 8.431 | 24.293 | 8.094–27.123 |
| H_zenos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 40.788 | 35.439 | 46.310 | 32.613–46.395 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 41.493 | 24.759 | 43.373 | 23.816–44.291 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 10.677 | 10.242 | 25.448 | 9.670–26.474 |
| H_zenos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 9 | 8.686 | 8.414 | 13.562 | 8.390–26.444 |
| H_zenos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 102.047 | 64.812 | 109.668 | 55.829–113.040 |
| H_zenos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 54.675 | 48.501 | 72.302 | 46.840–85.074 |
| H_zenos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 11.242 | 9.233 | 15.417 | 9.103–24.110 |
| H_zenos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.576 | 7.885 | 10.656 | 7.763–12.146 |
| H_zenos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 176.586 | 129.703 | 223.469 | 117.982–235.190 |
| H_zenos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 9.616 | 8.824 | 10.442 | 8.677–11.328 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 9.794 | 8.556 | 37.476 | 8.515–44.257 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 21.072 | 13.230 | 33.380 | 12.974–38.742 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 33.779 | 29.769 | 59.438 | 28.724–86.634 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.806 | 8.465 | 9.362 | 8.364–11.036 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 17.296 | 16.324 | 22.563 | 16.120–67.892 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 23.623 | 21.059 | 24.935 | 20.813–24.947 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 25.531 | 24.493 | 34.755 | 23.210–38.399 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.923 | 14.407 | 27.647 | 14.332–30.865 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 30.306 | 9.705 | 37.561 | 8.718–41.458 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 67.446 | 54.658 | 117.199 | 51.890–118.802 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 53.109 | 50.308 | 61.064 | 47.865–72.787 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 10.365 | 8.159 | 13.548 | 7.950–15.326 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.475 | 7.784 | 20.307 | 7.574–73.160 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 9.039 | 8.743 | 10.138 | 8.737–11.164 |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 10.620 | 9.337 | 40.988 | 8.556–51.909 |
| H_zenos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 20.752 | 13.330 | 31.288 | 13.226–31.563 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 34.009 | 30.899 | 40.270 | 28.433–40.779 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 9.053 | 8.286 | 9.459 | 8.183–12.047 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.633 | 15.576 | 17.141 | 11.666–17.300 |
| H_zenos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 23.335 | 22.477 | 24.457 | 21.829–25.321 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 26.294 | 25.276 | 36.464 | 24.604–40.165 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 27.335 | 14.656 | 30.682 | 13.424–31.971 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.864 | 8.485 | 22.958 | 7.622–25.116 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 63.118 | 58.591 | 111.392 | 56.783–111.689 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 54.008 | 48.732 | 73.177 | 41.026–74.783 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 9.671 | 8.120 | 13.031 | 7.926–18.062 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.338 | 7.926 | 19.694 | 7.867–70.123 |
| H_zenos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 9.099 | 8.436 | 9.973 | 7.876–10.833 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 181.464 | 162.456 | 193.675 | 158.978–202.705 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 9.760 | 8.713 | 11.872 | 7.771–16.908 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 187.206 | 176.152 | 194.104 | 170.578–215.384 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 30.074 | 26.094 | 39.480 | 11.522–52.157 |
| I_vos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 9.075 | 8.834 | 10.222 | 8.774–10.509 |
| I_vos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 20.031 | 16.999 | 33.084 | 15.596–38.973 |
| I_vos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 15.534 | 13.835 | 26.573 | 12.818–30.772 |
| I_vos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 147.040 | 139.854 | 154.482 | 138.057–156.342 |
| I_vos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 26.964 | 26.659 | 27.471 | 26.583–27.598 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 184.535 | 168.123 | 193.153 | 164.279–198.906 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 8.738 | 8.038 | 10.994 | 6.827–17.115 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 187.037 | 178.552 | 196.055 | 172.666–223.219 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 27.319 | 23.459 | 36.362 | 8.802–42.513 |
| I_vos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 8.388 | 8.366 | 9.112 | 8.361–9.293 |
| I_vos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 19.121 | 16.457 | 27.174 | 14.364–31.624 |
| I_vos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 14.688 | 13.014 | 17.551 | 11.952–29.514 |
| I_vos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 92.427 | 91.539 | 98.541 | 91.317–100.069 |
| I_vos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 22.453 | 15.809 | 26.588 | 14.148–27.622 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 17.936 | 17.912 | 18.522 | 17.906–18.669 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 18.047 | 16.943 | 18.451 | 16.667–18.552 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 159.536 | 158.485 | 171.789 | 157.594–176.345 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 7.896 | 7.047 | 8.879 | 6.738–12.689 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 12.351 | 9.446 | 34.633 | 9.061–47.230 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 160.200 | 158.235 | 189.369 | 157.418–246.202 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 20.557 | 17.205 | 27.800 | 9.420–39.994 |
| I_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 111.418 | 100.653 | 153.808 | 96.392–156.677 |
| I_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 61.157 | 58.012 | 67.603 | 56.046–69.251 |
| I_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 8.329 | 7.290 | 8.471 | 6.913–8.612 |
| I_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.392 | 7.776 | 9.132 | 7.634–9.307 |
| I_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 79.738 | 64.164 | 163.563 | 61.715–172.109 |
| I_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 21.819 | 14.240 | 76.879 | 11.645–80.173 |
| I_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 77.096 | 73.578 | 175.393 | 63.366–204.731 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 103.481 | 97.834 | 134.264 | 96.062–140.631 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.596 | 8.007 | 9.200 | 7.752–9.295 |
| I_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 23.459 | 18.044 | 86.567 | 15.244–153.074 |
| I_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 89.424 | 87.115 | 95.022 | 85.113–95.289 |
| I_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 90.639 | 86.375 | 95.175 | 85.801–97.094 |
| I_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 11.514 | 8.968 | 14.552 | 8.718–15.509 |
| I_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.301 | 7.734 | 8.757 | 7.204–8.865 |
| I_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 224.553 | 194.814 | 254.293 | 187.379–261.728 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 158.899 | 157.818 | 160.912 | 157.042–171.506 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 7.888 | 7.020 | 8.838 | 6.856–12.223 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 11.851 | 10.720 | 30.535 | 10.371–35.701 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 163.986 | 160.935 | 176.270 | 159.241–186.525 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 18.552 | 10.101 | 20.877 | 8.242–21.140 |
| I_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 44.550 | 27.637 | 63.701 | 27.005–70.609 |
| I_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 31.002 | 28.225 | 37.210 | 28.073–38.129 |
| I_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.589 | 7.933 | 9.023 | 7.928–9.070 |
| I_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.332 | 7.664 | 8.702 | 7.417–9.146 |
| I_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 32.605 | 31.023 | 57.483 | 30.797–68.843 |
| I_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 24.822 | 21.150 | 66.816 | 13.958–69.248 |
| I_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 45.099 | 32.918 | 95.651 | 27.790–107.465 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 49.690 | 37.767 | 66.227 | 34.879–66.636 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.333 | 7.548 | 19.452 | 5.458–45.009 |
| I_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 4 | 56.775 | 28.400 | 105.648 | 18.575–124.257 |
| I_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 60.621 | 57.686 | 66.595 | 53.258–68.296 |
| I_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 59.584 | 45.555 | 65.037 | 33.744–66.806 |
| I_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 13.100 | 11.967 | 14.576 | 11.561–21.750 |
| I_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.287 | 7.487 | 8.702 | 7.260–8.753 |
| I_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 214.750 | 175.769 | 253.731 | 166.024–263.476 |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 10.738 | 8.884 | 23.849 | 8.600–31.567 |
| I_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 42.452 | 7.458 | 68.322 | 6.958–82.212 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 30.059 | 27.171 | 33.547 | 26.888–37.074 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.312 | 7.970 | 8.894 | 7.624–9.215 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.220 | 8.015 | 8.559 | 7.765–8.678 |
| I_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 17.403 | 16.804 | 19.843 | 16.490–21.166 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 18.077 | 17.219 | 22.920 | 16.898–24.547 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 24.214 | 19.153 | 34.321 | 19.094–42.244 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.596 | 7.616 | 20.165 | 4.054–30.044 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 65.073 | 42.686 | 71.690 | 42.595–72.380 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 59.731 | 46.687 | 69.690 | 44.199–70.066 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 10.582 | 9.549 | 12.478 | 9.218–13.474 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.107 | 7.338 | 8.736 | 7.303–9.105 |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 16.950 | 14.763 | 27.399 | 14.506–30.626 |
| I_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 7.763 | 6.261 | 17.163 | 5.170–17.767 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 33.189 | 30.064 | 44.329 | 29.944–49.954 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 8.539 | 8.170 | 8.805 | 8.108–9.015 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.956 | 8.630 | 9.161 | 7.338–9.466 |
| I_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 17.438 | 16.512 | 19.948 | 16.299–20.744 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 17.752 | 17.038 | 23.617 | 16.256–23.775 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 21.593 | 19.091 | 25.206 | 18.447–28.028 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 10.591 | 7.749 | 13.936 | 4.720–22.507 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 39.865 | 37.344 | 42.547 | 35.540–54.616 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 41.059 | 38.301 | 44.992 | 37.239–53.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 15.961 | 15.236 | 18.470 | 15.086–28.162 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.643 | 8.223 | 10.634 | 8.175–12.339 |
| J_simpleui_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 17.776 | 11.701 | 33.575 | 10.252–43.494 |
| J_simpleui_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 16.986 | 14.854 | 30.901 | 11.528–39.609 |
| J_simpleui_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 28.207 | 26.252 | 29.877 | 25.763–30.295 |
| J_simpleui_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 13.423 | 10.199 | 26.376 | 6.052–34.571 |
| J_simpleui_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 13.753 | 10.657 | 19.452 | 7.733–27.835 |
| J_simpleui_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 13.263 | 10.437 | 21.405 | 9.731–23.440 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.136 | 8.879 | 9.247 | 8.815–9.275 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 23.495 | 22.697 | 23.891 | 22.497–23.990 |
| J_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 112.582 | 94.047 | 140.700 | 84.905–141.676 |
| J_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 252.469 | 240.096 | 263.107 | 239.002–266.211 |
| J_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 9.316 | 8.606 | 9.775 | 8.465–10.101 |
| J_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 13.006 | 10.990 | 15.220 | 10.630–23.650 |
| J_simpleui_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.191 | 11.366 | 36.764 | 9.895–39.673 |
| J_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 61.226 | 60.476 | 79.754 | 57.606–83.826 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 99.453 | 80.107 | 113.417 | 76.366–116.727 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 12.078 | 10.706 | 26.910 | 10.246–27.188 |
| J_simpleui_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.782 | 14.902 | 37.407 | 12.880–46.842 |
| J_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 118.257 | 98.177 | 134.984 | 95.796–152.061 |
| J_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 82.144 | 60.058 | 114.045 | 54.743–120.574 |
| J_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 30.633 | 28.394 | 31.977 | 23.810–32.987 |
| J_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 621.218 | 620.797 | 621.639 | 620.692–621.744 |
| J_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 13.771 | 8.376 | 22.059 | 8.292–23.201 |
| J_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 40.289 | 24.784 | 46.522 | 24.087–52.049 |
| J_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 54.733 | 44.428 | 68.797 | 43.910–142.080 |
| J_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 10.041 | 9.783 | 11.467 | 9.312–11.495 |
| J_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 14.322 | 12.843 | 15.914 | 12.362–24.468 |
| J_simpleui_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 12.636 | 10.014 | 26.980 | 9.387–35.608 |
| J_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 34.011 | 32.032 | 47.774 | 31.484–50.583 |
| J_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 36.709 | 20.418 | 39.325 | 18.128–40.193 |
| J_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.524 | 10.931 | 14.169 | 9.664–29.700 |
| J_simpleui_vos | warm | flat | 50 | library_sequential_paging | PASS | 6 | 16.183 | 12.893 | 28.651 | 11.792–36.405 |
| J_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 125.555 | 111.712 | 141.866 | 108.779–142.551 |
| J_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 83.215 | 60.912 | 94.687 | 60.048–103.181 |
| J_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 28.766 | 26.452 | 103.494 | 24.764–111.410 |
| J_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 294.871 | 228.673 | 361.069 | 212.124–377.618 |
| J_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 9.276 | 8.537 | 22.429 | 7.997–29.249 |
| J_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.494 | 8.620 | 23.638 | 8.601–24.960 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 38.380 | 37.834 | 41.813 | 37.491–47.468 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.306 | 4.805 | 8.614 | 4.142–9.433 |
| J_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.636 | 7.413 | 16.514 | 6.605–17.985 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 21.403 | 20.223 | 31.734 | 20.174–33.236 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 17.659 | 11.229 | 30.002 | 8.902–31.345 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 19.385 | 8.878 | 36.984 | 8.657–37.111 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 64.368 | 56.269 | 139.465 | 56.244–148.913 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 50.987 | 48.408 | 55.641 | 47.874–60.730 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.938 | 8.305 | 10.622 | 8.141–10.776 |
| J_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 9.280 | 8.346 | 15.219 | 7.945–15.921 |
| J_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.273 | 6.635 | 20.285 | 4.300–21.394 |
| J_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 32.796 | 30.342 | 38.022 | 28.451–39.682 |
| J_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.291 | 4.178 | 8.668 | 4.072–9.183 |
| J_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.556 | 7.206 | 13.327 | 5.613–17.907 |
| J_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.383 | 15.904 | 22.715 | 15.389–31.100 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 9.979 | 7.675 | 21.933 | 4.587–24.293 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 9.004 | 7.502 | 32.160 | 5.240–41.570 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 61.830 | 57.953 | 109.087 | 54.150–111.311 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 48.438 | 41.346 | 61.546 | 33.235–62.159 |
| J_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 7.968 | 7.075 | 9.014 | 6.851–11.818 |
| J_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 9.002 | 8.520 | 15.284 | 8.515–15.807 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 180.086 | 159.111 | 189.099 | 157.452–197.577 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 11.233 | 7.691 | 14.074 | 6.903–21.230 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 172.026 | 159.396 | 187.046 | 158.149–232.453 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 25.666 | 14.630 | 33.430 | 8.168–51.635 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 19.421 | 18.713 | 19.915 | 18.536–20.039 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 15.396 | 11.682 | 34.231 | 9.070–42.745 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 16.355 | 13.228 | 31.726 | 10.288–45.701 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 148.829 | 147.016 | 154.668 | 146.563–156.128 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 12.460 | 8.058 | 26.089 | 6.957–29.496 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 168.535 | 158.833 | 174.120 | 156.748–201.621 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 10.168 | 7.718 | 15.523 | 6.841–25.194 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 171.608 | 159.796 | 181.005 | 158.247–197.373 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 28.923 | 7.853 | 35.378 | 7.234–47.516 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 12.895 | 11.224 | 14.279 | 10.806–14.625 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 19.500 | 13.650 | 36.106 | 10.075–41.513 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 16.754 | 12.466 | 28.427 | 9.214–37.492 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 100.219 | 68.334 | 104.445 | 60.363–105.501 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 16.680 | 14.691 | 22.528 | 14.194–23.990 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.779 | 9.182 | 10.845 | 9.033–11.112 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 23.978 | 23.326 | 24.126 | 23.163–24.163 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 163.125 | 159.373 | 180.635 | 158.714–184.758 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 9.793 | 8.745 | 19.980 | 8.401–25.986 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 12.859 | 9.093 | 107.460 | 8.369–131.234 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 185.882 | 179.870 | 201.765 | 166.061–225.455 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.962 | 15.344 | 19.136 | 8.550–26.813 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 89.805 | 66.195 | 131.112 | 64.722–138.988 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 259.943 | 237.890 | 274.179 | 103.204–284.766 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 18.055 | 15.961 | 122.932 | 15.818–128.976 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.431 | 7.763 | 8.969 | 7.421–9.401 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 9.717 | 7.795 | 14.725 | 7.745–15.438 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 12.374 | 10.077 | 33.468 | 7.571–37.825 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 59.192 | 52.820 | 78.538 | 51.955–89.237 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 85.834 | 67.847 | 94.079 | 66.413–95.264 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 6.179 | 5.929 | 10.425 | 5.896–23.205 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 13.506 | 11.766 | 34.418 | 8.670–46.332 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 135.835 | 109.749 | 149.271 | 104.784–162.896 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 94.650 | 59.761 | 125.525 | 53.262–128.059 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 14.328 | 13.081 | 18.040 | 13.011–18.167 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 28.987 | 21.886 | 90.105 | 18.889–509.459 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 353.197 | 241.935 | 464.458 | 214.120–492.273 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 15.378 | 13.929 | 27.001 | 8.585–34.425 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 188.470 | 183.143 | 192.559 | 174.157–200.953 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 17.998 | 15.893 | 22.257 | 15.445–35.565 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 17.351 | 16.175 | 48.819 | 16.042–54.346 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 190.177 | 181.415 | 203.206 | 176.690–206.319 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 26.706 | 19.561 | 37.668 | 17.888–40.917 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 38.550 | 22.014 | 49.740 | 21.283–49.924 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 44.504 | 39.973 | 51.263 | 37.854–85.552 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 20.362 | 19.735 | 58.733 | 19.481–59.623 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 9.441 | 8.359 | 10.289 | 8.136–10.547 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 13.603 | 11.969 | 16.152 | 11.334–28.872 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 14.142 | 10.620 | 25.040 | 10.036–31.083 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 33.605 | 31.535 | 43.846 | 30.990–45.165 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 26.308 | 17.192 | 30.246 | 17.067–30.488 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.069 | 10.170 | 25.308 | 10.005–26.830 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 6 | 17.574 | 13.188 | 28.781 | 12.360–37.883 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 85.381 | 58.624 | 105.428 | 55.793–107.337 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 57.181 | 47.103 | 79.442 | 40.653–81.687 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 18.639 | 17.508 | 24.081 | 17.165–25.760 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 28.053 | 22.393 | 81.673 | 19.939–91.416 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 288.044 | 196.161 | 379.927 | 173.190–402.898 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 9.323 | 8.660 | 22.870 | 8.614–25.840 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.905 | 15.351 | 61.560 | 14.124–62.100 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 10.317 | 9.278 | 31.299 | 8.204–32.900 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 50.596 | 42.780 | 131.228 | 40.928–134.192 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 23.165 | 20.566 | 68.850 | 20.396–69.395 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.799 | 8.527 | 9.422 | 8.364–9.943 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.378 | 7.482 | 10.599 | 7.294–21.170 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 23.184 | 21.956 | 34.975 | 21.310–36.654 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.404 | 12.184 | 37.346 | 11.287–38.346 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 18.480 | 9.925 | 44.326 | 8.222–44.950 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 137.610 | 90.259 | 157.154 | 86.327–157.211 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 109.037 | 83.784 | 127.017 | 78.062–127.256 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 18.569 | 17.000 | 21.145 | 16.842–23.982 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 14.085 | 12.563 | 14.899 | 11.883–16.879 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 9.223 | 8.436 | 16.448 | 8.377–19.153 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 17.236 | 16.282 | 59.602 | 15.461–65.967 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 11.030 | 9.131 | 28.784 | 7.952–28.822 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 45.882 | 40.430 | 105.652 | 38.427–106.253 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 22.366 | 20.380 | 62.855 | 17.626–64.262 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.977 | 8.415 | 17.012 | 8.229–17.533 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.028 | 7.349 | 8.833 | 7.249–9.133 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 22.852 | 21.852 | 36.125 | 21.795–37.345 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 20.264 | 10.550 | 26.535 | 8.623–30.673 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.337 | 9.030 | 36.760 | 8.302–46.311 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 128.064 | 114.613 | 138.548 | 114.497–139.939 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 79.339 | 60.533 | 110.163 | 53.113–118.466 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 19.572 | 18.316 | 21.490 | 17.510–22.058 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 15.088 | 13.391 | 31.368 | 12.554–98.064 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 8.940 | 8.533 | 15.495 | 8.509–16.151 |
| K_vos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 18.860 | 18.850 | 19.094 | 18.847–19.152 |
| K_vos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 17.889 | 17.709 | 18.233 | 17.664–18.319 |
| L_project_title_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 8.915 | 7.985 | 10.697 | 7.103–15.167 |
| L_project_title_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 9.325 | 8.191 | 10.771 | 7.580–14.883 |
| L_project_title_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 8.684 | 8.246 | 8.875 | 8.137–8.923 |
| L_project_title_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 9.056 | 8.099 | 10.493 | 7.746–16.451 |
| L_project_title_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 9.167 | 8.219 | 10.449 | 8.005–11.335 |
| L_project_title_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 9.196 | 8.782 | 10.438 | 8.678–10.748 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 18.186 | 17.300 | 18.291 | 17.079–18.317 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.211 | 15.945 | 17.012 | 15.878–17.212 |
| L_project_title_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 75.347 | 71.709 | 83.803 | 70.573–90.011 |
| L_project_title_vos | warm | flat | 2000 | close_book | PASS | 10 | 54.983 | 52.473 | 57.771 | 51.713–57.787 |
| L_project_title_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.056 | 7.616 | 8.691 | 7.613–8.962 |
| L_project_title_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 46.879 | 44.655 | 55.555 | 43.463–56.601 |
| L_project_title_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 8.004 | 6.918 | 8.327 | 6.811–9.272 |
| L_project_title_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 47.495 | 45.050 | 54.805 | 44.278–56.031 |
| L_project_title_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 86.127 | 81.395 | 91.404 | 81.330–91.915 |
| L_project_title_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.824 | 8.264 | 9.044 | 8.162–9.143 |
| L_project_title_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 7.992 | 7.089 | 8.412 | 6.869–8.686 |
| L_project_title_vos | warm | flat | 2000 | open_book | PASS | 10 | 53.797 | 51.744 | 55.607 | 51.682–57.176 |
| L_project_title_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 52.668 | 50.061 | 53.982 | 48.971–55.729 |
| L_project_title_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.462 | 7.466 | 8.692 | 7.237–8.819 |
| L_project_title_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 83.620 | 83.414 | 83.827 | 83.362–83.879 |
| L_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 13.121 | 10.989 | 14.484 | 10.913–16.965 |
| L_project_title_vos | warm | flat | 50 | close_book | PASS | 10 | 25.270 | 23.407 | 28.631 | 23.359–30.821 |
| L_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.245 | 7.467 | 8.417 | 7.393–8.483 |
| L_project_title_vos | warm | flat | 50 | home_to_library | PASS | 10 | 22.406 | 21.740 | 23.966 | 21.646–24.602 |
| L_project_title_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 9.270 | 8.261 | 10.716 | 7.839–12.092 |
| L_project_title_vos | warm | flat | 50 | library_first_render | PASS | 10 | 22.274 | 21.142 | 23.790 | 21.031–23.861 |
| L_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 26.544 | 24.266 | 28.555 | 23.534–35.249 |
| L_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.645 | 8.128 | 8.744 | 7.782–8.916 |
| L_project_title_vos | warm | flat | 50 | library_sequential_paging | PASS | 3 | 9.903 | 8.785 | 10.485 | 8.506–10.630 |
| L_project_title_vos | warm | flat | 50 | open_book | PASS | 10 | 38.908 | 36.866 | 41.151 | 36.062–42.030 |
| L_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 39.793 | 35.649 | 41.614 | 34.497–41.998 |
| L_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.441 | 7.895 | 8.704 | 7.818–9.010 |
| L_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 83.514 | 83.261 | 83.768 | 83.197–83.832 |
| L_project_title_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 7.933 | 7.249 | 8.210 | 6.885–8.434 |
| L_project_title_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 27.748 | 24.536 | 35.123 | 24.088–39.517 |
| L_project_title_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.036 | 7.800 | 8.228 | 7.767–8.512 |
| L_project_title_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.817 | 16.631 | 17.871 | 15.972–18.934 |
| L_project_title_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 17.130 | 16.422 | 18.926 | 16.381–21.513 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 17.953 | 17.368 | 19.104 | 17.225–19.144 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 13.265 | 8.531 | 16.645 | 7.223–20.449 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 40.252 | 37.471 | 45.167 | 36.692–45.555 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 40.913 | 37.745 | 43.982 | 37.689–44.146 |
| L_project_title_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.431 | 7.772 | 8.877 | 7.619–9.284 |
| L_project_title_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 7.928 | 6.969 | 8.052 | 6.900–8.530 |
| L_project_title_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 22.720 | 20.610 | 25.750 | 20.257–27.325 |
| L_project_title_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.089 | 7.704 | 8.890 | 7.450–9.038 |
| L_project_title_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.190 | 15.674 | 16.885 | 15.189–17.277 |
| L_project_title_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.686 | 15.752 | 18.349 | 15.559–18.449 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 18.316 | 17.328 | 20.366 | 17.268–20.420 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 8.408 | 7.998 | 8.687 | 7.471–8.704 |
| L_project_title_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 37.411 | 35.372 | 39.609 | 33.323–40.865 |
| L_project_title_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 38.620 | 37.227 | 39.592 | 36.335–40.245 |
| L_project_title_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.534 | 8.229 | 9.079 | 8.188–9.148 |
| A_stock | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 10.254 | 10.254 | 10.254 | 10.254–10.254 |
| A_stock | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 8.189 | 8.189 | 8.189 | 8.189–8.189 |
| B_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 10.691 | 10.691 | 10.691 | 10.691–10.691 |
| B_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 8.869 | 8.869 | 8.869 | 8.869–8.869 |
| C_simpleui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 9.487 | 9.487 | 9.487 | 9.487–9.487 |
| C_simpleui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 24.599 | 24.599 | 24.599 | 24.599–24.599 |
| D_zenos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 34.483 | 34.483 | 34.483 | 34.483–34.483 |
| D_zenos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 23.803 | 23.803 | 23.803 | 23.803–23.803 |
| E_project_title | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 6.842 | 6.842 | 6.842 | 6.842–6.842 |
| E_project_title | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 8.334 | 8.334 | 8.334 | 8.334–8.334 |
| F_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 19.926 | 19.926 | 19.926 | 19.926–19.926 |
| F_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.650 | 16.650 | 16.650 | 16.650–16.650 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.373 | 8.373 | 8.373 | 8.373–8.373 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 23.016 | 23.016 | 23.016 | 23.016–23.016 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 34.431 | 34.431 | 34.431 | 34.431–34.431 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 26.342 | 26.342 | 26.342 | 26.342–26.342 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 18.574 | 18.574 | 18.574 | 18.574–18.574 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 18.426 | 18.426 | 18.426 | 18.426–18.426 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 9.249 | 9.249 | 9.249 | 9.249–9.249 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 24.434 | 24.434 | 24.434 | 24.434–24.434 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.818 | 8.818 | 8.818 | 8.818–8.818 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 25.996 | 25.996 | 25.996 | 25.996–25.996 |
| L_project_title_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 17.716 | 17.716 | 17.716 | 17.716–17.716 |
| L_project_title_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 15.687 | 15.687 | 15.687 | 15.687–15.687 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 484.934 | 451.427 | 507.697 | 443.050–513.388 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 508.255 | 475.325 | 531.791 | 467.093–537.675 |
| A_stock | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 512.648 | 479.849 | 536.176 | 471.649–542.058 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 551.618 | 521.734 | 575.359 | 514.263–581.294 |
| A_stock | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 406.386 | 399.904 | 570.665 | 398.284–611.735 |
| A_stock | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 428.489 | 421.670 | 594.673 | 419.965–636.219 |
| A_stock | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1826.864 | 1802.785 | 1999.888 | 1796.765–2043.144 |
| A_stock | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1887.505 | 1874.612 | 2065.051 | 1871.389–2109.438 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 346.482 | 342.448 | 348.063 | 341.439–348.458 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 376.012 | 372.582 | 377.562 | 371.725–377.950 |
| A_stock | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1479.213 | 1459.679 | 1479.880 | 1454.796–1480.047 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1522.660 | 1502.312 | 1527.840 | 1497.225–1529.134 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 559.547 | 465.790 | 684.414 | 442.351–715.630 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 583.872 | 488.209 | 705.872 | 464.294–736.372 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 588.066 | 493.069 | 710.726 | 469.320–741.391 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 654.878 | 537.575 | 755.349 | 508.249–780.467 |
| A_stock | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 594.358 | 594.358 | 594.358 | 594.358–594.358 |
| A_stock | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3699.540 | 3699.540 | 3699.540 | 3699.540–3699.540 |
| A_stock | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 15948.230 | 15948.230 | 15948.230 | 15948.230–15948.230 |
| A_stock | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 16142.308 | 16142.308 | 16142.308 | 16142.308–16142.308 |
| A_stock | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 371.671 | 371.671 | 371.671 | 371.671–371.671 |
| A_stock | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1320.998 | 1320.998 | 1320.998 | 1320.998–1320.998 |
| A_stock | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 8684.530 | 8684.530 | 8684.530 | 8684.530–8684.530 |
| A_stock | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8735.085 | 8735.085 | 8735.085 | 8735.085–8735.085 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 2115.710 | 2115.710 | 2115.710 | 2115.710–2115.710 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2480.620 | 2480.620 | 2480.620 | 2480.620–2480.620 |
| A_stock | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7271.131 | 7271.131 | 7271.131 | 7271.131–7271.131 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7342.974 | 7342.974 | 7342.974 | 7342.974–7342.974 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 600.326 | 600.326 | 600.326 | 600.326–600.326 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 958.248 | 958.248 | 958.248 | 958.248–958.248 |
| A_stock | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4873.793 | 4873.793 | 4873.793 | 4873.793–4873.793 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4974.315 | 4974.315 | 4974.315 | 4974.315–4974.315 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 546.157 | 497.005 | 547.908 | 484.717–548.346 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 568.823 | 521.146 | 571.905 | 509.227–572.675 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 574.249 | 525.959 | 577.110 | 513.886–577.825 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 614.495 | 568.201 | 617.378 | 556.628–618.099 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 475.762 | 424.164 | 477.564 | 411.264–478.014 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 498.421 | 444.824 | 499.598 | 431.424–499.892 |
| B_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 14416.300 | 13422.645 | 14469.835 | 13174.232–14483.219 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 14459.451 | 13464.775 | 14512.617 | 13216.105–14525.908 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 427.305 | 416.835 | 459.962 | 414.218–468.127 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 456.743 | 446.932 | 494.917 | 444.480–504.460 |
| B_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 12342.221 | 12226.328 | 12468.188 | 12197.355–12499.680 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 12384.816 | 12268.583 | 12509.793 | 12239.525–12541.038 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 455.971 | 455.019 | 526.222 | 454.781–543.784 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 477.918 | 476.982 | 549.136 | 476.749–566.940 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 482.535 | 482.166 | 553.737 | 482.073–571.538 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 521.216 | 520.493 | 592.312 | 520.312–610.086 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 655.453 | 655.453 | 655.453 | 655.453–655.453 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3902.396 | 3902.396 | 3902.396 | 3902.396–3902.396 |
| B_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 30332.075 | 30332.075 | 30332.075 | 30332.075–30332.075 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 30484.481 | 30484.481 | 30484.481 | 30484.481–30484.481 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 487.167 | 487.167 | 487.167 | 487.167–487.167 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1607.429 | 1607.429 | 1607.429 | 1607.429–1607.429 |
| B_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 16802.676 | 16802.676 | 16802.676 | 16802.676–16802.676 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 16855.417 | 16855.417 | 16855.417 | 16855.417–16855.417 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 560.925 | 560.925 | 560.925 | 560.925–560.925 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 924.383 | 924.383 | 924.383 | 924.383–924.383 |
| B_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 6494.682 | 6494.682 | 6494.682 | 6494.682–6494.682 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 6542.053 | 6542.053 | 6542.053 | 6542.053–6542.053 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 564.076 | 564.076 | 564.076 | 564.076–564.076 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 929.687 | 929.687 | 929.687 | 929.687–929.687 |
| B_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5615.449 | 5615.449 | 5615.449 | 5615.449–5615.449 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5662.988 | 5662.988 | 5662.988 | 5662.988–5662.988 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 565.465 | 538.590 | 581.795 | 531.872–585.878 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 608.644 | 579.692 | 627.102 | 572.453–631.716 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 616.684 | 587.901 | 634.952 | 580.706–639.519 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 656.708 | 626.986 | 676.901 | 619.556–681.950 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 495.230 | 481.361 | 501.006 | 477.894–502.450 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 528.744 | 512.354 | 530.755 | 508.257–531.258 |
| C_simpleui | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1943.501 | 1937.112 | 2041.914 | 1935.515–2066.517 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1982.999 | 1976.873 | 2082.595 | 1975.342–2107.494 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 460.119 | 433.155 | 472.578 | 426.414–475.692 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 494.229 | 468.463 | 505.767 | 462.021–508.651 |
| C_simpleui | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1702.381 | 1668.970 | 1722.297 | 1660.617–1727.276 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1742.545 | 1715.932 | 1761.126 | 1709.279–1765.771 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 591.023 | 549.392 | 595.976 | 538.985–597.215 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 632.668 | 591.441 | 635.652 | 581.134–636.398 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 639.579 | 599.290 | 642.325 | 589.218–643.012 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 688.981 | 646.228 | 689.435 | 635.540–689.548 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 779.906 | 779.906 | 779.906 | 779.906–779.906 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2238.078 | 2238.078 | 2238.078 | 2238.078–2238.078 |
| C_simpleui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 21894.020 | 21894.020 | 21894.020 | 21894.020–21894.020 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 21971.793 | 21971.793 | 21971.793 | 21971.793–21971.793 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 616.793 | 616.793 | 616.793 | 616.793–616.793 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1511.308 | 1511.308 | 1511.308 | 1511.308–1511.308 |
| C_simpleui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 10853.547 | 10853.547 | 10853.547 | 10853.547–10853.547 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10918.193 | 10918.193 | 10918.193 | 10918.193–10918.193 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 569.263 | 569.263 | 569.263 | 569.263–569.263 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1298.439 | 1298.439 | 1298.439 | 1298.439–1298.439 |
| C_simpleui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9628.166 | 9628.166 | 9628.166 | 9628.166–9628.166 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9716.283 | 9716.283 | 9716.283 | 9716.283–9716.283 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 629.206 | 629.206 | 629.206 | 629.206–629.206 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1482.500 | 1482.500 | 1482.500 | 1482.500–1482.500 |
| C_simpleui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9723.934 | 9723.934 | 9723.934 | 9723.934–9723.934 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9782.855 | 9782.855 | 9782.855 | 9782.855–9782.855 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 590.638 | 580.338 | 654.932 | 577.763–671.006 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 677.209 | 661.337 | 734.129 | 657.369–748.360 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 687.945 | 671.546 | 743.519 | 667.446–757.413 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 729.333 | 712.590 | 788.414 | 708.404–803.184 |
| D_zenos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 478.810 | 473.096 | 514.135 | 471.667–522.967 |
| D_zenos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 578.859 | 576.635 | 612.812 | 576.079–621.300 |
| D_zenos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1367.796 | 1359.294 | 1397.977 | 1357.169–1405.522 |
| D_zenos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1409.066 | 1400.130 | 1438.232 | 1397.896–1445.523 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 490.722 | 484.368 | 491.330 | 482.779–491.482 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 523.588 | 513.068 | 523.877 | 510.438–523.949 |
| D_zenos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1282.490 | 1280.538 | 1289.224 | 1280.051–1290.907 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1323.943 | 1322.460 | 1330.837 | 1322.089–1332.561 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 605.653 | 602.462 | 623.558 | 601.664–628.035 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 674.631 | 669.703 | 689.539 | 668.471–693.266 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 683.035 | 678.063 | 697.925 | 676.821–701.648 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 728.887 | 719.482 | 740.860 | 717.131–743.853 |
| D_zenos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 720.444 | 720.444 | 720.444 | 720.444–720.444 |
| D_zenos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3667.294 | 3667.294 | 3667.294 | 3667.294–3667.294 |
| D_zenos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 15919.264 | 15919.264 | 15919.264 | 15919.264–15919.264 |
| D_zenos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 15979.244 | 15979.244 | 15979.244 | 15979.244–15979.244 |
| D_zenos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 672.404 | 672.404 | 672.404 | 672.404–672.404 |
| D_zenos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2261.514 | 2261.514 | 2261.514 | 2261.514–2261.514 |
| D_zenos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 10760.023 | 10760.023 | 10760.023 | 10760.023–10760.023 |
| D_zenos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10861.403 | 10861.403 | 10861.403 | 10861.403–10861.403 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 679.672 | 679.672 | 679.672 | 679.672–679.672 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1909.201 | 1909.201 | 1909.201 | 1909.201–1909.201 |
| D_zenos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9023.304 | 9023.304 | 9023.304 | 9023.304–9023.304 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9074.810 | 9074.810 | 9074.810 | 9074.810–9074.810 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 778.576 | 778.576 | 778.576 | 778.576–778.576 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2014.542 | 2014.542 | 2014.542 | 2014.542–2014.542 |
| D_zenos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8896.989 | 8896.989 | 8896.989 | 8896.989–8896.989 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8954.702 | 8954.702 | 8954.702 | 8954.702–8954.702 |
| E_project_title | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 407.670 | 386.335 | 564.879 | 381.001–604.181 |
| E_project_title | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 421.700 | 400.922 | 580.323 | 395.728–619.978 |
| E_project_title | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1153.043 | 1116.933 | 1342.854 | 1107.906–1390.307 |
| E_project_title | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1191.686 | 1155.932 | 1383.935 | 1146.993–1431.997 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 329.249 | 323.592 | 329.330 | 322.178–329.350 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 350.436 | 349.264 | 352.613 | 348.971–353.158 |
| E_project_title | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 892.125 | 891.912 | 920.915 | 891.859–928.113 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 932.193 | 929.558 | 959.122 | 928.899–965.854 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 307.673 | 306.526 | 314.456 | 306.239–316.151 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 328.756 | 326.752 | 335.108 | 326.251–336.696 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 333.013 | 330.640 | 339.715 | 330.047–341.391 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 370.156 | 369.474 | 376.717 | 369.303–378.357 |
| E_project_title | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 412.383 | 412.383 | 412.383 | 412.383–412.383 |
| E_project_title | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1946.198 | 1946.198 | 1946.198 | 1946.198–1946.198 |
| E_project_title | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 9364.386 | 9364.386 | 9364.386 | 9364.386–9364.386 |
| E_project_title | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9407.492 | 9407.492 | 9407.492 | 9407.492–9407.492 |
| E_project_title | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 384.243 | 384.243 | 384.243 | 384.243–384.243 |
| E_project_title | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 921.577 | 921.577 | 921.577 | 921.577–921.577 |
| E_project_title | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 4522.050 | 4522.050 | 4522.050 | 4522.050–4522.050 |
| E_project_title | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4563.633 | 4563.633 | 4563.633 | 4563.633–4563.633 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 350.023 | 350.023 | 350.023 | 350.023–350.023 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 670.113 | 670.113 | 670.113 | 670.113–670.113 |
| E_project_title | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 3574.676 | 3574.676 | 3574.676 | 3574.676–3574.676 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 3616.785 | 3616.785 | 3616.785 | 3616.785–3616.785 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 347.184 | 347.184 | 347.184 | 347.184–347.184 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 657.844 | 657.844 | 657.844 | 657.844–657.844 |
| E_project_title | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 3274.482 | 3274.482 | 3274.482 | 3274.482–3274.482 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 3315.810 | 3315.810 | 3315.810 | 3315.810–3315.810 |
| F_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 415.810 | 413.402 | 417.700 | 412.800–418.173 |
| F_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 436.335 | 433.422 | 439.367 | 432.694–440.126 |
| F_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1837.637 | 1807.490 | 1861.061 | 1799.953–1866.917 |
| F_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1906.990 | 1888.416 | 1927.842 | 1883.773–1933.055 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 357.000 | 352.997 | 362.831 | 351.996–364.289 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 396.315 | 392.177 | 401.909 | 391.143–403.308 |
| F_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1511.564 | 1499.744 | 1512.861 | 1496.790–1513.186 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1553.473 | 1542.817 | 1555.128 | 1540.153–1555.542 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 428.286 | 405.903 | 486.386 | 400.308–500.911 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 468.354 | 448.190 | 529.735 | 443.149–545.081 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 474.041 | 453.456 | 535.235 | 448.310–550.533 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 514.258 | 492.609 | 574.179 | 487.196–589.160 |
| F_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 539.656 | 539.656 | 539.656 | 539.656–539.656 |
| F_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3501.436 | 3501.436 | 3501.436 | 3501.436–3501.436 |
| F_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 16184.436 | 16184.436 | 16184.436 | 16184.436–16184.436 |
| F_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 16316.642 | 16316.642 | 16316.642 | 16316.642–16316.642 |
| F_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 389.743 | 389.743 | 389.743 | 389.743–389.743 |
| F_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1738.836 | 1738.836 | 1738.836 | 1738.836–1738.836 |
| F_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 9651.674 | 9651.674 | 9651.674 | 9651.674–9651.674 |
| F_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9698.408 | 9698.408 | 9698.408 | 9698.408–9698.408 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 443.384 | 443.384 | 443.384 | 443.384–443.384 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1137.224 | 1137.224 | 1137.224 | 1137.224–1137.224 |
| F_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7010.698 | 7010.698 | 7010.698 | 7010.698–7010.698 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7062.140 | 7062.140 | 7062.140 | 7062.140–7062.140 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 611.071 | 611.071 | 611.071 | 611.071–611.071 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1242.174 | 1242.174 | 1242.174 | 1242.174–1242.174 |
| F_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5607.527 | 5607.527 | 5607.527 | 5607.527–5607.527 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5655.294 | 5655.294 | 5655.294 | 5655.294–5655.294 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 530.361 | 506.920 | 677.531 | 501.059–714.323 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 562.149 | 534.735 | 712.900 | 527.882–750.587 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 14908.434 | 14801.379 | 15099.189 | 14774.616–15146.878 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 14962.424 | 14857.551 | 15149.412 | 14831.333–15196.158 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 729.702 | 706.595 | 737.699 | 700.818–739.698 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 761.592 | 741.970 | 772.781 | 737.065–775.579 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 12364.611 | 12329.455 | 12534.546 | 12320.666–12577.029 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 12414.967 | 12385.079 | 12580.081 | 12377.606–12621.360 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 530.797 | 480.053 | 550.726 | 467.367–555.709 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 574.282 | 523.038 | 593.342 | 510.227–598.107 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 581.497 | 530.324 | 602.313 | 517.531–607.517 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 622.958 | 572.213 | 643.909 | 559.526–649.147 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 730.808 | 730.808 | 730.808 | 730.808–730.808 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2237.852 | 2237.852 | 2237.852 | 2237.852–2237.852 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 34964.941 | 34964.941 | 34964.941 | 34964.941–34964.941 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 35360.437 | 35360.437 | 35360.437 | 35360.437–35360.437 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 607.600 | 607.600 | 607.600 | 607.600–607.600 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1543.322 | 1543.322 | 1543.322 | 1543.322–1543.322 |
| G_simpleui_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 19020.404 | 19020.404 | 19020.404 | 19020.404–19020.404 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 19092.441 | 19092.441 | 19092.441 | 19092.441–19092.441 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 663.084 | 663.084 | 663.084 | 663.084–663.084 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1524.000 | 1524.000 | 1524.000 | 1524.000–1524.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 12211.418 | 12211.418 | 12211.418 | 12211.418–12211.418 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12275.096 | 12275.096 | 12275.096 | 12275.096–12275.096 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 704.826 | 704.826 | 704.826 | 704.826–704.826 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1567.836 | 1567.836 | 1567.836 | 1567.836–1567.836 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 11723.974 | 11723.974 | 11723.974 | 11723.974–11723.974 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11788.366 | 11788.366 | 11788.366 | 11788.366–11788.366 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 646.395 | 646.226 | 883.398 | 646.184–942.649 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 755.104 | 754.083 | 980.904 | 753.827–1037.353 |
| H_zenos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 13588.730 | 13069.832 | 13841.408 | 12940.108–13904.577 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 13700.848 | 13145.254 | 13952.363 | 13006.356–14015.241 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 487.101 | 484.268 | 595.535 | 483.559–622.643 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 518.445 | 515.487 | 629.018 | 514.748–656.662 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 11779.399 | 11523.882 | 11843.220 | 11460.003–11859.175 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 11822.761 | 11567.616 | 11887.064 | 11503.830–11903.140 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 590.152 | 568.823 | 593.535 | 563.491–594.380 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 660.373 | 636.867 | 662.320 | 630.990–662.807 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 670.049 | 646.728 | 672.634 | 640.898–673.281 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 713.413 | 688.968 | 721.443 | 682.857–723.451 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 739.886 | 739.886 | 739.886 | 739.886–739.886 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3731.168 | 3731.168 | 3731.168 | 3731.168–3731.168 |
| H_zenos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 27995.394 | 27995.394 | 27995.394 | 27995.394–27995.394 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 28058.463 | 28058.463 | 28058.463 | 28058.463–28058.463 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 712.864 | 712.864 | 712.864 | 712.864–712.864 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2233.676 | 2233.676 | 2233.676 | 2233.676–2233.676 |
| H_zenos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18015.055 | 18015.055 | 18015.055 | 18015.055–18015.055 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18068.899 | 18068.899 | 18068.899 | 18068.899–18068.899 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 637.787 | 637.787 | 637.787 | 637.787–637.787 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1857.605 | 1857.605 | 1857.605 | 1857.605–1857.605 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9804.764 | 9804.764 | 9804.764 | 9804.764–9804.764 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9863.441 | 9863.441 | 9863.441 | 9863.441–9863.441 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 754.562 | 754.562 | 754.562 | 754.562–754.562 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1986.025 | 1986.025 | 1986.025 | 1986.025–1986.025 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9733.460 | 9733.460 | 9733.460 | 9733.460–9733.460 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9789.022 | 9789.022 | 9789.022 | 9789.022–9789.022 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 504.173 | 458.525 | 504.508 | 447.113–504.592 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 525.358 | 477.283 | 526.275 | 465.264–526.505 |
| I_vos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 14931.558 | 14923.932 | 15026.090 | 14922.025–15049.722 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 14976.493 | 14966.646 | 15070.802 | 14964.185–15094.380 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 442.552 | 378.616 | 445.406 | 362.632–446.119 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 482.960 | 417.161 | 485.275 | 400.711–485.854 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 12387.491 | 12221.036 | 12459.403 | 12179.422–12477.380 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 12428.352 | 12263.609 | 12501.022 | 12222.423–12519.190 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 514.253 | 480.226 | 695.170 | 471.719–740.399 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 555.981 | 522.372 | 735.869 | 513.970–780.841 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 561.688 | 528.376 | 741.169 | 520.048–786.039 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 606.793 | 586.208 | 781.115 | 581.062–824.695 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 646.495 | 646.495 | 646.495 | 646.495–646.495 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3932.028 | 3932.028 | 3932.028 | 3932.028–3932.028 |
| I_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 29992.306 | 29992.306 | 29992.306 | 29992.306–29992.306 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 30196.171 | 30196.171 | 30196.171 | 30196.171–30196.171 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 530.847 | 530.847 | 530.847 | 530.847–530.847 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2000.435 | 2000.435 | 2000.435 | 2000.435–2000.435 |
| I_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 17542.724 | 17542.724 | 17542.724 | 17542.724–17542.724 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 17609.905 | 17609.905 | 17609.905 | 17609.905–17609.905 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 547.150 | 547.150 | 547.150 | 547.150–547.150 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1224.900 | 1224.900 | 1224.900 | 1224.900–1224.900 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7652.547 | 7652.547 | 7652.547 | 7652.547–7652.547 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7707.214 | 7707.214 | 7707.214 | 7707.214–7707.214 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 566.631 | 566.631 | 566.631 | 566.631–566.631 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1247.702 | 1247.702 | 1247.702 | 1247.702–1247.702 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6555.651 | 6555.651 | 6555.651 | 6555.651–6555.651 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6599.499 | 6599.499 | 6599.499 | 6599.499–6599.499 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 495.753 | 486.689 | 561.449 | 484.423–577.873 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 525.154 | 514.604 | 591.225 | 511.967–607.743 |
| J_simpleui_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1982.887 | 1948.426 | 1992.132 | 1939.811–1994.443 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2022.060 | 1988.517 | 2034.137 | 1980.131–2037.156 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 452.367 | 442.347 | 454.928 | 439.842–455.568 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 488.583 | 473.797 | 491.557 | 470.101–492.300 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1438.394 | 1418.143 | 1635.133 | 1413.081–1684.318 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1485.268 | 1462.699 | 1676.664 | 1457.057–1724.514 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 420.221 | 398.489 | 425.701 | 393.057–427.071 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 460.566 | 439.148 | 465.547 | 433.794–466.792 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 468.472 | 446.641 | 472.565 | 441.183–473.589 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 512.930 | 487.667 | 515.447 | 481.351–516.076 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 610.124 | 610.124 | 610.124 | 610.124–610.124 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2106.893 | 2106.893 | 2106.893 | 2106.893–2106.893 |
| J_simpleui_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 22585.459 | 22585.459 | 22585.459 | 22585.459–22585.459 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 22803.154 | 22803.154 | 22803.154 | 22803.154–22803.154 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 598.580 | 598.580 | 598.580 | 598.580–598.580 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1732.870 | 1732.870 | 1732.870 | 1732.870–1732.870 |
| J_simpleui_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 12519.094 | 12519.094 | 12519.094 | 12519.094–12519.094 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 12576.999 | 12576.999 | 12576.999 | 12576.999–12576.999 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 436.922 | 436.922 | 436.922 | 436.922–436.922 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1194.198 | 1194.198 | 1194.198 | 1194.198–1194.198 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 8853.436 | 8853.436 | 8853.436 | 8853.436–8853.436 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 8912.216 | 8912.216 | 8912.216 | 8912.216–8912.216 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 536.664 | 536.664 | 536.664 | 536.664–536.664 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1223.693 | 1223.693 | 1223.693 | 1223.693–1223.693 |
| J_simpleui_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 7586.033 | 7586.033 | 7586.033 | 7586.033–7586.033 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7640.364 | 7640.364 | 7640.364 | 7640.364–7640.364 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 524.519 | 506.743 | 621.860 | 502.299–646.196 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 555.564 | 536.034 | 648.936 | 531.152–672.279 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 14701.697 | 13627.757 | 14883.840 | 13359.272–14929.376 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 14752.158 | 13677.972 | 14935.295 | 13409.425–14981.079 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 689.435 | 610.306 | 731.871 | 590.524–742.480 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 728.728 | 645.781 | 769.958 | 625.044–780.266 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 12426.464 | 11099.298 | 12456.391 | 10767.507–12463.873 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 12475.528 | 11184.045 | 12508.925 | 10861.175–12517.274 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 572.280 | 547.489 | 584.226 | 541.291–587.213 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 614.234 | 591.656 | 626.749 | 586.011–629.877 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 621.826 | 599.911 | 634.505 | 594.432–637.675 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 660.726 | 640.442 | 675.375 | 635.371–679.037 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 759.228 | 759.228 | 759.228 | 759.228–759.228 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2292.036 | 2292.036 | 2292.036 | 2292.036–2292.036 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 36642.784 | 36642.784 | 36642.784 | 36642.784–36642.784 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 37083.061 | 37083.061 | 37083.061 | 37083.061–37083.061 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 581.088 | 581.088 | 581.088 | 581.088–581.088 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1693.925 | 1693.925 | 1693.925 | 1693.925–1693.925 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 20722.580 | 20722.580 | 20722.580 | 20722.580–20722.580 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 20786.909 | 20786.909 | 20786.909 | 20786.909–20786.909 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 762.843 | 762.843 | 762.843 | 762.843–762.843 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1581.711 | 1581.711 | 1581.711 | 1581.711–1581.711 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 12739.693 | 12739.693 | 12739.693 | 12739.693–12739.693 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12804.932 | 12804.932 | 12804.932 | 12804.932–12804.932 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 682.378 | 682.378 | 682.378 | 682.378–682.378 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1495.018 | 1495.018 | 1495.018 | 1495.018–1495.018 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 11323.144 | 11323.144 | 11323.144 | 11323.144–11323.144 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11394.660 | 11394.660 | 11394.660 | 11394.660–11394.660 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 496.883 | 480.026 | 511.548 | 475.812–515.214 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 539.118 | 522.304 | 554.075 | 518.100–557.815 |
| K_vos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 543.792 | 527.505 | 558.943 | 523.433–562.730 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 587.331 | 567.171 | 602.119 | 562.131–605.817 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 577.827 | 538.566 | 582.543 | 528.751–583.722 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 596.121 | 556.499 | 601.569 | 546.593–602.931 |
| L_project_title_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1371.549 | 1330.614 | 1373.105 | 1320.380–1373.494 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1415.047 | 1372.956 | 1416.209 | 1362.433–1416.500 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 499.923 | 479.864 | 567.004 | 474.849–583.774 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 533.200 | 516.554 | 600.795 | 512.393–617.694 |
| L_project_title_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1121.844 | 1111.835 | 1178.536 | 1109.333–1192.709 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1167.607 | 1153.819 | 1225.880 | 1150.372–1240.449 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 523.589 | 476.576 | 535.686 | 464.822–538.710 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 564.637 | 516.997 | 575.017 | 505.087–577.612 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 569.614 | 522.216 | 580.638 | 510.367–583.395 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 615.561 | 566.561 | 620.772 | 554.311–622.075 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 557.854 | 557.854 | 557.854 | 557.854–557.854 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2355.634 | 2355.634 | 2355.634 | 2355.634–2355.634 |
| L_project_title_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 10651.709 | 10651.709 | 10651.709 | 10651.709–10651.709 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 10699.725 | 10699.725 | 10699.725 | 10699.725–10699.725 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 532.293 | 532.293 | 532.293 | 532.293–532.293 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1374.039 | 1374.039 | 1374.039 | 1374.039–1374.039 |
| L_project_title_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 5808.604 | 5808.604 | 5808.604 | 5808.604–5808.604 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5856.966 | 5856.966 | 5856.966 | 5856.966–5856.966 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 651.687 | 651.687 | 651.687 | 651.687–651.687 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1299.002 | 1299.002 | 1299.002 | 1299.002–1299.002 |
| L_project_title_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 5136.846 | 5136.846 | 5136.846 | 5136.846–5136.846 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 5182.662 | 5182.662 | 5182.662 | 5182.662–5182.662 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 527.869 | 527.869 | 527.869 | 527.869–527.869 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1154.506 | 1154.506 | 1154.506 | 1154.506–1154.506 |
| L_project_title_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4600.670 | 4600.670 | 4600.670 | 4600.670–4600.670 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4643.749 | 4643.749 | 4643.749 | 4643.749–4643.749 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 688.045 | 688.045 | 688.045 | 688.045–688.045 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 713.006 | 713.006 | 713.006 | 713.006–713.006 |
| A_stock | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 717.500 | 717.500 | 717.500 | 717.500–717.500 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 761.423 | 761.423 | 761.423 | 761.423–761.423 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 495.986 | 495.986 | 495.986 | 495.986–495.986 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 521.221 | 521.221 | 521.221 | 521.221–521.221 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 525.994 | 525.994 | 525.994 | 525.994–525.994 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 563.870 | 563.870 | 563.870 | 563.870–563.870 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 614.093 | 614.093 | 614.093 | 614.093–614.093 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 657.657 | 657.657 | 657.657 | 657.657–657.657 |
| C_simpleui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 664.446 | 664.446 | 664.446 | 664.446–664.446 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 745.361 | 745.361 | 745.361 | 745.361–745.361 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 680.372 | 680.372 | 680.372 | 680.372–680.372 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 759.576 | 759.576 | 759.576 | 759.576–759.576 |
| D_zenos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 770.414 | 770.414 | 770.414 | 770.414–770.414 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 812.249 | 812.249 | 812.249 | 812.249–812.249 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 346.205 | 346.205 | 346.205 | 346.205–346.205 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 367.612 | 367.612 | 367.612 | 367.612–367.612 |
| E_project_title | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 371.870 | 371.870 | 371.870 | 371.870–371.870 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 409.885 | 409.885 | 409.885 | 409.885–409.885 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 533.999 | 533.999 | 533.999 | 533.999–533.999 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 575.956 | 575.956 | 575.956 | 575.956–575.956 |
| F_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 581.548 | 581.548 | 581.548 | 581.548–581.548 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 625.452 | 625.452 | 625.452 | 625.452–625.452 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 624.394 | 624.394 | 624.394 | 624.394–624.394 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 664.555 | 664.555 | 664.555 | 664.555–664.555 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 672.325 | 672.325 | 672.325 | 672.325–672.325 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 716.030 | 716.030 | 716.030 | 716.030–716.030 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 637.707 | 637.707 | 637.707 | 637.707–637.707 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 723.338 | 723.338 | 723.338 | 723.338–723.338 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 732.396 | 732.396 | 732.396 | 732.396–732.396 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 773.680 | 773.680 | 773.680 | 773.680–773.680 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 488.009 | 488.009 | 488.009 | 488.009–488.009 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 531.223 | 531.223 | 531.223 | 531.223–531.223 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 537.635 | 537.635 | 537.635 | 537.635–537.635 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 588.191 | 588.191 | 588.191 | 588.191–588.191 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 443.444 | 443.444 | 443.444 | 443.444–443.444 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 485.265 | 485.265 | 485.265 | 485.265–485.265 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 492.561 | 492.561 | 492.561 | 492.561–492.561 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 532.029 | 532.029 | 532.029 | 532.029–532.029 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 706.045 | 706.045 | 706.045 | 706.045–706.045 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 750.563 | 750.563 | 750.563 | 750.563–750.563 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 759.215 | 759.215 | 759.215 | 759.215–759.215 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 800.618 | 800.618 | 800.618 | 800.618–800.618 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 542.637 | 542.637 | 542.637 | 542.637–542.637 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 582.067 | 582.067 | 582.067 | 582.067–582.067 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 587.506 | 587.506 | 587.506 | 587.506–587.506 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 625.062 | 625.062 | 625.062 | 625.062–625.062 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|:--|--:|--:|
| A_stock | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8370.796 | 8389.865 | 8357.097–8394.632 | 9026.962 | 171792.000 |
| A_stock | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8272.854 | 8296.833 | 8249.687–8302.827 | 14545.701 | 163968.000 |
| A_stock | paging | flat | 2000 | post_stress_idle | PASS | 3 | 11463.812 | 11493.565 | 11457.647–11501.003 | 11518.069 | 196544.000 |
| A_stock | paging | flat | 2000 | post_init_idle | PASS | 3 | 10892.964 | 10917.195 | 10841.269–10923.253 | 17032.459 | 170640.000 |
| A_stock | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8304.077 | 8335.662 | 8241.983–8343.558 | 14565.255 | 166064.000 |
| A_stock | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 9212.964 | 9246.092 | 9211.401–9254.374 | 12067.549 | 194576.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8243.538 | 8275.794 | 8232.304–8283.858 | 11784.050 | 162528.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8211.726 | 8222.072 | 8193.038–8224.659 | 8952.615 | 171440.000 |
| A_stock | warm | flat | 2000 | post_init_idle | PASS | 1 | 10915.151 | 10915.151 | 10915.151–10915.151 | 16714.532 | 170688.000 |
| A_stock | warm | flat | 2000 | post_stress_idle | PASS | 1 | 22324.682 | 22324.682 | 22324.682–22324.682 | 26829.252 | 298144.000 |
| A_stock | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 26099.214 | 26099.214 | 26099.214–26099.214 | 46259.187 | 283216.000 |
| A_stock | warm | flat | 50 | post_init_idle | PASS | 1 | 8639.187 | 8639.187 | 8639.187–8639.187 | 12440.352 | 166096.000 |
| A_stock | warm | flat | 50 | post_library_render_idle | PASS | 1 | 26188.870 | 26188.870 | 26188.870–26188.870 | 26201.167 | 219136.000 |
| A_stock | warm | flat | 50 | post_stress_idle | PASS | 1 | 15883.100 | 15883.100 | 15883.100–15883.100 | 23488.924 | 243936.000 |
| A_stock | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 8271.577 | 8271.577 | 8271.577–8271.577 | 11329.464 | 161472.000 |
| A_stock | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 20201.549 | 20201.549 | 20201.549–20201.549 | 28028.341 | 231696.000 |
| A_stock | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8279.808 | 8279.808 | 8279.808–8279.808 | 9320.615 | 178208.000 |
| A_stock | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 8425.456 | 8425.456 | 8425.456–8425.456 | 14569.963 | 166816.000 |
| A_stock | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 8391.171 | 8391.171 | 8391.171–8391.171 | 9002.612 | 181376.000 |
| A_stock | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 13752.057 | 13752.057 | 13752.057–13752.057 | 20008.521 | 215184.000 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8466.938 | 8492.979 | 8465.396–8499.489 | 9361.641 | 167920.000 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8555.103 | 8589.071 | 8548.579–8597.563 | 9315.823 | 176112.000 |
| B_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 16587.295 | 17257.289 | 16475.588–17424.787 | 23896.768 | 234848.000 |
| B_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 11121.899 | 11364.587 | 11041.075–11425.259 | 18551.379 | 170496.000 |
| B_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 13334.986 | 13344.958 | 13300.990–13347.451 | 32055.882 | 226608.000 |
| B_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8609.173 | 8642.479 | 8449.751–8650.806 | 14973.379 | 167792.000 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8383.048 | 8519.073 | 8340.466–8553.079 | 9082.185 | 171088.000 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8385.157 | 8483.579 | 8325.181–8508.185 | 12948.743 | 162608.000 |
| B_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 11081.267 | 11081.267 | 11081.267–11081.267 | 18357.629 | 171568.000 |
| B_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 21700.708 | 21700.708 | 21700.708–21700.708 | 21718.458 | 287936.000 |
| B_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 66741.033 | 66741.033 | 66741.033–66741.033 | 84778.626 | 279632.000 |
| B_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 8838.333 | 8838.333 | 8838.333–8838.333 | 9435.450 | 165056.000 |
| B_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 18900.310 | 18900.310 | 18900.310–18900.310 | 18916.024 | 282496.000 |
| B_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 26587.403 | 26587.403 | 26587.403–26587.403 | 31388.971 | 213120.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 23869.263 | 23869.263 | 23869.263–23869.263 | 41331.799 | 248864.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 8526.489 | 8526.489 | 8526.489–8526.489 | 12199.949 | 168880.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8414.677 | 8414.677 | 8414.677–8414.677 | 9043.264 | 185504.000 |
| B_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 14775.388 | 14775.388 | 14775.388–14775.388 | 36920.179 | 234400.000 |
| B_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 8633.759 | 8633.759 | 8633.759–8633.759 | 14360.011 | 166016.000 |
| B_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 8431.591 | 8431.591 | 8431.591–8431.591 | 9475.436 | 182928.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 12465.187 | 12473.571 | 12437.046–12475.667 | 18211.308 | 173184.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 12682.233 | 12688.418 | 12673.925–12689.964 | 13814.534 | 181216.000 |
| C_simpleui | paging | flat | 2000 | post_init_idle | PASS | 3 | 14757.089 | 14782.486 | 14714.315–14788.835 | 18325.348 | 177792.000 |
| C_simpleui | paging | flat | 2000 | post_stress_idle | PASS | 3 | 15312.827 | 15333.008 | 15293.405–15338.054 | 17435.815 | 201712.000 |
| C_simpleui | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 12461.554 | 12473.169 | 12454.651–12476.073 | 18645.365 | 174368.000 |
| C_simpleui | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 13342.937 | 13348.527 | 13292.147–13349.925 | 17366.520 | 197904.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 12455.746 | 12752.190 | 12415.586–12826.301 | 15538.999 | 169792.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 12677.906 | 13298.163 | 12623.410–13453.227 | 13727.413 | 178512.000 |
| C_simpleui | warm | flat | 2000 | post_init_idle | PASS | 1 | 14762.093 | 14762.093 | 14762.093–14762.093 | 18158.545 | 177312.000 |
| C_simpleui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 17688.292 | 17688.292 | 17688.292–17688.292 | 18373.893 | 203632.000 |
| C_simpleui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 95734.830 | 95734.830 | 95734.830–95734.830 | 95780.730 | 329360.000 |
| C_simpleui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 14954.370 | 14954.370 | 14954.370–14954.370 | 16591.987 | 186304.000 |
| C_simpleui | warm | flat | 50 | post_stress_idle | PASS | 1 | 46468.607 | 46468.607 | 46468.607–46468.607 | 57855.791 | 273632.000 |
| C_simpleui | warm | flat | 50 | post_init_idle | PASS | 1 | 12752.339 | 12752.339 | 12752.339–12752.339 | 19348.070 | 174224.000 |
| C_simpleui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 12497.534 | 12497.534 | 12497.534–12497.534 | 16846.126 | 172608.000 |
| C_simpleui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 16980.159 | 16980.159 | 16980.159–16980.159 | 17433.446 | 181504.000 |
| C_simpleui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 49682.893 | 49682.893 | 49682.893–49682.893 | 52203.828 | 258720.000 |
| C_simpleui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 15473.772 | 15473.772 | 15473.772–15473.772 | 15565.569 | 177296.000 |
| C_simpleui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 47834.885 | 47834.885 | 47834.885–47834.885 | 51705.287 | 242640.000 |
| C_simpleui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 12441.702 | 12441.702 | 12441.702–12441.702 | 18390.291 | 172736.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 14260.431 | 14271.799 | 14211.946–14274.642 | 15792.589 | 175776.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 14705.728 | 14741.374 | 14694.860–14750.286 | 16730.293 | 190016.000 |
| D_zenos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 20224.771 | 20244.214 | 20217.392–20249.075 | 20239.798 | 206800.000 |
| D_zenos | paging | flat | 2000 | post_init_idle | PASS | 3 | 14195.489 | 14290.127 | 14174.673–14313.786 | 16005.299 | 174832.000 |
| D_zenos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 14288.528 | 14291.913 | 14241.981–14292.759 | 23450.972 | 174976.000 |
| D_zenos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 14873.649 | 14918.249 | 14857.599–14929.399 | 14888.677 | 198768.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 14305.240 | 14309.125 | 14296.896–14310.096 | 22415.187 | 183824.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 14679.537 | 14855.175 | 14612.768–14899.084 | 16494.984 | 186368.000 |
| D_zenos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 20878.543 | 20878.543 | 20878.543–20878.543 | 20895.938 | 218864.000 |
| D_zenos | warm | flat | 2000 | post_init_idle | PASS | 1 | 14176.466 | 14176.466 | 14176.466–14176.466 | 23251.115 | 178112.000 |
| D_zenos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 38721.367 | 38721.367 | 38721.367–38721.367 | 41248.263 | 258336.000 |
| D_zenos | warm | flat | 50 | post_init_idle | PASS | 1 | 14282.728 | 14282.728 | 14282.728–14282.728 | 15623.800 | 177008.000 |
| D_zenos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 15495.485 | 15495.485 | 15495.485–15495.485 | 15641.947 | 197792.000 |
| D_zenos | warm | flat | 50 | post_stress_idle | PASS | 1 | 32966.223 | 32966.223 | 32966.223–32966.223 | 34766.328 | 252288.000 |
| D_zenos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 14782.867 | 14782.867 | 14782.867–14782.867 | 14817.407 | 192608.000 |
| D_zenos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 14267.591 | 14267.591 | 14267.591–14267.591 | 16348.780 | 173568.000 |
| D_zenos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 35482.777 | 35482.777 | 35482.777–35482.777 | 35935.018 | 253904.000 |
| D_zenos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 32780.773 | 32780.773 | 32780.773–32780.773 | 33137.411 | 249648.000 |
| D_zenos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 14240.087 | 14240.087 | 14240.087–14240.087 | 15771.639 | 176704.000 |
| D_zenos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 14724.414 | 14724.414 | 14724.414–14724.414 | 14898.807 | 194496.000 |
| E_project_title | paging | flat | 2000 | post_stress_idle | PASS | 3 | 11807.853 | 11835.393 | 11783.962–11842.278 | 26209.401 | 201296.000 |
| E_project_title | paging | flat | 2000 | post_init_idle | PASS | 3 | 11085.833 | 11099.080 | 11039.704–11102.392 | 16931.705 | 168640.000 |
| E_project_title | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8331.790 | 8381.128 | 8329.528–8393.462 | 14612.825 | 165056.000 |
| E_project_title | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 9211.985 | 9238.092 | 9203.126–9244.618 | 19636.299 | 195312.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8286.665 | 8323.174 | 8281.813–8332.302 | 8984.132 | 169360.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8311.231 | 8323.506 | 8273.868–8326.575 | 12942.123 | 160912.000 |
| E_project_title | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 11057.411 | 11057.411 | 11057.411–11057.411 | 20314.946 | 192432.000 |
| E_project_title | warm | flat | 2000 | post_init_idle | PASS | 1 | 11025.388 | 11025.388 | 11025.388–11025.388 | 17281.305 | 168272.000 |
| E_project_title | warm | flat | 2000 | post_stress_idle | PASS | 1 | 17344.936 | 17344.936 | 17344.936–17344.936 | 29215.536 | 230720.000 |
| E_project_title | warm | flat | 50 | post_stress_idle | PASS | 1 | 13620.139 | 13620.139 | 13620.139–13620.139 | 25272.282 | 212688.000 |
| E_project_title | warm | flat | 50 | post_init_idle | PASS | 1 | 8864.321 | 8864.321 | 8864.321–8864.321 | 15388.431 | 168176.000 |
| E_project_title | warm | flat | 50 | post_library_render_idle | PASS | 1 | 8893.118 | 8893.118 | 8893.118–8893.118 | 18465.154 | 182336.000 |
| E_project_title | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8442.927 | 8442.927 | 8442.927–8442.927 | 10789.749 | 180576.000 |
| E_project_title | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 13737.120 | 13737.120 | 13737.120–13737.120 | 23166.233 | 209184.000 |
| E_project_title | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 8406.524 | 8406.524 | 8406.524–8406.524 | 14249.294 | 165696.000 |
| E_project_title | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 8280.048 | 8280.048 | 8280.048–8280.048 | 14527.838 | 164848.000 |
| E_project_title | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 11664.308 | 11664.308 | 11664.308–11664.308 | 22230.703 | 210848.000 |
| E_project_title | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 8349.356 | 8349.356 | 8349.356–8349.356 | 16113.953 | 179168.000 |
| F_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 11760.667 | 11760.936 | 11707.269–11761.003 | 19691.728 | 173872.000 |
| F_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 12366.694 | 12397.501 | 12360.136–12405.202 | 13536.451 | 198384.000 |
| F_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 10006.187 | 10053.008 | 9985.573–10064.714 | 12447.129 | 195680.000 |
| F_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 8888.800 | 8925.806 | 8883.722–8935.058 | 15274.971 | 168880.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8890.077 | 8910.905 | 8850.308–8916.112 | 9843.606 | 170496.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8863.995 | 8877.845 | 8834.218–8881.308 | 14794.334 | 162192.000 |
| F_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 19491.819 | 19491.819 | 19491.819–19491.819 | 45185.572 | 267488.000 |
| F_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 11745.565 | 11745.565 | 11745.565–11745.565 | 20304.722 | 172032.000 |
| F_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 17931.346 | 17931.346 | 17931.346–17931.346 | 21787.849 | 276896.000 |
| F_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 32783.917 | 32783.917 | 32783.917–32783.917 | 44429.341 | 244576.000 |
| F_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 9280.663 | 9280.663 | 9280.663–9280.663 | 9999.360 | 170544.000 |
| F_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 14697.955 | 14697.955 | 14697.955–14697.955 | 17590.134 | 246368.000 |
| F_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8977.452 | 8977.452 | 8977.452–8977.452 | 9855.196 | 177744.000 |
| F_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 8933.089 | 8933.089 | 8933.089–8933.089 | 15145.418 | 168704.000 |
| F_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 20341.838 | 20341.838 | 20341.838–20341.838 | 26486.173 | 226432.000 |
| F_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 14290.506 | 14290.506 | 14290.506–14290.506 | 20528.500 | 212416.000 |
| F_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 8897.999 | 8897.999 | 8897.999–8897.999 | 9520.526 | 169504.000 |
| F_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 10674.940 | 10674.940 | 10674.940–10674.940 | 10697.854 | 181808.000 |
| G_simpleui_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 19285.446 | 19314.896 | 19270.735–19322.259 | 39280.564 | 245392.000 |
| G_simpleui_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 14905.798 | 14906.835 | 14891.052–14907.095 | 20133.779 | 177632.000 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 12729.313 | 12733.157 | 12680.173–12734.118 | 17926.363 | 171424.000 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 16093.060 | 16145.972 | 16056.829–16159.200 | 23070.576 | 228176.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 12756.029 | 12787.114 | 12735.857–12794.885 | 13939.925 | 177600.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 12556.002 | 12564.246 | 12520.650–12566.307 | 16240.516 | 168832.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 18353.028 | 18353.028 | 18353.028–18353.028 | 18811.393 | 206720.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 14868.333 | 14868.333 | 14868.333–14868.333 | 20146.405 | 171904.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 100039.438 | 100039.438 | 100039.438–100039.438 | 107195.234 | 450816.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 12961.239 | 12961.239 | 12961.239–12961.239 | 18537.852 | 172448.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 49672.556 | 49672.556 | 49672.556–49672.556 | 64718.978 | 311824.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 14230.771 | 14230.771 | 14230.771–14230.771 | 14267.919 | 183952.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 49408.427 | 49408.427 | 49408.427–49408.427 | 52790.871 | 271200.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 12773.423 | 12773.423 | 12773.423–12773.423 | 19795.370 | 170880.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 15541.063 | 15541.063 | 15541.063–15541.063 | 15753.379 | 178352.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 50169.614 | 50169.614 | 50169.614–50169.614 | 53560.591 | 242560.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 12666.087 | 12666.087 | 12666.087–12666.087 | 19858.317 | 174368.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 15509.700 | 15509.700 | 15509.700–15509.700 | 15635.459 | 182096.000 |
| H_zenos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 14498.577 | 14862.387 | 14477.073–14953.339 | 17410.761 | 176384.000 |
| H_zenos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 24041.575 | 25392.391 | 23993.681–25730.095 | 51019.982 | 244272.000 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 14482.812 | 14487.158 | 14470.604–14488.245 | 16972.027 | 175840.000 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 17975.931 | 18014.603 | 17903.438–18024.271 | 34543.036 | 239072.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 14720.570 | 14726.755 | 14661.625–14728.301 | 16507.557 | 183824.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 14317.680 | 14353.736 | 14306.121–14362.750 | 22481.740 | 183824.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 21178.798 | 21178.798 | 21178.798–21178.798 | 21307.599 | 202448.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 14477.929 | 14477.929 | 14477.929–14477.929 | 16831.626 | 172720.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 41447.073 | 41447.073 | 41447.073–41447.073 | 44260.281 | 309088.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 35411.476 | 35411.476 | 35411.476–35411.476 | 35427.315 | 294928.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 14500.987 | 14500.987 | 14500.987–14500.987 | 15918.843 | 172432.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 15213.007 | 15213.007 | 15213.007–15213.007 | 15409.505 | 197920.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 37308.944 | 37308.944 | 37308.944–37308.944 | 37765.938 | 267072.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 14897.873 | 14897.873 | 14897.873–14897.873 | 14933.062 | 196928.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 14543.022 | 14543.022 | 14543.022–14543.022 | 21086.392 | 178016.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 14568.960 | 14568.960 | 14568.960–14568.960 | 16955.815 | 174832.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 36376.136 | 36376.136 | 36376.136–36376.136 | 36692.863 | 267568.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 14811.904 | 14811.904 | 14811.904–14811.904 | 15017.530 | 201696.000 |
| I_vos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 17431.435 | 17433.735 | 17408.071–17434.310 | 27564.085 | 233856.000 |
| I_vos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 11935.974 | 11971.583 | 11845.497–11980.485 | 19230.064 | 174240.000 |
| I_vos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 9227.786 | 9380.292 | 9170.731–9418.419 | 10755.766 | 167344.000 |
| I_vos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 14170.907 | 14179.767 | 14150.458–14181.981 | 20517.008 | 227024.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8994.017 | 9037.407 | 8986.501–9048.255 | 14499.854 | 165248.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8956.056 | 8985.024 | 8945.052–8992.267 | 10032.356 | 173168.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 12025.548 | 12025.548 | 12025.548–12025.548 | 21068.672 | 175792.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 22447.196 | 22447.196 | 22447.196–22447.196 | 26538.794 | 294048.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 69009.225 | 69009.225 | 69009.225–69009.225 | 87167.897 | 282688.000 |
| I_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 17145.646 | 17145.646 | 17145.646–17145.646 | 20431.689 | 253104.000 |
| I_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 32869.438 | 32869.438 | 32869.438–32869.438 | 45146.408 | 240896.000 |
| I_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 9584.106 | 9584.106 | 9584.106–9584.106 | 11201.141 | 163872.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 9088.204 | 9088.204 | 9088.204–9088.204 | 9630.172 | 180352.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 9186.243 | 9186.243 | 9186.243–9186.243 | 10770.367 | 169280.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 23330.872 | 23330.872 | 23330.872–23330.872 | 43173.261 | 243392.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 9025.173 | 9025.173 | 9025.173–9025.173 | 9646.146 | 178128.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 9320.474 | 9320.474 | 9320.474–9320.474 | 16767.011 | 168832.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 14308.411 | 14308.411 | 14308.411–14308.411 | 27709.647 | 225008.000 |
| J_simpleui_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 15342.468 | 15387.562 | 15304.761–15398.835 | 21099.857 | 175200.000 |
| J_simpleui_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 15942.956 | 15976.387 | 15863.562–15984.745 | 16765.790 | 201232.000 |
| J_simpleui_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 13007.976 | 13269.263 | 12923.124–13334.585 | 20000.755 | 173904.000 |
| J_simpleui_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 14979.581 | 15115.134 | 13970.940–15149.022 | 18108.710 | 197632.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 12933.707 | 12940.163 | 12926.926–12941.777 | 17044.378 | 168144.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 13092.379 | 13173.460 | 13054.980–13193.730 | 14087.315 | 178656.000 |
| J_simpleui_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 19110.542 | 19110.542 | 19110.542–19110.542 | 26281.851 | 211184.000 |
| J_simpleui_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 15328.628 | 15328.628 | 15328.628–15328.628 | 20539.082 | 174544.000 |
| J_simpleui_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 98723.932 | 98723.932 | 98723.932–98723.932 | 103831.426 | 316176.000 |
| J_simpleui_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 47059.467 | 47059.467 | 47059.467–47059.467 | 48150.520 | 245232.000 |
| J_simpleui_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 13268.612 | 13268.612 | 13268.612–13268.612 | 20598.960 | 172576.000 |
| J_simpleui_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 14153.456 | 14153.456 | 14153.456–14153.456 | 17649.939 | 186768.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 54398.037 | 54398.037 | 54398.037–54398.037 | 57666.561 | 264688.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 12967.519 | 12967.519 | 12967.519–12967.519 | 17949.547 | 173520.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 15428.644 | 15428.644 | 15428.644–15428.644 | 16154.127 | 184928.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 15882.655 | 15882.655 | 15882.655–15882.655 | 15927.495 | 188144.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 50548.549 | 50548.549 | 50548.549–50548.549 | 53508.020 | 265968.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 12913.362 | 12913.362 | 12913.362–12913.362 | 19930.891 | 174768.000 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 15585.044 | 15613.547 | 15573.606–15620.673 | 22378.948 | 176208.000 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 19959.095 | 20692.588 | 19938.177–20875.962 | 32969.456 | 247120.000 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 13228.731 | 13229.060 | 13127.880–13229.142 | 20272.267 | 173216.000 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 16676.181 | 16735.037 | 16672.548–16749.751 | 42015.478 | 234592.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 13017.510 | 13042.510 | 12997.100–13048.760 | 17370.198 | 168816.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 13246.994 | 13249.460 | 13210.670–13250.076 | 14231.896 | 179296.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 20271.231 | 20271.231 | 20271.231–20271.231 | 26644.981 | 210416.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 15621.759 | 15621.759 | 15621.759–15621.759 | 22388.336 | 176944.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 103370.067 | 103370.067 | 103370.067–103370.067 | 113196.188 | 473008.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 14270.915 | 14270.915 | 14270.915–14270.915 | 17799.067 | 187776.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 13478.349 | 13478.349 | 13478.349–13478.349 | 14181.614 | 175296.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 49818.571 | 49818.571 | 49818.571–49818.571 | 56143.693 | 357840.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 55174.845 | 55174.845 | 55174.845–55174.845 | 63441.438 | 248816.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 15530.106 | 15530.106 | 15530.106–15530.106 | 16933.921 | 182848.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 13339.313 | 13339.313 | 13339.313–13339.313 | 21409.572 | 172480.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 15581.149 | 15581.149 | 15581.149–15581.149 | 16448.555 | 184848.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 13163.536 | 13163.536 | 13163.536–13163.536 | 20239.869 | 174272.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 50814.724 | 50814.724 | 50814.724–50814.724 | 60778.027 | 266752.000 |
| K_vos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 8909.909 | 9015.069 | 8868.925–9041.358 | 9954.424 | 174432.000 |
| K_vos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8943.491 | 8986.876 | 8943.487–8997.722 | 9571.750 | 167712.000 |
| L_project_title_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 12044.306 | 12046.674 | 11924.817–12047.267 | 19979.076 | 173664.000 |
| L_project_title_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 12834.185 | 12835.253 | 12703.649–12835.521 | 26418.495 | 207264.000 |
| L_project_title_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 9028.927 | 9045.846 | 8983.208–9050.075 | 9645.172 | 170480.000 |
| L_project_title_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 10057.446 | 10068.346 | 10051.454–10071.071 | 19861.700 | 197712.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 8983.747 | 9184.197 | 8956.981–9234.310 | 15179.616 | 165808.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 9000.509 | 9017.499 | 8964.876–9021.747 | 9952.419 | 173744.000 |
| L_project_title_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 18009.619 | 18009.619 | 18009.619–18009.619 | 31777.794 | 224000.000 |
| L_project_title_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 11862.438 | 11862.438 | 11862.438–11862.438 | 17541.795 | 171280.000 |
| L_project_title_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 13026.880 | 13026.880 | 13026.880–13026.880 | 22976.169 | 201696.000 |
| L_project_title_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 9488.813 | 9488.813 | 9488.813–9488.813 | 10338.827 | 168368.000 |
| L_project_title_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 14283.447 | 14283.447 | 14283.447–14283.447 | 28422.489 | 219296.000 |
| L_project_title_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 9646.458 | 9646.458 | 9646.458–9646.458 | 27357.233 | 189248.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8995.837 | 8995.837 | 8995.837–8995.837 | 14128.822 | 180864.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 14393.646 | 14393.646 | 14393.646–14393.646 | 27267.773 | 212992.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 8950.903 | 8950.903 | 8950.903–8950.903 | 9439.847 | 166448.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 9063.856 | 9063.856 | 9063.856–9063.856 | 16008.297 | 165440.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 13051.037 | 13051.037 | 13051.037–13051.037 | 24880.957 | 206560.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 9039.204 | 9039.204 | 9039.204–9039.204 | 14016.225 | 179696.000 |
| A_stock | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 8257.312 | 8257.312 | 8257.312–8257.312 | 14662.819 | 164688.000 |
| A_stock | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8376.218 | 8376.218 | 8376.218–8376.218 | 9028.832 | 173168.000 |
| B_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 8606.688 | 8606.688 | 8606.688–8606.688 | 9588.264 | 167840.000 |
| B_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8684.165 | 8684.165 | 8684.165–8684.165 | 9459.325 | 176032.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 12453.101 | 12453.101 | 12453.101–12453.101 | 18244.721 | 168320.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 12652.987 | 12652.987 | 12652.987–12652.987 | 13764.679 | 175472.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 14722.349 | 14722.349 | 14722.349–14722.349 | 16755.609 | 192064.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 14227.599 | 14227.599 | 14227.599–14227.599 | 23478.693 | 177664.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 8256.290 | 8256.290 | 8256.290–8256.290 | 14328.307 | 164752.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8288.196 | 8288.196 | 8288.196–8288.196 | 8974.389 | 173232.000 |
| F_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 8980.929 | 8980.929 | 8980.929–8980.929 | 10114.534 | 174576.000 |
| F_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 8993.163 | 8993.163 | 8993.163–8993.163 | 13360.146 | 166208.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 13255.575 | 13255.575 | 13255.575–13255.575 | 13997.506 | 181968.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 12713.392 | 12713.392 | 12713.392–12713.392 | 18068.209 | 174416.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 14860.667 | 14860.667 | 14860.667–14860.667 | 16997.837 | 191632.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 14438.940 | 14438.940 | 14438.940–14438.940 | 16766.320 | 175648.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 9181.829 | 9181.829 | 9181.829–9181.829 | 10687.377 | 165312.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 9060.536 | 9060.536 | 9060.536–9060.536 | 10181.016 | 173008.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 13147.253 | 13147.253 | 13147.253–13147.253 | 14252.620 | 180416.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 13009.784 | 13009.784 | 13009.784–13009.784 | 17631.941 | 171104.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 13382.106 | 13382.106 | 13382.106–13382.106 | 14596.474 | 182912.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 13376.626 | 13376.626 | 13376.626–13376.626 | 21210.167 | 174208.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 9515.798 | 9515.798 | 9515.798–9515.798 | 10154.272 | 178320.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 9136.657 | 9136.657 | 9136.657–9136.657 | 15972.958 | 170048.000 |

## Data-derived comparisons

- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 18.064 ms vs 18.927 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 14.169 ms vs 15.748 ms (10.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 18.593 ms vs 18.959 ms (1.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.067 ms vs 14.492 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 21.633 ms vs 30.880 ms (29.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 21.143 ms vs 24.841 ms (14.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 25.665 ms vs 35.222 ms (27.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 79.741 ms vs 98.952 ms (19.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 18.293 ms vs 18.927 ms (3.3% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 15.748 ms vs 17.450 ms (9.8% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 17.672 ms vs 18.959 ms (6.8% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.492 ms vs 17.019 ms (14.9% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 10.802 ms vs 21.633 ms (50.1% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 13.997 ms vs 21.143 ms (33.8% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 10.247 ms vs 35.222 ms (70.9% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 20.793 ms vs 79.741 ms (73.9% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 8.122 ms vs 18.927 ms (57.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 8.273 ms vs 15.748 ms (47.5% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.310 ms vs 18.959 ms (56.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.236 ms vs 14.492 ms (43.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 12.081 ms vs 21.633 ms (44.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 8.425 ms vs 21.143 ms (60.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 13.039 ms vs 35.222 ms (63.0% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 8.594 ms vs 79.741 ms (89.2% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 8.431 ms vs 18.927 ms (55.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 8.765 ms vs 15.748 ms (44.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.575 ms vs 18.959 ms (54.8% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.793 ms vs 14.492 ms (39.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 8.625 ms vs 21.633 ms (60.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 8.732 ms vs 21.143 ms (58.7% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 9.171 ms vs 35.222 ms (74.0% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 9.492 ms vs 79.741 ms (88.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 18.927 ms vs 19.199 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 15.482 ms vs 15.748 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 18.959 ms vs 19.184 ms (1.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.492 ms vs 14.857 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 2000 books): 21.633 ms vs 24.280 ms (10.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 21.143 ms vs 23.340 ms (9.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 23.727 ms vs 35.222 ms (32.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 61.764 ms vs 79.741 ms (22.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 18.293 ms vs 19.569 ms (6.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 17.413 ms vs 17.450 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 17.672 ms vs 20.925 ms (15.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 17.019 ms vs 18.109 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 10.802 ms vs 13.093 ms (17.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 13.405 ms vs 13.997 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 10.247 ms vs 10.758 ms (4.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 20.793 ms vs 22.508 ms (7.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 8.122 ms vs 8.367 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, flat, 2000 books): 8.239 ms vs 8.273 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.235 ms vs 8.310 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.236 ms vs 8.256 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 2000 books): 12.019 ms vs 12.081 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 8.425 ms vs 8.601 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 13.039 ms vs 13.066 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 8.594 ms vs 8.686 ms (1.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 19.199 ms vs 20.031 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 15.482 ms vs 15.534 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 19.121 ms vs 19.184 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 14.688 ms vs 14.857 ms (1.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 2000 books): 21.819 ms vs 24.280 ms (10.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 23.340 ms vs 23.459 ms (0.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 23.727 ms vs 24.822 ms (4.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 56.775 ms vs 61.764 ms (8.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, flat, 2000 books): 17.776 ms vs 18.293 ms (2.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 16.986 ms vs 17.450 ms (2.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (paging, hierarchical, 2000 books): 13.423 ms vs 17.672 ms (24.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.753 ms vs 17.019 ms (19.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 10.802 ms vs 15.191 ms (28.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 13.997 ms vs 16.782 ms (16.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 10.247 ms vs 12.636 ms (18.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 16.183 ms vs 20.793 ms (22.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, flat, 2000 books): 15.396 ms vs 17.776 ms (13.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (paging, flat, 2000 books): 16.355 ms vs 16.986 ms (3.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 13.423 ms vs 19.500 ms (31.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.753 ms vs 16.754 ms (17.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 2000 books): 12.374 ms vs 15.191 ms (18.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 13.506 ms vs 16.782 ms (19.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 12.636 ms vs 14.142 ms (10.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 16.183 ms vs 17.574 ms (7.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (paging, flat, 2000 books): 8.431 ms vs 8.915 ms (5.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (paging, flat, 2000 books): 8.765 ms vs 9.325 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 8.575 ms vs 9.056 ms (5.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 8.793 ms vs 9.167 ms (4.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 2000 books): 8.004 ms vs 8.625 ms (7.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 2000 books): 7.992 ms vs 8.732 ms (8.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 50 books): 9.171 ms vs 9.270 ms (1.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 50 books): 9.492 ms vs 9.903 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
