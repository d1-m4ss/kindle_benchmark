# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[8.053,7.819,7.318,8.577,6.857,8.322,7.559,8.223,7.71,21.182,7.109,8.124,7.676,8.505,7.976,7.919,7.54,8.141,7.165,8.428,18.405,6.52,7.967,7.873,17.511,6.721,8.958,6.842,17.289,7.713]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_unit': 'milliseconds', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)'}`

Raw samples (30):

```json
[15.474,17.978,16.188,19.958,18.348,17.75,19.206,35.199,19.341,21.746,17.857,21.436,30.945,22.187,19.37,18.405,18.952,32.24,14.018,13.458,11.978,12.049,11.944,14.183,22.52,13.901,14.264,14.443,11.253,13.337]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[13.859,13.524,23.251,16.79,19.054,18.762,17.113,18.585,15.481,16.445,26.786,21.279,17.576,19.734,24.576,20.385,19.834,19.529,27.161,21.532,19.781,21.684,19.902,27.146,18.954,20.754,23.211,19.407,28.721,21.253]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=18.002 ms, full median=17.691 ms, delta=-0.311 ms, relative=-1.728%
