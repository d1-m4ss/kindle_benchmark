# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `71c62562577d75d79b6dab0405876eeae7ea19ad7d5db59667c6c9cf1bd57e06`
Reader flash setting: `unset`

Aggregated rows: 200; PASS=180; FAILED=0; UNSUPPORTED=20; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| E_project_title | warm | flat | 2000 | 7 | 286.000 | 1/1 | 30/30 | 15.902 | 26.473 | 12.058 | 27.993 | 21.386 | 32.383 | 10.703 | 35.181 |
| E_project_title | warm | flat | 50 | 7 | 8.000 | 1/1 | 7/30 | 16.498 | 17.838 | 14.666 | 18.085 | 20.126 | 26.404 | 9.889 | 31.516 |
| E_project_title | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| E_project_title | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | flat | 2000 | 7 | 286.000 | 1/1 | 30/30 | 16.554 | 30.340 | 13.787 | 31.849 | 22.748 | 33.230 | 10.822 | 34.876 |
| L_project_title_vos | warm | flat | 50 | 7 | 8.000 | 1/1 | 7/30 | 14.459 | 19.613 | 10.185 | 24.419 | 20.091 | 24.822 | 8.998 | 30.393 |
| L_project_title_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
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

- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 2000 books): 21.386 ms vs 22.748 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 2000 books): 15.902 ms vs 16.554 ms (3.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 50 books): 20.091 ms vs 20.126 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 50 books): 14.459 ms vs 16.498 ms (12.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| E_project_title | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 10.768 | 10.126 | 11.196 | 9.965–11.303 |
| E_project_title | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 11.014 | 10.581 | 11.214 | 10.473–11.264 |
| E_project_title | warm | flat | 2000 | change_sort_mode | PASS | 10 | 85.090 | 72.467 | 110.302 | 68.330–117.146 |
| E_project_title | warm | flat | 2000 | close_book | PASS | 10 | 47.410 | 44.807 | 64.945 | 43.568–66.566 |
| E_project_title | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.642 | 16.627 | 16.667 | 16.585–16.675 |
| E_project_title | warm | flat | 2000 | home_to_library | PASS | 10 | 44.943 | 43.534 | 57.260 | 43.125–59.246 |
| E_project_title | warm | flat | 2000 | library_cached_paging | PASS | 30 | 21.386 | 12.087 | 32.383 | 10.703–35.181 |
| E_project_title | warm | flat | 2000 | library_first_render | PASS | 10 | 44.097 | 42.369 | 56.390 | 42.322–59.781 |
| E_project_title | warm | flat | 2000 | library_folder_back | PASS | 10 | 84.265 | 73.955 | 95.212 | 71.638–101.762 |
| E_project_title | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.312 | 3.209 | 22.027 | 3.052–26.484 |
| E_project_title | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 15.902 | 13.887 | 26.473 | 12.058–27.993 |
| E_project_title | warm | flat | 2000 | open_book | PASS | 10 | 53.703 | 50.248 | 55.548 | 49.160–55.773 |
| E_project_title | warm | flat | 2000 | open_book_minimal | PASS | 10 | 50.893 | 37.647 | 57.847 | 37.355–57.922 |
| E_project_title | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.667 | 15.366 | 16.691 | 4.071–16.721 |
| E_project_title | warm | flat | 2000 | repeated_nav | PASS | 2 | 257.687 | 252.905 | 262.469 | 251.709–263.664 |
| E_project_title | warm | flat | 50 | change_sort_mode | PASS | 10 | 29.992 | 22.510 | 42.005 | 21.291–45.325 |
| E_project_title | warm | flat | 50 | close_book | PASS | 10 | 25.091 | 21.814 | 34.017 | 20.846–41.186 |
| E_project_title | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.662 | 16.648 | 16.672 | 16.614–16.689 |
| E_project_title | warm | flat | 50 | home_to_library | PASS | 10 | 18.077 | 16.715 | 22.726 | 16.171–24.889 |
| E_project_title | warm | flat | 50 | library_cached_paging | PASS | 30 | 20.126 | 11.947 | 26.404 | 9.889–31.516 |
| E_project_title | warm | flat | 50 | library_first_render | PASS | 10 | 17.733 | 17.177 | 22.616 | 16.753–23.711 |
| E_project_title | warm | flat | 50 | library_folder_back | PASS | 10 | 25.669 | 22.719 | 31.023 | 21.874–31.897 |
| E_project_title | warm | flat | 50 | library_folder_enter | PASS | 10 | 6.250 | 3.788 | 13.523 | 3.457–16.914 |
| E_project_title | warm | flat | 50 | library_sequential_paging | PASS | 7 | 16.498 | 15.612 | 17.838 | 14.666–18.085 |
| E_project_title | warm | flat | 50 | open_book | PASS | 10 | 40.311 | 37.595 | 43.114 | 29.184–49.383 |
| E_project_title | warm | flat | 50 | open_book_minimal | PASS | 10 | 40.527 | 35.437 | 47.863 | 33.650–52.889 |
| E_project_title | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.668 | 15.765 | 17.436 | 7.752–24.326 |
| E_project_title | warm | flat | 50 | repeated_nav | PASS | 2 | 229.725 | 200.926 | 258.524 | 193.726–265.724 |
| E_project_title | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 17.477 | 12.125 | 93.374 | 10.998–115.929 |
| E_project_title | warm | hierarchical | 2000 | close_book | PASS | 10 | 37.340 | 32.343 | 41.410 | 20.278–42.639 |
| E_project_title | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.670 | 16.614 | 16.827 | 16.431–16.837 |
| E_project_title | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.132 | 10.590 | 22.056 | 10.467–23.116 |
| E_project_title | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.115 | 10.928 | 21.839 | 10.749–22.181 |
| E_project_title | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 23.912 | 21.177 | 33.402 | 15.703–35.342 |
| E_project_title | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 13.831 | 11.330 | 16.174 | 10.156–22.623 |
| E_project_title | warm | hierarchical | 2000 | open_book | PASS | 10 | 36.052 | 35.376 | 38.621 | 34.696–48.011 |
| E_project_title | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 39.019 | 36.970 | 55.318 | 35.440–56.690 |
| E_project_title | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.651 | 13.573 | 16.818 | 4.363–16.896 |
| E_project_title | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 14.075 | 12.520 | 21.609 | 12.477–23.768 |
| E_project_title | warm | hierarchical | 50 | close_book | PASS | 10 | 20.939 | 17.319 | 29.908 | 15.028–37.181 |
| E_project_title | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.659 | 16.634 | 24.999 | 16.631–100.014 |
| E_project_title | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.053 | 11.522 | 21.894 | 10.872–23.248 |
| E_project_title | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.168 | 12.724 | 22.501 | 10.978–22.518 |
| E_project_title | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 22.178 | 16.962 | 32.504 | 14.306–33.515 |
| E_project_title | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 10.833 | 3.671 | 25.078 | 3.670–27.042 |
| E_project_title | warm | hierarchical | 50 | open_book | PASS | 10 | 43.511 | 38.601 | 46.873 | 30.220–48.457 |
| E_project_title | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 40.382 | 37.408 | 49.661 | 33.866–55.363 |
| E_project_title | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.655 | 15.544 | 25.815 | 5.887–108.011 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 18.777 | 17.891 | 26.400 | 17.669–28.306 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.681 | 29.832 | 32.695 | 29.120–32.698 |
| L_project_title_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 89.965 | 79.803 | 118.962 | 74.487–119.603 |
| L_project_title_vos | warm | flat | 2000 | close_book | PASS | 10 | 84.382 | 82.360 | 87.757 | 81.921–89.255 |
| L_project_title_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.664 | 16.631 | 16.675 | 16.611–16.679 |
| L_project_title_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 60.021 | 58.128 | 73.080 | 57.805–76.780 |
| L_project_title_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 22.748 | 12.115 | 33.230 | 10.822–34.876 |
| L_project_title_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 63.224 | 57.217 | 76.512 | 56.198–79.395 |
| L_project_title_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 102.593 | 95.719 | 110.184 | 94.688–112.738 |
| L_project_title_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.056 | 3.582 | 10.770 | 3.313–11.485 |
| L_project_title_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.554 | 14.198 | 30.340 | 13.787–31.849 |
| L_project_title_vos | warm | flat | 2000 | open_book | PASS | 10 | 46.022 | 44.959 | 47.508 | 44.265–49.149 |
| L_project_title_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 48.425 | 44.449 | 50.763 | 44.269–53.202 |
| L_project_title_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.660 | 16.175 | 18.915 | 11.941–32.453 |
| L_project_title_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 233.230 | 218.747 | 247.712 | 215.126–251.333 |
| L_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 30.299 | 26.757 | 33.941 | 25.711–35.043 |
| L_project_title_vos | warm | flat | 50 | close_book | PASS | 10 | 45.002 | 36.623 | 51.556 | 36.226–53.452 |
| L_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.654 | 16.646 | 16.661 | 16.638–16.664 |
| L_project_title_vos | warm | flat | 50 | home_to_library | PASS | 10 | 32.474 | 30.307 | 38.361 | 29.555–40.497 |
| L_project_title_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 20.091 | 9.889 | 24.822 | 8.998–30.393 |
| L_project_title_vos | warm | flat | 50 | library_first_render | PASS | 10 | 33.481 | 28.301 | 39.918 | 28.149–41.011 |
| L_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 42.319 | 38.130 | 45.450 | 37.184–46.763 |
| L_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 7.359 | 5.126 | 11.952 | 4.961–19.856 |
| L_project_title_vos | warm | flat | 50 | library_sequential_paging | PASS | 7 | 14.459 | 11.735 | 19.613 | 10.185–24.419 |
| L_project_title_vos | warm | flat | 50 | open_book | PASS | 10 | 43.059 | 37.925 | 49.783 | 34.464–50.334 |
| L_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 40.749 | 34.814 | 49.184 | 34.188–54.755 |
| L_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.668 | 15.850 | 16.685 | 8.867–16.692 |
| L_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 223.371 | 208.110 | 238.633 | 204.295–242.448 |
| L_project_title_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 17.860 | 12.204 | 57.736 | 11.232–132.561 |
| L_project_title_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 40.004 | 37.709 | 42.821 | 36.597–43.767 |
| L_project_title_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.668 | 16.621 | 21.771 | 16.532–66.649 |
| L_project_title_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.799 | 26.550 | 38.994 | 26.398–39.173 |
| L_project_title_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.811 | 26.776 | 38.789 | 26.702–38.932 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 34.917 | 25.879 | 45.083 | 24.430–51.545 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 18.059 | 11.230 | 28.146 | 7.267–29.377 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 48.986 | 44.254 | 52.917 | 38.430–57.362 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 49.107 | 45.013 | 52.611 | 39.617–53.860 |
| L_project_title_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.668 | 16.499 | 17.919 | 16.310–27.780 |
| L_project_title_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 14.573 | 13.567 | 46.128 | 12.831–136.989 |
| L_project_title_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 29.362 | 21.867 | 33.488 | 21.812–39.253 |
| L_project_title_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.681 | 16.638 | 16.710 | 16.606–16.744 |
| L_project_title_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.772 | 27.316 | 38.262 | 26.723–38.916 |
| L_project_title_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.817 | 26.850 | 38.770 | 26.572–38.956 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 34.012 | 28.855 | 40.085 | 27.095–44.301 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 11.959 | 6.233 | 16.889 | 3.189–18.741 |
| L_project_title_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 40.612 | 29.089 | 48.021 | 23.961–49.286 |
| L_project_title_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 34.721 | 27.260 | 45.396 | 25.579–47.214 |
| L_project_title_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.688 | 16.655 | 17.610 | 16.641–25.522 |
| E_project_title | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 12.902 | 12.902 | 12.902 | 12.902–12.902 |
| E_project_title | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 11.677 | 11.677 | 11.677 | 11.677–11.677 |
| L_project_title_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 29.122 | 29.122 | 29.122 | 29.122–29.122 |
| L_project_title_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.781 | 32.781 | 32.781 | 32.781–32.781 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 187.026 | 186.255 | 188.629 | 186.063–189.029 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 214.452 | 212.006 | 215.698 | 211.394–216.010 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 218.590 | 216.106 | 220.092 | 215.485–220.468 |
| E_project_title | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 228.206 | 225.196 | 229.619 | 224.444–229.972 |
| E_project_title | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 264.626 | 264.626 | 264.626 | 264.626–264.626 |
| E_project_title | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1977.874 | 1977.874 | 1977.874 | 1977.874–1977.874 |
| E_project_title | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 11749.806 | 11749.806 | 11749.806 | 11749.806–11749.806 |
| E_project_title | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11765.275 | 11765.275 | 11765.275 | 11765.275–11765.275 |
| E_project_title | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 223.369 | 223.369 | 223.369 | 223.369–223.369 |
| E_project_title | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 921.658 | 921.658 | 921.658 | 921.658–921.658 |
| E_project_title | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 6850.912 | 6850.912 | 6850.912 | 6850.912–6850.912 |
| E_project_title | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6863.801 | 6863.801 | 6863.801 | 6863.801–6863.801 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 209.142 | 209.142 | 209.142 | 209.142–209.142 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 809.351 | 809.351 | 809.351 | 809.351–809.351 |
| E_project_title | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 6092.925 | 6092.925 | 6092.925 | 6092.925–6092.925 |
| E_project_title | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 6108.290 | 6108.290 | 6108.290 | 6108.290–6108.290 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 216.448 | 216.448 | 216.448 | 216.448–216.448 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 815.889 | 815.889 | 815.889 | 815.889–815.889 |
| E_project_title | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 5342.238 | 5342.238 | 5342.238 | 5342.238–5342.238 |
| E_project_title | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5355.080 | 5355.080 | 5355.080 | 5355.080–5355.080 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 212.729 | 204.925 | 213.712 | 202.974–213.958 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 266.063 | 261.051 | 276.885 | 259.798–279.591 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 270.632 | 265.661 | 282.893 | 264.419–285.958 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 279.635 | 274.671 | 292.957 | 273.429–296.287 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 286.976 | 286.976 | 286.976 | 286.976–286.976 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2661.111 | 2661.111 | 2661.111 | 2661.111–2661.111 |
| L_project_title_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 14023.982 | 14023.982 | 14023.982 | 14023.982–14023.982 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 14043.018 | 14043.018 | 14043.018 | 14043.018–14043.018 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 243.031 | 243.031 | 243.031 | 243.031–243.031 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1481.650 | 1481.650 | 1481.650 | 1481.650–1481.650 |
| L_project_title_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 8386.896 | 8386.896 | 8386.896 | 8386.896–8386.896 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8400.343 | 8400.343 | 8400.343 | 8400.343–8400.343 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 225.279 | 225.279 | 225.279 | 225.279–225.279 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1426.043 | 1426.043 | 1426.043 | 1426.043–1426.043 |
| L_project_title_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7326.172 | 7326.172 | 7326.172 | 7326.172–7326.172 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7340.367 | 7340.367 | 7340.367 | 7340.367–7340.367 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 223.081 | 223.081 | 223.081 | 223.081–223.081 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1409.679 | 1409.679 | 1409.679 | 1409.679–1409.679 |
| L_project_title_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6422.652 | 6422.652 | 6422.652 | 6422.652–6422.652 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6435.049 | 6435.049 | 6435.049 | 6435.049–6435.049 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 206.638 | 206.638 | 206.638 | 206.638–206.638 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 236.060 | 236.060 | 236.060 | 236.060–236.060 |
| E_project_title | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 240.777 | 240.777 | 240.777 | 240.777–240.777 |
| E_project_title | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 249.873 | 249.873 | 249.873 | 249.873–249.873 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 224.950 | 224.950 | 224.950 | 224.950–224.950 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 291.056 | 291.056 | 291.056 | 291.056–291.056 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 295.679 | 295.679 | 295.679 | 295.679–295.679 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 304.476 | 304.476 | 304.476 | 304.476–304.476 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| E_project_title | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8402.031 | 8422.791 | 8396.578–8427.980 | 13371.882 | 80512.000 |
| E_project_title | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8395.273 | 8429.973 | 8385.762–8438.648 | 9297.316 | 81584.000 |
| E_project_title | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11067.867 | 11067.867 | 11067.867–11067.867 | 17855.666 | 89808.000 |
| E_project_title | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 11042.746 | 11042.746 | 11042.746–11042.746 | 25960.804 | 116128.000 |
| E_project_title | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 15161.317 | 15161.317 | 15161.317–15161.317 | 16633.282 | 138688.000 |
| E_project_title | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8768.938 | 8768.938 | 8768.938–8768.938 | 9706.645 | 87360.000 |
| E_project_title | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 8747.305 | 8747.305 | 8747.305–8747.305 | 11812.947 | 107968.000 |
| E_project_title | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 11600.923 | 11600.923 | 11600.923–11600.923 | 11623.306 | 138672.000 |
| E_project_title | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8464.641 | 8464.641 | 8464.641–8464.641 | 14882.961 | 85360.000 |
| E_project_title | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8445.922 | 8445.922 | 8445.922–8445.922 | 8872.374 | 92832.000 |
| E_project_title | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 17566.818 | 17566.818 | 17566.818–17566.818 | 27539.511 | 158352.000 |
| E_project_title | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8554.801 | 8554.801 | 8554.801–8554.801 | 14768.425 | 86272.000 |
| E_project_title | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8573.391 | 8573.391 | 8573.391–8573.391 | 9051.347 | 93328.000 |
| E_project_title | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12635.521 | 12635.521 | 12635.521–12635.521 | 23542.158 | 141600.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9118.375 | 9151.716 | 9098.379–9160.051 | 15509.301 | 83392.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9144.461 | 9193.052 | 9122.488–9205.199 | 10384.925 | 83728.000 |
| L_project_title_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11909.027 | 11909.027 | 11909.027–11909.027 | 20927.398 | 95888.000 |
| L_project_title_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 12119.402 | 12119.402 | 12119.402–12119.402 | 21251.014 | 113008.000 |
| L_project_title_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 16023.149 | 16023.149 | 16023.149–16023.149 | 17549.034 | 137664.000 |
| L_project_title_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9543.992 | 9543.992 | 9543.992–9543.992 | 10971.659 | 90608.000 |
| L_project_title_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 9638.348 | 9638.348 | 9638.348–9638.348 | 11963.759 | 103728.000 |
| L_project_title_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 12395.696 | 12395.696 | 12395.696–12395.696 | 13183.867 | 131392.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9100.492 | 9100.492 | 9100.492–9100.492 | 9724.607 | 86752.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9321.020 | 9321.020 | 9321.020–9321.020 | 10233.782 | 90608.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 17023.896 | 17023.896 | 17023.896–17023.896 | 29214.586 | 157312.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9116.777 | 9116.777 | 9116.777–9116.777 | 12900.604 | 86480.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9181.105 | 9181.105 | 9181.105–9181.105 | 10154.928 | 87984.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 13368.009 | 13368.009 | 13368.009–13368.009 | 20211.436 | 144064.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8457.070 | 8457.070 | 8457.070–8457.070 | 14861.633 | 84848.000 |
| E_project_title | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8473.855 | 8473.855 | 8473.855–8473.855 | 9401.169 | 85760.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9133.512 | 9133.512 | 9133.512–9133.512 | 9693.477 | 86592.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9114.543 | 9114.543 | 9114.543–9114.543 | 10456.434 | 86720.000 |

## Data-derived comparisons

- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_cached_paging` (warm, flat, 2000 books): 21.386 ms vs 22.748 ms (6.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `E_project_title` has a lower descriptive median than `L_project_title_vos` for `library_sequential_paging` (warm, flat, 2000 books): 15.902 ms vs 16.554 ms (3.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_cached_paging` (warm, flat, 50 books): 20.091 ms vs 20.126 ms (0.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `L_project_title_vos` has a lower descriptive median than `E_project_title` for `library_sequential_paging` (warm, flat, 50 books): 14.459 ms vs 16.498 ms (12.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
