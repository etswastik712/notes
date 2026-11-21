#!/usr/bin/env bash
# Open Joy Monteiro's EC2113 course site from the vault's offline copy (works with no internet, even if the site is removed).
# Most pages also open by double-click (file://), but the CERES explorer loads ES modules and data with fetch(), which
# browsers block on file://, so this serves the folder on http://localhost instead.
#   bash scripts/joy_site_offline.sh          (Ctrl-C to stop)
DIR="$(cd "$(dirname "$0")/.." && pwd)/earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science"
PORT="${PORT:-8765}"
URL="http://localhost:$PORT/index.html"
echo "Serving $DIR at $URL"
( sleep 1; xdg-open "$URL" >/dev/null 2>&1 ) &
exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$DIR"
