# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False}`

Raw samples (30):

```json
[12.831,10.794,31.347,12.601,9.673,10.382,10.774,14.058,11.798,8.781,10.923,11.379,11.746,30.146,12.985,8.77,12.123,11.434,29.069,10.804,11.035,28.559,10.393,10.217,13.939,27.888,12.127,9.21,9.998,11.526]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[24.624,27.409,25.417,28.836,27.882,46.64,25.849,26.901,27.753,48.238,28.782,30.437,27.809,51.97,24.817,26.957,18.016,24.202,18.259,21.121,35.03,24.021,20.655,19.398,16.358,18.735,39.386,20.185,18.552,20.982]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)'}`

Raw samples (30):

```json
[24.149,23.538,21.64,27.147,24.43,23.843,25.48,41.174,25.931,30.988,53.505,29.267,28.775,28.163,42.156,27.735,30.02,32.071,27.981,30.615,40.821,32.533,30.225,31.267,28.447,47.129,28.239,32.675,31.891,46.321]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=28.410 ms, full median=27.994 ms, delta=-0.416 ms, relative=-1.464%
