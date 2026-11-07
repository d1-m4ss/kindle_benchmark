# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 97; PASS=93; FAILED=0; UNSUPPORTED=4; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R0_stock | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.331 | 24.277 | 10.572 | 25.602 | 15.101 | 24.407 | 10.951 | 26.854 |
| R1_bookshelf | warm | real_2692 | 2692 | 10 | 51.000 | 1/1 | 30/30 | 15.183 | 23.375 | 11.371 | 26.351 | 14.893 | 24.516 | 9.769 | 27.590 |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R1_bookshelf | warm | real_2692 | 2692 | on | 84 | 33.000 | 1/1 | 0/30 | — | — | — | — | 100.891 | 126.081 | 92.741 | 174.166 |
| R1_bookshelf | warm | real_2692 | 2692 | off | 84 | 33.000 | 1/1 | 0/30 | — | — | — | — | 37.969 | 62.659 | 30.705 | 109.720 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R0_stock | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging | UNSUPPORTED | — |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_sequential_paging_anim_off | UNSUPPORTED | — |
| R1_bookshelf | warm | real_2692 | 2692 | start_to_home | UNSUPPORTED | — |

## Comparative Findings

- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 14.893 ms vs 15.101 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.183 ms vs 15.331 ms (1.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R0_stock | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 33.750 | 33.750 | 33.750 | 33.750–33.750 |
| R0_stock | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 33.493 | 33.493 | 33.493 | 33.493–33.493 |
| R0_stock | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 26.071 | 26.007 | 26.910 | 25.991–27.120 |
| R0_stock | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 25.057 | 24.855 | 25.394 | 24.804–25.478 |
| R0_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 53.167 | 41.647 | 78.002 | 39.390–82.753 |
| R0_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 27.847 | 25.531 | 34.603 | 23.157–40.542 |
| R0_stock | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.670 | 16.626 | 16.701 | 16.616–16.723 |
| R0_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 25.334 | 24.374 | 35.773 | 23.455–36.069 |
| R0_stock | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 15.101 | 11.920 | 24.407 | 10.951–26.854 |
| R0_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 24.910 | 23.231 | 30.512 | 23.127–33.771 |
| R0_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 33.422 | 29.801 | 45.440 | 28.999–45.720 |
| R0_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 21.431 | 15.783 | 34.621 | 12.268–35.199 |
| R0_stock | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.331 | 12.586 | 24.277 | 10.572–25.602 |
| R0_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 49.796 | 45.813 | 61.253 | 44.884–83.522 |
| R0_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 92.254 | 48.617 | 114.943 | 47.483–162.547 |
| R0_stock | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.669 | 16.633 | 16.688 | 16.562–16.708 |
| R0_stock | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 561.012 | 561.012 | 561.012 | 561.012–561.012 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 34.169 | 34.169 | 34.169 | 34.169–34.169 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 33.865 | 33.865 | 33.865 | 33.865–33.865 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 25.629 | 25.477 | 25.719 | 25.439–25.742 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 25.938 | 25.433 | 26.729 | 25.307–26.927 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging | PASS | 30 | 100.891 | 97.869 | 126.081 | 92.741–174.166 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_cached_paging_anim_off | PASS | 30 | 37.969 | 34.038 | 62.659 | 30.705–109.720 |
| R1_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 20.606 | 19.475 | 65.052 | 18.352–79.296 |
| R1_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 53.209 | 44.585 | 77.938 | 40.660–85.924 |
| R1_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 31.934 | 22.944 | 96.753 | 22.462–98.245 |
| R1_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 6.763 | 5.876 | 8.065 | 5.299–11.907 |
| R1_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 16.658 | 16.640 | 16.672 | 16.638–16.695 |
| R1_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 25.597 | 24.968 | 35.860 | 24.246–35.966 |
| R1_bookshelf | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 14.893 | 11.960 | 24.516 | 9.769–27.590 |
| R1_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 27.469 | 26.424 | 34.606 | 26.243–36.021 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 33.332 | 31.503 | 45.941 | 30.907–46.728 |
| R1_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 21.463 | 16.298 | 34.889 | 13.266–37.483 |
| R1_bookshelf | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 15.183 | 13.771 | 23.375 | 11.371–26.351 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 77.535 | 59.442 | 100.533 | 57.303–111.668 |
| R1_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 101.026 | 62.535 | 128.921 | 55.025–174.429 |
| R1_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 28.001 | 26.505 | 31.868 | 24.704–53.879 |
| R1_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 16.688 | 16.611 | 16.726 | 16.590–16.773 |
| R1_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 703.725 | 703.725 | 703.725 | 703.725–703.725 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 35.050 | 35.050 | 35.050 | 35.050–35.050 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 32.780 | 32.780 | 32.780 | 32.780–32.780 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 24.491 | 22.389 | 30.539 | 21.863–32.051 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 22.246 | 19.888 | 24.340 | 19.298–24.863 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 224.577 | 224.577 | 224.577 | 224.577–224.577 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 298.478 | 298.478 | 298.478 | 298.478–298.478 |
| R0_stock | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 306.222 | 306.222 | 306.222 | 306.222–306.222 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 360.912 | 360.912 | 360.912 | 360.912–360.912 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 193.028 | 189.735 | 205.953 | 188.911–209.185 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 249.475 | 246.531 | 261.377 | 245.794–264.352 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 255.440 | 252.269 | 267.048 | 251.476–269.950 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 264.334 | 261.155 | 275.896 | 260.361–278.786 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 200.076 | 200.076 | 200.076 | 200.076–200.076 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1200.771 | 1200.771 | 1200.771 | 1200.771–1200.771 |
| R0_stock | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 9593.334 | 9593.334 | 9593.334 | 9593.334–9593.334 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 9621.118 | 9621.118 | 9621.118 | 9621.118–9621.118 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 240.023 | 240.023 | 240.023 | 240.023–240.023 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 315.858 | 315.858 | 315.858 | 315.858–315.858 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 324.396 | 324.396 | 324.396 | 324.396–324.396 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 378.500 | 378.500 | 378.500 | 378.500–378.500 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 198.012 | 195.696 | 211.330 | 195.117–214.659 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 254.636 | 251.366 | 268.962 | 250.549–272.543 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 260.705 | 257.415 | 275.683 | 256.592–279.427 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 269.534 | 266.486 | 284.461 | 265.723–288.192 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 196.631 | 196.631 | 196.631 | 196.631–196.631 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1224.243 | 1224.243 | 1224.243 | 1224.243–1224.243 |
| R1_bookshelf | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 18137.049 | 18137.049 | 18137.049 | 18137.049–18137.049 |
| R1_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 18177.860 | 18177.860 | 18177.860 | 18177.860–18177.860 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 431.636 | 431.636 | 431.636 | 431.636–431.636 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 510.114 | 510.114 | 510.114 | 510.114–510.114 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 526.020 | 526.020 | 526.020 | 526.020–526.020 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 549.292 | 549.292 | 549.292 | 549.292–549.292 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 376.376 | 364.922 | 391.061 | 362.058–394.732 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 431.794 | 424.538 | 456.539 | 422.724–462.725 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 440.891 | 434.103 | 467.440 | 432.405–474.078 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 452.696 | 446.019 | 1737.192 | 444.350–2058.317 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R0_stock | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9077.909 | 9077.909 | 9077.909–9077.909 | 11563.740 | 87072.000 |
| R0_stock | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10409.722 | 10409.722 | 10409.722–10409.722 | 15038.713 | 90032.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9357.917 | 9392.051 | 9047.698–9400.585 | 11031.436 | 85296.000 |
| R0_stock | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9296.253 | 9325.497 | 9136.229–9332.808 | 15394.904 | 86976.000 |
| R0_stock | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9307.659 | 9307.659 | 9307.659–9307.659 | 16230.235 | 84784.000 |
| R0_stock | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9403.483 | 9403.483 | 9403.483–9403.483 | 11772.845 | 97600.000 |
| R0_stock | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 14480.253 | 14480.253 | 14480.253–14480.253 | 17005.643 | 232544.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9891.085 | 9891.085 | 9891.085–9891.085 | 14589.194 | 85472.000 |
| R1_bookshelf | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 11208.073 | 11208.073 | 11208.073–11208.073 | 15989.941 | 88992.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 9736.273 | 9836.289 | 9718.656–9861.293 | 11575.896 | 84240.000 |
| R1_bookshelf | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 9788.766 | 9825.737 | 9758.207–9834.980 | 15684.242 | 85440.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 9730.707 | 9730.707 | 9730.707–9730.707 | 10556.646 | 84832.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 9821.410 | 9821.410 | 9821.410–9821.410 | 9833.316 | 99392.000 |
| R1_bookshelf | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 25188.846 | 25188.846 | 25188.846–25188.846 | 25235.420 | 349536.000 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 19116.827 | 19116.827 | 19116.827–19116.827 | 23260.466 | 117936.000 |
| R1_bookshelf_start | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 20244.753 | 20244.753 | 20244.753–20244.753 | 24342.262 | 120304.000 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 19244.801 | 19519.038 | 19065.641–19587.598 | 34090.465 | 114240.000 |
| R1_bookshelf_start | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 19056.168 | 19335.690 | 19036.926–19405.570 | 24142.426 | 114240.000 |

## Data-derived comparisons

- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_cached_paging` (warm, real_2692, 2692 books): 14.893 ms vs 15.101 ms (1.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `R1_bookshelf` has a lower descriptive median than `R0_stock` for `library_sequential_paging` (warm, real_2692, 2692 books): 15.183 ms vs 15.331 ms (1.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
