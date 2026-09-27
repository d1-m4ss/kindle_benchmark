"""Regressions: legacy configuration, truncated PNG, mutable source and fake paint."""
import copy
import dataclasses
import struct
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import run_benchmarks as runner


class MeasurementContract(unittest.TestCase):
    def test_png_with_only_ihdr_is_not_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'truncated.png'
            path.write_bytes(b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13)
                             + b'IHDR' + struct.pack('>II', 1236, 1648))
            self.assertFalse(runner.verify_png_file(path)[0])

    def test_rebuild_settings_are_written_to_actual_store(self):
        with tempfile.TemporaryDirectory() as tmp:
            job = runner.Job('contract', 'opt', 'opt', 'M_leanui', ('leanui',),
                             tmp, str(Path(tmp) / 'home'), 'warm', 'paging',
                             'flat', 500, 0, 30, False)
            runner.setup_isolated_home(job)
            self.assertTrue((Path(job.ko_home) / 'settings/leanui_settings.lua').is_file())

    def test_contract_rejects_unverified_measurements(self):
        validate = getattr(runner, 'measurement_errors', None)
        self.assertTrue(callable(validate), 'measurement validator missing')
        valid = {'effective_library_mode': 'compact_list',
                 'plugin_files_sha256': 'a' * 64, 'effective_config_sha256': 'b' * 64,
                 'source_verified': True, 'memory_method': 'getrusage_peak;current_unavailable',
                 'rss_current_kib': None, 'rss_current_reason': 'not sampled',
                 'scenarios': {'library_sequential_paging': {'iterations': [{
                     'status': 'PASS', 'action_cpu_ms': 2, 'first_content_paint_ms': 4,
                     'settled_verified_ms': 16, 'wall_time_ms': 16,
                     'paint_target_verified': True}]}}}
        self.assertEqual(validate(valid, 'compact_list'), [])
        for key, value in [('effective_library_mode', 'cover_grid'),
                           ('source_verified', False), ('plugin_files_sha256', ''),
                           ('memory_method', 'rss_current=getrusage')]:
            with self.subTest(key=key):
                bad = copy.deepcopy(valid); bad[key] = value
                self.assertTrue(validate(bad, 'compact_list'))
        for key, value in [('first_content_paint_ms', None),
                           ('paint_target_verified', False), ('settled_verified_ms', -1)]:
            with self.subTest(key=key):
                bad = copy.deepcopy(valid)
                bad['scenarios']['library_sequential_paging']['iterations'][0][key] = value
                self.assertTrue(validate(bad, 'compact_list'))

    def test_plugin_manifest_detects_file_changes_not_path_changes(self):
        manifest = getattr(runner, 'plugin_tree_sha256', None)
        self.assertTrue(callable(manifest), 'source identity missing')
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / 'a', Path(tmp) / 'b'
            a.mkdir(); b.mkdir()
            (a / 'main.lua').write_text('return 1'); (b / 'main.lua').write_text('return 1')
            self.assertEqual(manifest(a), manifest(b))
            (b / 'main.lua').write_text('return 2')
            self.assertNotEqual(manifest(a), manifest(b))


if __name__ == '__main__':
    unittest.main()
