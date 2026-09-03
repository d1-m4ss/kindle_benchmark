# Benchmark validation

Generated only from schema-v2 raw results.

## `precision_zenos_start` / `start_to_home`

Timer: `{'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds'}`

Raw samples (20):

```json
[11.683,12.571,13.32,15.628,27.562,25.825,13.035,11.936,12.207,12.869,28.698,15.682,26.883,12.866,11.856,38.135,12.61,30.597,13.09,11.688]
```

## `precision_simpleui_start` / `start_to_home`

Timer: `{'raw_unit': 'milliseconds', 'integer_rounding': False, 'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)'}`

Raw samples (20):

```json
[0.069,0.013,0.082,0.084,0.024,0.058,0.04,0.022,0.009,0.072,0.053,0.008,0.032,0.051,0.066,0.029,0.005,0.051,0.008,0.003]
```

## `precision_stock_page` / `library_next_page`

Timer: `{'raw_resolution': 'microsecond representation (time.to_us / 1000)', 'source': 'clock_gettime(CLOCK_MONOTONIC)', 'raw_unit': 'milliseconds', 'integer_rounding': False}`

Raw samples (20):

```json
[34.885,19.918,9.165,8.14,8.621,24.925,8.643,8.126,9.133,8.638,8.429,7.942,8.976,8.045,9.305,9.154,8.004,8.188,8.419,8.815]
```

## Instrumentation overhead

- `library_first_render`: n=30, minimal median=21.321 ms, full median=16.783 ms, delta=-4.538 ms, relative=-21.284%
- `library_next_page`: n=30, minimal median=10.100 ms, full median=10.630 ms, delta=0.531 ms, relative=5.258%
- `open_book`: n=30, minimal median=68.400 ms, full median=63.551 ms, delta=-4.849 ms, relative=-7.090%
