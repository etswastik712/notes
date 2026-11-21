#!/usr/bin/env bash
# Set up (or update) the "notes" second-brain vault on any Linux/macOS desktop.
#
#   curl -fsSL <release asset URL> -o setup_vault.sh   (or: gh release download vault-setup -R etswastik712/notes -p setup_vault.sh)
#   bash setup_vault.sh [TARGET_DIR]          default TARGET_DIR: ~/Documents/notes
#   bash setup_vault.sh [TARGET_DIR] --no-python
#
# What it does: clone the private repo (or fast-forward pull if it is already there), restore the Obsidian
# community plugins from the GitHub release "vault-setup" (they are gitignored), build the Python .venv from
# requirements.txt, check optional tools, and print what is left to do by hand (books, Classroom login).
# Re-run it any time to bring the vault up to date.
set -euo pipefail
REPO="etswastik712/notes"
TAG="vault-setup"
TARGET="${HOME}/Documents/notes"
PYTHON=1
for a in "$@"; do
  case "$a" in
    --no-python) PYTHON=0 ;;
    -h|--help) sed -n '2,14p' "$0"; exit 0 ;;
    *) TARGET="$a" ;;
  esac
done
say() { printf '\n\033[1;34m==> %s\033[0m\n' "$*"; }
warn() { printf '\033[1;33m[!] %s\033[0m\n' "$*"; }
have() { command -v "$1" >/dev/null 2>&1; }

have git || { echo "git is required (install it, then re-run)."; exit 1; }

# 1. authentication (the repository is private)
USE_GH=0
if have gh; then
  if ! gh auth status >/dev/null 2>&1; then say "Logging in to GitHub (gh)"; gh auth login; fi
  USE_GH=1
else
  warn "GitHub CLI 'gh' not found: git will ask for your GitHub username and a personal access token (repo scope)."
  warn "Plugins are then downloaded only if you install gh (https://cli.github.com) and re-run."
fi

# 2. clone or update
if [ -d "$TARGET/.git" ]; then
  say "Updating $TARGET"
  git -C "$TARGET" pull --ff-only || warn "pull failed (local changes?): resolve with 'git -C \"$TARGET\" status' and re-run"
else
  say "Cloning $REPO into $TARGET"
  mkdir -p "$(dirname "$TARGET")"
  if [ "$USE_GH" = 1 ]; then gh repo clone "$REPO" "$TARGET"; else git clone "https://github.com/$REPO.git" "$TARGET"; fi
fi
cd "$TARGET"

# 3. Obsidian plugins (gitignored binaries, shipped as a release asset)
if [ ! -d .obsidian/plugins ] || [ -z "$(ls -A .obsidian/plugins 2>/dev/null)" ] || [ "${REFRESH_PLUGINS:-0}" = 1 ]; then
  if [ "$USE_GH" = 1 ]; then
    say "Installing Obsidian plugins from release '$TAG'"
    tmp="$(mktemp -d)"
    gh release download "$TAG" -R "$REPO" -p "obsidian-plugins.tar.gz" -D "$tmp"
    mkdir -p .obsidian
    tar -xzf "$tmp/obsidian-plugins.tar.gz" -C .obsidian
    rm -rf "$tmp"
  else
    warn "Skipping plugins (needs gh)."
  fi
else
  say "Obsidian plugins already present (REFRESH_PLUGINS=1 to reinstall)"
fi

# 4. Python environment for the scripts
if [ "$PYTHON" = 1 ]; then
  if have python3; then
    say "Python environment (.venv)"
    if have uv; then
      [ -d .venv ] || uv venv .venv
      uv pip install --python .venv/bin/python -r requirements.txt
    else
      [ -d .venv ] || python3 -m venv .venv
      .venv/bin/python -m pip install --upgrade pip -q
      .venv/bin/python -m pip install -r requirements.txt -q
    fi
  else
    warn "python3 not found: skipping .venv (the vault itself works without it; only scripts/ need it)."
  fi
fi

# 5. optional tools used by some scripts
say "Optional tools"
for t in pdftotext pdftoppm tesseract rsync firefox node; do
  if have "$t"; then echo "  ok      $t"; else echo "  missing $t"; fi
done
echo "  (pdftotext/pdftoppm = poppler-utils; tesseract = OCR; firefox = slide-PDF and tool screenshots; node = tool syntax checks)"

# 6. what is left
say "Done: $TARGET"
cat <<MSG
Next steps
  1. Obsidian: "Open folder as vault" -> $TARGET. Settings -> Community plugins -> turn off Restricted mode.
     Start at 00-Home/Home.md; 00-Home/PROGRESS.md has the full state.
  2. Books are NOT in git (about 8 GB, gitignored: <area>/*/books/). Copy them from your main machine, e.g.
       rsync -av --include='*/' --include='*/books/***' --exclude='*' main-pc:Documents/notes/ "$TARGET/"
  3. Classroom/Drive sync (optional): put the OAuth client JSON at ~/.config/vault-sync/client_secret.json, then
       .venv/bin/python scripts/classroom_sync.py auth
  4. Joy's course site works offline:  bash scripts/joy_site_offline.sh
  5. Re-run this script to update. Note: the main machine auto-commits and pushes (Kurooto); commit here
     only if you also push, and pull before editing to avoid conflicts.
MSG
