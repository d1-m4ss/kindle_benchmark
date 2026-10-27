# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `71c62562577d75d79b6dab0405876eeae7ea19ad7d5db59667c6c9cf1bd57e06`
Reader flash setting: `unset`

Aggregated rows: 74; PASS=72; FAILED=0; UNSUPPORTED=2; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R11_project_title_vos | warm | real_2692 | 2692 | 7 | 73.000 | 1/1 | 30/30 | 14.017 | 25.401 | 10.862 | 26.922 | 19.045 | 24.448 | 11.358 | 29.613 |
| R4_project_title | warm | real_2692 | 2692 | 7 | 73.000 | 1/1 | 30/30 | 14.797 | 23.786 | 12.008 | 25.964 | 20.749 | 25.141 | 8.482 | 31.294 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R11_project_title_vos | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R4_project_title | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (warm, real_2692, 2692 books): 19.045 ms vs 20.749 ms (8.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (warm, real_2692, 2692 books): 14.017 ms vs 14.797 ms (5.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R11_project_title_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 46.177 | 46.177 | 46.177 | 46.177–46.177 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 44.300 | 44.300 | 44.300 | 44.300–44.300 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 47.234 | 43.829 | 47.628 | 42.978–47.727 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 44.019 | 43.074 | 45.566 | 42.838–45.953 |
| R11_project_title_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 58.427 | 47.636 | 64.917 | 46.213–80.343 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 52.921 | 43.416 | 64.325 | 41.506–65.149 |
| R11_project_title_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.647 | 16.616 | 16.719 | 16.610–16.955 |
| R11_project_title_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 44.813 | 42.410 | 52.097 | 41.695–52.606 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 19.045 | 12.301 | 24.448 | 11.358–29.613 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 46.252 | 43.322 | 53.678 | 42.228–55.803 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 72.599 | 68.382 | 90.532 | 67.388–95.953 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 22.879 | 20.447 | 92.105 | 17.741–122.359 |
| R11_project_title_vos | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 14.017 | 12.061 | 25.401 | 10.862–26.922 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 56.456 | 45.072 | 62.556 | 39.549–79.291 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 103.215 | 60.041 | 119.612 | 59.187–173.324 |
| R11_project_title_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.664 | 16.647 | 16.671 | 16.637–16.673 |
| R11_project_title_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 827.038 | 827.038 | 827.038 | 827.038–827.038 |
| R4_project_title | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 32.548 | 32.548 | 32.548 | 32.548–32.548 |
| R4_project_title | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 33.410 | 33.410 | 33.410 | 33.410–33.410 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 31.089 | 30.527 | 31.203 | 30.387–31.232 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 29.194 | 28.679 | 29.578 | 28.550–29.674 |
| R4_project_title | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 66.720 | 57.462 | 97.244 | 56.986–116.085 |
| R4_project_title | warm | real_2692 | 2692 | close_book | PASS | 10 | 27.827 | 22.756 | 34.646 | 22.529–37.713 |
| R4_project_title | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.660 | 16.635 | 16.668 | 16.598–16.671 |
| R4_project_title | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 31.698 | 30.413 | 41.308 | 29.259–42.166 |
| R4_project_title | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 20.749 | 11.321 | 25.141 | 8.482–31.294 |
| R4_project_title | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 30.436 | 28.954 | 39.919 | 28.509–40.418 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 81.727 | 62.220 | 117.350 | 62.196–123.829 |
| R4_project_title | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 24.415 | 19.739 | 44.324 | 16.252–116.680 |
| R4_project_title | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 14.797 | 13.482 | 23.786 | 12.008–25.964 |
| R4_project_title | warm | real_2692 | 2692 | open_book | PASS | 10 | 52.150 | 46.270 | 64.600 | 43.328–80.819 |
| R4_project_title | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 98.105 | 52.749 | 120.587 | 52.094–173.190 |
| R4_project_title | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.659 | 15.478 | 16.686 | 5.065–16.718 |
| R4_project_title | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 792.049 | 792.049 | 792.049 | 792.049–792.049 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 253.760 | 253.760 | 253.760 | 253.760–253.760 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 350.464 | 350.464 | 350.464 | 350.464–350.464 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 357.317 | 357.317 | 357.317 | 357.317–357.317 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 366.758 | 366.758 | 366.758 | 366.758–366.758 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 236.842 | 230.933 | 237.462 | 229.456–237.617 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 333.333 | 324.417 | 335.733 | 322.188–336.333 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 340.491 | 331.681 | 343.062 | 329.478–343.705 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 349.776 | 341.062 | 352.637 | 338.883–353.352 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 234.032 | 234.032 | 234.032 | 234.032–234.032 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1980.502 | 1980.502 | 1980.502 | 1980.502–1980.502 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 12937.928 | 12937.928 | 12937.928 | 12937.928–12937.928 |
| R11_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 12957.783 | 12957.783 | 12957.783 | 12957.783–12957.783 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 233.801 | 233.801 | 233.801 | 233.801–233.801 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 305.097 | 305.097 | 305.097 | 305.097–305.097 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 310.823 | 310.823 | 310.823 | 310.823–310.823 |
| R4_project_title | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 319.605 | 319.605 | 319.605 | 319.605–319.605 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 214.251 | 212.107 | 216.132 | 211.571–216.602 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 278.705 | 278.614 | 280.777 | 278.592–281.295 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 284.745 | 284.700 | 286.822 | 284.688–287.342 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 293.602 | 293.575 | 295.625 | 293.568–296.130 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 210.915 | 210.915 | 210.915 | 210.915–210.915 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1406.045 | 1406.045 | 1406.045 | 1406.045–1406.045 |
| R4_project_title | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 11972.013 | 11972.013 | 11972.013 | 11972.013–11972.013 |
| R4_project_title | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 11994.205 | 11994.205 | 11994.205 | 11994.205–11994.205 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10328.168 | 10328.168 | 10328.168–10328.168 | 15048.059 | 85984.000 |
| R11_project_title_vos | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10341.316 | 10341.316 | 10341.316–10341.316 | 17581.070 | 90000.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10321.840 | 10341.840 | 10277.871–10346.840 | 12752.979 | 85024.000 |
| R11_project_title_vos | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10371.316 | 10418.026 | 10351.746–10429.703 | 17435.112 | 87184.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10252.367 | 10252.367 | 10252.367–10252.367 | 13085.828 | 84928.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10372.141 | 10372.141 | 10372.141–10372.141 | 11586.026 | 96672.000 |
| R11_project_title_vos | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 15484.532 | 15484.532 | 15484.532–15484.532 | 16865.983 | 259344.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9139.465 | 9139.465 | 9139.465–9139.465 | 12309.674 | 85392.000 |
| R4_project_title | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9118.805 | 9118.805 | 9118.805–9118.805 | 15238.264 | 87696.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9397.398 | 9422.536 | 9350.434–9428.820 | 10660.484 | 83696.000 |
| R4_project_title | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9356.000 | 9375.741 | 9338.574–9380.676 | 15343.025 | 86048.000 |
| R4_project_title | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9433.012 | 9433.012 | 9433.012–9433.012 | 16853.217 | 83840.000 |
| R4_project_title | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9359.043 | 9359.043 | 9359.043–9359.043 | 15569.514 | 103712.000 |
| R4_project_title | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14201.817 | 14201.817 | 14201.817–14201.817 | 17182.757 | 280720.000 |

## Data-derived comparisons

- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_cached_paging` (warm, real_2692, 2692 books): 19.045 ms vs 20.749 ms (8.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R11_project_title_vos` has a lower descriptive median than `R4_project_title` for `library_sequential_paging` (warm, real_2692, 2692 books): 14.017 ms vs 14.797 ms (5.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
