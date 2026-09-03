#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "=========================================="
echo "Starting KOReader Benchmark Validation (long phases require explicit flags)"
echo "=========================================="

# This entry point is deliberately validation-only. Phase 1/2 must be started
# explicitly with scripts/run_benchmarks.py --phase1/--phase2.
if [ ! -d "libraries/flat/books_50" ]; then
    echo "Missing validation corpus: libraries/flat/books_50" >&2
    exit 1
fi

CAMPAIGN="${CAMPAIGN:-$(date +%F)}"
python3 scripts/run_benchmarks.py --validate --campaign "${CAMPAIGN}" --lanes 1

echo "=========================================="
echo "Validation finished. No Phase 1/Phase 2 job was started."
echo "=========================================="
