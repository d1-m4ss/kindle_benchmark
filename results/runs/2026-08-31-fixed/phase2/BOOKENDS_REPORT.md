# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `bookends_control`

Aggregated rows: 40; PASS=34; FAILED=0; UNSUPPORTED=6.

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
| A_stock | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 513.453 | 513.453 | 513.453–513.453 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 950.336 | 950.336 | 950.336–950.336 |
| A_stock | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 7472.865 | 7472.865 | 7472.865–7472.865 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_ui_ready_ms | PASS | 1 | 540.414 | 540.414 | 540.414–540.414 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_library_ready_ms | PASS | 1 | 981.648 | 981.648 | 981.648–981.648 |
| K_stock_bookends | warm | real_2692 | 2692 | process:spawn_to_process_exit_ms | PASS | 1 | 8945.412 | 8945.412 | 8945.412–8945.412 |

## Data-derived comparisons

- `A_stock` has the lower descriptive median than `K_stock_bookends` for `library_first_render` (warm, real_2692, 2692 books): 10.870 vs 11.369 (4.4% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `memory:post_library_render_idle` (warm, real_2692, 2692 books): 8313.975 vs 9033.754 (8.0% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `open_book` (warm, real_2692, 2692 books): 50.814 vs 71.033 (28.5% lower).
- `A_stock` has the lower descriptive median than `K_stock_bookends` for `process:spawn_to_library_ready_ms` (warm, real_2692, 2692 books): 950.336 vs 981.648 (3.2% lower).

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. No universal winner is selected.
