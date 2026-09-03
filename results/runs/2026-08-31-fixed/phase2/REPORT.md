# KOReader UI Benchmark Report

> **DEPRECATED_INVALID_FOR_RANKING (paging scenarios only):** this campaign was generated on 2026-08-31, before the paging-instrumentation and hierarchical-dataset fixes and before the KOReader/Bookshelf/Project:Title baseline bump recorded in `versions.lock.json` (see README "Baseline change"). Its `library_next_page` / paging / cached-paging rows use a scenario name now rejected by the audit as deprecated and must not be used to rank stacks. Startup, open-book, memory, and Bookends rows are unaffected and remain valid.

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `all`

Aggregated rows: 467; PASS=437; FAILED=0; UNSUPPORTED=30.

## Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|:--|
| A_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 10.705 | 16.884 | 8.999–17.901 |
| A_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 17.833 | 20.315 | 12.920–31.382 |
| A_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 11.485 | 13.553 | 8.963–20.651 |
| A_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 10.870 | 17.020 | 10.118–17.794 |
| A_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 12.706 | 14.759 | 9.629–20.646 |
| A_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 10.918 | 12.357 | 8.719–19.033 |
| A_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 50.814 | 80.608 | 33.957–85.618 |
| A_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 101.700 | 133.864 | 53.946–236.514 |
| A_stock | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 8.578 | 9.376 | 4.050–9.510 |
| K_stock_bookends | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 10.856 | 16.821 | 9.762–24.162 |
| K_stock_bookends | warm | real_2692 | 2692 | close_book | PASS | 10 | 20.584 | 55.775 | 13.280–60.585 |
| K_stock_bookends | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 11.211 | 12.912 | 9.819–20.186 |
| K_stock_bookends | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 11.369 | 17.234 | 9.607–17.507 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 13.436 | 20.425 | 11.309–21.186 |
| K_stock_bookends | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 10.859 | 11.459 | 7.900–11.733 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book | PASS | 10 | 71.033 | 86.904 | 49.262–107.788 |
| K_stock_bookends | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 104.986 | 150.206 | 46.457–237.752 |
| K_stock_bookends | warm | real_2692 | 2692 | reader_page_turn | PASS | 10 | 8.229 | 8.655 | 7.532–8.715 |
| R0_stock | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 11.734 | 11.734 | 11.734–11.734 |
| R0_stock | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 11.120 | 11.120 | 11.120–11.120 |
| R0_stock | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 11.601 | 11.956 | 11.494–12.045 |
| R0_stock | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 10.501 | 11.178 | 9.349–11.347 |
| R0_stock | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 9.861 | 19.484 | 9.029–19.504 |
| R0_stock | warm | real_2692 | 2692 | close_book | PASS | 10 | 19.522 | 23.572 | 15.519–25.593 |
| R0_stock | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.357 | 8.844 | 7.709–9.208 |
| R0_stock | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 10.772 | 13.024 | 9.345–22.116 |
| R0_stock | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 10.736 | 18.888 | 9.181–19.617 |
| R0_stock | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 13.880 | 22.026 | 11.338–22.639 |
| R0_stock | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.418 | 20.443 | 10.273–20.754 |
| R0_stock | warm | real_2692 | 2692 | open_book | PASS | 10 | 59.898 | 83.930 | 48.727–87.990 |
| R0_stock | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 110.701 | 144.738 | 50.194–246.109 |
| R0_stock | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.415 | 20.545 | 7.962–22.407 |
| R0_stock | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 458.711 | 458.711 | 458.711–458.711 |
| R10_project_title_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 20.958 | 20.958 | 20.958–20.958 |
| R10_project_title_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 17.683 | 17.683 | 17.683–17.683 |
| R10_project_title_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 18.730 | 19.992 | 17.769–20.307 |
| R10_project_title_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 18.680 | 18.762 | 18.600–18.783 |
| R10_project_title_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 8.840 | 9.417 | 8.253–10.090 |
| R10_project_title_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 21.846 | 28.265 | 18.762–30.687 |
| R10_project_title_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.479 | 10.545 | 8.265–10.977 |
| R10_project_title_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 18.808 | 20.325 | 17.957–21.424 |
| R10_project_title_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 18.361 | 20.710 | 16.074–21.430 |
| R10_project_title_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 8.521 | 9.037 | 7.714–9.912 |
| R10_project_title_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 8.375 | 8.781 | 7.862–8.810 |
| R10_project_title_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 48.245 | 75.869 | 36.534–81.596 |
| R10_project_title_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 91.334 | 130.722 | 42.261–224.844 |
| R10_project_title_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.357 | 8.822 | 7.479–9.380 |
| R10_project_title_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 378.842 | 378.842 | 378.842–378.842 |
| R1_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 22.229 | 22.229 | 22.229–22.229 |
| R1_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 21.414 | 21.414 | 21.414–21.414 |
| R1_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 20.830 | 21.218 | 20.106–21.315 |
| R1_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 20.274 | 20.521 | 19.298–20.583 |
| R1_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 8.452 | 10.184 | 4.248–20.130 |
| R1_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 26.885 | 30.873 | 24.109–32.119 |
| R1_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.619 | 9.064 | 7.182–9.364 |
| R1_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 19.430 | 21.180 | 17.390–25.158 |
| R1_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 19.244 | 21.477 | 17.668–23.090 |
| R1_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 12.986 | 18.167 | 9.606–19.341 |
| R1_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.383 | 20.466 | 8.265–20.616 |
| R1_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 62.889 | 84.792 | 30.354–102.367 |
| R1_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 108.419 | 140.054 | 48.302–250.315 |
| R1_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.325 | 8.606 | 3.088–8.881 |
| R1_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 513.457 | 513.457 | 513.457–513.457 |
| R2_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 12.858 | 12.858 | 12.858–12.858 |
| R2_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 11.657 | 11.657 | 11.657–11.657 |
| R2_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 11.194 | 11.724 | 9.346–11.857 |
| R2_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 10.435 | 10.784 | 9.867–10.871 |
| R2_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 3.866 | 13.167 | 3.274–20.654 |
| R2_bookshelf | warm | real_2692 | 2692 | bookshelf_page_turn | PASS | 10 | 0.074 | 0.210 | 0.028–0.239 |
| R2_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 10.632 | 19.504 | 8.898–19.734 |
| R2_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 19.551 | 23.382 | 15.499–26.125 |
| R2_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 8.857 | 9.323 | 8.021–9.486 |
| R2_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.182 | 8.961 | 7.777–9.117 |
| R2_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 11.383 | 13.447 | 10.232–24.651 |
| R2_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 9.916 | 17.805 | 9.228–18.107 |
| R2_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 13.877 | 22.362 | 12.311–23.101 |
| R2_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.610 | 20.371 | 10.220–21.161 |
| R2_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 54.267 | 84.394 | 41.216–94.275 |
| R2_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 112.413 | 145.101 | 50.790–249.432 |
| R2_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 9.140 | 13.681 | 7.840–13.704 |
| R2_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.149 | 9.141 | 7.354–13.547 |
| R2_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 570.139 | 570.139 | 570.139–570.139 |
| R3_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 23.245 | 23.245 | 23.245–23.245 |
| R3_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 20.643 | 20.643 | 20.643–20.643 |
| R3_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 19.320 | 20.127 | 18.392–20.329 |
| R3_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 17.814 | 19.003 | 17.693–19.300 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 3.598 | 13.622 | 3.066–20.116 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_page_turn | PASS | 10 | 0.057 | 0.171 | 0.021–0.244 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 9.093 | 11.272 | 8.096–19.193 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 30.760 | 34.942 | 23.286–38.023 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 8.938 | 9.373 | 7.953–9.401 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.604 | 8.759 | 7.776–8.911 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 20.022 | 23.069 | 18.399–24.848 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 19.875 | 28.610 | 19.188–31.662 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 13.669 | 23.012 | 12.071–23.178 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.249 | 12.713 | 8.572–20.545 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 71.606 | 80.586 | 38.218–98.741 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 112.186 | 139.941 | 54.972–246.560 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 9.004 | 11.375 | 8.192–12.890 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.411 | 8.875 | 7.825–9.050 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 535.740 | 535.740 | 535.740–535.740 |
| R4_simpleui | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 0.087 | 0.087 | 0.087–0.087 |
| R4_simpleui | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 17.605 | 17.605 | 17.605–17.605 |
| R4_simpleui | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 0.061 | 0.091 | 0.046–0.099 |
| R4_simpleui | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 17.844 | 18.397 | 15.392–18.535 |
| R4_simpleui | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 8.369 | 12.465 | 6.792–40.478 |
| R4_simpleui | warm | real_2692 | 2692 | close_book | PASS | 10 | 37.718 | 1822.849 | 24.947–17155.345 |
| R4_simpleui | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.241 | 8.386 | 7.811–8.653 |
| R4_simpleui | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 0.067 | 0.096 | 0.014–0.107 |
| R4_simpleui | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 24.069 | 32.085 | 22.442–42.680 |
| R4_simpleui | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 17.915 | 40.042 | 7.563–47.759 |
| R4_simpleui | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.933 | 16.429 | 10.933–37.894 |
| R4_simpleui | warm | real_2692 | 2692 | open_book | PASS | 10 | 150.739 | 167.367 | 79.194–170.303 |
| R4_simpleui | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 154.871 | 204.466 | 96.264–300.731 |
| R4_simpleui | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.230 | 9.021 | 7.523–9.134 |
| R4_simpleui | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 784.846 | 784.846 | 784.846–784.846 |
| R4_simpleui | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 0.060 | 0.109 | 0.016–0.109 |
| R5_simpleui_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 0.026 | 0.026 | 0.026–0.026 |
| R5_simpleui_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 17.282 | 17.282 | 17.282–17.282 |
| R5_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 0.039 | 0.077 | 0.027–0.086 |
| R5_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 18.262 | 19.086 | 17.171–19.292 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 6.730 | 44.228 | 6.284–48.072 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | bookshelf_page_turn | PASS | 10 | 0.197 | 0.262 | 0.104–0.445 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 12.742 | 39.808 | 11.108–41.309 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 52.863 | 1695.500 | 39.486–13087.060 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 23.777 | 66.058 | 21.036–68.720 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.759 | 9.063 | 8.121–9.511 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 0.018 | 0.043 | 0.014–0.055 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 25.025 | 27.984 | 22.097–39.483 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 18.636 | 46.434 | 11.379–48.020 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.774 | 16.153 | 10.476–41.596 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 150.886 | 180.661 | 86.182–194.821 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 164.630 | 203.216 | 95.811–305.362 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 14.518 | 16.814 | 12.829–18.676 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.496 | 9.104 | 7.638–9.155 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 733.971 | 733.971 | 733.971–733.971 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 0.052 | 0.092 | 0.012–0.103 |
| R6_simpleui_vos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 0.069 | 0.069 | 0.069–0.069 |
| R6_simpleui_vos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 15.633 | 15.633 | 15.633–15.633 |
| R6_simpleui_vos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 0.062 | 0.117 | 0.030–0.131 |
| R6_simpleui_vos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 13.945 | 14.815 | 12.536–15.033 |
| R6_simpleui_vos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 8.835 | 26.604 | 5.712–27.860 |
| R6_simpleui_vos | warm | real_2692 | 2692 | close_book | PASS | 10 | 40.790 | 94.188 | 33.503–111.081 |
| R6_simpleui_vos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 9.206 | 1583.110 | 7.296–13630.291 |
| R6_simpleui_vos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 0.018 | 0.037 | 0.006–0.044 |
| R6_simpleui_vos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 22.059 | 24.472 | 21.143–25.628 |
| R6_simpleui_vos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 11.036 | 28.207 | 7.782–28.650 |
| R6_simpleui_vos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.273 | 28.659 | 10.569–32.332 |
| R6_simpleui_vos | warm | real_2692 | 2692 | open_book | PASS | 10 | 129.128 | 178.219 | 65.302–180.092 |
| R6_simpleui_vos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 135.519 | 184.137 | 69.369–283.810 |
| R6_simpleui_vos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.391 | 8.610 | 7.602–9.129 |
| R6_simpleui_vos | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 660.269 | 660.269 | 660.269–660.269 |
| R6_simpleui_vos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 0.025 | 0.054 | 0.013–0.159 |
| R7_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 0.023 | 0.023 | 0.023–0.023 |
| R7_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 17.789 | 17.789 | 17.789–17.789 |
| R7_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 0.069 | 0.099 | 0.047–0.106 |
| R7_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 14.025 | 14.932 | 12.724–15.159 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 5.439 | 42.245 | 4.886–43.798 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | bookshelf_page_turn | PASS | 10 | 0.183 | 0.229 | 0.050–0.234 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 8.819 | 23.760 | 7.375–26.742 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 39.544 | 102.112 | 29.919–122.117 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 27.604 | 71.652 | 25.705–72.724 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 11.761 | 14.864 | 9.060–16.237 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 0.040 | 0.104 | 0.018–0.152 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 22.502 | 27.266 | 20.220–27.456 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 10.082 | 24.571 | 8.601–32.000 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 11.244 | 30.733 | 9.013–32.039 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 131.957 | 164.029 | 93.184–170.181 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 145.181 | 173.478 | 91.843–289.151 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 13.335 | 38.344 | 11.085–256.031 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.591 | 8.946 | 8.029–8.975 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 718.056 | 718.056 | 718.056–718.056 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 0.056 | 0.069 | 0.023–0.082 |
| R8_zenos | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 44.899 | 44.899 | 44.899–44.899 |
| R8_zenos | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 19.640 | 19.640 | 19.640–19.640 |
| R8_zenos | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 57.759 | 58.027 | 54.327–58.094 |
| R8_zenos | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 27.018 | 27.640 | 24.068–27.795 |
| R8_zenos | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 16.433 | 26.555 | 13.605–27.207 |
| R8_zenos | warm | real_2692 | 2692 | close_book | PASS | 10 | 32.475 | 39.082 | 25.850–45.111 |
| R8_zenos | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.433 | 8.982 | 7.697–9.038 |
| R8_zenos | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 34.412 | 37.438 | 31.169–39.694 |
| R8_zenos | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 26.834 | 31.394 | 23.771–31.767 |
| R8_zenos | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 14.611 | 27.942 | 12.978–28.155 |
| R8_zenos | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 9.303 | 23.520 | 8.616–27.740 |
| R8_zenos | warm | real_2692 | 2692 | library_next_page | PASS | 10 | 12.819 | 16.148 | 9.578–25.789 |
| R8_zenos | warm | real_2692 | 2692 | library_prev_page | PASS | 10 | 12.472 | 29.564 | 11.052–30.685 |
| R8_zenos | warm | real_2692 | 2692 | open_book | PASS | 10 | 71.659 | 131.096 | 63.712–132.828 |
| R8_zenos | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 130.685 | 158.228 | 79.577–252.904 |
| R8_zenos | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.293 | 8.895 | 7.316–8.980 |
| R8_zenos | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 9.837 | 21.964 | 7.964–24.714 |
| R9_zenos_bookshelf | real_first_run | real_2692 | 2692 | home_to_library | PASS | 1 | 57.713 | 57.713 | 57.713–57.713 |
| R9_zenos_bookshelf | real_first_run | real_2692 | 2692 | library_first_render | PASS | 1 | 28.829 | 28.829 | 28.829–28.829 |
| R9_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | home_to_library | PASS | 3 | 53.559 | 57.005 | 52.763–57.867 |
| R9_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | library_first_render | PASS | 3 | 26.303 | 26.505 | 25.733–26.556 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_first_render | PASS | 10 | 3.989 | 30.059 | 3.049–38.277 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | bookshelf_page_turn | PASS | 10 | 0.064 | 0.113 | 0.026–0.214 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | change_sort_mode | PASS | 10 | 8.634 | 23.672 | 5.582–25.232 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | close_book | PASS | 10 | 35.579 | 43.356 | 27.663–79.699 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | close_bookshelf | PASS | 10 | 8.261 | 9.042 | 7.662–9.201 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | close_quick_settings | PASS | 10 | 8.560 | 10.361 | 7.739–13.174 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | home_to_library | PASS | 10 | 25.279 | 29.651 | 21.092–30.343 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | library_first_render | PASS | 10 | 17.243 | 25.128 | 16.054–41.040 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_back | PASS | 10 | 8.520 | 20.906 | 5.846–21.532 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | library_folder_enter | PASS | 10 | 8.675 | 21.089 | 4.464–21.680 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | library_next_page | PASS | 10 | 8.850 | 19.603 | 7.623–20.080 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | library_prev_page | PASS | 10 | 8.692 | 20.810 | 3.903–21.185 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | open_book | PASS | 10 | 72.925 | 111.294 | 62.284–127.541 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | open_book_minimal | PASS | 10 | 126.541 | 155.488 | 77.539–254.879 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | open_bookshelf | PASS | 10 | 9.249 | 10.385 | 7.714–11.003 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | open_quick_settings | PASS | 10 | 8.755 | 9.142 | 2.989–9.256 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | repeated_nav | PASS | 1 | 498.652 | 498.652 | 498.652–498.652 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | start_to_home | PASS | 10 | 9.009 | 11.855 | 8.485–28.728 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 513.453 | 513.453 | 513.453–513.453 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 950.336 | 950.336 | 950.336–950.336 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 7472.865 | 7472.865 | 7472.865–7472.865 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 540.414 | 540.414 | 540.414–540.414 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 981.648 | 981.648 | 981.648–981.648 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 8945.412 | 8945.412 | 8945.412–8945.412 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 774.630 | 774.630 | 774.630–774.630 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 803.023 | 803.023 | 803.023–803.023 |
| R0_stock | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 832.722 | 832.722 | 832.722–832.722 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 503.774 | 504.801 | 460.826–505.058 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 531.948 | 532.116 | 487.688–532.158 |
| R0_stock | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 559.988 | 561.377 | 514.617–561.725 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 470.076 | 470.076 | 470.076–470.076 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 904.154 | 904.154 | 904.154–904.154 |
| R0_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 6673.825 | 6673.825 | 6673.825–6673.825 |
| R10_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 471.818 | 471.818 | 471.818–471.818 |
| R10_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 515.397 | 515.397 | 515.397–515.397 |
| R10_project_title_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 539.778 | 539.778 | 539.778–539.778 |
| R10_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 416.867 | 434.295 | 415.203–438.652 |
| R10_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 460.853 | 476.142 | 456.619–479.964 |
| R10_project_title_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 484.279 | 501.243 | 483.517–505.484 |
| R10_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 392.894 | 392.894 | 392.894–392.894 |
| R10_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1077.220 | 1077.220 | 1077.220–1077.220 |
| R10_project_title_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 5854.966 | 5854.966 | 5854.966–5854.966 |
| R1_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 551.432 | 551.432 | 551.432–551.432 |
| R1_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 601.156 | 601.156 | 601.156–601.156 |
| R1_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 632.726 | 632.726 | 632.726–632.726 |
| R1_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 504.527 | 536.849 | 485.046–544.929 |
| R1_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 549.880 | 584.004 | 530.038–592.535 |
| R1_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 580.106 | 611.507 | 557.129–619.358 |
| R1_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 488.456 | 488.456 | 488.456–488.456 |
| R1_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1215.906 | 1215.906 | 1215.906–1215.906 |
| R1_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 7276.506 | 7276.506 | 7276.506–7276.506 |
| R2_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 531.560 | 531.560 | 531.560–531.560 |
| R2_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 560.523 | 560.523 | 560.523–560.523 |
| R2_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 591.018 | 591.018 | 591.018–591.018 |
| R2_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 489.797 | 501.160 | 484.858–504.001 |
| R2_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 515.380 | 527.652 | 512.779–530.720 |
| R2_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 542.882 | 554.951 | 542.690–557.968 |
| R2_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 481.781 | 481.781 | 481.781–481.781 |
| R2_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 907.329 | 907.329 | 907.329–907.329 |
| R2_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 7749.850 | 7749.850 | 7749.850–7749.850 |
| R3_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 569.467 | 569.467 | 569.467–569.467 |
| R3_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 618.217 | 618.217 | 618.217–618.217 |
| R3_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 648.665 | 648.665 | 648.665–648.665 |
| R3_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 511.426 | 547.925 | 492.428–557.050 |
| R3_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 556.195 | 588.703 | 536.565–596.830 |
| R3_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 582.945 | 614.965 | 563.503–622.971 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 482.200 | 482.200 | 482.200–482.200 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1244.856 | 1244.856 | 1244.856–1244.856 |
| R3_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 8120.674 | 8120.674 | 8120.674–8120.674 |
| R4_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 657.029 | 657.029 | 657.029–657.029 |
| R4_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 685.191 | 685.191 | 685.191–685.191 |
| R4_simpleui | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 722.000 | 722.000 | 722.000–722.000 |
| R4_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 590.635 | 597.932 | 586.360–599.756 |
| R4_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 617.023 | 623.257 | 615.007–624.815 |
| R4_simpleui | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 652.342 | 658.636 | 649.090–660.210 |
| R4_simpleui | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 582.758 | 582.758 | 582.758–582.758 |
| R4_simpleui | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 891.434 | 891.434 | 891.434–891.434 |
| R4_simpleui | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 49193.724 | 49193.724 | 49193.724–49193.724 |
| R5_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 869.904 | 869.904 | 869.904–869.904 |
| R5_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 897.303 | 897.303 | 897.303–897.303 |
| R5_simpleui_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 932.240 | 932.240 | 932.240–932.240 |
| R5_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 584.985 | 595.302 | 545.982–597.882 |
| R5_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 615.587 | 623.355 | 571.461–625.297 |
| R5_simpleui_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 646.455 | 659.973 | 608.937–663.352 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 561.365 | 561.365 | 561.365–561.365 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 863.704 | 863.704 | 863.704–863.704 |
| R5_simpleui_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 47759.544 | 47759.544 | 47759.544–47759.544 |
| R6_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 717.380 | 717.380 | 717.380–717.380 |
| R6_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 741.012 | 741.012 | 741.012–741.012 |
| R6_simpleui_vos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 773.708 | 773.708 | 773.708–773.708 |
| R6_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 483.179 | 538.356 | 482.810–552.151 |
| R6_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 504.721 | 560.423 | 503.357–574.348 |
| R6_simpleui_vos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 533.073 | 586.637 | 529.182–600.028 |
| R6_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 463.663 | 463.663 | 463.663–463.663 |
| R6_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 724.731 | 724.731 | 724.731–724.731 |
| R6_simpleui_vos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 29604.525 | 29604.525 | 29604.525–29604.525 |
| R7_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 554.888 | 554.888 | 554.888–554.888 |
| R7_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 579.707 | 579.707 | 579.707–579.707 |
| R7_simpleui_vos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 610.831 | 610.831 | 610.831–610.831 |
| R7_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 492.196 | 492.795 | 470.284–492.945 |
| R7_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 513.818 | 515.191 | 491.058–515.534 |
| R7_simpleui_vos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 540.230 | 542.460 | 517.667–543.017 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 471.355 | 471.355 | 471.355–471.355 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 743.918 | 743.918 | 743.918–743.918 |
| R7_simpleui_vos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 30976.667 | 30976.667 | 30976.667–30976.667 |
| R8_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 616.664 | 616.664 | 616.664–616.664 |
| R8_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 704.522 | 704.522 | 704.522–704.522 |
| R8_zenos | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 736.222 | 736.222 | 736.222–736.222 |
| R8_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 513.356 | 535.057 | 499.830–540.482 |
| R8_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 607.674 | 622.387 | 594.398–626.066 |
| R8_zenos | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 638.057 | 652.920 | 622.355–656.636 |
| R8_zenos | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 514.917 | 514.917 | 514.917–514.917 |
| R8_zenos | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1963.421 | 1963.421 | 1963.421–1963.421 |
| R8_zenos | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 9898.353 | 9898.353 | 9898.353–9898.353 |
| R9_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 574.441 | 574.441 | 574.441–574.441 |
| R9_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 680.508 | 680.508 | 680.508–680.508 |
| R9_zenos_bookshelf | real_first_run | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 714.680 | 714.680 | 714.680–714.680 |
| R9_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 3 | 496.916 | 532.934 | 496.811–541.939 |
| R9_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 3 | 586.068 | 624.629 | 584.851–634.269 |
| R9_zenos_bookshelf | real_steady_cold | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 3 | 618.952 | 657.089 | 613.617–666.623 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 506.762 | 506.762 | 506.762–506.762 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 1698.236 | 1698.236 | 1698.236–1698.236 |
| R9_zenos_bookshelf | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 10333.705 | 10333.705 | 10333.705–10333.705 |

