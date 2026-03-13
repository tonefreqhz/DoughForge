$repoRoot = & git rev-parse --show-toplevel 2>$null
if (-not $repoRoot) { Write-Host "Not a git repo."; exit 1 }
$repoRoot = $repoRoot.Trim().Replace("/","\")
Set-Location $repoRoot

$hooksDir = Join-Path $repoRoot ".git\hooks"

$postCheckout = "#!/bin/sh`ncd `"`$(git rev-parse --show-toplevel)`"`necho 'W-Anchor: Running anchor.py...`npy anchor.py"
$postMerge    = "#!/bin/sh`ncd `"`$(git rev-parse --show-toplevel)`"`necho 'W-Anchor: Re-verifying anchor after pull...`npy anchor.py"

Set-Content -Path "$hooksDir\post-checkout" -Value $postCheckout -NoNewline
Set-Content -Path "$hooksDir\post-merge"    -Value $postMerge    -NoNewline

Write-Host "Git hooks installed." -ForegroundColor Green
Write-Host "  post-checkout -> anchor.py runs after clone/branch switch"
Write-Host "  post-merge    -> anchor.py runs after pull"
