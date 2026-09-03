# Formal Specification: Benchmark Scenarios & Semantic Equivalences

This document formally defines the preconditions, actions, semantic postconditions, metadata requirements, and measurement intervals for all benchmark scenarios.

---

## Metric Definitions & Invariants

* **Display Size:** $W = 1236$, $H = 1648$, Total Pixels = $2{,}036{,}928$.
* **Clipped Rectangle:** For each requested refresh region $(x, y, w, h)$:
  $$x' = \max(0, \min(W, x)), \quad y' = \max(0, \min(H, y))$$
  $$w' = \max(0, \min(W - x', w)), \quad h' = \max(0, \min(H - y', h))$$
* **Cumulative Dirty Area:** $\sum (w'_i \times h'_i)$. Reported as screen-equivalents or percentage.
* **Spatial Union Area:** $\text{Area}\left(\bigcup R_i\right)$ computed via 1D coordinate compression sweep-line algorithm.
* **Invariants:**
  1. $0 \le \text{Spatial Union Area} \le W \times H$ ($0\% \le \text{Unique Dirty \%} \le 100\%$).
  2. $\text{Spatial Union Area} \le \text{Cumulative Dirty Area}$.
  3. **Paging Anti-No-Op Invariant:** Every paging transition must have $\text{page\_before} \ne \text{page\_after}$ and $\text{visible\_signature\_before} \ne \text{visible\_signature\_after}$. Any transition with unchanged page or identical visible signature is a hard failure (`FAILED`).
  4. **Paging Anti-Wrap Invariant:** Sequential paging strictly requires $\text{page\_after} = \text{page\_before} + 1$. Wrapping to page 1 from the final page during sequential paging is prohibited.
  5. **Bookshelf Non-Empty Shelf Invariant:** Bookshelf benchmarks must open on a populated catalog shelf (chip `"all"` / Home tab) with $\text{visible\_count} > 0$ and $\text{total\_pages} \ge 2$. Measuring an empty "Recent" view is an automatic validation failure.
* **Timing Contract:**
  1. Record $t_0$ with `clock_gettime(CLOCK_MONOTONIC)` via `time.monotonic()`.
  2. Initiate the action through the active UI-backend adapter.
  3. Yield the benchmark coroutine for naturally scheduled `nextTick` processing; do not remove or invoke private queue entries manually.
  4. Capture naturally emitted `UIManager.setDirty` refresh requests, including type, region and dither flag.
  5. Run the deferred semantic verifier after natural settling.
  6. Record $t_{\text{end}}$ and store `time.to_us(t_end - t0) / 1000.0` in raw JSON. Never call integer-rounding `time.to_ms()` for raw samples.
  7. A scenario that requires a visible transition fails if no natural refresh request is observed.
  8. **No unconditional `forceRePaint()` in the measured interval.**
* **Process startup contract:** the Python orchestrator records process-spawn time with `time.monotonic_ns()` and timestamps `[BENCHMARK_UI_READY]` and `[BENCHMARK_LIBRARY_READY]` markers emitted only after natural event-loop settling and semantic readiness checks.

---

## Scenario Specifications

### 1. `start_to_home`
* **Role:** Transition from cold start / library to the dedicated Home Screen.
* **Precondition:** Library or initial screen visible.
* **Action:** Invoke backend's Home Screen navigation.
* **Postcondition:** The backend's concrete Home Screen instance is shown and is the top widget.
* **Support:** `SimpleUI`, `ZenOS`, `Bookshelf`. (Marked `UNSUPPORTED` for Stock / Project: Title).

### 2. `home_to_library`
* **Role:** Transition from Home Screen to Library / File Browser.
* **Precondition:** Home Screen active.
* **Action:** Invoke backend's Library navigation.
* **Postcondition:** Target Library/FileManager instance is shown on top, points at the deterministic target path, and has a non-empty item table/visible signature.
* **Support:** All backends (`Stock`, `SimpleUI`, `ZenOS`, `Bookshelf`, `ProjectTitle`, `VOS`).

### 3. `library_first_render`
* **Role:** Initial render and layout of target library directory.
* **Precondition:** Target library directory set.
* **Action:** Initialize / load directory contents into library view.
* **Postcondition:** Items rendered on screen; visible count $> 0$ and signature is non-empty.
* **Support:** All backends.

### 4. `library_sequential_paging`
* **Role:** Measure fair, uncached sequential forward page turns ($1 \to 2 \to 3 \to \dots$).
* **Precondition:** Library UI active at page 1, $\text{total\_pages} \ge 2$, $\text{visible\_count} > 0$.
* **Action:** Execute sequential next-page transitions up to 30 transitions without resets or wrapping.
* **Postcondition:** For step $k$, $\text{page\_before} = k$, $\text{page\_after} = k+1$, $\text{visible\_signature\_before} \ne \text{visible\_signature\_after}$, $\text{visible\_count} > 0$.
* **Support:** All backends.

