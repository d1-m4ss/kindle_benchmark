# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase2`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 37; PASS=35; FAILED=0; UNSUPPORTED=2; DEPRECATED=0.

`Real 2692` names the complete corpus. Paging traverses its root with **505 visible entries (500 books + 5 folders)**; the remaining EPUBs are inside those folders. `Books/page` always reports the visible page size, not `2692 / page size`.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| R14_cyberui | warm | real_2692 | 2692 | 8 | 64.000 | 1/1 | 30/30 | 16.123 | 16.178 | 10.710 | 19.728 | 16.089 | 16.159 | 9.229 | 32.278 |

## Unsupported Configurations

| Stack | Mode | Dataset | Books | Scenario | Status | Reason |
|:--|:--|:--|--:|:--|:--|:--|
| R14_cyberui | warm | real_2692 | 2692 | close_quick_settings | UNSUPPORTED | — |
| R14_cyberui | warm | real_2692 | 2692 | open_quick_settings | UNSUPPORTED | — |

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| R14_cyberui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 20.697 | 20.697 | 20.697 | 20.697–20.697 |
| R14_cyberui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 13.769 | 13.769 | 13.769 | 13.769–13.769 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 30.752 | 28.720 | 31.561 | 28.212–31.763 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 8.227 | 7.646 | 9.778 | 7.501–10.166 |
| R14_cyberui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 16.098 | 7.630 | 18.023 | 7.540–34.619 |
| R14_cyberui | warm | real_2692 | 2692 | close_book | PASS | 10 | 32.102 | 30.643 | 43.038 | 29.931–48.606 |
| R14_cyberui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 16.674 | 16.658 | 16.702 | 16.653–16.731 |
| R14_cyberui | warm | real_2692 | 2692 | library_cached_paging | PASS | 30 | 16.089 | 14.659 | 16.159 | 9.229–32.278 |
| R14_cyberui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 16.069 | 16.048 | 16.168 | 16.045–16.172 |
| R14_cyberui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 16.635 | 16.496 | 16.656 | 15.975–16.689 |
| R14_cyberui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 16.670 | 16.642 | 16.950 | 16.604–19.183 |
| R14_cyberui | warm | real_2692 | 2692 | library_sequential_paging | PASS | 30 | 16.123 | 16.012 | 16.178 | 10.710–19.728 |
| R14_cyberui | warm | real_2692 | 2692 | open_book | PASS | 10 | 57.319 | 48.682 | 67.820 | 44.428–77.551 |
| R14_cyberui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 93.461 | 51.106 | 113.544 | 50.188–166.167 |
| R14_cyberui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 503.776 | 503.776 | 503.776 | 503.776–503.776 |
| R14_cyberui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 16.634 | 16.609 | 16.663 | 16.595–16.707 |
| R14_cyberui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 276.431 | 276.431 | 276.431 | 276.431–276.431 |
| R14_cyberui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 327.286 | 327.286 | 327.286 | 327.286–327.286 |
| R14_cyberui | real_first_run | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 333.875 | 333.875 | 333.875 | 333.875–333.875 |
| R14_cyberui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 453.457 | 453.457 | 453.457 | 453.457–453.457 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 231.856 | 228.132 | 259.476 | 227.201–266.382 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 278.928 | 277.495 | 314.682 | 277.137–323.621 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | process:complete_marker_ms | PASS | 3 | 284.950 | 283.443 | 321.600 | 283.066–330.762 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 294.172 | 292.913 | 332.267 | 292.598–341.791 |
| R14_cyberui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 230.475 | 230.475 | 230.475 | 230.475–230.475 |
| R14_cyberui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1240.924 | 1240.924 | 1240.924 | 1240.924–1240.924 |
| R14_cyberui | warm | real_2692 | 2692 | process:complete_marker_ms | PASS | 1 | 7768.342 | 7768.342 | 7768.342 | 7768.342–7768.342 |
| R14_cyberui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 7786.305 | 7786.305 | 7786.305 | 7786.305–7786.305 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| R14_cyberui | real_first_run | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10260.345 | 10260.345 | 10260.345–10260.345 | 15182.516 | 85760.000 |
| R14_cyberui | real_first_run | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10455.186 | 10455.186 | 10455.186–10455.186 | 12045.157 | 85760.000 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | post_init_idle | PASS | 3 | 3 | 10285.505 | 10305.952 | 10273.075–10311.063 | 13174.035 | 83312.000 |
| R14_cyberui | real_steady_cold | real_2692 | 2692 | post_library_render_idle | PASS | 3 | 3 | 10475.580 | 10527.058 | 10474.752–10539.928 | 14031.271 | 86512.000 |
| R14_cyberui | warm | real_2692 | 2692 | post_init_idle | PASS | 1 | 1 | 10349.220 | 10349.220 | 10349.220–10349.220 | 11395.043 | 83120.000 |
| R14_cyberui | warm | real_2692 | 2692 | post_library_render_idle | PASS | 1 | 1 | 10608.416 | 10608.416 | 10608.416–10608.416 | 20567.900 | 95104.000 |
| R14_cyberui | warm | real_2692 | 2692 | post_stress_idle | PASS | 1 | 1 | 13587.901 | 13587.901 | 13587.901–13587.901 | 25054.680 | 238224.000 |

## Data-derived comparisons

No complete paired comparisons are available yet.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
