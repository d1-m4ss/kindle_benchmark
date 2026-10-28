# Notes for campaign 2026-10-28-cyberui-b

CyberUI v1.0.0 only (`--configs O_cyberui,R14_cyberui`); the validation gate ran for all stacks. CyberUI is driven
through its own screens (the harness paints/reads its window, not the FileChooser). Quick-settings scenarios are UNSUPPORTED
(no such panel). Sort uses two of CyberUI's four sort orders that differ on page one for the corpus. Wall times of its
library actions are pinned at the harness's 16 ms frame floor; action CPU is 1.5-2.1 ms. Runner and harness hashes differ
from the 2026-10-27 campaigns. `versions.lock.json` was edited afterwards only to make local plugin paths relative.
