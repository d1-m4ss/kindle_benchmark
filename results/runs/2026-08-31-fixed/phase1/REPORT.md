# KOReader UI Benchmark Report

> **DEPRECATED_INVALID_FOR_RANKING (paging scenarios only):** this campaign was generated on 2026-08-31, before the paging-instrumentation and hierarchical-dataset fixes and before the KOReader/Bookshelf/Project:Title baseline bump recorded in `versions.lock.json` (see README "Baseline change"). Its `library_next_page` / paging / cached-paging rows use a scenario name now rejected by the audit as deprecated and must not be used to rank stacks. Startup, open-book, memory, and Bookends rows are unaffected and remain valid.

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `all`

Aggregated rows: 1338; PASS=1260; FAILED=0; UNSUPPORTED=78.

## Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|:--|
| A_stock | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 13.664 | 13.881 | 13.219–13.935 |
| A_stock | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 13.084 | 13.163 | 12.570–13.183 |
| A_stock | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 11.897 | 12.166 | 10.083–12.233 |
| A_stock | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 12.293 | 13.843 | 11.195–14.230 |
| A_stock | warm | flat | 2000 | change_sort_mode | PASS | 10 | 136.885 | 184.406 | 117.823–189.257 |
| A_stock | warm | flat | 2000 | close_book | PASS | 10 | 69.840 | 85.706 | 64.742–89.526 |
| A_stock | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.220 | 9.144 | 7.406–9.950 |
| A_stock | warm | flat | 2000 | home_to_library | PASS | 10 | 105.137 | 152.840 | 73.722–166.281 |
| A_stock | warm | flat | 2000 | library_first_render | PASS | 10 | 66.575 | 108.359 | 63.681–112.512 |
| A_stock | warm | flat | 2000 | library_folder_back | PASS | 10 | 63.084 | 92.231 | 58.956–92.736 |
| A_stock | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.497 | 9.119 | 7.255–9.257 |
| A_stock | warm | flat | 2000 | library_next_page | PASS | 10 | 20.130 | 34.950 | 17.958–43.877 |
| A_stock | warm | flat | 2000 | library_prev_page | PASS | 10 | 31.242 | 37.491 | 24.979–67.724 |
| A_stock | warm | flat | 2000 | open_book | PASS | 10 | 80.352 | 89.796 | 59.780–89.986 |
| A_stock | warm | flat | 2000 | open_book_minimal | PASS | 10 | 108.647 | 113.065 | 105.465–113.279 |
| A_stock | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.457 | 8.935 | 7.483–9.225 |
| A_stock | warm | flat | 2000 | repeated_nav | PASS | 2 | 219.794 | 224.965 | 213.332–226.257 |
| A_stock | warm | flat | 50 | change_sort_mode | PASS | 10 | 59.700 | 70.851 | 39.048–71.709 |
| A_stock | warm | flat | 50 | close_book | PASS | 10 | 27.559 | 39.111 | 23.343–47.902 |
| A_stock | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.292 | 9.036 | 7.758–9.086 |
| A_stock | warm | flat | 50 | home_to_library | PASS | 10 | 34.114 | 57.627 | 27.179–57.920 |
| A_stock | warm | flat | 50 | library_first_render | PASS | 10 | 65.638 | 86.512 | 27.458–134.488 |
| A_stock | warm | flat | 50 | library_folder_back | PASS | 10 | 25.776 | 27.802 | 23.021–28.151 |
| A_stock | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.012 | 9.278 | 6.903–9.362 |
| A_stock | warm | flat | 50 | library_next_page | PASS | 10 | 60.861 | 120.349 | 21.322–125.578 |
| A_stock | warm | flat | 50 | library_prev_page | PASS | 10 | 33.891 | 55.397 | 27.124–56.727 |
| A_stock | warm | flat | 50 | open_book | PASS | 10 | 64.732 | 69.938 | 47.161–85.815 |
| A_stock | warm | flat | 50 | open_book_minimal | PASS | 10 | 65.977 | 72.539 | 48.898–75.551 |
| A_stock | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.139 | 8.998 | 4.274–9.483 |
| A_stock | warm | flat | 50 | repeated_nav | PASS | 2 | 130.201 | 156.151 | 97.762–162.639 |
| A_stock | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.816 | 13.240 | 8.780–21.202 |
| A_stock | warm | hierarchical | 2000 | close_book | PASS | 10 | 30.655 | 37.893 | 20.773–43.494 |
| A_stock | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 7.923 | 8.718 | 7.347–8.881 |
| A_stock | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 13.137 | 20.728 | 11.384–21.165 |
| A_stock | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 12.610 | 20.373 | 11.852–20.953 |
| A_stock | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 13.787 | 26.154 | 8.986–26.407 |
| A_stock | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 23.529 | 34.244 | 8.439–35.327 |
| A_stock | warm | hierarchical | 2000 | open_book | PASS | 10 | 43.438 | 50.811 | 41.107–52.309 |
| A_stock | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 56.046 | 58.607 | 38.443–60.099 |
| A_stock | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.415 | 19.366 | 7.483–20.793 |
| A_stock | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 156.114 | 168.079 | 141.159–171.070 |
| A_stock | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 10.474 | 18.267 | 9.231–18.720 |
| A_stock | warm | hierarchical | 50 | close_book | PASS | 10 | 34.656 | 41.267 | 24.789–41.717 |
| A_stock | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.468 | 8.979 | 7.282–9.209 |
| A_stock | warm | hierarchical | 50 | home_to_library | PASS | 10 | 12.721 | 22.275 | 10.358–23.030 |
| A_stock | warm | hierarchical | 50 | library_first_render | PASS | 10 | 12.537 | 18.122 | 10.550–19.532 |
| A_stock | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 14.367 | 22.977 | 9.815–24.216 |
| A_stock | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.033 | 19.289 | 6.109–23.900 |
| A_stock | warm | hierarchical | 50 | open_book | PASS | 10 | 42.587 | 50.721 | 38.162–60.598 |
| A_stock | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 54.239 | 58.769 | 40.331–59.927 |
| A_stock | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 7.941 | 8.566 | 3.540–8.821 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 14.721 | 15.344 | 14.379–15.500 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 13.289 | 15.047 | 12.797–15.486 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.347 | 13.178 | 11.461–13.386 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 10.987 | 12.569 | 10.483–12.964 |
| B_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 4.298 | 18.855 | 3.466–25.252 |
| B_bookshelf | warm | flat | 2000 | bookshelf_page_turn | PASS | 10 | 0.069 | 0.179 | 0.037–0.340 |
| B_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 132.880 | 193.478 | 109.145–195.715 |
| B_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 64.966 | 73.520 | 60.210–87.923 |
| B_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 8.910 | 9.193 | 8.161–9.384 |
| B_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.238 | 8.773 | 7.590–9.125 |
| B_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 115.151 | 153.744 | 101.737–203.429 |
| B_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 94.049 | 131.476 | 72.341–204.254 |
| B_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 68.347 | 106.815 | 62.487–108.025 |
| B_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.110 | 45.526 | 7.421–48.938 |
| B_bookshelf | warm | flat | 2000 | library_next_page | PASS | 10 | 29.322 | 61.129 | 17.089–69.401 |
| B_bookshelf | warm | flat | 2000 | library_prev_page | PASS | 10 | 37.204 | 86.092 | 32.637–89.922 |
| B_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 85.498 | 88.938 | 62.220–95.994 |
| B_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 119.071 | 125.665 | 79.024–138.802 |
| B_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 10.017 | 14.794 | 9.034–17.816 |
| B_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.418 | 17.768 | 7.585–97.829 |
| B_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 231.732 | 233.947 | 228.963–234.501 |
| B_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 4.165 | 16.301 | 3.640–23.327 |
| B_bookshelf | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.114 | 0.208 | 0.034–0.249 |
| B_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 51.445 | 65.881 | 36.608–70.170 |
| B_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 31.730 | 36.386 | 26.654–41.042 |
| B_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.739 | 9.192 | 8.134–9.296 |
| B_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.537 | 9.310 | 7.471–11.888 |
| B_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 35.115 | 57.125 | 27.866–67.200 |
| B_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 69.962 | 108.740 | 38.072–120.315 |
| B_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 27.367 | 52.910 | 22.643–63.211 |
| B_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.904 | 73.897 | 7.392–78.353 |
| B_bookshelf | warm | flat | 50 | library_next_page | PASS | 10 | 22.027 | 61.396 | 17.366–63.425 |
| B_bookshelf | warm | flat | 50 | library_prev_page | PASS | 10 | 64.017 | 68.709 | 27.433–69.964 |
| B_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 63.071 | 68.233 | 55.876–72.431 |
| B_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 63.636 | 71.890 | 46.342–82.037 |
| B_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 11.101 | 12.148 | 8.627–13.630 |
| B_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.188 | 9.055 | 7.356–9.136 |
| B_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 239.224 | 242.039 | 235.705–242.743 |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 3.592 | 15.386 | 2.923–19.235 |
| B_bookshelf | warm | hierarchical | 2000 | bookshelf_page_turn | PASS | 10 | 0.061 | 0.192 | 0.044–0.321 |
| B_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 10.851 | 14.149 | 9.373–22.742 |
| B_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 26.767 | 33.878 | 24.539–35.307 |
| B_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.737 | 8.942 | 8.340–9.140 |
| B_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.505 | 13.797 | 8.003–54.713 |
| B_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 13.355 | 23.214 | 11.287–25.200 |
| B_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 13.482 | 21.424 | 12.157–21.668 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 14.976 | 24.646 | 10.959–25.699 |
| B_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 22.742 | 33.829 | 8.851–35.609 |
| B_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 57.581 | 63.642 | 43.722–65.642 |
| B_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 59.248 | 62.840 | 54.011–63.513 |
| B_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 10.848 | 14.981 | 8.326–15.466 |
| B_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.078 | 8.659 | 7.580–8.773 |
| B_bookshelf | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 195.431 | 199.267 | 190.636–200.226 |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 7.749 | 18.481 | 6.550–23.199 |
| B_bookshelf | warm | hierarchical | 50 | bookshelf_page_turn | PASS | 10 | 0.373 | 0.545 | 0.212–0.619 |
| B_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 9.859 | 18.897 | 8.911–20.022 |
| B_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 24.748 | 30.752 | 19.615–48.296 |
| B_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 8.670 | 9.746 | 8.276–10.382 |
| B_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 11.678 | 13.339 | 10.476–13.846 |
| B_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 12.009 | 21.482 | 10.531–22.686 |
| B_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 13.329 | 22.569 | 11.852–23.493 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 14.512 | 19.403 | 9.269–21.543 |
| B_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.335 | 22.156 | 8.503–26.212 |
| B_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 59.620 | 61.786 | 47.200–64.185 |
| B_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 58.653 | 62.371 | 52.960–62.914 |
| B_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 14.950 | 17.055 | 13.258–17.417 |
| B_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.895 | 15.430 | 7.495–69.491 |
| C_simpleui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 0.108 | 0.125 | 0.087–0.129 |
| C_simpleui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 22.817 | 23.596 | 19.855–23.791 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 0.257 | 0.265 | 0.060–0.267 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 19.484 | 21.176 | 18.957–21.599 |
| C_simpleui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 131.143 | 170.601 | 102.675–174.554 |
| C_simpleui | warm | flat | 2000 | close_book | PASS | 10 | 104.848 | 113.475 | 98.845–117.863 |
| C_simpleui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 11.926 | 12.797 | 9.526–12.865 |
| C_simpleui | warm | flat | 2000 | home_to_library | PASS | 10 | 0.034 | 0.078 | 0.005–0.096 |
| C_simpleui | warm | flat | 2000 | library_first_render | PASS | 10 | 98.166 | 121.195 | 86.251–123.657 |
| C_simpleui | warm | flat | 2000 | library_folder_back | PASS | 10 | 65.648 | 91.247 | 61.652–93.126 |
| C_simpleui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.930 | 10.456 | 8.342–10.813 |
| C_simpleui | warm | flat | 2000 | library_next_page | PASS | 10 | 18.805 | 42.419 | 14.535–43.208 |
| C_simpleui | warm | flat | 2000 | library_prev_page | PASS | 10 | 28.159 | 40.086 | 20.891–50.444 |
| C_simpleui | warm | flat | 2000 | open_book | PASS | 10 | 153.529 | 1328.778 | 134.486–3623.898 |
| C_simpleui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 110.245 | 268.226 | 88.024–1601.258 |
| C_simpleui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.918 | 20.411 | 7.606–22.579 |
| C_simpleui | warm | flat | 2000 | repeated_nav | PASS | 2 | 528.554 | 805.641 | 182.197–874.912 |
| C_simpleui | warm | flat | 2000 | start_to_home | PASS | 10 | 0.044 | 0.065 | 0.011–0.070 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 10 | 40.809 | 67.472 | 34.643–68.255 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 10 | 66.003 | 177.925 | 51.084–447.480 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 10 | 12.437 | 13.364 | 9.985–13.929 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 10 | 0.023 | 0.046 | 0.005–0.053 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 10 | 62.952 | 77.020 | 42.559–83.253 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 10 | 24.312 | 39.112 | 23.142–40.107 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 10 | 9.073 | 16.069 | 7.494–34.550 |
| C_simpleui | warm | flat | 50 | library_next_page | PASS | 10 | 18.761 | 39.438 | 15.543–69.510 |
| C_simpleui | warm | flat | 50 | library_prev_page | PASS | 10 | 20.242 | 38.356 | 16.634–40.526 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 10 | 132.156 | 237.974 | 98.852–1073.666 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 10 | 106.281 | 114.896 | 79.502–126.661 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.579 | 9.087 | 8.004–9.292 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 2 | 301.642 | 470.220 | 90.920–512.364 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 10 | 0.041 | 0.075 | 0.019–0.114 |
| C_simpleui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 14.568 | 20.152 | 11.819–44.718 |
| C_simpleui | warm | hierarchical | 2000 | close_book | PASS | 10 | 78.184 | 981.970 | 54.988–8304.586 |
| C_simpleui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 11.697 | 12.499 | 10.306–13.168 |
| C_simpleui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 0.078 | 0.127 | 0.035–0.137 |
| C_simpleui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 28.425 | 40.906 | 25.855–43.805 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 17.477 | 21.893 | 12.340–36.668 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 24.384 | 39.726 | 8.725–49.652 |
| C_simpleui | warm | hierarchical | 2000 | open_book | PASS | 10 | 137.248 | 186.106 | 96.683–188.033 |
| C_simpleui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 111.265 | 135.049 | 93.522–143.071 |
| C_simpleui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.864 | 9.133 | 7.464–9.211 |
| C_simpleui | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 322.018 | 511.455 | 85.222–558.814 |
| C_simpleui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 0.044 | 0.085 | 0.009–0.101 |
| C_simpleui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 11.824 | 31.923 | 9.665–34.297 |
| C_simpleui | warm | hierarchical | 50 | close_book | PASS | 10 | 88.817 | 2427.887 | 49.735–22987.582 |
| C_simpleui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 11.905 | 12.917 | 10.707–13.250 |
| C_simpleui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 0.045 | 0.061 | 0.011–0.079 |
| C_simpleui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 28.300 | 39.665 | 26.039–46.443 |
| C_simpleui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 17.572 | 41.133 | 10.366–44.294 |
| C_simpleui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 22.972 | 48.922 | 9.595–57.366 |
| C_simpleui | warm | hierarchical | 50 | open_book | PASS | 10 | 137.594 | 157.400 | 96.913–158.707 |
| C_simpleui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 114.832 | 127.958 | 75.509–132.136 |
| C_simpleui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.642 | 9.249 | 7.787–9.271 |
| C_simpleui | warm | hierarchical | 50 | repeated_nav | PASS | 2 | 286.709 | 441.640 | 93.046–480.373 |
| C_simpleui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 0.053 | 0.065 | 0.006–0.119 |
| D_zenos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 68.240 | 71.286 | 66.770–72.047 |
| D_zenos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 30.857 | 31.115 | 30.802–31.179 |
| D_zenos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 69.863 | 71.769 | 68.799–72.246 |
| D_zenos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 29.796 | 30.766 | 28.057–31.008 |
| D_zenos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 101.207 | 135.302 | 88.263–138.885 |
| D_zenos | warm | flat | 2000 | close_book | PASS | 10 | 79.642 | 118.379 | 42.836–119.602 |
| D_zenos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 11.367 | 12.514 | 10.645–12.741 |
| D_zenos | warm | flat | 2000 | home_to_library | PASS | 10 | 82.419 | 109.466 | 70.529–142.492 |
| D_zenos | warm | flat | 2000 | library_first_render | PASS | 10 | 73.345 | 108.244 | 66.240–120.742 |
| D_zenos | warm | flat | 2000 | library_folder_back | PASS | 10 | 54.467 | 80.499 | 50.956–88.715 |
| D_zenos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.608 | 9.243 | 4.959–9.286 |
| D_zenos | warm | flat | 2000 | library_next_page | PASS | 10 | 8.418 | 18.999 | 6.852–37.122 |
| D_zenos | warm | flat | 2000 | library_prev_page | PASS | 10 | 9.068 | 38.417 | 6.991–41.487 |
| D_zenos | warm | flat | 2000 | open_book | PASS | 10 | 143.232 | 164.165 | 92.697–174.965 |
| D_zenos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 128.032 | 136.268 | 111.347–136.505 |
| D_zenos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.918 | 9.662 | 8.444–9.664 |
| D_zenos | warm | flat | 2000 | start_to_home | PASS | 10 | 9.989 | 12.991 | 8.499–13.283 |
| D_zenos | warm | flat | 50 | change_sort_mode | PASS | 10 | 20.979 | 42.379 | 16.390–46.598 |
| D_zenos | warm | flat | 50 | close_book | PASS | 10 | 50.995 | 61.406 | 43.087–62.123 |
| D_zenos | warm | flat | 50 | close_quick_settings | PASS | 10 | 10.566 | 10.738 | 10.066–10.833 |
| D_zenos | warm | flat | 50 | home_to_library | PASS | 10 | 42.835 | 55.902 | 38.487–56.191 |
| D_zenos | warm | flat | 50 | library_first_render | PASS | 10 | 38.529 | 59.940 | 28.604–78.806 |
| D_zenos | warm | flat | 50 | library_folder_back | PASS | 10 | 25.711 | 47.887 | 21.413–51.017 |
| D_zenos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.781 | 9.505 | 7.243–9.591 |
| D_zenos | warm | flat | 50 | library_next_page | PASS | 10 | 24.139 | 42.514 | 18.467–45.870 |
| D_zenos | warm | flat | 50 | library_prev_page | PASS | 10 | 22.746 | 40.709 | 17.977–42.693 |
| D_zenos | warm | flat | 50 | open_book | PASS | 10 | 132.720 | 140.084 | 92.631–140.481 |
| D_zenos | warm | flat | 50 | open_book_minimal | PASS | 10 | 107.790 | 117.995 | 72.502–132.546 |
| D_zenos | warm | flat | 50 | open_quick_settings | PASS | 10 | 9.155 | 9.392 | 8.588–9.533 |
| D_zenos | warm | flat | 50 | start_to_home | PASS | 10 | 14.707 | 45.839 | 13.136–49.175 |
| D_zenos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 17.505 | 37.648 | 15.230–39.806 |
| D_zenos | warm | hierarchical | 2000 | close_book | PASS | 10 | 47.692 | 59.999 | 42.979–114.041 |
| D_zenos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 11.296 | 11.924 | 10.481–12.272 |
| D_zenos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 41.613 | 49.096 | 38.722–50.247 |
| D_zenos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 31.009 | 42.453 | 28.873–48.053 |
| D_zenos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.907 | 37.384 | 15.439–41.574 |
| D_zenos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 28.102 | 43.065 | 9.028–44.754 |
| D_zenos | warm | hierarchical | 2000 | open_book | PASS | 10 | 126.052 | 132.403 | 114.620–133.792 |
| D_zenos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 107.302 | 112.325 | 66.498–112.776 |
| D_zenos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 9.034 | 9.724 | 8.599–12.849 |
| D_zenos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 14.029 | 18.193 | 12.316–38.850 |
| D_zenos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 17.202 | 36.439 | 14.684–37.061 |
| D_zenos | warm | hierarchical | 50 | close_book | PASS | 10 | 48.751 | 56.936 | 43.165–58.408 |
| D_zenos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 10.905 | 11.970 | 10.191–12.424 |
| D_zenos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 41.650 | 50.994 | 38.991–55.625 |
| D_zenos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 29.724 | 42.050 | 27.227–47.917 |
| D_zenos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 17.564 | 37.158 | 14.492–40.699 |
| D_zenos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 13.443 | 26.787 | 7.761–35.257 |
| D_zenos | warm | hierarchical | 50 | open_book | PASS | 10 | 119.312 | 126.384 | 108.150–131.309 |
| D_zenos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 96.582 | 109.169 | 68.849–114.151 |
| D_zenos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.832 | 9.237 | 8.331–9.246 |
| D_zenos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 13.471 | 14.655 | 11.115–14.669 |
| E_project_title | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.783 | 14.187 | 12.557–14.538 |
| E_project_title | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 10.582 | 10.880 | 10.416–10.954 |
| E_project_title | warm | flat | 2000 | change_sort_mode | PASS | 10 | 104.849 | 112.286 | 96.364–113.109 |
| E_project_title | warm | flat | 2000 | close_book | PASS | 10 | 58.924 | 62.021 | 57.066–66.754 |
| E_project_title | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.264 | 8.984 | 7.582–9.137 |
| E_project_title | warm | flat | 2000 | home_to_library | PASS | 10 | 66.654 | 75.236 | 63.880–78.160 |
| E_project_title | warm | flat | 2000 | library_first_render | PASS | 10 | 68.054 | 74.984 | 63.491–77.438 |
| E_project_title | warm | flat | 2000 | library_folder_back | PASS | 10 | 63.164 | 69.363 | 56.441–71.371 |
| E_project_title | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.291 | 9.518 | 8.438–9.905 |
| E_project_title | warm | flat | 2000 | library_next_page | PASS | 10 | 13.683 | 16.427 | 10.724–17.765 |
| E_project_title | warm | flat | 2000 | library_prev_page | PASS | 10 | 13.041 | 15.363 | 11.711–17.189 |
| E_project_title | warm | flat | 2000 | open_book | PASS | 10 | 64.831 | 68.286 | 62.432–69.653 |
| E_project_title | warm | flat | 2000 | open_book_minimal | PASS | 10 | 64.001 | 68.610 | 59.660–73.097 |
| E_project_title | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.104 | 8.804 | 7.441–8.850 |
| E_project_title | warm | flat | 2000 | repeated_nav | PASS | 2 | 88.146 | 91.460 | 84.003–92.289 |
| E_project_title | warm | flat | 50 | change_sort_mode | PASS | 10 | 21.082 | 22.834 | 18.985–23.911 |
| E_project_title | warm | flat | 50 | close_book | PASS | 10 | 19.816 | 24.398 | 16.516–25.635 |
| E_project_title | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.236 | 8.849 | 7.762–8.923 |
| E_project_title | warm | flat | 50 | home_to_library | PASS | 10 | 18.184 | 19.276 | 16.639–19.418 |
| E_project_title | warm | flat | 50 | library_first_render | PASS | 10 | 19.459 | 21.919 | 16.726–26.298 |
| E_project_title | warm | flat | 50 | library_folder_back | PASS | 10 | 17.160 | 19.640 | 14.466–21.546 |
| E_project_title | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.913 | 9.179 | 8.309–9.246 |
| E_project_title | warm | flat | 50 | library_next_page | PASS | 10 | 13.037 | 14.990 | 10.848–15.927 |
| E_project_title | warm | flat | 50 | library_prev_page | PASS | 10 | 13.833 | 15.524 | 11.527–16.291 |
| E_project_title | warm | flat | 50 | open_book | PASS | 10 | 47.264 | 49.911 | 44.346–54.090 |
| E_project_title | warm | flat | 50 | open_book_minimal | PASS | 10 | 50.411 | 52.875 | 46.635–54.539 |
| E_project_title | warm | flat | 50 | open_quick_settings | PASS | 10 | 7.876 | 8.704 | 7.465–8.991 |
| E_project_title | warm | flat | 50 | repeated_nav | PASS | 2 | 86.168 | 87.951 | 83.939–88.397 |
| E_project_title | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 9.232 | 10.232 | 8.422–10.954 |
| E_project_title | warm | hierarchical | 2000 | close_book | PASS | 10 | 24.130 | 33.168 | 18.599–33.236 |
| E_project_title | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 7.976 | 8.694 | 7.393–8.825 |
| E_project_title | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 11.049 | 12.275 | 8.802–12.511 |
| E_project_title | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 11.743 | 13.010 | 9.154–13.978 |
| E_project_title | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 9.348 | 10.859 | 8.475–11.575 |
| E_project_title | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 19.509 | 22.789 | 8.520–26.473 |
| E_project_title | warm | hierarchical | 2000 | open_book | PASS | 10 | 52.035 | 54.250 | 51.587–54.962 |
| E_project_title | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 52.127 | 53.458 | 48.689–54.157 |
| E_project_title | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.146 | 8.773 | 7.606–8.910 |
| E_project_title | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 86.679 | 89.721 | 82.878–90.481 |
| E_project_title | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.996 | 9.572 | 7.711–10.587 |
| E_project_title | warm | hierarchical | 50 | close_book | PASS | 10 | 18.599 | 20.915 | 15.456–23.863 |
| E_project_title | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.325 | 8.753 | 7.725–8.978 |
| E_project_title | warm | hierarchical | 50 | home_to_library | PASS | 10 | 11.037 | 12.267 | 9.446–12.425 |
| E_project_title | warm | hierarchical | 50 | library_first_render | PASS | 10 | 10.825 | 12.002 | 9.934–13.265 |
| E_project_title | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 9.643 | 10.446 | 8.000–10.487 |
| E_project_title | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 9.582 | 11.769 | 8.685–12.247 |
| E_project_title | warm | hierarchical | 50 | open_book | PASS | 10 | 49.311 | 50.697 | 46.188–53.490 |
| E_project_title | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 48.987 | 51.647 | 48.095–52.136 |
| E_project_title | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.250 | 8.615 | 7.573–9.343 |
| F_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 12.162 | 13.070 | 11.991–13.297 |
| F_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 12.382 | 12.818 | 12.000–12.927 |
| F_bookshelf_bookends | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 3.454 | 28.457 | 2.822–38.761 |
| F_bookshelf_bookends | warm | flat | 2000 | bookshelf_page_turn | PASS | 10 | 0.059 | 0.095 | 0.033–0.173 |
| F_bookshelf_bookends | warm | flat | 2000 | change_sort_mode | PASS | 10 | 141.195 | 200.185 | 122.439–203.196 |
| F_bookshelf_bookends | warm | flat | 2000 | close_book | PASS | 10 | 97.501 | 140.205 | 68.172–140.996 |
| F_bookshelf_bookends | warm | flat | 2000 | close_bookshelf | PASS | 10 | 8.927 | 9.365 | 8.303–10.077 |
| F_bookshelf_bookends | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.247 | 8.667 | 7.572–8.904 |
| F_bookshelf_bookends | warm | flat | 2000 | home_to_library | PASS | 10 | 114.244 | 160.335 | 81.048–205.952 |
| F_bookshelf_bookends | warm | flat | 2000 | library_first_render | PASS | 10 | 99.549 | 119.556 | 79.664–231.417 |
| F_bookshelf_bookends | warm | flat | 2000 | library_folder_back | PASS | 10 | 68.779 | 110.010 | 64.534–115.277 |
| F_bookshelf_bookends | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.759 | 9.080 | 6.148–9.111 |
| F_bookshelf_bookends | warm | flat | 2000 | library_next_page | PASS | 10 | 31.358 | 57.619 | 19.042–73.409 |
| F_bookshelf_bookends | warm | flat | 2000 | library_prev_page | PASS | 10 | 36.657 | 83.040 | 27.245–84.623 |
| F_bookshelf_bookends | warm | flat | 2000 | open_book | PASS | 10 | 125.791 | 127.328 | 83.034–128.603 |
| F_bookshelf_bookends | warm | flat | 2000 | open_book_minimal | PASS | 10 | 120.853 | 148.970 | 82.406–154.087 |
| F_bookshelf_bookends | warm | flat | 2000 | open_bookshelf | PASS | 10 | 9.034 | 14.366 | 7.925–17.760 |
| F_bookshelf_bookends | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.211 | 8.710 | 7.389–9.089 |
| F_bookshelf_bookends | warm | flat | 2000 | repeated_nav | PASS | 2 | 284.546 | 322.663 | 236.898–332.193 |
| F_bookshelf_bookends | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 3.910 | 25.089 | 3.307–33.401 |
| F_bookshelf_bookends | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.075 | 0.290 | 0.036–0.529 |
| F_bookshelf_bookends | warm | flat | 50 | change_sort_mode | PASS | 10 | 57.276 | 66.804 | 42.574–81.325 |
| F_bookshelf_bookends | warm | flat | 50 | close_book | PASS | 10 | 30.337 | 39.910 | 24.784–41.623 |
| F_bookshelf_bookends | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.688 | 9.120 | 7.263–10.170 |
| F_bookshelf_bookends | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.058 | 8.364 | 6.019–9.714 |
| F_bookshelf_bookends | warm | flat | 50 | home_to_library | PASS | 10 | 32.512 | 58.149 | 28.252–60.446 |
| F_bookshelf_bookends | warm | flat | 50 | library_first_render | PASS | 10 | 73.118 | 84.417 | 29.268–131.172 |
| F_bookshelf_bookends | warm | flat | 50 | library_folder_back | PASS | 10 | 26.162 | 42.268 | 23.872–44.587 |
| F_bookshelf_bookends | warm | flat | 50 | library_folder_enter | PASS | 10 | 13.107 | 36.172 | 7.093–43.071 |
| F_bookshelf_bookends | warm | flat | 50 | library_next_page | PASS | 10 | 42.957 | 95.713 | 22.568–100.685 |
| F_bookshelf_bookends | warm | flat | 50 | library_prev_page | PASS | 10 | 41.264 | 101.016 | 26.972–111.020 |
| F_bookshelf_bookends | warm | flat | 50 | open_book | PASS | 10 | 63.946 | 91.987 | 55.561–94.457 |
| F_bookshelf_bookends | warm | flat | 50 | open_book_minimal | PASS | 10 | 63.496 | 86.770 | 49.509–87.732 |
| F_bookshelf_bookends | warm | flat | 50 | open_bookshelf | PASS | 10 | 11.859 | 14.869 | 9.609–17.664 |
| F_bookshelf_bookends | warm | flat | 50 | open_quick_settings | PASS | 10 | 7.968 | 8.504 | 6.815–9.152 |
| F_bookshelf_bookends | warm | flat | 50 | repeated_nav | PASS | 2 | 166.018 | 215.298 | 104.418–227.618 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 3.734 | 24.878 | 2.532–31.937 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | bookshelf_page_turn | PASS | 10 | 0.096 | 0.201 | 0.051–0.299 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 10.910 | 13.470 | 8.749–20.968 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | close_book | PASS | 10 | 59.831 | 65.419 | 29.184–67.079 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 8.575 | 9.012 | 7.465–9.525 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 7.998 | 9.120 | 7.503–9.291 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 13.130 | 20.665 | 11.956–22.914 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 12.352 | 21.578 | 10.605–22.445 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 14.846 | 26.796 | 10.408–26.801 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 26.331 | 36.409 | 8.301–37.523 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | open_book | PASS | 10 | 62.005 | 92.998 | 50.762–127.849 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 63.734 | 74.814 | 53.667–79.453 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 10.027 | 14.843 | 8.288–15.257 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.716 | 9.453 | 7.478–10.399 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 217.058 | 218.658 | 215.058–219.058 |
| F_bookshelf_bookends | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 3.373 | 26.527 | 2.783–31.122 |
| F_bookshelf_bookends | warm | hierarchical | 50 | bookshelf_page_turn | PASS | 10 | 0.087 | 0.175 | 0.039–0.221 |
| F_bookshelf_bookends | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 11.119 | 21.662 | 9.096–21.743 |
| F_bookshelf_bookends | warm | hierarchical | 50 | close_book | PASS | 10 | 59.460 | 67.060 | 54.283–67.381 |
| F_bookshelf_bookends | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 8.995 | 10.604 | 8.434–10.723 |
| F_bookshelf_bookends | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.494 | 8.812 | 6.648–10.045 |
| F_bookshelf_bookends | warm | hierarchical | 50 | home_to_library | PASS | 10 | 13.562 | 21.414 | 11.961–22.881 |
| F_bookshelf_bookends | warm | hierarchical | 50 | library_first_render | PASS | 10 | 13.776 | 23.129 | 11.120–24.761 |
| F_bookshelf_bookends | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 14.041 | 19.854 | 9.271–26.682 |
| F_bookshelf_bookends | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.090 | 29.813 | 6.827–30.063 |
| F_bookshelf_bookends | warm | hierarchical | 50 | open_book | PASS | 10 | 73.027 | 86.543 | 53.676–89.475 |
| F_bookshelf_bookends | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 67.085 | 70.491 | 52.226–76.599 |
| F_bookshelf_bookends | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 11.633 | 13.855 | 9.331–14.597 |
| F_bookshelf_bookends | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.087 | 15.695 | 7.558–62.124 |
| G_simpleui_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 0.123 | 0.158 | 0.088–0.167 |
| G_simpleui_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 19.182 | 20.557 | 19.129–20.901 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 4.183 | 107.459 | 3.357–136.969 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | bookshelf_page_turn | PASS | 10 | 0.145 | 0.356 | 0.050–0.640 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | change_sort_mode | PASS | 10 | 148.305 | 203.728 | 103.667–204.716 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | close_book | PASS | 10 | 98.731 | 105.485 | 92.013–106.624 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | close_bookshelf | PASS | 10 | 21.283 | 411.931 | 18.349–3051.813 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.595 | 9.039 | 8.171–9.047 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | home_to_library | PASS | 10 | 0.037 | 0.055 | 0.006–0.097 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | library_first_render | PASS | 10 | 95.076 | 129.659 | 80.148–132.563 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | library_folder_back | PASS | 10 | 69.200 | 97.430 | 62.287–99.511 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.917 | 9.984 | 8.556–10.162 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | library_next_page | PASS | 10 | 17.586 | 45.697 | 15.543–45.975 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | library_prev_page | PASS | 10 | 28.946 | 34.154 | 24.336–63.269 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | open_book | PASS | 10 | 169.245 | 1562.781 | 138.668–13738.721 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | open_book_minimal | PASS | 10 | 104.225 | 200.871 | 87.997–915.584 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | open_bookshelf | PASS | 10 | 13.258 | 16.227 | 10.077–16.841 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.201 | 9.251 | 7.473–9.384 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | repeated_nav | PASS | 2 | 580.468 | 939.374 | 131.837–1029.100 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | start_to_home | PASS | 10 | 0.048 | 0.104 | 0.020–0.118 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 7.465 | 50.251 | 5.874–51.542 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.306 | 0.676 | 0.093–0.820 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | change_sort_mode | PASS | 10 | 45.612 | 64.483 | 33.191–72.174 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | close_book | PASS | 10 | 70.965 | 2330.870 | 58.313–22113.691 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | close_bookshelf | PASS | 10 | 29.892 | 77.773 | 27.929–79.858 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | close_quick_settings | PASS | 10 | 12.865 | 14.034 | 11.466–14.438 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | home_to_library | PASS | 10 | 0.041 | 0.088 | 0.012–0.114 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_first_render | PASS | 10 | 72.639 | 92.565 | 44.686–104.629 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_folder_back | PASS | 10 | 23.431 | 46.767 | 18.686–95.642 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_folder_enter | PASS | 10 | 10.158 | 14.880 | 8.650–16.474 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_next_page | PASS | 10 | 21.422 | 52.275 | 16.451–73.958 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_prev_page | PASS | 10 | 24.560 | 32.575 | 15.158–41.246 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_book | PASS | 10 | 158.637 | 221.923 | 104.986–585.237 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_book_minimal | PASS | 10 | 109.377 | 119.494 | 82.970–125.017 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_bookshelf | PASS | 10 | 17.666 | 18.555 | 16.185–19.575 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.984 | 9.309 | 8.371–9.474 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | repeated_nav | PASS | 2 | 297.918 | 460.701 | 94.439–501.397 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | start_to_home | PASS | 10 | 0.050 | 0.084 | 0.007–0.105 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 6.786 | 51.175 | 4.939–55.078 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | bookshelf_page_turn | PASS | 10 | 0.362 | 0.533 | 0.182–0.742 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 12.008 | 16.498 | 9.826–30.391 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | close_book | PASS | 10 | 161.761 | 886.203 | 54.896–3828.445 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 30.843 | 76.960 | 23.207–82.785 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 11.777 | 13.505 | 8.415–14.943 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 0.015 | 0.044 | 0.004–0.047 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 27.957 | 39.515 | 25.376–39.965 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.484 | 17.912 | 10.327–18.235 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 25.765 | 33.829 | 9.428–49.353 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | open_book | PASS | 10 | 134.613 | 200.702 | 95.414–302.594 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 101.361 | 132.488 | 88.206–142.521 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.855 | 18.505 | 15.014–21.086 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.723 | 9.349 | 8.180–9.354 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 357.467 | 570.392 | 91.311–623.623 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 0.028 | 0.050 | 0.006–0.061 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 3.486 | 44.270 | 3.042–44.370 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | bookshelf_page_turn | PASS | 10 | 0.100 | 0.209 | 0.032–0.299 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 13.107 | 27.094 | 11.462–28.503 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | close_book | PASS | 10 | 56.500 | 123.000 | 38.852–128.244 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 19.585 | 65.164 | 18.174–70.585 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.579 | 8.953 | 7.787–9.036 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | home_to_library | PASS | 10 | 0.036 | 0.057 | 0.006–0.061 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | library_first_render | PASS | 10 | 29.565 | 45.481 | 25.974–47.537 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 14.683 | 36.624 | 10.750–37.463 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.464 | 19.513 | 8.049–21.160 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | open_book | PASS | 10 | 131.697 | 161.096 | 89.231–169.442 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 106.960 | 124.126 | 67.902–128.555 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 13.273 | 2843.167 | 11.810–28278.646 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 7.902 | 9.129 | 7.414–9.143 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | repeated_nav | PASS | 2 | 295.014 | 464.860 | 82.706–507.321 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | start_to_home | PASS | 10 | 0.053 | 0.088 | 0.016–0.116 |
| H_zenos_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 69.530 | 72.785 | 65.874–73.599 |
| H_zenos_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 29.327 | 29.413 | 27.758–29.434 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 4.177 | 42.417 | 3.877–51.771 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | bookshelf_page_turn | PASS | 10 | 0.100 | 0.342 | 0.047–0.475 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | change_sort_mode | PASS | 10 | 108.030 | 140.710 | 90.017–141.715 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | close_book | PASS | 10 | 84.153 | 120.816 | 47.277–128.443 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | close_bookshelf | PASS | 10 | 11.034 | 13.521 | 10.153–19.319 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | close_quick_settings | PASS | 10 | 10.762 | 12.319 | 10.145–13.009 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | home_to_library | PASS | 10 | 78.909 | 103.203 | 69.886–112.152 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | library_first_render | PASS | 10 | 76.125 | 113.259 | 64.894–113.409 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | library_folder_back | PASS | 10 | 51.558 | 77.652 | 49.257–79.881 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.498 | 9.104 | 5.132–9.427 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | library_next_page | PASS | 10 | 8.764 | 17.307 | 7.558–33.882 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | library_prev_page | PASS | 10 | 8.764 | 34.147 | 6.880–38.307 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | open_book | PASS | 10 | 143.831 | 150.599 | 101.052–151.215 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | open_book_minimal | PASS | 10 | 127.858 | 137.562 | 110.348–145.176 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | open_bookshelf | PASS | 10 | 10.190 | 14.021 | 8.676–16.927 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.777 | 9.439 | 5.822–9.852 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | repeated_nav | PASS | 2 | 262.073 | 405.395 | 82.920–441.226 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | start_to_home | PASS | 10 | 9.619 | 12.466 | 8.576–12.507 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 7.518 | 40.549 | 6.514–48.552 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.308 | 0.677 | 0.118–0.685 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | change_sort_mode | PASS | 10 | 21.722 | 39.694 | 17.524–40.476 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | close_book | PASS | 10 | 61.745 | 113.275 | 58.700–117.504 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | close_bookshelf | PASS | 10 | 17.494 | 19.046 | 16.471–19.363 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | close_quick_settings | PASS | 10 | 22.867 | 23.560 | 19.549–23.612 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | home_to_library | PASS | 10 | 41.874 | 51.667 | 39.036–54.986 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_first_render | PASS | 10 | 41.072 | 56.978 | 27.055–80.579 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_folder_back | PASS | 10 | 26.781 | 43.787 | 23.886–45.924 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.450 | 11.337 | 7.837–28.578 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_next_page | PASS | 10 | 21.538 | 33.534 | 17.481–42.621 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_prev_page | PASS | 10 | 22.204 | 39.865 | 17.856–41.820 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_book | PASS | 10 | 126.847 | 140.127 | 95.303–141.656 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_book_minimal | PASS | 10 | 102.744 | 114.293 | 71.274–118.928 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_bookshelf | PASS | 10 | 15.328 | 19.228 | 13.905–19.412 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_quick_settings | PASS | 10 | 9.458 | 10.461 | 8.941–11.565 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | start_to_home | PASS | 10 | 14.620 | 16.032 | 13.007–16.379 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 3.204 | 38.314 | 2.688–49.869 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | bookshelf_page_turn | PASS | 10 | 0.092 | 0.266 | 0.037–0.273 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.523 | 32.862 | 14.830–36.051 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | close_book | PASS | 10 | 53.197 | 106.687 | 44.857–114.581 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 9.779 | 10.674 | 9.341–15.764 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 10.963 | 12.700 | 9.708–13.252 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 40.803 | 51.316 | 38.199–51.877 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 29.968 | 43.147 | 25.523–48.536 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 17.462 | 35.065 | 14.385–35.275 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 24.008 | 42.567 | 6.483–42.635 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | open_book | PASS | 10 | 122.857 | 130.810 | 114.083–132.406 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 107.496 | 121.773 | 73.457–135.716 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 11.494 | 19.184 | 8.589–19.763 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.983 | 9.366 | 7.103–9.464 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 14.006 | 18.048 | 11.272–43.416 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 4.437 | 38.805 | 3.916–48.284 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | bookshelf_page_turn | PASS | 10 | 0.133 | 0.198 | 0.058–0.228 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 9.831 | 27.670 | 6.180–30.191 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | close_book | PASS | 10 | 53.895 | 63.344 | 43.811–114.276 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 9.818 | 17.742 | 9.016–20.380 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 12.314 | 12.982 | 11.528–14.146 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | home_to_library | PASS | 10 | 30.804 | 35.815 | 27.383–39.659 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | library_first_render | PASS | 10 | 19.630 | 29.181 | 18.303–40.243 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 8.102 | 10.789 | 6.409–30.087 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 10.558 | 28.883 | 7.772–33.034 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | open_book | PASS | 10 | 123.427 | 132.056 | 102.151–132.421 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 104.406 | 115.030 | 64.434–124.103 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 10.633 | 14.158 | 9.436–14.797 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.541 | 9.009 | 8.183–9.073 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | repeated_nav | PASS | 2 | 251.167 | 384.881 | 84.024–418.309 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | start_to_home | PASS | 10 | 9.756 | 13.703 | 8.361–27.526 |
| I_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 0.051 | 0.062 | 0.022–0.065 |
| I_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 13.527 | 14.405 | 11.061–14.624 |
| I_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 131.004 | 155.924 | 99.888–164.736 |
| I_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 101.605 | 110.691 | 93.410–150.845 |
| I_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 8.145 | 8.748 | 7.192–8.820 |
| I_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 0.024 | 0.039 | 0.006–0.065 |
| I_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 85.306 | 131.270 | 78.184–141.490 |
| I_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 63.010 | 93.496 | 59.119–95.716 |
| I_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.956 | 9.361 | 5.735–9.424 |
| I_simpleui_vos | warm | flat | 2000 | library_next_page | PASS | 10 | 16.970 | 58.303 | 11.009–64.482 |
| I_simpleui_vos | warm | flat | 2000 | library_prev_page | PASS | 10 | 17.376 | 57.420 | 12.418–59.340 |
| I_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 152.556 | 875.986 | 128.298–7230.650 |
| I_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 108.275 | 183.619 | 73.687–651.840 |
| I_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.827 | 9.521 | 7.776–10.495 |
| I_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 643.665 | 1078.231 | 100.458–1186.872 |
| I_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 0.044 | 0.085 | 0.006–0.162 |
| I_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 38.936 | 57.216 | 21.348–62.537 |
| I_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 51.480 | 5388.190 | 33.192–52795.034 |
| I_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.284 | 8.849 | 7.445–9.379 |
| I_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 0.038 | 0.126 | 0.009–0.190 |
| I_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 43.233 | 56.188 | 33.992–56.310 |
| I_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 20.951 | 35.906 | 18.806–36.996 |
| I_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.963 | 11.035 | 8.344–25.125 |
| I_simpleui_vos | warm | flat | 50 | library_next_page | PASS | 10 | 17.405 | 21.150 | 16.262–33.180 |
| I_simpleui_vos | warm | flat | 50 | library_prev_page | PASS | 10 | 17.326 | 20.454 | 16.052–36.733 |
| I_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 133.095 | 149.170 | 117.854–155.252 |
| I_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 81.524 | 106.893 | 57.837–110.005 |
| I_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.460 | 9.067 | 7.979–9.123 |
| I_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 267.469 | 414.669 | 83.470–451.469 |
| I_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 0.040 | 0.089 | 0.022–0.105 |
| I_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 11.381 | 14.671 | 10.462–31.708 |
| I_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 119.749 | 4229.274 | 53.696–39711.634 |
| I_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 10.136 | 11.577 | 9.375–12.489 |
| I_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 0.004 | 0.015 | 0.003–0.015 |
| I_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 25.864 | 31.263 | 24.958–45.660 |
| I_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 14.820 | 20.960 | 11.310–41.231 |
| I_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 25.440 | 48.033 | 8.302–50.836 |
| I_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 153.678 | 178.941 | 106.620–180.521 |
| I_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 115.927 | 125.952 | 91.264–148.781 |
| I_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.475 | 8.871 | 7.763–8.980 |
| I_simpleui_vos | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 268.582 | 416.866 | 83.228–453.937 |
| I_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 0.047 | 0.078 | 0.023–0.084 |
| I_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 11.584 | 28.246 | 10.038–29.630 |
| I_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 83.157 | 3231.533 | 53.763–31161.143 |
| I_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 17.657 | 44.239 | 16.514–270.482 |
| I_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 0.013 | 0.051 | 0.004–0.101 |
| I_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 26.630 | 30.591 | 24.838–44.816 |
| I_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 14.168 | 21.938 | 9.770–32.178 |
| I_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.044 | 22.473 | 9.449–33.889 |
| I_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 149.565 | 175.259 | 91.734–182.466 |
| I_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 117.950 | 129.034 | 106.441–132.169 |
| I_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 10.439 | 10.893 | 9.410–11.673 |
| I_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 0.048 | 0.129 | 0.020–0.164 |
| J_project_title_vos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 18.189 | 18.323 | 16.834–18.356 |
| J_project_title_vos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 17.072 | 17.721 | 16.367–17.883 |
| J_project_title_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 17.079 | 17.203 | 16.330–17.234 |
| J_project_title_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.530 | 16.762 | 16.448–16.820 |
| J_project_title_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 78.133 | 83.158 | 76.081–90.190 |
| J_project_title_vos | warm | flat | 2000 | close_book | PASS | 10 | 60.320 | 64.345 | 58.958–65.094 |
| J_project_title_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 9.752 | 11.455 | 8.228–12.063 |
| J_project_title_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 53.993 | 62.234 | 51.959–65.489 |
| J_project_title_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 57.687 | 62.270 | 52.643–68.116 |
| J_project_title_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 43.145 | 50.708 | 41.093–51.068 |
| J_project_title_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.665 | 9.111 | 8.407–9.466 |
| J_project_title_vos | warm | flat | 2000 | library_next_page | PASS | 10 | 9.671 | 10.278 | 7.980–10.537 |
| J_project_title_vos | warm | flat | 2000 | library_prev_page | PASS | 10 | 8.770 | 9.440 | 7.765–9.553 |
| J_project_title_vos | warm | flat | 2000 | open_book | PASS | 10 | 52.852 | 60.999 | 48.974–63.217 |
| J_project_title_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 54.928 | 60.206 | 51.823–60.252 |
| J_project_title_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 8.252 | 9.086 | 7.745–9.096 |
| J_project_title_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 117.494 | 119.986 | 114.379–120.609 |
| J_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 8.446 | 9.094 | 7.591–11.344 |
| J_project_title_vos | warm | flat | 50 | close_book | PASS | 10 | 22.181 | 23.941 | 20.596–26.693 |
| J_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 8.226 | 8.450 | 7.959–9.324 |
| J_project_title_vos | warm | flat | 50 | home_to_library | PASS | 10 | 16.713 | 17.496 | 16.050–18.877 |
| J_project_title_vos | warm | flat | 50 | library_first_render | PASS | 10 | 16.709 | 17.478 | 15.554–20.196 |
| J_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 8.710 | 9.013 | 7.659–9.312 |
| J_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.442 | 8.889 | 7.629–9.329 |
| J_project_title_vos | warm | flat | 50 | library_next_page | PASS | 10 | 8.135 | 9.104 | 7.643–9.256 |
| J_project_title_vos | warm | flat | 50 | library_prev_page | PASS | 10 | 8.738 | 9.434 | 7.214–10.542 |
| J_project_title_vos | warm | flat | 50 | open_book | PASS | 10 | 37.344 | 39.538 | 34.706–42.265 |
| J_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 37.519 | 38.999 | 33.610–39.760 |
| J_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 8.163 | 8.660 | 7.729–9.042 |
| J_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 84.251 | 84.854 | 83.498–85.005 |
| J_project_title_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 8.276 | 8.915 | 7.340–9.262 |
| J_project_title_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 27.372 | 33.300 | 24.972–33.786 |
| J_project_title_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 8.357 | 8.717 | 7.607–9.252 |
| J_project_title_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.573 | 17.400 | 15.898–17.439 |
| J_project_title_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 17.116 | 18.878 | 16.175–20.374 |
| J_project_title_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 9.046 | 9.435 | 7.772–9.447 |
| J_project_title_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 13.855 | 18.132 | 8.306–20.134 |
| J_project_title_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 39.858 | 41.218 | 34.994–41.227 |
| J_project_title_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 39.066 | 41.924 | 37.005–43.167 |
| J_project_title_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 8.136 | 8.669 | 7.538–8.873 |
| J_project_title_vos | warm | hierarchical | 2000 | repeated_nav | PASS | 2 | 83.716 | 84.512 | 82.722–84.711 |
| J_project_title_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 8.378 | 8.954 | 7.580–8.963 |
| J_project_title_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 21.768 | 24.336 | 19.960–26.876 |
| J_project_title_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 8.429 | 8.593 | 7.985–8.666 |
| J_project_title_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.753 | 17.209 | 16.108–17.841 |
| J_project_title_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.934 | 17.817 | 16.139–19.419 |
| J_project_title_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 8.453 | 8.986 | 7.367–9.025 |
| J_project_title_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 8.643 | 9.357 | 7.802–9.567 |
| J_project_title_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 36.156 | 38.931 | 34.392–39.943 |
| J_project_title_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 36.734 | 37.428 | 33.615–38.145 |
| J_project_title_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 8.353 | 8.580 | 7.749–8.759 |
| K_vos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 24.386 | 25.246 | 22.470–25.461 |
| K_vos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 21.789 | 22.663 | 20.986–22.881 |
| A_stock | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 12.330 | 12.330 | 12.330–12.330 |
| A_stock | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 12.635 | 12.635 | 12.635–12.635 |
| B_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 14.977 | 14.977 | 14.977–14.977 |
| B_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 11.949 | 11.949 | 11.949–11.949 |
| C_simpleui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 0.028 | 0.028 | 0.028–0.028 |
| C_simpleui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 23.385 | 23.385 | 23.385–23.385 |
| D_zenos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 70.263 | 70.263 | 70.263–70.263 |
| D_zenos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.444 | 32.444 | 32.444–32.444 |
| E_project_title | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 11.624 | 11.624 | 11.624–11.624 |
| E_project_title | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 8.380 | 8.380 | 8.380–8.380 |
| F_bookshelf_bookends | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 14.779 | 14.779 | 14.779–14.779 |
| F_bookshelf_bookends | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 13.941 | 13.941 | 13.941–13.941 |
| G_simpleui_bookshelf_bookends | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 0.026 | 0.026 | 0.026–0.026 |
| G_simpleui_bookshelf_bookends | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 24.907 | 24.907 | 24.907–24.907 |
| H_zenos_bookshelf_bookends | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 64.342 | 64.342 | 64.342–64.342 |
| H_zenos_bookshelf_bookends | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 31.155 | 31.155 | 31.155–31.155 |
| I_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 0.029 | 0.029 | 0.029–0.029 |
| I_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 12.905 | 12.905 | 12.905–12.905 |
| J_project_title_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 18.170 | 18.170 | 18.170–18.170 |
| J_project_title_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 17.192 | 17.192 | 17.192–17.192 |
| A_stock | warm | flat | 50 | change_sort_mode | PASS | 25 | 42.412 | 68.184 | 20.163–136.519 |
| A_stock | warm | flat | 50 | close_book | PASS | 25 | 28.897 | 61.363 | 22.821–65.800 |
| A_stock | warm | flat | 50 | close_quick_settings | PASS | 25 | 8.338 | 8.818 | 7.482–9.095 |
| A_stock | warm | flat | 50 | home_to_library | PASS | 25 | 36.700 | 76.558 | 12.088–89.502 |
| A_stock | warm | flat | 50 | library_first_render | PASS | 25 | 13.970 | 37.204 | 11.163–52.531 |
| A_stock | warm | flat | 50 | library_folder_back | PASS | 25 | 10.456 | 28.828 | 9.528–61.412 |
| A_stock | warm | flat | 50 | library_folder_enter | PASS | 25 | 9.049 | 38.380 | 4.451–81.217 |
| A_stock | warm | flat | 50 | library_next_page | PASS | 25 | 8.976 | 27.936 | 7.942–34.885 |
| A_stock | warm | flat | 50 | library_prev_page | PASS | 25 | 16.824 | 53.298 | 11.117–143.333 |
| A_stock | warm | flat | 50 | open_book | PASS | 25 | 62.942 | 71.829 | 52.817–90.020 |
| A_stock | warm | flat | 50 | open_book_minimal | PASS | 25 | 61.550 | 66.814 | 43.691–68.792 |
| A_stock | warm | flat | 50 | open_quick_settings | PASS | 25 | 8.320 | 8.885 | 5.002–9.270 |
| A_stock | warm | flat | 50 | repeated_nav | PASS | 4 | 186.759 | 233.916 | 112.896–235.678 |
| B_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 4.186 | 26.154 | 3.581–31.973 |
| B_bookshelf | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.144 | 0.349 | 0.036–0.441 |
| B_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 5 | 43.876 | 67.895 | 37.636–69.019 |
| B_bookshelf | warm | flat | 50 | close_book | PASS | 5 | 28.138 | 49.793 | 26.109–62.725 |
| B_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.988 | 10.045 | 7.672–17.089 |
| B_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 5 | 8.609 | 9.175 | 7.597–9.335 |
| B_bookshelf | warm | flat | 50 | home_to_library | PASS | 5 | 29.441 | 41.462 | 25.750–46.408 |
| B_bookshelf | warm | flat | 50 | library_first_render | PASS | 5 | 32.004 | 44.985 | 27.204–50.335 |
| B_bookshelf | warm | flat | 50 | library_folder_back | PASS | 5 | 26.937 | 27.299 | 22.596–27.505 |
| B_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 5 | 12.953 | 39.501 | 12.678–55.277 |
| B_bookshelf | warm | flat | 50 | library_next_page | PASS | 5 | 25.793 | 42.311 | 22.754–51.657 |
| B_bookshelf | warm | flat | 50 | library_prev_page | PASS | 5 | 72.114 | 96.904 | 30.424–100.706 |
| B_bookshelf | warm | flat | 50 | open_book | PASS | 5 | 66.680 | 71.158 | 57.929–73.124 |
| B_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 5 | 69.154 | 78.991 | 67.766–84.997 |
| B_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 11.021 | 16.613 | 9.514–21.046 |
| B_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 5 | 8.031 | 64.447 | 7.368–100.299 |
| B_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 196.406 | 207.815 | 182.145–210.667 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 25 | 36.757 | 53.857 | 14.361–58.831 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 25 | 56.169 | 161.627 | 36.732–192.389 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 25 | 8.659 | 17.619 | 7.384–19.690 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 25 | 0.004 | 0.034 | 0.003–0.096 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 25 | 47.187 | 67.316 | 22.185–73.124 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 25 | 14.486 | 38.786 | 9.648–58.457 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 25 | 9.229 | 29.339 | 4.928–59.658 |
| C_simpleui | warm | flat | 50 | library_next_page | PASS | 25 | 9.443 | 34.279 | 7.850–52.589 |
| C_simpleui | warm | flat | 50 | library_prev_page | PASS | 25 | 17.727 | 35.833 | 7.761–45.116 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 25 | 131.348 | 221.349 | 91.193–761.448 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 25 | 107.567 | 130.401 | 59.474–397.011 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 25 | 8.356 | 9.775 | 7.576–11.075 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 4 | 246.079 | 585.685 | 82.888–699.446 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 25 | 0.040 | 0.078 | 0.003–0.125 |
| D_zenos | warm | flat | 50 | change_sort_mode | PASS | 25 | 23.292 | 37.878 | 16.655–38.518 |
| D_zenos | warm | flat | 50 | close_book | PASS | 25 | 48.927 | 121.051 | 39.871–134.234 |
| D_zenos | warm | flat | 50 | close_quick_settings | PASS | 25 | 9.730 | 13.538 | 9.383–20.507 |
| D_zenos | warm | flat | 50 | home_to_library | PASS | 25 | 39.730 | 54.886 | 34.132–59.655 |
| D_zenos | warm | flat | 50 | library_first_render | PASS | 25 | 40.473 | 64.242 | 27.130–89.684 |
| D_zenos | warm | flat | 50 | library_folder_back | PASS | 25 | 25.322 | 40.541 | 22.058–47.581 |
| D_zenos | warm | flat | 50 | library_folder_enter | PASS | 25 | 8.611 | 10.022 | 5.867–24.832 |
| D_zenos | warm | flat | 50 | library_next_page | PASS | 25 | 22.128 | 41.797 | 18.220–42.346 |
| D_zenos | warm | flat | 50 | library_prev_page | PASS | 25 | 21.925 | 37.275 | 17.800–40.979 |
| D_zenos | warm | flat | 50 | open_book | PASS | 25 | 133.013 | 155.062 | 69.680–162.265 |
| D_zenos | warm | flat | 50 | open_book_minimal | PASS | 25 | 96.380 | 127.790 | 56.873–140.748 |
| D_zenos | warm | flat | 50 | open_quick_settings | PASS | 25 | 9.135 | 9.365 | 5.857–9.509 |
| D_zenos | warm | flat | 50 | start_to_home | PASS | 25 | 13.320 | 28.244 | 11.683–38.135 |
| E_project_title | warm | flat | 50 | change_sort_mode | PASS | 5 | 15.969 | 17.716 | 15.271–18.157 |
| E_project_title | warm | flat | 50 | close_book | PASS | 5 | 26.811 | 29.128 | 23.975–29.792 |
| E_project_title | warm | flat | 50 | close_quick_settings | PASS | 5 | 12.106 | 14.161 | 10.764–14.728 |
| E_project_title | warm | flat | 50 | home_to_library | PASS | 5 | 18.788 | 19.662 | 16.310–19.964 |
| E_project_title | warm | flat | 50 | library_first_render | PASS | 5 | 17.290 | 19.047 | 15.492–19.427 |
| E_project_title | warm | flat | 50 | library_folder_back | PASS | 5 | 16.752 | 18.509 | 15.326–19.587 |
| E_project_title | warm | flat | 50 | library_folder_enter | PASS | 5 | 9.086 | 9.311 | 8.415–9.385 |
| E_project_title | warm | flat | 50 | library_next_page | PASS | 5 | 14.087 | 14.798 | 10.488–15.019 |
| E_project_title | warm | flat | 50 | library_prev_page | PASS | 5 | 12.849 | 16.630 | 12.211–17.804 |
| E_project_title | warm | flat | 50 | open_book | PASS | 5 | 56.314 | 57.075 | 49.421–57.545 |
| E_project_title | warm | flat | 50 | open_book_minimal | PASS | 5 | 47.480 | 49.291 | 45.392–50.158 |
| E_project_title | warm | flat | 50 | open_quick_settings | PASS | 5 | 8.932 | 9.030 | 8.140–9.054 |
| E_project_title | warm | flat | 50 | repeated_nav | PASS | 2 | 173.923 | 176.141 | 171.150–176.696 |
| F_bookshelf_bookends | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 3.066 | 19.164 | 2.581–29.431 |
| F_bookshelf_bookends | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.108 | 0.195 | 0.057–0.509 |
| F_bookshelf_bookends | warm | flat | 50 | change_sort_mode | PASS | 5 | 45.016 | 69.099 | 34.952–73.460 |
| F_bookshelf_bookends | warm | flat | 50 | close_book | PASS | 5 | 59.679 | 61.202 | 35.755–61.216 |
| F_bookshelf_bookends | warm | flat | 50 | close_bookshelf | PASS | 10 | 8.945 | 9.472 | 7.802–10.144 |
| F_bookshelf_bookends | warm | flat | 50 | close_quick_settings | PASS | 5 | 8.070 | 8.175 | 6.047–8.207 |
| F_bookshelf_bookends | warm | flat | 50 | home_to_library | PASS | 5 | 29.800 | 40.615 | 26.099–46.311 |
| F_bookshelf_bookends | warm | flat | 50 | library_first_render | PASS | 5 | 31.738 | 47.300 | 31.267–55.521 |
| F_bookshelf_bookends | warm | flat | 50 | library_folder_back | PASS | 5 | 57.333 | 81.007 | 32.657–94.616 |
| F_bookshelf_bookends | warm | flat | 50 | library_folder_enter | PASS | 5 | 12.266 | 39.778 | 9.164–42.750 |
| F_bookshelf_bookends | warm | flat | 50 | library_next_page | PASS | 5 | 25.785 | 27.362 | 22.425–27.804 |
| F_bookshelf_bookends | warm | flat | 50 | library_prev_page | PASS | 5 | 29.153 | 110.729 | 24.281–116.632 |
| F_bookshelf_bookends | warm | flat | 50 | open_book | PASS | 5 | 121.203 | 123.006 | 101.364–123.965 |
| F_bookshelf_bookends | warm | flat | 50 | open_book_minimal | PASS | 5 | 106.122 | 111.119 | 105.331–112.467 |
| F_bookshelf_bookends | warm | flat | 50 | open_bookshelf | PASS | 10 | 9.930 | 13.867 | 8.549–17.108 |
| F_bookshelf_bookends | warm | flat | 50 | open_quick_settings | PASS | 5 | 8.237 | 8.551 | 7.484–8.609 |
| F_bookshelf_bookends | warm | flat | 50 | repeated_nav | PASS | 2 | 192.493 | 268.666 | 97.276–287.709 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 6.388 | 31.074 | 5.388–33.784 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.343 | 5.449 | 0.212–49.225 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | change_sort_mode | PASS | 5 | 51.507 | 68.874 | 34.630–75.892 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | close_book | PASS | 5 | 74.076 | 121.312 | 60.777–123.768 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | close_bookshelf | PASS | 10 | 25.303 | 54.748 | 19.420–60.199 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | close_quick_settings | PASS | 5 | 8.685 | 8.986 | 7.362–9.012 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | home_to_library | PASS | 5 | 0.040 | 0.081 | 0.008–0.106 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_first_render | PASS | 5 | 70.439 | 89.337 | 29.295–95.836 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_folder_back | PASS | 5 | 30.305 | 49.432 | 26.453–50.372 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_folder_enter | PASS | 5 | 9.363 | 12.840 | 8.711–15.111 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_next_page | PASS | 5 | 30.038 | 33.061 | 24.303–34.061 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | library_prev_page | PASS | 5 | 33.253 | 68.230 | 20.843–78.028 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_book | PASS | 5 | 98.634 | 113.344 | 92.440–117.128 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_book_minimal | PASS | 5 | 98.995 | 108.424 | 95.549–111.518 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_bookshelf | PASS | 10 | 18.342 | 21.691 | 15.985–24.073 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | open_quick_settings | PASS | 5 | 8.433 | 8.648 | 6.713–8.669 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | repeated_nav | PASS | 2 | 697.139 | 1183.454 | 89.245–1305.033 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | start_to_home | PASS | 5 | 0.035 | 0.053 | 0.022–0.063 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 6.966 | 35.922 | 4.911–40.606 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | bookshelf_page_turn | PASS | 10 | 0.332 | 0.561 | 0.137–0.589 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | change_sort_mode | PASS | 5 | 22.433 | 40.953 | 17.767–49.319 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | close_book | PASS | 5 | 60.280 | 61.522 | 58.283–61.844 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | close_bookshelf | PASS | 10 | 18.853 | 28.318 | 18.117–51.740 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | close_quick_settings | PASS | 5 | 21.473 | 23.620 | 19.802–25.018 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | home_to_library | PASS | 5 | 43.764 | 55.445 | 40.759–55.572 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_first_render | PASS | 5 | 30.858 | 54.478 | 27.847–59.336 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_folder_back | PASS | 5 | 26.563 | 44.010 | 21.168–46.274 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_folder_enter | PASS | 5 | 8.464 | 9.568 | 7.775–10.164 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_next_page | PASS | 5 | 35.132 | 50.623 | 19.487–57.300 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | library_prev_page | PASS | 5 | 20.998 | 24.964 | 17.878–27.174 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_book | PASS | 5 | 95.610 | 102.366 | 93.192–105.656 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_book_minimal | PASS | 5 | 91.290 | 99.561 | 62.944–104.287 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.779 | 20.203 | 13.036–27.901 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | open_quick_settings | PASS | 5 | 9.093 | 10.074 | 8.925–10.258 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | repeated_nav | PASS | 2 | 187.508 | 271.161 | 82.942–292.074 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | start_to_home | PASS | 5 | 14.451 | 29.690 | 11.261–38.928 |
| I_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 5 | 37.105 | 56.149 | 32.697–56.736 |
| I_simpleui_vos | warm | flat | 50 | close_book | PASS | 5 | 49.868 | 56.748 | 42.935–57.685 |
| I_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 5 | 15.522 | 16.856 | 14.172–16.892 |
| I_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 5 | 0.079 | 0.082 | 0.050–0.084 |
| I_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 5 | 48.352 | 52.969 | 27.574–55.083 |
| I_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 5 | 21.049 | 24.054 | 19.321–24.376 |
| I_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 5 | 9.366 | 20.563 | 8.493–21.792 |
| I_simpleui_vos | warm | flat | 50 | library_next_page | PASS | 5 | 28.473 | 51.999 | 18.702–53.809 |
| I_simpleui_vos | warm | flat | 50 | library_prev_page | PASS | 5 | 25.904 | 35.365 | 24.915–40.143 |
| I_simpleui_vos | warm | flat | 50 | open_book | PASS | 5 | 97.808 | 105.095 | 94.632–105.866 |
| I_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 5 | 88.147 | 92.486 | 60.861–94.308 |
| I_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 5 | 9.813 | 11.337 | 8.476–11.519 |
| I_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 188.882 | 253.483 | 108.132–269.633 |
| I_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 5 | 0.065 | 0.123 | 0.050–0.160 |
| J_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 5 | 18.200 | 23.984 | 16.762–27.108 |
| J_project_title_vos | warm | flat | 50 | close_book | PASS | 5 | 35.806 | 39.575 | 32.317–40.175 |
| J_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 5 | 14.471 | 16.723 | 13.863–17.076 |
| J_project_title_vos | warm | flat | 50 | home_to_library | PASS | 5 | 28.766 | 31.713 | 26.325–32.318 |
| J_project_title_vos | warm | flat | 50 | library_first_render | PASS | 5 | 27.664 | 28.526 | 25.720–28.876 |
| J_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 5 | 12.833 | 14.164 | 11.929–14.255 |
| J_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 5 | 9.112 | 9.371 | 8.784–9.413 |
| J_project_title_vos | warm | flat | 50 | library_next_page | PASS | 5 | 13.411 | 15.321 | 12.020–15.839 |
| J_project_title_vos | warm | flat | 50 | library_prev_page | PASS | 5 | 14.008 | 16.698 | 12.520–18.120 |
| J_project_title_vos | warm | flat | 50 | open_book | PASS | 5 | 50.601 | 53.852 | 48.821–55.982 |
| J_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 5 | 47.669 | 49.514 | 46.803–50.423 |
| J_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 5 | 9.537 | 10.792 | 9.172–11.153 |
| J_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 170.981 | 171.935 | 169.789–172.174 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 899.690 | 944.415 | 804.047–955.596 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 932.192 | 977.313 | 836.710–988.593 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1012.372 | 1029.064 | 872.631–1033.237 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 458.383 | 503.738 | 457.072–515.077 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 487.782 | 533.762 | 485.560–545.256 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 550.937 | 569.275 | 512.386–573.860 |
| A_stock | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 591.378 | 591.378 | 591.378–591.378 |
| A_stock | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4267.149 | 4267.149 | 4267.149–4267.149 |
| A_stock | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 16361.476 | 16361.476 | 16361.476–16361.476 |
| A_stock | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 572.016 | 572.016 | 572.016–572.016 |
| A_stock | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2129.061 | 2129.061 | 2129.061–2129.061 |
| A_stock | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10409.587 | 10409.587 | 10409.587–10409.587 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 513.370 | 513.370 | 513.370–513.370 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1007.524 | 1007.524 | 1007.524–1007.524 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 5974.308 | 5974.308 | 5974.308–5974.308 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 534.347 | 534.347 | 534.347–534.347 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1021.073 | 1021.073 | 1021.073–1021.073 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5229.706 | 5229.706 | 5229.706–5229.706 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 529.936 | 530.737 | 523.794–530.937 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 563.274 | 563.286 | 560.099–563.289 |
| B_bookshelf | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 593.067 | 596.612 | 589.668–597.498 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 460.180 | 487.669 | 459.636–494.541 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 490.315 | 517.858 | 488.071–524.743 |
| B_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 519.152 | 545.441 | 516.131–552.014 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 608.052 | 608.052 | 608.052–608.052 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4943.953 | 4943.953 | 4943.953–4943.953 |
| B_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 18863.468 | 18863.468 | 18863.468–18863.468 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 628.506 | 628.506 | 628.506–628.506 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2286.501 | 2286.501 | 2286.501–2286.501 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11948.767 | 11948.767 | 11948.767–11948.767 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 523.762 | 523.762 | 523.762–523.762 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1037.189 | 1037.189 | 1037.189–1037.189 |
| B_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7087.136 | 7087.136 | 7087.136–7087.136 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 518.545 | 518.545 | 518.545–518.545 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1010.073 | 1010.073 | 1010.073–1010.073 |
| B_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6487.887 | 6487.887 | 6487.887–6487.887 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 745.448 | 747.556 | 743.667–748.082 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 780.748 | 782.686 | 774.484–783.170 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 815.708 | 830.024 | 811.898–833.603 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 669.050 | 705.072 | 658.764–714.078 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 696.827 | 734.143 | 689.398–743.472 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 738.851 | 770.927 | 724.088–778.946 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 870.564 | 870.564 | 870.564–870.564 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2074.968 | 2074.968 | 2074.968–2074.968 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 50099.579 | 50099.579 | 50099.579–50099.579 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 740.154 | 740.154 | 740.154–740.154 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1416.428 | 1416.428 | 1416.428–1416.428 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 21039.711 | 21039.711 | 21039.711–21039.711 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 902.398 | 902.398 | 902.398–902.398 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1260.377 | 1260.377 | 1260.377–1260.377 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 48663.207 | 48663.207 | 48663.207–48663.207 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 747.100 | 747.100 | 747.100–747.100 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1103.140 | 1103.140 | 1103.140–1103.140 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 44851.628 | 44851.628 | 44851.628–44851.628 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 845.258 | 879.363 | 829.399–887.889 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 969.943 | 1006.627 | 967.251–1015.798 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 1018.251 | 1055.083 | 1012.076–1064.291 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 752.223 | 784.776 | 749.327–792.915 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 866.628 | 894.835 | 856.693–901.887 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 906.973 | 936.371 | 895.759–943.721 |
| D_zenos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 848.577 | 848.577 | 848.577–848.577 |
| D_zenos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4262.964 | 4262.964 | 4262.964–4262.964 |
| D_zenos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 16052.202 | 16052.202 | 16052.202–16052.202 |
| D_zenos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 959.973 | 959.973 | 959.973–959.973 |
| D_zenos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 3047.137 | 3047.137 | 3047.137–3047.137 |
| D_zenos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 12944.618 | 12944.618 | 12944.618–12944.618 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 843.799 | 843.799 | 843.799–843.799 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2753.715 | 2753.715 | 2753.715–2753.715 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11173.975 | 11173.975 | 11173.975–11173.975 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 842.556 | 842.556 | 842.556–842.556 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2709.687 | 2709.687 | 2709.687–2709.687 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10783.392 | 10783.392 | 10783.392–10783.392 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 526.595 | 562.482 | 517.315–571.454 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 555.633 | 592.709 | 545.658–601.978 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 584.085 | 626.159 | 573.909–636.677 |
| E_project_title | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 685.146 | 685.146 | 685.146–685.146 |
| E_project_title | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3121.390 | 3121.390 | 3121.390–3121.390 |
| E_project_title | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12115.704 | 12115.704 | 12115.704–12115.704 |
| E_project_title | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 620.829 | 620.829 | 620.829–620.829 |
| E_project_title | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1314.443 | 1314.443 | 1314.443–1314.443 |
| E_project_title | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6128.028 | 6128.028 | 6128.028–6128.028 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 569.545 | 569.545 | 569.545–569.545 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 983.182 | 983.182 | 983.182–983.182 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 5323.245 | 5323.245 | 5323.245–5323.245 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 603.293 | 603.293 | 603.293–603.293 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1006.012 | 1006.012 | 1006.012–1006.012 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4578.002 | 4578.002 | 4578.002–4578.002 |
| F_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 581.789 | 620.277 | 579.352–629.899 |
| F_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 612.362 | 649.851 | 611.804–659.223 |
| F_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 643.309 | 683.905 | 643.260–694.054 |
| F_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 700.270 | 700.270 | 700.270–700.270 |
| F_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 5119.640 | 5119.640 | 5119.640–5119.640 |
| F_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 20708.637 | 20708.637 | 20708.637–20708.637 |
| F_bookshelf_bookends | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 632.497 | 632.497 | 632.497–632.497 |
| F_bookshelf_bookends | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2192.294 | 2192.294 | 2192.294–2192.294 |
| F_bookshelf_bookends | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 12955.854 | 12955.854 | 12955.854–12955.854 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 608.209 | 608.209 | 608.209–608.209 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1103.361 | 1103.361 | 1103.361–1103.361 |
| F_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 8403.680 | 8403.680 | 8403.680–8403.680 |
| F_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 633.681 | 633.681 | 633.681–633.681 |
| F_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1156.190 | 1156.190 | 1156.190–1156.190 |
| F_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7512.608 | 7512.608 | 7512.608–7512.608 |
| G_simpleui_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 608.330 | 651.666 | 606.463–662.500 |
| G_simpleui_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 638.173 | 683.414 | 637.653–694.724 |
| G_simpleui_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 673.650 | 718.794 | 673.111–730.081 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 795.792 | 795.792 | 795.792–795.792 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1995.837 | 1995.837 | 1995.837–1995.837 |
| G_simpleui_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 56941.306 | 56941.306 | 56941.306–56941.306 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 901.402 | 901.402 | 901.402–901.402 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1690.071 | 1690.071 | 1690.071–1690.071 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 47202.039 | 47202.039 | 47202.039–47202.039 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 691.506 | 691.506 | 691.506–691.506 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1033.126 | 1033.126 | 1033.126–1033.126 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 49247.457 | 49247.457 | 49247.457–49247.457 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 770.100 | 770.100 | 770.100–770.100 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1137.705 | 1137.705 | 1137.705–1137.705 |
| G_simpleui_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 47845.499 | 47845.499 | 47845.499–47845.499 |
| H_zenos_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 675.012 | 710.710 | 674.297–719.635 |
| H_zenos_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 786.548 | 823.612 | 781.769–832.877 |
| H_zenos_bookshelf_bookends | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 827.425 | 862.223 | 821.351–870.922 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 799.574 | 799.574 | 799.574–799.574 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 4312.524 | 4312.524 | 4312.524–4312.524 |
| H_zenos_bookshelf_bookends | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 17901.594 | 17901.594 | 17901.594–17901.594 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 806.949 | 806.949 | 806.949–806.949 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2795.313 | 2795.313 | 2795.313–2795.313 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 14177.238 | 14177.238 | 14177.238–14177.238 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 781.963 | 781.963 | 781.963–781.963 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2659.967 | 2659.967 | 2659.967–2659.967 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12020.021 | 12020.021 | 12020.021–12020.021 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 778.296 | 778.296 | 778.296–778.296 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2213.825 | 2213.825 | 2213.825–2213.825 |
| H_zenos_bookshelf_bookends | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11568.117 | 11568.117 | 11568.117–11568.117 |
| I_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 526.614 | 543.918 | 512.119–548.244 |
| I_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 552.583 | 566.009 | 532.016–569.365 |
| I_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 581.298 | 592.627 | 557.384–595.459 |
| I_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 910.617 | 910.617 | 910.617–910.617 |
| I_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2051.362 | 2051.362 | 2051.362–2051.362 |
| I_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 53739.902 | 53739.902 | 53739.902–53739.902 |
| I_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 704.953 | 704.953 | 704.953–704.953 |
| I_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1221.731 | 1221.731 | 1221.731–1221.731 |
| I_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 73366.197 | 73366.197 | 73366.197–73366.197 |
| I_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 746.709 | 746.709 | 746.709–746.709 |
| I_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1073.923 | 1073.923 | 1073.923–1073.923 |
| I_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 63969.751 | 63969.751 | 63969.751–63969.751 |
| I_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 865.980 | 865.980 | 865.980–865.980 |
| I_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1196.125 | 1196.125 | 1196.125–1196.125 |
| I_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 49647.108 | 49647.108 | 49647.108–49647.108 |
| J_project_title_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 495.166 | 536.234 | 484.341–546.501 |
| J_project_title_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 534.505 | 575.944 | 524.023–586.304 |
| J_project_title_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 564.644 | 599.177 | 550.397–607.810 |
| J_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 449.057 | 461.695 | 445.335–464.855 |
| J_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 486.847 | 500.729 | 483.376–504.199 |
| J_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 513.526 | 525.746 | 509.655–528.801 |
| J_project_title_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 530.748 | 530.748 | 530.748–530.748 |
| J_project_title_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2582.274 | 2582.274 | 2582.274–2582.274 |
| J_project_title_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 10264.346 | 10264.346 | 10264.346–10264.346 |
| J_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 482.250 | 482.250 | 482.250–482.250 |
| J_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1098.998 | 1098.998 | 1098.998–1098.998 |
| J_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4892.247 | 4892.247 | 4892.247–4892.247 |
| J_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 485.039 | 485.039 | 485.039–485.039 |
| J_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1102.021 | 1102.021 | 1102.021–1102.021 |
| J_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 4817.682 | 4817.682 | 4817.682–4817.682 |
| J_project_title_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 480.614 | 480.614 | 480.614–480.614 |
| J_project_title_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1094.993 | 1094.993 | 1094.993–1094.993 |
| J_project_title_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4186.061 | 4186.061 | 4186.061–4186.061 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 630.293 | 667.555 | 557.991–676.870 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 682.302 | 718.269 | 611.420–727.261 |
| K_vos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 714.479 | 749.602 | 643.910–758.382 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 505.919 | 505.919 | 505.919–505.919 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 536.141 | 536.141 | 536.141–536.141 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 564.155 | 564.155 | 564.155–564.155 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 513.818 | 513.818 | 513.818–513.818 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 546.250 | 546.250 | 546.250–546.250 |
| B_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 574.849 | 574.849 | 574.849–574.849 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 847.685 | 847.685 | 847.685–847.685 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 881.632 | 881.632 | 881.632–881.632 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 918.071 | 918.071 | 918.071–918.071 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 850.605 | 850.605 | 850.605–850.605 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 981.081 | 981.081 | 981.081–981.081 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 1022.617 | 1022.617 | 1022.617–1022.617 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 576.202 | 576.202 | 576.202–576.202 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 601.975 | 601.975 | 601.975–601.975 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 631.432 | 631.432 | 631.432–631.432 |
| F_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 628.727 | 628.727 | 628.727–628.727 |
| F_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 663.493 | 663.493 | 663.493–663.493 |
| F_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 696.388 | 696.388 | 696.388–696.388 |
| G_simpleui_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 816.749 | 816.749 | 816.749–816.749 |
| G_simpleui_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 852.311 | 852.311 | 852.311–852.311 |
| G_simpleui_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 888.616 | 888.616 | 888.616–888.616 |
| H_zenos_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 771.631 | 771.631 | 771.631–771.631 |
| H_zenos_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 892.393 | 892.393 | 892.393–892.393 |
| H_zenos_bookshelf_bookends | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 931.611 | 931.611 | 931.611–931.611 |
| I_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 689.769 | 689.769 | 689.769–689.769 |
| I_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 710.183 | 710.183 | 710.183–710.183 |
| I_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 739.819 | 739.819 | 739.819–739.819 |
| J_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 494.054 | 494.054 | 494.054–494.054 |
| J_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 534.171 | 534.171 | 534.171–534.171 |
| J_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 562.597 | 562.597 | 562.597–562.597 |
| A_stock | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 2 | 589.146 | 635.364 | 531.373–646.918 |
| A_stock | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 2 | 2230.850 | 3045.751 | 1212.223–3249.477 |
| A_stock | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 2 | 14981.801 | 21298.101 | 7086.427–22877.175 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 683.784 | 683.784 | 683.784–683.784 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1265.045 | 1265.045 | 1265.045–1265.045 |
| B_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7365.717 | 7365.717 | 7365.717–7365.717 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 2 | 798.116 | 817.386 | 774.029–822.203 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 2 | 1403.972 | 1588.379 | 1173.464–1634.480 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 2 | 16858.656 | 23770.361 | 8219.025–25498.287 |
| D_zenos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 2 | 885.259 | 905.895 | 859.463–911.055 |
| D_zenos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 2 | 3175.199 | 4254.031 | 1826.660–4523.739 |
| D_zenos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 2 | 14336.058 | 20840.659 | 6205.307–22466.809 |
| E_project_title | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 535.698 | 535.698 | 535.698–535.698 |
| E_project_title | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 878.899 | 878.899 | 878.899–878.899 |
| E_project_title | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 3853.425 | 3853.425 | 3853.425–3853.425 |
| F_bookshelf_bookends | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 586.527 | 586.527 | 586.527–586.527 |
| F_bookshelf_bookends | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1178.839 | 1178.839 | 1178.839–1178.839 |
| F_bookshelf_bookends | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7615.144 | 7615.144 | 7615.144–7615.144 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 768.336 | 768.336 | 768.336–768.336 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1157.106 | 1157.106 | 1157.106–1157.106 |
| G_simpleui_bookshelf_bookends | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9935.010 | 9935.010 | 9935.010–9935.010 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 869.835 | 869.835 | 869.835–869.835 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1872.581 | 1872.581 | 1872.581–1872.581 |
| H_zenos_bookshelf_bookends | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8147.053 | 8147.053 | 8147.053–8147.053 |
| I_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 700.463 | 700.463 | 700.463–700.463 |
| I_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 969.335 | 969.335 | 969.335–969.335 |
| I_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6224.123 | 6224.123 | 6224.123–6224.123 |
| J_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 556.967 | 556.967 | 556.967–556.967 |
| J_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1073.951 | 1073.951 | 1073.951–1073.951 |
| J_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4189.518 | 4189.518 | 4189.518–4189.518 |

