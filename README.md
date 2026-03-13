## 🔒 Session Anchor — Start Here Every Time

Before every session (human or AI), run:

``powershell
cd "<YOUR_REPO_ROOT>"
.\AutoAnchor.ps1
````n
Paste the full output into your AI prompt before asking anything else.
**ANCHOR VERIFIED — no drift detected.** means you are safe to proceed.
Never skip this step. Never assume the shell is already in the right place.

---

## 🔒 Session Anchor — Start Here Every Time

Before every session (human or AI), run:

``powershell
cd "<YOUR_REPO_ROOT>"
.\AutoAnchor.ps1
````n
Paste the full output into your AI prompt before asking anything else.
**ANCHOR VERIFIED — no drift detected.** means you are safe to proceed.
Never skip this step. Never assume the shell is already in the right place.

---

# DoughForge

A publishing pipeline for independent authors, built on the W-Anchor Protocol.

## What This Is

DoughForge is a book project and a toolkit. It contains:

- **The manuscript** — *The Conquest of DoughForge*
- **The pipeline** — Pandoc builds producing EPUB, PDF, and DOCX from one Markdown source
- **The anchor** — `anchor.py`, a path verifier that keeps every session grounded

## Quick Start

### Step 0 — Install the W-Anchor hook (once, after cloning)

    .\setup.ps1

This installs anchor.py as an automatic post-checkout hook and stores your
baseline hash. Every future git checkout re-verifies your file tree automatically.

### Step 1 — Verify your environment before every LLM session

    .\anchor_verify.ps1

Paste the full output into your AI prompt before asking anything else.
The model is then reading from the same ground truth as your file system.

### Step 2 — Build commands

Build commands:

    pandoc publication\your_book.md -o outputs\your_book.docx
    pandoc publication\your_book.md --epub-cover-image="assets\cover\front_cover.jpg" -o outputs\your_book.epub
    pandoc publication\your_book.md --pdf-engine=lualatex --include-in-header=preamble.tex -o outputs\your_book.pdf

## The W-Anchor Protocol

Context drift is what happens when an AI assistant forgets what you agreed on three hours ago.
The W-Anchor Protocol prevents it by keeping a single document — ANCHOR.md — that both
human and AI read at the start of every session.

Full documentation: ANCHOR.md

## Folder Structure

    publication/       the manuscript lives here — edit this, never the outputs
    outputs/           generated EPUB, PDF, DOCX files — never edit directly
    assets/cover/      cover images
    scripts/           build helper scripts
    docs/              documentation and session archive
    anchor.py          run this to verify your build environment
    preamble.tex       LaTeX settings for PDF builds
    book.yaml          chapter list and EPUB metadata

## Related

reproducible-self-pub-kit: https://github.com/tonefreqhz/reproducible-self-pub-kit

## Licence

MIT
