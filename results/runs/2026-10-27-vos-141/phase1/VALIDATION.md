# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False}`

Raw samples (30):

```json
[16.65,16.087,16.145,27.899,6.428,14,16.14,16.14,16.097,16.063,25.929,6.43,15.943,16.131,16.084,25.432,7.525,15.389,16.106,16.111,26.277,7.755,14.284,16.094,16.091,26.19,7.593,14.495,16.116,16.075]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False}`

Raw samples (30):

```json
[15.359,16.185,28.469,10.99,9.241,15.943,16.102,16.108,16.182,16.155,28.816,10.775,9.446,15.638,16.182,26.87,6.974,14.605,16.185,16.175,28.036,10.917,9.809,15.918,16.183,26.749,10.114,12.016,15.845,16.134]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[17.762,15.155,16.628,17.37,20.865,17.565,17.346,16.794,17.055,27.936,18.823,20.773,25.33,26.328,17.873,25.09,21.596,26.172,18.87,22.991,18.757,20.651,19.87,31.201,19.744,22.343,19.496,17.564,28.353,18.255]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=16.478 ms, full median=16.061 ms, delta=-0.417 ms, relative=-2.534%
