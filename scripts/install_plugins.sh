#!/usr/bin/env bash
# Restore the Obsidian community plugins (with settings) from the Landlab-SSIIM vault.
set -euo pipefail
SRC="${1:-$HOME/Documents/Landlab-SSIIM-Vault/.obsidian}"
DST="$(cd "$(dirname "$0")/.." && pwd)/.obsidian"
mkdir -p "$DST/plugins"
cp -a "$SRC/plugins/." "$DST/plugins/"
cp -n "$SRC/community-plugins.json" "$DST/community-plugins.json" || true
echo "installed $(ls "$DST/plugins" | wc -l) plugin folders into $DST/plugins"
