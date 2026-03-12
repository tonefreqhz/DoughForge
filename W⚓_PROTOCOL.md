\# W⚓ (WeighAnchor) Protocol — DoughForge Reproducible Self-Pub Kit



\## Overview

W⚓ is the emergency reset mechanism in the DoughForge Reproducible Self-Pub Kit,

designed to anchor back to ground truth when builds fail. It re-fixes syntax,

re-assembles manuscripts from canonical sources, re-runs cover and build tools,

commits/pushes changes, and prepares for upload.



The goal is a "happy ending": a successful build with correct cover, title, and

PDF/EPUB output, ready for Draft2Digital publishing.



\---



\## THE 1-RUB RULE — CANONICAL ACROSS ALL REPOS



\*\*Maximum rubs: 1. This is not a suggestion. It is the protocol.\*\*



W⚓ is a diagnostic trigger, not a retry loop. If 1 rub does not resolve the

issue, stop immediately. Switch to Manual Override (see below).



Repeated W⚓ invocations add noise to Git history, risk data loss, and delay

release without improving diagnosis. The cycle of reset → fail → reset → fail

is not W⚓ working. It is W⚓ being misused.



\---



\## Before You Invoke W⚓ (Mandatory)



1\. Log the exact error message verbatim.

2\. Check canonical inputs for corruption — verify Markdown chunks are valid.

3\. Confirm environment: Python 3.8+, Pandoc, XeLaTeX installed and on PATH.

4\. Run `python anchor.py` — all paths must resolve before any build attempt.



\---



\## W⚓ Invocation (1 rub only)



1\. Reset to clean state from canonical sources.

2\. Apply the single targeted fix for the logged error.

3\. Rebuild and verify output manually: cover renders, PDF generates, EPUB opens.

4\. If successful: commit, push, tag.

5\. If still failing: \*\*STOP. Go to Manual Override immediately.\*\*



\---



\## Manual Override



Open the failing file in VS Code. Edit directly. Run tools step-by-step from

the command line. Use a Git branch for experiments — never experiment on main.

This breaks the automation loop and allows direct inspection of root cause.



\---



\## Post-Resolution



\- Document the fix in release notes.

\- Tag a stable commit.

\- Update this protocol if the fix reveals a systemic issue.



\---



\## Prevention



\- Unit tests for all tools.

\- Validate inputs on commit hooks.

\- `python anchor.py` is always the first command of every session.



\---



\*W⚓ is the anchor for quick resets. 1 rub. Diagnose first. No loops.\*

\*Canonical across: reproducible-self-pub-kit · DoughForge · hom-ixFAIRindex\*



