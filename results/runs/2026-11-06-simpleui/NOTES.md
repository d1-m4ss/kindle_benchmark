# Notes for campaign 2026-11-06-simpleui

Re-measurement of `R2_simpleui`, `R6_simpleui_bookshelf`, `R9_simpleui_vos`, `R10_simpleui_vos_bookshelf` and their Phase 1
counterparts after the SimpleUI adapter stopped navigating to the library when it is already there. Headless, 0 FAILED. Stock
was not re-run: its rows come from `2026-11-05-issue2`, whose harness differs only by this adapter change.

Started through the same local wrapper as `2026-11-05-issue2`: m1n1mal, pagecount and leanui were left out of the
pinned-revision check and the gate, and the harness carries the same not yet committed changes (see that campaign's notes).
