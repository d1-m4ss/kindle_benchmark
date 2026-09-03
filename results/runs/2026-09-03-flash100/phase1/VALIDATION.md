# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_page` / `library_cached_paging`

Timer: `{'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)'}`

Raw samples (30):

```json
[110.061,110.529,111.941,112.04,125.201,111.948,110.632,113.805,111.497,124.771,110.24,111.406,111.075,110.87,125.16,110.945,110.483,109.604,110.851,125.074,110.34,111.835,111.76,109.345,125.748,112.349,110.888,110.123,113.214,124.395]
```

## `precision_simpleui_page` / `library_cached_paging`

Timer: `{'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds'}`

Raw samples (30):

```json
[114.337,114.345,112.644,113.911,126.701,115.165,113.421,114.886,113.876,127.699,114.201,113.614,114.992,115.27,125.589,114.39,113.522,114.319,114.197,127.956,115.767,115.527,115.052,113.868,125.403,115.616,114.186,116.394,114.668,127.492]
```

## `precision_stock_page` / `library_cached_paging`

Timer: `{'raw_unit': 'milliseconds', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'integer_rounding': False}`

Raw samples (30):

```json
[125.563,117.251,118.315,117.104,117.115,124.756,115.06,115.356,114.981,115.705,123.312,115.572,116.288,115.291,113.589,121.322,117.138,115.167,116.96,116.29,122.838,117.894,116.501,116.865,115.918,122.566,114.546,117.096,116.255,116.821]
```

## Instrumentation overhead

- `library_sequential_paging`: n=30, minimal median=117.349 ms, full median=117.501 ms, delta=0.151 ms, relative=0.129%
