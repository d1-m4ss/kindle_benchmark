# KOReader UI Benchmark Report

> LOCAL EMULATOR FACTS ONLY. No physical-Kindle latency multiplier is applied.

Scope: `phase1`

Versions lock SHA-256: `2cdf45f8dfbb2504fce73c7a91c76384954a65bb1d59fdbc0884740b8ccd46fe`
Reader flash setting: `unset`

Aggregated rows: 808; PASS=738; FAILED=0; UNSUPPORTED=70; DEPRECATED=0.

## Default UI paging

| Stack | Mode | Dataset | Books | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| A_stock | warm | flat | 2000 | 10 | 201.000 | 1/1 | 30/30 | 20.224 | 55.320 | 15.085 | 57.888 | 23.340 | 67.880 | 12.328 | 73.959 |
| A_stock | warm | flat | 50 | 10 | 6.000 | 1/1 | 5/30 | 149.326 | 158.933 | 18.040 | 164.820 | 17.636 | 34.443 | 14.882 | 66.005 |
| A_stock | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| A_stock | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 13.546 | 36.862 | 8.860 | 46.286 | 15.993 | 37.122 | 11.783 | 44.806 |
| C_simpleui | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 11.407 | 22.486 | 10.172 | 28.471 | 14.595 | 33.204 | 8.622 | 37.333 |
| C_simpleui | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| C_simpleui | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 15.954 | 32.209 | 6.725 | 38.359 | 14.096 | 32.255 | 7.348 | 36.657 |
| D_zenos | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 14.907 | 23.112 | 7.346 | 46.237 | 16.071 | 28.371 | 3.833 | 31.537 |
| D_zenos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| D_zenos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | flat | 2000 | 9 | 223.000 | 1/1 | 30/30 | 15.121 | 33.854 | 8.236 | 49.420 | 15.274 | 35.228 | 10.776 | 36.947 |
| G_simpleui_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 10.995 | 22.065 | 8.456 | 28.687 | 15.842 | 32.823 | 9.418 | 34.591 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | flat | 2000 | 5 | 400.000 | 1/1 | 30/30 | 16.023 | 32.078 | 7.100 | 35.256 | 15.323 | 33.547 | 6.416 | 36.574 |
| H_zenos_bookshelf | warm | flat | 50 | 5 | 10.000 | 1/1 | 9/30 | 13.257 | 28.987 | 8.280 | 60.129 | 14.253 | 29.679 | 6.479 | 31.424 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | flat | 2000 | 9 | 222.000 | 1/1 | 30/30 | 14.139 | 32.752 | 8.176 | 54.575 | 13.181 | 37.538 | 9.887 | 40.231 |
| J_simpleui_vos | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 11.965 | 26.449 | 10.483 | 32.139 | 13.566 | 27.940 | 10.203 | 29.246 |
| J_simpleui_vos | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| J_simpleui_vos | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | 9 | 222.000 | 1/1 | 30/30 | 16.037 | 32.678 | 8.381 | 49.642 | 13.883 | 34.673 | 10.867 | 47.023 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | 9 | 6.000 | 1/1 | 5/30 | 11.016 | 26.995 | 10.929 | 32.035 | 13.470 | 28.568 | 10.196 | 29.029 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |

## Bookshelf paging

| Stack | Mode | Dataset | Books | Animation | Books/page (median, min–max) | Total pages | Runs (seq/cac) | Samples (seq/cac) | Sequential median ms | p90 ms | Min ms | Max ms | Cached median ms | p90 ms | Min ms | Max ms |
|:--|:--|:--|--:|:--|:--|--:|:--:|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| G_simpleui_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 148.884 | 181.532 | 132.413 | 265.391 | 132.257 | 133.808 | 122.263 | 230.835 |
| G_simpleui_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 23.023 | 26.299 | 11.139 | 116.732 | 16.111 | 16.286 | 11.123 | 102.179 |
| G_simpleui_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 148.790 | 149.425 | 131.686 | 149.499 | 132.346 | 147.340 | 115.383 | 181.995 |
| G_simpleui_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 16.779 | 20.924 | 10.427 | 21.119 | 16.117 | 20.338 | 10.315 | 62.135 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| G_simpleui_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 133.814 | 156.576 | 129.586 | 181.674 | 138.800 | 148.462 | 123.100 | 165.638 |
| H_zenos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 26.670 | 36.265 | 22.507 | 61.645 | 16.085 | 18.548 | 10.716 | 26.485 |
| H_zenos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 154.700 | 160.975 | 133.392 | 163.697 | 135.661 | 144.937 | 122.156 | 174.273 |
| H_zenos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 30.021 | 39.306 | 12.555 | 47.853 | 16.106 | 21.557 | 10.444 | 33.783 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 2000 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | default (medium) | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| H_zenos_bookshelf | warm | hierarchical | 50 | off | — | — | 1/1 | 0/0 | — | — | — | — | — | — | — | — |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | default (medium) | 8 | 250.000 | 1/1 | 30/30 | 132.689 | 141.593 | 117.859 | 246.267 | 132.243 | 137.161 | 118.511 | 257.853 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | off | 8 | 250.000 | 1/1 | 30/30 | 16.042 | 16.268 | 7.986 | 139.691 | 16.130 | 16.560 | 5.223 | 126.151 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | default (medium) | 8 | 7.000 | 1/1 | 6/30 | 132.704 | 140.999 | 132.114 | 149.245 | 132.750 | 167.527 | 114.845 | 195.518 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | off | 8 | 7.000 | 1/1 | 6/30 | 16.438 | 32.377 | 14.480 | 32.416 | 16.195 | 32.691 | 9.602 | 63.290 |
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

## Comparative Findings

- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 15.993 ms vs 23.340 ms (31.5% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 13.546 ms vs 20.224 ms (33.0% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 14.595 ms vs 17.636 ms (17.2% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 11.407 ms vs 149.326 ms (92.4% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 14.096 ms vs 23.340 ms (39.6% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 15.954 ms vs 20.224 ms (21.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 16.071 ms vs 17.636 ms (8.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 14.907 ms vs 149.326 ms (90.0% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 2000 books): 15.274 ms vs 15.993 ms (4.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 13.546 ms vs 15.121 ms (10.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 14.595 ms vs 15.842 ms (7.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 10.995 ms vs 11.407 ms (3.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 14.096 ms vs 15.323 ms (8.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 15.954 ms vs 16.023 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 14.253 ms vs 16.071 ms (11.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 50 books): 13.257 ms vs 14.907 ms (11.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 2000 books): 13.181 ms vs 15.993 ms (17.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 13.546 ms vs 14.139 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 13.566 ms vs 14.595 ms (7.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 11.407 ms vs 11.965 ms (4.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.181 ms vs 13.883 ms (5.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 14.139 ms vs 16.037 ms (11.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 13.470 ms vs 13.566 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 11.016 ms vs 11.965 ms (7.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## All Scenario Results

| Stack | Mode | Dataset | Books | Scenario | Status | n | Median ms | p10 ms | p90 ms | Min–max ms |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|
| A_stock | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 10.939 | 10.780 | 11.193 | 10.740–11.257 |
| A_stock | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.196 | 16.176 | 16.198 | 16.171–16.198 |
| A_stock | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 11.753 | 8.209 | 12.081 | 7.323–12.163 |
| A_stock | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.106 | 15.250 | 16.123 | 15.036–16.127 |
| A_stock | warm | flat | 2000 | change_sort_mode | PASS | 10 | 105.136 | 84.708 | 133.340 | 82.694–134.427 |
| A_stock | warm | flat | 2000 | close_book | PASS | 10 | 54.469 | 52.894 | 57.593 | 52.510–58.551 |
| A_stock | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.646 | 16.634 | 16.676 | 16.607–16.678 |
| A_stock | warm | flat | 2000 | home_to_library | PASS | 10 | 90.206 | 52.483 | 185.066 | 42.377–200.100 |
| A_stock | warm | flat | 2000 | library_cached_paging | PASS | 30 | 23.340 | 14.005 | 67.880 | 12.328–73.959 |
| A_stock | warm | flat | 2000 | library_first_render | PASS | 10 | 42.694 | 41.168 | 81.256 | 39.588–92.476 |
| A_stock | warm | flat | 2000 | library_folder_back | PASS | 10 | 41.422 | 39.712 | 68.441 | 39.473–73.054 |
| A_stock | warm | flat | 2000 | library_folder_enter | PASS | 10 | 7.203 | 4.056 | 29.914 | 3.822–31.002 |
| A_stock | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 20.224 | 17.425 | 55.320 | 15.085–57.888 |
| A_stock | warm | flat | 2000 | open_book | PASS | 10 | 51.382 | 50.083 | 53.578 | 46.844–55.045 |
| A_stock | warm | flat | 2000 | open_book_minimal | PASS | 10 | 58.568 | 57.685 | 60.528 | 57.546–60.605 |
| A_stock | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.661 | 15.729 | 16.692 | 7.507–16.696 |
| A_stock | warm | flat | 2000 | repeated_nav | PASS | 2 | 310.259 | 306.192 | 314.326 | 305.175–315.343 |
| A_stock | warm | flat | 50 | change_sort_mode | PASS | 10 | 35.308 | 30.152 | 55.188 | 29.989–60.575 |
| A_stock | warm | flat | 50 | close_book | PASS | 10 | 25.523 | 24.028 | 35.623 | 23.502–36.744 |
| A_stock | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.662 | 16.633 | 16.670 | 16.619–16.689 |
| A_stock | warm | flat | 50 | home_to_library | PASS | 10 | 24.515 | 22.823 | 39.189 | 21.515–44.096 |
| A_stock | warm | flat | 50 | library_cached_paging | PASS | 30 | 17.636 | 15.633 | 34.443 | 14.882–66.005 |
| A_stock | warm | flat | 50 | library_first_render | PASS | 10 | 31.080 | 26.233 | 126.247 | 25.616–173.304 |
| A_stock | warm | flat | 50 | library_folder_back | PASS | 10 | 17.074 | 16.654 | 26.215 | 16.470–26.489 |
| A_stock | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.543 | 4.536 | 17.708 | 3.972–27.084 |
| A_stock | warm | flat | 50 | library_sequential_paging | PASS | 5 | 149.326 | 50.516 | 158.933 | 18.040–164.820 |
| A_stock | warm | flat | 50 | open_book | PASS | 10 | 37.276 | 29.273 | 52.743 | 29.135–53.087 |
| A_stock | warm | flat | 50 | open_book_minimal | PASS | 10 | 41.572 | 30.688 | 51.981 | 30.325–58.825 |
| A_stock | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.666 | 15.082 | 16.686 | 6.235–16.691 |
| A_stock | warm | flat | 50 | repeated_nav | PASS | 2 | 179.299 | 169.007 | 189.591 | 166.434–192.164 |
| A_stock | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 16.095 | 9.669 | 22.478 | 7.811–24.409 |
| A_stock | warm | hierarchical | 2000 | close_book | PASS | 10 | 24.360 | 14.817 | 26.052 | 14.768–29.390 |
| A_stock | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.665 | 16.624 | 16.708 | 16.597–16.718 |
| A_stock | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.101 | 10.137 | 21.995 | 8.604–23.577 |
| A_stock | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.116 | 10.374 | 22.292 | 9.258–22.953 |
| A_stock | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 14.264 | 11.680 | 17.317 | 8.680–23.297 |
| A_stock | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 18.139 | 7.471 | 27.206 | 4.556–29.412 |
| A_stock | warm | hierarchical | 2000 | open_book | PASS | 10 | 30.022 | 27.510 | 34.136 | 26.645–45.533 |
| A_stock | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 41.175 | 33.430 | 44.644 | 32.205–45.322 |
| A_stock | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.665 | 15.939 | 17.495 | 9.679–24.247 |
| A_stock | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 16.087 | 10.519 | 21.686 | 10.406–21.747 |
| A_stock | warm | hierarchical | 50 | close_book | PASS | 10 | 18.813 | 17.064 | 23.241 | 16.032–23.887 |
| A_stock | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.665 | 16.642 | 16.711 | 16.630–16.743 |
| A_stock | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.131 | 10.351 | 21.848 | 9.285–22.992 |
| A_stock | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.111 | 10.359 | 21.866 | 10.153–22.420 |
| A_stock | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.611 | 10.685 | 17.271 | 9.555–22.496 |
| A_stock | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.599 | 13.059 | 25.147 | 12.627–25.279 |
| A_stock | warm | hierarchical | 50 | open_book | PASS | 10 | 42.302 | 38.274 | 48.299 | 34.375–48.558 |
| A_stock | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 33.772 | 28.613 | 40.011 | 27.808–40.621 |
| A_stock | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.666 | 16.649 | 23.765 | 16.642–24.210 |
| C_simpleui | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.170 | 8.094 | 10.128 | 8.075–10.617 |
| C_simpleui | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 22.045 | 21.799 | 23.083 | 21.738–23.342 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 9.629 | 9.413 | 10.243 | 9.359–10.397 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 24.878 | 22.084 | 30.032 | 21.386–31.321 |
| C_simpleui | warm | flat | 2000 | change_sort_mode | PASS | 10 | 85.226 | 66.624 | 92.184 | 65.288–95.876 |
| C_simpleui | warm | flat | 2000 | close_book | PASS | 10 | 164.123 | 102.584 | 242.281 | 100.524–246.886 |
| C_simpleui | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.645 | 16.070 | 34.540 | 11.724–195.344 |
| C_simpleui | warm | flat | 2000 | home_to_library | PASS | 10 | 16.674 | 12.752 | 32.287 | 11.834–33.156 |
| C_simpleui | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.993 | 12.747 | 37.122 | 11.783–44.806 |
| C_simpleui | warm | flat | 2000 | library_first_render | PASS | 10 | 85.212 | 62.793 | 89.480 | 61.218–94.421 |
| C_simpleui | warm | flat | 2000 | library_folder_back | PASS | 10 | 40.779 | 39.862 | 60.190 | 38.479–60.706 |
| C_simpleui | warm | flat | 2000 | library_folder_enter | PASS | 10 | 12.352 | 10.676 | 16.867 | 9.308–34.697 |
| C_simpleui | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 13.546 | 10.042 | 36.862 | 8.860–46.286 |
| C_simpleui | warm | flat | 2000 | open_book | PASS | 10 | 130.392 | 119.082 | 135.502 | 114.407–150.223 |
| C_simpleui | warm | flat | 2000 | open_book_minimal | PASS | 10 | 93.321 | 80.421 | 124.692 | 79.711–125.587 |
| C_simpleui | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.944 | 16.661 | 57.052 | 16.653–312.074 |
| C_simpleui | warm | flat | 2000 | repeated_nav | PASS | 2 | 709.843 | 677.807 | 741.880 | 669.798–749.889 |
| C_simpleui | warm | flat | 2000 | start_to_home | PASS | 10 | 16.660 | 12.308 | 16.697 | 7.321–16.697 |
| C_simpleui | warm | flat | 50 | change_sort_mode | PASS | 10 | 29.779 | 20.212 | 45.450 | 19.014–50.566 |
| C_simpleui | warm | flat | 50 | close_book | PASS | 10 | 48.687 | 36.734 | 112.406 | 33.858–128.900 |
| C_simpleui | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.658 | 13.151 | 16.683 | 6.646–16.687 |
| C_simpleui | warm | flat | 50 | home_to_library | PASS | 10 | 16.665 | 15.428 | 29.132 | 13.561–29.217 |
| C_simpleui | warm | flat | 50 | library_cached_paging | PASS | 30 | 14.595 | 9.900 | 33.204 | 8.622–37.333 |
| C_simpleui | warm | flat | 50 | library_first_render | PASS | 10 | 45.561 | 36.221 | 54.660 | 35.949–62.252 |
| C_simpleui | warm | flat | 50 | library_folder_back | PASS | 10 | 13.280 | 11.519 | 29.023 | 11.506–30.068 |
| C_simpleui | warm | flat | 50 | library_folder_enter | PASS | 10 | 13.141 | 11.008 | 25.400 | 10.616–26.197 |
| C_simpleui | warm | flat | 50 | library_sequential_paging | PASS | 5 | 11.407 | 10.270 | 22.486 | 10.172–28.471 |
| C_simpleui | warm | flat | 50 | open_book | PASS | 10 | 107.080 | 65.621 | 115.286 | 53.931–122.567 |
| C_simpleui | warm | flat | 50 | open_book_minimal | PASS | 10 | 68.434 | 44.879 | 87.186 | 41.716–92.469 |
| C_simpleui | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.633 | 9.825 | 24.256 | 8.612–92.151 |
| C_simpleui | warm | flat | 50 | repeated_nav | PASS | 2 | 347.496 | 291.896 | 403.097 | 277.996–416.997 |
| C_simpleui | warm | flat | 50 | start_to_home | PASS | 10 | 16.667 | 15.576 | 16.684 | 6.797–16.715 |
| C_simpleui | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 38.278 | 25.358 | 42.552 | 23.429–43.646 |
| C_simpleui | warm | hierarchical | 2000 | close_book | PASS | 10 | 52.751 | 48.383 | 67.645 | 48.315–152.842 |
| C_simpleui | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.679 | 16.217 | 23.059 | 12.863–80.036 |
| C_simpleui | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.636 | 13.339 | 28.217 | 13.136–28.982 |
| C_simpleui | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.771 | 31.805 | 34.339 | 23.537–40.977 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 20.355 | 14.979 | 27.056 | 14.937–27.484 |
| C_simpleui | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.585 | 13.179 | 29.126 | 8.486–33.208 |
| C_simpleui | warm | hierarchical | 2000 | open_book | PASS | 10 | 102.304 | 96.128 | 113.445 | 93.291–118.024 |
| C_simpleui | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 49.665 | 40.377 | 62.375 | 38.800–67.668 |
| C_simpleui | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.633 | 13.029 | 87.356 | 11.845–98.875 |
| C_simpleui | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.685 | 15.749 | 16.728 | 7.438–16.749 |
| C_simpleui | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 12.028 | 10.828 | 25.813 | 10.157–26.124 |
| C_simpleui | warm | hierarchical | 50 | close_book | PASS | 10 | 45.760 | 36.686 | 57.744 | 34.769–103.436 |
| C_simpleui | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.666 | 16.327 | 23.007 | 13.620–79.335 |
| C_simpleui | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.636 | 13.721 | 27.998 | 10.048–28.253 |
| C_simpleui | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.751 | 23.325 | 42.131 | 20.921–44.922 |
| C_simpleui | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 15.767 | 7.777 | 25.790 | 7.530–25.813 |
| C_simpleui | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.906 | 8.214 | 29.517 | 8.056–55.164 |
| C_simpleui | warm | hierarchical | 50 | open_book | PASS | 10 | 83.116 | 59.327 | 108.126 | 54.825–108.400 |
| C_simpleui | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 45.654 | 41.901 | 61.620 | 34.721–63.941 |
| C_simpleui | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.632 | 13.245 | 16.686 | 13.101–16.726 |
| C_simpleui | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.668 | 15.671 | 16.708 | 6.960–16.709 |
| D_zenos | first_run_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 31.910 | 31.864 | 31.928 | 31.853–31.932 |
| D_zenos | first_run_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 16.906 | 16.689 | 16.945 | 16.635–16.955 |
| D_zenos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 29.252 | 19.796 | 31.970 | 17.432–32.649 |
| D_zenos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 15.071 | 15.069 | 15.264 | 15.069–15.312 |
| D_zenos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 60.159 | 53.126 | 77.443 | 52.537–78.827 |
| D_zenos | warm | flat | 2000 | close_book | PASS | 10 | 33.552 | 27.022 | 62.552 | 23.718–78.793 |
| D_zenos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 33.314 | 33.036 | 33.371 | 31.336–33.374 |
| D_zenos | warm | flat | 2000 | home_to_library | PASS | 10 | 33.373 | 33.355 | 33.384 | 33.353–33.401 |
| D_zenos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 14.096 | 8.047 | 32.255 | 7.348–36.657 |
| D_zenos | warm | flat | 2000 | library_first_render | PASS | 10 | 26.951 | 23.609 | 46.872 | 22.639–49.567 |
| D_zenos | warm | flat | 2000 | library_folder_back | PASS | 10 | 23.386 | 21.741 | 37.517 | 21.714–39.584 |
| D_zenos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 13.552 | 9.856 | 23.029 | 4.767–23.248 |
| D_zenos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 15.954 | 8.684 | 32.209 | 6.725–38.359 |
| D_zenos | warm | flat | 2000 | open_book | PASS | 10 | 71.515 | 44.594 | 79.827 | 43.284–84.601 |
| D_zenos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 58.563 | 44.115 | 74.465 | 43.816–77.722 |
| D_zenos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.702 | 16.599 | 21.064 | 16.597–33.570 |
| D_zenos | warm | flat | 2000 | repeated_nav | PASS | 2 | 190.303 | 175.545 | 205.061 | 171.855–208.751 |
| D_zenos | warm | flat | 2000 | start_to_home | PASS | 10 | 33.292 | 32.694 | 33.389 | 31.492–33.744 |
| D_zenos | warm | flat | 50 | change_sort_mode | PASS | 10 | 16.090 | 7.307 | 28.721 | 5.959–28.798 |
| D_zenos | warm | flat | 50 | close_book | PASS | 10 | 30.463 | 26.723 | 33.028 | 25.296–33.409 |
| D_zenos | warm | flat | 50 | close_quick_settings | PASS | 10 | 33.335 | 33.312 | 33.395 | 33.199–33.406 |
| D_zenos | warm | flat | 50 | home_to_library | PASS | 10 | 33.376 | 33.327 | 33.406 | 33.323–33.463 |
| D_zenos | warm | flat | 50 | library_cached_paging | PASS | 30 | 16.071 | 5.475 | 28.371 | 3.833–31.537 |
| D_zenos | warm | flat | 50 | library_first_render | PASS | 10 | 18.930 | 17.877 | 21.562 | 17.125–21.801 |
| D_zenos | warm | flat | 50 | library_folder_back | PASS | 10 | 16.613 | 8.025 | 28.351 | 6.095–28.807 |
| D_zenos | warm | flat | 50 | library_folder_enter | PASS | 10 | 16.645 | 4.476 | 29.088 | 4.345–29.740 |
| D_zenos | warm | flat | 50 | library_sequential_paging | PASS | 9 | 14.907 | 8.365 | 23.112 | 7.346–46.237 |
| D_zenos | warm | flat | 50 | open_book | PASS | 10 | 63.691 | 59.812 | 67.825 | 56.331–71.906 |
| D_zenos | warm | flat | 50 | open_book_minimal | PASS | 10 | 61.839 | 51.420 | 65.738 | 34.823–68.002 |
| D_zenos | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.664 | 13.858 | 16.710 | 4.832–16.729 |
| D_zenos | warm | flat | 50 | repeated_nav | PASS | 2 | 187.786 | 180.221 | 195.350 | 178.330–197.241 |
| D_zenos | warm | flat | 50 | start_to_home | PASS | 10 | 33.277 | 30.799 | 33.415 | 24.570–33.870 |
| D_zenos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 13.829 | 9.713 | 24.791 | 9.679–29.826 |
| D_zenos | warm | hierarchical | 2000 | close_book | PASS | 10 | 38.589 | 31.811 | 61.937 | 28.907–82.880 |
| D_zenos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 33.293 | 33.253 | 33.377 | 33.206–33.406 |
| D_zenos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 33.419 | 33.327 | 33.439 | 33.320–33.498 |
| D_zenos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.054 | 15.077 | 16.234 | 12.702–17.010 |
| D_zenos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.238 | 9.026 | 28.594 | 8.580–29.462 |
| D_zenos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.991 | 11.171 | 26.936 | 8.882–29.259 |
| D_zenos | warm | hierarchical | 2000 | open_book | PASS | 10 | 64.794 | 41.682 | 89.082 | 41.223–99.683 |
| D_zenos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 63.008 | 39.950 | 68.848 | 37.144–70.210 |
| D_zenos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.691 | 16.088 | 16.720 | 11.111–16.736 |
| D_zenos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 33.261 | 31.240 | 33.354 | 15.911–33.417 |
| D_zenos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 15.645 | 10.222 | 27.298 | 9.479–27.821 |
| D_zenos | warm | hierarchical | 50 | close_book | PASS | 10 | 39.147 | 38.347 | 43.137 | 38.130–58.367 |
| D_zenos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 33.328 | 33.307 | 33.342 | 33.305–33.375 |
| D_zenos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 33.367 | 33.314 | 33.480 | 33.292–33.512 |
| D_zenos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.104 | 16.011 | 16.174 | 15.574–16.187 |
| D_zenos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.665 | 9.760 | 27.094 | 8.750–27.334 |
| D_zenos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 16.660 | 8.689 | 27.516 | 6.329–30.011 |
| D_zenos | warm | hierarchical | 50 | open_book | PASS | 10 | 57.197 | 41.651 | 63.334 | 40.207–65.903 |
| D_zenos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 52.240 | 39.732 | 65.683 | 35.714–65.775 |
| D_zenos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.671 | 16.637 | 18.392 | 16.631–33.357 |
| D_zenos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 33.255 | 32.535 | 33.334 | 26.366–33.341 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.737 | 8.603 | 9.071 | 8.569–9.155 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 25.249 | 22.403 | 26.161 | 21.692–26.389 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.257 | 130.453 | 133.808 | 122.263–230.835 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.111 | 12.529 | 16.286 | 11.123–102.179 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 14.310 | 11.821 | 95.866 | 11.758–110.450 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 148.884 | 133.116 | 181.532 | 132.413–265.391 |
| G_simpleui_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 23.023 | 16.680 | 26.299 | 11.139–116.732 |
| G_simpleui_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 82.829 | 70.842 | 102.003 | 70.836–105.372 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 105.703 | 102.322 | 235.126 | 101.165–259.321 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 32.862 | 27.148 | 33.168 | 25.983–33.209 |
| G_simpleui_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.636 | 15.830 | 35.675 | 8.768–206.658 |
| G_simpleui_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.666 | 12.251 | 31.382 | 11.173–31.556 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.274 | 12.627 | 35.228 | 10.776–36.947 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 89.003 | 63.517 | 100.008 | 60.393–101.302 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 41.245 | 38.861 | 61.101 | 38.406–61.750 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 9.683 | 9.348 | 10.995 | 9.102–16.511 |
| G_simpleui_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 15.121 | 9.286 | 33.854 | 8.236–49.420 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 136.332 | 107.257 | 166.870 | 88.645–168.062 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 89.925 | 80.462 | 120.441 | 61.201–122.227 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.850 | 16.666 | 17.917 | 16.364–18.851 |
| G_simpleui_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 17.361 | 16.871 | 52.031 | 16.728–196.081 |
| G_simpleui_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 721.054 | 644.514 | 797.594 | 625.379–816.729 |
| G_simpleui_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.650 | 10.944 | 16.672 | 7.420–16.676 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.346 | 130.835 | 147.340 | 115.383–181.995 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.117 | 11.129 | 20.338 | 10.315–62.135 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 21.684 | 19.601 | 61.908 | 18.621–70.798 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 148.790 | 132.266 | 149.425 | 131.686–149.499 |
| G_simpleui_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 16.779 | 12.832 | 20.924 | 10.427–21.119 |
| G_simpleui_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 34.200 | 20.606 | 41.276 | 19.085–42.490 |
| G_simpleui_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 70.931 | 54.743 | 135.633 | 52.561–138.588 |
| G_simpleui_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 29.591 | 26.870 | 32.828 | 23.538–32.854 |
| G_simpleui_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.646 | 16.295 | 24.697 | 13.383–96.602 |
| G_simpleui_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.676 | 13.744 | 29.638 | 13.039–30.379 |
| G_simpleui_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 15.842 | 10.555 | 32.823 | 9.418–34.591 |
| G_simpleui_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 44.317 | 35.674 | 56.890 | 35.164–59.415 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 12.361 | 11.644 | 28.158 | 10.986–28.869 |
| G_simpleui_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 14.280 | 10.101 | 32.080 | 9.296–32.367 |
| G_simpleui_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 10.995 | 9.232 | 22.065 | 8.456–28.687 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 113.495 | 97.673 | 134.136 | 83.488–136.883 |
| G_simpleui_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 86.728 | 44.535 | 92.839 | 43.889–95.156 |
| G_simpleui_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 23.602 | 21.916 | 27.448 | 21.334–30.717 |
| G_simpleui_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 19.692 | 17.978 | 100.238 | 17.750–112.524 |
| G_simpleui_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 435.383 | 393.995 | 476.771 | 383.648–487.118 |
| G_simpleui_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.664 | 13.195 | 16.701 | 6.878–16.718 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 17.596 | 16.397 | 62.005 | 16.319–68.668 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 39.082 | 26.364 | 44.236 | 24.976–49.077 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 63.366 | 58.621 | 76.390 | 54.694–156.158 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 26.911 | 24.028 | 29.412 | 23.669–31.998 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.681 | 15.182 | 26.929 | 7.490–118.770 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.635 | 12.622 | 29.108 | 9.525–32.265 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.760 | 22.782 | 42.705 | 21.031–44.799 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 19.739 | 14.988 | 28.250 | 14.860–28.643 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 15.184 | 7.413 | 19.040 | 7.116–21.035 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 118.605 | 104.069 | 138.042 | 95.973–143.641 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 85.846 | 52.881 | 107.162 | 50.483–148.585 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 22.087 | 21.159 | 27.003 | 20.560–27.253 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.657 | 14.724 | 92.437 | 13.336–101.457 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.660 | 15.849 | 16.692 | 8.790–16.706 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 15.995 | 13.264 | 53.121 | 13.262–60.286 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 12.230 | 10.053 | 26.511 | 10.020–26.960 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 41.451 | 38.333 | 84.793 | 34.562–114.203 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 30.040 | 27.732 | 31.455 | 25.557–32.714 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.644 | 11.888 | 17.197 | 7.032–21.760 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.636 | 12.744 | 28.861 | 11.588–29.865 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.740 | 30.505 | 35.089 | 21.092–45.360 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 15.174 | 8.136 | 26.580 | 8.122–27.607 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.678 | 8.256 | 26.977 | 7.809–27.251 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 101.340 | 61.807 | 111.485 | 54.531–114.185 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 50.070 | 47.161 | 59.898 | 45.828–73.910 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 17.253 | 16.874 | 20.608 | 16.801–21.767 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.665 | 11.575 | 25.066 | 11.229–87.331 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.675 | 15.827 | 16.714 | 8.586–16.783 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 27.457 | 20.143 | 28.223 | 18.315–28.415 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 15.082 | 15.012 | 15.267 | 14.994–15.313 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 138.800 | 132.091 | 148.462 | 123.100–165.638 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.085 | 13.319 | 18.548 | 10.716–26.485 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 19.477 | 17.989 | 59.495 | 15.582–64.642 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 133.814 | 132.187 | 156.576 | 129.586–181.674 |
| H_zenos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 26.670 | 23.796 | 36.265 | 22.507–61.645 |
| H_zenos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 59.174 | 52.513 | 86.719 | 51.230–89.920 |
| H_zenos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 41.187 | 37.754 | 84.519 | 37.699–132.707 |
| H_zenos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 15.819 | 11.908 | 16.389 | 11.241–16.649 |
| H_zenos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 33.323 | 33.292 | 33.354 | 33.291–33.367 |
| H_zenos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 33.370 | 33.341 | 33.400 | 33.331–33.420 |
| H_zenos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 15.323 | 7.972 | 33.547 | 6.416–36.574 |
| H_zenos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 27.739 | 25.298 | 43.185 | 25.018–46.555 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 23.828 | 21.735 | 36.226 | 21.572–38.540 |
| H_zenos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 5.732 | 4.610 | 12.920 | 4.533–15.390 |
| H_zenos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.023 | 7.729 | 32.078 | 7.100–35.256 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 102.120 | 63.976 | 117.398 | 62.798–119.088 |
| H_zenos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 60.755 | 52.853 | 74.542 | 52.038–86.989 |
| H_zenos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 20.662 | 19.880 | 24.915 | 18.568–38.179 |
| H_zenos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.672 | 15.732 | 16.694 | 7.462–16.698 |
| H_zenos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 219.298 | 204.893 | 233.704 | 201.292–237.305 |
| H_zenos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 33.264 | 31.408 | 33.382 | 30.440–33.807 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 135.661 | 132.231 | 144.937 | 122.156–174.273 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.106 | 12.580 | 21.557 | 10.444–33.783 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 20.193 | 15.945 | 55.779 | 15.695–66.376 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 154.700 | 142.507 | 160.975 | 133.392–163.697 |
| H_zenos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 30.021 | 20.046 | 39.306 | 12.555–47.853 |
| H_zenos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 14.937 | 13.079 | 30.565 | 11.980–32.735 |
| H_zenos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 41.845 | 40.586 | 51.659 | 40.564–99.728 |
| H_zenos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 15.322 | 11.304 | 16.326 | 10.755–16.608 |
| H_zenos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 33.328 | 33.290 | 33.344 | 33.282–33.347 |
| H_zenos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 33.342 | 33.299 | 33.423 | 33.275–33.444 |
| H_zenos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 14.253 | 8.271 | 29.679 | 6.479–31.424 |
| H_zenos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 19.378 | 18.294 | 20.526 | 16.284–22.880 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 16.709 | 15.105 | 29.289 | 14.937–29.742 |
| H_zenos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 10.399 | 4.116 | 26.935 | 3.850–37.669 |
| H_zenos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 9 | 13.257 | 9.197 | 28.987 | 8.280–60.129 |
| H_zenos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 64.621 | 60.060 | 111.868 | 59.132–114.276 |
| H_zenos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 53.579 | 46.000 | 58.351 | 45.283–59.064 |
| H_zenos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 23.376 | 20.433 | 27.023 | 19.884–41.088 |
| H_zenos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 16.675 | 16.228 | 17.461 | 12.564–19.583 |
| H_zenos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 172.887 | 165.539 | 180.236 | 163.702–182.073 |
| H_zenos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 33.264 | 31.023 | 33.416 | 25.740–33.753 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 14.264 | 8.838 | 45.609 | 6.931–54.213 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 12.829 | 11.057 | 30.060 | 10.923–36.626 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 60.254 | 29.914 | 70.505 | 28.513–70.665 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 16.309 | 16.161 | 16.700 | 15.873–19.006 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 33.322 | 33.090 | 33.365 | 31.217–33.381 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 33.386 | 33.326 | 33.415 | 33.308–33.425 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 16.130 | 15.333 | 16.199 | 14.006–16.256 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 16.087 | 10.714 | 29.142 | 10.580–29.255 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 13.284 | 11.298 | 17.970 | 9.683–29.828 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 59.239 | 45.885 | 86.217 | 45.437–90.268 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 51.919 | 46.943 | 60.581 | 46.210–79.088 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 17.053 | 16.599 | 18.546 | 13.650–31.451 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.655 | 16.588 | 16.701 | 16.316–16.740 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 33.248 | 31.078 | 33.367 | 15.414–33.510 |
| H_zenos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 15.303 | 8.397 | 48.060 | 8.209–49.370 |
| H_zenos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 14.305 | 10.469 | 27.574 | 10.252–28.541 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 34.320 | 30.124 | 68.174 | 29.450–73.428 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 16.351 | 16.196 | 16.418 | 16.020–16.422 |
| H_zenos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 33.300 | 33.181 | 33.342 | 33.128–33.354 |
| H_zenos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 33.380 | 33.341 | 33.416 | 33.333–33.533 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 16.087 | 15.974 | 16.171 | 15.966–16.230 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.658 | 10.777 | 27.570 | 10.328–27.655 |
| H_zenos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.852 | 7.454 | 29.817 | 5.057–34.464 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 58.915 | 48.136 | 89.116 | 47.125–155.759 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 59.630 | 44.975 | 78.052 | 37.134–88.010 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 16.960 | 16.852 | 18.238 | 16.824–27.237 |
| H_zenos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.671 | 16.592 | 16.744 | 16.588–16.771 |
| H_zenos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 33.284 | 32.516 | 33.320 | 26.515–33.411 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 7.912 | 7.827 | 8.553 | 7.806–8.713 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 19.792 | 18.531 | 26.190 | 18.216–27.790 |
| J_simpleui_vos | warm | flat | 2000 | change_sort_mode | PASS | 10 | 130.284 | 100.552 | 144.233 | 99.704–144.410 |
| J_simpleui_vos | warm | flat | 2000 | close_book | PASS | 10 | 133.377 | 128.002 | 275.328 | 116.621–276.160 |
| J_simpleui_vos | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.656 | 16.603 | 16.695 | 16.414–16.699 |
| J_simpleui_vos | warm | flat | 2000 | home_to_library | PASS | 10 | 16.646 | 12.073 | 31.817 | 11.975–31.970 |
| J_simpleui_vos | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.181 | 11.236 | 37.538 | 9.887–40.231 |
| J_simpleui_vos | warm | flat | 2000 | library_first_render | PASS | 10 | 74.930 | 67.729 | 93.552 | 66.152–95.598 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_back | PASS | 10 | 74.733 | 52.080 | 79.639 | 50.156–79.964 |
| J_simpleui_vos | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.597 | 10.077 | 11.225 | 9.604–12.000 |
| J_simpleui_vos | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 14.139 | 8.940 | 32.752 | 8.176–54.575 |
| J_simpleui_vos | warm | flat | 2000 | open_book | PASS | 10 | 144.618 | 123.633 | 155.962 | 117.203–170.327 |
| J_simpleui_vos | warm | flat | 2000 | open_book_minimal | PASS | 10 | 86.233 | 67.579 | 101.998 | 54.888–106.130 |
| J_simpleui_vos | warm | flat | 2000 | open_quick_settings | PASS | 10 | 20.488 | 17.585 | 60.256 | 16.477–401.422 |
| J_simpleui_vos | warm | flat | 2000 | repeated_nav | PASS | 2 | 786.106 | 748.040 | 824.172 | 738.524–833.688 |
| J_simpleui_vos | warm | flat | 2000 | start_to_home | PASS | 10 | 16.655 | 13.653 | 16.695 | 7.700–16.705 |
| J_simpleui_vos | warm | flat | 50 | change_sort_mode | PASS | 10 | 32.055 | 22.236 | 35.265 | 22.202–37.305 |
| J_simpleui_vos | warm | flat | 50 | close_book | PASS | 10 | 51.364 | 48.382 | 65.216 | 44.389–126.654 |
| J_simpleui_vos | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.652 | 15.914 | 16.681 | 9.597–16.704 |
| J_simpleui_vos | warm | flat | 50 | home_to_library | PASS | 10 | 16.667 | 13.134 | 29.901 | 12.330–29.950 |
| J_simpleui_vos | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.566 | 11.869 | 27.940 | 10.203–29.246 |
| J_simpleui_vos | warm | flat | 50 | library_first_render | PASS | 10 | 36.138 | 32.788 | 45.883 | 32.772–45.984 |
| J_simpleui_vos | warm | flat | 50 | library_folder_back | PASS | 10 | 21.855 | 13.984 | 32.357 | 13.657–32.988 |
| J_simpleui_vos | warm | flat | 50 | library_folder_enter | PASS | 10 | 12.704 | 10.262 | 24.039 | 10.254–28.412 |
| J_simpleui_vos | warm | flat | 50 | library_sequential_paging | PASS | 5 | 11.965 | 10.663 | 26.449 | 10.483–32.139 |
| J_simpleui_vos | warm | flat | 50 | open_book | PASS | 10 | 119.284 | 96.873 | 125.409 | 96.148–125.743 |
| J_simpleui_vos | warm | flat | 50 | open_book_minimal | PASS | 10 | 84.334 | 54.209 | 92.361 | 42.882–96.740 |
| J_simpleui_vos | warm | flat | 50 | open_quick_settings | PASS | 10 | 21.973 | 20.017 | 94.615 | 19.769–100.704 |
| J_simpleui_vos | warm | flat | 50 | repeated_nav | PASS | 2 | 416.266 | 403.355 | 429.177 | 400.127–432.405 |
| J_simpleui_vos | warm | flat | 50 | start_to_home | PASS | 10 | 16.662 | 14.946 | 16.683 | 7.904–16.689 |
| J_simpleui_vos | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 23.270 | 17.765 | 38.569 | 17.687–38.979 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_book | PASS | 10 | 57.602 | 54.401 | 149.753 | 53.168–155.231 |
| J_simpleui_vos | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.666 | 16.646 | 16.713 | 16.632–16.754 |
| J_simpleui_vos | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.609 | 12.324 | 28.787 | 11.163–29.439 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.780 | 32.696 | 32.840 | 32.488–32.991 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.522 | 7.816 | 26.565 | 6.688–28.179 |
| J_simpleui_vos | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.240 | 8.054 | 26.998 | 6.889–31.009 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book | PASS | 10 | 115.138 | 71.498 | 137.197 | 53.245–150.048 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 56.517 | 42.947 | 86.941 | 42.664–95.976 |
| J_simpleui_vos | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.687 | 16.310 | 87.538 | 13.372–102.461 |
| J_simpleui_vos | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.659 | 15.653 | 16.712 | 6.982–16.726 |
| J_simpleui_vos | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 11.438 | 10.479 | 26.538 | 10.140–26.641 |
| J_simpleui_vos | warm | hierarchical | 50 | close_book | PASS | 10 | 39.838 | 36.084 | 49.195 | 34.043–57.628 |
| J_simpleui_vos | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.648 | 16.618 | 16.686 | 16.616–16.708 |
| J_simpleui_vos | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.647 | 13.625 | 28.872 | 12.355–28.914 |
| J_simpleui_vos | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.764 | 32.692 | 32.858 | 32.486–33.012 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 16.040 | 7.412 | 26.751 | 7.047–27.009 |
| J_simpleui_vos | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 15.350 | 9.499 | 17.740 | 9.013–26.688 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book | PASS | 10 | 102.188 | 58.300 | 114.167 | 56.046–132.236 |
| J_simpleui_vos | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 51.666 | 41.553 | 66.877 | 38.578–86.853 |
| J_simpleui_vos | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.672 | 16.495 | 27.551 | 15.259–102.811 |
| J_simpleui_vos | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.662 | 15.663 | 16.726 | 7.012–16.742 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | home_to_library | PASS | 3 | 8.096 | 7.774 | 8.534 | 7.694–8.644 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | library_first_render | PASS | 3 | 28.503 | 24.208 | 28.627 | 23.134–28.658 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging | PASS | 30 | 132.243 | 130.379 | 137.161 | 118.511–257.853 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.130 | 15.133 | 16.560 | 5.223–126.151 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_first_render | PASS | 10 | 16.117 | 5.838 | 112.116 | 5.680–132.373 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging | PASS | 30 | 132.689 | 130.696 | 141.593 | 117.859–246.267 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | bookshelf_sequential_paging_anim_off | PASS | 30 | 16.042 | 13.822 | 16.268 | 7.986–139.691 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | change_sort_mode | PASS | 10 | 129.238 | 105.715 | 139.383 | 105.429–139.907 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_book | PASS | 10 | 126.232 | 117.875 | 292.676 | 117.569–314.486 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_bookshelf | PASS | 10 | 33.152 | 28.205 | 33.754 | 27.409–37.964 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | close_quick_settings | PASS | 10 | 16.662 | 16.628 | 16.689 | 16.623–16.705 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | home_to_library | PASS | 10 | 16.659 | 12.682 | 32.365 | 11.874–35.299 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_cached_paging | PASS | 30 | 13.883 | 11.706 | 34.673 | 10.867–47.023 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_first_render | PASS | 10 | 75.425 | 68.139 | 96.192 | 66.612–98.752 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_back | PASS | 10 | 77.737 | 53.340 | 87.313 | 51.746–87.478 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_folder_enter | PASS | 10 | 10.895 | 9.720 | 13.303 | 9.113–13.655 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | library_sequential_paging | PASS | 30 | 16.037 | 8.845 | 32.678 | 8.381–49.642 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book | PASS | 10 | 150.705 | 120.683 | 157.477 | 117.964–175.552 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_book_minimal | PASS | 10 | 86.698 | 67.052 | 105.408 | 65.745–126.550 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_bookshelf | PASS | 10 | 16.757 | 15.793 | 16.832 | 14.745–16.835 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | open_quick_settings | PASS | 10 | 16.645 | 15.766 | 61.777 | 8.409–460.077 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | repeated_nav | PASS | 2 | 825.035 | 778.316 | 871.755 | 766.636–883.435 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | start_to_home | PASS | 10 | 16.626 | 13.175 | 16.668 | 5.818–16.674 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging | PASS | 30 | 132.750 | 131.180 | 167.527 | 114.845–195.518 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_cached_paging_anim_off | PASS | 30 | 16.195 | 15.566 | 32.691 | 9.602–63.290 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_first_render | PASS | 10 | 16.151 | 14.794 | 57.984 | 13.998–64.796 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging | PASS | 6 | 132.704 | 132.296 | 140.999 | 132.114–149.245 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | bookshelf_sequential_paging_anim_off | PASS | 6 | 16.438 | 15.271 | 32.377 | 14.480–32.416 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | change_sort_mode | PASS | 10 | 31.513 | 21.946 | 34.761 | 20.783–35.275 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_book | PASS | 10 | 50.755 | 45.997 | 116.130 | 38.348–118.388 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_bookshelf | PASS | 10 | 33.139 | 32.861 | 33.225 | 32.129–33.245 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | close_quick_settings | PASS | 10 | 16.667 | 16.596 | 17.348 | 16.407–20.367 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | home_to_library | PASS | 10 | 16.656 | 12.677 | 30.058 | 11.753–30.158 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_cached_paging | PASS | 30 | 13.470 | 11.372 | 28.568 | 10.196–29.029 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_first_render | PASS | 10 | 37.204 | 32.715 | 43.106 | 32.661–47.468 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_back | PASS | 10 | 14.290 | 12.686 | 31.810 | 12.334–32.686 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_folder_enter | PASS | 10 | 11.588 | 10.321 | 23.853 | 10.128–29.329 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | library_sequential_paging | PASS | 5 | 11.016 | 10.948 | 26.995 | 10.929–32.035 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book | PASS | 10 | 111.672 | 97.816 | 131.466 | 94.470–153.518 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_book_minimal | PASS | 10 | 48.230 | 44.097 | 88.431 | 40.882–90.893 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_bookshelf | PASS | 10 | 16.791 | 16.418 | 16.916 | 14.948–17.012 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | open_quick_settings | PASS | 10 | 21.330 | 19.017 | 109.004 | 17.311–118.744 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | repeated_nav | PASS | 2 | 429.672 | 412.153 | 447.191 | 407.773–451.571 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | start_to_home | PASS | 10 | 16.640 | 14.100 | 16.685 | 7.938–16.692 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | bookshelf_first_render | PASS | 10 | 16.169 | 13.937 | 64.394 | 13.684–72.490 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | change_sort_mode | PASS | 10 | 18.176 | 17.327 | 33.448 | 17.224–49.975 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_book | PASS | 10 | 61.547 | 52.826 | 150.299 | 52.406–154.130 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_bookshelf | PASS | 10 | 31.443 | 30.193 | 32.694 | 29.255–33.579 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | close_quick_settings | PASS | 10 | 16.688 | 16.610 | 16.732 | 16.604–16.786 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | home_to_library | PASS | 10 | 16.648 | 12.807 | 29.267 | 12.370–29.392 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_first_render | PASS | 10 | 32.762 | 32.589 | 32.962 | 32.575–32.997 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_back | PASS | 10 | 15.755 | 7.382 | 28.256 | 6.109–28.328 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | library_folder_enter | PASS | 10 | 16.946 | 12.469 | 29.957 | 6.358–32.187 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book | PASS | 10 | 121.035 | 109.113 | 131.477 | 102.817–134.453 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_book_minimal | PASS | 10 | 68.947 | 49.729 | 92.440 | 45.612–94.032 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_bookshelf | PASS | 10 | 19.429 | 18.835 | 20.752 | 17.856–21.074 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | open_quick_settings | PASS | 10 | 16.683 | 16.095 | 105.796 | 14.415–110.483 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | start_to_home | PASS | 10 | 16.648 | 15.674 | 16.731 | 7.030–16.755 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | bookshelf_first_render | PASS | 10 | 16.223 | 15.095 | 57.307 | 14.389–61.963 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | change_sort_mode | PASS | 10 | 12.075 | 10.182 | 26.394 | 9.917–27.006 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_book | PASS | 10 | 38.859 | 37.262 | 45.894 | 36.362–47.444 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_bookshelf | PASS | 10 | 31.582 | 30.122 | 34.362 | 29.950–38.667 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | close_quick_settings | PASS | 10 | 16.654 | 16.116 | 17.169 | 11.621–21.455 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | home_to_library | PASS | 10 | 16.669 | 11.774 | 29.534 | 11.196–29.998 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_first_render | PASS | 10 | 32.748 | 32.657 | 32.853 | 32.545–32.957 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_back | PASS | 10 | 15.838 | 7.279 | 27.216 | 6.987–27.278 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | library_folder_enter | PASS | 10 | 14.631 | 9.877 | 17.742 | 8.514–26.995 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book | PASS | 10 | 91.880 | 56.733 | 118.265 | 55.214–121.861 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_book_minimal | PASS | 10 | 47.948 | 44.797 | 64.365 | 43.766–94.014 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_bookshelf | PASS | 10 | 17.509 | 16.653 | 20.423 | 16.368–20.791 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | open_quick_settings | PASS | 10 | 16.680 | 14.615 | 24.570 | 14.201–94.297 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | start_to_home | PASS | 10 | 16.675 | 15.704 | 16.721 | 7.402–16.730 |
| A_stock | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 11.005 | 11.005 | 11.005 | 11.005–11.005 |
| A_stock | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.149 | 16.149 | 16.149 | 16.149–16.149 |
| C_simpleui | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 9.591 | 9.591 | 9.591 | 9.591–9.591 |
| C_simpleui | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 30.849 | 30.849 | 30.849 | 30.849–30.849 |
| D_zenos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 31.901 | 31.901 | 31.901 | 31.901–31.901 |
| D_zenos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.573 | 16.573 | 16.573 | 16.573–16.573 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.699 | 8.699 | 8.699 | 8.699–8.699 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 21.782 | 21.782 | 21.782 | 21.782–21.782 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 31.586 | 31.586 | 31.586 | 31.586–31.586 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 16.692 | 16.692 | 16.692 | 16.692–16.692 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 7.703 | 7.703 | 7.703 | 7.703–7.703 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 20.443 | 20.443 | 20.443 | 20.443–20.443 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | home_to_library | PASS | 1 | 8.007 | 8.007 | 8.007 | 8.007–8.007 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | library_first_render | PASS | 1 | 27.715 | 27.715 | 27.715 | 27.715–27.715 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 212.764 | 211.393 | 213.331 | 211.050–213.473 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 244.599 | 243.549 | 244.956 | 243.287–245.046 |
| A_stock | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 248.429 | 247.558 | 248.768 | 247.340–248.853 |
| A_stock | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 257.336 | 256.352 | 257.386 | 256.106–257.398 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 178.272 | 177.069 | 196.593 | 176.768–201.173 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 211.089 | 209.588 | 224.624 | 209.213–228.008 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 214.706 | 213.294 | 228.248 | 212.941–231.633 |
| A_stock | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 223.060 | 221.746 | 236.830 | 221.418–240.273 |
| A_stock | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 259.868 | 259.868 | 259.868 | 259.868–259.868 |
| A_stock | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 3231.029 | 3231.029 | 3231.029 | 3231.029–3231.029 |
| A_stock | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 14946.035 | 14946.035 | 14946.035 | 14946.035–14946.035 |
| A_stock | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 14991.022 | 14991.022 | 14991.022 | 14991.022–14991.022 |
| A_stock | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 222.697 | 222.697 | 222.697 | 222.697–222.697 |
| A_stock | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1479.073 | 1479.073 | 1479.073 | 1479.073–1479.073 |
| A_stock | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 8733.744 | 8733.744 | 8733.744 | 8733.744–8733.744 |
| A_stock | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8755.334 | 8755.334 | 8755.334 | 8755.334–8755.334 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 215.222 | 215.222 | 215.222 | 215.222–215.222 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 818.259 | 818.259 | 818.259 | 818.259–818.259 |
| A_stock | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 4813.345 | 4813.345 | 4813.345 | 4813.345–4813.345 |
| A_stock | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 4827.355 | 4827.355 | 4827.355 | 4827.355–4827.355 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 266.878 | 266.878 | 266.878 | 266.878–266.878 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 858.965 | 858.965 | 858.965 | 858.965–858.965 |
| A_stock | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 4883.324 | 4883.324 | 4883.324 | 4883.324–4883.324 |
| A_stock | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 4895.957 | 4895.957 | 4895.957 | 4895.957–4895.957 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 324.629 | 321.743 | 325.590 | 321.022–325.830 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 363.113 | 362.902 | 364.349 | 362.849–364.658 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 371.038 | 370.645 | 372.152 | 370.546–372.430 |
| C_simpleui | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 382.052 | 381.435 | 383.184 | 381.281–383.467 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 284.098 | 274.173 | 294.772 | 271.692–297.440 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 327.595 | 315.563 | 341.559 | 312.554–345.050 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 335.053 | 322.871 | 349.221 | 319.825–352.763 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 345.969 | 333.942 | 360.682 | 330.935–364.360 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 383.038 | 383.038 | 383.038 | 383.038–383.038 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2100.831 | 2100.831 | 2100.831 | 2100.831–2100.831 |
| C_simpleui | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 21213.108 | 21213.108 | 21213.108 | 21213.108–21213.108 |
| C_simpleui | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 22336.903 | 22336.903 | 22336.903 | 22336.903–22336.903 |
| C_simpleui | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 343.798 | 343.798 | 343.798 | 343.798–343.798 |
| C_simpleui | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1681.726 | 1681.726 | 1681.726 | 1681.726–1681.726 |
| C_simpleui | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11954.499 | 11954.499 | 11954.499 | 11954.499–11954.499 |
| C_simpleui | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 12051.009 | 12051.009 | 12051.009 | 12051.009–12051.009 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 322.462 | 322.462 | 322.462 | 322.462–322.462 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1495.493 | 1495.493 | 1495.493 | 1495.493–1495.493 |
| C_simpleui | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 9920.724 | 9920.724 | 9920.724 | 9920.724–9920.724 |
| C_simpleui | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 9948.565 | 9948.565 | 9948.565 | 9948.565–9948.565 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 456.845 | 456.845 | 456.845 | 456.845–456.845 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1639.298 | 1639.298 | 1639.298 | 1639.298–1639.298 |
| C_simpleui | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9162.793 | 9162.793 | 9162.793 | 9162.793–9162.793 |
| C_simpleui | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9190.370 | 9190.370 | 9190.370 | 9190.370–9190.370 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 347.683 | 341.969 | 347.770 | 340.540–347.791 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 419.737 | 414.381 | 428.021 | 413.042–430.092 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 428.797 | 422.822 | 436.339 | 421.328–438.225 |
| D_zenos | first_run_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 441.395 | 435.043 | 448.595 | 433.455–450.394 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 293.044 | 289.083 | 317.730 | 288.092–323.902 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 346.646 | 333.358 | 373.810 | 330.036–380.601 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 354.417 | 340.868 | 381.759 | 337.481–388.595 |
| D_zenos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 366.723 | 353.194 | 394.470 | 349.812–401.406 |
| D_zenos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 348.252 | 348.252 | 348.252 | 348.252–348.252 |
| D_zenos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2357.530 | 2357.530 | 2357.530 | 2357.530–2357.530 |
| D_zenos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 10868.587 | 10868.587 | 10868.587 | 10868.587–10868.587 |
| D_zenos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 10886.562 | 10886.562 | 10886.562 | 10886.562–10886.562 |
| D_zenos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 335.324 | 335.324 | 335.324 | 335.324–335.324 |
| D_zenos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2154.302 | 2154.302 | 2154.302 | 2154.302–2154.302 |
| D_zenos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 9140.940 | 9140.940 | 9140.940 | 9140.940–9140.940 |
| D_zenos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9157.112 | 9157.112 | 9157.112 | 9157.112–9157.112 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 337.527 | 337.527 | 337.527 | 337.527–337.527 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2097.849 | 2097.849 | 2097.849 | 2097.849–2097.849 |
| D_zenos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 8171.103 | 8171.103 | 8171.103 | 8171.103–8171.103 |
| D_zenos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 8189.663 | 8189.663 | 8189.663 | 8189.663–8189.663 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 353.531 | 353.531 | 353.531 | 353.531–353.531 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2117.877 | 2117.877 | 2117.877 | 2117.877–2117.877 |
| D_zenos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 8071.783 | 8071.783 | 8071.783 | 8071.783–8071.783 |
| D_zenos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 8087.216 | 8087.216 | 8087.216 | 8087.216–8087.216 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 292.479 | 290.776 | 302.595 | 290.350–305.124 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 336.653 | 332.009 | 344.162 | 330.847–346.039 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 344.514 | 339.976 | 352.005 | 338.841–353.878 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 355.278 | 351.282 | 363.274 | 350.283–365.273 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 391.980 | 391.980 | 391.980 | 391.980–391.980 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2165.250 | 2165.250 | 2165.250 | 2165.250–2165.250 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 33641.728 | 33641.728 | 33641.728 | 33641.728–33641.728 |
| G_simpleui_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 35155.596 | 35155.596 | 35155.596 | 35155.596–35155.596 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 350.631 | 350.631 | 350.631 | 350.631–350.631 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1694.423 | 1694.423 | 1694.423 | 1694.423–1694.423 |
| G_simpleui_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 20327.486 | 20327.486 | 20327.486 | 20327.486–20327.486 |
| G_simpleui_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 20361.038 | 20361.038 | 20361.038 | 20361.038–20361.038 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 464.891 | 464.891 | 464.891 | 464.891–464.891 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1639.960 | 1639.960 | 1639.960 | 1639.960–1639.960 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 12346.878 | 12346.878 | 12346.878 | 12346.878–12346.878 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 12437.655 | 12437.655 | 12437.655 | 12437.655–12437.655 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 459.975 | 459.975 | 459.975 | 459.975–459.975 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1643.637 | 1643.637 | 1643.637 | 1643.637–1643.637 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10778.158 | 10778.158 | 10778.158 | 10778.158–10778.158 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10810.941 | 10810.941 | 10810.941 | 10810.941–10810.941 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 291.688 | 290.365 | 312.012 | 290.034–317.093 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 344.203 | 343.358 | 357.158 | 343.147–360.397 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 352.141 | 351.327 | 365.539 | 351.123–368.889 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 364.118 | 363.456 | 377.763 | 363.291–381.174 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 438.803 | 438.803 | 438.803 | 438.803–438.803 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2452.081 | 2452.081 | 2452.081 | 2452.081–2452.081 |
| H_zenos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 23951.203 | 23951.203 | 23951.203 | 23951.203–23951.203 |
| H_zenos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 23995.570 | 23995.570 | 23995.570 | 23995.570–23995.570 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 344.558 | 344.558 | 344.558 | 344.558–344.558 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2173.351 | 2173.351 | 2173.351 | 2173.351–2173.351 |
| H_zenos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 18459.180 | 18459.180 | 18459.180 | 18459.180–18459.180 |
| H_zenos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 18478.428 | 18478.428 | 18478.428 | 18478.428–18478.428 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 345.484 | 345.484 | 345.484 | 345.484–345.484 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2114.294 | 2114.294 | 2114.294 | 2114.294–2114.294 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 10169.927 | 10169.927 | 10169.927 | 10169.927–10169.927 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 10198.997 | 10198.997 | 10198.997 | 10198.997–10198.997 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 348.413 | 348.413 | 348.413 | 348.413–348.413 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 2113.843 | 2113.843 | 2113.843 | 2113.843–2113.843 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9951.956 | 9951.956 | 9951.956 | 9951.956–9951.956 |
| H_zenos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9979.176 | 9979.176 | 9979.176 | 9979.176–9979.176 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 276.499 | 274.511 | 298.589 | 274.014–304.111 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 312.267 | 311.248 | 338.419 | 310.993–344.958 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 319.625 | 318.850 | 345.597 | 318.657–352.090 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 331.950 | 330.823 | 357.154 | 330.541–363.455 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 390.701 | 390.701 | 390.701 | 390.701–390.701 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2147.797 | 2147.797 | 2147.797 | 2147.797–2147.797 |
| J_simpleui_vos | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 23703.655 | 23703.655 | 23703.655 | 23703.655–23703.655 |
| J_simpleui_vos | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 23757.541 | 23757.541 | 23757.541 | 23757.541–23757.541 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 369.590 | 369.590 | 369.590 | 369.590–369.590 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1612.179 | 1612.179 | 1612.179 | 1612.179–1612.179 |
| J_simpleui_vos | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 11761.108 | 11761.108 | 11761.108 | 11761.108–11761.108 |
| J_simpleui_vos | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 11791.595 | 11791.595 | 11791.595 | 11791.595–11791.595 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 333.389 | 333.389 | 333.389 | 333.389–333.389 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1512.278 | 1512.278 | 1512.278 | 1512.278–1512.278 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 10326.040 | 10326.040 | 10326.040 | 10326.040–10326.040 |
| J_simpleui_vos | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 10355.269 | 10355.269 | 10355.269 | 10355.269–10355.269 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 335.605 | 335.605 | 335.605 | 335.605–335.605 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1517.129 | 1517.129 | 1517.129 | 1517.129–1517.129 |
| J_simpleui_vos | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 9111.481 | 9111.481 | 9111.481 | 9111.481–9111.481 |
| J_simpleui_vos | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 9139.857 | 9139.857 | 9139.857 | 9139.857–9139.857 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 3 | 282.527 | 282.123 | 305.183 | 282.022–310.847 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 3 | 329.237 | 328.312 | 344.824 | 328.080–348.721 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:complete_marker_ms | PASS | 3 | 337.195 | 336.132 | 352.447 | 335.866–356.260 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 3 | 347.799 | 347.306 | 363.546 | 347.182–367.483 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 386.887 | 386.887 | 386.887 | 386.887–386.887 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 2165.293 | 2165.293 | 2165.293 | 2165.293–2165.293 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:complete_marker_ms | PASS | 1 | 36187.404 | 36187.404 | 36187.404 | 36187.404–36187.404 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 78554.194 | 78554.194 | 78554.194 | 78554.194–78554.194 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 342.612 | 342.612 | 342.612 | 342.612–342.612 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1594.492 | 1594.492 | 1594.492 | 1594.492–1594.492 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:complete_marker_ms | PASS | 1 | 19291.566 | 19291.566 | 19291.566 | 19291.566–19291.566 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 19400.516 | 19400.516 | 19400.516 | 19400.516–19400.516 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 333.750 | 333.750 | 333.750 | 333.750–333.750 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 1513.251 | 1513.251 | 1513.251 | 1513.251–1513.251 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 11913.679 | 11913.679 | 11913.679 | 11913.679–11913.679 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 11990.302 | 11990.302 | 11990.302 | 11990.302–11990.302 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_ui_ready_ms | PASS | 1 | 454.667 | 454.667 | 454.667 | 454.667–454.667 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_library_ready_ms | PASS | 1 | 1636.771 | 1636.771 | 1636.771 | 1636.771–1636.771 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:complete_marker_ms | PASS | 1 | 10835.879 | 10835.879 | 10835.879 | 10835.879–10835.879 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | process:spawn_to_process_exit_ms | PASS | 1 | 10866.255 | 10866.255 | 10866.255 | 10866.255–10866.255 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 213.597 | 213.597 | 213.597 | 213.597–213.597 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 245.498 | 245.498 | 245.498 | 245.498–245.498 |
| A_stock | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 249.253 | 249.253 | 249.253 | 249.253–249.253 |
| A_stock | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 257.914 | 257.914 | 257.914 | 257.914–257.914 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 331.091 | 331.091 | 331.091 | 331.091–331.091 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 378.581 | 378.581 | 378.581 | 378.581–378.581 |
| C_simpleui | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 385.725 | 385.725 | 385.725 | 385.725–385.725 |
| C_simpleui | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 396.617 | 396.617 | 396.617 | 396.617–396.617 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 336.665 | 336.665 | 336.665 | 336.665–336.665 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 413.084 | 413.084 | 413.084 | 413.084–413.084 |
| D_zenos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 421.480 | 421.480 | 421.480 | 421.480–421.480 |
| D_zenos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 433.719 | 433.719 | 433.719 | 433.719–433.719 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 348.981 | 348.981 | 348.981 | 348.981–348.981 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 387.620 | 387.620 | 387.620 | 387.620–387.620 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 395.229 | 395.229 | 395.229 | 395.229–395.229 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 406.615 | 406.615 | 406.615 | 406.615–406.615 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 344.454 | 344.454 | 344.454 | 344.454–344.454 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 415.318 | 415.318 | 415.318 | 415.318–415.318 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 423.994 | 423.994 | 423.994 | 423.994–423.994 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 436.742 | 436.742 | 436.742 | 436.742–436.742 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 325.046 | 325.046 | 325.046 | 325.046–325.046 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 362.389 | 362.389 | 362.389 | 362.389–362.389 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 370.334 | 370.334 | 370.334 | 370.334–370.334 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 381.038 | 381.038 | 381.038 | 381.038–381.038 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_ui_ready_ms | PASS | 1 | 352.691 | 352.691 | 352.691 | 352.691–352.691 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_library_ready_ms | PASS | 1 | 397.475 | 397.475 | 397.475 | 397.475–397.475 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:complete_marker_ms | PASS | 1 | 405.498 | 405.498 | 405.498 | 405.498–405.498 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | process:spawn_to_process_exit_ms | PASS | 1 | 416.436 | 416.436 | 416.436 | 416.436–416.436 |

## Memory Checkpoints

| Stack | Mode | Dataset | Books | Checkpoint | Status | Processes | n | Forced-GC Live Heap Median KiB | p90 KiB | Min–max KiB | Natural Heap Median KiB | RSS Median KiB |
|:--|:--|:--|--:|:--|:--|--:|--:|--:|--:|:--|--:|--:|
| A_stock | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8323.392 | 8347.670 | 8316.677–8353.739 | 14544.121 | 85088.000 |
| A_stock | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8462.380 | 8489.571 | 8454.599–8496.368 | 9199.490 | 85088.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 8292.806 | 8316.031 | 8219.849–8321.837 | 12694.335 | 79568.000 |
| A_stock | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 8341.692 | 8371.083 | 8223.634–8378.431 | 9030.630 | 79600.000 |
| A_stock | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 10945.993 | 10945.993 | 10945.993–10945.993 | 16850.085 | 87760.000 |
| A_stock | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 27633.755 | 27633.755 | 27633.755–27633.755 | 38440.197 | 197264.000 |
| A_stock | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 22918.254 | 22918.254 | 22918.254–22918.254 | 26191.100 | 215312.000 |
| A_stock | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 8679.923 | 8679.923 | 8679.923–8679.923 | 15177.404 | 85232.000 |
| A_stock | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 26820.411 | 26820.411 | 26820.411–26820.411 | 33657.765 | 138928.000 |
| A_stock | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 15705.820 | 15705.820 | 15705.820–15705.820 | 21378.786 | 180704.000 |
| A_stock | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8339.442 | 8339.442 | 8339.442–8339.442 | 14888.583 | 85280.000 |
| A_stock | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8369.079 | 8369.079 | 8369.079–8369.079 | 8380.610 | 88736.000 |
| A_stock | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 13896.415 | 13896.415 | 13896.415–13896.415 | 18508.436 | 111616.000 |
| A_stock | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 8371.622 | 8371.622 | 8371.622–8371.622 | 14707.821 | 85136.000 |
| A_stock | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 8310.833 | 8310.833 | 8310.833–8310.833 | 8322.364 | 88400.000 |
| A_stock | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 11694.364 | 11694.364 | 11694.364–11694.364 | 19573.048 | 114976.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14055.975 | 14071.046 | 14049.592–14074.814 | 16044.392 | 95776.000 |
| C_simpleui | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14282.932 | 14430.610 | 14232.135–14467.529 | 15657.621 | 96112.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14052.436 | 14054.826 | 14016.061–14055.424 | 21165.173 | 90736.000 |
| C_simpleui | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14211.479 | 14275.910 | 14196.256–14292.018 | 15563.988 | 91152.000 |
| C_simpleui | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16439.010 | 16439.010 | 16439.010–16439.010 | 23225.357 | 96400.000 |
| C_simpleui | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 25517.334 | 25517.334 | 25517.334–25517.334 | 32029.311 | 117632.000 |
| C_simpleui | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 104347.693 | 104347.693 | 104347.693–104347.693 | 105487.812 | 234160.000 |
| C_simpleui | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14404.643 | 14404.643 | 14404.643–14404.643 | 17589.495 | 94752.000 |
| C_simpleui | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 17516.963 | 17516.963 | 17516.963–17516.963 | 19995.403 | 107120.000 |
| C_simpleui | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 57699.033 | 57699.033 | 57699.033–57699.033 | 58307.779 | 185712.000 |
| C_simpleui | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14084.756 | 14084.756 | 14084.756–14084.756 | 15862.862 | 95840.000 |
| C_simpleui | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14373.811 | 14373.811 | 14373.811–14373.811 | 15642.940 | 96496.000 |
| C_simpleui | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 51511.979 | 51511.979 | 51511.979–51511.979 | 55394.377 | 176064.000 |
| C_simpleui | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14176.475 | 14176.475 | 14176.475–14176.475 | 15039.051 | 95936.000 |
| C_simpleui | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14326.553 | 14326.553 | 14326.553–14326.553 | 15589.918 | 97648.000 |
| C_simpleui | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 50729.389 | 50729.389 | 50729.389–50729.389 | 54629.553 | 173072.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14457.232 | 14528.907 | 14400.674–14546.826 | 19089.411 | 94000.000 |
| D_zenos | first_run_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15621.369 | 15681.991 | 15595.076–15697.146 | 17080.789 | 99696.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14442.147 | 14504.729 | 14410.976–14520.374 | 23534.343 | 94448.000 |
| D_zenos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15331.964 | 15621.042 | 15328.175–15693.312 | 16440.346 | 96992.000 |
| D_zenos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 15996.390 | 15996.390 | 15996.390–15996.390 | 24853.164 | 98480.000 |
| D_zenos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 24870.007 | 24870.007 | 24870.007–24870.007 | 28640.221 | 128608.000 |
| D_zenos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 23687.539 | 23687.539 | 23687.539–23687.539 | 23710.520 | 170176.000 |
| D_zenos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14444.979 | 14444.979 | 14444.979–14444.979 | 19658.855 | 93968.000 |
| D_zenos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 18805.089 | 18805.089 | 18805.089–18805.089 | 27413.640 | 121872.000 |
| D_zenos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 18447.031 | 18447.031 | 18447.031–18447.031 | 18471.105 | 162128.000 |
| D_zenos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14459.607 | 14459.607 | 14459.607–14459.607 | 18945.804 | 93872.000 |
| D_zenos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 16396.562 | 16396.562 | 16396.562–16396.562 | 23224.649 | 121296.000 |
| D_zenos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 20810.215 | 20810.215 | 20810.215–20810.215 | 32683.393 | 158720.000 |
| D_zenos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14508.611 | 14508.611 | 14508.611–14508.611 | 19390.630 | 93792.000 |
| D_zenos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14916.726 | 14916.726 | 14916.726–14916.726 | 31790.550 | 118752.000 |
| D_zenos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 17938.031 | 17938.031 | 17938.031–17938.031 | 30622.690 | 155856.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14437.183 | 14485.989 | 14406.229–14498.190 | 22147.552 | 93136.000 |
| G_simpleui_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14662.124 | 14710.818 | 14635.968–14722.991 | 15807.411 | 93808.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17044.006 | 17044.006 | 17044.006–17044.006 | 28433.340 | 101824.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 25990.002 | 25990.002 | 25990.002–25990.002 | 32939.499 | 120928.000 |
| G_simpleui_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 110317.319 | 110317.319 | 110317.319–110317.319 | 111718.955 | 281616.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15048.752 | 15048.752 | 15048.752–15048.752 | 19173.194 | 95232.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 18097.107 | 18097.107 | 18097.107–18097.107 | 20602.268 | 107984.000 |
| G_simpleui_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 59944.643 | 59944.643 | 59944.643–59944.643 | 60711.518 | 221744.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14706.666 | 14706.666 | 14706.666–14706.666 | 18542.476 | 95552.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14893.885 | 14893.885 | 14893.885–14893.885 | 16090.049 | 96240.000 |
| G_simpleui_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 58636.063 | 58636.063 | 58636.063–58636.063 | 62371.241 | 222816.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14764.818 | 14764.818 | 14764.818–14764.818 | 17345.985 | 95440.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14998.100 | 14998.100 | 14998.100–14998.100 | 16242.224 | 97184.000 |
| G_simpleui_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 54423.989 | 54423.989 | 54423.989–54423.989 | 58068.264 | 199632.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14834.195 | 14856.848 | 14827.211–14862.512 | 24454.200 | 95488.000 |
| H_zenos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15814.562 | 15826.406 | 15686.898–15829.367 | 16834.949 | 97936.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 16737.198 | 16737.198 | 16737.198–16737.198 | 27057.558 | 100880.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 25520.171 | 25520.171 | 25520.171–25520.171 | 29046.603 | 130672.000 |
| H_zenos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 28296.063 | 28296.063 | 28296.063–28296.063 | 28886.636 | 224880.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15187.886 | 15187.886 | 15187.886–15187.886 | 19439.174 | 96880.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 19480.050 | 19480.050 | 19480.050–19480.050 | 36835.564 | 125104.000 |
| H_zenos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 21631.238 | 21631.238 | 21631.238–21631.238 | 22212.933 | 204608.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15153.881 | 15153.881 | 15153.881–15153.881 | 20856.467 | 94368.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 17166.011 | 17166.011 | 17166.011–17166.011 | 36142.214 | 123552.000 |
| H_zenos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 50023.061 | 50023.061 | 50023.061–50023.061 | 65933.854 | 211136.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 15077.369 | 15077.369 | 15077.369–15077.369 | 21242.403 | 94592.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15520.644 | 15520.644 | 15520.644–15520.644 | 32535.895 | 119856.000 |
| H_zenos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 44689.838 | 44689.838 | 44689.838–44689.838 | 52286.660 | 197872.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14531.749 | 14550.546 | 14477.390–14555.245 | 21638.643 | 91424.000 |
| J_simpleui_vos | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 14665.874 | 14688.027 | 14664.499–14693.565 | 15761.315 | 91808.000 |
| J_simpleui_vos | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 17354.179 | 17354.179 | 17354.179–17354.179 | 23280.951 | 96448.000 |
| J_simpleui_vos | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 28126.140 | 28126.140 | 28126.140–28126.140 | 41950.434 | 132016.000 |
| J_simpleui_vos | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 124627.612 | 124627.612 | 124627.612–124627.612 | 128246.190 | 267424.000 |
| J_simpleui_vos | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 14845.339 | 14845.339 | 14845.339–14845.339 | 16517.598 | 96144.000 |
| J_simpleui_vos | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 15894.882 | 15894.882 | 15894.882–15894.882 | 19886.687 | 105008.000 |
| J_simpleui_vos | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 58867.116 | 58867.116 | 58867.116–58867.116 | 59789.953 | 198672.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14552.335 | 14552.335 | 14552.335–14552.335 | 16858.465 | 95728.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14923.253 | 14923.253 | 14923.253–14923.253 | 16038.346 | 96384.000 |
| J_simpleui_vos | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 58260.675 | 58260.675 | 58260.675–58260.675 | 67381.545 | 179936.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 14543.218 | 14543.218 | 14543.218–14543.218 | 15762.088 | 96592.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 14921.452 | 14921.452 | 14921.452–14921.452 | 15971.516 | 97040.000 |
| J_simpleui_vos | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 53062.323 | 53062.323 | 53062.323–53062.323 | 62205.559 | 174704.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_init_idle | PASS | 3 | 3 | 14998.422 | 14999.656 | 14994.824–14999.965 | 23189.525 | 92992.000 |
| K_simpleui_vos_bookshelf | steady_state_cold | hierarchical | 2000 | post_library_render_idle | PASS | 3 | 3 | 15106.637 | 15107.565 | 15098.793–15107.797 | 16244.709 | 93280.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_init_idle | PASS | 1 | 1 | 18052.042 | 18052.042 | 18052.042–18052.042 | 28055.468 | 100896.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_library_render_idle | PASS | 1 | 1 | 28593.726 | 28593.726 | 28593.726–28593.726 | 42411.516 | 134736.000 |
| K_simpleui_vos_bookshelf | warm | flat | 2000 | post_stress_idle | PASS | 1 | 1 | 130685.906 | 130685.906 | 130685.906–130685.906 | 133812.256 | 311136.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_init_idle | PASS | 1 | 1 | 15469.550 | 15469.550 | 15469.550–15469.550 | 18189.979 | 95648.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_library_render_idle | PASS | 1 | 1 | 16460.229 | 16460.229 | 16460.229–16460.229 | 20475.312 | 104544.000 |
| K_simpleui_vos_bookshelf | warm | flat | 50 | post_stress_idle | PASS | 1 | 1 | 62317.585 | 62317.585 | 62317.585–62317.585 | 63114.481 | 217760.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15254.847 | 15254.847 | 15254.847–15254.847 | 19759.543 | 95392.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15481.565 | 15481.565 | 15481.565–15481.565 | 16437.693 | 97472.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 2000 | post_stress_idle | PASS | 1 | 1 | 64961.451 | 64961.451 | 64961.451–64961.451 | 74102.373 | 219600.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_init_idle | PASS | 1 | 1 | 15190.144 | 15190.144 | 15190.144–15190.144 | 17776.092 | 96160.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_library_render_idle | PASS | 1 | 1 | 15432.464 | 15432.464 | 15432.464–15432.464 | 16541.731 | 96832.000 |
| K_simpleui_vos_bookshelf | warm | hierarchical | 50 | post_stress_idle | PASS | 1 | 1 | 56692.994 | 56692.994 | 56692.994–56692.994 | 65487.757 | 201360.000 |
| A_stock | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 8431.747 | 8431.747 | 8431.747–8431.747 | 14842.839 | 85376.000 |
| A_stock | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 8568.454 | 8568.454 | 8568.454–8568.454 | 9240.169 | 85408.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14117.404 | 14117.404 | 14117.404–14117.404 | 15762.684 | 96176.000 |
| C_simpleui | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14284.713 | 14284.713 | 14284.713–14284.713 | 15718.177 | 96544.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14420.916 | 14420.916 | 14420.916–14420.916 | 19110.471 | 94720.000 |
| D_zenos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15618.307 | 15618.307 | 15618.307–15618.307 | 16996.181 | 100544.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14710.412 | 14710.412 | 14710.412–14710.412 | 17785.173 | 95616.000 |
| G_simpleui_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14828.502 | 14828.502 | 14828.502–14828.502 | 16134.538 | 95712.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15033.498 | 15033.498 | 15033.498–15033.498 | 21175.195 | 94352.000 |
| H_zenos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 16237.264 | 16237.264 | 16237.264–16237.264 | 17669.559 | 100128.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 14604.229 | 14604.229 | 14604.229–14604.229 | 23653.021 | 96448.000 |
| J_simpleui_vos | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 14717.581 | 14717.581 | 14717.581–14717.581 | 15977.351 | 96624.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_init_idle | PASS | 1 | 1 | 15223.187 | 15223.187 | 15223.187–15223.187 | 19038.271 | 96240.000 |
| K_simpleui_vos_bookshelf | steady_init | hierarchical | 2000 | post_library_render_idle | PASS | 1 | 1 | 15298.753 | 15298.753 | 15298.753–15298.753 | 16513.693 | 96608.000 |

## Data-derived comparisons

- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 15.993 ms vs 23.340 ms (31.5% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 13.546 ms vs 20.224 ms (33.0% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 14.595 ms vs 17.636 ms (17.2% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 11.407 ms vs 149.326 ms (92.4% lower) (UX-level comparison: books/page differs, 9.000 vs 10.000).
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 2000 books): 14.096 ms vs 23.340 ms (39.6% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 2000 books): 15.954 ms vs 20.224 ms (21.1% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_cached_paging` (warm, flat, 50 books): 16.071 ms vs 17.636 ms (8.9% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `A_stock` for `library_sequential_paging` (warm, flat, 50 books): 14.907 ms vs 149.326 ms (90.0% lower) (UX-level comparison: books/page differs, 5.000 vs 10.000).
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 2000 books): 15.274 ms vs 15.993 ms (4.5% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 13.546 ms vs 15.121 ms (10.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `G_simpleui_bookshelf` for `library_cached_paging` (warm, flat, 50 books): 14.595 ms vs 15.842 ms (7.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `G_simpleui_bookshelf` has a lower descriptive median than `C_simpleui` for `library_sequential_paging` (warm, flat, 50 books): 10.995 ms vs 11.407 ms (3.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 14.096 ms vs 15.323 ms (8.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `D_zenos` has a lower descriptive median than `H_zenos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 15.954 ms vs 16.023 ms (0.4% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_cached_paging` (warm, flat, 50 books): 14.253 ms vs 16.071 ms (11.3% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `H_zenos_bookshelf` has a lower descriptive median than `D_zenos` for `library_sequential_paging` (warm, flat, 50 books): 13.257 ms vs 14.907 ms (11.1% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 2000 books): 13.181 ms vs 15.993 ms (17.6% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 2000 books): 13.546 ms vs 14.139 ms (4.2% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `C_simpleui` for `library_cached_paging` (warm, flat, 50 books): 13.566 ms vs 14.595 ms (7.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `C_simpleui` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 11.407 ms vs 11.965 ms (4.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_cached_paging` (warm, flat, 2000 books): 13.181 ms vs 13.883 ms (5.0% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `J_simpleui_vos` has a lower descriptive median than `K_simpleui_vos_bookshelf` for `library_sequential_paging` (warm, flat, 2000 books): 14.139 ms vs 16.037 ms (11.8% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_cached_paging` (warm, flat, 50 books): 13.470 ms vs 13.566 ms (0.7% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.
- `K_simpleui_vos_bookshelf` has a lower descriptive median than `J_simpleui_vos` for `library_sequential_paging` (warm, flat, 50 books): 11.016 ms vs 11.965 ms (7.9% lower). Distributions overlap within [p10, p90]; differences are not statistically definitive under this workload.

## Interpretation limits

These are descriptive local-emulator medians, not significance claims or physical-Kindle latency estimates. Differences where distributions substantially overlap are reported as descriptive run medians rather than definitive superiority. No universal winner is selected.
