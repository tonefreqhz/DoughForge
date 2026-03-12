# Quick Start Guide

*DoughForge — Reproducible Self-Publishing Kit*

---

This guide gets you from a blank terminal to a built cover, a packaged EPUB,
and a print-ready PDF. It assumes you have cloned the repo and are sitting at
the repo root. Nothing here is theoretical — every path and every command has
been verified against a live build.

---

## What You Are Building

DoughForge is a book that is also its own build system. The manuscript lives in
`publication/your_book.md`. The outputs — EPUB, PDF, DOCX — are generated
artefacts. You never edit the outputs directly. You edit the manuscript, run
the build, and the outputs follow.

The single source of truth for all paths is `anchor.py`. If you ever lose your
bearings, run it:

    python anchor.py

You will see something like this:

    [OK] Repo Root:   C:\path\to\DoughForge
    [OK] Manuscript:  C:\path\to\DoughForge\publication\your_book.md
    [OK] Outputs:     C:\path\to\DoughForge\outputs
    [OK] Base Cover:  C:\path\to\DoughForge\assets\cover\base_cover.png
    [OK] Final Cover: C:\path\to\DoughForge\assets\cover\front_cover.jpg

All five lines must read `[OK]` before you build. If any read `[MISSING]`,
stop and resolve before proceeding. This is the W⚓ Protocol: anchor first,
build second, never the other way around.

---

## Prerequisites

Install these once. They do not change between builds.

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.12+ | python.org |
| Pandoc | 3.x | pandoc.org |
| Pillow | latest | `pip install pillow` |
| PyYAML | latest | `pip install pyyaml` |

Verify your environment:

    python --version
    pandoc --version

If either command fails, install the missing tool before continuing.

---

## Step 1 — Confirm Your Anchor

From the repo root:

    python anchor.py

All five paths must show `[OK]`. This is not optional. It takes three seconds
and it has saved hours.

---

## Step 2 — Configure Your Book

Open `book.yaml`. This file controls the title, author, chapter order, and
cover image path. The current configuration for this volume is:

    title    : "DoughForge"
    subtitle : "Reproducible Pub Kit"
    author   : "Roger G Lewis"
    language : en
    publisher: "DoughForge Press"

The chapter list runs from `Ch0.0-SeriesIntroduction.md` through
`Ch0.7-TheGreySpace.md`. To add a chapter, add an entry to the `chapters:`
block and create the corresponding file in `chapters/`. The build will pick
it up automatically.

---

## Step 3 — Build the Cover

The cover compositor reads `assets/cover/base_cover.png` and writes
`assets/cover/front_cover.jpg`. Both paths are confirmed by `anchor.py`.

    python scripts/build_cover.py

Output: `assets/cover/front_cover.jpg`

If the script reports a missing base cover, check `[OK] Base Cover` in your
anchor output. If it reads `[MISSING]`, the source image is absent — place
your base cover PNG at `assets/cover/base_cover.png` and re-run.

---

## Step 4 — Build the EPUB

    python scripts/build_epub.py

Output: `outputs/doughforge.epub`

Note: the output lives in `outputs/` — not `dist/`, not `build/`. The
`outputs/` directory is the only place generated artefacts are written.
This is enforced by `anchor.py`. Do not move outputs manually.

---

## Step 5 — Build the PDF

    python scripts/build_pdf.py

Output: `outputs/doughforge.pdf`

The PDF build uses `preamble.tex` for typography settings. If you are
customising fonts or margins, edit `preamble.tex` — not the Pandoc command
directly. The canonical Pandoc command lives in `anchor.py` as `BUILD_PDF`
and is the only version that should ever be run.

---

## Step 6 — Proofread

Open `outputs/doughforge.epub` in Calibre or upload directly to
Draft2Digital for preview. For the PDF, open in any PDF viewer and check:

- Cover image renders correctly
- Chapter headings are consistent
- No orphaned lines at page breaks
- Page numbers present (print edition)

Do not edit `outputs/` directly. If you find an error, fix it in
`publication/your_book.md` or the relevant `chapters/` file, then rebuild.

---

## The W⚓ Protocol — Emergency Reset

If the build breaks and you cannot identify why, run the three-step reset:

1. `python anchor.py` — confirm all paths OK
2. Check `book.yaml` — confirm chapter files exist on disk
3. Delete `outputs/` contents and rebuild from Step 3

If all three steps fail to resolve the issue, consult `ANCHOR.md` at the
repo root. It contains the full path registry and the canonical build
commands. That file is the manual override.

---

## What Comes Next

This volume — *DoughForge: Reproducible Pub Kit* — is Volume 0 of the
Home@ix series. It documents the build system by being built with it.
The chapters that follow are not a manual. They are a record of the
Mental Fight required to make reproducible publishing work in practice:
the errors, the resets, the decisions, and the reasoning behind them.

Volume 2 will extend the kit for technical authors: equations, citations,
FAIR data outputs, and integration with the `hom-ixFAIRindex` research
pipeline. That work begins when this volume ships.

For now: anchor, build, publish.

---

*Generated against anchor state: all five paths [OK] — 9 March 2026*
