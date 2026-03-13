Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

try {
    $repoRoot = & git rev-parse --show-toplevel 2>$null
    if (-not $repoRoot) { throw "git failed" }
    $repoRoot = $repoRoot.Trim().Replace("/", "\")
} catch {
    Write-Host "ANCHOR FAIL: Could not detect repo root via git." -ForegroundColor Red
    exit 1
}

Set-Location $repoRoot
Write-Host "ANCHOR: cd to $repoRoot" -ForegroundColor Cyan

$anchorScript = Join-Path $repoRoot "anchor.py"
if (-not (Test-Path $anchorScript)) {
    Write-Host "ANCHOR FAIL: anchor.py not found." -ForegroundColor Red
    exit 1
}

$anchorOutput = & py $anchorScript 2>&1
$anchorOutput | Write-Host

function Get-AnchorHash($text) {
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($text -join "`n")
    $sha   = [System.Security.Cryptography.SHA256]::Create()
    return [BitConverter]::ToString($sha.ComputeHash($bytes)).Replace("-","").ToLower()
}

$hashFile    = Join-Path $repoRoot ".anchor_hash"
$currentHash = Get-AnchorHash $anchorOutput

if (Test-Path $hashFile) {
    $storedHash = (Get-Content $hashFile -Raw).Trim()
    if ($currentHash -eq $storedHash) {
        Write-Host "ANCHOR VERIFIED — no drift detected." -ForegroundColor Green
    } else {
        Write-Host "DRIFT DETECTED — environment has changed since last anchor." -ForegroundColor Yellow
        Write-Host "If intentional: Remove-Item .anchor_hash ; .\AutoAnchor.ps1" -ForegroundColor Yellow
        Write-Host "DO NOT PROCEED until drift is resolved." -ForegroundColor Red
        exit 1
    }
} else {
    Set-Content -Path $hashFile -Value $currentHash -NoNewline
    Write-Host "INITIAL ANCHOR SET — hash stored in .anchor_hash" -ForegroundColor Green
    Write-Host "Commit .anchor_hash to git." -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Session anchored. Safe to proceed." -ForegroundColor Green
