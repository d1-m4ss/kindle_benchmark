# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)'}`

Raw samples (30):

```json
[16.617,16.134,16.129,28.136,7.804,12.362,16.13,16.094,16.127,16.113,26.465,8.988,12.898,16.145,16.084,25.626,6.714,16.007,16.135,16.038,25.989,8.832,13.573,16.048,16.118,26.309,6.818,15.295,16.092,16.142]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds'}`

Raw samples (30):

```json
[16.629,29.127,7.618,11.673,16.152,16.152,16.152,16.133,16.197,16.142,28.211,13.757,9.25,13.425,15.938,26.916,9.005,12.448,16.136,16.135,26.896,10.905,10.928,15.941,16.131,26.835,11.783,11.99,13.944,16.122]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'raw_unit': 'milliseconds', 'integer_rounding': False}`

Raw samples (30):

```json
[17.887,27.113,16.596,24.426,22.003,17.199,20.48,20.038,29.114,23.241,21.484,23.465,34.222,20.155,24.97,24.535,21.224,31.282,21.977,21.029,23.374,25.136,35.84,25.8,22.606,22.905,32.89,23.349,23.337,24.699]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=16.771 ms, full median=18.407 ms, delta=1.637 ms, relative=9.758%
