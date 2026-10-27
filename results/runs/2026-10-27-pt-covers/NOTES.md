# Notes for campaign 2026-10-27-pt-covers

Project:Title and Project:Title + VOS only (`--configs E_project_title,L_project_title_vos,R4_project_title,R11_project_title_vos`),
measured with the cover list enabled (`library_probe.cover_build_ui=true` in every warm result).
It replaces the Project:Title rows of `2026-10-27-m1n1mal-v3`. The validation gate ran for all stacks;
only the Project:Title configs have Phase 1 and Phase 2 data. The runner hash differs from
`2026-10-27-m1n1mal-v3` (Project:Title setup no longer pre-marked done; `--configs` scopes the Phase 2 gate).
VOS is pinned to v1.4 (see the v3 notes). `versions.lock.json` was edited afterwards only to make local plugin
paths relative.
