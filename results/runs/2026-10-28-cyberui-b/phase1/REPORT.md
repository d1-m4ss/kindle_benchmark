# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 108; PASS=91; FAILED=0; UNSUPPORTED=17; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| O_cyberui | warm | flat | 2000 | 8 | 250.000 | 1/1 | 30/30 | 16.160 | 16.214 | 12.398 | 16.233 | 16.130 | 16.194 | 14.690 | 17.453 |
| O_cyberui | warm | flat | 50 | 8 | 7.000 | 1/1 | 6/30 | 16.129 | 16.281 | 16.109 | 16.391 | 16.088 | 16.126 | 15.974 | 16.632 |
| O_cyberui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| O_cyberui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| O_cyberui | warm | flat | 2000 | close_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | flat | 2000 | open_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | flat | 50 | change_sort_mode | UNSUPPORTED | — |
| O_cyberui | warm | flat | 50 | close_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | flat | 50 | open_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 2000 | change_sort_mode | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 2000 | close_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 2000 | library_cached_paging | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 2000 | library_sequential_paging | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 2000 | open_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 2000 | repeated_nav | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 50 | change_sort_mode | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 50 | close_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 50 | library_cached_paging | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 50 | library_sequential_paging | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 50 | open_quick_settings | UNSUPPORTED | — |
| O_cyberui | warm | hierarchical | 50 | repeated_nav | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| O_cyberui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 16.692 | 16.674 | 16.698 | 16.669–16.699 |
| O_cyberui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.093 | 16.091 | 16.107 | 16.091–16.110 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 16.592 | 10.010 | 16.649 | 8.364–16.663 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.089 | 15.785 | 16.137 | 15.709–16.149 |
| O_cyberui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 16.131 | 9.039 | 17.867 | 8.299–33.200 |
| O_cyberui | warm | flat | 2000 | close_book | PASS | 10 | 46.919 | 44.916 | 50.375 | 43.804–50.852 |
| O_cyberui | warm | flat | 2000 | home_to_library | PASS | 10 | 16.663 | 16.640 | 16.686 | 16.602–16.691 |
| O_cyberui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 16.130 | 15.885 | 16.194 | 14.690–17.453 |
| O_cyberui | warm | flat | 2000 | library_first_render | PASS | 10 | 16.123 | 15.898 | 19.445 | 14.293–32.797 |
| O_cyberui | warm | flat | 2000 | library_folder_back | PASS | 10 | 16.672 | 16.655 | 16.824 | 16.652–17.915 |
| O_cyberui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 16.666 | 16.544 | 16.687 | 15.888–16.688 |
| O_cyberui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.160 | 16.115 | 16.214 | 12.398–16.233 |
| O_cyberui | warm | flat | 2000 | open_book | PASS | 10 | 54.408 | 38.304 | 56.556 | 37.390–58.847 |
| O_cyberui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 45.753 | 41.140 | 55.397 | 40.968–67.112 |
| O_cyberui | warm | flat | 2000 | repeated_nav | PASS | 2 | 166.681 | 166.680 | 166.683 | 166.680–166.683 |
| O_cyberui | warm | flat | 2000 | start_to_home | PASS | 10 | 16.651 | 16.626 | 16.663 | 16.605–16.669 |
| O_cyberui | warm | flat | 50 | close_book | PASS | 10 | 22.968 | 22.608 | 29.645 | 22.550–31.954 |
| O_cyberui | warm | flat | 50 | home_to_library | PASS | 10 | 16.675 | 16.654 | 16.709 | 16.647–16.719 |
| O_cyberui | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.088 | 16.033 | 16.126 | 15.974–16.632 |
| O_cyberui | warm | flat | 50 | library_first_render | PASS | 10 | 16.054 | 16.033 | 17.771 | 16.023–32.762 |
| O_cyberui | warm | flat | 50 | library_folder_back | PASS | 10 | 16.660 | 16.616 | 16.677 | 16.616–16.682 |
| O_cyberui | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.663 | 16.643 | 16.675 | 16.564–16.689 |
| O_cyberui | warm | flat | 50 | library_sequential_paging | PASS | 6 | 16.129 | 16.111 | 16.281 | 16.109–16.391 |
| O_cyberui | warm | flat | 50 | open_book | PASS | 10 | 42.510 | 27.990 | 46.805 | 26.146–52.501 |
| O_cyberui | warm | flat | 50 | open_book_minimal | PASS | 10 | 42.573 | 31.786 | 44.219 | 25.138–44.972 |
| O_cyberui | warm | flat | 50 | repeated_nav | PASS | 2 | 166.702 | 166.651 | 166.754 | 166.638–166.767 |
| O_cyberui | warm | flat | 50 | start_to_home | PASS | 10 | 16.651 | 16.625 | 16.661 | 16.623–16.665 |
| O_cyberui | warm | hierarchical | 2000 | close_book | PASS | 10 | 33.656 | 22.720 | 43.525 | 19.512–48.489 |
| O_cyberui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.672 | 16.632 | 16.688 | 16.626–16.721 |
| O_cyberui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 15.989 | 15.944 | 16.007 | 15.896–16.012 |
| O_cyberui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.632 | 15.929 | 16.681 | 9.789–16.703 |
| O_cyberui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.672 | 16.645 | 17.721 | 16.641–26.587 |
| O_cyberui | warm | hierarchical | 2000 | open_book | PASS | 10 | 39.005 | 31.226 | 45.944 | 29.365–47.191 |
| O_cyberui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 39.877 | 35.338 | 46.593 | 34.216–46.882 |
| O_cyberui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.657 | 16.621 | 16.674 | 16.604–16.679 |
| O_cyberui | warm | hierarchical | 50 | close_book | PASS | 10 | 23.330 | 22.186 | 25.038 | 21.808–28.612 |
| O_cyberui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.673 | 16.654 | 16.687 | 16.652–16.701 |
| O_cyberui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 15.932 | 15.871 | 15.998 | 15.851–16.012 |
| O_cyberui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.662 | 16.640 | 16.675 | 16.634–16.693 |
| O_cyberui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.666 | 16.641 | 16.687 | 16.630–16.708 |
| O_cyberui | warm | hierarchical | 50 | open_book | PASS | 10 | 42.456 | 37.797 | 44.711 | 24.500–44.943 |
| O_cyberui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 42.921 | 42.492 | 43.905 | 41.493–43.998 |
| O_cyberui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.658 | 16.653 | 16.665 | 16.646–16.684 |
| O_cyberui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 16.627 | 16.627 | 16.627 | 16.627–16.627 |
| O_cyberui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.120 | 16.120 | 16.120 | 16.120–16.120 |
| O_cyberui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 228.589 | 225.710 | 244.718 | 224.990–248.751 |
| O_cyberui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 275.548 | 273.972 | 291.339 | 273.578–295.286 |
| O_cyberui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 279.663 | 278.520 | 295.626 | 278.235–299.616 |
| O_cyberui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 288.884 | 288.020 | 304.965 | 287.804–308.985 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 206.575 | 196.567 | 231.087 | 194.066–237.215 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 249.132 | 242.338 | 268.150 | 240.640–272.905 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 254.743 | 247.099 | 273.715 | 245.188–278.458 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 264.700 | 256.629 | 283.387 | 254.612–288.059 |
| O_cyberui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 274.244 | 274.244 | 274.244 | 274.244–274.244 |
| O_cyberui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1289.019 | 1289.019 | 1289.019 | 1289.019–1289.019 |
| O_cyberui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 7603.318 | 7603.318 | 7603.318 | 7603.318–7603.318 |
| O_cyberui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 7618.380 | 7618.380 | 7618.380 | 7618.380–7618.380 |
| O_cyberui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 221.912 | 221.912 | 221.912 | 221.912–221.912 |
| O_cyberui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1238.965 | 1238.965 | 1238.965 | 1238.965–1238.965 |
| O_cyberui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 5693.080 | 5693.080 | 5693.080 | 5693.080–5693.080 |
| O_cyberui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 5706.368 | 5706.368 | 5706.368 | 5706.368–5706.368 |
| O_cyberui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 222.726 | 222.726 | 222.726 | 222.726–222.726 |
| O_cyberui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1222.964 | 1222.964 | 1222.964 | 1222.964–1222.964 |
| O_cyberui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 4683.862 | 4683.862 | 4683.862 | 4683.862–4683.862 |
| O_cyberui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 4704.559 | 4704.559 | 4704.559 | 4704.559–4704.559 |
| O_cyberui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 231.780 | 231.780 | 231.780 | 231.780–231.780 |
| O_cyberui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1228.345 | 1228.345 | 1228.345 | 1228.345–1228.345 |
| O_cyberui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4519.899 | 4519.899 | 4519.899 | 4519.899–4519.899 |
| O_cyberui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4535.720 | 4535.720 | 4535.720 | 4535.720–4535.720 |
| O_cyberui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 244.087 | 244.087 | 244.087 | 244.087–244.087 |
| O_cyberui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 292.728 | 292.728 | 292.728 | 292.728–292.728 |
| O_cyberui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 297.199 | 297.199 | 297.199 | 297.199–297.199 |
| O_cyberui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 306.790 | 306.790 | 306.790 | 306.790–306.790 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| O_cyberui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9622.915 | 9713.871 | 9559.454–9736.610 | 11482.393 | 85376.000 |
| O_cyberui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9680.807 | 9722.207 | 9662.096–9732.557 | 10393.843 | 85376.000 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 9534.470 | 9580.163 | 9472.063–9591.587 | 15126.450 | 81584.000 |
| O_cyberui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 9604.201 | 9621.414 | 9602.947–9625.717 | 10356.662 | 81664.000 |
| O_cyberui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 11574.310 | 11574.310 | 11574.310–11574.310 | 19825.450 | 89888.000 |
| O_cyberui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 12001.193 | 12001.193 | 12001.193–12001.193 | 19868.684 | 103824.000 |
| O_cyberui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 16911.717 | 16911.717 | 16911.717–16911.717 | 37408.415 | 130960.000 |
| O_cyberui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 9258.310 | 9258.310 | 9258.310–9258.310 | 10870.319 | 84416.000 |
| O_cyberui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 9348.041 | 9348.041 | 9348.041–9348.041 | 18198.354 | 93152.000 |
| O_cyberui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 11722.057 | 11722.057 | 11722.057–11722.057 | 17017.472 | 134400.000 |
| O_cyberui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9580.091 | 9580.091 | 9580.091–9580.091 | 11733.249 | 85040.000 |
| O_cyberui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9728.451 | 9728.451 | 9728.451–9728.451 | 20673.051 | 91104.000 |
| O_cyberui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 11797.580 | 11797.580 | 11797.580–11797.580 | 12436.635 | 126736.000 |
| O_cyberui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 9001.489 | 9001.489 | 9001.489–9001.489 | 9721.663 | 85456.000 |
| O_cyberui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 9099.381 | 9099.381 | 9099.381–9099.381 | 19866.586 | 90160.000 |
| O_cyberui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 11484.229 | 11484.229 | 11484.229–11484.229 | 11736.192 | 119168.000 |
| O_cyberui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 9564.353 | 9564.353 | 9564.353–9564.353 | 11279.397 | 86720.000 |
| O_cyberui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 9636.119 | 9636.119 | 9636.119–9636.119 | 10379.932 | 86720.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