### 5. `library_cached_paging`
* **Role:** Measure repeated page turns between already-rendered pages ($1 \leftrightarrow 2$).
* **Precondition:** Library UI active at page 1, $\text{total\_pages} \ge 2$.
* **Action:** Perform unmeasured warm-up ($1 \to 2$, $2 \to 1$), then measure 30 transitions alternating between $1 \to 2$ and $2 \to 1$.
* **Postcondition:** Page index toggles between 1 and 2; visible signatures match expected page states; natural refresh observed.
* **Support:** All backends.

### 6. `bookshelf_sequential_paging` & `bookshelf_cached_paging` (Default Animation: `"medium"`)
* **Role:** Measure Bookshelf sequential and cached paging under the default user experience (page wipe animation active).
* **Precondition:** Bookshelf open on populated catalog (chip `"all"`), $\text{visible\_count} > 0$, $\text{total\_pages} \ge 2$, `shelf_page_animation = "medium"`.
* **Action:** Execute sequential ($1 \to 2 \to 3 \dots$) and cached ($1 \leftrightarrow 2$) transitions.
* **Postcondition:** Concrete page change, visible signature change, animation refresh frames captured.
* **Support:** Bookshelf configurations.

### 7. `bookshelf_sequential_paging_anim_off` & `bookshelf_cached_paging_anim_off` (Animation: `"off"`)
* **Role:** Measure Bookshelf paging in pure renderer comparison mode without page wipe animation latency.
* **Precondition:** Bookshelf open on populated catalog, `shelf_page_animation = "off"`.
* **Action:** Execute sequential and cached transitions.
* **Postcondition:** Instant shelf swap in place, visible signature change, dirty region updated.
* **Support:** Bookshelf configurations.

### 8. `library_folder_enter` & `library_folder_back`
* **Role:** Drill down into subfolder and return to root library.
* **Precondition:** Hierarchical library loaded, target subfolder exists.
* **Action:** Change path to subfolder / change path back to library root.
* **Postcondition:** FileChooser path and items match target folder / root library.
* **Support:** Hierarchical corpora on all file-tree backends.

### 9. `change_sort_mode`
* **Role:** Toggle sorting order (e.g. filename $\leftrightarrow$ date / author).
* **Precondition:** Library active, current sort $= S_1$.
* **Action:** Change sort order to $S_2$.
* **Postcondition:** Persisted sort setting equals $S_2$ and visible-item signature changes.
* **Support:** All backends supporting configurable sort.

### 10. `open_book` & `close_book`
* **Role:** Open target EPUB into `ReaderUI` and return to library.
* **Precondition:** Deterministic target EPUB exists on disk.
* **Action:** `ReaderUI:showReader(target_path)` / `ReaderUI.instance:onHome()`.
* **Postcondition:** Reader view active / Reader destroyed and base UI restored on top.
* **Support:** All configurations.

### 11. `open_quick_settings` & `close_quick_settings`
* **Role:** Open top controls / start menu dialog and dismiss back to base view.
* **Precondition:** Base view active on top.
* **Action:** Show menu dialog / close menu dialog.
* **Postcondition:** Dialog shown on top / dialog dismissed and base view restored.
* **Support:** All backends.

### 12. `repeated_nav`
* **Role:** Alternating forward/backward stress test ($1 \to 2 \to 1 \to 2 \dots$).
* **Precondition:** Library UI active with $\ge 2$ pages.
* **Action:** Execute alternating forward and backward transitions without wrapping.
* **Postcondition:** All transitions complete successfully with natural refreshes.
* **Support:** All backends.

---

## Deprecated Scenarios

The following legacy scenarios are formally **deprecated** and marked `DEPRECATED_INVALID_FOR_RANKING`:
- `library_next_page` (deprecated due to uncontrolled boundary wrapping).
- `library_prev_page` (deprecated due to uncontrolled boundary wrapping).
- `bookshelf_page_turn` (deprecated due to empty Recent shelf no-op measurements).

## Paging root

Paging needs a listing with more than one page. The runner counts the books directly in the library root and, only when that count is below `PAGING_MIN_ROOT_BOOKS` (403 — the books needed for 30 transitions at the coarsest 14-entries-per-page layout), names the fullest leaf folder as the paging root. The harness then pages through that folder instead of an unpaginatable root, and records `paging_root` with the leaf path, its book count, and the full library book count.