## Data-derived comparisons

- `R0_stock` has the lower descriptive median than `R1_vos` for `library_first_render` (real_first_run, real_2692, 2692 books): 11.120 vs 21.414 (48.1% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 8350.870 vs 8986.487 (7.1% lower).
- `R1_vos` has the lower descriptive median than `R0_stock` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 601.156 vs 803.023 (25.1% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 10.501 vs 20.274 (48.2% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 8303.585 vs 8892.456 (6.6% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 531.948 vs 549.880 (3.3% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `library_first_render` (warm, real_2692, 2692 books): 10.736 vs 19.244 (44.2% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8350.831 vs 8901.784 (6.2% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `open_book` (warm, real_2692, 2692 books): 59.898 vs 62.889 (4.8% lower).
- `R0_stock` has the lower descriptive median than `R1_vos` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 904.154 vs 1215.906 (25.6% lower).
- `R0_stock` has the lower descriptive median than `R2_bookshelf` for `library_first_render` (real_first_run, real_2692, 2692 books): 11.120 vs 11.657 (4.6% lower).
- `R0_stock` has the lower descriptive median than `R2_bookshelf` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 8350.870 vs 8514.466 (1.9% lower).
- `R2_bookshelf` has the lower descriptive median than `R0_stock` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 560.523 vs 803.023 (30.2% lower).
- `R2_bookshelf` has the lower descriptive median than `R0_stock` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 10.435 vs 10.501 (0.6% lower).
- `R0_stock` has the lower descriptive median than `R2_bookshelf` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 8303.585 vs 8381.997 (0.9% lower).
- `R2_bookshelf` has the lower descriptive median than `R0_stock` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 515.380 vs 531.948 (3.1% lower).
- `R2_bookshelf` has the lower descriptive median than `R0_stock` for `library_first_render` (warm, real_2692, 2692 books): 9.916 vs 10.736 (7.6% lower).
- `R0_stock` has the lower descriptive median than `R2_bookshelf` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8350.831 vs 8412.747 (0.7% lower).
- `R2_bookshelf` has the lower descriptive median than `R0_stock` for `open_book` (warm, real_2692, 2692 books): 54.267 vs 59.898 (9.4% lower).
- `R0_stock` has the lower descriptive median than `R2_bookshelf` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 904.154 vs 907.329 (0.3% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `library_first_render` (real_first_run, real_2692, 2692 books): 11.120 vs 17.605 (36.8% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 8350.870 vs 12949.465 (35.5% lower).
- `R4_simpleui` has the lower descriptive median than `R0_stock` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 685.191 vs 803.023 (14.7% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 10.501 vs 17.844 (41.2% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 8303.585 vs 12974.470 (36.0% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 531.948 vs 617.023 (13.8% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `library_first_render` (warm, real_2692, 2692 books): 10.736 vs 24.069 (55.4% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8350.831 vs 15824.540 (47.2% lower).
- `R0_stock` has the lower descriptive median than `R4_simpleui` for `open_book` (warm, real_2692, 2692 books): 59.898 vs 150.739 (60.3% lower).
- `R4_simpleui` has the lower descriptive median than `R0_stock` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 891.434 vs 904.154 (1.4% lower).
- `R3_vos_bookshelf` has the lower descriptive median than `R1_vos` for `library_first_render` (real_first_run, real_2692, 2692 books): 20.643 vs 21.414 (3.6% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 8986.487 vs 9137.888 (1.7% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 601.156 vs 618.217 (2.8% lower).
- `R3_vos_bookshelf` has the lower descriptive median than `R1_vos` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 17.814 vs 20.274 (12.1% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 8892.456 vs 9069.923 (2.0% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 549.880 vs 556.195 (1.1% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `library_first_render` (warm, real_2692, 2692 books): 19.244 vs 19.875 (3.2% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8901.784 vs 9019.853 (1.3% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `open_book` (warm, real_2692, 2692 books): 62.889 vs 71.606 (12.2% lower).
- `R1_vos` has the lower descriptive median than `R3_vos_bookshelf` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 1215.906 vs 1244.856 (2.3% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R1_vos` for `library_first_render` (real_first_run, real_2692, 2692 books): 15.633 vs 21.414 (27.0% lower).
- `R1_vos` has the lower descriptive median than `R6_simpleui_vos` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 8986.487 vs 13391.957 (32.9% lower).
- `R1_vos` has the lower descriptive median than `R6_simpleui_vos` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 601.156 vs 741.012 (18.9% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R1_vos` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 13.945 vs 20.274 (31.2% lower).
- `R1_vos` has the lower descriptive median than `R6_simpleui_vos` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 8892.456 vs 13438.142 (33.8% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R1_vos` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 504.721 vs 549.880 (8.2% lower).
- `R1_vos` has the lower descriptive median than `R6_simpleui_vos` for `library_first_render` (warm, real_2692, 2692 books): 19.244 vs 22.059 (12.8% lower).
- `R1_vos` has the lower descriptive median than `R6_simpleui_vos` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8901.784 vs 15456.173 (42.4% lower).
- `R1_vos` has the lower descriptive median than `R6_simpleui_vos` for `open_book` (warm, real_2692, 2692 books): 62.889 vs 129.128 (51.3% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R1_vos` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 724.731 vs 1215.906 (40.4% lower).
- `R5_simpleui_bookshelf` has the lower descriptive median than `R4_simpleui` for `library_first_render` (real_first_run, real_2692, 2692 books): 17.282 vs 17.605 (1.8% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 12949.465 vs 13168.568 (1.7% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 685.191 vs 897.303 (23.6% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 17.844 vs 18.262 (2.3% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 12974.470 vs 13058.003 (0.6% lower).
- `R5_simpleui_bookshelf` has the lower descriptive median than `R4_simpleui` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 615.587 vs 617.023 (0.2% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `library_first_render` (warm, real_2692, 2692 books): 24.069 vs 25.025 (3.8% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 15824.540 vs 15935.815 (0.7% lower).
- `R4_simpleui` has the lower descriptive median than `R5_simpleui_bookshelf` for `open_book` (warm, real_2692, 2692 books): 150.739 vs 150.886 (0.1% lower).
- `R5_simpleui_bookshelf` has the lower descriptive median than `R4_simpleui` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 863.704 vs 891.434 (3.1% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `library_first_render` (real_first_run, real_2692, 2692 books): 15.633 vs 17.789 (12.1% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 13391.957 vs 13618.139 (1.7% lower).
- `R7_simpleui_vos_bookshelf` has the lower descriptive median than `R6_simpleui_vos` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 579.707 vs 741.012 (21.8% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 13.945 vs 14.025 (0.6% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 13438.142 vs 13512.394 (0.5% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 504.721 vs 513.818 (1.8% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `library_first_render` (warm, real_2692, 2692 books): 22.059 vs 22.502 (2.0% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 15456.173 vs 15543.315 (0.6% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `open_book` (warm, real_2692, 2692 books): 129.128 vs 131.957 (2.1% lower).
- `R6_simpleui_vos` has the lower descriptive median than `R7_simpleui_vos_bookshelf` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 724.731 vs 743.918 (2.6% lower).
- `R8_zenos` has the lower descriptive median than `R9_zenos_bookshelf` for `library_first_render` (real_first_run, real_2692, 2692 books): 19.640 vs 28.829 (31.9% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `memory:post_library_render_idle` (real_first_run, real_2692, 2692 books): 15136.253 vs 15910.880 (4.9% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `process:spawn_to_library_ready_ms` (real_first_run, real_2692, 2692 books): 680.508 vs 704.522 (3.4% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `library_first_render` (real_steady_cold, real_2692, 2692 books): 26.303 vs 27.018 (2.6% lower).
- `R8_zenos` has the lower descriptive median than `R9_zenos_bookshelf` for `memory:post_library_render_idle` (real_steady_cold, real_2692, 2692 books): 14660.420 vs 14791.176 (0.9% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `process:spawn_to_library_ready_ms` (real_steady_cold, real_2692, 2692 books): 586.068 vs 607.674 (3.6% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `library_first_render` (warm, real_2692, 2692 books): 17.243 vs 26.834 (35.7% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `library_next_page` (warm, real_2692, 2692 books): 8.850 vs 12.819 (31.0% lower).
- `R8_zenos` has the lower descriptive median than `R9_zenos_bookshelf` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 14861.540 vs 15130.050 (1.8% lower).
- `R8_zenos` has the lower descriptive median than `R9_zenos_bookshelf` for `open_book` (warm, real_2692, 2692 books): 71.659 vs 72.925 (1.7% lower).
- `R9_zenos_bookshelf` has the lower descriptive median than `R8_zenos` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 1698.236 vs 1963.421 (13.5% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `library_first_render` (warm, real_2692, 2692 books): 10.870 vs 11.369 (4.4% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8313.975 vs 9033.754 (8.0% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `open_book` (warm, real_2692, 2692 books): 50.814 vs 71.033 (28.5% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 950.336 vs 981.648 (3.2% lower).

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. No universal winner is selected.
