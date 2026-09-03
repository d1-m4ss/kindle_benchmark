#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "=========================================="
echo "Preparing Deterministic EPUB Libraries (Flat + Hierarchical)"
echo "=========================================="

mkdir -p libraries
uv run --with pillow python3 scripts/generate_library.py libraries both 50 250 1000 2000

echo "Libraries ready: Flat & Hierarchical (50, 250, 1000, 2000 books)."
