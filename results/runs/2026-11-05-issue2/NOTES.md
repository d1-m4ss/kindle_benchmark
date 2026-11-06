# Notes for campaign 2026-11-05-issue2

Re-measurement after the harness fixes for issue #2: `R0_stock`, `R2_simpleui`, `R3_zenos`, `R6_simpleui_bookshelf`,
`R7_zenos_bookshelf`, `R9_simpleui_vos`, `R10_simpleui_vos_bookshelf`, and their Phase 1 counterparts. Headless
(`SDL_VIDEODRIVER=dummy`), 0 FAILED. Stock is the control against `2026-10-27-m1n1mal-v3`.

The runner was started through a local wrapper that left m1n1mal, pagecount and leanui out of the pinned-revision check and
the validation gate, because their checkouts held unpublished work and had drifted from the pins. Those stacks were not run
and their published rows are unchanged. Pins of every measured plugin were verified as usual.

The harness also carried changes that are still not committed, so this campaign's harness hash does not match the committed code: time spent in screen refresh calls is recorded,
`library_folder_back` no longer rebuilds at the root first, and `close_book`'s reset shows the book's page first. Folder-back
and close-book rows are directly exposed to those changes. Stock's close book moved from 28.5 to 33.9 ms in this campaign;
action CPU barely moved (19.35 to 20.14 ms) and the cause was not established.
