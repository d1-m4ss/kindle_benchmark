#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

echo "=========================================="
echo "KOReader Benchmark Suite - Setup"
echo "=========================================="

OS="$(uname -s)"
ARCH="$(uname -m)"
echo "Host OS: ${OS} (${ARCH})"

if [[ "${OS}" == "Darwin" ]]; then
    if ! command -v brew >/dev/null 2>&1; then
        echo "Error: Homebrew is required on macOS."
        exit 1
    fi
    echo "Installing required build prerequisites via Homebrew..."
    brew install autoconf automake binutils findutils gnu-getopt libtool make meson nasm ninja pkgconf sdl3 util-linux wget python uv || true
fi

# versions.lock.json is the single source of truth for every pinned revision.
# Bump a version there and re-run this script; nothing below hardcodes a SHA.
LOCK="${SCRIPT_DIR}/versions.lock.json"
if [ ! -f "${LOCK}" ]; then
    echo "Error: versions.lock.json not found at ${LOCK}" >&2
    exit 1
fi

lock_field() {
    python3 -c '
import json, sys
lock = json.load(open(sys.argv[1]))
node = lock if sys.argv[2] == "koreader" else lock["plugins"][sys.argv[2]]
value = node.get(sys.argv[3]) if sys.argv[2] != "koreader" else lock["koreader"].get(sys.argv[3])
if not value:
    raise SystemExit(f"missing {sys.argv[2]}.{sys.argv[3]} in versions.lock.json")
print(value)
' "${LOCK}" "$1" "$2"
}

plugin_names() {
    python3 -c '
import json, sys
print("\n".join(json.load(open(sys.argv[1]))["plugins"]))
' "${LOCK}"
}

echo "Pinned revisions (from versions.lock.json):"
python3 -c '
import json, sys
lock = json.load(open(sys.argv[1]))
rows = [("koreader", lock["koreader"])] + list(lock["plugins"].items())
for name, info in rows:
    print("  %-14s %-20s %s" % (name, info["tag"], info["commit"]))
' "${LOCK}"

KOREADER_REPO="$(lock_field koreader repo)"
KOREADER_SHA="$(lock_field koreader commit)"
KOREADER_TAG="$(lock_field koreader tag)"

if [ ! -d "koreader_src" ]; then
    echo "Cloning KOReader repository (${KOREADER_TAG})..."
    git clone "${KOREADER_REPO}" koreader_src
fi

cd koreader_src
echo "Checking out KOReader ${KOREADER_TAG} (${KOREADER_SHA})..."
git fetch --tags --quiet origin || true
git checkout "${KOREADER_SHA}"

# Fetch KOReader thirdparty dependencies
echo "Fetching KOReader thirdparty submodules..."
if command -v brew >/dev/null 2>&1; then
    export PATH="$(brew --prefix)/opt/findutils/libexec/gnubin:$(brew --prefix)/opt/gnu-getopt/bin:$(brew --prefix)/opt/make/libexec/gnubin:$(brew --prefix)/opt/util-linux/bin:${PATH}"
fi
./kodev fetch-thirdparty
cd "${SCRIPT_DIR}"

# Clone plugin repositories and checkout pinned SHAs
mkdir -p plugins_source
cd plugins_source

clone_and_pin() {
    local name="$1"
    local url="$2"
    local sha="$3"
    local tag="$4"
    if [ ! -d "${name}" ]; then
        echo "Cloning plugin: ${name} (${url})..."
        git clone "${url}" "${name}"
    fi
    echo "Checking out ${name} ${tag} (${sha})..."
    cd "${name}"
    git fetch --tags --quiet origin || true
    git checkout "${sha}"
    cd ..
}

while read -r plugin; do
    [ -n "${plugin}" ] || continue
    clone_and_pin "${plugin}" \
        "$(lock_field "${plugin}" repo)" \
        "$(lock_field "${plugin}" commit)" \
        "$(lock_field "${plugin}" tag)"
done < <(plugin_names)

cd "${SCRIPT_DIR}"

# Fail loudly if any checkout drifted from versions.lock.json.
python3 -c '
import json, subprocess, sys
lock = json.load(open(sys.argv[1]))
entries = [("koreader", lock["koreader"])] + list(lock["plugins"].items())
bad = []
for name, info in entries:
    head = subprocess.check_output(
        ["git", "-C", info["checkout_path"], "rev-parse", "HEAD"], text=True).strip()
    if head != info["commit"]:
        bad.append("%s: expected %s (%s), got %s" % (name, info["commit"], info["tag"], head))
if bad:
    raise SystemExit("Pinned revision mismatch:\n  " + "\n  ".join(bad))
print("All checkouts match versions.lock.json.")
' "${LOCK}"

echo "Setup and pinned SHA verification completed successfully."
