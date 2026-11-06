# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False}`

Raw samples (30):

```json
[16.648,16.115,16.177,16.053,28.476,4.439,15.257,16.124,16.022,15.984,26.2,5.895,16.045,16.101,16.082,25.764,6.309,16.095,16.058,16.161,26.558,5.563,15.94,16.128,16.048,26.583,5.628,16.026,16.115,16.034]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds', 'integer_rounding': False}`

Raw samples (30):

```json
[16.641,16.176,28.8,12.344,8.825,14.679,16.155,16.164,16.193,16.07,28.208,13.022,7.729,15.716,16.162,26.491,9.073,13.688,15.334,16.146,26.221,10.201,12.101,16.228,16.136,26.331,8.353,13.748,16.163,16.18]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False}`

Raw samples (30):

```json
[16.36,26.421,16.336,18.434,20.202,17.727,17.926,18.441,15.764,27.898,19.466,17.603,17.673,18.653,27.778,20.886,21.331,21.294,29.566,22.132,18.134,21.802,28.587,18.67,19.63,21.008,21.41,21.97,30.059,21.012]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=16.937 ms, full median=15.602 ms, delta=-1.335 ms, relative=-7.879%
