#!/usr/bin/env python3
"""Permanent unit test suite for KOReader benchmark paging validation invariants."""

import copy
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch
import sys

# Ensure repo root is on sys.path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.run_benchmarks import (
    Job, PAGING_MIN_ROOT_BOOKS, REAL_FOLDER_BOOKS, REAL_ROOT_BOOKS, RunLayout,
    SCHEMA_VERSION, bookends_blocks, ensure_layout, paging_phase1_blocks,
    plan_real_corpus_layout, prepare_real_corpora_for_jobs,
    validate_result_artifact, write_corpus_manifest, write_deterministic_targets,
)


class TestPagingValidation(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.raw_dir = self.root / "raw"
        self.logs_dir = self.root / "logs"
        self.raw_dir.mkdir(parents=True)
        self.logs_dir.mkdir(parents=True)
        self.screenshots_dir = self.root / "screenshots"
        self.screenshots_dir.mkdir(parents=True)
        self.layout = RunLayout(
            campaign="test_campaign", phase="phase1",
            root=self.root / "phase1", raw=self.raw_dir, logs=self.logs_dir,
            checkpoints=self.root / "checkpoints",
            charts=self.root / "charts",
            screenshots=self.screenshots_dir,
            environment=self.root / "environment.json",
        )
        self.job = Job(
            run_id="test_run", block="phase1", phase="phase1",
            config="A_stock", plugins=(),
            library_dir="/tmp/lib", ko_home="/tmp/home",
            mode="warm", profile="paging",
            dataset_mode="flat", book_count=2000,
            warmup=1, measure=1, fresh_home=True,
        )
        # Create a valid log file
        log_file = self.logs_dir / f"{self.job.run_id}.log"
        log_file.write_text("framebuffer resolution: 1236x1648\nBENCHMARK_COMPLETE\n")

        # Base valid artifact
        items_p1 = [f"book_{i}.epub" for i in range(1, 11)]
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p3 = [f"book_{i}.epub" for i in range(21, 31)]

        self.valid_artifact = {
            "schema_version": SCHEMA_VERSION,
            "run_id": self.job.run_id,
            "process_returncode": 0,
            "campaign": self.layout.campaign,
            "output_phase": self.layout.phase,
            "screen_size": {"w": 1236, "h": 1648},
            "framebuffer_resolution": "1236x1648",
            "campaign_environment": {"runner_sha256": "abcdef"},
            "external_process_timing": {
                "spawn_to_ui_ready_ms": 100.0,
                "spawn_to_library_ready_ms": 200.0,
                "complete_marker_ms": 500.0,
            },
            "plugin_load_assertion": {"status": "PASS"},
            "run_status": "PASS",
            "scenarios": {
                "library_sequential_paging": {
                    "status": "PASS",
                    "transition_cap": 30,
                    "available_transitions": 2,
                    "requested_transitions": 2,
                    "actual_transitions": 2,
                    "total_pages": 3,
                    "iterations": [
                        {
                            "status": "PASS",
                            "wall_time_ms": 15.0,
                            "page_before": 1,
                            "page_after": 2,
                            "visible_count_before": 10,
                            "visible_count_after": 10,
                            "visible_items_before": items_p1,
                            "visible_items_after": items_p2,
                            "visible_signature_before": "sig_p1",
                            "visible_signature_after": "sig_p2",
                            "total_pages": 3,
                            "refresh_count": 1,
                            "unique_dirty_pct": 50.0,
                            "spatial_union_dirty_area_pixels": 1000,
                            "cumulative_dirty_area_pixels": 1000,
                        },
                        {
                            "status": "PASS",
                            "wall_time_ms": 16.0,
                            "page_before": 2,
                            "page_after": 3,
                            "visible_count_before": 10,
                            "visible_count_after": 10,
                            "visible_items_before": items_p2,
                            "visible_items_after": items_p3,
                            "visible_signature_before": "sig_p2",
                            "visible_signature_after": "sig_p3",
                            "total_pages": 3,
                            "refresh_count": 1,
                            "unique_dirty_pct": 50.0,
                            "spatial_union_dirty_area_pixels": 1000,
                            "cumulative_dirty_area_pixels": 1000,
                        },
                    ],
                },
                "library_cached_paging": {
                    "status": "PASS",
                    "transition_cap": 30,
                    "available_transitions": 2,
                    "requested_transitions": 2,
                    "actual_transitions": 2,
                    "total_pages": 3,
                    "warmup_verified": True,
                    "iterations": [
                        {
                            "status": "PASS",
                            "wall_time_ms": 12.0,
                            "page_before": 1,
                            "page_after": 2,
                            "visible_count_before": 10,
                            "visible_count_after": 10,
                            "visible_items_before": items_p1,
                            "visible_items_after": items_p2,
                            "visible_signature_before": "sig_p1",
                            "visible_signature_after": "sig_p2",
                            "total_pages": 3,
                            "refresh_count": 1,
                            "unique_dirty_pct": 50.0,
                            "spatial_union_dirty_area_pixels": 1000,
                            "cumulative_dirty_area_pixels": 1000,
                        },
                        {
                            "status": "PASS",
                            "wall_time_ms": 11.0,
                            "page_before": 2,
                            "page_after": 1,
                            "visible_count_before": 10,
                            "visible_count_after": 10,
                            "visible_items_before": items_p2,
                            "visible_items_after": items_p1,
                            "visible_signature_before": "sig_p2",
                            "visible_signature_after": "sig_p1",
                            "total_pages": 3,
                            "refresh_count": 1,
                            "unique_dirty_pct": 50.0,
                            "spatial_union_dirty_area_pixels": 1000,
                            "cumulative_dirty_area_pixels": 1000,
                        },
                    ],
                },
            },
        }
        # The paging profile requires a visual probe; a library with too few
        # pages legitimately skips it, which is what this fixture declares.
        self.valid_artifact["scenarios"]["paging_probe_step_2_to_3"] = {
            "status": "UNSUPPORTED",
            "reason": "Library has <3 pages, probe 2->3 skipped",
            "transition_cap": 1, "available_transitions": 0,
            "requested_transitions": 0, "actual_transitions": 0,
            "total_pages": 3, "iterations": [],
        }
        # Every measured transition must record what was on the window stack;
        # inject that evidence rather than repeating it per iteration.
        for scenario in self.valid_artifact["scenarios"].values():
            for iteration in scenario.get("iterations", []):
                iteration.setdefault("top_widget", "filemanager")
                iteration.setdefault("windows_above_measured", 0)
                iteration.setdefault("windows_above_names", [])
                iteration.setdefault("measured_widget_on_stack", True)
        for scenario_name, scenario in self.valid_artifact["scenarios"].items():
            for position, iteration in enumerate(scenario.get("iterations", [])):
                iteration.setdefault("framebuffer_hash", f"{scenario_name}-frame-{position:04d}")

    def tearDown(self):
        self.temp_dir.cleanup()

    def _write_artifact(self, data: dict) -> None:
        raw_file = self.raw_dir / f"{self.job.run_id}.json"
        raw_file.write_text(json.dumps(data))

    def test_valid_artifact_passes(self):
        self._write_artifact(self.valid_artifact)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertTrue(valid, f"Expected valid artifact to pass, got errors: {errors}")

    def test_reject_noop_transition(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["page_after"] = 1
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("no-op transition" in e for e in errors))

    def test_reject_wraparound_transition(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][1]["page_before"] = 3
        data["scenarios"]["library_sequential_paging"]["iterations"][1]["page_after"] = 1
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("broken sequential chain" in e for e in errors))

    def test_reject_broken_sequential_chain(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][1]["page_before"] = 2
        data["scenarios"]["library_sequential_paging"]["iterations"][1]["page_after"] = 4
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("broken sequential chain" in e for e in errors))

    def test_reject_first_step_not_1_to_2(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["page_before"] = 2
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["page_after"] = 3
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("first sequential iteration" in e for e in errors))

    def test_reject_count_mismatch(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["requested_transitions"] = 30
        data["scenarios"]["library_sequential_paging"]["actual_transitions"] = 2
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("count mismatch" in e for e in errors))

    def test_reject_empty_visible_signature(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["visible_signature_after"] = ""
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("empty visible signature" in e for e in errors))

    def test_reject_unchanged_visible_signature(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["visible_signature_after"] = "sig_p1"
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("unchanged visible signature" in e for e in errors))

    def test_reject_zero_visible_items(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["visible_count_before"] = 0
        data["scenarios"]["library_sequential_paging"]["iterations"][0]["visible_items_before"] = []
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("zero visible items" in e or "empty visible_items" in e for e in errors))

    def test_reject_bookshelf_single_page(self):
        bs_job = Job(
            run_id="bs_run", block="phase1", phase="phase1",
            config="B_bookshelf", plugins=("bookshelf",),
            library_dir="/tmp/lib", ko_home="/tmp/home",
            mode="warm", profile="paging",
            dataset_mode="flat", book_count=2000,
            warmup=1, measure=1, fresh_home=True,
        )
        data = copy.deepcopy(self.valid_artifact)
        data["run_id"] = bs_job.run_id
        items_p1 = [f"book_{i}.epub" for i in range(1, 11)]
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        data["scenarios"]["open_bookshelf"] = {"status": "PASS", "iterations": [{"status": "PASS", "wall_time_ms": 10.0, "unique_dirty_pct": 50.0, "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100}]}
        data["scenarios"]["close_bookshelf"] = {"status": "PASS", "iterations": [{"status": "PASS", "wall_time_ms": 10.0, "unique_dirty_pct": 50.0, "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100}]}
        data["scenarios"]["bookshelf_sequential_paging"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 1,
            "animation": "animation_on_default", "animation_verified": True,
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 1, "page_after": 2,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p1, "visible_items_after": items_p2,
                "visible_signature_before": "sig1", "visible_signature_after": "sig2",
                "total_pages": 1, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        data["scenarios"]["bookshelf_cached_paging"] = copy.deepcopy(data["scenarios"]["bookshelf_sequential_paging"])
        data["scenarios"]["bookshelf_sequential_paging_anim_off"] = copy.deepcopy(data["scenarios"]["bookshelf_sequential_paging"])
        data["scenarios"]["bookshelf_cached_paging_anim_off"] = copy.deepcopy(data["scenarios"]["bookshelf_sequential_paging"])
        raw_file = self.raw_dir / f"{bs_job.run_id}.json"
        raw_file.write_text(json.dumps(data))
        valid, errors = validate_result_artifact(bs_job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("bookshelf shelf has <2 pages" in e for e in errors))

    def test_paging_phase1_has_three_process_runs_per_dataset(self):
        blocks = paging_phase1_blocks("test_campaign", process_runs=3)
        self.assertEqual(len(blocks), 12)
        self.assertEqual(sorted({len(jobs) for jobs in blocks.values()}), [6])
        self.assertEqual(
            sorted({job.run_id.rsplit("_r", 1)[-1] for jobs in blocks.values() for job in jobs}),
            ["01", "02", "03"],
        )

    def test_smoke_noop_guard_requires_rejected_attempt(self):
        from analyze_results import audit_records
        data = {
            "run_id": "smoke",
            "profile": "smoke_validation",
            "scenarios": {
                "smoke_noop_guard": {
                    "status": "PASS",
                    "attempted_status": "PASS",
                },
            },
        }
        _, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("no-op guard did not reject" in violation for violation in violations))

    def test_reject_deprecated_scenario(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_next_page"] = {"status": "PASS", "iterations": []}
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("deprecated scenarios found" in e for e in errors))

    def test_flash_setting_is_campaign_identity(self):
        metadata = ensure_layout(self.layout, emulate_reader_flash_ms=100)
        self.assertEqual(metadata["emulate_reader_flash_ms"], 100)
        with self.assertRaisesRegex(RuntimeError, "campaign identity changed for emulate_reader_flash_ms"):
            ensure_layout(self.layout, emulate_reader_flash_ms=None)

    def test_reject_probe_noop(self):
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 3,
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 2,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p2,
                "visible_signature_before": "sig2", "visible_signature_after": "sig2",
                "total_pages": 3, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("no-op transition" in e or "probe 2->3" in e for e in errors))

        from analyze_results import audit_records
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("no-op transition" in v or "invalid probe" in v for v in violations))

    def test_audit_rejects_truncated_or_non_alternating_paging(self):
        from analyze_results import audit_records

        truncated = copy.deepcopy(self.valid_artifact)
        truncated["scenarios"]["library_sequential_paging"]["iterations"].pop()
        _, violations = audit_records([truncated], scope="phase1", strict=True)
        self.assertTrue(any("iteration count mismatch" in violation for violation in violations))

        non_alternating = copy.deepcopy(self.valid_artifact)
        non_alternating["scenarios"]["library_cached_paging"]["iterations"][1]["page_before"] = 1
        non_alternating["scenarios"]["library_cached_paging"]["iterations"][1]["page_after"] = 2
        _, violations = audit_records([non_alternating], scope="phase1", strict=True)
        self.assertTrue(any("broken cached alternation" in violation for violation in violations))

    def test_reject_probe_invalid_step(self):
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p4 = [f"book_{i}.epub" for i in range(31, 41)]
        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 4,
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 4,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p4,
                "visible_signature_before": "sig2", "visible_signature_after": "sig4",
                "total_pages": 4, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("probe 2->3 in smoke_probe_step_2_to_3 is not 2->3" in e for e in errors))

        from analyze_results import audit_records
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("invalid probe transition" in v for v in violations))

    def test_probe_valid_screenshots_pass(self):
        import hashlib, struct
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p3 = [f"book_{i}.epub" for i in range(21, 31)]

        # Valid PNG mock builder
        def mock_png(w=1236, h=1648, extra=b""):
            return b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", w, h) + b"\x08\x02\x00\x00\x00\x00\x00\x00\x00" + extra

        png_b = mock_png(1236, 1648, b"page_2_visual_data")
        png_a = mock_png(1236, 1648, b"page_3_visual_data")
        hash_b = hashlib.sha256(png_b).hexdigest()
        hash_a = hashlib.sha256(png_a).hexdigest()

        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 3,
            "screenshot_before": "smoke_probe_page2_before.png",
            "screenshot_after": "smoke_probe_page3_after.png",
            "screenshot_before_sha256": hash_b,
            "screenshot_after_sha256": hash_a,
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 3,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p3,
                "visible_signature_before": "sig2", "visible_signature_after": "sig3",
                "total_pages": 3, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        job_shot_dir = self.screenshots_dir / self.job.run_id
        job_shot_dir.mkdir(parents=True, exist_ok=True)
        (job_shot_dir / "smoke_probe_page2_before.png").write_bytes(png_b)
        (job_shot_dir / "smoke_probe_page3_after.png").write_bytes(png_a)

        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertTrue(valid, f"Expected valid probe screenshots to pass, got: {errors}")

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertEqual(violations, [])

    def test_reject_probe_missing_screenshot_fields(self):
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p3 = [f"book_{i}.epub" for i in range(21, 31)]
        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 3,
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 3,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p3,
                "visible_signature_before": "sig2", "visible_signature_after": "sig3",
                "total_pages": 3, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("mandatory probe screenshots missing" in e for e in errors))

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("missing mandatory probe screenshots" in v for v in violations))

    def test_reject_probe_missing_screenshot_file(self):
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p3 = [f"book_{i}.epub" for i in range(21, 31)]
        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 3,
            "screenshot_before": "smoke_probe_page2_before.png",
            "screenshot_after": "smoke_probe_page3_after.png",
            "screenshot_before_sha256": "fakehash1",
            "screenshot_after_sha256": "fakehash2",
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 3,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p3,
                "visible_signature_before": "sig2", "visible_signature_after": "sig3",
                "total_pages": 3, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        # Do not create files on disk
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("invalid" in e for e in errors))

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("invalid" in v for v in violations))

    def test_reject_probe_invalid_png_magic_or_dimensions(self):
        import hashlib, struct
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p3 = [f"book_{i}.epub" for i in range(21, 31)]

        # Both dimensions are individually allowed but not a supported pair.
        png_bad = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", 618, 1648) + b"\x08\x02\x00\x00\x00\x00\x00\x00\x00"
        png_good = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", 1236, 1648) + b"\x08\x02\x00\x00\x00\x00\x00\x00\x00page3"

        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 3,
            "screenshot_before": "smoke_probe_page2_before.png",
            "screenshot_after": "smoke_probe_page3_after.png",
            "screenshot_before_sha256": hashlib.sha256(png_bad).hexdigest(),
            "screenshot_after_sha256": hashlib.sha256(png_good).hexdigest(),
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 3,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p3,
                "visible_signature_before": "sig2", "visible_signature_after": "sig3",
                "total_pages": 3, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        job_shot_dir = self.screenshots_dir / self.job.run_id
        job_shot_dir.mkdir(parents=True, exist_ok=True)
        (job_shot_dir / "smoke_probe_page2_before.png").write_bytes(png_bad)
        (job_shot_dir / "smoke_probe_page3_after.png").write_bytes(png_good)

        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("unexpected resolution" in e or "invalid" in e for e in errors))

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("unexpected resolution" in v or "invalid" in v for v in violations))

    def test_reject_probe_identical_screenshots(self):
        import hashlib, struct
        data = copy.deepcopy(self.valid_artifact)
        items_p2 = [f"book_{i}.epub" for i in range(11, 21)]
        items_p3 = [f"book_{i}.epub" for i in range(21, 31)]

        png_same = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", 1236, 1648) + b"\x08\x02\x00\x00\x00\x00\x00\x00\x00same"
        h = hashlib.sha256(png_same).hexdigest()

        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "PASS", "requested_transitions": 1, "actual_transitions": 1, "total_pages": 3,
            "screenshot_before": "smoke_probe_page2_before.png",
            "screenshot_after": "smoke_probe_page3_after.png",
            "screenshot_before_sha256": h,
            "screenshot_after_sha256": h,
            "iterations": [{
                "status": "PASS", "wall_time_ms": 10.0, "page_before": 2, "page_after": 3,
                "visible_count_before": 10, "visible_count_after": 10,
                "visible_items_before": items_p2, "visible_items_after": items_p3,
                "visible_signature_before": "sig2", "visible_signature_after": "sig3",
                "total_pages": 3, "refresh_count": 1, "unique_dirty_pct": 50.0,
                "spatial_union_dirty_area_pixels": 100, "cumulative_dirty_area_pixels": 100,
                "top_widget": "filemanager", "windows_above_measured": 0,
                "measured_widget_on_stack": True, "windows_above_names": [],
                "framebuffer_hash": "probe-frame-0000",
            }],
        }
        job_shot_dir = self.screenshots_dir / self.job.run_id
        job_shot_dir.mkdir(parents=True, exist_ok=True)
        (job_shot_dir / "smoke_probe_page2_before.png").write_bytes(png_same)
        (job_shot_dir / "smoke_probe_page3_after.png").write_bytes(png_same)

        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("probe screenshots identical" in e for e in errors))

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        count, violations = audit_records([data], scope="validation", strict=True)
        self.assertTrue(any("probe screenshots identical" in v for v in violations))


    def test_reject_unsupported_paging_scenario(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"] = {
            "status": "UNSUPPORTED",
            "reason": "Library has only 1 page, cannot measure sequential paging",
            "iterations": [],
        }
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("UNSUPPORTED (zero pages available)" in e for e in errors))

        from analyze_results import audit_records
        data["profile"] = "paging"
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        _, violations = audit_records([data], scope="phase1", strict=True)
        self.assertTrue(any("UNSUPPORTED (zero pages available)" in v for v in violations))

    def test_full_synthetic_allows_unsupported_small_library_paging(self):
        from analyze_results import audit_records
        from scripts.run_benchmarks import expected_scenarios

        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_sequential_paging"] = {
            "status": "UNSUPPORTED", "reason": "Library has <2 pages", "iterations": [],
        }
        data["scenarios"]["library_cached_paging"] = {
            "status": "UNSUPPORTED", "reason": "Library has <2 pages", "iterations": [],
        }
        synthetic_job = replace(
            self.job, profile="synthetic", dataset_mode="hierarchical", book_count=50,
        )
        for scenario_name in expected_scenarios(synthetic_job) - set(data["scenarios"]):
            data["scenarios"][scenario_name] = {
                "status": "UNSUPPORTED", "reason": "Not exercised by this fixture", "iterations": [],
            }

        self._write_artifact(data)
        valid, errors = validate_result_artifact(synthetic_job, self.layout, require_success=True)
        self.assertTrue(valid, errors)

        data["_path"] = str(self.raw_dir / f"{synthetic_job.run_id}.json")
        _, violations = audit_records([data], scope="phase1", strict=True)
        self.assertFalse(violations, violations)

    def test_probe_unsupported_is_not_flagged_as_zero_page_violation(self):
        # Probes legitimately skip on <3 pages; only the mandatory
        # sequential/cached paging scenarios must always produce real data.
        from analyze_results import audit_records
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["smoke_probe_step_2_to_3"] = {
            "status": "UNSUPPORTED",
            "reason": "Library has <3 pages, probe 2->3 skipped",
            "iterations": [],
        }
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        _, violations = audit_records([data], scope="phase1", strict=True)
        self.assertFalse(any("zero pages available" in v for v in violations))

    def test_audit_summary_flags_zero_data_paging_cell(self):
        from analyze_results import audit_summary
        data = copy.deepcopy(self.valid_artifact)
        data["phase"] = "phase1"
        data["config"] = "A_stock"
        data["dataset_mode"] = "hierarchical"
        data["profile"] = "paging"
        data["mode"] = "warm"
        data["_path"] = "fake/path.json"
        data["scenarios"]["library_sequential_paging"] = {
            "status": "UNSUPPORTED", "reason": "Library has only 1 page", "iterations": [],
        }
        data["scenarios"]["library_cached_paging"] = {
            "status": "UNSUPPORTED", "reason": "Library requires at least 2 pages", "iterations": [],
        }
        summary = audit_summary([data])
        self.assertEqual(summary["zero_data_cells"], ["phase1:A_stock:hierarchical:paging:warm"])

    def test_audit_summary_does_not_flag_cell_with_real_samples(self):
        from analyze_results import audit_summary
        data = copy.deepcopy(self.valid_artifact)
        data["phase"] = "phase1"
        data["config"] = "A_stock"
        data["dataset_mode"] = "flat"
        data["profile"] = "paging"
        data["mode"] = "warm"
        data["_path"] = "fake/path.json"
        summary = audit_summary([data])
        self.assertEqual(summary["zero_data_cells"], [])

    def test_audit_summary_allows_zero_data_full_synthetic_cell(self):
        from analyze_results import audit_summary
        data = copy.deepcopy(self.valid_artifact)
        data["phase"] = "phase1"
        data["config"] = "A_stock"
        data["dataset_mode"] = "hierarchical"
        data["profile"] = "synthetic"
        data["mode"] = "warm"
        data["_path"] = "fake/path.json"
        data["scenarios"]["library_sequential_paging"] = {
            "status": "UNSUPPORTED", "reason": "Library has only 1 page", "iterations": [],
        }
        data["scenarios"]["library_cached_paging"] = {
            "status": "UNSUPPORTED", "reason": "Library requires at least 2 pages", "iterations": [],
        }
        summary = audit_summary([data])
        self.assertEqual(summary["zero_data_cells"], [])

    def test_write_deterministic_targets_picks_leaf_with_most_books(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = Path(tmp) / "hierarchical_lib"
            small_leaf = library / "Fiction" / "Cyberpunk"
            big_leaf = library / "Nonfiction" / "ComputerScience"
            small_leaf.mkdir(parents=True)
            big_leaf.mkdir(parents=True)
            for i in range(3):
                (small_leaf / f"book_{i}.epub").write_text("x")
            for i in range(20):
                (big_leaf / f"book_{i}.epub").write_text("x")

            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertEqual(Path(decoded["leaf_folder"]), big_leaf)

    def test_write_deterministic_targets_no_books_yields_no_leaf_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = Path(tmp) / "empty_lib"
            library.mkdir()
            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertIsNone(decoded["leaf_folder"])
            self.assertEqual(decoded["leaf_folder_book_count"], 0)

    def test_write_deterministic_targets_reports_leaf_book_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = Path(tmp) / "lib"
            small = library / "Small"
            big = library / "Big"
            small.mkdir(parents=True)
            big.mkdir(parents=True)
            for index in range(2):
                (small / f"s{index}.epub").write_text("x")
            for index in range(5):
                (big / f"b{index}.epub").write_text("x")
            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertEqual(Path(decoded["leaf_folder"]).name, "Big")
            self.assertEqual(decoded["leaf_folder_book_count"], 5)

    def _job_with_targets(self, tmp: Path, leaf_folder=None, leaf_books=0):
        """A job whose isolated home declares (or omits) a narrowed paging root."""
        home = tmp / "home"
        home.mkdir(parents=True, exist_ok=True)
        (home / "benchmark_targets.json").write_text(json.dumps({
            "seed": 1, "books": [], "folders": [],
            "leaf_folder": leaf_folder, "leaf_folder_book_count": leaf_books,
        }))
        return replace(self.job, ko_home=str(home))

    def test_narrowed_paging_requires_declared_paging_root(self):
        # Narrowing measures a smaller workload than the library, so a run that
        # was told to narrow must say so in its artifact.
        with tempfile.TemporaryDirectory() as tmp:
            job = self._job_with_targets(Path(tmp), "/tmp/lib/Fiction", 165)
            self._write_artifact(copy.deepcopy(self.valid_artifact))
            valid, errors = validate_result_artifact(job, self.layout, require_success=True)
            self.assertFalse(valid)
            self.assertTrue(any("paging_root metadata missing" in e for e in errors))

    def test_narrowed_paging_rejects_zero_book_paging_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            job = self._job_with_targets(Path(tmp), "/tmp/lib/Fiction", 0)
            data = copy.deepcopy(self.valid_artifact)
            data["paging_root"] = {"path": "/tmp/lib/Fiction", "book_count": 0}
            self._write_artifact(data)
            valid, errors = validate_result_artifact(job, self.layout, require_success=True)
            self.assertFalse(valid)
            self.assertTrue(any("paging_root.book_count must be > 0" in e for e in errors))

    def test_narrowed_paging_accepts_matching_paging_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            leaf = "/tmp/lib/Nonfiction/ComputerScience"
            job = self._job_with_targets(Path(tmp), leaf, 165)
            data = copy.deepcopy(self.valid_artifact)
            data["paging_root"] = {"path": leaf, "book_count": 165}
            self._write_artifact(data)
            valid, errors = validate_result_artifact(job, self.layout, require_success=True)
            self.assertTrue(valid, errors)

    def test_narrowed_paging_rejects_mismatched_book_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            leaf = "/tmp/lib/Nonfiction/ComputerScience"
            job = self._job_with_targets(Path(tmp), leaf, 165)
            data = copy.deepcopy(self.valid_artifact)
            data["paging_root"] = {"path": leaf, "book_count": 61}
            self._write_artifact(data)
            valid, errors = validate_result_artifact(job, self.layout, require_success=True)
            self.assertFalse(valid)
            self.assertTrue(any("book_count mismatch" in e for e in errors))

    def test_paginating_root_must_not_be_narrowed(self):
        # The real working corpus keeps 500 books in its root, so a run that
        # narrowed anyway measured the wrong thing and must fail.
        with tempfile.TemporaryDirectory() as tmp:
            job = self._job_with_targets(Path(tmp), None, 0)
            data = copy.deepcopy(self.valid_artifact)
            data["paging_root"] = {"path": "/tmp/lib/folder1", "book_count": 500}
            self._write_artifact(data)
            valid, errors = validate_result_artifact(job, self.layout, require_success=True)
            self.assertFalse(valid)
            self.assertTrue(any("paginates on its own" in e for e in errors))

    def test_reject_two_transitions_leaving_an_identical_screen(self):
        # A static overlay covering the library leaves the framebuffer byte
        # identical while pages and signatures still change underneath.
        data = copy.deepcopy(self.valid_artifact)
        its = data["scenarios"]["library_sequential_paging"]["iterations"]
        its[1]["framebuffer_hash"] = its[0]["framebuffer_hash"]
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("screen did not change" in e for e in errors), errors)

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        _, violations = audit_records([data], scope="phase1", strict=True)
        self.assertTrue(any("screen did not change" in v for v in violations), violations)

    def test_reject_transition_without_framebuffer_hash(self):
        data = copy.deepcopy(self.valid_artifact)
        data["scenarios"]["library_cached_paging"]["iterations"][0].pop("framebuffer_hash", None)
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("missing framebuffer_hash" in e for e in errors), errors)

    def test_distinct_framebuffer_hashes_pass(self):
        # Cached paging alternates 1<->2, so hashes repeat every other step;
        # only *consecutive* repeats mean the screen froze.
        data = copy.deepcopy(self.valid_artifact)
        its = data["scenarios"]["library_cached_paging"]["iterations"]
        for position, iteration in enumerate(its):
            iteration["framebuffer_hash"] = "page1" if position % 2 == 0 else "page2"
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertTrue(valid, errors)

    def test_reject_transition_whose_widget_left_the_window_stack(self):
        # If the measured widget is not on the window stack at all, nothing was
        # on screen to measure.
        data = copy.deepcopy(self.valid_artifact)
        it = data["scenarios"]["library_sequential_paging"]["iterations"][0]
        it["measured_widget_on_stack"] = False
        it["top_widget"] = "quickstart"
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("not on the window stack" in e for e in errors), errors)

        from analyze_results import audit_records
        data["_path"] = str(self.raw_dir / f"{self.job.run_id}.json")
        _, violations = audit_records([data], scope="phase1", strict=True)
        self.assertTrue(any("not on the window stack" in v for v in violations), violations)

    def test_reject_transition_without_window_stack_evidence(self):
        # An older harness that records no window-stack evidence must not pass
        # as if it had proved what was on screen.
        data = copy.deepcopy(self.valid_artifact)
        for key in ("top_widget", "windows_above_measured", "measured_widget_on_stack"):
            data["scenarios"]["library_cached_paging"]["iterations"][0].pop(key, None)
        self._write_artifact(data)
        valid, errors = validate_result_artifact(self.job, self.layout, require_success=True)
        self.assertFalse(valid)
        self.assertTrue(any("top_widget evidence" in e for e in errors), errors)
        self.assertTrue(any("windows_above_measured" in e for e in errors), errors)
        self.assertTrue(any("not on the window stack" in e for e in errors), errors)

    def test_zenos_home_declares_quickstart_already_shown(self):
        # A fresh ZenOS profile opens a full-screen quickstart wizard that
        # covers the library, so every measured page turn would be occluded.
        from scripts.run_benchmarks import setup_isolated_home, zenos_plugin_version
        with tempfile.TemporaryDirectory() as tmp:
            job = replace(self.job, ko_home=str(Path(tmp) / "home"), plugins=("zenos",))
            home = setup_isolated_home(job)
            config = home / "settings" / "ZenOS" / "config.lua"
            self.assertTrue(config.exists(), "ZenOS config was not seeded")
            text = config.read_text()
            version = zenos_plugin_version()
            self.assertIn(f'["quickstart_shown_for_version"] = "{version}"', text)
            self.assertIn('["quickstart_completed"] = true', text)
            # A real version string is required: nil or "pre-quickstart" makes
            # ZenOS treat the profile as fresh and show the wizard anyway.
            self.assertNotIn("pre-quickstart", text)
            self.assertRegex(version, r"^\d+\.\d+")

    def test_non_zenos_home_gets_no_zenos_config(self):
        from scripts.run_benchmarks import setup_isolated_home
        with tempfile.TemporaryDirectory() as tmp:
            job = replace(self.job, ko_home=str(Path(tmp) / "home"), plugins=())
            home = setup_isolated_home(job)
            self.assertFalse((home / "settings" / "ZenOS" / "config.lua").exists())

    def test_bookends_requires_a_pinned_reader_book(self):
        with tempfile.TemporaryDirectory() as tmp:
            job = replace(self._job_with_targets(Path(tmp), None, 0), profile="bookends_control")
            self._write_artifact(copy.deepcopy(self.valid_artifact))
            valid, errors = validate_result_artifact(job, self.layout, require_success=False)
            self.assertFalse(valid)
            self.assertTrue(any("not pinned to one document" in e for e in errors))

    def test_bookends_accepts_a_pinned_reader_book(self):
        with tempfile.TemporaryDirectory() as tmp:
            job = replace(self._job_with_targets(Path(tmp), None, 0), profile="bookends_control")
            data = copy.deepcopy(self.valid_artifact)
            data["reader_book"] = {"path": "/corpus/book.epub", "bytes": 765979, "pinned": True}
            data["bookends_reader_cycles_completed"] = 10
            data["bookends_reader_cycle_failures"] = []
            data["bookends_reader_cycles_live_heap_kb"] = [10000.0 + index for index in range(10)]
            data["bookends_reader_cycles_stats"] = {"count": 10}
            self._write_artifact(data)
            _, errors = validate_result_artifact(job, self.layout, require_success=False)
            self.assertFalse(
                any("not pinned to one document" in e or "reader_book.path" in e for e in errors),
                errors,
            )
            self.assertFalse(any("reader memory" in e for e in errors), errors)

    def test_bookends_rejects_a_single_final_heap_checkpoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            job = replace(self._job_with_targets(Path(tmp), None, 0), profile="bookends_control")
            data = copy.deepcopy(self.valid_artifact)
            data["reader_book"] = {"path": "/corpus/book.epub", "bytes": 765979, "pinned": True}
            data["memory_checkpoints"] = {
                "post_reader_live_heap": {"forced_gc_live_heap_kb": 32000.0},
            }
            self._write_artifact(data)
            valid, errors = validate_result_artifact(job, self.layout, require_success=False)
            self.assertFalse(valid)
            self.assertTrue(any("exactly 10 forced-GC samples" in error for error in errors), errors)

    def test_analyzer_distinguishes_memory_samples_from_process_runs(self):
        from analyze_results import add_memory_rows

        rows = []
        add_memory_rows([{
            "_path": "one_process.json",
            "phase": "bookends_control",
            "config": "A_stock",
            "mode": "warm",
            "profile": "bookends_control",
            "dataset_mode": "real_2692",
            "book_count": 2692,
            "memory_checkpoints": {},
            "bookends_reader_cycles_live_heap_kb": [10000.0 + index for index in range(10)],
        }], rows)
        row = next(item for item in rows if item["Scenario"] == "memory:post_reader_cycles_forced_gc")
        self.assertEqual(row["ProcessRuns"], 1)
        self.assertEqual(row["PassSamples"], 10)
        self.assertEqual(row["forced_gc_live_heap_kb_median"], 10004.5)

    def test_bookends_block_prepares_both_real_corpora(self):
        jobs = bookends_blocks("test_campaign")["bookends_control"]
        with patch("scripts.run_benchmarks.prepare_real_corpora") as prepare:
            corpora = prepare_real_corpora_for_jobs("test_campaign", jobs, lanes=1)
        prepare.assert_called_once_with(
            "test_campaign",
            ["bookends_A_stock", "bookends_K_stock_bookends"],
            lanes=1,
        )
        self.assertEqual(
            [corpus.parent.name for corpus in corpora],
            ["bookends_A_stock", "bookends_K_stock_bookends"],
        )

    def test_paginating_root_accepts_absent_paging_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            job = self._job_with_targets(Path(tmp), None, 0)
            self._write_artifact(copy.deepcopy(self.valid_artifact))
            valid, errors = validate_result_artifact(job, self.layout, require_success=True)
            self.assertTrue(valid, errors)

    def test_audit_summary_reports_narrowed_paging_root(self):
        from analyze_results import audit_summary
        data = copy.deepcopy(self.valid_artifact)
        data.update({
            "phase": "phase1", "config": "R0_stock", "dataset_mode": "real_2692",
            "profile": "paging", "mode": "paging", "_path": "fake/path.json",
            "paging_root": {
                "path": "/corpus/Fiction/Science Fiction/99",
                "book_count": 61,
                "dataset_mode": "real_2692",
                "library_book_count": 2692,
            },
        })
        summary = audit_summary([data])
        self.assertEqual(
            summary["paging_roots"]["phase1:R0_stock:real_2692:paging:paging"],
            "99 (61 of 2692 books)",
        )

    # --- library root vs. narrowed paging root ---

    @staticmethod
    def _make_library(tmp: Path, root_books: int, folders: dict[str, int]) -> Path:
        library = tmp / "lib"
        library.mkdir(parents=True)
        for index in range(root_books):
            (library / f"root_{index:05d}.epub").write_text("x")
        for name, count in folders.items():
            folder = library / name
            folder.mkdir()
            for index in range(count):
                (folder / f"{name}_{index:05d}.epub").write_text("x")
        return library

    def test_root_with_enough_books_is_not_narrowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = self._make_library(
                Path(tmp), PAGING_MIN_ROOT_BOOKS, {"folderX": 50})
            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertEqual(decoded["root_book_count"], PAGING_MIN_ROOT_BOOKS)
            self.assertIsNone(decoded["leaf_folder"])

    def test_root_below_threshold_descends_into_fullest_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = self._make_library(
                Path(tmp), 3, {"small": 10, "big": 40})
            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertEqual(decoded["root_book_count"], 3)
            self.assertEqual(Path(decoded["leaf_folder"]).name, "big")
            self.assertEqual(decoded["leaf_folder_book_count"], 40)

    def test_flat_library_without_subfolders_is_never_narrowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = self._make_library(Path(tmp), 50, {})
            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertIsNone(decoded["leaf_folder"])

    def test_pinned_reader_book_is_near_median_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            library = Path(tmp) / "lib"
            library.mkdir()
            for name, size in (("tiny", 10), ("mid", 1000), ("huge", 500_000)):
                (library / f"{name}.epub").write_text("x" * size)
            output = Path(tmp) / "targets.json"
            write_deterministic_targets(library, output)
            decoded = json.loads(output.read_text())
            self.assertEqual(Path(decoded["reader_book"]).stem, "mid")
            self.assertEqual(decoded["reader_book_bytes"], 1000)

    # --- flat real working-corpus layout ---

    def test_real_layout_fills_root_then_neutral_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            master = Path(tmp) / "real_books"
            total = REAL_ROOT_BOOKS + REAL_FOLDER_BOOKS + 7
            for index in range(total):
                folder = master / f"Personal Series {index % 5}"
                folder.mkdir(parents=True, exist_ok=True)
                (folder / f"book_{index:05d}.epub").write_text("x")
            books = sorted(master.rglob("*.epub"))
            layout = plan_real_corpus_layout(master, books)

            self.assertEqual(len(layout), total)
            root = [rel for _, rel in layout if rel.parent == Path(".")]
            self.assertEqual(len(root), REAL_ROOT_BOOKS)
            buckets: dict[str, int] = {}
            for _, rel in layout:
                if rel.parent != Path("."):
                    buckets[rel.parts[0]] = buckets.get(rel.parts[0], 0) + 1
            self.assertEqual(buckets, {"folder1": REAL_FOLDER_BOOKS, "folder2": 7})
            self.assertEqual(max(len(rel.parts) for _, rel in layout), 2)
            # No personal folder name survives into the working corpus.
            self.assertFalse(any("Personal" in str(rel) for _, rel in layout))

    def test_real_layout_preserves_every_book_on_filename_collision(self):
        with tempfile.TemporaryDirectory() as tmp:
            master = Path(tmp) / "real_books"
            for index in range(4):
                folder = master / f"tree{index}"
                folder.mkdir(parents=True)
                (folder / "Same Title.epub").write_text("x")
            books = sorted(master.rglob("*.epub"))
            layout = plan_real_corpus_layout(master, books)
            targets = [rel for _, rel in layout]
            self.assertEqual(len(layout), 4)
            self.assertEqual(len(set(targets)), 4, targets)

    def test_real_layout_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            master = Path(tmp) / "real_books"
            master.mkdir()
            for index in range(20):
                (master / f"b{index:03d}.epub").write_text("x")
            books = sorted(master.rglob("*.epub"))
            first = plan_real_corpus_layout(master, books)
            second = plan_real_corpus_layout(master, list(reversed(books)))
            self.assertEqual(dict(first), dict(second))

    def test_publishable_corpus_manifest_excludes_stable_path_identifiers(self):
        with tempfile.TemporaryDirectory() as tmp:
            master = Path(tmp) / "real_books"
            private_folder = master / "Private collection"
            private_folder.mkdir(parents=True)
            for index in range(2692):
                (private_folder / f"Personal title {index:04d}.epub").write_text("x")
            output = Path(tmp) / "real_corpus_manifest.json"

            write_corpus_manifest(master, output)

            manifest = json.loads(output.read_text())
            self.assertNotIn("selected_anonymous_ids", manifest)
            self.assertEqual(manifest["book_count"], 2692)
            self.assertNotIn("Private collection", output.read_text())
            self.assertNotIn("Personal title.epub", output.read_text())


if __name__ == "__main__":
    unittest.main()
