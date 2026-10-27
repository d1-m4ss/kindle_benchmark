# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False, 'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)'}`

Raw samples (30):

```json
[16.701,16.082,16.178,28.358,7.206,12.687,16.091,16.104,16.088,16.095,26.443,9.044,12.839,16.037,16.103,25.305,6.912,16.131,16.091,16.083,26.666,6.661,14.981,16.153,16.04,26.658,6.821,14.868,16.198,16.061]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[16.639,16.156,28.436,9.745,10.466,16.008,16.194,16.154,16.195,16.135,27.596,11.592,9.387,16.122,16.234,27.617,9.34,11.56,16.06,16.169,26.929,10.733,10.849,16.197,16.165,27.711,9.292,11.581,16.095,16.111]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False, 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds'}`

Raw samples (30):

```json
[14.836,25.835,17.68,20.9,18.613,16.171,16.655,15.545,18.51,26.788,17.252,20.359,18.446,17.986,29.135,22.4,21.422,19.263,27.551,19.16,21.018,22.428,28.772,17.735,21.614,20.177,21.288,31.433,20.559,21.145]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=15.455 ms, full median=15.168 ms, delta=-0.287 ms, relative=-1.860%
