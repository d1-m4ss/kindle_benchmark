# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `c792a7f6cfd87cad3e4f4f44f45eae9070b409392d420b44dc24bb4639bd823d`
Reader flash setting: `unset`

Aggregated rows: 556; PASS=498; FAILED=0; UNSUPPORTED=58; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| F_vos | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 18.613 | 33.336 | 13.069 | 35.072 | 17.169 | 33.500 | 11.362 | 37.243 |
| F_vos | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 25.425 | 103.255 | 15.671 | 133.477 | 16.192 | 32.822 | 9.954 | 48.940 |
| F_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| F_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | flat | 2000 | 10 | 200.000 | 1/1 | 30/30 | 18.179 | 34.779 | 13.353 | 37.820 | 18.991 | 32.515 | 12.163 | 40.505 |
| I_vos_bookshelf | warm | flat | 50 | 10 | 5.000 | 1/1 | 4/30 | 110.948 | 147.413 | 82.676 | 157.996 | 16.127 | 32.180 | 10.269 | 82.546 |
| I_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | flat | 2000 | 9 | 222.000 | 1/1 | 30/30 | 16.123 | 32.937 | 7.049 | 49.816 | 12.716 | 36.973 | 9.847 | 38.841 |
| J_simpleui_vos | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 10.872 | 25.126 | 9.374 | 32.248 | 15.928 | 26.800 | 9.504 | 28.969 |
| J_simpleui_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | 9 | 222.000 | 1/1 | 30/30 | 16.104 | 39.771 | 6.618 | 43.695 | 15.104 | 38.678 | 8.424 | 40.395 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 14.693 | 24.801 | 7.316 | 30.560 | 16.035 | 28.105 | 9.387 | 32.430 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | flat | 2000 | 7 | 286.000 | 1/1 | 30/30 | 17.227 | 33.923 | 12.663 | 34.896 | 21.997 | 36.440 | 12.035 | 39.344 |
| L_project_title_vos | warm | flat | 50 | 7 | 8.000 | 1/1 | 7/30 | 15.454 | 24.808 | 10.778 | 27.047 | 18.704 | 26.581 | 7.880 | 28.510 |
| L_project_title_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| L_project_title_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| I_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 147.556 | 164.173 | 124.096 | 241.491 | 132.495 | 156.695 | 126.822 | 180.226 |
| I_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 41.596 | 58.007 | 13.452 | 76.491 | 16.129 | 18.150 | 9.897 | 27.847 |
| I_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 145.743 | 153.688 | 130.637 | 157.681 | 133.150 | 154.423 | 129.961 | 202.553 |
| I_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 32.353 | 40.763 | 21.980 | 43.242 | 23.573 | 37.079 | 16.889 | 47.665 |
| I_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| I_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 148.260 | 152.497 | 129.676 | 280.887 | 132.279 | 134.159 | 121.651 | 243.773 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 23.300 | 26.502 | 10.511 | 141.067 | 16.132 | 16.446 | 9.012 | 127.702 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 157.641 | 165.546 | 132.855 | 165.704 | 132.618 | 145.367 | 111.663 | 186.068 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 14.867 | 18.828 | 6.378 | 20.150 | 16.123 | 16.447 | 8.996 | 62.721 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
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

- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 17.169 ms vs 18.991 ms (9.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 18.179 ms vs 18.613 ms (2.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 16.127 ms vs 16.192 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 25.425 ms vs 110.948 ms (77.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 12.716 ms vs 15.104 ms (15.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 16.104 ms vs 16.123 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 15.928 ms vs 16.035 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 10.872 ms vs 14.693 ms (26.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| F_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 18.348 | 17.195 | 21.274 | 16.907–22.005 |
| F_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.832 | 32.796 | 32.842 | 32.787–32.845 |
| F_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 108.164 | 80.958 | 131.263 | 80.789–132.564 |
| F_vos | warm | flat | 2000 | close_book | PASS | 10 | 81.242 | 78.764 | 82.815 | 77.582–83.529 |
| F_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.661 | 16.643 | 16.676 | 16.635–16.683 |
| F_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 59.768 | 56.731 | 68.695 | 54.784–86.793 |
| F_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 17.169 | 13.080 | 33.500 | 11.362–37.243 |
| F_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 66.085 | 53.093 | 68.308 | 52.258–82.847 |
| F_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 103.264 | 100.000 | 111.315 | 99.984–117.419 |
| F_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 14.427 | 6.357 | 16.646 | 4.955–16.648 |
| F_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 18.613 | 15.642 | 33.336 | 13.069–35.072 |
| F_vos | warm | flat | 2000 | open_book | PASS | 10 | 46.333 | 42.236 | 51.422 | 41.637–51.895 |
| F_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 47.915 | 43.966 | 51.290 | 42.859–51.393 |
| F_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.662 | 16.007 | 18.444 | 10.300–34.345 |
| F_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 238.500 | 226.958 | 250.043 | 224.072–252.929 |
| F_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 39.965 | 24.934 | 49.148 | 23.823–52.438 |
| F_vos | warm | flat | 50 | close_book | PASS | 10 | 31.849 | 29.044 | 34.260 | 29.011–35.396 |
| F_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.663 | 16.654 | 16.680 | 16.651–16.689 |
| F_vos | warm | flat | 50 | home_to_library | PASS | 10 | 32.817 | 29.700 | 49.499 | 26.668–53.315 |
| F_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.192 | 12.878 | 32.822 | 9.954–48.940 |
| F_vos | warm | flat | 50 | library_first_render | PASS | 10 | 43.366 | 39.285 | 93.239 | 32.804–104.377 |
| F_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 33.356 | 28.093 | 36.142 | 27.995–38.430 |
| F_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 21.255 | 11.949 | 26.972 | 10.065–28.015 |
| F_vos | warm | flat | 50 | library_sequential_paging | PASS | 4 | 25.425 | 16.403 | 103.255 | 15.671–133.477 |
| F_vos | warm | flat | 50 | open_book | PASS | 10 | 37.022 | 28.899 | 46.629 | 27.084–50.450 |
| F_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 42.506 | 31.117 | 49.933 | 30.109–53.362 |
| F_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.646 | 14.774 | 16.666 | 8.099–16.673 |
| F_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 168.209 | 161.146 | 175.272 | 159.380–177.038 |
| F_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 27.231 | 9.734 | 121.024 | 8.507–166.052 |
| F_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 32.823 | 28.799 | 41.551 | 26.177–43.566 |
| F_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.662 | 16.634 | 16.754 | 16.522–16.841 |
| F_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.653 | 32.645 | 32.719 | 32.640–32.720 |
| F_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.671 | 32.645 | 32.714 | 32.621–32.752 |
| F_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 31.818 | 20.976 | 35.812 | 19.450–40.598 |
| F_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.800 | 16.387 | 21.237 | 16.363–27.794 |
| F_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 51.695 | 40.590 | 53.814 | 39.721–56.345 |
| F_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 49.204 | 41.361 | 54.178 | 41.267–57.473 |
| F_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.669 | 16.654 | 17.987 | 16.646–28.252 |
| F_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.031 | 12.139 | 104.365 | 6.728–149.213 |
| F_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 22.835 | 21.556 | 25.466 | 20.849–25.747 |
| F_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.660 | 16.648 | 16.683 | 16.628–16.687 |
| F_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.649 | 32.589 | 32.687 | 32.540–32.713 |
| F_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.672 | 32.638 | 32.711 | 32.631–32.714 |
| F_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.322 | 31.491 | 33.377 | 26.383–33.418 |
| F_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 17.270 | 16.592 | 18.737 | 16.220–24.424 |
| F_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 44.695 | 29.448 | 46.347 | 28.253–46.792 |
| F_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 41.772 | 30.644 | 44.625 | 29.720–45.932 |
| F_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.654 | 9.852 | 16.668 | 9.656–16.672 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 15.111 | 14.324 | 24.285 | 14.127–26.578 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.754 | 32.708 | 32.786 | 32.697–32.794 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.495 | 131.018 | 156.695 | 126.822–180.226 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.129 | 12.085 | 18.150 | 9.897–27.847 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 20.669 | 18.464 | 124.755 | 18.126–126.054 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 147.556 | 132.408 | 164.173 | 124.096–241.491 |
| I_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 41.596 | 29.549 | 58.007 | 13.452–76.491 |
| I_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 108.891 | 82.296 | 130.866 | 81.083–148.193 |
| I_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 128.759 | 67.066 | 241.667 | 64.240–251.204 |
| I_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 16.248 | 15.680 | 16.319 | 10.865–16.323 |
| I_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.660 | 16.633 | 16.674 | 16.628–16.679 |
| I_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 57.903 | 54.827 | 78.106 | 53.849–84.926 |
| I_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 18.991 | 13.400 | 32.515 | 12.163–40.505 |
| I_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 60.802 | 53.899 | 72.414 | 52.526–73.549 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 102.498 | 99.924 | 112.345 | 99.632–118.787 |
| I_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 13.753 | 5.679 | 16.642 | 3.018–16.682 |
| I_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 18.179 | 16.204 | 34.779 | 13.353–37.820 |
| I_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 132.974 | 97.364 | 183.350 | 87.880–199.780 |
| I_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 75.726 | 53.475 | 106.779 | 51.922–117.500 |
| I_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 19.258 | 17.433 | 20.923 | 17.126–23.723 |
| I_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.663 | 16.650 | 16.677 | 16.613–16.683 |
| I_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 302.341 | 300.168 | 304.515 | 299.625–305.058 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 133.150 | 131.063 | 154.423 | 129.961–202.553 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 23.573 | 21.268 | 37.079 | 16.889–47.665 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 23.639 | 20.317 | 57.079 | 19.205–61.473 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 145.743 | 131.613 | 153.688 | 130.637–157.681 |
| I_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 32.353 | 22.850 | 40.763 | 21.980–43.242 |
| I_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 28.503 | 19.973 | 50.520 | 19.883–52.123 |
| I_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 33.779 | 32.543 | 42.862 | 28.461–78.256 |
| I_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 16.299 | 13.396 | 16.343 | 5.103–16.348 |
| I_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.654 | 16.630 | 16.687 | 16.623–16.696 |
| I_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 32.755 | 28.991 | 43.611 | 26.184–47.551 |
| I_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.127 | 12.345 | 32.180 | 10.269–82.546 |
| I_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 36.989 | 32.750 | 79.861 | 32.736–80.095 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 33.346 | 29.128 | 40.024 | 28.709–40.919 |
| I_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.621 | 7.413 | 26.623 | 4.555–28.241 |
| I_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 4 | 110.948 | 87.626 | 147.413 | 82.676–157.996 |
| I_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 68.316 | 53.144 | 88.176 | 43.601–96.750 |
| I_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 61.141 | 56.087 | 66.398 | 54.501–67.928 |
| I_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 21.636 | 20.651 | 22.742 | 19.000–23.968 |
| I_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.637 | 16.601 | 16.662 | 16.596–16.667 |
| I_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 256.717 | 247.482 | 265.953 | 245.173–268.262 |
| I_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.497 | 11.691 | 50.603 | 11.539–55.202 |
| I_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 18.773 | 15.090 | 119.729 | 10.678–182.902 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 34.026 | 32.066 | 39.877 | 29.623–69.069 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 16.463 | 15.955 | 16.542 | 15.952–16.657 |
| I_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.666 | 16.642 | 16.823 | 16.588–16.945 |
| I_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.674 | 32.626 | 32.736 | 32.610–32.771 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.666 | 32.636 | 32.734 | 32.570–32.741 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 31.738 | 19.074 | 38.422 | 18.228–39.068 |
| I_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 17.721 | 15.385 | 19.332 | 5.009–29.709 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 76.981 | 52.088 | 88.366 | 49.859–92.871 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 63.424 | 45.494 | 76.194 | 42.514–110.061 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 16.765 | 15.743 | 16.856 | 15.361–16.932 |
| I_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.662 | 16.486 | 16.692 | 16.436–16.724 |
| I_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 13.361 | 6.475 | 42.711 | 6.317–46.511 |
| I_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.041 | 11.460 | 104.407 | 6.517–149.204 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 23.166 | 18.942 | 31.492 | 16.781–43.650 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 16.514 | 16.084 | 16.587 | 12.887–16.599 |
| I_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.648 | 16.579 | 16.695 | 16.551–16.708 |
| I_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.669 | 32.635 | 32.706 | 32.619–32.708 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.660 | 32.630 | 32.694 | 32.612–32.696 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 33.325 | 31.411 | 33.356 | 25.813–33.373 |
| I_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 17.235 | 15.806 | 18.723 | 8.432–24.440 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 69.443 | 64.434 | 74.331 | 62.651–76.476 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 39.687 | 30.442 | 52.893 | 28.863–55.267 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.819 | 16.442 | 17.051 | 14.136–17.289 |
| I_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.655 | 16.645 | 16.679 | 16.627–16.681 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.325 | 7.129 | 7.760 | 7.080–7.869 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 28.379 | 25.972 | 31.869 | 25.370–32.742 |
| J_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 98.023 | 86.637 | 114.697 | 82.828–117.221 |
| J_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 265.756 | 224.782 | 278.389 | 106.355–280.897 |
| J_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.671 | 16.644 | 16.716 | 16.611–16.723 |
| J_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 16.654 | 11.949 | 31.367 | 11.729–31.413 |
| J_simpleui_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 12.716 | 10.309 | 36.973 | 9.847–38.841 |
| J_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 67.394 | 61.303 | 88.875 | 59.453–93.333 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 120.546 | 100.789 | 129.420 | 100.684–141.886 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.901 | 8.390 | 9.982 | 8.377–15.447 |
| J_simpleui_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.123 | 8.040 | 32.937 | 7.049–49.816 |
| J_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 137.177 | 109.408 | 148.428 | 103.406–164.042 |
| J_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 78.513 | 65.633 | 107.909 | 63.036–115.322 |
| J_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.664 | 15.704 | 52.398 | 7.595–373.640 |
| J_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 791.649 | 744.947 | 838.350 | 733.272–850.025 |
| J_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 16.670 | 15.371 | 16.690 | 5.974–16.696 |
| J_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 26.922 | 17.760 | 29.966 | 17.723–31.726 |
| J_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 39.543 | 36.225 | 48.856 | 35.228–106.658 |
| J_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.659 | 16.640 | 16.672 | 16.634–16.688 |
| J_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 16.651 | 13.748 | 29.564 | 12.862–29.753 |
| J_simpleui_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 15.928 | 10.337 | 26.800 | 9.504–28.969 |
| J_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 32.778 | 27.394 | 38.781 | 26.752–38.895 |
| J_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 22.904 | 15.390 | 33.401 | 13.455–34.134 |
| J_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 15.720 | 8.480 | 21.028 | 8.059–22.644 |
| J_simpleui_vos | warm | flat | 50 | library_sequential_paging | PASS | 5 | 10.872 | 9.664 | 25.126 | 9.374–32.248 |
| J_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 60.537 | 54.366 | 122.306 | 46.694–126.034 |
| J_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 53.008 | 41.137 | 85.947 | 33.346–88.666 |
| J_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.954 | 16.680 | 24.985 | 16.651–89.012 |
| J_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 347.285 | 345.068 | 349.502 | 344.514–350.056 |
| J_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 16.666 | 15.224 | 16.680 | 6.351–16.682 |
| J_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 23.120 | 15.396 | 28.565 | 14.617–35.911 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 48.448 | 45.140 | 113.685 | 45.036–156.307 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.646 | 16.632 | 16.664 | 16.618–16.672 |
| J_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.645 | 14.151 | 28.604 | 12.847–29.735 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.772 | 32.717 | 32.791 | 32.696–32.804 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 17.113 | 8.616 | 26.407 | 8.462–26.470 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.410 | 6.392 | 27.978 | 6.262–28.728 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 105.841 | 70.271 | 121.068 | 67.189–130.744 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 40.790 | 38.891 | 84.173 | 38.856–92.853 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.654 | 15.634 | 93.782 | 15.222–104.754 |
| J_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.663 | 15.610 | 16.673 | 6.321–16.675 |
| J_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 15.168 | 8.889 | 25.650 | 8.497–27.527 |
| J_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 33.829 | 32.914 | 43.052 | 32.607–79.917 |
| J_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.661 | 16.630 | 16.679 | 16.590–16.696 |
| J_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.660 | 14.934 | 28.014 | 13.983–28.498 |
| J_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.754 | 32.707 | 32.789 | 32.690–32.843 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 19.553 | 11.571 | 26.584 | 8.075–26.593 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.068 | 6.667 | 26.509 | 6.476–28.257 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 66.054 | 49.594 | 95.429 | 48.222–111.324 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 48.977 | 43.498 | 59.402 | 37.418–61.281 |
| J_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.654 | 16.171 | 22.701 | 13.857–76.871 |
| J_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.668 | 15.665 | 16.707 | 6.942–16.708 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.236 | 6.697 | 8.713 | 6.312–8.832 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 28.963 | 24.739 | 31.800 | 23.683–32.509 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.279 | 130.776 | 134.159 | 121.651–243.773 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.132 | 15.929 | 16.446 | 9.012–127.702 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 15.255 | 12.210 | 119.382 | 11.376–140.988 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 148.260 | 132.531 | 152.497 | 129.676–280.887 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 23.300 | 16.226 | 26.502 | 10.511–141.067 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 100.367 | 84.812 | 112.120 | 82.402–115.159 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 301.435 | 284.998 | 328.094 | 283.888–335.976 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 33.160 | 28.366 | 33.777 | 25.385–38.697 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.663 | 16.613 | 16.673 | 16.604–16.699 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.639 | 11.642 | 31.929 | 11.001–32.471 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.104 | 9.707 | 38.678 | 8.424–40.395 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 68.948 | 62.847 | 90.608 | 59.966–99.233 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 124.754 | 97.093 | 126.490 | 95.208–133.776 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 8.582 | 8.066 | 37.863 | 7.935–45.239 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.104 | 7.424 | 39.771 | 6.618–43.695 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 140.477 | 110.295 | 154.442 | 110.067–160.281 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 83.456 | 72.061 | 97.237 | 60.733–100.104 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.878 | 16.821 | 17.725 | 16.788–21.090 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 17.203 | 16.620 | 63.826 | 15.844–457.041 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 816.693 | 776.691 | 856.695 | 766.690–866.696 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.660 | 13.445 | 16.710 | 6.368–16.714 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.618 | 129.766 | 145.367 | 111.663–186.068 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.123 | 15.542 | 16.447 | 8.996–62.721 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 21.573 | 15.966 | 65.991 | 15.834–72.737 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 157.641 | 132.909 | 165.546 | 132.855–165.704 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 14.867 | 9.250 | 18.828 | 6.378–20.150 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 27.643 | 18.652 | 30.187 | 17.713–32.354 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 40.097 | 35.826 | 45.365 | 34.526–46.153 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 33.206 | 33.064 | 33.228 | 32.618–33.238 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.659 | 16.640 | 16.669 | 16.627–16.674 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.651 | 12.919 | 30.559 | 10.756–32.710 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.035 | 9.770 | 28.105 | 9.387–32.430 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 32.516 | 27.625 | 38.813 | 26.336–39.272 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 19.840 | 16.655 | 34.825 | 14.980–35.144 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.187 | 9.235 | 23.207 | 9.130–23.401 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 14.693 | 7.845 | 24.801 | 7.316–30.560 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 102.285 | 61.907 | 123.414 | 61.580–130.595 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 46.993 | 39.710 | 65.264 | 36.499–90.079 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.782 | 16.734 | 33.110 | 16.687–33.484 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 18.168 | 16.750 | 94.564 | 16.673–102.453 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 376.793 | 371.546 | 382.040 | 370.234–383.352 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.657 | 14.574 | 16.686 | 6.387–16.698 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 15.287 | 12.266 | 56.838 | 11.709–66.243 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 15.530 | 14.317 | 27.824 | 13.992–30.516 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 46.802 | 44.477 | 55.736 | 44.269–102.484 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 32.861 | 31.773 | 33.066 | 29.111–33.115 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.654 | 15.296 | 16.669 | 14.501–16.671 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.662 | 14.326 | 28.793 | 13.043–29.326 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.748 | 32.708 | 32.787 | 32.663–32.791 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 21.304 | 7.448 | 26.496 | 7.421–28.684 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 14.991 | 6.203 | 26.693 | 6.090–26.911 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 103.752 | 95.347 | 121.582 | 92.653–123.814 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 43.136 | 39.201 | 83.759 | 39.098–86.825 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 17.180 | 16.854 | 18.014 | 16.815–18.080 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.788 | 16.374 | 91.872 | 14.040–98.528 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.653 | 15.626 | 16.676 | 6.552–16.679 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 14.893 | 13.079 | 48.802 | 12.714–60.435 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.166 | 9.180 | 26.846 | 8.244–26.896 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 36.165 | 32.389 | 43.851 | 30.048–95.221 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 32.950 | 30.371 | 33.754 | 19.160–37.818 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.664 | 16.176 | 16.680 | 16.092–16.705 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.662 | 13.907 | 28.782 | 12.805–29.458 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.740 | 32.595 | 32.937 | 32.587–32.958 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 12.542 | 7.425 | 27.008 | 7.313–28.726 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.733 | 9.734 | 26.528 | 6.324–26.766 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 63.407 | 53.408 | 100.854 | 53.068–107.338 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 52.977 | 39.306 | 67.828 | 38.070–91.813 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 17.277 | 16.752 | 17.704 | 16.315–17.889 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.660 | 15.696 | 24.477 | 13.308–94.652 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.664 | 15.648 | 16.729 | 6.789–16.736 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 22.832 | 19.712 | 23.968 | 18.932–24.252 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 32.777 | 32.711 | 32.799 | 32.695–32.805 |
| L_project_title_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 103.040 | 82.590 | 114.657 | 77.933–116.449 |
| L_project_title_vos | warm | flat | 2000 | close_book | PASS | 10 | 87.404 | 85.434 | 89.657 | 85.135–91.838 |
| L_project_title_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.660 | 16.634 | 16.675 | 16.606–16.704 |
| L_project_title_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 59.538 | 57.580 | 80.340 | 57.478–81.005 |
| L_project_title_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 21.997 | 12.876 | 36.440 | 12.035–39.344 |
| L_project_title_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 60.981 | 58.430 | 73.665 | 57.667–79.272 |
| L_project_title_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 105.677 | 99.413 | 111.507 | 93.967–114.929 |
| L_project_title_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 7.643 | 2.992 | 16.630 | 2.855–16.652 |
| L_project_title_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 17.227 | 14.617 | 33.923 | 12.663–34.896 |
| L_project_title_vos | warm | flat | 2000 | open_book | PASS | 10 | 44.385 | 43.791 | 46.403 | 43.165–47.520 |
| L_project_title_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 45.512 | 44.474 | 48.241 | 42.888–49.056 |
| L_project_title_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.655 | 16.144 | 18.386 | 11.791–33.743 |
| L_project_title_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 252.445 | 249.111 | 255.780 | 248.277–256.614 |
| L_project_title_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 30.081 | 27.474 | 34.871 | 26.296–35.791 |
| L_project_title_vos | warm | flat | 50 | close_book | PASS | 10 | 30.629 | 27.305 | 39.722 | 24.086–47.533 |
| L_project_title_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.671 | 16.658 | 16.686 | 16.656–16.699 |
| L_project_title_vos | warm | flat | 50 | home_to_library | PASS | 10 | 30.251 | 27.929 | 38.873 | 26.509–39.591 |
| L_project_title_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 18.704 | 10.566 | 26.581 | 7.880–28.510 |
| L_project_title_vos | warm | flat | 50 | library_first_render | PASS | 10 | 31.663 | 28.970 | 36.681 | 28.494–37.678 |
| L_project_title_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 37.052 | 33.472 | 40.201 | 33.180–40.990 |
| L_project_title_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 8.576 | 5.227 | 15.854 | 5.067–23.347 |
| L_project_title_vos | warm | flat | 50 | library_sequential_paging | PASS | 7 | 15.454 | 12.191 | 24.808 | 10.778–27.047 |
| L_project_title_vos | warm | flat | 50 | open_book | PASS | 10 | 33.647 | 26.604 | 39.853 | 24.562–43.749 |
| L_project_title_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 35.972 | 31.898 | 44.437 | 28.988–46.417 |
| L_project_title_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.665 | 16.592 | 24.629 | 16.577–24.872 |
| L_project_title_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 168.984 | 167.159 | 170.810 | 166.703–171.266 |
| L_project_title_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 46.776 | 12.008 | 117.664 | 11.742–132.821 |
| L_project_title_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 44.338 | 39.779 | 47.797 | 39.255–50.915 |
| L_project_title_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.674 | 16.624 | 16.761 | 16.573–16.828 |
| L_project_title_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 32.763 | 26.809 | 38.705 | 26.788–38.814 |
| L_project_title_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.803 | 26.853 | 38.768 | 26.648–38.914 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 39.418 | 30.605 | 49.231 | 28.886–49.553 |
| L_project_title_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 18.448 | 12.888 | 26.676 | 12.086–28.888 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 46.305 | 36.153 | 52.231 | 36.041–53.175 |
| L_project_title_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 47.392 | 42.361 | 54.036 | 37.488–55.047 |
| L_project_title_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.657 | 15.537 | 21.825 | 6.482–66.639 |
| L_project_title_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.142 | 14.896 | 19.512 | 13.941–49.355 |
| L_project_title_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 27.015 | 21.800 | 30.653 | 21.271–34.924 |
| L_project_title_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.676 | 16.669 | 16.698 | 16.666–16.701 |
| L_project_title_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 32.791 | 27.083 | 38.454 | 26.933–38.660 |
| L_project_title_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.814 | 26.848 | 38.711 | 26.822–38.763 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 34.327 | 26.462 | 42.498 | 26.080–42.953 |
| L_project_title_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.771 | 5.287 | 18.004 | 3.269–18.558 |
| L_project_title_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 38.555 | 28.265 | 45.005 | 23.240–45.309 |
| L_project_title_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 30.852 | 26.807 | 46.016 | 24.940–46.645 |
| L_project_title_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.648 | 9.874 | 16.675 | 9.541–16.681 |
| F_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 23.228 | 23.228 | 23.228 | 23.228–23.228 |
| F_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.677 | 32.677 | 32.677 | 32.677–32.677 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 24.042 | 24.042 | 24.042 | 24.042–24.042 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.683 | 32.683 | 32.683 | 32.683–32.683 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 6.468 | 6.468 | 6.468 | 6.468–6.468 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 25.007 | 25.007 | 25.007 | 25.007–25.007 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 6.792 | 6.792 | 6.792 | 6.792–6.792 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 24.550 | 24.550 | 24.550 | 24.550–24.550 |
| L_project_title_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 26.328 | 26.328 | 26.328 | 26.328–26.328 |
| L_project_title_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 32.802 | 32.802 | 32.802 | 32.802–32.802 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 185.360 | 181.659 | 198.487 | 180.734–201.769 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 241.179 | 240.374 | 253.195 | 240.173–256.200 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 245.350 | 244.598 | 257.456 | 244.411–260.483 |
| F_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 254.495 | 254.093 | 266.602 | 253.992–269.629 |
| F_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 270.135 | 270.135 | 270.135 | 270.135–270.135 |
| F_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2807.634 | 2807.634 | 2807.634 | 2807.634–2807.634 |
| F_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 14343.586 | 14343.586 | 14343.586 | 14343.586–14343.586 |
| F_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 14395.740 | 14395.740 | 14395.740 | 14395.740–14395.740 |
| F_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 223.694 | 223.694 | 223.694 | 223.694–223.694 |
| F_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1689.308 | 1689.308 | 1689.308 | 1689.308–1689.308 |
| F_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 8893.675 | 8893.675 | 8893.675 | 8893.675–8893.675 |
| F_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8912.256 | 8912.256 | 8912.256 | 8912.256–8912.256 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 210.353 | 210.353 | 210.353 | 210.353–210.353 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1406.270 | 1406.270 | 1406.270 | 1406.270–1406.270 |
| F_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7456.444 | 7456.444 | 7456.444 | 7456.444–7456.444 |
| F_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7470.894 | 7470.894 | 7470.894 | 7470.894–7470.894 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 213.520 | 213.520 | 213.520 | 213.520–213.520 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1406.219 | 1406.219 | 1406.219 | 1406.219–1406.219 |
| F_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6304.170 | 6304.170 | 6304.170 | 6304.170–6304.170 |
| F_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6315.530 | 6315.530 | 6315.530 | 6315.530–6315.530 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 186.964 | 185.822 | 203.671 | 185.537–207.848 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 239.055 | 238.540 | 265.034 | 238.411–271.529 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 243.215 | 243.130 | 269.476 | 243.109–276.042 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 252.557 | 252.453 | 278.677 | 252.427–285.207 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 290.004 | 290.004 | 290.004 | 290.004–290.004 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2641.951 | 2641.951 | 2641.951 | 2641.951–2641.951 |
| I_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 30814.491 | 30814.491 | 30814.491 | 30814.491–30814.491 |
| I_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 30854.274 | 30854.274 | 30854.274 | 30854.274–30854.274 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 232.043 | 232.043 | 232.043 | 232.043–232.043 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1592.789 | 1592.789 | 1592.789 | 1592.789–1592.789 |
| I_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18356.348 | 18356.348 | 18356.348 | 18356.348–18356.348 |
| I_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18374.383 | 18374.383 | 18374.383 | 18374.383–18374.383 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 222.768 | 222.768 | 222.768 | 222.768–222.768 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1423.355 | 1423.355 | 1423.355 | 1423.355–1423.355 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9700.667 | 9700.667 | 9700.667 | 9700.667–9700.667 |
| I_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9726.689 | 9726.689 | 9726.689 | 9726.689–9726.689 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 224.713 | 224.713 | 224.713 | 224.713–224.713 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1425.095 | 1425.095 | 1425.095 | 1425.095–1425.095 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8281.657 | 8281.657 | 8281.657 | 8281.657–8281.657 |
| I_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8306.021 | 8306.021 | 8306.021 | 8306.021–8306.021 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 270.544 | 259.330 | 286.806 | 256.526–290.872 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 314.940 | 307.426 | 327.015 | 305.548–330.033 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 321.391 | 314.438 | 333.716 | 312.699–336.798 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 331.544 | 326.229 | 343.959 | 324.900–347.062 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 353.998 | 353.998 | 353.998 | 353.998–353.998 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2023.429 | 2023.429 | 2023.429 | 2023.429–2023.429 |
| J_simpleui_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 23153.111 | 23153.111 | 23153.111 | 23153.111–23153.111 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 23202.700 | 23202.700 | 23202.700 | 23202.700–23202.700 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 310.244 | 310.244 | 310.244 | 310.244–310.244 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1507.020 | 1507.020 | 1507.020 | 1507.020–1507.020 |
| J_simpleui_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 10755.814 | 10755.814 | 10755.814 | 10755.814–10755.814 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10784.041 | 10784.041 | 10784.041 | 10784.041–10784.041 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 306.609 | 306.609 | 306.609 | 306.609–306.609 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1490.015 | 1490.015 | 1490.015 | 1490.015–1490.015 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9435.609 | 9435.609 | 9435.609 | 9435.609–9435.609 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9463.171 | 9463.171 | 9463.171 | 9463.171–9463.171 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 302.227 | 302.227 | 302.227 | 302.227–302.227 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1474.250 | 1474.250 | 1474.250 | 1474.250–1474.250 |
| J_simpleui_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8514.219 | 8514.219 | 8514.219 | 8514.219–8514.219 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8541.766 | 8541.766 | 8541.766 | 8541.766–8541.766 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 264.040 | 262.424 | 284.719 | 262.020–289.889 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 306.140 | 305.281 | 331.884 | 305.067–338.320 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 313.027 | 312.447 | 339.156 | 312.302–345.688 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 323.656 | 323.476 | 350.106 | 323.431–356.718 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 509.833 | 509.833 | 509.833 | 509.833–509.833 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2189.337 | 2189.337 | 2189.337 | 2189.337–2189.337 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 36565.219 | 36565.219 | 36565.219 | 36565.219–36565.219 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 75429.826 | 75429.826 | 75429.826 | 75429.826–75429.826 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 323.381 | 323.381 | 323.381 | 323.381–323.381 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1506.279 | 1506.279 | 1506.279 | 1506.279–1506.279 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18626.555 | 18626.555 | 18626.555 | 18626.555–18626.555 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18733.153 | 18733.153 | 18733.153 | 18733.153–18733.153 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 322.204 | 322.204 | 322.204 | 322.204–322.204 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1495.716 | 1495.716 | 1495.716 | 1495.716–1495.716 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 10867.807 | 10867.807 | 10867.807 | 10867.807–10867.807 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 10900.323 | 10900.323 | 10900.323 | 10900.323–10900.323 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 438.350 | 438.350 | 438.350 | 438.350–438.350 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1614.965 | 1614.965 | 1614.965 | 1614.965–1614.965 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10141.058 | 10141.058 | 10141.058 | 10141.058–10141.058 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10216.868 | 10216.868 | 10216.868 | 10216.868–10216.868 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 194.554 | 193.820 | 199.417 | 193.636–200.632 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 255.898 | 255.276 | 257.144 | 255.120–257.455 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 260.625 | 259.821 | 261.707 | 259.620–261.978 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 270.439 | 268.718 | 270.910 | 268.288–271.028 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 282.419 | 282.419 | 282.419 | 282.419–282.419 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2821.989 | 2821.989 | 2821.989 | 2821.989–2821.989 |
| L_project_title_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 14361.173 | 14361.173 | 14361.173 | 14361.173–14361.173 |
| L_project_title_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 14380.451 | 14380.451 | 14380.451 | 14380.451–14380.451 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 228.967 | 228.967 | 228.967 | 228.967–228.967 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1436.901 | 1436.901 | 1436.901 | 1436.901–1436.901 |
| L_project_title_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 7772.244 | 7772.244 | 7772.244 | 7772.244–7772.244 |
| L_project_title_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 7791.837 | 7791.837 | 7791.837 | 7791.837–7791.837 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 214.569 | 214.569 | 214.569 | 214.569–214.569 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1404.451 | 1404.451 | 1404.451 | 1404.451–1404.451 |
| L_project_title_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 7469.916 | 7469.916 | 7469.916 | 7469.916–7469.916 |
| L_project_title_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7483.406 | 7483.406 | 7483.406 | 7483.406–7483.406 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 212.008 | 212.008 | 212.008 | 212.008–212.008 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1402.967 | 1402.967 | 1402.967 | 1402.967–1402.967 |
| L_project_title_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 6483.287 | 6483.287 | 6483.287 | 6483.287–6483.287 |
| L_project_title_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 6496.027 | 6496.027 | 6496.027 | 6496.027–6496.027 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 214.775 | 214.775 | 214.775 | 214.775–214.775 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 275.232 | 275.232 | 275.232 | 275.232–275.232 |
| F_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 279.472 | 279.472 | 279.472 | 279.472–279.472 |
| F_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 288.810 | 288.810 | 288.810 | 288.810–288.810 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 233.131 | 233.131 | 233.131 | 233.131–233.131 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 294.814 | 294.814 | 294.814 | 294.814–294.814 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 299.452 | 299.452 | 299.452 | 299.452–299.452 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 308.742 | 308.742 | 308.742 | 308.742–308.742 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 320.429 | 320.429 | 320.429 | 320.429–320.429 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 358.994 | 358.994 | 358.994 | 358.994–358.994 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 367.048 | 367.048 | 367.048 | 367.048–367.048 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 377.789 | 377.789 | 377.789 | 377.789–377.789 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 318.367 | 318.367 | 318.367 | 318.367–318.367 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 357.071 | 357.071 | 357.071 | 357.071–357.071 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 363.995 | 363.995 | 363.995 | 363.995–363.995 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 374.635 | 374.635 | 374.635 | 374.635–374.635 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 231.944 | 231.944 | 231.944 | 231.944–231.944 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 295.246 | 295.246 | 295.246 | 295.246–295.246 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 299.795 | 299.795 | 299.795 | 299.795–299.795 |
| L_project_title_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 308.618 | 308.618 | 308.618 | 308.618–308.618 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| F_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8946.203 | 8947.837 | 8899.402–8948.246 | 14874.765 | 81632.000 |
| F_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8908.133 | 8911.742 | 8889.953–8912.645 | 9864.570 | 81664.000 |
| F_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 12197.398 | 12197.398 | 12197.398–12197.398 | 20347.602 | 90704.000 |
| F_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 14544.965 | 14544.965 | 14544.965–14544.965 | 33281.280 | 164208.000 |
| F_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17238.761 | 17238.761 | 17238.761–17238.761 | 17273.085 | 185296.000 |
| F_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9499.727 | 9499.727 | 9499.727–9499.727 | 16091.960 | 85904.000 |
| F_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 26078.805 | 26078.805 | 26078.805–26078.805 | 39367.950 | 151440.000 |
| F_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 13468.323 | 13468.323 | 13468.323–13468.323 | 17324.220 | 170624.000 |
| F_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8986.137 | 8986.137 | 8986.137–8986.137 | 9435.307 | 88000.000 |
| F_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8938.258 | 8938.258 | 8938.258–8938.258 | 9508.217 | 89088.000 |
| F_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 17626.948 | 17626.948 | 17626.948–17626.948 | 28059.278 | 130000.000 |
| F_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9005.410 | 9005.410 | 9005.410–9005.410 | 9434.730 | 86400.000 |
| F_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9008.242 | 9008.242 | 9008.242–9008.242 | 9468.243 | 86608.000 |
| F_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 12073.222 | 12073.222 | 12073.222–12073.222 | 23258.824 | 115008.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9354.837 | 9442.493 | 9296.935–9464.407 | 15763.236 | 82992.000 |
| I_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9325.130 | 9345.480 | 9296.810–9350.567 | 10303.401 | 82992.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 12708.434 | 12708.434 | 12708.434–12708.434 | 13323.890 | 92224.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 16976.254 | 16976.254 | 16976.254–16976.254 | 35247.968 | 152288.000 |
| I_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 23145.867 | 23145.867 | 23145.867–23145.867 | 25729.326 | 278512.000 |
| I_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 10021.938 | 10021.938 | 10021.938–10021.938 | 12189.921 | 85216.000 |
| I_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 30387.176 | 30387.176 | 30387.176–30387.176 | 38969.052 | 144528.000 |
| I_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 17870.694 | 17870.694 | 17870.694–17870.694 | 19833.263 | 225792.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9564.555 | 9564.555 | 9564.555–9564.555 | 10635.120 | 86864.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9494.414 | 9494.414 | 9494.414–9494.414 | 10017.475 | 86896.000 |
| I_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 56663.806 | 56663.806 | 56663.806–56663.806 | 72061.776 | 197184.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9550.578 | 9550.578 | 9550.578–9550.578 | 11427.467 | 85952.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9532.629 | 9532.629 | 9532.629–9532.629 | 9991.721 | 86560.000 |
| I_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 45826.552 | 45826.552 | 45826.552–45826.552 | 57161.092 | 164608.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14529.521 | 14553.834 | 14480.139–14559.912 | 21906.249 | 90432.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14724.674 | 14780.133 | 14679.123–14793.998 | 15762.986 | 90784.000 |
| J_simpleui_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17385.561 | 17385.561 | 17385.561–17385.561 | 26051.861 | 97712.000 |
| J_simpleui_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 30165.100 | 30165.100 | 30165.100–30165.100 | 44090.931 | 130896.000 |
| J_simpleui_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 126376.064 | 126376.064 | 126376.064–126376.064 | 128666.768 | 267504.000 |
| J_simpleui_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14836.838 | 14836.838 | 14836.838–14836.838 | 16211.252 | 94160.000 |
| J_simpleui_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 15863.021 | 15863.021 | 15863.021–15863.021 | 17970.910 | 102704.000 |
| J_simpleui_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 58218.479 | 58218.479 | 58218.479–58218.479 | 60960.615 | 191728.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14536.936 | 14536.936 | 14536.936–14536.936 | 16986.986 | 94592.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14888.291 | 14888.291 | 14888.291–14888.291 | 15934.212 | 95056.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 57887.791 | 57887.791 | 57887.791–57887.791 | 66295.334 | 177536.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14530.521 | 14530.521 | 14530.521–14530.521 | 15493.152 | 95200.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14892.654 | 14892.654 | 14892.654–14892.654 | 15852.894 | 97168.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 52991.650 | 52991.650 | 52991.650–52991.650 | 60916.403 | 173600.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14945.839 | 14956.589 | 14938.472–14959.276 | 22749.817 | 91216.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15145.565 | 15158.512 | 15109.370–15161.749 | 16199.804 | 91600.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17937.592 | 17937.592 | 17937.592–17937.592 | 27669.709 | 99392.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 30756.525 | 30756.525 | 30756.525–30756.525 | 44456.604 | 131456.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 130556.253 | 130556.253 | 130556.253–130556.253 | 133260.493 | 293840.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15508.959 | 15508.959 | 15508.959–15508.959 | 16400.696 | 96304.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16550.295 | 16550.295 | 16550.295–16550.295 | 18469.687 | 103968.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 62803.732 | 62803.732 | 62803.732–62803.732 | 62830.475 | 219936.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15186.248 | 15186.248 | 15186.248–15186.248 | 19471.749 | 94336.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15469.900 | 15469.900 | 15469.900–15469.900 | 16374.188 | 96288.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 64422.903 | 64422.903 | 64422.903–64422.903 | 73635.074 | 220672.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 15216.990 | 15216.990 | 15216.990–15216.990 | 17530.793 | 95968.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15377.240 | 15377.240 | 15377.240–15377.240 | 16492.655 | 98064.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 57160.880 | 57160.880 | 57160.880–57160.880 | 65827.494 | 203344.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9111.355 | 9154.849 | 9106.922–9165.723 | 15625.698 | 83616.000 |
| L_project_title_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9144.039 | 9164.380 | 9141.914–9169.465 | 10464.741 | 83616.000 |
| L_project_title_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 12353.906 | 12353.906 | 12353.906–12353.906 | 21414.562 | 95712.000 |
| L_project_title_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 14748.621 | 14748.621 | 14748.621–14748.621 | 24277.966 | 142720.000 |
| L_project_title_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 17357.075 | 17357.075 | 17357.075–17357.075 | 19045.370 | 216256.000 |
| L_project_title_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9583.148 | 9583.148 | 9583.148–9583.148 | 11064.746 | 90240.000 |
| L_project_title_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 9655.629 | 9655.629 | 9655.629–9655.629 | 11415.097 | 101280.000 |
| L_project_title_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 14534.489 | 14534.489 | 14534.489–14534.489 | 16566.474 | 144592.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9159.586 | 9159.586 | 9159.586–9159.586 | 10195.689 | 86432.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9216.445 | 9216.445 | 9216.445–9216.445 | 10161.177 | 89280.000 |
| L_project_title_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 16733.298 | 16733.298 | 16733.298–16733.298 | 29779.562 | 158944.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9124.520 | 9124.520 | 9124.520–9124.520 | 10000.231 | 85792.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9199.027 | 9199.027 | 9199.027–9199.027 | 10234.198 | 87088.000 |
| L_project_title_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 13251.563 | 13251.563 | 13251.563–13251.563 | 20144.146 | 147984.000 |
| F_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8935.688 | 8935.688 | 8935.688–8935.688 | 9770.644 | 86160.000 |
| F_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9031.414 | 9031.414 | 9031.414–9031.414 | 9896.740 | 86192.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9575.719 | 9575.719 | 9575.719–9575.719 | 11511.604 | 85792.000 |
| I_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9596.531 | 9596.531 | 9596.531–9596.531 | 10687.311 | 85792.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14601.975 | 14601.975 | 14601.975–14601.975 | 16821.760 | 94576.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14772.760 | 14772.760 | 14772.760–14772.760 | 16011.319 | 94928.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15111.693 | 15111.693 | 15111.693–15111.693 | 18714.178 | 94912.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15288.295 | 15288.295 | 15288.295–15288.295 | 16497.055 | 95296.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9098.238 | 9098.238 | 9098.238–9098.238 | 9847.364 | 86512.000 |
| L_project_title_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9157.281 | 9157.281 | 9157.281–9157.281 | 10385.506 | 86608.000 |

## Data-derived comparisons

- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 17.169 ms vs 18.991 ms (9.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_sequential_paging` (warm, flat, 2000 books): 18.179 ms vs 18.613 ms (2.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `I_vos_bookshelf` has a lower descriptive median than `F_vos` for `library_cached_paging` (warm, flat, 50 books): 16.127 ms vs 16.192 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `F_vos` has a lower descriptive median than `I_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 25.425 ms vs 110.948 ms (77.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 12.716 ms vs 15.104 ms (15.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 16.104 ms vs 16.123 ms (0.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 15.928 ms vs 16.035 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 50 books): 10.872 ms vs 14.693 ms (26.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
