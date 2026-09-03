#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "=========================================="
echo "KOReader Benchmark Suite - Build Emulator"
echo "=========================================="

if [ ! -d "koreader_src" ]; then
    echo "koreader_src not found. Running setup.sh first..."
    ./setup.sh
fi

cd koreader_src
if command -v brew >/dev/null 2>&1; then
    export PATH="$(brew --prefix)/opt/findutils/libexec/gnubin:$(brew --prefix)/opt/gnu-getopt/bin:$(brew --prefix)/opt/make/libexec/gnubin:$(brew --prefix)/opt/util-linux/bin:${PATH}"
fi

echo "Building KOReader emulator..."
./kodev build

cd "${SCRIPT_DIR}"

EMU_DIR="$(ls -d koreader_src/koreader-emulator-* 2>/dev/null | head -n 1)"
if [ -z "${EMU_DIR}" ] || [ ! -f "${EMU_DIR}/koreader/luajit" ]; then
    echo "Error: KOReader emulator build failed or binary not found."
    exit 1
fi

echo "KOReader emulator successfully built at ${EMU_DIR}/koreader"
