# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `b7aa678f5eef72bc810dedd92ebabb1d9973e5a3d10230e9401af28e1a995ad4`
Reader flash setting: `unset`

Aggregated rows: 1782; PASS=1636; FAILED=0; UNSUPPORTED=146; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | paging | flat | 2000 | 10 | 201.000 | 3/3 | 90/90 | 21.806 | 36.291 | 17.088 | 43.180 | 26.831 | 40.754 | 19.320 | 45.260 |
| A_stock | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 19.381 | 30.284 | 15.397 | 37.057 | 26.566 | 39.538 | 18.381 | 45.662 |
| A_stock | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 25.764 | 61.058 | 18.817 | 68.003 | 27.883 | 68.012 | 17.452 | 78.159 |
| A_stock | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 42.397 | 45.459 | 10.492 | 46.968 | 56.113 | 92.664 | 17.484 | 136.873 |
| A_stock | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| A_stock | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | paging | flat | 2000 | 10 | 201.000 | 3/3 | 90/90 | 21.235 | 36.135 | 17.057 | 41.766 | 26.095 | 41.241 | 18.790 | 57.747 |
| B_bookshelf | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 20.114 | 31.503 | 16.193 | 36.610 | 27.421 | 39.605 | 19.909 | 48.305 |
| B_bookshelf | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 24.727 | 70.353 | 18.231 | 76.365 | 29.710 | 79.595 | 17.798 | 82.745 |
| B_bookshelf | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 60.424 | 69.758 | 26.792 | 70.688 | 34.068 | 80.393 | 20.443 | 99.786 |
| B_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | paging | flat | 2000 | 8 | 251.000 | 3/3 | 90/90 | 23.477 | 39.865 | 11.509 | 51.250 | 24.283 | 42.493 | 13.766 | 54.728 |
| C_simpleui | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 21.422 | 36.672 | 12.277 | 42.356 | 21.083 | 36.599 | 12.642 | 45.464 |
| C_simpleui | warm | flat | 2000 | 8 | 251.000 | 1/1 | 30/30 | 16.837 | 39.206 | 11.570 | 51.065 | 14.708 | 37.233 | 10.129 | 50.835 |
| C_simpleui | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 26.532 | 35.060 | 16.057 | 39.139 | 19.282 | 33.452 | 14.417 | 40.545 |
| C_simpleui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | paging | flat | 2000 | 5 | 400.000 | 3/3 | 90/90 | 12.011 | 31.640 | 7.981 | 46.512 | 11.131 | 30.696 | 7.798 | 35.881 |
| D_zenos | paging | hierarchical | 2000 | 5 | 33.000 | 3/3 | 90/90 | 11.687 | 26.047 | 8.071 | 33.701 | 11.259 | 26.759 | 7.693 | 31.477 |
| D_zenos | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 11.043 | 33.188 | 8.192 | 37.376 | 18.004 | 39.327 | 8.488 | 42.511 |
| D_zenos | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 12.333 | 16.992 | 9.914 | 27.534 | 18.129 | 28.505 | 10.026 | 41.225 |
| D_zenos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 13.518 | 15.912 | 10.404 | 21.547 | 13.338 | 15.714 | 10.279 | 19.952 |
| E_project_title | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 13.395 | 14.598 | 10.484 | 16.790 | 12.983 | 15.499 | 9.552 | 20.479 |
| E_project_title | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 12.988 | 14.756 | 11.068 | 18.616 | 12.708 | 14.836 | 10.199 | 18.853 |
| E_project_title | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 7.972 | 8.619 | 7.106 | 8.781 | 7.548 | 7.991 | 6.555 | 10.586 |
| E_project_title | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | paging | flat | 2000 | 10 | 200.000 | 3/3 | 90/90 | 21.628 | 38.270 | 16.889 | 42.971 | 27.641 | 43.985 | 21.134 | 52.837 |
| F_vos | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 21.056 | 30.636 | 16.416 | 37.563 | 27.026 | 40.797 | 20.120 | 46.169 |
| F_vos | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 24.586 | 50.826 | 19.825 | 52.707 | 25.135 | 54.089 | 17.500 | 55.751 |
| F_vos | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 61.745 | 79.025 | 59.849 | 85.856 | 26.785 | 51.433 | 18.424 | 71.336 |
| F_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | paging | flat | 2000 | 8 | 251.000 | 3/3 | 90/90 | 23.400 | 43.503 | 17.058 | 49.697 | 27.189 | 47.913 | 19.107 | 56.271 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 23.370 | 36.446 | 19.543 | 44.806 | 26.022 | 42.336 | 14.855 | 51.894 |
| G_simpleui_bookshelf | warm | flat | 2000 | 8 | 251.000 | 1/1 | 30/30 | 22.542 | 49.834 | 17.932 | 56.528 | 22.923 | 45.719 | 14.232 | 51.228 |
| G_simpleui_bookshelf | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 17.090 | 27.639 | 11.025 | 35.278 | 14.200 | 33.145 | 8.256 | 34.052 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | paging | flat | 2000 | 5 | 400.000 | 3/3 | 90/90 | 11.994 | 30.311 | 8.191 | 33.579 | 11.218 | 32.084 | 7.625 | 37.251 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | 5 | 33.000 | 3/3 | 90/90 | 11.244 | 24.778 | 8.109 | 31.735 | 10.985 | 25.045 | 8.148 | 28.823 |
| H_zenos_bookshelf | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 10.639 | 31.942 | 7.906 | 35.671 | 16.718 | 39.524 | 9.359 | 44.378 |
| H_zenos_bookshelf | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 11.864 | 29.851 | 10.246 | 32.766 | 17.261 | 33.238 | 9.266 | 38.863 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | paging | flat | 2000 | 10 | 200.000 | 3/3 | 90/90 | 21.080 | 35.510 | 10.782 | 43.108 | 25.069 | 40.398 | 10.985 | 49.048 |
| I_vos_bookshelf | paging | hierarchical | 2000 | 10 | 17.000 | 3/3 | 48/90 | 19.209 | 27.305 | 11.598 | 36.013 | 25.924 | 38.636 | 12.915 | 49.399 |
| I_vos_bookshelf | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 26.547 | 55.474 | 19.398 | 61.734 | 27.819 | 53.949 | 16.985 | 63.676 |
| I_vos_bookshelf | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 46.890 | 99.570 | 11.808 | 110.135 | 18.474 | 40.176 | 13.189 | 54.804 |
| I_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | paging | flat | 2000 | 8 | 250.000 | 3/3 | 90/90 | 23.450 | 43.334 | 18.402 | 49.517 | 27.807 | 48.224 | 14.993 | 56.656 |
| J_simpleui_vos | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 21.115 | 37.475 | 12.565 | 46.098 | 22.084 | 36.915 | 14.323 | 53.082 |
| J_simpleui_vos | warm | flat | 2000 | 8 | 250.000 | 1/1 | 30/30 | 15.892 | 42.644 | 11.568 | 48.027 | 13.242 | 39.427 | 7.923 | 42.518 |
| J_simpleui_vos | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 21.740 | 34.638 | 18.211 | 45.144 | 19.279 | 39.211 | 13.591 | 50.083 |
| J_simpleui_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | 8 | 250.000 | 3/3 | 90/90 | 23.927 | 43.737 | 18.609 | 54.110 | 27.125 | 48.655 | 19.426 | 54.425 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | 8 | 21.000 | 3/3 | 60/90 | 21.443 | 39.806 | 11.289 | 43.303 | 21.956 | 39.562 | 12.413 | 49.077 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | 8 | 250.000 | 1/1 | 30/30 | 26.008 | 55.826 | 16.542 | 66.908 | 25.473 | 62.897 | 15.283 | 67.034 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 15.346 | 29.126 | 12.772 | 37.203 | 13.125 | 32.591 | 9.962 | 33.499 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 12.816 | 15.112 | 9.202 | 19.378 | 12.300 | 14.927 | 9.512 | 20.701 |
| L_project_title_vos | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 13.069 | 14.952 | 10.143 | 17.508 | 12.319 | 14.929 | 9.727 | 19.425 |
| L_project_title_vos | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 13.106 | 14.509 | 10.465 | 19.574 | 12.527 | 13.942 | 10.862 | 20.158 |
| L_project_title_vos | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 13.506 | 13.928 | 10.020 | 14.034 | 12.840 | 14.871 | 10.333 | 18.061 |
| L_project_title_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| M_leanui | paging | flat | 2000 | 14 | 143.000 | 3/3 | 90/90 | 13.752 | 15.504 | 9.750 | 18.718 | 12.894 | 15.231 | 10.181 | 20.241 |
| M_leanui | paging | hierarchical | 2000 | 14 | 12.000 | 3/3 | 33/90 | 13.147 | 15.171 | 10.345 | 16.303 | 12.724 | 14.644 | 10.399 | 20.935 |
| M_leanui | warm | flat | 2000 | 14 | 143.000 | 1/1 | 30/30 | 7.495 | 8.103 | 6.505 | 9.153 | 7.385 | 8.290 | 6.983 | 8.554 |
| M_leanui | warm | flat | 50 | 14 | 4.000 | 1/1 | 3/30 | 7.920 | 8.413 | 7.528 | 8.536 | 7.579 | 9.401 | 6.508 | 11.244 |
| M_leanui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| M_leanui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| B_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 95.289 | 101.830 | 87.284 | 171.667 | 87.739 | 95.811 | 72.587 | 107.826 |
| B_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 35.587 | 41.031 | 25.151 | 50.924 | 28.907 | 39.161 | 13.881 | 61.625 |
| B_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 97.884 | 106.626 | 83.262 | 130.094 | 92.046 | 97.518 | 84.546 | 107.867 |
| B_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 34.816 | 43.513 | 23.993 | 46.831 | 32.281 | 38.104 | 25.563 | 49.193 |
| B_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 103.850 | 126.255 | 73.511 | 168.923 | 77.070 | 99.856 | 71.789 | 118.204 |
| B_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 52.578 | 67.479 | 13.621 | 79.739 | 15.741 | 25.139 | 13.211 | 33.070 |
| B_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 80.275 | 90.204 | 66.364 | 92.049 | 70.767 | 80.714 | 65.905 | 100.999 |
| B_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 11.041 | 14.864 | 8.821 | 18.300 | 11.780 | 18.838 | 7.740 | 29.954 |
| B_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| B_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 93.865 | 100.833 | 86.234 | 122.611 | 80.772 | 89.599 | 75.800 | 107.991 |
| G_simpleui_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 32.740 | 42.728 | 19.697 | 58.898 | 22.334 | 35.438 | 16.972 | 64.022 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 94.718 | 102.270 | 83.884 | 122.431 | 82.816 | 91.652 | 76.988 | 100.959 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 33.084 | 41.386 | 21.592 | 48.026 | 23.450 | 31.964 | 18.396 | 42.565 |
| G_simpleui_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 126.005 | 135.835 | 97.860 | 336.800 | 87.287 | 110.633 | 72.348 | 304.568 |
| G_simpleui_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 57.462 | 67.411 | 20.006 | 251.768 | 19.236 | 21.537 | 14.813 | 181.080 |
| G_simpleui_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 104.067 | 113.212 | 83.924 | 120.299 | 92.567 | 103.215 | 83.683 | 138.148 |
| G_simpleui_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 36.022 | 46.697 | 10.162 | 47.344 | 31.075 | 45.519 | 26.005 | 82.186 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 97.130 | 107.122 | 85.152 | 166.122 | 76.661 | 97.406 | 72.219 | 103.362 |
| H_zenos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 32.862 | 41.725 | 14.915 | 64.021 | 16.791 | 27.097 | 12.548 | 37.269 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 99.781 | 113.690 | 79.245 | 137.113 | 74.933 | 94.220 | 71.275 | 101.808 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 33.915 | 43.036 | 15.940 | 53.048 | 15.605 | 21.191 | 12.395 | 34.021 |
| H_zenos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 75.831 | 96.193 | 71.320 | 124.492 | 72.401 | 83.982 | 65.876 | 109.108 |
| H_zenos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 12.909 | 31.195 | 9.633 | 58.590 | 10.347 | 20.219 | 6.884 | 47.684 |
| H_zenos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 79.943 | 92.969 | 68.312 | 98.495 | 73.131 | 87.029 | 66.400 | 104.209 |
| H_zenos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 27.902 | 36.913 | 8.285 | 38.754 | 9.930 | 20.916 | 7.099 | 45.903 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 89.030 | 98.447 | 69.968 | 186.009 | 79.856 | 91.870 | 67.258 | 104.435 |
| I_vos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 28.098 | 37.154 | 9.826 | 49.745 | 19.483 | 29.582 | 7.922 | 35.995 |
| I_vos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 90.349 | 102.957 | 68.369 | 127.202 | 85.185 | 94.931 | 67.261 | 108.727 |
| I_vos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 29.468 | 37.549 | 7.614 | 50.286 | 25.279 | 38.155 | 7.029 | 45.395 |
| I_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 77.098 | 100.685 | 70.548 | 157.357 | 76.142 | 93.055 | 65.494 | 100.366 |
| I_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 28.353 | 42.627 | 8.506 | 60.417 | 7.970 | 11.024 | 5.783 | 24.088 |
| I_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 76.429 | 86.068 | 68.127 | 89.753 | 73.740 | 92.019 | 66.547 | 95.087 |
| I_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 23.245 | 34.553 | 8.649 | 40.615 | 7.557 | 13.807 | 5.688 | 25.281 |
| I_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | default (medium) | 8 | 250.000 | 3/3 | 90/90 | 90.829 | 101.667 | 83.231 | 117.638 | 79.419 | 88.516 | 74.149 | 104.813 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | off | 8 | 250.000 | 3/3 | 90/90 | 29.996 | 36.323 | 18.390 | 47.401 | 20.307 | 28.898 | 16.288 | 43.920 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | default (medium) | 8 | 21.000 | 3/3 | 60/90 | 91.632 | 101.823 | 69.939 | 131.386 | 81.162 | 89.641 | 66.218 | 103.812 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | off | 8 | 21.000 | 3/3 | 60/90 | 30.206 | 36.685 | 8.700 | 48.021 | 22.963 | 29.231 | 7.384 | 44.704 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 95.546 | 111.743 | 69.923 | 251.958 | 79.338 | 101.907 | 66.690 | 250.829 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 38.123 | 45.398 | 10.408 | 208.916 | 8.555 | 11.217 | 7.316 | 145.482 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 81.486 | 93.936 | 67.657 | 95.977 | 70.924 | 84.391 | 66.959 | 138.850 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 10.212 | 12.287 | 7.712 | 13.982 | 9.242 | 17.744 | 7.706 | 84.470 |
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

## Comparative Findings

- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 26.095 ms vs 26.831 ms (2.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 21.235 ms vs 21.806 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 26.566 ms vs 27.421 ms (3.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.381 ms vs 20.114 ms (3.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 27.883 ms vs 29.710 ms (6.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 24.727 ms vs 25.764 ms (4.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 34.068 ms vs 56.113 ms (39.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 42.397 ms vs 60.424 ms (29.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 24.283 ms vs 26.831 ms (9.5% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 21.806 ms vs 23.477 ms (7.1% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.083 ms vs 26.566 ms (20.6% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.381 ms vs 21.422 ms (9.5% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 14.708 ms vs 27.883 ms (47.3% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.837 ms vs 25.764 ms (34.7% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 19.282 ms vs 56.113 ms (65.6% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 26.532 ms vs 42.397 ms (37.4% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 11.131 ms vs 26.831 ms (58.5% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 12.011 ms vs 21.806 ms (44.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 11.259 ms vs 26.566 ms (57.6% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 11.687 ms vs 19.381 ms (39.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 18.004 ms vs 27.883 ms (35.4% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 11.043 ms vs 25.764 ms (57.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 18.129 ms vs 56.113 ms (67.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 12.333 ms vs 42.397 ms (70.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 13.338 ms vs 26.831 ms (50.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 13.518 ms vs 21.806 ms (38.0% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 12.983 ms vs 26.566 ms (51.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.395 ms vs 19.381 ms (30.9% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 12.708 ms vs 27.883 ms (54.4% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 12.988 ms vs 25.764 ms (49.6% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 7.548 ms vs 56.113 ms (86.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 7.972 ms vs 42.397 ms (81.2% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 26.831 ms vs 27.641 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 21.628 ms vs 21.806 ms (0.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 26.566 ms vs 27.026 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.381 ms vs 21.056 ms (8.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 25.135 ms vs 27.883 ms (9.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 24.586 ms vs 25.764 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 26.785 ms vs 56.113 ms (52.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 42.397 ms vs 61.745 ms (31.3% lower).
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 24.283 ms vs 27.189 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 23.400 ms vs 23.477 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.083 ms vs 26.022 ms (19.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 21.422 ms vs 23.370 ms (8.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 14.708 ms vs 22.923 ms (35.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 16.837 ms vs 22.542 ms (25.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 14.200 ms vs 19.282 ms (26.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 17.090 ms vs 26.532 ms (35.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 11.131 ms vs 11.218 ms (0.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, flat, 2000 books): 11.994 ms vs 12.011 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (paging, hierarchical, 2000 books): 10.985 ms vs 11.259 ms (2.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 11.244 ms vs 11.687 ms (3.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 2000 books): 16.718 ms vs 18.004 ms (7.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 2000 books): 10.639 ms vs 11.043 ms (3.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 17.261 ms vs 18.129 ms (4.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 50 books): 11.864 ms vs 12.333 ms (3.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 25.069 ms vs 27.641 ms (9.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, flat, 2000 books): 21.080 ms vs 21.628 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 25.924 ms vs 27.026 ms (4.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.209 ms vs 21.056 ms (8.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 25.135 ms vs 27.819 ms (9.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 24.586 ms vs 26.547 ms (7.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 18.474 ms vs 26.785 ms (31.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 46.890 ms vs 61.745 ms (24.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, flat, 2000 books): 24.283 ms vs 27.807 ms (12.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 23.450 ms vs 23.477 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.083 ms vs 22.084 ms (4.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 21.115 ms vs 21.422 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 2000 books): 13.242 ms vs 14.708 ms (10.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 15.892 ms vs 16.837 ms (5.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 19.279 ms vs 19.282 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 21.740 ms vs 26.532 ms (18.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, flat, 2000 books): 27.125 ms vs 27.807 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 23.450 ms vs 23.927 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.956 ms vs 22.084 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 21.115 ms vs 21.443 ms (1.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.242 ms vs 25.473 ms (48.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 15.892 ms vs 26.008 ms (38.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 13.125 ms vs 19.279 ms (31.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 15.346 ms vs 21.740 ms (29.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, flat, 2000 books): 12.300 ms vs 13.338 ms (7.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (paging, flat, 2000 books): 12.816 ms vs 13.518 ms (5.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, hierarchical, 2000 books): 12.319 ms vs 12.983 ms (5.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.069 ms vs 13.395 ms (2.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 2000 books): 12.527 ms vs 12.708 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 2000 books): 12.988 ms vs 13.106 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 50 books): 7.548 ms vs 12.840 ms (41.2% lower).
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 50 books): 7.972 ms vs 13.506 ms (41.0% lower).

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 13.102 | 12.992 | 14.350 | 12.965–14.662 |
| A_stock | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.634 | 11.051 | 13.306 | 10.905–13.724 |
| A_stock | paging | flat | 2000 | library_cached_paging | PASS | 90 | 26.831 | 22.506 | 40.754 | 19.320–45.260 |
| A_stock | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 21.806 | 18.899 | 36.291 | 17.088–43.180 |
| A_stock | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 21.096 | 20.935 | 31.792 | 20.895–34.466 |
| A_stock | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 26.566 | 20.957 | 39.538 | 18.381–45.662 |
| A_stock | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 19.381 | 17.463 | 30.284 | 15.397–37.057 |
| A_stock | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 30.489 | 30.092 | 33.119 | 29.993–33.776 |
| A_stock | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.174 | 10.436 | 12.829 | 10.001–12.993 |
| A_stock | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.605 | 11.354 | 12.027 | 11.291–12.133 |
| A_stock | warm | flat | 2000 | change_sort_mode | PASS | 10 | 125.043 | 121.348 | 179.479 | 111.182–180.969 |
| A_stock | warm | flat | 2000 | close_book | PASS | 10 | 68.505 | 65.476 | 76.781 | 65.176–76.845 |
| A_stock | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.308 | 7.558 | 8.774 | 7.508–9.192 |
| A_stock | warm | flat | 2000 | home_to_library | PASS | 10 | 110.778 | 81.498 | 135.220 | 69.052–148.633 |
| A_stock | warm | flat | 2000 | library_cached_paging | PASS | 30 | 27.883 | 19.067 | 68.012 | 17.452–78.159 |
| A_stock | warm | flat | 2000 | library_first_render | PASS | 10 | 67.620 | 62.904 | 118.658 | 62.118–154.752 |
| A_stock | warm | flat | 2000 | library_folder_back | PASS | 10 | 154.257 | 117.758 | 157.312 | 113.397–157.488 |
| A_stock | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.552 | 7.629 | 9.367 | 7.592–9.393 |
| A_stock | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 25.764 | 22.456 | 61.058 | 18.817–68.003 |
| A_stock | warm | flat | 2000 | open_book | PASS | 10 | 94.878 | 91.405 | 100.226 | 81.501–100.806 |
| A_stock | warm | flat | 2000 | open_book_minimal | PASS | 10 | 122.118 | 113.024 | 130.169 | 111.094–133.134 |
| A_stock | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.466 | 8.093 | 8.869 | 8.081–8.987 |
| A_stock | warm | flat | 2000 | repeated_nav | PASS | 2 | 368.017 | 347.685 | 388.349 | 342.602–393.432 |
| A_stock | warm | flat | 50 | change_sort_mode | PASS | 10 | 54.420 | 35.259 | 63.832 | 34.699–64.189 |
| A_stock | warm | flat | 50 | close_book | PASS | 10 | 42.080 | 37.820 | 61.433 | 36.890–64.303 |
| A_stock | warm | flat | 50 | close_quick_settings | PASS | 10 | 12.488 | 10.372 | 14.445 | 10.223–14.737 |
| A_stock | warm | flat | 50 | home_to_library | PASS | 10 | 29.465 | 27.493 | 43.503 | 25.886–49.937 |
| A_stock | warm | flat | 50 | library_cached_paging | PASS | 30 | 56.113 | 26.567 | 92.664 | 17.484–136.873 |
| A_stock | warm | flat | 50 | library_first_render | PASS | 10 | 67.573 | 27.700 | 100.442 | 27.006–128.509 |
| A_stock | warm | flat | 50 | library_folder_back | PASS | 10 | 58.447 | 44.227 | 61.908 | 42.649–63.794 |
| A_stock | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.201 | 6.907 | 9.275 | 6.727–9.296 |
| A_stock | warm | flat | 50 | library_sequential_paging | PASS | 5 | 42.397 | 15.768 | 45.459 | 10.492–46.968 |
| A_stock | warm | flat | 50 | open_book | PASS | 10 | 55.403 | 43.072 | 68.966 | 42.433–69.908 |
| A_stock | warm | flat | 50 | open_book_minimal | PASS | 10 | 55.620 | 47.324 | 67.812 | 46.807–71.750 |
| A_stock | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.630 | 7.659 | 9.280 | 6.021–9.547 |
| A_stock | warm | flat | 50 | repeated_nav | PASS | 2 | 317.836 | 301.838 | 333.833 | 297.839–337.832 |
| A_stock | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.973 | 8.544 | 13.814 | 8.337–34.556 |
| A_stock | warm | hierarchical | 2000 | close_book | PASS | 10 | 56.514 | 35.887 | 76.670 | 35.090–77.289 |
| A_stock | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.623 | 7.729 | 9.215 | 7.417–9.538 |
| A_stock | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 12.887 | 12.078 | 22.877 | 10.343–24.128 |
| A_stock | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 12.710 | 11.614 | 19.727 | 11.563–20.983 |
| A_stock | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 19.237 | 14.958 | 36.908 | 14.441–64.444 |
| A_stock | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 23.001 | 17.976 | 27.129 | 8.574–33.866 |
| A_stock | warm | hierarchical | 2000 | open_book | PASS | 10 | 61.909 | 54.227 | 70.309 | 51.958–85.434 |
| A_stock | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 56.782 | 50.314 | 71.256 | 49.387–74.015 |
| A_stock | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.129 | 7.384 | 8.740 | 6.519–9.171 |
| A_stock | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 9.002 | 8.161 | 18.789 | 8.136–20.307 |
| A_stock | warm | hierarchical | 50 | close_book | PASS | 10 | 23.164 | 20.015 | 31.223 | 19.874–47.767 |
| A_stock | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.496 | 8.121 | 13.978 | 7.768–58.639 |
| A_stock | warm | hierarchical | 50 | home_to_library | PASS | 10 | 11.812 | 11.215 | 20.641 | 11.156–23.823 |
| A_stock | warm | hierarchical | 50 | library_first_render | PASS | 10 | 12.927 | 11.641 | 20.566 | 11.542–20.645 |
| A_stock | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 18.615 | 14.438 | 30.345 | 13.519–30.693 |
| A_stock | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 12.482 | 7.025 | 16.480 | 6.931–16.570 |
| A_stock | warm | hierarchical | 50 | open_book | PASS | 10 | 54.349 | 43.698 | 65.750 | 42.383–66.262 |
| A_stock | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 59.648 | 52.152 | 63.087 | 40.702–63.492 |
| A_stock | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.296 | 7.485 | 10.193 | 7.371–21.322 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 13.951 | 13.682 | 14.263 | 13.615–14.341 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.521 | 11.297 | 12.295 | 11.241–12.489 |
| B_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 87.739 | 74.568 | 95.811 | 72.587–107.826 |
| B_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 28.907 | 15.919 | 39.161 | 13.881–61.625 |
| B_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 95.289 | 90.658 | 101.830 | 87.284–171.667 |
| B_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 35.587 | 28.988 | 41.031 | 25.151–50.924 |
| B_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 14.102 | 12.161 | 17.988 | 11.676–18.960 |
| B_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 26.095 | 22.824 | 41.241 | 18.790–57.747 |
| B_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 21.235 | 18.955 | 36.135 | 17.057–41.766 |
| B_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 217.356 | 207.678 | 222.689 | 205.259–224.022 |
| B_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 36.062 | 22.832 | 36.607 | 19.525–36.743 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 92.046 | 88.003 | 97.518 | 84.546–107.867 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 32.281 | 28.296 | 38.104 | 25.563–49.193 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 97.884 | 89.684 | 106.626 | 83.262–130.094 |
| B_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 34.816 | 27.789 | 43.513 | 23.993–46.831 |
| B_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 14.007 | 13.794 | 17.867 | 13.741–18.832 |
| B_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 27.421 | 22.785 | 39.605 | 19.909–48.305 |
| B_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 20.114 | 17.805 | 31.503 | 16.193–36.610 |
| B_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 144.537 | 143.326 | 148.018 | 143.023–148.888 |
| B_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 29.161 | 28.053 | 30.827 | 27.776–31.243 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 11.295 | 10.651 | 11.497 | 10.490–11.547 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.240 | 9.614 | 11.603 | 9.208–11.694 |
| B_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 77.070 | 73.220 | 99.856 | 71.789–118.204 |
| B_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 15.741 | 13.650 | 25.139 | 13.211–33.070 |
| B_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 15.622 | 11.288 | 40.542 | 10.814–45.167 |
| B_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 103.850 | 74.909 | 126.255 | 73.511–168.923 |
| B_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 52.578 | 39.716 | 67.479 | 13.621–79.739 |
| B_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 131.127 | 116.713 | 186.257 | 115.916–188.434 |
| B_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 68.330 | 62.899 | 70.000 | 62.189–74.883 |
| B_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 10.315 | 8.881 | 11.151 | 8.663–11.189 |
| B_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 12.486 | 11.462 | 13.000 | 10.095–13.789 |
| B_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 107.541 | 81.930 | 131.068 | 77.399–147.918 |
| B_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 29.710 | 19.946 | 79.595 | 17.798–82.745 |
| B_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 83.810 | 68.452 | 180.834 | 66.801–181.421 |
| B_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 154.478 | 117.132 | 162.529 | 115.669–167.000 |
| B_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.999 | 7.230 | 47.963 | 6.750–58.656 |
| B_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 24.727 | 22.830 | 70.353 | 18.231–76.365 |
| B_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 112.960 | 105.488 | 121.767 | 99.940–123.483 |
| B_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 121.605 | 119.353 | 126.834 | 116.644–127.057 |
| B_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 15.150 | 12.754 | 19.270 | 11.729–21.948 |
| B_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 9.180 | 8.397 | 9.368 | 8.390–9.371 |
| B_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 341.438 | 336.942 | 345.934 | 335.818–347.058 |
| B_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 70.767 | 66.986 | 80.714 | 65.905–100.999 |
| B_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 11.780 | 8.868 | 18.838 | 7.740–29.954 |
| B_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 11.123 | 10.413 | 29.704 | 10.245–37.328 |
| B_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 80.275 | 71.072 | 90.204 | 66.364–92.049 |
| B_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 11.041 | 9.712 | 14.864 | 8.821–18.300 |
| B_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 57.029 | 37.020 | 74.001 | 36.975–80.325 |
| B_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 34.553 | 27.874 | 61.345 | 27.111–70.864 |
| B_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 7.980 | 7.617 | 8.769 | 7.558–9.206 |
| B_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.130 | 7.866 | 9.032 | 7.752–9.253 |
| B_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 31.015 | 26.944 | 52.678 | 26.460–54.909 |
| B_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 34.068 | 25.338 | 80.393 | 20.443–99.786 |
| B_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 69.573 | 31.181 | 88.076 | 25.914–116.224 |
| B_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 59.311 | 43.963 | 62.854 | 43.794–62.873 |
| B_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 13.058 | 7.702 | 71.548 | 7.265–77.198 |
| B_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 60.424 | 32.843 | 69.758 | 26.792–70.688 |
| B_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 63.041 | 41.499 | 71.696 | 38.521–73.511 |
| B_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 60.986 | 50.761 | 67.407 | 50.558–72.122 |
| B_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.939 | 11.345 | 32.968 | 10.782–34.315 |
| B_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.689 | 8.399 | 8.883 | 8.360–8.885 |
| B_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 279.646 | 268.789 | 290.503 | 266.075–293.217 |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.746 | 11.818 | 31.131 | 11.284–41.748 |
| B_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 10.404 | 9.790 | 30.894 | 8.324–46.971 |
| B_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 32.236 | 24.216 | 57.632 | 23.351–65.235 |
| B_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.325 | 7.844 | 8.819 | 7.367–9.025 |
| B_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.055 | 7.602 | 8.322 | 6.950–8.816 |
| B_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 12.140 | 11.378 | 20.982 | 10.605–22.580 |
| B_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 12.810 | 11.283 | 20.010 | 11.123–21.701 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 20.524 | 17.911 | 39.455 | 17.531–45.439 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 22.811 | 19.788 | 38.036 | 6.681–40.291 |
| B_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 64.254 | 51.304 | 77.758 | 48.512–78.186 |
| B_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 74.328 | 53.509 | 78.864 | 51.391–79.151 |
| B_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 13.878 | 12.866 | 25.239 | 12.115–46.706 |
| B_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 7.990 | 7.643 | 8.588 | 7.548–8.732 |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 14.046 | 11.459 | 29.118 | 11.431–34.833 |
| B_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 9.633 | 8.683 | 20.116 | 8.656–20.893 |
| B_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 24.998 | 19.385 | 35.034 | 18.120–43.833 |
| B_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 8.323 | 7.879 | 8.723 | 7.334–8.828 |
| B_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.329 | 7.779 | 8.938 | 7.239–9.165 |
| B_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 11.730 | 10.499 | 20.662 | 10.470–24.154 |
| B_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 11.715 | 10.863 | 19.420 | 10.654–19.905 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 17.550 | 15.257 | 27.082 | 15.037–28.383 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.079 | 7.799 | 19.017 | 6.389–29.215 |
| B_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 62.835 | 60.697 | 69.705 | 59.082–72.187 |
| B_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 63.430 | 52.108 | 73.764 | 49.620–78.361 |
| B_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 15.047 | 12.627 | 37.164 | 12.583–67.895 |
| B_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.184 | 8.035 | 8.582 | 7.923–8.839 |
| C_simpleui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.470 | 12.131 | 12.965 | 12.046–13.089 |
| C_simpleui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 31.342 | 29.298 | 32.740 | 28.787–33.090 |
| C_simpleui | paging | flat | 2000 | library_cached_paging | PASS | 90 | 24.283 | 17.426 | 42.493 | 13.766–54.728 |
| C_simpleui | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 23.477 | 15.877 | 39.865 | 11.509–51.250 |
| C_simpleui | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 35.968 | 15.870 | 37.467 | 10.845–37.842 |
| C_simpleui | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 21.083 | 16.469 | 36.599 | 12.642–45.464 |
| C_simpleui | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 21.422 | 16.637 | 36.672 | 12.277–42.356 |
| C_simpleui | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 32.847 | 17.637 | 34.478 | 13.834–34.886 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.981 | 11.965 | 14.217 | 11.711–14.526 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 30.246 | 29.616 | 31.078 | 29.459–31.286 |
| C_simpleui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 119.204 | 92.863 | 153.251 | 89.295–154.619 |
| C_simpleui | warm | flat | 2000 | close_book | PASS | 10 | 150.146 | 139.055 | 250.794 | 138.212–286.810 |
| C_simpleui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.368 | 8.135 | 8.527 | 8.032–8.692 |
| C_simpleui | warm | flat | 2000 | home_to_library | PASS | 10 | 11.446 | 10.803 | 14.055 | 10.305–28.397 |
| C_simpleui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 14.708 | 10.496 | 37.233 | 10.129–50.835 |
| C_simpleui | warm | flat | 2000 | library_first_render | PASS | 10 | 88.990 | 68.539 | 102.102 | 67.788–103.641 |
| C_simpleui | warm | flat | 2000 | library_folder_back | PASS | 10 | 118.819 | 98.603 | 124.347 | 96.190–127.941 |
| C_simpleui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.648 | 8.993 | 14.970 | 8.809–33.854 |
| C_simpleui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.837 | 12.664 | 39.206 | 11.570–51.065 |
| C_simpleui | warm | flat | 2000 | open_book | PASS | 10 | 183.342 | 166.314 | 213.840 | 153.895–396.147 |
| C_simpleui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 91.121 | 81.721 | 109.610 | 71.042–122.643 |
| C_simpleui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 15.392 | 12.489 | 68.397 | 12.395–443.218 |
| C_simpleui | warm | flat | 2000 | repeated_nav | PASS | 2 | 783.101 | 721.922 | 844.281 | 706.627–859.576 |
| C_simpleui | warm | flat | 2000 | start_to_home | PASS | 10 | 17.264 | 9.802 | 28.618 | 9.364–32.593 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 10 | 77.249 | 50.928 | 121.188 | 47.976–385.918 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 10 | 87.178 | 58.409 | 160.886 | 45.019–188.036 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.809 | 7.893 | 11.591 | 7.627–11.635 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 10 | 21.072 | 19.300 | 24.594 | 18.598–32.946 |
| C_simpleui | warm | flat | 50 | library_cached_paging | PASS | 30 | 19.282 | 15.967 | 33.452 | 14.417–40.545 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 10 | 61.413 | 48.657 | 67.325 | 47.728–68.720 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 10 | 39.433 | 29.001 | 49.500 | 28.942–52.493 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 10 | 19.398 | 15.881 | 27.603 | 15.574–30.754 |
| C_simpleui | warm | flat | 50 | library_sequential_paging | PASS | 6 | 26.532 | 18.281 | 35.060 | 16.057–39.139 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 10 | 122.069 | 75.206 | 175.485 | 71.008–199.249 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 10 | 88.921 | 82.576 | 98.884 | 62.930–101.338 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 10 | 15.216 | 13.375 | 115.810 | 13.025–123.077 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 2 | 437.233 | 410.197 | 464.270 | 403.438–471.029 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 10 | 11.530 | 9.870 | 22.851 | 8.790–27.767 |
| C_simpleui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 14.636 | 12.670 | 34.090 | 11.221–38.790 |
| C_simpleui | warm | hierarchical | 2000 | close_book | PASS | 10 | 64.968 | 53.721 | 182.166 | 43.849–209.187 |
| C_simpleui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.607 | 7.571 | 8.673 | 6.836–8.757 |
| C_simpleui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 11.761 | 10.359 | 13.509 | 10.243–22.326 |
| C_simpleui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 36.120 | 27.516 | 43.627 | 25.022–47.176 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 18.739 | 14.094 | 41.463 | 13.343–42.675 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 37.451 | 21.752 | 49.592 | 11.937–53.868 |
| C_simpleui | warm | hierarchical | 2000 | open_book | PASS | 10 | 124.828 | 91.693 | 168.152 | 91.031–189.261 |
| C_simpleui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 111.700 | 90.378 | 133.629 | 83.892–139.630 |
| C_simpleui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 10.547 | 9.965 | 25.102 | 9.077–128.899 |
| C_simpleui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 11.030 | 10.011 | 18.664 | 9.431–19.397 |
| C_simpleui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 39.066 | 14.791 | 44.202 | 13.631–61.794 |
| C_simpleui | warm | hierarchical | 50 | close_book | PASS | 10 | 64.531 | 39.066 | 130.465 | 37.730–133.015 |
| C_simpleui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.649 | 7.726 | 9.400 | 7.496–11.270 |
| C_simpleui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 12.538 | 10.498 | 22.503 | 10.167–24.514 |
| C_simpleui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 36.327 | 28.446 | 45.664 | 26.703–50.338 |
| C_simpleui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.887 | 14.595 | 37.341 | 13.753–42.845 |
| C_simpleui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 18.255 | 11.864 | 40.384 | 11.517–40.478 |
| C_simpleui | warm | hierarchical | 50 | open_book | PASS | 10 | 128.197 | 84.739 | 166.607 | 84.572–177.801 |
| C_simpleui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 106.479 | 98.890 | 119.177 | 91.378–127.957 |
| C_simpleui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 9.863 | 9.419 | 20.203 | 9.390–97.860 |
| C_simpleui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 11.755 | 10.692 | 21.167 | 10.633–21.569 |
| D_zenos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 45.131 | 40.564 | 47.805 | 39.422–48.474 |
| D_zenos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 33.054 | 31.280 | 34.329 | 30.836–34.648 |
| D_zenos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 11.131 | 9.335 | 30.696 | 7.798–35.881 |
| D_zenos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 12.011 | 9.928 | 31.640 | 7.981–46.512 |
| D_zenos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 30.817 | 29.983 | 34.715 | 29.774–35.690 |
| D_zenos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 11.259 | 9.811 | 26.759 | 7.693–31.477 |
| D_zenos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 90 | 11.687 | 9.681 | 26.047 | 8.071–33.701 |
| D_zenos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 27.260 | 23.902 | 30.090 | 23.063–30.798 |
| D_zenos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 44.500 | 33.468 | 45.906 | 30.710–46.257 |
| D_zenos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 31.511 | 23.406 | 32.701 | 21.380–32.999 |
| D_zenos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 129.415 | 102.353 | 137.159 | 99.591–140.322 |
| D_zenos | warm | flat | 2000 | close_book | PASS | 10 | 52.705 | 42.052 | 116.025 | 39.883–120.223 |
| D_zenos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 17.236 | 16.593 | 17.691 | 13.414–17.729 |
| D_zenos | warm | flat | 2000 | home_to_library | PASS | 10 | 83.541 | 82.911 | 110.781 | 81.732–141.091 |
| D_zenos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 18.004 | 10.418 | 39.327 | 8.488–42.511 |
| D_zenos | warm | flat | 2000 | library_first_render | PASS | 10 | 94.376 | 87.106 | 107.190 | 86.098–110.072 |
| D_zenos | warm | flat | 2000 | library_folder_back | PASS | 10 | 138.346 | 121.025 | 142.716 | 116.077–143.131 |
| D_zenos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 14.497 | 13.803 | 15.870 | 12.797–16.054 |
| D_zenos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 11.043 | 9.156 | 33.188 | 8.192–37.376 |
| D_zenos | warm | flat | 2000 | open_book | PASS | 10 | 132.168 | 114.748 | 148.146 | 95.739–159.763 |
| D_zenos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 121.947 | 108.137 | 124.246 | 105.581–126.572 |
| D_zenos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 9.712 | 8.714 | 12.289 | 8.638–12.568 |
| D_zenos | warm | flat | 2000 | repeated_nav | PASS | 2 | 184.174 | 146.685 | 221.663 | 137.313–231.035 |
| D_zenos | warm | flat | 2000 | start_to_home | PASS | 10 | 13.486 | 10.320 | 15.964 | 8.776–16.391 |
| D_zenos | warm | flat | 50 | change_sort_mode | PASS | 10 | 39.931 | 23.825 | 45.172 | 23.744–48.767 |
| D_zenos | warm | flat | 50 | close_book | PASS | 10 | 45.510 | 41.899 | 53.963 | 38.832–58.349 |
| D_zenos | warm | flat | 50 | close_quick_settings | PASS | 10 | 17.280 | 16.747 | 21.643 | 16.707–58.771 |
| D_zenos | warm | flat | 50 | home_to_library | PASS | 10 | 38.410 | 37.207 | 50.173 | 35.997–59.727 |
| D_zenos | warm | flat | 50 | library_cached_paging | PASS | 30 | 18.129 | 10.466 | 28.505 | 10.026–41.225 |
| D_zenos | warm | flat | 50 | library_first_render | PASS | 10 | 46.450 | 43.740 | 57.206 | 42.103–59.816 |
| D_zenos | warm | flat | 50 | library_folder_back | PASS | 10 | 50.161 | 33.604 | 53.061 | 31.780–53.377 |
| D_zenos | warm | flat | 50 | library_folder_enter | PASS | 10 | 18.147 | 15.120 | 34.695 | 14.135–37.713 |
| D_zenos | warm | flat | 50 | library_sequential_paging | PASS | 9 | 12.333 | 10.000 | 16.992 | 9.914–27.534 |
| D_zenos | warm | flat | 50 | open_book | PASS | 10 | 111.739 | 104.320 | 116.558 | 101.680–134.345 |
| D_zenos | warm | flat | 50 | open_book_minimal | PASS | 10 | 88.868 | 67.697 | 94.949 | 63.774–105.119 |
| D_zenos | warm | flat | 50 | open_quick_settings | PASS | 10 | 9.476 | 8.224 | 12.028 | 8.201–13.316 |
| D_zenos | warm | flat | 50 | repeated_nav | PASS | 2 | 199.273 | 106.727 | 291.819 | 83.591–314.955 |
| D_zenos | warm | flat | 50 | start_to_home | PASS | 10 | 14.026 | 11.117 | 15.381 | 10.580–16.113 |
| D_zenos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 36.728 | 20.034 | 40.049 | 19.803–40.103 |
| D_zenos | warm | hierarchical | 2000 | close_book | PASS | 10 | 43.106 | 40.618 | 51.327 | 40.390–54.401 |
| D_zenos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 17.401 | 16.374 | 24.406 | 13.495–84.650 |
| D_zenos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 30.483 | 28.481 | 31.854 | 28.096–32.219 |
| D_zenos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 34.050 | 31.740 | 41.334 | 31.440–48.482 |
| D_zenos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 23.294 | 17.854 | 37.830 | 17.216–39.302 |
| D_zenos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 26.424 | 12.606 | 47.543 | 11.659–48.898 |
| D_zenos | warm | hierarchical | 2000 | open_book | PASS | 10 | 118.664 | 96.127 | 132.666 | 71.371–138.689 |
| D_zenos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 91.209 | 83.987 | 102.682 | 69.123–106.828 |
| D_zenos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 9.540 | 8.691 | 11.211 | 8.469–11.630 |
| D_zenos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 13.288 | 11.015 | 29.127 | 9.954–33.031 |
| D_zenos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 35.229 | 18.820 | 37.390 | 18.678–38.329 |
| D_zenos | warm | hierarchical | 50 | close_book | PASS | 10 | 47.257 | 43.225 | 60.968 | 41.979–95.965 |
| D_zenos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 17.162 | 16.651 | 22.368 | 16.648–64.733 |
| D_zenos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 27.620 | 26.609 | 29.725 | 25.656–29.951 |
| D_zenos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.929 | 29.603 | 43.970 | 29.540–49.039 |
| D_zenos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 23.295 | 19.600 | 37.041 | 18.427–39.178 |
| D_zenos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 17.434 | 12.762 | 38.346 | 12.455–48.679 |
| D_zenos | warm | hierarchical | 50 | open_book | PASS | 10 | 105.950 | 99.653 | 118.008 | 67.846–118.203 |
| D_zenos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 64.880 | 59.405 | 88.936 | 58.900–90.631 |
| D_zenos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 11.190 | 8.944 | 21.454 | 8.655–68.991 |
| D_zenos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 13.113 | 11.118 | 30.284 | 11.062–34.304 |
| E_project_title | paging | flat | 2000 | library_cached_paging | PASS | 90 | 13.338 | 11.526 | 15.714 | 10.279–19.952 |
| E_project_title | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 13.518 | 11.623 | 15.912 | 10.404–21.547 |
| E_project_title | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 12.843 | 12.684 | 14.769 | 12.644–15.250 |
| E_project_title | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 12.983 | 11.057 | 15.499 | 9.552–20.479 |
| E_project_title | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 13.395 | 12.053 | 14.598 | 10.484–16.790 |
| E_project_title | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 16.622 | 13.636 | 17.097 | 12.890–17.216 |
| E_project_title | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.319 | 12.085 | 13.963 | 12.027–14.374 |
| E_project_title | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 10.175 | 10.114 | 12.329 | 10.099–12.867 |
| E_project_title | warm | flat | 2000 | change_sort_mode | PASS | 10 | 97.496 | 86.808 | 109.251 | 86.114–109.437 |
| E_project_title | warm | flat | 2000 | close_book | PASS | 10 | 58.979 | 55.386 | 64.537 | 55.260–65.069 |
| E_project_title | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.740 | 8.203 | 9.982 | 7.971–10.105 |
| E_project_title | warm | flat | 2000 | home_to_library | PASS | 10 | 57.518 | 56.045 | 66.267 | 55.396–67.385 |
| E_project_title | warm | flat | 2000 | library_cached_paging | PASS | 30 | 12.708 | 11.100 | 14.836 | 10.199–18.853 |
| E_project_title | warm | flat | 2000 | library_first_render | PASS | 10 | 60.498 | 57.049 | 67.942 | 56.808–69.692 |
| E_project_title | warm | flat | 2000 | library_folder_back | PASS | 10 | 105.343 | 97.338 | 110.917 | 96.865–113.636 |
| E_project_title | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.732 | 8.383 | 9.218 | 8.339–9.268 |
| E_project_title | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 12.988 | 11.315 | 14.756 | 11.068–18.616 |
| E_project_title | warm | flat | 2000 | open_book | PASS | 10 | 58.075 | 54.566 | 65.263 | 54.300–65.758 |
| E_project_title | warm | flat | 2000 | open_book_minimal | PASS | 10 | 63.190 | 60.978 | 64.584 | 59.379–66.698 |
| E_project_title | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.450 | 7.789 | 9.000 | 7.658–9.188 |
| E_project_title | warm | flat | 2000 | repeated_nav | PASS | 2 | 87.797 | 84.600 | 90.994 | 83.801–91.793 |
| E_project_title | warm | flat | 50 | change_sort_mode | PASS | 10 | 7.704 | 7.460 | 8.550 | 7.304–8.631 |
| E_project_title | warm | flat | 50 | close_book | PASS | 10 | 16.059 | 15.015 | 19.369 | 14.982–22.844 |
| E_project_title | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.204 | 7.467 | 8.772 | 7.387–8.959 |
| E_project_title | warm | flat | 50 | home_to_library | PASS | 10 | 8.471 | 7.815 | 9.401 | 7.688–13.073 |
| E_project_title | warm | flat | 50 | library_cached_paging | PASS | 30 | 7.548 | 6.958 | 7.991 | 6.555–10.586 |
| E_project_title | warm | flat | 50 | library_first_render | PASS | 10 | 7.633 | 6.984 | 8.194 | 6.963–8.230 |
| E_project_title | warm | flat | 50 | library_folder_back | PASS | 10 | 11.151 | 10.155 | 14.672 | 10.098–16.262 |
| E_project_title | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.117 | 8.939 | 9.334 | 8.751–9.339 |
| E_project_title | warm | flat | 50 | library_sequential_paging | PASS | 3 | 7.972 | 7.279 | 8.619 | 7.106–8.781 |
| E_project_title | warm | flat | 50 | open_book | PASS | 10 | 43.090 | 42.694 | 44.112 | 42.114–44.586 |
| E_project_title | warm | flat | 50 | open_book_minimal | PASS | 10 | 43.647 | 42.047 | 45.868 | 41.767–47.296 |
| E_project_title | warm | flat | 50 | open_quick_settings | PASS | 10 | 7.806 | 7.533 | 8.813 | 7.475–8.872 |
| E_project_title | warm | flat | 50 | repeated_nav | PASS | 2 | 84.080 | 84.043 | 84.117 | 84.034–84.126 |
| E_project_title | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 8.442 | 7.644 | 9.436 | 7.496–10.518 |
| E_project_title | warm | hierarchical | 2000 | close_book | PASS | 10 | 21.721 | 20.428 | 26.443 | 18.721–28.310 |
| E_project_title | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.597 | 8.109 | 9.144 | 7.990–9.253 |
| E_project_title | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 10.180 | 9.254 | 11.768 | 8.816–11.827 |
| E_project_title | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 10.611 | 9.135 | 11.048 | 8.664–11.067 |
| E_project_title | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 13.066 | 12.120 | 14.510 | 11.693–16.743 |
| E_project_title | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.130 | 8.941 | 20.475 | 8.384–30.092 |
| E_project_title | warm | hierarchical | 2000 | open_book | PASS | 10 | 46.590 | 44.692 | 47.407 | 42.060–48.540 |
| E_project_title | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 46.350 | 44.059 | 49.377 | 44.010–50.480 |
| E_project_title | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.124 | 7.785 | 8.826 | 7.626–8.933 |
| E_project_title | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.147 | 7.304 | 9.500 | 6.865–9.828 |
| E_project_title | warm | hierarchical | 50 | close_book | PASS | 10 | 16.102 | 13.617 | 21.463 | 13.084–22.542 |
| E_project_title | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.236 | 7.985 | 8.999 | 7.779–9.085 |
| E_project_title | warm | hierarchical | 50 | home_to_library | PASS | 10 | 10.305 | 9.515 | 11.223 | 9.506–12.304 |
| E_project_title | warm | hierarchical | 50 | library_first_render | PASS | 10 | 11.458 | 10.385 | 12.521 | 9.599–14.816 |
| E_project_title | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 13.700 | 12.437 | 14.374 | 10.722–14.779 |
| E_project_title | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 9.213 | 8.881 | 11.561 | 8.567–12.640 |
| E_project_title | warm | hierarchical | 50 | open_book | PASS | 10 | 43.939 | 41.880 | 45.632 | 41.543–45.654 |
| E_project_title | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 45.242 | 42.660 | 49.021 | 42.394–49.912 |
| E_project_title | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 7.942 | 7.534 | 8.492 | 7.520–8.668 |
| F_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 27.641 | 23.363 | 43.985 | 21.134–52.837 |
| F_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 21.628 | 19.250 | 38.270 | 16.889–42.971 |
| F_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 35.460 | 24.852 | 41.354 | 22.200–42.827 |
| F_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 27.026 | 22.835 | 40.797 | 20.120–46.169 |
| F_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 21.056 | 18.381 | 30.636 | 16.416–37.563 |
| F_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 31.223 | 30.608 | 31.559 | 30.454–31.643 |
| F_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 20.625 | 19.547 | 20.748 | 19.277–20.779 |
| F_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 19.886 | 18.336 | 20.230 | 17.949–20.316 |
| F_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 134.783 | 115.956 | 163.324 | 111.215–169.432 |
| F_vos | warm | flat | 2000 | close_book | PASS | 10 | 80.325 | 78.442 | 85.359 | 77.822–89.476 |
| F_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.727 | 7.984 | 9.084 | 7.573–9.300 |
| F_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 85.072 | 77.136 | 99.276 | 76.519–170.801 |
| F_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 25.135 | 20.869 | 54.089 | 17.500–55.751 |
| F_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 80.431 | 77.431 | 111.944 | 75.820–137.042 |
| F_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 149.102 | 129.799 | 160.818 | 128.709–162.117 |
| F_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.740 | 8.482 | 11.342 | 8.476–28.388 |
| F_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 24.586 | 21.551 | 50.826 | 19.825–52.707 |
| F_vos | warm | flat | 2000 | open_book | PASS | 10 | 77.709 | 75.296 | 79.936 | 73.245–83.501 |
| F_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 76.285 | 74.422 | 79.660 | 74.182–81.730 |
| F_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.147 | 7.705 | 8.664 | 7.564–8.983 |
| F_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 206.863 | 187.377 | 226.350 | 182.506–231.221 |
| F_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 45.243 | 39.264 | 59.417 | 37.585–61.204 |
| F_vos | warm | flat | 50 | close_book | PASS | 10 | 41.281 | 36.887 | 63.146 | 34.051–63.586 |
| F_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.484 | 7.943 | 8.849 | 7.550–9.246 |
| F_vos | warm | flat | 50 | home_to_library | PASS | 10 | 41.809 | 39.558 | 65.378 | 39.203–79.353 |
| F_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 26.785 | 21.471 | 51.433 | 18.424–71.336 |
| F_vos | warm | flat | 50 | library_first_render | PASS | 10 | 52.383 | 49.305 | 90.672 | 35.400–98.097 |
| F_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 55.481 | 54.162 | 69.704 | 53.587–70.047 |
| F_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.963 | 5.644 | 10.850 | 5.549–23.932 |
| F_vos | warm | flat | 50 | library_sequential_paging | PASS | 4 | 61.745 | 60.016 | 79.025 | 59.849–85.856 |
| F_vos | warm | flat | 50 | open_book | PASS | 10 | 58.083 | 39.781 | 68.244 | 38.547–69.201 |
| F_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 49.576 | 46.480 | 63.470 | 44.718–65.143 |
| F_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.510 | 7.618 | 9.114 | 4.935–9.337 |
| F_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 198.609 | 176.875 | 220.344 | 171.441–225.778 |
| F_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 10.745 | 8.099 | 33.386 | 7.507–88.171 |
| F_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 70.564 | 31.026 | 74.755 | 30.264–77.857 |
| F_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.160 | 7.778 | 8.957 | 7.705–9.407 |
| F_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 21.068 | 19.897 | 21.831 | 19.603–23.318 |
| F_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 21.202 | 19.908 | 29.521 | 19.877–31.128 |
| F_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 25.643 | 23.358 | 31.325 | 22.697–37.204 |
| F_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 25.389 | 8.673 | 38.790 | 7.962–39.031 |
| F_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 57.495 | 54.803 | 60.130 | 54.046–60.302 |
| F_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 57.308 | 55.834 | 66.548 | 54.210–84.063 |
| F_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.374 | 7.466 | 8.963 | 5.247–9.291 |
| F_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 9.908 | 8.152 | 20.649 | 7.693–36.165 |
| F_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 32.925 | 28.779 | 36.601 | 28.090–36.992 |
| F_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.273 | 8.097 | 8.885 | 7.778–9.119 |
| F_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 21.183 | 19.264 | 28.144 | 19.254–28.172 |
| F_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 21.038 | 19.893 | 24.392 | 19.765–28.411 |
| F_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 28.258 | 23.593 | 31.813 | 22.762–32.623 |
| F_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.097 | 8.376 | 19.347 | 7.913–29.126 |
| F_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 57.611 | 55.485 | 60.988 | 54.769–60.999 |
| F_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 58.382 | 48.752 | 64.221 | 47.940–64.820 |
| F_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.380 | 7.875 | 10.230 | 7.593–21.209 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 80.772 | 77.384 | 89.599 | 75.800–107.991 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 22.334 | 18.849 | 35.438 | 16.972–64.022 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 93.865 | 88.101 | 100.833 | 86.234–122.611 |
| G_simpleui_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 32.740 | 27.381 | 42.728 | 19.697–58.898 |
| G_simpleui_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 21.549 | 20.967 | 31.643 | 20.821–34.167 |
| G_simpleui_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 27.189 | 23.017 | 47.913 | 19.107–56.271 |
| G_simpleui_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 23.400 | 19.971 | 43.503 | 17.058–49.697 |
| G_simpleui_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 198.798 | 181.042 | 199.623 | 176.603–199.829 |
| G_simpleui_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 37.457 | 37.227 | 37.643 | 37.169–37.690 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 82.816 | 79.104 | 91.652 | 76.988–100.959 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 23.450 | 19.954 | 31.964 | 18.396–42.565 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 94.718 | 88.582 | 102.270 | 83.884–122.431 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 33.084 | 25.988 | 41.386 | 21.592–48.026 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 14.252 | 11.712 | 14.631 | 11.077–14.726 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 26.022 | 19.460 | 42.336 | 14.855–51.894 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 23.370 | 20.704 | 36.446 | 19.543–44.806 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 121.280 | 118.253 | 127.763 | 117.496–129.384 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 34.197 | 33.776 | 38.241 | 33.671–39.252 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 13.786 | 13.676 | 13.802 | 13.649–13.806 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 29.034 | 27.882 | 30.020 | 27.594–30.266 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 87.287 | 74.654 | 110.633 | 72.348–304.568 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 19.236 | 16.860 | 21.537 | 14.813–181.080 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 23.709 | 21.500 | 127.490 | 20.953–137.375 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 126.005 | 110.835 | 135.835 | 97.860–336.800 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 57.462 | 48.549 | 67.411 | 20.006–251.768 |
| G_simpleui_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 132.718 | 113.237 | 159.235 | 106.039–159.455 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 176.303 | 169.247 | 286.690 | 168.322–322.758 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 28.953 | 25.922 | 139.043 | 24.431–163.891 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 14.267 | 12.608 | 37.462 | 12.369–236.106 |
| G_simpleui_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 21.587 | 19.118 | 37.108 | 19.056–41.402 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 22.923 | 16.638 | 45.719 | 14.232–51.228 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 110.055 | 90.947 | 121.050 | 86.895–137.520 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 126.881 | 109.515 | 130.452 | 104.248–130.936 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 17.473 | 15.958 | 22.816 | 15.852–39.230 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 22.542 | 19.225 | 49.834 | 17.932–56.528 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 178.351 | 153.611 | 193.990 | 141.492–203.101 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 89.237 | 77.180 | 114.014 | 72.066–119.986 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 27.038 | 25.042 | 28.882 | 24.342–30.339 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 28.000 | 26.684 | 68.807 | 24.324–430.082 |
| G_simpleui_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 870.477 | 855.369 | 885.586 | 851.592–889.363 |
| G_simpleui_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 17.334 | 10.676 | 29.631 | 9.490–41.016 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 92.567 | 85.553 | 103.215 | 83.683–138.148 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 31.075 | 27.933 | 45.519 | 26.005–82.186 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 37.060 | 31.418 | 86.646 | 30.665–108.635 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 104.067 | 92.900 | 113.212 | 83.924–120.299 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 36.022 | 21.128 | 46.697 | 10.162–47.344 |
| G_simpleui_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 40.312 | 29.239 | 52.850 | 29.233–54.413 |
| G_simpleui_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 94.679 | 75.666 | 181.052 | 54.590–228.169 |
| G_simpleui_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 27.335 | 23.636 | 84.457 | 22.839–90.930 |
| G_simpleui_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 14.645 | 13.519 | 17.042 | 12.342–18.249 |
| G_simpleui_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 18.403 | 17.276 | 19.470 | 16.283–21.011 |
| G_simpleui_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 14.200 | 10.143 | 33.145 | 8.256–34.052 |
| G_simpleui_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 32.343 | 23.162 | 46.066 | 22.556–53.483 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 17.400 | 15.190 | 32.835 | 14.888–35.900 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 13.747 | 8.807 | 40.813 | 8.666–41.586 |
| G_simpleui_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 6 | 17.090 | 12.626 | 27.639 | 11.025–35.278 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 102.438 | 79.425 | 144.379 | 72.971–146.969 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 82.359 | 50.115 | 105.723 | 49.323–106.363 |
| G_simpleui_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 36.268 | 35.175 | 39.037 | 35.010–40.254 |
| G_simpleui_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 31.319 | 28.299 | 134.814 | 27.746–146.195 |
| G_simpleui_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 521.583 | 491.969 | 551.197 | 484.566–558.600 |
| G_simpleui_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 11.659 | 10.238 | 23.116 | 10.201–25.997 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 22.137 | 19.811 | 75.108 | 18.624–78.214 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 15.949 | 13.479 | 41.005 | 13.101–49.821 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 77.962 | 62.831 | 122.259 | 56.490–129.011 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 26.739 | 25.317 | 90.131 | 24.385–91.861 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 11.194 | 10.106 | 24.298 | 8.899–130.819 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 12.303 | 11.410 | 14.305 | 11.110–22.863 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 34.939 | 27.511 | 45.560 | 27.495–47.036 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 18.845 | 13.654 | 42.510 | 13.514–43.224 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 38.614 | 22.619 | 51.943 | 11.133–59.221 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 142.904 | 94.995 | 170.491 | 87.953–186.554 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 105.931 | 66.081 | 109.592 | 65.318–118.268 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 23.576 | 22.307 | 27.707 | 19.256–28.132 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 18.934 | 16.704 | 128.697 | 16.448–131.149 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 12.456 | 10.720 | 20.334 | 10.714–24.402 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 16.252 | 12.600 | 71.993 | 12.119–87.614 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 7.550 | 6.939 | 22.952 | 6.713–25.666 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 56.287 | 37.616 | 95.304 | 36.646–102.267 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 19.168 | 17.909 | 84.127 | 17.598–90.427 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.518 | 7.490 | 8.710 | 7.468–8.884 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 8.105 | 6.586 | 8.799 | 6.458–8.933 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 23.379 | 19.616 | 36.503 | 18.508–40.305 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 10.090 | 7.660 | 15.741 | 7.153–28.578 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.146 | 8.456 | 41.136 | 6.875–41.146 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 135.516 | 86.587 | 182.068 | 80.601–197.076 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 92.897 | 61.804 | 123.864 | 58.055–125.192 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 19.612 | 15.775 | 28.111 | 15.738–31.909 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 10.294 | 9.215 | 22.311 | 9.016–117.901 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 9.260 | 8.425 | 19.410 | 8.267–23.872 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 76.661 | 73.917 | 97.406 | 72.219–103.362 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 16.791 | 14.595 | 27.097 | 12.548–37.269 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 97.130 | 89.507 | 107.122 | 85.152–166.122 |
| H_zenos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 32.862 | 28.441 | 41.725 | 14.915–64.021 |
| H_zenos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 21.732 | 19.849 | 23.134 | 19.378–23.484 |
| H_zenos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 11.218 | 9.146 | 32.084 | 7.625–37.251 |
| H_zenos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 11.994 | 10.290 | 30.311 | 8.191–33.579 |
| H_zenos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 238.658 | 236.081 | 251.260 | 235.437–254.411 |
| H_zenos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 30.707 | 30.674 | 33.613 | 30.666–34.340 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 74.933 | 72.557 | 94.220 | 71.275–101.808 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 15.605 | 13.572 | 21.191 | 12.395–34.021 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 99.781 | 87.894 | 113.690 | 79.245–137.113 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 33.915 | 25.251 | 43.036 | 15.940–53.048 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 18.574 | 16.707 | 19.033 | 16.240–19.148 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 10.985 | 9.096 | 25.045 | 8.148–28.823 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 90 | 11.244 | 9.342 | 24.778 | 8.109–31.735 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 130.615 | 124.428 | 138.841 | 122.881–140.898 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 24.905 | 23.695 | 26.431 | 23.393–26.812 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 41.942 | 41.205 | 42.452 | 41.021–42.580 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 31.810 | 31.468 | 33.123 | 31.382–33.451 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 72.401 | 66.648 | 83.982 | 65.876–109.108 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 10.347 | 7.541 | 20.219 | 6.884–47.684 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 18.904 | 13.192 | 56.950 | 12.818–72.599 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 75.831 | 72.865 | 96.193 | 71.320–124.492 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 12.909 | 11.465 | 31.195 | 9.633–58.590 |
| H_zenos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 125.427 | 96.892 | 140.457 | 95.808–143.885 |
| H_zenos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 47.206 | 38.793 | 114.621 | 36.722–121.403 |
| H_zenos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 10.865 | 10.373 | 11.828 | 10.215–12.216 |
| H_zenos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 17.404 | 17.145 | 95.296 | 17.086–103.571 |
| H_zenos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 86.792 | 83.849 | 117.003 | 82.341–139.122 |
| H_zenos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 16.718 | 10.264 | 39.524 | 9.359–44.378 |
| H_zenos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 92.759 | 87.023 | 110.538 | 86.406–115.574 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 139.205 | 114.104 | 142.318 | 113.669–143.445 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 16.164 | 13.336 | 20.818 | 12.712–36.883 |
| H_zenos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 10.639 | 8.243 | 31.942 | 7.906–35.671 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 143.811 | 124.945 | 159.042 | 93.467–186.549 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 117.376 | 102.220 | 129.426 | 71.953–130.354 |
| H_zenos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.922 | 15.491 | 23.491 | 15.193–44.166 |
| H_zenos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 10.149 | 8.688 | 11.185 | 8.411–12.027 |
| H_zenos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 240.153 | 115.218 | 365.089 | 83.984–396.323 |
| H_zenos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 13.659 | 12.026 | 15.136 | 10.704–15.911 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 73.131 | 67.549 | 87.029 | 66.400–104.209 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 9.930 | 8.002 | 20.916 | 7.099–45.903 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 16.170 | 11.377 | 52.810 | 10.986–69.609 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 79.943 | 70.666 | 92.969 | 68.312–98.495 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 27.902 | 9.531 | 36.913 | 8.285–38.754 |
| H_zenos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 39.218 | 23.478 | 43.932 | 23.077–48.249 |
| H_zenos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 49.203 | 40.783 | 55.108 | 40.115–62.342 |
| H_zenos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 10.662 | 10.314 | 13.151 | 10.229–14.924 |
| H_zenos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 17.071 | 14.806 | 17.973 | 14.428–20.747 |
| H_zenos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 37.531 | 35.708 | 46.355 | 35.443–46.609 |
| H_zenos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 17.261 | 10.934 | 33.238 | 9.266–38.863 |
| H_zenos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 46.005 | 40.754 | 61.040 | 40.676–68.587 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 50.289 | 34.996 | 52.092 | 34.391–52.714 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 15.857 | 14.528 | 19.069 | 14.495–29.457 |
| H_zenos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 9 | 11.864 | 10.442 | 29.851 | 10.246–32.766 |
| H_zenos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 110.667 | 98.036 | 125.788 | 93.002–131.237 |
| H_zenos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 90.114 | 67.410 | 93.026 | 66.027–95.412 |
| H_zenos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 17.184 | 14.106 | 34.162 | 14.008–35.433 |
| H_zenos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 12.334 | 11.290 | 18.218 | 10.255–22.334 |
| H_zenos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 240.647 | 115.025 | 366.268 | 83.620–397.673 |
| H_zenos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 13.883 | 12.620 | 15.628 | 12.545–16.615 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 13.046 | 11.914 | 50.234 | 11.477–52.217 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 33.774 | 18.818 | 38.353 | 17.345–40.035 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 46.779 | 39.040 | 55.860 | 38.954–56.660 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 11.344 | 9.663 | 15.236 | 9.657–17.235 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 17.201 | 16.022 | 17.536 | 13.226–17.694 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 28.743 | 27.901 | 30.543 | 26.934–31.803 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 33.218 | 32.023 | 42.543 | 31.891–51.874 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 37.572 | 19.770 | 40.881 | 17.317–41.902 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 25.880 | 19.031 | 44.407 | 13.888–46.522 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 114.144 | 104.592 | 126.184 | 101.459–140.220 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 67.728 | 65.754 | 94.249 | 64.859–95.588 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 17.054 | 14.233 | 20.970 | 13.058–22.742 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 11.590 | 10.179 | 29.130 | 9.180–92.797 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 13.564 | 12.650 | 32.911 | 12.456–35.348 |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 13.654 | 11.726 | 45.470 | 11.701–48.781 |
| H_zenos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 23.152 | 18.915 | 37.802 | 18.775–44.369 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 51.230 | 41.141 | 57.589 | 39.405–58.468 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 9.823 | 9.520 | 11.478 | 9.435–11.973 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 17.347 | 16.349 | 24.055 | 13.465–82.429 |
| H_zenos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 29.651 | 27.337 | 31.735 | 27.039–31.972 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.994 | 31.655 | 44.273 | 30.913–52.166 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 27.025 | 19.105 | 36.728 | 18.864–40.876 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 18.598 | 12.643 | 28.236 | 11.970–45.864 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 113.779 | 101.591 | 117.610 | 100.666–131.453 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 86.026 | 63.100 | 91.221 | 61.374–94.573 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 13.977 | 12.178 | 24.883 | 11.847–29.253 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 9.445 | 8.872 | 11.724 | 8.149–11.735 |
| H_zenos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 13.279 | 10.655 | 28.713 | 9.216–31.239 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 79.856 | 69.915 | 91.870 | 67.258–104.435 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 19.483 | 9.139 | 29.582 | 7.922–35.995 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 89.030 | 71.891 | 98.447 | 69.968–186.009 |
| I_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 28.098 | 11.211 | 37.154 | 9.826–49.745 |
| I_vos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 11.753 | 11.169 | 13.369 | 11.023–13.773 |
| I_vos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 25.069 | 15.454 | 40.398 | 10.985–49.048 |
| I_vos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 21.080 | 13.575 | 35.510 | 10.782–43.108 |
| I_vos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 202.546 | 200.864 | 205.679 | 200.443–206.462 |
| I_vos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 36.713 | 30.553 | 37.855 | 29.013–38.140 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 85.185 | 70.280 | 94.931 | 67.261–108.727 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 25.279 | 9.788 | 38.155 | 7.029–45.395 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 90.349 | 73.007 | 102.957 | 68.369–127.202 |
| I_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 29.468 | 11.096 | 37.549 | 7.614–50.286 |
| I_vos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 12.840 | 10.913 | 13.476 | 10.431–13.635 |
| I_vos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 25.924 | 14.566 | 38.636 | 12.915–49.399 |
| I_vos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 48 | 19.209 | 12.642 | 27.305 | 11.598–36.013 |
| I_vos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 123.842 | 119.966 | 138.842 | 118.997–142.592 |
| I_vos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 31.947 | 24.757 | 33.357 | 22.959–33.710 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 21.059 | 20.977 | 21.797 | 20.957–21.982 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 21.273 | 19.900 | 21.817 | 19.557–21.953 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 76.142 | 66.029 | 93.055 | 65.494–100.366 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 7.970 | 7.149 | 11.024 | 5.783–24.088 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 12.878 | 10.436 | 36.287 | 10.260–44.535 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 77.098 | 70.941 | 100.685 | 70.548–157.357 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 28.353 | 24.208 | 42.627 | 8.506–60.417 |
| I_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 133.835 | 117.059 | 173.088 | 113.111–175.147 |
| I_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 82.602 | 79.649 | 91.091 | 78.256–92.557 |
| I_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 7.691 | 7.458 | 8.440 | 6.622–8.590 |
| I_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.457 | 8.047 | 8.637 | 7.399–8.717 |
| I_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 96.755 | 81.082 | 165.446 | 79.385–184.717 |
| I_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 27.819 | 21.923 | 53.949 | 16.985–63.676 |
| I_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 80.712 | 76.634 | 139.663 | 74.442–151.561 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 138.341 | 126.387 | 158.184 | 126.001–161.798 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.878 | 6.668 | 9.220 | 6.385–9.351 |
| I_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 26.547 | 20.547 | 55.474 | 19.398–61.734 |
| I_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 87.864 | 79.733 | 93.602 | 77.923–100.870 |
| I_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 102.567 | 86.822 | 106.335 | 73.838–108.139 |
| I_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 11.071 | 10.322 | 16.299 | 9.863–18.622 |
| I_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.156 | 7.507 | 8.315 | 7.375–8.408 |
| I_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 224.237 | 194.207 | 254.267 | 186.699–261.775 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 73.740 | 67.080 | 92.019 | 66.547–95.087 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 7.557 | 6.875 | 13.807 | 5.688–25.281 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 22.174 | 14.159 | 34.182 | 13.807–50.254 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 76.429 | 71.049 | 86.068 | 68.127–89.753 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 23.245 | 13.595 | 34.553 | 8.649–40.615 |
| I_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 37.831 | 22.592 | 44.779 | 22.339–45.947 |
| I_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 44.294 | 35.941 | 66.150 | 34.603–66.579 |
| I_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 7.987 | 7.586 | 8.365 | 7.530–8.396 |
| I_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.480 | 8.324 | 8.977 | 8.171–9.079 |
| I_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 26.148 | 24.279 | 57.602 | 24.170–60.634 |
| I_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 18.474 | 15.117 | 40.176 | 13.189–54.804 |
| I_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 26.314 | 23.268 | 67.447 | 22.922–68.615 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 36.812 | 30.122 | 61.602 | 29.841–75.014 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.890 | 8.379 | 28.927 | 8.363–30.051 |
| I_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 4 | 46.890 | 13.924 | 99.570 | 11.808–110.135 |
| I_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 56.973 | 43.532 | 65.078 | 43.463–67.315 |
| I_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 51.987 | 40.402 | 66.564 | 38.964–67.978 |
| I_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 18.380 | 16.818 | 23.706 | 16.119–29.498 |
| I_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.383 | 7.789 | 8.704 | 7.416–8.951 |
| I_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 308.325 | 303.745 | 312.905 | 302.600–314.050 |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 13.509 | 12.288 | 37.532 | 11.648–38.637 |
| I_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 8.845 | 7.621 | 11.292 | 7.528–18.470 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 70.198 | 66.897 | 73.280 | 59.537–73.873 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.779 | 7.985 | 8.953 | 7.799–9.094 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.243 | 7.480 | 8.488 | 7.354–8.521 |
| I_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 21.455 | 20.622 | 27.238 | 18.962–28.044 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 22.160 | 20.695 | 27.837 | 19.565–34.095 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 29.150 | 23.903 | 48.705 | 21.580–52.591 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 25.389 | 8.792 | 42.038 | 8.635–44.932 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 64.014 | 61.326 | 96.437 | 60.805–98.563 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 61.949 | 59.097 | 91.150 | 59.012–100.265 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 13.501 | 13.055 | 17.223 | 12.615–22.345 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.255 | 7.462 | 8.804 | 7.439–8.982 |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 12.651 | 10.641 | 23.679 | 10.633–26.237 |
| I_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 10.298 | 8.405 | 64.247 | 7.595–87.934 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 30.118 | 28.480 | 33.301 | 25.916–34.011 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 8.460 | 7.975 | 8.911 | 7.767–9.105 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.244 | 8.013 | 8.711 | 7.586–8.721 |
| I_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 20.923 | 19.571 | 25.225 | 19.207–27.318 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 20.821 | 19.878 | 26.134 | 19.073–27.667 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 29.936 | 23.068 | 32.362 | 22.084–34.937 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 12.930 | 9.069 | 20.344 | 8.321–29.971 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 58.249 | 54.681 | 60.585 | 54.470–61.762 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 59.565 | 55.848 | 61.085 | 48.518–61.323 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 15.367 | 12.551 | 18.986 | 12.348–20.758 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.114 | 7.858 | 9.053 | 7.584–9.076 |
| J_simpleui_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 27.807 | 19.828 | 48.224 | 14.993–56.656 |
| J_simpleui_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 23.450 | 20.548 | 43.334 | 18.402–49.517 |
| J_simpleui_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 38.436 | 38.416 | 42.177 | 38.411–43.112 |
| J_simpleui_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 22.084 | 16.602 | 36.915 | 14.323–53.082 |
| J_simpleui_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 21.115 | 16.343 | 37.475 | 12.565–46.098 |
| J_simpleui_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 34.873 | 33.801 | 37.159 | 33.533–37.731 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.847 | 12.320 | 12.915 | 12.188–12.932 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 29.666 | 25.874 | 30.765 | 24.926–31.040 |
| J_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 128.008 | 107.271 | 168.051 | 100.533–172.434 |
| J_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 150.601 | 142.796 | 278.052 | 138.814–311.664 |
| J_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.361 | 7.784 | 8.848 | 7.607–8.906 |
| J_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 11.038 | 10.449 | 11.857 | 10.442–11.861 |
| J_simpleui_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.242 | 10.242 | 39.427 | 7.923–42.518 |
| J_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 81.212 | 73.076 | 110.379 | 70.785–113.246 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 133.327 | 112.370 | 144.164 | 106.939–144.593 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.990 | 9.206 | 14.045 | 8.360–33.796 |
| J_simpleui_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 15.892 | 12.586 | 42.644 | 11.568–48.027 |
| J_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 161.910 | 146.890 | 369.303 | 145.080–398.993 |
| J_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 101.793 | 73.778 | 128.291 | 59.740–139.280 |
| J_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 29.723 | 25.292 | 105.575 | 24.379–758.412 |
| J_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 1042.216 | 916.520 | 1167.911 | 885.096–1199.335 |
| J_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 18.382 | 8.839 | 31.741 | 8.800–35.810 |
| J_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 46.433 | 32.884 | 64.742 | 31.003–88.846 |
| J_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 82.817 | 67.406 | 164.419 | 65.690–193.155 |
| J_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 7.888 | 7.708 | 8.478 | 7.634–9.026 |
| J_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 21.166 | 17.354 | 36.474 | 16.217–36.728 |
| J_simpleui_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 19.279 | 15.246 | 39.211 | 13.591–50.083 |
| J_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 45.590 | 41.042 | 62.216 | 39.530–62.289 |
| J_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 43.293 | 29.689 | 46.437 | 24.409–49.062 |
| J_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.508 | 15.250 | 20.001 | 14.080–31.534 |
| J_simpleui_vos | warm | flat | 50 | library_sequential_paging | PASS | 6 | 21.740 | 19.139 | 34.638 | 18.211–45.144 |
| J_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 131.214 | 93.221 | 151.664 | 80.550–161.058 |
| J_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 100.659 | 59.793 | 112.706 | 59.338–113.556 |
| J_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 26.265 | 22.287 | 32.792 | 21.986–33.371 |
| J_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 411.841 | 170.820 | 652.863 | 110.565–713.118 |
| J_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 11.468 | 9.759 | 21.891 | 9.554–31.413 |
| J_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 10.078 | 8.378 | 30.836 | 7.141–32.425 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 56.959 | 49.370 | 122.307 | 45.114–140.549 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.365 | 7.804 | 10.797 | 7.615–12.969 |
| J_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 7.817 | 7.353 | 8.763 | 7.286–9.035 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 21.646 | 19.863 | 37.066 | 19.581–39.947 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 12.611 | 8.923 | 37.058 | 8.193–41.013 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 18.218 | 9.022 | 41.903 | 8.815–45.837 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 135.600 | 92.689 | 232.835 | 81.497–316.747 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 96.541 | 69.460 | 118.692 | 60.261–131.051 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 10.346 | 9.549 | 12.546 | 9.524–13.246 |
| J_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 10.015 | 8.640 | 19.314 | 8.580–20.601 |
| J_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 24.125 | 14.153 | 33.382 | 13.737–34.174 |
| J_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 39.808 | 28.340 | 117.817 | 26.824–141.533 |
| J_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.571 | 7.801 | 9.356 | 6.979–10.507 |
| J_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 10.736 | 9.898 | 11.873 | 9.071–13.443 |
| J_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 26.728 | 25.050 | 42.505 | 24.872–45.539 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 17.587 | 13.163 | 33.383 | 12.908–36.662 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 21.154 | 13.732 | 38.901 | 13.718–39.825 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 143.460 | 97.184 | 167.117 | 81.654–170.336 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 105.935 | 70.553 | 122.185 | 66.260–122.504 |
| J_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 10.930 | 9.898 | 13.796 | 9.568–16.739 |
| J_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 11.267 | 10.354 | 21.514 | 10.216–21.788 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging | PASS | 90 | 79.419 | 76.533 | 88.516 | 74.149–104.813 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 20.307 | 17.851 | 28.898 | 16.288–43.920 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging | PASS | 90 | 90.829 | 85.454 | 101.667 | 83.231–117.638 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 90 | 29.996 | 25.339 | 36.323 | 18.390–47.401 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | close_bookshelf | PASS | 3 | 28.674 | 26.025 | 29.760 | 25.363–30.031 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | library_cached_paging | PASS | 90 | 27.125 | 23.930 | 48.655 | 19.426–54.425 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 23.927 | 21.492 | 43.737 | 18.609–54.110 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | open_bookshelf | PASS | 3 | 180.127 | 177.756 | 183.578 | 177.163–184.441 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 37.387 | 36.166 | 37.753 | 35.861–37.844 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging | PASS | 90 | 81.162 | 69.869 | 89.641 | 66.218–103.812 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_cached_paging_anim_off | PASS | 90 | 22.963 | 9.161 | 29.231 | 7.384–44.704 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging | PASS | 60 | 91.632 | 72.578 | 101.823 | 69.939–131.386 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | bookshelf_sequential_paging_anim_off | PASS | 60 | 30.206 | 10.614 | 36.685 | 8.700–48.021 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | close_bookshelf | PASS | 3 | 14.052 | 11.014 | 15.213 | 10.255–15.503 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 21.956 | 16.909 | 39.562 | 12.413–49.077 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | library_sequential_paging | PASS | 60 | 21.443 | 16.461 | 39.806 | 11.289–43.303 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | open_bookshelf | PASS | 3 | 113.865 | 110.502 | 120.709 | 109.661–122.420 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 35.696 | 34.205 | 36.758 | 33.832–37.024 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 14.203 | 13.117 | 14.421 | 12.846–14.475 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 27.731 | 27.701 | 28.487 | 27.693–28.676 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 79.338 | 67.650 | 101.907 | 66.690–250.829 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 8.555 | 7.940 | 11.217 | 7.316–145.482 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 14.873 | 10.927 | 122.564 | 10.100–128.382 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 95.546 | 72.925 | 111.743 | 69.923–251.958 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 38.123 | 24.787 | 45.398 | 10.408–208.916 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 145.126 | 122.024 | 171.718 | 109.350–191.236 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 153.177 | 142.705 | 276.914 | 140.097–302.279 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 17.758 | 16.670 | 140.605 | 16.053–171.541 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.406 | 7.922 | 8.696 | 7.740–8.699 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 21.918 | 20.054 | 26.275 | 19.193–42.259 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 25.473 | 20.405 | 62.897 | 15.283–67.034 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 107.211 | 89.590 | 130.107 | 86.588–155.034 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 139.454 | 115.236 | 144.875 | 111.590–149.811 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 16.157 | 15.269 | 17.211 | 14.399–17.865 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 26.008 | 22.579 | 55.826 | 16.542–66.908 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 176.477 | 157.608 | 195.413 | 146.242–195.807 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 108.660 | 85.834 | 135.090 | 77.506–142.977 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 18.233 | 16.386 | 22.539 | 15.042–29.836 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 33.922 | 27.164 | 336.415 | 22.066–368.505 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 945.166 | 917.794 | 972.538 | 910.951–979.381 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 20.392 | 18.632 | 35.378 | 12.863–35.607 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 70.924 | 68.094 | 84.391 | 66.959–138.850 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 9.242 | 8.200 | 17.744 | 7.706–84.470 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 13.433 | 12.714 | 77.070 | 12.403–85.128 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 81.486 | 74.193 | 93.936 | 67.657–95.977 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 10.212 | 8.561 | 12.287 | 7.712–13.982 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 37.833 | 21.488 | 44.869 | 20.542–53.658 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 72.255 | 56.664 | 139.488 | 40.714–207.017 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 19.788 | 17.633 | 94.207 | 16.610–94.276 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.143 | 7.387 | 8.434 | 7.364–8.448 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 18.422 | 15.471 | 20.031 | 11.219–20.332 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.125 | 10.581 | 32.591 | 9.962–33.499 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 24.273 | 23.103 | 45.103 | 22.698–50.603 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 18.402 | 10.519 | 27.729 | 9.948–34.125 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.675 | 7.946 | 22.739 | 7.807–26.316 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 6 | 15.346 | 12.838 | 29.126 | 12.772–37.203 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 119.631 | 88.358 | 168.471 | 81.136–185.737 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 83.153 | 54.534 | 98.914 | 51.519–103.982 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 20.727 | 17.865 | 27.960 | 17.586–28.851 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 29.246 | 15.147 | 136.728 | 14.533–148.041 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 448.836 | 413.895 | 483.776 | 405.160–492.511 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 11.825 | 10.314 | 21.678 | 9.881–27.877 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 14.846 | 13.552 | 88.137 | 13.438–92.301 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.270 | 7.529 | 30.577 | 6.856–31.487 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 100.573 | 58.821 | 195.130 | 50.569–195.189 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 22.524 | 18.349 | 91.501 | 14.050–93.409 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 11.345 | 10.382 | 12.810 | 10.074–17.001 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 8.273 | 7.659 | 8.794 | 7.099–8.851 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 25.492 | 19.817 | 37.357 | 19.815–39.221 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.096 | 10.237 | 31.762 | 9.769–36.618 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 20.730 | 7.769 | 41.921 | 7.270–43.626 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 132.438 | 94.147 | 211.461 | 93.584–224.239 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 109.011 | 97.692 | 136.834 | 96.076–152.086 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 24.795 | 20.506 | 26.538 | 20.131–26.749 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 10.585 | 9.575 | 13.457 | 9.480–13.992 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 10.799 | 9.906 | 19.659 | 9.295–21.671 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 13.956 | 12.491 | 65.219 | 12.341–75.051 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 24.616 | 14.438 | 39.300 | 14.102–41.391 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 98.562 | 54.443 | 182.557 | 52.491–222.358 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 22.573 | 18.072 | 85.490 | 17.002–86.269 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.430 | 7.945 | 8.868 | 7.748–8.932 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 11.589 | 10.406 | 13.738 | 10.285–27.036 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 27.983 | 26.702 | 44.806 | 25.569–46.047 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 18.695 | 13.342 | 41.284 | 11.439–41.669 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 20.325 | 16.332 | 39.777 | 12.141–56.459 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 164.810 | 92.842 | 200.391 | 92.525–202.243 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 109.056 | 72.586 | 131.788 | 63.542–138.255 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 24.148 | 18.425 | 26.104 | 14.884–27.352 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 11.366 | 9.942 | 29.790 | 9.362–139.829 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 11.277 | 9.605 | 23.106 | 9.090–32.871 |
| K_vos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 22.529 | 21.943 | 24.145 | 21.797–24.549 |
| K_vos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 20.302 | 20.160 | 20.816 | 20.124–20.945 |
| L_project_title_vos | paging | flat | 2000 | library_cached_paging | PASS | 90 | 12.300 | 10.862 | 14.927 | 9.512–20.701 |
| L_project_title_vos | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 12.816 | 10.785 | 15.112 | 9.202–19.378 |
| L_project_title_vos | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 12.912 | 12.290 | 13.964 | 12.134–14.227 |
| L_project_title_vos | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 12.319 | 10.674 | 14.929 | 9.727–19.425 |
| L_project_title_vos | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 13.069 | 10.975 | 14.952 | 10.143–17.508 |
| L_project_title_vos | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 15.097 | 11.943 | 16.092 | 11.154–16.341 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 21.212 | 19.499 | 22.662 | 19.071–23.025 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 19.866 | 19.322 | 20.323 | 19.186–20.437 |
| L_project_title_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 108.715 | 95.605 | 117.722 | 95.474–118.610 |
| L_project_title_vos | warm | flat | 2000 | close_book | PASS | 10 | 76.638 | 73.726 | 78.199 | 73.451–80.853 |
| L_project_title_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.451 | 7.968 | 9.011 | 7.954–9.337 |
| L_project_title_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 73.350 | 71.289 | 81.283 | 70.859–84.597 |
| L_project_title_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 12.527 | 11.113 | 13.942 | 10.862–20.158 |
| L_project_title_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 73.144 | 69.769 | 82.944 | 67.695–83.288 |
| L_project_title_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 129.950 | 121.389 | 134.941 | 121.147–137.396 |
| L_project_title_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.442 | 7.778 | 8.729 | 7.777–8.843 |
| L_project_title_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 13.106 | 11.087 | 14.509 | 10.465–19.574 |
| L_project_title_vos | warm | flat | 2000 | open_book | PASS | 10 | 61.686 | 60.406 | 63.062 | 60.011–64.387 |
| L_project_title_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 63.900 | 61.534 | 68.160 | 61.079–71.823 |
| L_project_title_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.181 | 7.419 | 8.550 | 7.354–9.254 |
| L_project_title_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 83.160 | 82.774 | 83.546 | 82.677–83.643 |
| L_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 17.268 | 16.349 | 22.085 | 16.063–24.652 |
| L_project_title_vos | warm | flat | 50 | close_book | PASS | 10 | 28.996 | 26.051 | 36.832 | 25.787–39.705 |
| L_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.306 | 7.809 | 9.110 | 7.569–9.210 |
| L_project_title_vos | warm | flat | 50 | home_to_library | PASS | 10 | 26.831 | 25.607 | 28.907 | 25.223–29.163 |
| L_project_title_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 12.840 | 11.286 | 14.871 | 10.333–18.061 |
| L_project_title_vos | warm | flat | 50 | library_first_render | PASS | 10 | 27.372 | 25.474 | 29.423 | 24.489–30.782 |
| L_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 32.428 | 29.995 | 35.128 | 29.990–37.134 |
| L_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.747 | 7.701 | 9.228 | 7.422–9.374 |
| L_project_title_vos | warm | flat | 50 | library_sequential_paging | PASS | 3 | 13.506 | 10.717 | 13.928 | 10.020–14.034 |
| L_project_title_vos | warm | flat | 50 | open_book | PASS | 10 | 49.635 | 47.309 | 50.269 | 47.242–50.735 |
| L_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 50.459 | 48.601 | 52.106 | 48.590–52.561 |
| L_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.192 | 7.591 | 8.748 | 7.370–8.929 |
| L_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 84.130 | 83.880 | 84.381 | 83.817–84.444 |
| L_project_title_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 7.848 | 6.849 | 8.528 | 6.410–9.273 |
| L_project_title_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 31.966 | 29.050 | 36.493 | 27.188–37.717 |
| L_project_title_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.216 | 7.943 | 8.383 | 7.264–8.443 |
| L_project_title_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 18.980 | 18.058 | 20.181 | 17.346–20.827 |
| L_project_title_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 20.282 | 19.417 | 22.653 | 18.719–23.348 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 22.057 | 20.338 | 23.996 | 19.715–24.146 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 19.541 | 8.262 | 26.091 | 7.429–28.184 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 48.770 | 47.192 | 52.787 | 47.183–55.520 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 51.968 | 50.889 | 52.802 | 48.950–53.575 |
| L_project_title_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.325 | 8.072 | 8.928 | 8.051–9.982 |
| L_project_title_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 7.772 | 7.483 | 8.599 | 7.468–9.014 |
| L_project_title_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 28.027 | 25.580 | 29.838 | 22.923–34.321 |
| L_project_title_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.248 | 8.051 | 8.719 | 7.835–9.083 |
| L_project_title_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 19.938 | 19.413 | 21.342 | 18.930–21.553 |
| L_project_title_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 19.870 | 18.977 | 21.679 | 18.595–23.465 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 21.613 | 20.650 | 24.519 | 20.274–25.329 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 8.921 | 8.475 | 10.298 | 7.769–12.493 |
| L_project_title_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 47.823 | 45.927 | 49.147 | 45.585–49.856 |
| L_project_title_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 45.487 | 43.679 | 47.161 | 42.531–48.155 |
| L_project_title_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.168 | 7.604 | 9.029 | 7.508–9.157 |
| M_leanui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.354 | 12.349 | 13.092 | 12.348–13.276 |
| M_leanui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 12.377 | 11.683 | 12.403 | 11.509–12.409 |
| M_leanui | paging | flat | 2000 | library_cached_paging | PASS | 90 | 12.894 | 11.317 | 15.231 | 10.181–20.241 |
| M_leanui | paging | flat | 2000 | library_sequential_paging | PASS | 90 | 13.752 | 11.578 | 15.504 | 9.750–18.718 |
| M_leanui | paging | flat | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 11.865 | 11.563 | 13.277 | 11.487–13.630 |
| M_leanui | paging | hierarchical | 2000 | library_cached_paging | PASS | 90 | 12.724 | 11.224 | 14.644 | 10.399–20.935 |
| M_leanui | paging | hierarchical | 2000 | library_sequential_paging | PASS | 33 | 13.147 | 11.720 | 15.171 | 10.345–16.303 |
| M_leanui | paging | hierarchical | 2000 | paging_probe_step_2_to_3 | PASS | 3 | 16.071 | 14.884 | 17.730 | 14.587–18.145 |
| M_leanui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 11.433 | 11.261 | 11.693 | 11.218–11.758 |
| M_leanui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.665 | 10.519 | 12.217 | 10.233–12.355 |
| M_leanui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 94.911 | 80.140 | 97.407 | 80.010–101.437 |
| M_leanui | warm | flat | 2000 | close_book | PASS | 10 | 62.254 | 56.886 | 68.179 | 56.038–69.460 |
| M_leanui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.422 | 8.050 | 8.941 | 8.016–9.093 |
| M_leanui | warm | flat | 2000 | home_to_library | PASS | 10 | 48.071 | 46.518 | 57.434 | 46.440–57.957 |
| M_leanui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 7.385 | 7.125 | 8.290 | 6.983–8.554 |
| M_leanui | warm | flat | 2000 | library_first_render | PASS | 10 | 48.109 | 46.323 | 58.162 | 45.766–59.630 |
| M_leanui | warm | flat | 2000 | library_folder_back | PASS | 10 | 97.198 | 87.338 | 101.971 | 86.569–102.137 |
| M_leanui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.895 | 8.639 | 9.146 | 8.314–9.350 |
| M_leanui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 7.495 | 6.995 | 8.103 | 6.505–9.153 |
| M_leanui | warm | flat | 2000 | open_book | PASS | 10 | 60.330 | 58.015 | 62.174 | 57.261–64.530 |
| M_leanui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 60.948 | 57.067 | 63.096 | 55.515–64.480 |
| M_leanui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.497 | 7.663 | 9.130 | 7.496–9.244 |
| M_leanui | warm | flat | 2000 | repeated_nav | PASS | 2 | 87.631 | 84.530 | 90.733 | 83.755–91.508 |
| M_leanui | warm | flat | 50 | change_sort_mode | PASS | 10 | 9.823 | 8.662 | 11.759 | 8.416–18.474 |
| M_leanui | warm | flat | 50 | close_book | PASS | 10 | 18.004 | 16.062 | 23.917 | 14.652–26.681 |
| M_leanui | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.636 | 7.544 | 9.068 | 7.524–9.216 |
| M_leanui | warm | flat | 50 | home_to_library | PASS | 10 | 8.038 | 7.462 | 9.630 | 7.195–14.397 |
| M_leanui | warm | flat | 50 | library_cached_paging | PASS | 30 | 7.579 | 6.966 | 9.401 | 6.508–11.244 |
| M_leanui | warm | flat | 50 | library_first_render | PASS | 10 | 7.716 | 7.198 | 8.944 | 7.120–12.107 |
| M_leanui | warm | flat | 50 | library_folder_back | PASS | 10 | 10.111 | 9.629 | 16.875 | 9.181–17.060 |
| M_leanui | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.014 | 8.799 | 9.365 | 8.614–9.560 |
| M_leanui | warm | flat | 50 | library_sequential_paging | PASS | 3 | 7.920 | 7.606 | 8.413 | 7.528–8.536 |
| M_leanui | warm | flat | 50 | open_book | PASS | 10 | 44.618 | 43.558 | 46.634 | 42.953–48.314 |
| M_leanui | warm | flat | 50 | open_book_minimal | PASS | 10 | 44.782 | 42.374 | 47.349 | 41.719–47.640 |
| M_leanui | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.391 | 7.764 | 8.599 | 7.453–8.875 |
| M_leanui | warm | flat | 50 | repeated_nav | PASS | 2 | 86.277 | 83.579 | 88.975 | 82.904–89.650 |
| M_leanui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 8.310 | 7.959 | 9.361 | 7.251–9.410 |
| M_leanui | warm | hierarchical | 2000 | close_book | PASS | 10 | 21.749 | 18.665 | 25.316 | 18.026–28.625 |
| M_leanui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 7.938 | 7.526 | 8.389 | 7.520–8.555 |
| M_leanui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 10.509 | 9.309 | 13.098 | 9.253–13.153 |
| M_leanui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 10.485 | 8.934 | 12.573 | 8.713–14.051 |
| M_leanui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 13.592 | 13.079 | 15.931 | 13.042–16.418 |
| M_leanui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.675 | 9.281 | 20.718 | 8.555–27.909 |
| M_leanui | warm | hierarchical | 2000 | open_book | PASS | 10 | 46.565 | 44.006 | 50.894 | 43.567–51.167 |
| M_leanui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 48.086 | 44.837 | 50.444 | 42.240–50.550 |
| M_leanui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.618 | 8.284 | 8.905 | 7.781–9.045 |
| M_leanui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.476 | 8.062 | 9.008 | 7.512–9.755 |
| M_leanui | warm | hierarchical | 50 | close_book | PASS | 10 | 19.279 | 16.338 | 24.196 | 14.660–25.735 |
| M_leanui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.158 | 7.749 | 8.627 | 7.497–8.973 |
| M_leanui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 10.666 | 9.695 | 12.066 | 9.647–12.395 |
| M_leanui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 11.369 | 9.914 | 12.390 | 9.905–12.683 |
| M_leanui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 13.123 | 10.985 | 14.845 | 10.587–16.011 |
| M_leanui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 9.223 | 8.430 | 11.162 | 8.419–12.139 |
| M_leanui | warm | hierarchical | 50 | open_book | PASS | 10 | 42.455 | 40.816 | 45.400 | 40.618–46.736 |
| M_leanui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 42.953 | 40.589 | 47.388 | 40.418–47.501 |
| M_leanui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 7.917 | 7.700 | 9.149 | 7.596–9.187 |
| A_stock | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 14.591 | 14.591 | 14.591 | 14.591–14.591 |
| A_stock | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 13.811 | 13.811 | 13.811 | 13.811–13.811 |
| B_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 13.544 | 13.544 | 13.544 | 13.544–13.544 |
| B_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 10.902 | 10.902 | 10.902 | 10.902–10.902 |
| C_simpleui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 13.326 | 13.326 | 13.326 | 13.326–13.326 |
| C_simpleui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 31.838 | 31.838 | 31.838 | 31.838–31.838 |
| D_zenos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 44.515 | 44.515 | 44.515 | 44.515–44.515 |
| D_zenos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 31.192 | 31.192 | 31.192 | 31.192–31.192 |
| E_project_title | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 10.845 | 10.845 | 10.845 | 10.845–10.845 |
| E_project_title | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 10.403 | 10.403 | 10.403 | 10.403–10.403 |
| F_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 22.621 | 22.621 | 22.621 | 22.621–22.621 |
| F_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 20.576 | 20.576 | 20.576 | 20.576–20.576 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 12.905 | 12.905 | 12.905 | 12.905–12.905 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 30.972 | 30.972 | 30.972 | 30.972–30.972 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 37.832 | 37.832 | 37.832 | 37.832–37.832 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 31.495 | 31.495 | 31.495 | 31.495–31.495 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 23.469 | 23.469 | 23.469 | 23.469–23.469 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 21.191 | 21.191 | 21.191 | 21.191–21.191 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 14.565 | 14.565 | 14.565 | 14.565–14.565 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 31.577 | 31.577 | 31.577 | 31.577–31.577 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 13.029 | 13.029 | 13.029 | 13.029–13.029 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 30.316 | 30.316 | 30.316 | 30.316–30.316 |
| L_project_title_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 22.303 | 22.303 | 22.303 | 22.303–22.303 |
| L_project_title_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 18.990 | 18.990 | 18.990 | 18.990–18.990 |
| M_leanui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 13.271 | 13.271 | 13.271 | 13.271–13.271 |
| M_leanui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 11.999 | 11.999 | 11.999 | 11.999–11.999 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 488.322 | 485.274 | 494.093 | 484.512–495.536 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 522.788 | 518.707 | 526.155 | 517.687–526.997 |
| A_stock | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 529.191 | 524.842 | 532.148 | 523.755–532.887 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 574.735 | 570.626 | 576.874 | 569.598–577.408 |
| A_stock | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 579.938 | 578.812 | 609.043 | 578.530–616.319 |
| A_stock | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 607.269 | 606.655 | 638.143 | 606.502–645.861 |
| A_stock | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 2563.655 | 2532.984 | 2597.015 | 2525.316–2605.355 |
| A_stock | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2669.170 | 2626.082 | 2712.298 | 2615.310–2723.080 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 513.309 | 507.015 | 517.747 | 505.442–518.856 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 553.704 | 548.358 | 558.491 | 547.021–559.688 |
| A_stock | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 2071.696 | 2067.625 | 2123.479 | 2066.608–2136.425 |
| A_stock | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2160.147 | 2132.567 | 2191.101 | 2125.671–2198.839 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 446.015 | 438.135 | 469.501 | 436.164–475.372 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 474.434 | 468.955 | 500.697 | 467.585–507.263 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 479.933 | 475.167 | 506.548 | 473.975–513.201 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 521.673 | 519.651 | 551.874 | 519.146–559.424 |
| A_stock | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 577.881 | 577.881 | 577.881 | 577.881–577.881 |
| A_stock | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4307.399 | 4307.399 | 4307.399 | 4307.399–4307.399 |
| A_stock | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 19885.204 | 19885.204 | 19885.204 | 19885.204–19885.204 |
| A_stock | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 19938.582 | 19938.582 | 19938.582 | 19938.582–19938.582 |
| A_stock | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 513.491 | 513.491 | 513.491 | 513.491–513.491 |
| A_stock | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1987.846 | 1987.846 | 1987.846 | 1987.846–1987.846 |
| A_stock | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11906.907 | 11906.907 | 11906.907 | 11906.907–11906.907 |
| A_stock | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11971.091 | 11971.091 | 11971.091 | 11971.091–11971.091 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 492.541 | 492.541 | 492.541 | 492.541–492.541 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1011.418 | 1011.418 | 1011.418 | 1011.418–1011.418 |
| A_stock | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7492.360 | 7492.360 | 7492.360 | 7492.360–7492.360 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7555.070 | 7555.070 | 7555.070 | 7555.070–7555.070 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 491.099 | 491.099 | 491.099 | 491.099–491.099 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1000.575 | 1000.575 | 1000.575 | 1000.575–1000.575 |
| A_stock | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5876.132 | 5876.132 | 5876.132 | 5876.132–5876.132 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5932.133 | 5932.133 | 5932.133 | 5932.133–5932.133 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 492.200 | 492.025 | 496.231 | 491.981–497.239 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 525.931 | 524.124 | 529.524 | 523.673–530.422 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 532.127 | 530.123 | 535.507 | 529.622–536.352 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 575.037 | 575.020 | 578.997 | 575.015–579.987 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 589.095 | 582.361 | 606.187 | 580.678–610.460 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 616.796 | 610.370 | 636.718 | 608.763–641.698 |
| B_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 10515.745 | 10503.767 | 10978.743 | 10500.773–11094.493 |
| B_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 10569.265 | 10555.175 | 11149.283 | 10551.653–11294.288 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 513.688 | 507.764 | 523.795 | 506.283–526.322 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 558.730 | 551.146 | 565.307 | 549.250–566.951 |
| B_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 9302.150 | 9228.149 | 9352.085 | 9209.649–9364.569 |
| B_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9350.836 | 9279.288 | 9401.671 | 9261.401–9414.380 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 457.148 | 455.624 | 485.793 | 455.243–492.954 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 485.734 | 484.410 | 515.780 | 484.079–523.291 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 491.455 | 490.234 | 522.117 | 489.929–529.783 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 535.888 | 534.402 | 567.405 | 534.031–575.284 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 577.848 | 577.848 | 577.848 | 577.848–577.848 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4514.675 | 4514.675 | 4514.675 | 4514.675–4514.675 |
| B_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 29817.652 | 29817.652 | 29817.652 | 29817.652–29817.652 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 29899.706 | 29899.706 | 29899.706 | 29899.706–29899.706 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 549.411 | 549.411 | 549.411 | 549.411–549.411 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2086.854 | 2086.854 | 2086.854 | 2086.854–2086.854 |
| B_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 16273.627 | 16273.627 | 16273.627 | 16273.627–16273.627 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 16327.954 | 16327.954 | 16327.954 | 16327.954–16327.954 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 533.188 | 533.188 | 533.188 | 533.188–533.188 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1045.494 | 1045.494 | 1045.494 | 1045.494–1045.494 |
| B_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 8046.943 | 8046.943 | 8046.943 | 8046.943–8046.943 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 8100.529 | 8100.529 | 8100.529 | 8100.529–8100.529 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 496.855 | 496.855 | 496.855 | 496.855–496.855 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 986.985 | 986.985 | 986.985 | 986.985–986.985 |
| B_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6929.644 | 6929.644 | 6929.644 | 6929.644–6929.644 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6988.538 | 6988.538 | 6988.538 | 6988.538–6988.538 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 611.444 | 609.357 | 612.162 | 608.836–612.341 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 663.436 | 663.048 | 667.649 | 662.951–668.702 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 672.753 | 672.114 | 677.371 | 671.954–678.526 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 717.727 | 717.138 | 722.313 | 716.991–723.459 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 729.866 | 720.848 | 740.477 | 718.594–743.130 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 774.424 | 762.534 | 778.114 | 759.561–779.037 |
| C_simpleui | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 2872.339 | 2494.746 | 2876.766 | 2400.347–2877.872 |
| C_simpleui | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2923.709 | 2542.812 | 2925.565 | 2447.588–2926.029 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 611.770 | 606.021 | 617.375 | 604.584–618.776 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 652.346 | 651.527 | 662.757 | 651.323–665.360 |
| C_simpleui | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 2308.838 | 2061.375 | 2331.307 | 1999.509–2336.925 |
| C_simpleui | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2356.515 | 2107.668 | 2378.072 | 2045.456–2383.461 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 559.655 | 551.885 | 581.250 | 549.942–586.649 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 612.228 | 603.842 | 635.281 | 601.745–641.044 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 621.748 | 613.101 | 644.167 | 610.939–649.772 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 666.529 | 661.150 | 689.452 | 659.805–695.183 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 757.981 | 757.981 | 757.981 | 757.981–757.981 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2688.597 | 2688.597 | 2688.597 | 2688.597–2688.597 |
| C_simpleui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 29557.687 | 29557.687 | 29557.687 | 29557.687–29557.687 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 29833.955 | 29833.955 | 29833.955 | 29833.955–29833.955 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 660.602 | 660.602 | 660.602 | 660.602–660.602 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2278.121 | 2278.121 | 2278.121 | 2278.121–2278.121 |
| C_simpleui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 16082.616 | 16082.616 | 16082.616 | 16082.616–16082.616 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 16154.093 | 16154.093 | 16154.093 | 16154.093–16154.093 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 632.632 | 632.632 | 632.632 | 632.632–632.632 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1714.263 | 1714.263 | 1714.263 | 1714.263–1714.263 |
| C_simpleui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 12947.488 | 12947.488 | 12947.488 | 12947.488–12947.488 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 13016.898 | 13016.898 | 13016.898 | 13016.898–13016.898 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 654.934 | 654.934 | 654.934 | 654.934–654.934 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1784.341 | 1784.341 | 1784.341 | 1784.341–1784.341 |
| C_simpleui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 12012.463 | 12012.463 | 12012.463 | 12012.463–12012.463 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 12082.311 | 12082.311 | 12082.311 | 12082.311–12082.311 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 688.523 | 679.658 | 688.592 | 677.441–688.610 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 786.225 | 783.185 | 792.056 | 782.425–793.514 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 797.779 | 795.622 | 802.970 | 795.082–804.268 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 845.125 | 841.559 | 849.797 | 840.668–850.965 |
| D_zenos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 703.545 | 696.951 | 725.500 | 695.303–730.988 |
| D_zenos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 859.007 | 846.915 | 875.036 | 843.892–879.043 |
| D_zenos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 2023.361 | 2020.569 | 2030.379 | 2019.871–2032.133 |
| D_zenos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2086.519 | 2075.909 | 2094.932 | 2073.256–2097.036 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 703.850 | 701.900 | 705.743 | 701.413–706.216 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 748.008 | 742.575 | 749.888 | 741.217–750.358 |
| D_zenos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1862.765 | 1832.945 | 1871.696 | 1825.490–1873.928 |
| D_zenos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1920.775 | 1881.037 | 1920.831 | 1871.102–1920.845 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 620.286 | 616.566 | 656.669 | 615.636–665.765 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 709.980 | 706.137 | 725.895 | 705.177–729.874 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 722.160 | 718.358 | 737.935 | 717.407–741.879 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 768.684 | 764.943 | 785.500 | 764.007–789.703 |
| D_zenos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 698.140 | 698.140 | 698.140 | 698.140–698.140 |
| D_zenos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4581.489 | 4581.489 | 4581.489 | 4581.489–4581.489 |
| D_zenos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 19426.929 | 19426.929 | 19426.929 | 19426.929–19426.929 |
| D_zenos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 19568.128 | 19568.128 | 19568.128 | 19568.128–19568.128 |
| D_zenos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 728.547 | 728.547 | 728.547 | 728.547–728.547 |
| D_zenos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2769.501 | 2769.501 | 2769.501 | 2769.501–2769.501 |
| D_zenos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 13000.563 | 13000.563 | 13000.563 | 13000.563–13000.563 |
| D_zenos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 13062.527 | 13062.527 | 13062.527 | 13062.527–13062.527 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 689.938 | 689.938 | 689.938 | 689.938–689.938 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2282.939 | 2282.939 | 2282.939 | 2282.939–2282.939 |
| D_zenos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11042.102 | 11042.102 | 11042.102 | 11042.102–11042.102 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11104.991 | 11104.991 | 11104.991 | 11104.991–11104.991 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 698.492 | 698.492 | 698.492 | 698.492–698.492 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2245.236 | 2245.236 | 2245.236 | 2245.236–2245.236 |
| D_zenos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10517.535 | 10517.535 | 10517.535 | 10517.535–10517.535 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10581.379 | 10581.379 | 10581.379 | 10581.379–10581.379 |
| E_project_title | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 575.081 | 545.314 | 587.118 | 537.872–590.127 |
| E_project_title | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 599.394 | 567.790 | 610.649 | 559.889–613.462 |
| E_project_title | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1740.359 | 1689.198 | 1745.453 | 1676.408–1746.726 |
| E_project_title | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1785.180 | 1734.356 | 1790.767 | 1721.650–1792.164 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 495.325 | 480.294 | 534.134 | 476.536–543.836 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 533.316 | 516.029 | 577.605 | 511.707–588.678 |
| E_project_title | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1351.596 | 1338.432 | 1432.963 | 1335.141–1453.305 |
| E_project_title | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1396.028 | 1383.710 | 1479.764 | 1380.630–1500.697 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 447.085 | 446.674 | 462.087 | 446.571–465.838 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 479.233 | 478.998 | 492.276 | 478.939–495.537 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 485.270 | 484.716 | 497.998 | 484.578–501.180 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 532.638 | 529.482 | 544.188 | 528.693–547.075 |
| E_project_title | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 541.106 | 541.106 | 541.106 | 541.106–541.106 |
| E_project_title | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2744.891 | 2744.891 | 2744.891 | 2744.891–2744.891 |
| E_project_title | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 12736.284 | 12736.284 | 12736.284 | 12736.284–12736.284 |
| E_project_title | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12787.269 | 12787.269 | 12787.269 | 12787.269–12787.269 |
| E_project_title | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 497.123 | 497.123 | 497.123 | 497.123–497.123 |
| E_project_title | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 855.598 | 855.598 | 855.598 | 855.598–855.598 |
| E_project_title | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 4779.450 | 4779.450 | 4779.450 | 4779.450–4779.450 |
| E_project_title | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4828.538 | 4828.538 | 4828.538 | 4828.538–4828.538 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 480.784 | 480.784 | 480.784 | 480.784–480.784 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 890.578 | 890.578 | 890.578 | 890.578–890.578 |
| E_project_title | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 4757.585 | 4757.585 | 4757.585 | 4757.585–4757.585 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 4806.492 | 4806.492 | 4806.492 | 4806.492–4806.492 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 489.301 | 489.301 | 489.301 | 489.301–489.301 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 911.212 | 911.212 | 911.212 | 911.212–911.212 |
| E_project_title | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4351.946 | 4351.946 | 4351.946 | 4351.946–4351.946 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4399.713 | 4399.713 | 4399.713 | 4399.713–4399.713 |
| F_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 611.147 | 592.800 | 621.368 | 588.213–623.923 |
| F_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 638.333 | 619.663 | 651.348 | 614.995–654.602 |
| F_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 2679.585 | 2636.241 | 2691.472 | 2625.405–2694.443 |
| F_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2775.508 | 2766.323 | 2810.026 | 2764.026–2818.655 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 510.751 | 508.474 | 542.222 | 507.905–550.090 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 563.802 | 562.295 | 596.361 | 561.919–604.501 |
| F_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 2185.956 | 2148.227 | 2188.321 | 2138.795–2188.912 |
| F_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2240.354 | 2203.014 | 2251.207 | 2193.679–2253.920 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 471.498 | 463.900 | 505.048 | 462.001–513.435 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 519.994 | 510.064 | 553.213 | 507.582–561.518 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 526.971 | 517.397 | 559.876 | 515.004–568.103 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 570.098 | 560.553 | 606.493 | 558.167–615.592 |
| F_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 607.745 | 607.745 | 607.745 | 607.745–607.745 |
| F_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4118.397 | 4118.397 | 4118.397 | 4118.397–4118.397 |
| F_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 18362.068 | 18362.068 | 18362.068 | 18362.068–18362.068 |
| F_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 18479.224 | 18479.224 | 18479.224 | 18479.224–18479.224 |
| F_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 546.217 | 546.217 | 546.217 | 546.217–546.217 |
| F_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2415.272 | 2415.272 | 2415.272 | 2415.272–2415.272 |
| F_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11178.429 | 11178.429 | 11178.429 | 11178.429–11178.429 |
| F_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11243.546 | 11243.546 | 11243.546 | 11243.546–11243.546 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 524.338 | 524.338 | 524.338 | 524.338–524.338 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1363.084 | 1363.084 | 1363.084 | 1363.084–1363.084 |
| F_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 8453.366 | 8453.366 | 8453.366 | 8453.366–8453.366 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 8504.808 | 8504.808 | 8504.808 | 8504.808–8504.808 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 538.694 | 538.694 | 538.694 | 538.694–538.694 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1356.122 | 1356.122 | 1356.122 | 1356.122–1356.122 |
| F_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6483.549 | 6483.549 | 6483.549 | 6483.549–6483.549 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6532.621 | 6532.621 | 6532.621 | 6532.621–6532.621 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 703.932 | 701.537 | 710.396 | 700.938–712.012 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 743.697 | 740.604 | 752.913 | 739.830–755.216 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 10503.768 | 10471.549 | 10907.222 | 10463.494–11008.085 |
| G_simpleui_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 10560.805 | 10528.802 | 10994.650 | 10520.801–11103.111 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 630.940 | 628.833 | 754.621 | 628.306–785.542 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 678.086 | 676.155 | 803.383 | 675.673–834.707 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 8888.491 | 8819.398 | 9001.090 | 8802.125–9029.239 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8950.468 | 8872.562 | 9053.022 | 8853.085–9078.660 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 567.713 | 566.063 | 584.055 | 565.651–588.140 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 620.956 | 620.934 | 636.573 | 620.928–640.477 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 631.726 | 630.580 | 645.983 | 630.293–649.547 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 678.799 | 676.301 | 692.083 | 675.677–695.404 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 710.584 | 710.584 | 710.584 | 710.584–710.584 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3006.411 | 3006.411 | 3006.411 | 3006.411–3006.411 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 46436.203 | 46436.203 | 46436.203 | 46436.203–46436.203 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 46531.958 | 46531.958 | 46531.958 | 46531.958–46531.958 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 658.719 | 658.719 | 658.719 | 658.719–658.719 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1978.614 | 1978.614 | 1978.614 | 1978.614–1978.614 |
| G_simpleui_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 23617.899 | 23617.899 | 23617.899 | 23617.899–23617.899 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 23693.208 | 23693.208 | 23693.208 | 23693.208–23693.208 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 630.237 | 630.237 | 630.237 | 630.237–630.237 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1735.507 | 1735.507 | 1735.507 | 1735.507–1735.507 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 14998.492 | 14998.492 | 14998.492 | 14998.492–14998.492 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 15070.793 | 15070.793 | 15070.793 | 15070.793–15070.793 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 723.183 | 723.183 | 723.183 | 723.183–723.183 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1584.131 | 1584.131 | 1584.131 | 1584.131–1584.131 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 13784.316 | 13784.316 | 13784.316 | 13784.316–13784.316 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 13858.496 | 13858.496 | 13858.496 | 13858.496–13858.496 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 744.279 | 709.993 | 755.269 | 701.422–758.016 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 894.934 | 861.468 | 906.586 | 853.102–909.500 |
| H_zenos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 9812.206 | 9790.326 | 9985.015 | 9784.856–10028.217 |
| H_zenos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9864.774 | 9843.530 | 10038.805 | 9838.219–10082.313 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 690.641 | 683.421 | 711.650 | 681.616–716.902 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 733.141 | 723.813 | 757.537 | 721.481–763.636 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 7972.262 | 7876.072 | 8049.861 | 7852.025–8069.261 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8022.993 | 7930.274 | 8102.430 | 7907.095–8122.289 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 633.564 | 627.008 | 660.918 | 625.370–667.756 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 719.035 | 715.013 | 744.601 | 714.007–750.993 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 729.685 | 726.669 | 756.791 | 725.914–763.567 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 774.233 | 773.219 | 803.305 | 772.965–810.573 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 692.058 | 692.058 | 692.058 | 692.058–692.058 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4615.607 | 4615.607 | 4615.607 | 4615.607–4615.607 |
| H_zenos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 26949.336 | 26949.336 | 26949.336 | 26949.336–26949.336 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 27017.231 | 27017.231 | 27017.231 | 27017.231–27017.231 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 736.100 | 736.100 | 736.100 | 736.100–736.100 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2739.877 | 2739.877 | 2739.877 | 2739.877–2739.877 |
| H_zenos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 17900.163 | 17900.163 | 17900.163 | 17900.163–17900.163 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 17961.990 | 17961.990 | 17961.990 | 17961.990–17961.990 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 693.776 | 693.776 | 693.776 | 693.776–693.776 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2277.437 | 2277.437 | 2277.437 | 2277.437–2277.437 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 12045.045 | 12045.045 | 12045.045 | 12045.045–12045.045 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12109.906 | 12109.906 | 12109.906 | 12109.906–12109.906 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 824.337 | 824.337 | 824.337 | 824.337–824.337 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2378.426 | 2378.426 | 2378.426 | 2378.426–2378.426 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 11809.620 | 11809.620 | 11809.620 | 11809.620–11809.620 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11874.577 | 11874.577 | 11874.577 | 11874.577–11874.577 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 606.285 | 595.519 | 613.785 | 592.828–615.660 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 635.236 | 625.866 | 642.287 | 623.523–644.049 |
| I_vos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 10271.933 | 8369.822 | 10426.016 | 7894.295–10464.537 |
| I_vos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 10321.875 | 8420.558 | 10475.781 | 7945.229–10514.258 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 518.546 | 504.388 | 520.208 | 500.848–520.624 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 572.130 | 557.728 | 575.735 | 554.128–576.636 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 9025.970 | 7055.177 | 9073.319 | 6562.478–9085.156 |
| I_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 9075.411 | 7104.555 | 9122.145 | 6611.841–9133.829 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 506.727 | 479.902 | 521.821 | 473.195–525.594 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 558.809 | 528.843 | 572.098 | 521.352–575.421 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 566.242 | 535.475 | 578.903 | 527.783–582.068 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 609.738 | 578.649 | 622.355 | 570.876–625.509 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 770.499 | 770.499 | 770.499 | 770.499–770.499 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4404.100 | 4404.100 | 4404.100 | 4404.100–4404.100 |
| I_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 27026.030 | 27026.030 | 27026.030 | 27026.030–27026.030 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 27178.848 | 27178.848 | 27178.848 | 27178.848–27178.848 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 553.720 | 553.720 | 553.720 | 553.720–553.720 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1724.559 | 1724.559 | 1724.559 | 1724.559–1724.559 |
| I_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 14525.532 | 14525.532 | 14525.532 | 14525.532–14525.532 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 14607.189 | 14607.189 | 14607.189 | 14607.189–14607.189 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 529.170 | 529.170 | 529.170 | 529.170–529.170 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1371.293 | 1371.293 | 1371.293 | 1371.293–1371.293 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9716.573 | 9716.573 | 9716.573 | 9716.573–9716.573 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9774.213 | 9774.213 | 9774.213 | 9774.213–9774.213 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 530.982 | 530.982 | 530.982 | 530.982–530.982 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1347.361 | 1347.361 | 1347.361 | 1347.361–1347.361 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 7435.563 | 7435.563 | 7435.563 | 7435.563–7435.563 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7486.469 | 7486.469 | 7486.469 | 7486.469–7486.469 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 730.674 | 712.289 | 738.373 | 707.693–740.298 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 769.302 | 750.996 | 778.654 | 746.420–780.992 |
| J_simpleui_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 2887.938 | 2832.564 | 2910.339 | 2818.721–2915.939 |
| J_simpleui_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2936.037 | 2879.912 | 2957.971 | 2865.881–2963.455 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 643.190 | 639.994 | 646.010 | 639.194–646.714 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 690.344 | 687.128 | 691.217 | 686.324–691.435 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 2337.682 | 2121.602 | 2346.455 | 2067.583–2348.648 |
| J_simpleui_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 2385.652 | 2169.159 | 2393.808 | 2115.036–2395.846 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 561.701 | 559.825 | 586.307 | 559.356–592.459 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 616.875 | 613.879 | 636.309 | 613.130–641.167 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 627.267 | 624.068 | 645.957 | 623.269–650.630 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 674.470 | 670.895 | 692.739 | 670.002–697.306 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 738.262 | 738.262 | 738.262 | 738.262–738.262 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2640.108 | 2640.108 | 2640.108 | 2640.108–2640.108 |
| J_simpleui_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 30988.908 | 30988.908 | 30988.908 | 30988.908–30988.908 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 31103.931 | 31103.931 | 31103.931 | 31103.931–31103.931 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 695.842 | 695.842 | 695.842 | 695.842–695.842 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2235.420 | 2235.420 | 2235.420 | 2235.420–2235.420 |
| J_simpleui_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 15049.898 | 15049.898 | 15049.898 | 15049.898–15049.898 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 15224.845 | 15224.845 | 15224.845 | 15224.845–15224.845 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 630.010 | 630.010 | 630.010 | 630.010–630.010 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1493.179 | 1493.179 | 1493.179 | 1493.179–1493.179 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 13165.614 | 13165.614 | 13165.614 | 13165.614–13165.614 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 13239.650 | 13239.650 | 13239.650 | 13239.650–13239.650 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 619.206 | 619.206 | 619.206 | 619.206–619.206 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1648.128 | 1648.128 | 1648.128 | 1648.128–1648.128 |
| J_simpleui_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 11146.075 | 11146.075 | 11146.075 | 11146.075–11146.075 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11218.615 | 11218.615 | 11218.615 | 11218.615–11218.615 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 711.070 | 711.069 | 764.077 | 711.068–777.329 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 751.887 | 749.259 | 802.407 | 748.601–815.036 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 10381.586 | 10368.898 | 10425.666 | 10365.726–10436.686 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 10438.650 | 10425.684 | 10484.389 | 10422.443–10495.824 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 625.972 | 623.631 | 654.449 | 623.046–661.568 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 676.859 | 671.114 | 699.648 | 669.678–705.346 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 8838.462 | 7347.428 | 8851.157 | 6974.670–8854.331 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 8888.975 | 7401.603 | 8901.697 | 7029.760–8904.877 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 576.313 | 574.088 | 592.338 | 573.532–596.345 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 628.611 | 626.395 | 645.002 | 625.841–649.100 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 637.814 | 636.160 | 654.504 | 635.746–658.677 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 684.880 | 681.701 | 704.149 | 680.906–708.966 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 994.757 | 994.757 | 994.757 | 994.757–994.757 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3476.419 | 3476.419 | 3476.419 | 3476.419–3476.419 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 44000.094 | 44000.094 | 44000.094 | 44000.094–44000.094 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 44355.593 | 44355.593 | 44355.593 | 44355.593–44355.593 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 641.750 | 641.750 | 641.750 | 641.750–641.750 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1889.136 | 1889.136 | 1889.136 | 1889.136–1889.136 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 19849.630 | 19849.630 | 19849.630 | 19849.630–19849.630 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 20062.101 | 20062.101 | 20062.101 | 20062.101–20062.101 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 640.218 | 640.218 | 640.218 | 640.218–640.218 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1527.529 | 1527.529 | 1527.529 | 1527.529–1527.529 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 15392.432 | 15392.432 | 15392.432 | 15392.432–15392.432 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 15468.059 | 15468.059 | 15468.059 | 15468.059–15468.059 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 820.909 | 820.909 | 820.909 | 820.909–820.909 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1899.048 | 1899.048 | 1899.048 | 1899.048–1899.048 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 14953.163 | 14953.163 | 14953.163 | 14953.163–14953.163 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 15027.045 | 15027.045 | 15027.045 | 15027.045–15027.045 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 540.717 | 535.795 | 545.054 | 534.565–546.139 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 590.377 | 586.138 | 597.014 | 585.078–598.673 |
| K_vos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 597.817 | 593.256 | 603.578 | 592.115–605.018 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 644.385 | 637.482 | 647.530 | 635.756–648.317 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 585.599 | 576.793 | 590.230 | 574.591–591.388 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 610.874 | 599.787 | 614.762 | 597.015–615.734 |
| L_project_title_vos | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1674.886 | 1659.996 | 1694.004 | 1656.273–1698.784 |
| L_project_title_vos | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1721.782 | 1705.020 | 1740.041 | 1700.829–1744.605 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 496.228 | 495.339 | 496.997 | 495.117–497.189 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 542.332 | 539.500 | 543.012 | 538.793–543.182 |
| L_project_title_vos | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1351.536 | 1341.033 | 1358.098 | 1338.408–1359.738 |
| L_project_title_vos | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1396.749 | 1385.072 | 1402.151 | 1382.153–1403.501 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 480.222 | 473.443 | 483.692 | 471.749–484.560 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 526.941 | 523.203 | 532.685 | 522.268–534.121 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 533.720 | 530.268 | 539.335 | 529.405–540.739 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 577.279 | 576.022 | 582.884 | 575.708–584.285 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 591.931 | 591.931 | 591.931 | 591.931–591.931 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3338.090 | 3338.090 | 3338.090 | 3338.090–3338.090 |
| L_project_title_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 14634.949 | 14634.949 | 14634.949 | 14634.949–14634.949 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 14686.967 | 14686.967 | 14686.967 | 14686.967–14686.967 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 519.289 | 519.289 | 519.289 | 519.289–519.289 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1566.632 | 1566.632 | 1566.632 | 1566.632–1566.632 |
| L_project_title_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 7150.401 | 7150.401 | 7150.401 | 7150.401–7150.401 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7198.205 | 7198.205 | 7198.205 | 7198.205–7198.205 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 500.238 | 500.238 | 500.238 | 500.238–500.238 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1248.796 | 1248.796 | 1248.796 | 1248.796–1248.796 |
| L_project_title_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 5916.667 | 5916.667 | 5916.667 | 5916.667–5916.667 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 5964.547 | 5964.547 | 5964.547 | 5964.547–5964.547 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 514.025 | 514.025 | 514.025 | 514.025–514.025 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1277.469 | 1277.469 | 1277.469 | 1277.469–1277.469 |
| L_project_title_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5325.061 | 5325.061 | 5325.061 | 5325.061–5325.061 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5374.464 | 5374.464 | 5374.464 | 5374.464–5374.464 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 491.338 | 490.582 | 493.031 | 490.394–493.455 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 524.132 | 522.568 | 524.688 | 522.177–524.827 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 529.764 | 528.089 | 530.411 | 527.671–530.573 |
| M_leanui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 572.675 | 570.101 | 573.167 | 569.458–573.290 |
| M_leanui | paging | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 554.643 | 551.882 | 559.332 | 551.191–560.505 |
| M_leanui | paging | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 574.731 | 573.458 | 581.474 | 573.140–583.160 |
| M_leanui | paging | flat | 2000 | process:complete_marker_ms | PASS | 3 | 1694.387 | 1669.685 | 1714.314 | 1663.509–1719.296 |
| M_leanui | paging | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1741.116 | 1714.921 | 1759.618 | 1708.372–1764.244 |
| M_leanui | paging | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 475.782 | 472.751 | 483.294 | 471.994–485.172 |
| M_leanui | paging | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 512.137 | 507.519 | 521.018 | 506.365–523.239 |
| M_leanui | paging | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 1334.114 | 1319.307 | 1359.188 | 1315.605–1365.457 |
| M_leanui | paging | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1377.461 | 1362.851 | 1403.021 | 1359.199–1409.411 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 459.317 | 449.566 | 487.643 | 447.128–494.725 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 488.329 | 479.080 | 518.341 | 476.768–525.844 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 493.851 | 484.681 | 524.643 | 482.389–532.341 |
| M_leanui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 536.015 | 530.264 | 569.373 | 528.826–577.712 |
| M_leanui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 551.129 | 551.129 | 551.129 | 551.129–551.129 |
| M_leanui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2418.781 | 2418.781 | 2418.781 | 2418.781–2418.781 |
| M_leanui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 11692.850 | 11692.850 | 11692.850 | 11692.850–11692.850 |
| M_leanui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11744.836 | 11744.836 | 11744.836 | 11744.836–11744.836 |
| M_leanui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 510.203 | 510.203 | 510.203 | 510.203–510.203 |
| M_leanui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 870.697 | 870.697 | 870.697 | 870.697–870.697 |
| M_leanui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 4931.718 | 4931.718 | 4931.718 | 4931.718–4931.718 |
| M_leanui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4981.327 | 4981.327 | 4981.327 | 4981.327–4981.327 |
| M_leanui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 486.759 | 486.759 | 486.759 | 486.759–486.759 |
| M_leanui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 921.423 | 921.423 | 921.423 | 921.423–921.423 |
| M_leanui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 4857.227 | 4857.227 | 4857.227 | 4857.227–4857.227 |
| M_leanui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 4905.532 | 4905.532 | 4905.532 | 4905.532–4905.532 |
| M_leanui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 493.493 | 493.493 | 493.493 | 493.493–493.493 |
| M_leanui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 925.694 | 925.694 | 925.694 | 925.694–925.694 |
| M_leanui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4345.726 | 4345.726 | 4345.726 | 4345.726–4345.726 |
| M_leanui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4394.110 | 4394.110 | 4394.110 | 4394.110–4394.110 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 508.002 | 508.002 | 508.002 | 508.002–508.002 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 544.016 | 544.016 | 544.016 | 544.016–544.016 |
| A_stock | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 550.135 | 550.135 | 550.135 | 550.135–550.135 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 595.526 | 595.526 | 595.526 | 595.526–595.526 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 516.007 | 516.007 | 516.007 | 516.007–516.007 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 548.501 | 548.501 | 548.501 | 548.501–548.501 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 555.155 | 555.155 | 555.155 | 555.155–555.155 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 598.486 | 598.486 | 598.486 | 598.486–598.486 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 617.254 | 617.254 | 617.254 | 617.254–617.254 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 673.027 | 673.027 | 673.027 | 673.027–673.027 |
| C_simpleui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 682.248 | 682.248 | 682.248 | 682.248–682.248 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 727.438 | 727.438 | 727.438 | 727.438–727.438 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 687.269 | 687.269 | 687.269 | 687.269–687.269 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 786.373 | 786.373 | 786.373 | 786.373–786.373 |
| D_zenos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 797.220 | 797.220 | 797.220 | 797.220–797.220 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 846.389 | 846.389 | 846.389 | 846.389–846.389 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 472.364 | 472.364 | 472.364 | 472.364–472.364 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 500.615 | 500.615 | 500.615 | 500.615–500.615 |
| E_project_title | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 507.002 | 507.002 | 507.002 | 507.002–507.002 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 554.674 | 554.674 | 554.674 | 554.674–554.674 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 536.770 | 536.770 | 536.770 | 536.770–536.770 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 587.156 | 587.156 | 587.156 | 587.156–587.156 |
| F_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 593.718 | 593.718 | 593.718 | 593.718–593.718 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 636.802 | 636.802 | 636.802 | 636.802–636.802 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 628.434 | 628.434 | 628.434 | 628.434–628.434 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 683.096 | 683.096 | 683.096 | 683.096–683.096 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 693.998 | 693.998 | 693.998 | 693.998–693.998 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 739.295 | 739.295 | 739.295 | 739.295–739.295 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 687.170 | 687.170 | 687.170 | 687.170–687.170 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 783.691 | 783.691 | 783.691 | 783.691–783.691 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 795.692 | 795.692 | 795.692 | 795.692–795.692 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 843.645 | 843.645 | 843.645 | 843.645–843.645 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 544.062 | 544.062 | 544.062 | 544.062–544.062 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 596.453 | 596.453 | 596.453 | 596.453–596.453 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 603.556 | 603.556 | 603.556 | 603.556–603.556 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 647.626 | 647.626 | 647.626 | 647.626–647.626 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 630.557 | 630.557 | 630.557 | 630.557–630.557 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 688.149 | 688.149 | 688.149 | 688.149–688.149 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 698.730 | 698.730 | 698.730 | 698.730–698.730 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 744.947 | 744.947 | 744.947 | 744.947–744.947 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 628.184 | 628.184 | 628.184 | 628.184–628.184 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 682.710 | 682.710 | 682.710 | 682.710–682.710 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 692.489 | 692.489 | 692.489 | 692.489–692.489 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 742.159 | 742.159 | 742.159 | 742.159–742.159 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 507.847 | 507.847 | 507.847 | 507.847–507.847 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 556.559 | 556.559 | 556.559 | 556.559–556.559 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 563.146 | 563.146 | 563.146 | 563.146–563.146 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 606.257 | 606.257 | 606.257 | 606.257–606.257 |
| M_leanui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 510.006 | 510.006 | 510.006 | 510.006–510.006 |
| M_leanui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 542.675 | 542.675 | 542.675 | 542.675–542.675 |
| M_leanui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 549.183 | 549.183 | 549.183 | 549.183–549.183 |
| M_leanui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 596.764 | 596.764 | 596.764 | 596.764–596.764 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8312.817 | 8320.730 | 8298.071–8322.708 | 14106.199 | 164672.000 |
| A_stock | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8372.122 | 8388.500 | 8338.396–8392.595 | 9120.399 | 173120.000 |
| A_stock | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 10914.454 | 10926.426 | 10833.563–10929.419 | 16566.264 | 168048.000 |
| A_stock | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 11489.892 | 11498.820 | 11459.653–11501.052 | 15431.110 | 192560.000 |
| A_stock | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8296.712 | 8303.078 | 8255.567–8304.669 | 14580.519 | 164992.000 |
| A_stock | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 9207.716 | 9235.716 | 9203.860–9242.716 | 9259.556 | 193664.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8225.825 | 8233.394 | 8182.063–8235.286 | 11864.188 | 159600.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8249.638 | 8282.053 | 8190.231–8290.157 | 8903.759 | 168256.000 |
| A_stock | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 10885.419 | 10885.419 | 10885.419–10885.419 | 16627.817 | 167552.000 |
| A_stock | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 25535.966 | 25535.966 | 25535.966–25535.966 | 45991.380 | 274496.000 |
| A_stock | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 18952.227 | 18952.227 | 18952.227–18952.227 | 18969.453 | 283248.000 |
| A_stock | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8583.325 | 8583.325 | 8583.325–8583.325 | 15119.972 | 164832.000 |
| A_stock | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 27138.524 | 27138.524 | 27138.524–27138.524 | 36586.888 | 218928.000 |
| A_stock | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13638.230 | 13638.230 | 13638.230–13638.230 | 19453.181 | 255008.000 |
| A_stock | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8329.356 | 8329.356 | 8329.356–8329.356 | 14465.431 | 164240.000 |
| A_stock | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8297.173 | 8297.173 | 8297.173–8297.173 | 9690.709 | 176032.000 |
| A_stock | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 18832.595 | 18832.595 | 18832.595–18832.595 | 27266.992 | 220224.000 |
| A_stock | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8299.771 | 8299.771 | 8299.771–8299.771 | 14740.645 | 164608.000 |
| A_stock | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8321.009 | 8321.009 | 8321.009–8321.009 | 9645.729 | 177072.000 |
| A_stock | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 14145.254 | 14145.254 | 14145.254–14145.254 | 21354.380 | 210272.000 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8515.888 | 8652.919 | 8501.610–8687.177 | 9287.544 | 165408.000 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8591.720 | 8668.242 | 8581.892–8687.372 | 9366.784 | 174032.000 |
| B_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 11157.454 | 11166.342 | 11077.919–11168.563 | 16653.236 | 168800.000 |
| B_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 16793.432 | 16953.157 | 16789.908–16993.088 | 17369.168 | 205120.000 |
| B_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8526.224 | 8533.621 | 8515.192–8535.470 | 9201.156 | 166688.000 |
| B_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 13849.980 | 13852.877 | 13813.727–13853.602 | 21978.265 | 201840.000 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8390.544 | 8488.010 | 8363.778–8512.376 | 13527.799 | 159792.000 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8388.763 | 8463.510 | 8356.747–8482.196 | 9053.546 | 168464.000 |
| B_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11130.048 | 11130.048 | 11130.048–11130.048 | 16593.708 | 167296.000 |
| B_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 28042.865 | 28042.865 | 28042.865–28042.865 | 59814.245 | 268128.000 |
| B_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 20100.533 | 20100.533 | 20100.533–20100.533 | 23521.439 | 290368.000 |
| B_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8865.466 | 8865.466 | 8865.466–8865.466 | 9533.641 | 165824.000 |
| B_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 27357.665 | 27357.665 | 27357.665–27357.665 | 37551.038 | 222704.000 |
| B_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 18840.571 | 18840.571 | 18840.571–18840.571 | 22899.157 | 273120.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8556.196 | 8556.196 | 8556.196–8556.196 | 9169.000 | 167040.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8451.505 | 8451.505 | 8451.505–8451.505 | 9805.966 | 179056.000 |
| B_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 21001.345 | 21001.345 | 21001.345–21001.345 | 43199.688 | 253824.000 |
| B_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8557.067 | 8557.067 | 8557.067–8557.067 | 9481.303 | 165344.000 |
| B_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8430.532 | 8430.532 | 8430.532–8430.532 | 9766.994 | 179056.000 |
| B_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 16217.696 | 16217.696 | 16217.696–16217.696 | 34534.641 | 235120.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12490.209 | 12509.212 | 12448.033–12513.963 | 18646.225 | 170880.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 12675.002 | 12752.521 | 12671.393–12771.900 | 13900.043 | 177536.000 |
| C_simpleui | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 14770.826 | 14792.273 | 14715.732–14797.635 | 18878.904 | 176848.000 |
| C_simpleui | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 15216.447 | 16488.135 | 15212.068–16806.057 | 17389.684 | 200992.000 |
| C_simpleui | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12499.971 | 12775.371 | 12478.529–12844.221 | 18551.341 | 171536.000 |
| C_simpleui | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 13256.717 | 14592.179 | 13255.514–14926.045 | 16131.200 | 195776.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12416.808 | 12450.901 | 12411.827–12459.425 | 16303.705 | 166384.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 12683.269 | 12707.119 | 12657.437–12713.081 | 13747.308 | 175056.000 |
| C_simpleui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 14818.057 | 14818.057 | 14818.057–14818.057 | 19320.665 | 176224.000 |
| C_simpleui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 18591.627 | 18591.627 | 18591.627–18591.627 | 25242.926 | 201136.000 |
| C_simpleui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 105487.969 | 105487.969 | 105487.969–105487.969 | 110637.128 | 336736.000 |
| C_simpleui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 12751.107 | 12751.107 | 12751.107–12751.107 | 19101.267 | 171424.000 |
| C_simpleui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 13420.955 | 13420.955 | 13420.955–13420.955 | 13872.905 | 180512.000 |
| C_simpleui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 53672.664 | 53672.664 | 53672.664–53672.664 | 55605.634 | 273616.000 |
| C_simpleui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 12511.502 | 12511.502 | 12511.502–12511.502 | 18681.305 | 170656.000 |
| C_simpleui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15470.131 | 15470.131 | 15470.131–15470.131 | 15502.618 | 178480.000 |
| C_simpleui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 53135.262 | 53135.262 | 53135.262–53135.262 | 55854.854 | 266960.000 |
| C_simpleui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 12449.557 | 12449.557 | 12449.557–12449.557 | 18159.993 | 172704.000 |
| C_simpleui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15415.791 | 15415.791 | 15415.791–15415.791 | 15614.475 | 181120.000 |
| C_simpleui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 52399.062 | 52399.062 | 52399.062–52399.062 | 57542.724 | 268528.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14188.882 | 14261.185 | 14185.081–14279.261 | 15609.230 | 173120.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14672.972 | 14689.122 | 14661.749–14693.159 | 16730.219 | 188576.000 |
| D_zenos | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 14239.437 | 14245.640 | 14223.183–14247.190 | 16237.941 | 173904.000 |
| D_zenos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 20207.433 | 20241.876 | 20200.929–20250.487 | 21278.334 | 206512.000 |
| D_zenos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14217.249 | 14244.205 | 14156.804–14250.944 | 15778.983 | 173936.000 |
| D_zenos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 14854.702 | 14855.358 | 14781.647–14855.522 | 15583.663 | 197440.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14302.758 | 14733.808 | 14207.277–14841.570 | 21283.340 | 170576.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14659.859 | 15380.859 | 14640.230–15561.109 | 16605.143 | 182208.000 |
| D_zenos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 14253.585 | 14253.585 | 14253.585–14253.585 | 15878.674 | 172224.000 |
| D_zenos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 20830.959 | 20830.959 | 20830.959–20830.959 | 21067.720 | 225376.000 |
| D_zenos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 37682.740 | 37682.740 | 37682.740–37682.740 | 38846.644 | 252208.000 |
| D_zenos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14164.894 | 14164.894 | 14164.894–14164.894 | 15119.992 | 174016.000 |
| D_zenos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16671.096 | 16671.096 | 16671.096–16671.096 | 19114.352 | 197360.000 |
| D_zenos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 33503.221 | 33503.221 | 33503.221–33503.221 | 36886.782 | 247856.000 |
| D_zenos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14281.394 | 14281.394 | 14281.394–14281.394 | 15660.502 | 172416.000 |
| D_zenos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14704.662 | 14704.662 | 14704.662–14704.662 | 14823.607 | 192560.000 |
| D_zenos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 35258.045 | 35258.045 | 35258.045–35258.045 | 36143.635 | 244368.000 |
| D_zenos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14210.769 | 14210.769 | 14210.769–14210.769 | 15580.682 | 174336.000 |
| D_zenos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14690.033 | 14690.033 | 14690.033–14690.033 | 16561.293 | 197168.000 |
| D_zenos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 34052.639 | 34052.639 | 34052.639–34052.639 | 34839.812 | 246848.000 |
| E_project_title | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 11052.800 | 11086.606 | 10994.155–11095.058 | 16893.204 | 168256.000 |
| E_project_title | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 11780.452 | 11786.243 | 11755.694–11787.690 | 26264.660 | 202960.000 |
| E_project_title | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8327.565 | 8441.175 | 8290.460–8469.577 | 14588.524 | 165120.000 |
| E_project_title | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 9218.499 | 9313.390 | 9214.085–9337.112 | 19713.867 | 195664.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8348.288 | 8359.182 | 8292.034–8361.905 | 13351.962 | 159664.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8272.745 | 8319.998 | 8258.476–8331.812 | 9043.594 | 167808.000 |
| E_project_title | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11077.628 | 11077.628 | 11077.628–11077.628 | 16958.704 | 166720.000 |
| E_project_title | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 11026.788 | 11026.788 | 11026.788–11026.788 | 17224.565 | 191792.000 |
| E_project_title | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17433.297 | 17433.297 | 17433.297–17433.297 | 29837.107 | 223008.000 |
| E_project_title | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8756.546 | 8756.546 | 8756.546–8756.546 | 15227.497 | 164704.000 |
| E_project_title | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 10000.077 | 10000.077 | 10000.077–10000.077 | 24422.544 | 184400.000 |
| E_project_title | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13993.758 | 13993.758 | 13993.758–13993.758 | 26706.924 | 210816.000 |
| E_project_title | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8378.940 | 8378.940 | 8378.940–8378.940 | 14599.615 | 164384.000 |
| E_project_title | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8434.905 | 8434.905 | 8434.905–8434.905 | 19737.975 | 178608.000 |
| E_project_title | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 13168.243 | 13168.243 | 13168.243–13168.243 | 24322.509 | 208896.000 |
| E_project_title | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8273.229 | 8273.229 | 8273.229–8273.229 | 14559.134 | 163872.000 |
| E_project_title | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8382.437 | 8382.437 | 8382.437–8382.437 | 10255.182 | 178128.000 |
| E_project_title | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12323.427 | 12323.427 | 12323.427–12323.427 | 22346.267 | 205904.000 |
| F_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 11694.442 | 11707.599 | 11660.517–11710.888 | 19637.108 | 171344.000 |
| F_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 12342.294 | 12377.313 | 12322.481–12386.067 | 16833.915 | 192752.000 |
| F_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8918.173 | 8949.573 | 8883.263–8957.423 | 15285.281 | 166800.000 |
| F_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 10011.407 | 10057.263 | 10010.208–10068.728 | 10029.388 | 192208.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8892.083 | 8943.827 | 8868.310–8956.763 | 14248.708 | 162944.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8904.450 | 8950.850 | 8888.985–8962.450 | 9788.499 | 170944.000 |
| F_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11723.517 | 11723.517 | 11723.517–11723.517 | 19653.860 | 171136.000 |
| F_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 15624.392 | 15624.392 | 15624.392–15624.392 | 21501.331 | 262944.000 |
| F_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17409.785 | 17409.785 | 17409.785–17409.785 | 20455.575 | 273312.000 |
| F_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9334.013 | 9334.013 | 9334.013–9334.013 | 16230.869 | 167424.000 |
| F_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 29528.899 | 29528.899 | 29528.899–29528.899 | 42483.025 | 239712.000 |
| F_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 14391.883 | 14391.883 | 14391.883–14391.883 | 18068.766 | 249408.000 |
| F_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8999.810 | 8999.810 | 8999.810–8999.810 | 9715.127 | 167072.000 |
| F_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8946.958 | 8946.958 | 8946.958–8946.958 | 10310.480 | 175712.000 |
| F_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 20678.113 | 20678.113 | 20678.113–20678.113 | 27538.825 | 219712.000 |
| F_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8957.087 | 8957.087 | 8957.087–8957.087 | 9886.449 | 165904.000 |
| F_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8974.321 | 8974.321 | 8974.321–8974.321 | 10324.250 | 174720.000 |
| F_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 13413.773 | 13413.773 | 13413.773–13413.773 | 21053.953 | 203520.000 |
| G_simpleui_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 14963.186 | 14981.654 | 14951.475–14986.271 | 20020.798 | 174880.000 |
| G_simpleui_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 19702.450 | 19728.760 | 19652.290–19735.337 | 20607.081 | 213952.000 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12713.033 | 12733.024 | 12711.096–12738.021 | 19801.713 | 172608.000 |
| G_simpleui_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 16580.624 | 16596.574 | 16525.183–16600.562 | 24045.377 | 208544.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12564.726 | 12575.072 | 12559.679–12577.659 | 16493.834 | 167856.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 12834.612 | 12902.522 | 12824.433–12919.499 | 13849.390 | 176640.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 14954.854 | 14954.854 | 14954.854–14954.854 | 20179.116 | 174912.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 18743.466 | 18743.466 | 18743.466–18743.466 | 19184.265 | 199072.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 108776.584 | 108776.584 | 108776.584–108776.584 | 111758.454 | 370928.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 13017.896 | 13017.896 | 13017.896–13017.896 | 20480.104 | 173024.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 14743.158 | 14743.158 | 14743.158–14743.158 | 14777.348 | 186192.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 55107.079 | 55107.079 | 55107.079–55107.079 | 56449.187 | 305120.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 12714.420 | 12714.420 | 12714.420–12714.420 | 18040.010 | 169936.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15587.592 | 15587.592 | 15587.592–15587.592 | 15784.678 | 177712.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 55117.005 | 55117.005 | 55117.005–55117.005 | 58056.948 | 272464.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 12750.693 | 12750.693 | 12750.693–12750.693 | 19798.784 | 172944.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 16168.896 | 16168.896 | 16168.896–16168.896 | 16643.430 | 186176.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 58519.341 | 58519.341 | 58519.341–58519.341 | 61244.636 | 274112.000 |
| H_zenos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 14579.417 | 14583.264 | 14538.636–14584.226 | 17692.948 | 175472.000 |
| H_zenos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 24522.419 | 24524.625 | 24427.083–24525.177 | 25040.661 | 223024.000 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14530.026 | 14567.092 | 14509.335–14576.358 | 15973.277 | 173424.000 |
| H_zenos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 18447.913 | 18457.994 | 18382.796–18460.515 | 20114.848 | 209520.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14400.777 | 14472.659 | 14374.371–14490.629 | 22123.003 | 176336.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14752.008 | 14789.095 | 14712.176–14798.367 | 16598.334 | 183296.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 14511.351 | 14511.351 | 14511.351–14511.351 | 17591.965 | 173264.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 21139.577 | 21139.577 | 21139.577–21139.577 | 21376.490 | 218864.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 42508.836 | 42508.836 | 42508.836–42508.836 | 44841.885 | 303440.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14497.003 | 14497.003 | 14497.003–14497.003 | 16859.527 | 173184.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16909.638 | 16909.638 | 16909.638–16909.638 | 18721.263 | 197776.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 35748.722 | 35748.722 | 35748.722–35748.722 | 39032.562 | 281136.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14521.515 | 14521.515 | 14521.515–14521.515 | 17205.273 | 174000.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14936.607 | 14936.607 | 14936.607–14936.607 | 16723.647 | 193840.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 38111.589 | 38111.589 | 38111.589–38111.589 | 39083.661 | 272480.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14478.069 | 14478.069 | 14478.069–14478.069 | 16274.679 | 173616.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14884.049 | 14884.049 | 14884.049–14884.049 | 16708.312 | 193664.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 36422.569 | 36422.569 | 36422.569–36422.569 | 37527.126 | 267680.000 |
| I_vos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 11937.778 | 12014.694 | 11926.220–12033.923 | 19896.111 | 173920.000 |
| I_vos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 17785.700 | 17890.394 | 17731.771–17916.567 | 18322.754 | 208528.000 |
| I_vos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9270.060 | 9281.281 | 9159.794–9284.087 | 16743.555 | 168240.000 |
| I_vos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 14629.272 | 15543.572 | 14625.226–15772.147 | 22610.888 | 203552.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8991.306 | 9068.178 | 8974.294–9087.396 | 15220.449 | 164832.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9046.903 | 9318.266 | 9008.017–9386.106 | 9995.935 | 173392.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11877.540 | 11877.540 | 11877.540–11877.540 | 18440.901 | 172464.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 19512.818 | 19512.818 | 19512.818–19512.818 | 42463.035 | 275520.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 22215.658 | 22215.658 | 22215.658–22215.658 | 24603.796 | 305952.000 |
| I_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9873.622 | 9873.622 | 9873.622–9873.622 | 11430.022 | 166048.000 |
| I_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 28386.974 | 28386.974 | 28386.974–28386.974 | 33358.059 | 236224.000 |
| I_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 18615.228 | 18615.228 | 18615.228–18615.228 | 23790.347 | 268432.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9369.427 | 9369.427 | 9369.427–9369.427 | 16910.069 | 168000.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9122.192 | 9122.192 | 9122.192–9122.192 | 10645.543 | 176656.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 24327.142 | 24327.142 | 24327.142–24327.142 | 44562.411 | 248464.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9200.829 | 9200.829 | 9200.829–9200.829 | 10709.924 | 166064.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9101.013 | 9101.013 | 9101.013–9101.013 | 10562.959 | 175424.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 16283.700 | 16283.700 | 16283.700–16283.700 | 35016.110 | 218160.000 |
| J_simpleui_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 15315.506 | 15383.668 | 15309.701–15400.709 | 20783.843 | 175728.000 |
| J_simpleui_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 15939.205 | 15997.911 | 15937.826–16012.588 | 17880.835 | 200160.000 |
| J_simpleui_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12978.916 | 12982.407 | 12900.424–12983.279 | 19632.600 | 172240.000 |
| J_simpleui_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 13870.521 | 15054.093 | 13864.170–15349.986 | 14828.627 | 197168.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 12965.823 | 13192.554 | 12862.644–13249.237 | 16761.856 | 168240.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 13163.905 | 13688.008 | 13147.745–13819.034 | 14166.545 | 178704.000 |
| J_simpleui_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 15463.498 | 15463.498 | 15463.498–15463.498 | 18180.049 | 178384.000 |
| J_simpleui_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 20629.787 | 20629.787 | 20629.787–20629.787 | 32503.428 | 215568.000 |
| J_simpleui_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 109500.031 | 109500.031 | 109500.031–109500.031 | 111800.594 | 337056.000 |
| J_simpleui_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 13235.334 | 13235.334 | 13235.334–13235.334 | 20309.781 | 173840.000 |
| J_simpleui_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 14054.033 | 14054.033 | 14054.033–14054.033 | 14294.680 | 188736.000 |
| J_simpleui_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 52616.883 | 52616.883 | 52616.883–52616.883 | 67202.205 | 267776.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 13038.088 | 13038.088 | 13038.088–13038.088 | 19811.718 | 171584.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 16733.455 | 16733.455 | 16733.455–16733.455 | 17362.778 | 182832.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 59076.980 | 59076.980 | 59076.980–59076.980 | 65175.328 | 258976.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 12937.162 | 12937.162 | 12937.162–12937.162 | 19984.244 | 172144.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15478.486 | 15478.486 | 15478.486–15478.486 | 16205.744 | 182416.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 53641.109 | 53641.109 | 53641.109–53641.109 | 57972.076 | 257280.000 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 15628.432 | 15665.841 | 15526.197–15675.193 | 22348.223 | 177168.000 |
| K_simpleui_vos_bookshelf | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 20395.985 | 20408.379 | 20376.981–20411.478 | 21443.823 | 218096.000 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 13346.744 | 13557.410 | 13205.014–13610.076 | 19203.510 | 171200.000 |
| K_simpleui_vos_bookshelf | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 17221.964 | 18795.858 | 17221.597–19189.331 | 25778.481 | 205968.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 13042.804 | 13126.701 | 13041.378–13147.675 | 16985.743 | 168800.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 13263.370 | 13297.448 | 13254.577–13305.968 | 14136.425 | 179296.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 15530.951 | 15530.951 | 15530.951–15530.951 | 19058.151 | 177648.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 24302.001 | 24302.001 | 24302.001–24302.001 | 24427.905 | 213600.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 115666.346 | 115666.346 | 115666.346–115666.346 | 118193.982 | 371328.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 13445.760 | 13445.760 | 13445.760–13445.760 | 19624.704 | 171664.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 15255.412 | 15255.412 | 15255.412–15255.412 | 16379.941 | 192976.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 59296.173 | 59296.173 | 59296.173–59296.173 | 61820.965 | 288784.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 13343.139 | 13343.139 | 13343.139–13343.139 | 21499.245 | 173728.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 16861.771 | 16861.771 | 16861.771–16861.771 | 16886.368 | 185136.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 61065.157 | 61065.157 | 61065.157–61065.157 | 70704.443 | 278992.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 13366.904 | 13366.904 | 13366.904–13366.904 | 21508.075 | 174416.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15618.057 | 15618.057 | 15618.057–15618.057 | 16327.484 | 184752.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 56175.786 | 56175.786 | 56175.786–56175.786 | 60771.910 | 272272.000 |
| K_vos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8890.384 | 9051.590 | 8888.751–9091.892 | 9592.433 | 169152.000 |
| K_vos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8928.813 | 9010.329 | 8926.524–9030.708 | 9921.282 | 177440.000 |
| L_project_title_vos | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 11990.897 | 12001.922 | 11953.843–12004.679 | 20143.964 | 171456.000 |
| L_project_title_vos | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 12745.827 | 12763.493 | 12736.792–12767.909 | 26238.295 | 204464.000 |
| L_project_title_vos | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9050.569 | 9057.441 | 9000.659–9059.159 | 9540.872 | 167200.000 |
| L_project_title_vos | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 10040.890 | 10063.674 | 10026.323–10069.370 | 20240.842 | 197040.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8965.667 | 8976.186 | 8947.772–8978.815 | 15215.386 | 163904.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8999.519 | 9031.253 | 8955.640–9039.187 | 9904.716 | 171888.000 |
| L_project_title_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11973.827 | 11973.827 | 11973.827–11973.827 | 19604.109 | 171216.000 |
| L_project_title_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 11996.604 | 11996.604 | 11996.604–11996.604 | 26725.707 | 196560.000 |
| L_project_title_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 18811.062 | 18811.062 | 18811.062–18811.062 | 32159.857 | 219984.000 |
| L_project_title_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9562.655 | 9562.655 | 9562.655–9562.655 | 10288.578 | 167568.000 |
| L_project_title_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 9584.214 | 9584.214 | 9584.214–9584.214 | 25642.136 | 188336.000 |
| L_project_title_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13837.168 | 13837.168 | 13837.168–13837.168 | 30112.041 | 209168.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8955.729 | 8955.729 | 8955.729–8955.729 | 9479.045 | 167328.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9072.581 | 9072.581 | 9072.581–9072.581 | 14539.274 | 181776.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 13518.047 | 13518.047 | 13518.047–13518.047 | 26572.588 | 214352.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9004.479 | 9004.479 | 9004.479–9004.479 | 9419.855 | 168176.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9026.843 | 9026.843 | 9026.843–9026.843 | 14190.027 | 182640.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 13061.098 | 13061.098 | 13061.098–13061.098 | 24826.417 | 204912.000 |
| M_leanui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8325.164 | 8335.723 | 8258.152–8338.363 | 14578.257 | 165536.000 |
| M_leanui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8262.617 | 8271.439 | 8218.848–8273.645 | 9128.717 | 173984.000 |
| M_leanui | paging | flat | 2000 | post_init_idle | PASS | 3 | 3 | 11006.773 | 11009.455 | 10967.492–11010.125 | 16519.739 | 168992.000 |
| M_leanui | paging | flat | 2000 | post_stress_idle | PASS | 3 | 3 | 11745.578 | 11764.609 | 11711.070–11769.367 | 27956.356 | 202160.000 |
| M_leanui | paging | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8218.512 | 8293.659 | 8185.598–8312.445 | 14516.916 | 164208.000 |
| M_leanui | paging | hierarchical | 2000 | post_stress_idle | PASS | 3 | 3 | 9104.961 | 9172.386 | 9077.840–9189.242 | 20390.843 | 193312.000 |
| M_leanui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8161.984 | 8209.394 | 8152.633–8221.246 | 11687.720 | 160544.000 |
| M_leanui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8248.289 | 8265.230 | 8205.449–8269.465 | 8924.375 | 169056.000 |
| M_leanui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 10883.898 | 10883.898 | 10883.898–10883.898 | 16949.851 | 167024.000 |
| M_leanui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 12116.645 | 12116.645 | 12116.645–12116.645 | 20861.316 | 195376.000 |
| M_leanui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17365.081 | 17365.081 | 17365.081–17365.081 | 28416.778 | 224608.000 |
| M_leanui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8760.988 | 8760.988 | 8760.988–8760.988 | 15501.880 | 167136.000 |
| M_leanui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 10032.477 | 10032.477 | 10032.477–10032.477 | 12797.908 | 186096.000 |
| M_leanui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 14017.366 | 14017.366 | 14017.366–14017.366 | 25532.982 | 212928.000 |
| M_leanui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8280.012 | 8280.012 | 8280.012–8280.012 | 14662.963 | 164336.000 |
| M_leanui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8300.625 | 8300.625 | 8300.625–8300.625 | 10663.264 | 178448.000 |
| M_leanui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 13347.855 | 13347.855 | 13347.855–13347.855 | 23885.160 | 215024.000 |
| M_leanui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8223.172 | 8223.172 | 8223.172–8223.172 | 14534.479 | 164768.000 |
| M_leanui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8208.867 | 8208.867 | 8208.867–8208.867 | 11003.753 | 178976.000 |
| M_leanui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12912.980 | 12912.980 | 12912.980–12912.980 | 22461.469 | 212576.000 |
| A_stock | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8399.614 | 8399.614 | 8399.614–8399.614 | 12786.648 | 163360.000 |
| A_stock | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8531.591 | 8531.591 | 8531.591–8531.591 | 9186.459 | 171856.000 |
| B_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8651.610 | 8651.610 | 8651.610–8651.610 | 14275.903 | 164688.000 |
| B_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8598.302 | 8598.302 | 8598.302–8598.302 | 9364.171 | 172592.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 12456.533 | 12456.533 | 12456.533–12456.533 | 18788.995 | 171296.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 12741.049 | 12741.049 | 12741.049–12741.049 | 13858.142 | 178176.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14210.421 | 14210.421 | 14210.421–14210.421 | 15679.010 | 172160.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14696.253 | 14696.253 | 14696.253–14696.253 | 16580.962 | 188384.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8340.171 | 8340.171 | 8340.171–8340.171 | 14614.184 | 164576.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8327.464 | 8327.464 | 8327.464–8327.464 | 9094.618 | 173040.000 |
| F_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8897.853 | 8897.853 | 8897.853–8897.853 | 9491.500 | 166848.000 |
| F_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8881.579 | 8881.579 | 8881.579–8881.579 | 9944.342 | 174848.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 12751.604 | 12751.604 | 12751.604–12751.604 | 19866.792 | 172576.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 12946.986 | 12946.986 | 12946.986–12946.986 | 14069.577 | 179296.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14472.487 | 14472.487 | 14472.487–14472.487 | 16892.714 | 174256.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14819.405 | 14819.405 | 14819.405–14819.405 | 16748.385 | 189680.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9324.063 | 9324.063 | 9324.063–9324.063 | 16574.399 | 168000.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9206.708 | 9206.708 | 9206.708–9206.708 | 10384.130 | 175840.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 12973.525 | 12973.525 | 12973.525–12973.525 | 19896.190 | 174016.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 13172.018 | 13172.018 | 13172.018–13172.018 | 14245.679 | 183520.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 13338.619 | 13338.619 | 13338.619–13338.619 | 21408.721 | 175776.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 13389.166 | 13389.166 | 13389.166–13389.166 | 14609.263 | 185376.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8998.565 | 8998.565 | 8998.565–8998.565 | 9420.305 | 167232.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8966.440 | 8966.440 | 8966.440–8966.440 | 10075.600 | 175184.000 |
| M_leanui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8201.980 | 8201.980 | 8201.980–8201.980 | 14577.073 | 165552.000 |
| M_leanui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8206.398 | 8206.398 | 8206.398–8206.398 | 8965.769 | 174032.000 |

## Data-derived comparisons

- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 26.095 ms vs 26.831 ms (2.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 21.235 ms vs 21.806 ms (2.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 26.566 ms vs 27.421 ms (3.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.381 ms vs 20.114 ms (3.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 27.883 ms vs 29.710 ms (6.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 24.727 ms vs 25.764 ms (4.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `B_bookshelf` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 34.068 ms vs 56.113 ms (39.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `B_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 42.397 ms vs 60.424 ms (29.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 24.283 ms vs 26.831 ms (9.5% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 21.806 ms vs 23.477 ms (7.1% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.083 ms vs 26.566 ms (20.6% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.381 ms vs 21.422 ms (9.5% lower) (UX-level comparison: books/page differs, 10.000 vs 8.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 14.708 ms vs 27.883 ms (47.3% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 16.837 ms vs 25.764 ms (34.7% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 19.282 ms vs 56.113 ms (65.6% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 26.532 ms vs 42.397 ms (37.4% lower) (UX-level comparison: books/page differs, 8.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 11.131 ms vs 26.831 ms (58.5% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 12.011 ms vs 21.806 ms (44.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 11.259 ms vs 26.566 ms (57.6% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 11.687 ms vs 19.381 ms (39.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 18.004 ms vs 27.883 ms (35.4% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 11.043 ms vs 25.764 ms (57.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 18.129 ms vs 56.113 ms (67.7% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 12.333 ms vs 42.397 ms (70.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, flat, 2000 books): 13.338 ms vs 26.831 ms (50.3% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 13.518 ms vs 21.806 ms (38.0% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (paging, hierarchical, 2000 books): 12.983 ms vs 26.566 ms (51.1% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.395 ms vs 19.381 ms (30.9% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 12.708 ms vs 27.883 ms (54.4% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 12.988 ms vs 25.764 ms (49.6% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 7.548 ms vs 56.113 ms (86.5% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `E_project_title` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 7.972 ms vs 42.397 ms (81.2% lower) (UX-level comparison: books/page differs, 14.000 vs 10.000).
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 26.831 ms vs 27.641 ms (2.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (paging, flat, 2000 books): 21.628 ms vs 21.806 ms (0.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 26.566 ms vs 27.026 ms (1.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.381 ms vs 21.056 ms (8.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 25.135 ms vs 27.883 ms (9.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 24.586 ms vs 25.764 ms (4.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 26.785 ms vs 56.113 ms (52.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `A_stock` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 42.397 ms vs 61.745 ms (31.3% lower).
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 24.283 ms vs 27.189 ms (10.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 23.400 ms vs 23.477 ms (0.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.083 ms vs 26.022 ms (19.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 21.422 ms vs 23.370 ms (8.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 14.708 ms vs 22.923 ms (35.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 16.837 ms vs 22.542 ms (25.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 14.200 ms vs 19.282 ms (26.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 17.090 ms vs 26.532 ms (35.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (paging, flat, 2000 books): 11.131 ms vs 11.218 ms (0.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, flat, 2000 books): 11.994 ms vs 12.011 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (paging, hierarchical, 2000 books): 10.985 ms vs 11.259 ms (2.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 11.244 ms vs 11.687 ms (3.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 2000 books): 16.718 ms vs 18.004 ms (7.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 2000 books): 10.639 ms vs 11.043 ms (3.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 17.261 ms vs 18.129 ms (4.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 50 books): 11.864 ms vs 12.333 ms (3.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, flat, 2000 books): 25.069 ms vs 27.641 ms (9.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, flat, 2000 books): 21.080 ms vs 21.628 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 25.924 ms vs 27.026 ms (4.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (paging, hierarchical, 2000 books): 19.209 ms vs 21.056 ms (8.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 25.135 ms vs 27.819 ms (9.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 24.586 ms vs 26.547 ms (7.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 18.474 ms vs 26.785 ms (31.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 50 books): 46.890 ms vs 61.745 ms (24.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, flat, 2000 books): 24.283 ms vs 27.807 ms (12.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, flat, 2000 books): 23.450 ms vs 23.477 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.083 ms vs 22.084 ms (4.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (paging, hierarchical, 2000 books): 21.115 ms vs 21.422 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 2000 books): 13.242 ms vs 14.708 ms (10.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 2000 books): 15.892 ms vs 16.837 ms (5.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 19.279 ms vs 19.282 ms (0.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 21.740 ms vs 26.532 ms (18.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, flat, 2000 books): 27.125 ms vs 27.807 ms (2.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, flat, 2000 books): 23.450 ms vs 23.927 ms (2.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (paging, hierarchical, 2000 books): 21.956 ms vs 22.084 ms (0.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (paging, hierarchical, 2000 books): 21.115 ms vs 21.443 ms (1.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.242 ms vs 25.473 ms (48.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 15.892 ms vs 26.008 ms (38.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 13.125 ms vs 19.279 ms (31.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 15.346 ms vs 21.740 ms (29.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, flat, 2000 books): 12.300 ms vs 13.338 ms (7.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (paging, flat, 2000 books): 12.816 ms vs 13.518 ms (5.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (paging, hierarchical, 2000 books): 12.319 ms vs 12.983 ms (5.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (paging, hierarchical, 2000 books): 13.069 ms vs 13.395 ms (2.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 2000 books): 12.527 ms vs 12.708 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 2000 books): 12.988 ms vs 13.106 ms (0.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 50 books): 7.548 ms vs 12.840 ms (41.2% lower).
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 50 books): 7.972 ms vs 13.506 ms (41.0% lower).

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
