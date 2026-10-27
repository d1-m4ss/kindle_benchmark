# Notes for campaign 2026-10-27-m1n1mal-v3

- Project:Title rows were measured **without covers** (plain list): the harness pre-marked its first-run
  setup as done. All other CoverBrowser stacks, including N_m1n1mal / R13_m1n1mal, ran with covers.
  Do not compare Project:Title rows with the others; see the correction in the repository README.
- VOS rows here are VOS v1.4. They are superseded by campaign `2026-10-27-vos-141` (VOS v1.4.1). v1.4.1 first
  failed `library_folder_enter` because it enables `hide_empty_folders` by default and the flat libraries'
  folder-enter target is an empty `.sdr` directory; the harness now turns that option off.
- SimpleUI 3.0.x defaults to the file manager, so the harness sets `start_with = homescreen_simpleui`.
- LeanUI here is the abandoned local rebuild.
- Single-process scenarios (open_book, first_run, heap) have one sample per stack.
- Project:Title rows are superseded by campaign `2026-10-27-pt-covers` (cover list enabled; see the README).
- `versions.lock.json` was edited after these runs only to make the local plugins' source paths relative,
  so the committed lock's SHA-256 differs from `versions_lock_sha256` in `campaign.json`; the pinned
  revisions are the same.
