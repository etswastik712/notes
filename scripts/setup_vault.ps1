# Set up (or update) the "notes" second-brain vault on a Windows desktop (PowerShell 5+).
#   gh release download vault-setup -R etswastik712/notes -p setup_vault.ps1
#   powershell -ExecutionPolicy Bypass -File setup_vault.ps1 [-Target C:\Users\you\Documents\notes] [-NoPython]
# Clones the private repo (or pulls), restores the Obsidian plugins from release "vault-setup",
# builds the Python .venv, and prints the manual steps. Re-run any time to update.
param([string]$Target = "$HOME\Documents\notes", [switch]$NoPython)
$ErrorActionPreference = "Stop"
$Repo = "etswastik712/notes"; $Tag = "vault-setup"
function Say($m) { Write-Host "`n==> $m" -ForegroundColor Cyan }
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
if (-not (Have git)) { Write-Host "git is required: https://git-scm.com/download/win"; exit 1 }
$UseGh = Have gh
if ($UseGh) { gh auth status *> $null; if ($LASTEXITCODE -ne 0) { Say "Logging in to GitHub"; gh auth login } }
else { Write-Warning "GitHub CLI 'gh' not found (winget install GitHub.cli). git will ask for a username and token; plugins need gh." }

if (Test-Path "$Target\.git") { Say "Updating $Target"; git -C $Target pull --ff-only }
else {
  Say "Cloning $Repo into $Target"
  New-Item -ItemType Directory -Force -Path (Split-Path $Target) | Out-Null
  if ($UseGh) { gh repo clone $Repo $Target } else { git clone "https://github.com/$Repo.git" $Target }
}
Set-Location $Target
git config core.longpaths true   # deep paths in the course-site mirror

$plug = ".obsidian\plugins"
if ((-not (Test-Path $plug)) -or (-not (Get-ChildItem $plug -ErrorAction SilentlyContinue)) -or $env:REFRESH_PLUGINS -eq "1") {
  if ($UseGh) {
    Say "Installing Obsidian plugins from release '$Tag'"
    $tmp = Join-Path $env:TEMP ("vault-plugins-" + [guid]::NewGuid())
    gh release download $Tag -R $Repo -p "obsidian-plugins.zip" -D $tmp
    New-Item -ItemType Directory -Force -Path ".obsidian" | Out-Null
    Expand-Archive -Force "$tmp\obsidian-plugins.zip" -DestinationPath ".obsidian"
    Remove-Item -Recurse -Force $tmp
  } else { Write-Warning "Skipping plugins (needs gh)." }
} else { Say "Obsidian plugins already present (set REFRESH_PLUGINS=1 to reinstall)" }

if (-not $NoPython) {
  $py = if (Have py) { "py" } elseif (Have python) { "python" } else { $null }
  if ($py) {
    Say "Python environment (.venv)"
    if (-not (Test-Path ".venv")) { & $py -m venv .venv }
    & .\.venv\Scripts\python.exe -m pip install --upgrade pip -q
    & .\.venv\Scripts\python.exe -m pip install -r requirements.txt -q
  } else { Write-Warning "Python not found: skipping .venv (only scripts\ need it)." }
}

Say "Optional tools"
foreach ($t in "pdftotext","pdftoppm","tesseract","firefox","node") { if (Have $t) { "  ok      $t" } else { "  missing $t" } }

Say "Done: $Target"
@"
Next steps
  1. Obsidian: Open folder as vault -> $Target. Settings -> Community plugins -> turn off Restricted mode.
  2. Books are NOT in git (~8 GB, <area>\*\books\): copy them from your main machine.
  3. Classroom/Drive sync (optional): put the OAuth client JSON at %USERPROFILE%\.config\vault-sync\client_secret.json, then
       .\.venv\Scripts\python.exe scripts\classroom_sync.py auth
  4. Re-run this script to update. The main machine auto-commits and pushes; pull before editing here.
"@
