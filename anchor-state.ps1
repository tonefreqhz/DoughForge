# ============================================================
# DOUGHFORGE ANCHOR STATE
# Going Direct Paradigm — Part Zero Preface Sequence
# Roger G. Lewis — Grub Street In Exile
# Last updated: 2026-03-08
# ============================================================

# Part Zero — The Poet Who Needed a Workflow
# Ch 0.0 — TO DRAFT:  "Series Introduction"
# Ch 0.1 — DRAFTED:   "The Unacknowledged Legislator Writes a Build Script"
# Ch 0.2 — DRAFTED:   "The Ration Still Arriving"
# Ch 0.3 — DRAFTED:   "Who Do We Owe This Money To, Exactly?"
# Ch 0.4 — DRAFTED:   "The Moral Sign"
# Ch 0.5 — DRAFTED:   "The Dying Bird and the Plumage"
# Ch 0.6 — DRAFTED:   "The Formula and the Counter-Spell"
# Ch 0.7 — DRAFTED:   "The Grey Space"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DOUGHFORGE ANCHOR STATE — Going Direct Paradigm" -ForegroundColor Cyan
Write-Host " Part Zero: The Poet Who Needed a Workflow" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ch 0.0 — TO DRAFT : Series Introduction" -ForegroundColor Yellow
Write-Host "Ch 0.1 — DRAFTED  : The Unacknowledged Legislator Writes a Build Script" -ForegroundColor Green
Write-Host "Ch 0.2 — DRAFTED  : The Ration Still Arriving" -ForegroundColor Green
Write-Host "Ch 0.3 — DRAFTED  : Who Do We Owe This Money To, Exactly?" -ForegroundColor Green
Write-Host "Ch 0.4 — DRAFTED  : The Moral Sign" -ForegroundColor Green
Write-Host "Ch 0.5 — DRAFTED  : The Dying Bird and the Plumage" -ForegroundColor Green
Write-Host "Ch 0.6 — DRAFTED  : The Formula and the Counter-Spell" -ForegroundColor Green
Write-Host "Ch 0.7 — DRAFTED  : The Grey Space" -ForegroundColor Green
Write-Host ""

$AnchorState = @(
    [PSCustomObject]@{ Chapter = "0.0"; Title = "Series Introduction"; Status = "TO DRAFT" },
    [PSCustomObject]@{ Chapter = "0.1"; Title = "The Unacknowledged Legislator Writes a Build Script"; Status = "DRAFTED" },
    [PSCustomObject]@{ Chapter = "0.2"; Title = "The Ration Still Arriving"; Status = "DRAFTED" },
    [PSCustomObject]@{ Chapter = "0.3"; Title = "Who Do We Owe This Money To, Exactly?"; Status = "DRAFTED" },
    [PSCustomObject]@{ Chapter = "0.4"; Title = "The Moral Sign"; Status = "DRAFTED" },
    [PSCustomObject]@{ Chapter = "0.5"; Title = "The Dying Bird and the Plumage"; Status = "DRAFTED" },
    [PSCustomObject]@{ Chapter = "0.6"; Title = "The Formula and the Counter-Spell"; Status = "DRAFTED" },
    [PSCustomObject]@{ Chapter = "0.7"; Title = "The Grey Space"; Status = "DRAFTED" }
)

$AnchorState | Format-Table -AutoSize

$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$Drafted   = ($AnchorState | Where-Object { $_.Status -eq "DRAFTED" }).Count
$ToDraft   = ($AnchorState | Where-Object { $_.Status -eq "TO DRAFT" }).Count

$LogEntry = @"
[$Timestamp]
  Drafted  : $Drafted chapters
  To Draft : $ToDraft chapters
  Next     : Ch 0.0 — Series Introduction
  Note     : The machine cannot parse the human without a wrapper.
             The wrapper is the workflow. The workflow is the loom.
"@

Add-Content -Path ".\doughforge-log.txt" -Value $LogEntry
Add-Content -Path ".\doughforge-log.txt" -Value "------------------------------------------------------------"

Write-Host "Log entry written to: doughforge-log.txt" -ForegroundColor Cyan
Write-Host ""