## Data-derived comparisons

- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_first_render` (first_run_cold, hierarchical, 2000 books): 13.084 vs 13.289 (1.5% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (first_run_cold, hierarchical, 2000 books): 8274.362 vs 8445.829 (2.0% lower).
- `B_bookshelf` has the lower descriptive median than `A_stock` for `process:spawn_to_library_ready_ms` (first_run_cold, hierarchical, 2000 books): 563.274 vs 932.192 (39.6% lower).
- `B_bookshelf` has the lower descriptive median than `A_stock` for `library_first_render` (steady_init, hierarchical, 2000 books): 11.949 vs 12.635 (5.4% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (steady_init, hierarchical, 2000 books): 8238.269 vs 8447.899 (2.5% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `process:spawn_to_library_ready_ms` (steady_init, hierarchical, 2000 books): 536.141 vs 546.250 (1.9% lower).
- `B_bookshelf` has the lower descriptive median than `A_stock` for `library_first_render` (steady_state_cold, hierarchical, 2000 books): 10.987 vs 12.293 (10.6% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (steady_state_cold, hierarchical, 2000 books): 8166.769 vs 8310.864 (1.7% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `process:spawn_to_library_ready_ms` (steady_state_cold, hierarchical, 2000 books): 487.782 vs 490.315 (0.5% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_first_render` (warm, flat, 2000 books): 66.575 vs 94.049 (29.2% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_next_page` (warm, flat, 2000 books): 20.130 vs 29.322 (31.3% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (warm, flat, 2000 books): 22026.733 vs 33481.334 (34.2% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `open_book` (warm, flat, 2000 books): 80.352 vs 85.498 (6.0% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `process:spawn_to_library_ready_ms` (warm, flat, 2000 books): 4267.149 vs 4943.953 (13.7% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_first_render` (warm, flat, 50 books): 13.970 vs 32.004 (56.3% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_next_page` (warm, flat, 50 books): 8.976 vs 25.793 (65.2% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (warm, flat, 50 books): 15899.204 vs 16679.388 (4.7% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `open_book` (warm, flat, 50 books): 62.942 vs 66.680 (5.6% lower).
- `B_bookshelf` has the lower descriptive median than `A_stock` for `process:spawn_to_library_ready_ms` (warm, flat, 50 books): 1265.045 vs 2230.850 (43.3% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_first_render` (warm, hierarchical, 2000 books): 12.610 vs 13.482 (6.5% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (warm, hierarchical, 2000 books): 8343.417 vs 8347.411 (0.0% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `open_book` (warm, hierarchical, 2000 books): 43.438 vs 57.581 (24.6% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 2000 books): 1007.524 vs 1037.189 (2.9% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `library_first_render` (warm, hierarchical, 50 books): 12.537 vs 13.329 (5.9% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `memory:post_library_render_idle` (warm, hierarchical, 50 books): 8348.499 vs 8392.161 (0.5% lower).
- `A_stock` has the lower descriptive median than `B_bookshelf` for `open_book` (warm, hierarchical, 50 books): 42.587 vs 59.620 (28.6% lower).
- `B_bookshelf` has the lower descriptive median than `A_stock` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 50 books): 1010.073 vs 1021.073 (1.1% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (first_run_cold, hierarchical, 2000 books): 13.084 vs 22.817 (42.7% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (first_run_cold, hierarchical, 2000 books): 8274.362 vs 12821.207 (35.5% lower).
- `C_simpleui` has the lower descriptive median than `A_stock` for `process:spawn_to_library_ready_ms` (first_run_cold, hierarchical, 2000 books): 780.748 vs 932.192 (16.2% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (steady_init, hierarchical, 2000 books): 12.635 vs 23.385 (46.0% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (steady_init, hierarchical, 2000 books): 8238.269 vs 12818.715 (35.7% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (steady_init, hierarchical, 2000 books): 536.141 vs 881.632 (39.2% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (steady_state_cold, hierarchical, 2000 books): 12.293 vs 19.484 (36.9% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (steady_state_cold, hierarchical, 2000 books): 8166.769 vs 12823.220 (36.3% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (steady_state_cold, hierarchical, 2000 books): 487.782 vs 696.827 (30.0% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (warm, flat, 2000 books): 66.575 vs 98.166 (32.2% lower).
- `C_simpleui` has the lower descriptive median than `A_stock` for `library_next_page` (warm, flat, 2000 books): 18.805 vs 20.130 (6.6% lower).
- `C_simpleui` has the lower descriptive median than `A_stock` for `memory:post_library_render_idle` (warm, flat, 2000 books): 20702.094 vs 22026.733 (6.0% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `open_book` (warm, flat, 2000 books): 80.352 vs 153.529 (47.7% lower).
- `C_simpleui` has the lower descriptive median than `A_stock` for `process:spawn_to_library_ready_ms` (warm, flat, 2000 books): 2074.968 vs 4267.149 (51.4% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (warm, flat, 50 books): 13.970 vs 47.187 (70.4% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_next_page` (warm, flat, 50 books): 8.976 vs 9.443 (4.9% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (warm, flat, 50 books): 15899.204 vs 16278.262 (2.3% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `open_book` (warm, flat, 50 books): 62.942 vs 131.348 (52.1% lower).
- `C_simpleui` has the lower descriptive median than `A_stock` for `process:spawn_to_library_ready_ms` (warm, flat, 50 books): 1403.972 vs 2230.850 (37.1% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (warm, hierarchical, 2000 books): 12.610 vs 28.425 (55.6% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (warm, hierarchical, 2000 books): 8343.417 vs 14539.340 (42.6% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `open_book` (warm, hierarchical, 2000 books): 43.438 vs 137.248 (68.4% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 2000 books): 1007.524 vs 1260.377 (20.1% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `library_first_render` (warm, hierarchical, 50 books): 12.537 vs 28.300 (55.7% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (warm, hierarchical, 50 books): 8348.499 vs 14535.832 (42.6% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `open_book` (warm, hierarchical, 50 books): 42.587 vs 137.594 (69.0% lower).
- `A_stock` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 50 books): 1021.073 vs 1103.140 (7.4% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `library_first_render` (steady_init, hierarchical, 2000 books): 23.385 vs 24.907 (6.1% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `memory:post_library_render_idle` (steady_init, hierarchical, 2000 books): 12818.715 vs 13629.961 (6.0% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (steady_init, hierarchical, 2000 books): 852.311 vs 881.632 (3.3% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `library_first_render` (steady_state_cold, hierarchical, 2000 books): 19.182 vs 19.484 (1.5% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `memory:post_library_render_idle` (steady_state_cold, hierarchical, 2000 books): 12823.220 vs 13542.630 (5.3% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (steady_state_cold, hierarchical, 2000 books): 638.173 vs 696.827 (8.4% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `library_first_render` (warm, flat, 2000 books): 95.076 vs 98.166 (3.1% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `library_next_page` (warm, flat, 2000 books): 17.586 vs 18.805 (6.5% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `memory:post_library_render_idle` (warm, flat, 2000 books): 20702.094 vs 23025.473 (10.1% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `open_book` (warm, flat, 2000 books): 153.529 vs 169.245 (9.3% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (warm, flat, 2000 books): 1995.837 vs 2074.968 (3.8% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `library_first_render` (warm, flat, 50 books): 47.187 vs 70.439 (33.0% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `library_next_page` (warm, flat, 50 books): 9.443 vs 30.038 (68.6% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `memory:post_library_render_idle` (warm, flat, 50 books): 15719.883 vs 16278.262 (3.4% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `open_book` (warm, flat, 50 books): 98.634 vs 131.348 (24.9% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (warm, flat, 50 books): 1157.106 vs 1403.972 (17.6% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `library_first_render` (warm, hierarchical, 2000 books): 27.957 vs 28.425 (1.6% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `memory:post_library_render_idle` (warm, hierarchical, 2000 books): 14539.340 vs 15252.656 (4.7% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `open_book` (warm, hierarchical, 2000 books): 134.613 vs 137.248 (1.9% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 2000 books): 1033.126 vs 1260.377 (18.0% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `library_first_render` (warm, hierarchical, 50 books): 28.300 vs 29.565 (4.3% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `memory:post_library_render_idle` (warm, hierarchical, 50 books): 14535.832 vs 15267.852 (4.8% lower).
- `G_simpleui_bookshelf_bookends` has the lower descriptive median than `C_simpleui` for `open_book` (warm, hierarchical, 50 books): 131.697 vs 137.594 (4.3% lower).
- `C_simpleui` has the lower descriptive median than `G_simpleui_bookshelf_bookends` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 50 books): 1103.140 vs 1137.705 (3.0% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `library_first_render` (steady_init, hierarchical, 2000 books): 31.155 vs 32.444 (4.0% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `memory:post_library_render_idle` (steady_init, hierarchical, 2000 books): 14853.864 vs 15498.087 (4.2% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `process:spawn_to_library_ready_ms` (steady_init, hierarchical, 2000 books): 892.393 vs 981.081 (9.0% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `library_first_render` (steady_state_cold, hierarchical, 2000 books): 29.327 vs 29.796 (1.6% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `memory:post_library_render_idle` (steady_state_cold, hierarchical, 2000 books): 14532.119 vs 15253.865 (4.7% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `process:spawn_to_library_ready_ms` (steady_state_cold, hierarchical, 2000 books): 786.548 vs 866.628 (9.2% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `library_first_render` (warm, flat, 2000 books): 73.345 vs 76.125 (3.7% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `library_next_page` (warm, flat, 2000 books): 8.418 vs 8.764 (3.9% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `memory:post_library_render_idle` (warm, flat, 2000 books): 20964.637 vs 22744.687 (7.8% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `open_book` (warm, flat, 2000 books): 143.232 vs 143.831 (0.4% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `process:spawn_to_library_ready_ms` (warm, flat, 2000 books): 4262.964 vs 4312.524 (1.1% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `library_first_render` (warm, flat, 50 books): 30.858 vs 40.473 (23.8% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `library_next_page` (warm, flat, 50 books): 22.128 vs 35.132 (37.0% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `memory:post_library_render_idle` (warm, flat, 50 books): 16217.377 vs 17501.191 (7.3% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `open_book` (warm, flat, 50 books): 95.610 vs 133.013 (28.1% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `process:spawn_to_library_ready_ms` (warm, flat, 50 books): 1872.581 vs 3175.199 (41.0% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `library_first_render` (warm, hierarchical, 2000 books): 29.968 vs 31.009 (3.4% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `memory:post_library_render_idle` (warm, hierarchical, 2000 books): 14985.508 vs 15750.183 (4.9% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `open_book` (warm, hierarchical, 2000 books): 122.857 vs 126.052 (2.5% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 2000 books): 2659.967 vs 2753.715 (3.4% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `library_first_render` (warm, hierarchical, 50 books): 19.630 vs 29.724 (34.0% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `memory:post_library_render_idle` (warm, hierarchical, 50 books): 14896.590 vs 16730.172 (11.0% lower).
- `D_zenos` has the lower descriptive median than `H_zenos_bookshelf_bookends` for `open_book` (warm, hierarchical, 50 books): 119.312 vs 123.427 (3.3% lower).
- `H_zenos_bookshelf_bookends` has the lower descriptive median than `D_zenos` for `process:spawn_to_library_ready_ms` (warm, hierarchical, 50 books): 2213.825 vs 2709.687 (18.3% lower).

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. No universal winner is selected.