Validation rejects both directions of disagreement: a run that narrowed without declaring it, and a run that narrowed although its root paginates on its own. `paging_root` therefore states exactly which subset a paging number describes — a leaf holding 165 of 2,000 books is not "paging over 2,000 books".

The real working corpus keeps 500 books in its root precisely so it is never narrowed. See the README for that layout.

## Reader page turns

`reader_page_turn` is measured inside one document, pinned deterministically to the book nearest the corpus median size. Page-turn latency tracks document size and complexity, so rotating documents between iterations would blend unrelated documents into one median. The artifact records `reader_book` and validation fails a control run whose page turns were not pinned.

`open_book`, `open_book_minimal` and `close_book` keep rotating through ten deterministic books on purpose: repeating one file would measure a warm document cache rather than a cold open.

## Window-stack evidence and visual proof

A page turn under a full-screen overlay changes the widget's page, changes its
visible signature and fires a refresh, so every semantic guard passes while the
screen shows something else. A fresh ZenOS profile did exactly that with its
quickstart wizard.

Window-stack topology cannot detect this on its own: SimpleUI renders its library
through a painted full-screen container that sits **above** the FileManager, so a
full-screen window above the measured widget describes a healthy stack as
accurately as an occluding wizard. Therefore:

- Every measured library and Bookshelf transition records `top_widget`,
  `windows_above_measured`, `windows_above_names` (each entry naming a window and
  its screen coverage, for example `modal@100%`), `measured_widget_on_stack` and
  `fullscreen_above`. This is evidence, not a verdict.
- The only hard failure is `measured_widget_on_stack != true`: the measured widget
  was not on the window stack, so there was nothing on screen to measure.
- Every measured transition also records `framebuffer_hash`, an xxHash3 of the
  finished frame taken outside the timing window. `invoke()` already settles and
  repaints inside the timed window, so no extra settling is needed and the
  measured sequence is untouched: about 0.2 ms for a 2 MB buffer, no file.
- **Two consecutive transitions that leave an identical `framebuffer_hash` fail.**
  Nothing visibly moved between them, which is what a static overlay covering the
  measured widget looks like. Only *consecutive* repeats count: cached paging
  alternates between two pages, and `bookshelf_cached_paging_anim_off` legitimately
  produces just two distinct frames across thirty transitions, so requiring all
  hashes to be unique would fail a healthy run.
- A screenshot per transition was rejected deliberately. `probe_screenshot()` runs
  its own settle pass and a synchronous PNG encode of the whole framebuffer, so
  doing that between every measurement would change the workload: sequential
  paging would stop being continuous forward navigation, and cached paging would
  have the very cache state it measures disturbed between samples. The cost was
  never the disk.
- Visual proof comes from mandatory probe screenshots. `paging_probe_step_2_to_3`
  captures an unmeasured before/after pair around a real 2 -> 3 turn in every
  paging run, and `smoke_probe_step_2_to_3` / `bookshelf_probe_step_2_to_3` do the
  same in the smoke profile. Each pair is checked for PNG magic bytes, one exact
  emulator resolution, matching recorded SHA-256 and **differing** hashes.

The screenshots cover one transition per run and answer "what was on screen"; the
per-transition hashes cover all thirty and answer "did the screen change at all".
An overlay appearing mid-series is caught by the hashes even though no screenshot
captures it.

## Smoke no-op guard

The smoke profile includes `smoke_noop_guard`. It sends an invalid `1 -> 1` request to the adapter and passes only when the attempted transition is explicitly recorded as `FAILED`; an adapter that accepts the no-op fails the smoke result.

## Paging-only rerun scope

The final navigation/paging rerun uses the runner's separate paging-only commands:
- `--paging-phase1`: FLAT 2000 and HIERARCHICAL 2000 synthetic corpora, three independent process runs per configuration and dataset.
- `--paging-phase2`: the full `real_books` corpus, three independent process runs per configuration.

These commands use profile `paging` and do not run startup, memory, Bookends reader-control, or open-book workloads. The legacy `--phase1` and `--phase2` commands remain separate and are not the final paging result source.

---

## Result State Classifications

Every measurement records one of three distinct statuses:
1. **`PASS`**: Action executed, timing measured naturally, concrete value/state postcondition strictly verified.
2. **`UNSUPPORTED`**: The action is not semantically supported by this UI stack architecture. Reported explicitly as `UNSUPPORTED` (never converted to 0 ms or counted as failure).
3. **`FAILED`**: The action was attempted, but threw an error or failed its semantic postcondition. Reported as `FAILED` with explicit diagnostic error reason; excluded from valid latency statistics.
