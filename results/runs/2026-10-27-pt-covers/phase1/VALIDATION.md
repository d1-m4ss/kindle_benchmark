# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds', 'integer_rounding': False}`

Raw samples (30):

```json
[16.666,16.087,16.095,29.494,6.394,12.506,16.137,16.114,16.148,16.104,28.213,5.777,14.38,16.112,16.12,29.187,7.203,12.02,16.117,16.168,28.435,7.602,12.374,16.115,16.12,27.502,6.157,14.767,16.118,16.122]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds'}`

Raw samples (30):

```json
[16.692,16.042,30.867,10.774,9.02,13.882,16.133,16.091,16.143,16.097,29.705,11.037,7.752,15.959,16.16,28.808,8.04,11.603,16.058,16.12,28.927,9.087,10.468,16.115,16.035,28.83,8.992,10.541,16.133,16.13]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'source': 'clock_gettime(CLOCK_MONOTONIC)', 'integer_rounding': False, 'raw_unit': 'milliseconds', 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[15.694,27.703,17.798,21.139,30.779,26.802,18.961,30.19,17.825,22.509,19.227,16.852,28.529,22.021,20.896,23.915,22.805,30.576,21.4,21.042,20.532,19.809,34.969,20.41,24.989,24.451,19.161,34.722,24.41,22.182]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=17.687 ms, full median=15.281 ms, delta=-2.406 ms, relative=-13.603%
