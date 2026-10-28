# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[16.657,28.39,6.005,14.012,15.807,16.199,16.001,16.076,16.094,16.053,29.597,8.524,10.281,16.001,16.158,28.107,5.471,14.655,16.035,16.103,28.003,6.531,13.895,16.105,16.169,26.638,6.747,14.951,16.164,16.086]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'integer_rounding': False, 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[16.647,28.645,8.76,12.674,14.615,16.124,16.179,16.202,16.137,16.168,28.286,10.694,10.114,15.394,16.168,29.029,9.483,10.635,15.532,16.102,26.819,10.806,10.833,16.161,16.151,26.295,7.688,14.487,16.216,16.139]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'source': 'clock_gettime(CLOCK_MONOTONIC)', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'raw_unit': 'milliseconds'}`

Raw samples (30):

```json
[18.347,18.428,17.437,18.542,17.6,17.483,22.488,18.361,27.667,16.123,18.785,19.611,21.935,25.591,19.57,22.615,21.101,21.609,28.089,20.263,22.071,21.965,29.9,18.933,20.63,21.861,21.475,34.502,21.383,18.354]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=15.850 ms, full median=15.607 ms, delta=-0.243 ms, relative=-1.536%
