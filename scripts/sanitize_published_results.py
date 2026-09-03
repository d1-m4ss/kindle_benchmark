#!/usr/bin/env python3
"""Remove local filesystem values from publishable raw benchmark JSON."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


DEFAULT_REDACT_PREFIX = f"{Path.home()}/"


def redact_value(value: Any, prefix: str) -> tuple[Any, int]:
    """Hash a complete string that exposes the local home path.

    Semantic-evidence paths and visible-item signatures are used for equality
    checks while running the benchmark, not for publication. Hashing the whole
    value keeps equal evidence equal, removes book names, and leaves all
    statuses and numeric measurements untouched.
    """
    if isinstance(value, dict):
        changed = 0
        result: dict[str, Any] = {}
        for key, item in value.items():
            result[key], item_changed = redact_value(item, prefix)
            changed += item_changed
        return result, changed
    if isinstance(value, list):
        changed = 0
        result = []
        for item in value:
            sanitized, item_changed = redact_value(item, prefix)
            result.append(sanitized)
            changed += item_changed
        return result, changed
    if isinstance(value, str) and prefix in value and not value.startswith("sha256:"):
        digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
        return f"sha256:{digest}", 1
    return value, 0


def raw_files(run_dir: Path) -> list[Path]:
    files = sorted(run_dir.glob("phase*/raw/*.json"))
    if not files:
        raise ValueError(f"No raw JSON files found under {run_dir}")
    return files


def find_exposed_values(value: Any, prefix: str) -> int:
    if isinstance(value, dict):
        return sum(find_exposed_values(item, prefix) for item in value.values())
    if isinstance(value, list):
        return sum(find_exposed_values(item, prefix) for item in value)
    return int(isinstance(value, str) and prefix in value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument(
        "--redact-prefix",
        default=DEFAULT_REDACT_PREFIX,
        help="string prefix to redact (default: current user's home directory)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if any raw JSON still exposes the prefix; do not modify files",
    )
    args = parser.parse_args()

    files = raw_files(args.run_dir)
    exposed = 0
    changed = 0
    for filename in files:
        data = json.loads(filename.read_text(encoding="utf-8"))
        exposed += find_exposed_values(data, args.redact_prefix)
        if args.check:
            continue
        sanitized, file_changed = redact_value(data, args.redact_prefix)
        if file_changed:
            filename.write_text(
                json.dumps(sanitized, ensure_ascii=False, separators=(",", ":")) + "\n",
                encoding="utf-8",
            )
            changed += file_changed

    if args.check:
        if exposed:
            print(f"FAIL: {exposed} exposed local-path values in {len(files)} raw files")
            return 1
        print(f"PASS: no exposed local-path values in {len(files)} raw files")
        return 0

    print(f"Sanitized {changed} local-path values in {len(files)} raw files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
