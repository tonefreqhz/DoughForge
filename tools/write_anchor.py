# tools/_write_anchor.py
# Run once from repo root: python tools\_write_anchor.py
# Writes the canonical anchor.py — no shell quoting involved.

import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO_ROOT, "anchor.py")

CONTENT = '''\
import os

# DoughForge W\u26d3 Protocol \u2014 Single Source of Truth for All Paths
# Import anywhere with: from anchor import REPO_ROOT, PUBLICATION_DIR, etc.
#
# -----------------------------------------------------------------------
# POWERSHELL RULE \u2014 READ THIS FIRST
# -----------------------------------------------------------------------
# ALL PowerShell command sequences must begin with:
#
#   cd "C:\\\\Users\\\\peewe\\\\Documents\\\\DoughForge"
#
# This is the canonical repo root. No placeholders. No guessing.
# Never assume the shell is already in the right directory.
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# REPO ROOT
# -----------------------------------------------------------------------
REPO_ROOT         = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------
# PUBLICATION
# -----------------------------------------------------------------------
PUBLICATION_DIR   = os.path.join(REPO_ROOT, "publication")
MANUSCRIPT        = os.path.join(PUBLICATION_DIR, "your_book.md")
MANUSCRIPT_BUMPER = os.path.join(PUBLICATION_DIR, "THE CONQUEST OF DOUGHFORGE.md")

# -----------------------------------------------------------------------
# FRONT MATTER
# -----------------------------------------------------------------------
FRONT_MATTER_DIR      = os.path.join(PUBLICATION_DIR, "front_matter")
FOREWORD_FOSTER       = os.path.join(FRONT_MATTER_DIR, "foreword_foster_lewis.md")
FOREWORD_BUMPER       = os.path.join(FRONT_MATTER_DIR, "foreword_bumper.md")
DEDICATION_BUMPER     = os.path.join(FRONT_MATTER_DIR, "dedication_bumper.md")
PREFACE_BUMPER        = os.path.join(FRONT_MATTER_DIR, "preface_bumper.md")

# -----------------------------------------------------------------------
# OUTPUTS
# -----------------------------------------------------------------------
OUTPUTS_DIR        = os.path.join(REPO_ROOT, "outputs")
OUTPUT_PDF         = os.path.join(OUTPUTS_DIR, "your_book.pdf")
OUTPUT_EPUB        = os.path.join(OUTPUTS_DIR, "your_book.epub")
OUTPUT_DOCX        = os.path.join(OUTPUTS_DIR, "your_book.docx")

OUTPUT_PDF_BUMPER  = os.path.join(OUTPUTS_DIR, "conquest_of_doughforge_bumper.pdf")
OUTPUT_EPUB_BUMPER = os.path.join(OUTPUTS_DIR, "conquest_of_doughforge_bumper.epub")
OUTPUT_DOCX_BUMPER = os.path.join(OUTPUTS_DIR, "conquest_of_doughforge_bumper.docx")

# -----------------------------------------------------------------------
# ASSETS
# -----------------------------------------------------------------------
ASSETS_DIR         = os.path.join(REPO_ROOT, "assets")
COVER_DIR          = os.path.join(ASSETS_DIR, "cover")
FONTS_DIR          = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR         = os.path.join(ASSETS_DIR, "images")

BASE_COVER         = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER        = os.path.join(COVER_DIR, "front_cover.jpg")

BASE_COVER_BUMPER  = os.path.join(COVER_DIR, "base_cover_bumper.png")
FINAL_COVER_BUMPER = os.path.join(COVER_DIR, "front_cover_bumper.jpg")

# -----------------------------------------------------------------------
# TOOLS
# -----------------------------------------------------------------------
TOOLS_DIR           = os.path.join(REPO_ROOT, "tools")
PREAMBLE_TEX        = os.path.join(REPO_ROOT, "preamble.tex")
PREAMBLE_TEX_BUMPER = os.path.join(REPO_ROOT, "preamble_bumper.tex")
ANCHOR_MD           = os.path.join(REPO_ROOT, "ANCHOR.md")
PROGRESS_LOG        = os.path.join(REPO_ROOT, "INTERIM_PROGRESS_LOG.md")

# -----------------------------------------------------------------------
# BOOK METADATA
# -----------------------------------------------------------------------
BOOK_TITLE_STANDARD  = "DoughForge: The Reproducible Self-Publishing Desktop Kit"
BOOK_TITLE_BUMPER    = "The Conquest of DoughForge"
BOOK_SUBTITLE_BUMPER = "The Truth Will Set You Free \\u2014 But First It Will Piss You Off"
BOOK_AUTHOR          = "Roger G Lewis"
FOREWORD_AUTHOR      = "Foster Lewis"
EDITION_BUMPER       = "Bumper Edition"
EDITION_PRICE        = ""

# -----------------------------------------------------------------------
# POWERSHELL CD NOTE
# -----------------------------------------------------------------------
POWERSHELL_CD_NOTE = (
    "\\n  WARNING  PowerShell Rule: Always start every session with:"
    "\\n  cd \\"C:\\\\Users\\\\peewe\\\\Documents\\\\DoughForge\\""
    "\\n  Never assume the shell is already in the right place.\\n"
)

# -----------------------------------------------------------------------
# BUILD COMMANDS \\u2014 STANDARD EDITION
# -----------------------------------------------------------------------
BUILD_DOCX = (
    f\'pandoc "{MANUSCRIPT}" \'
    f\'-o "{OUTPUT_DOCX}"\\'
)

BUILD_EPUB = (
    f\'pandoc "{MANUSCRIPT}" \'
    f\'--include-before-body="{FOREWORD_FOSTER}" \'
    f\'--epub-cover-image="{FINAL_COVER}" \'
    f\'--toc \'
    f\'--toc-depth=2 \'
    f\'--epub-chapter-level=1 \'
    f\'--metadata title="{BOOK_TITLE_STANDARD}" \'
    f\'--metadata author="{BOOK_AUTHOR}" \'
    f\'-o "{OUTPUT_EPUB}"\\'
)

BUILD_PDF = (
    f\'pandoc "{MANUSCRIPT}" \'
    f\'--include-before-body="{FOREWORD_FOSTER}" \'
    f\'--pdf-engine=lualatex \'
    f\'--include-in-header="{PREAMBLE_TEX}" \'
    f\'--toc \'
    f\'--toc-depth=2 \'
    f\'--metadata title="{BOOK_TITLE_STANDARD}" \'
    f\'--metadata author="{BOOK_AUTHOR}" \'
    f\'-o "{OUTPUT_PDF}"\\'
)

# -----------------------------------------------------------------------
# BUILD COMMANDS \\u2014 BUMPER EDITION
# -----------------------------------------------------------------------
BUILD_DOCX_BUMPER = (
    f\'pandoc "{MANUSCRIPT_BUMPER}" \'
    f\'-o "{OUTPUT_DOCX_BUMPER}"\\'
)

BUILD_EPUB_BUMPER = (
    f\'pandoc "{MANUSCRIPT_BUMPER}" \'
    f\'--include-before-body="{DEDICATION_BUMPER}" \'
    f\'--include-before-body="{FOREWORD_BUMPER}" \'
    f\'--include-before-body="{PREFACE_BUMPER}" \'
    f\'--epub-cover-image="{FINAL_COVER_BUMPER}" \'
    f\'--toc \'
    f\'--toc-depth=2 \'
    f\'--epub-chapter-level=1 \'
    f\'--metadata title="{BOOK_TITLE_BUMPER}" \'
    f\'--metadata author="{BOOK_AUTHOR}" \'
    f\'-o "{OUTPUT_EPUB_BUMPER}"\\'
)

BUILD_PDF_BUMPER = (
    f\'pandoc "{MANUSCRIPT_BUMPER}" \'
    f\'--include-before-body="{DEDICATION_BUMPER}" \'
    f\'--include-before-body="{FOREWORD_BUMPER}" \'
    f\'--include-before-body="{PREFACE_BUMPER}" \'
    f\'--pdf-engine=lualatex \'
    f\'--include-in-header="{PREAMBLE_TEX_BUMPER}" \'
    f\'--toc \'
    f\'--toc-depth=2 \'
    f\'--metadata title="{BOOK_TITLE_BUMPER}" \'
    f\'--metadata author="{BOOK_AUTHOR}" \'
    f\'-o "{OUTPUT_PDF_BUMPER}"\\'
)

# -----------------------------------------------------------------------
# VERIFICATION DICTIONARIES
# -----------------------------------------------------------------------
REQUIRED_PATHS = {
    "Repo Root":              REPO_ROOT,
    "Manuscript":             MANUSCRIPT,
    "Front Matter Dir":       FRONT_MATTER_DIR,
    "Foreword (Foster)":      FOREWORD_FOSTER,
    "Assets Dir":             ASSETS_DIR,
    "Cover Dir":              COVER_DIR,
    "Base Cover":             BASE_COVER,
    "Fonts Dir":              FONTS_DIR,
    "Images Dir":             IMAGES_DIR,
    "Tools Dir":              TOOLS_DIR,
    "Preamble TeX":           PREAMBLE_TEX,
    "Anchor MD":              ANCHOR_MD,
    "Progress Log":           PROGRESS_LOG,
}

REQUIRED_PATHS_BUMPER = {
    "Base Cover (Bumper)":    BASE_COVER_BUMPER,
    "Foreword (Bumper)":      FOREWORD_BUMPER,
    "Dedication (Bumper)":    DEDICATION_BUMPER,
    "Preface (Bumper)":       PREFACE_BUMPER,
    "Preamble TeX (Bumper)":  PREAMBLE_TEX_BUMPER,
}

GENERATED_PATHS = {
    "Outputs Dir":            OUTPUTS_DIR,
    "PDF Output":             OUTPUT_PDF,
    "EPUB Output":            OUTPUT_EPUB,
    "DOCX Output":            OUTPUT_DOCX,
    "Final Cover":            FINAL_COVER,
}

GENERATED_PATHS_BUMPER = {
    "Final Cover (Bumper)":   FINAL_COVER_BUMPER,
    "PDF Output (Bumper)":    OUTPUT_PDF_BUMPER,
    "EPUB Output (Bumper)":   OUTPUT_EPUB_BUMPER,
    "DOCX Output (Bumper)":   OUTPUT_DOCX_BUMPER,
}

# -----------------------------------------------------------------------
# VERIFICATION RUNNER
# -----------------------------------------------------------------------
if __name__ == "__main__":

    print(POWERSHELL_CD_NOTE)
    print("\\n=== DoughForge W-Anchor Anchor \\u2014 Path Verification ===")
    print("  -- Standard Edition: Required --\\n")
    required_ok = True
    for label, path in REQUIRED_PATHS.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "MISSING"
        if not exists:
            required_ok = False
        print(f"  [{status}] {label:<26} {path}")

    print("\\n  -- Bumper Edition: Required --\\n")
    bumper_ok = True
    for label, path in REQUIRED_PATHS_BUMPER.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "MISSING"
        if not exists:
            bumper_ok = False
        print(f"  [{status}] {label:<26} {path}")

    print("\\n  -- Generated (missing is normal before first build) --\\n")
    for label, path in {**GENERATED_PATHS, **GENERATED_PATHS_BUMPER}.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "not yet"
        print(f"  [{status}] {label:<26} {path}")

    print()
    if required_ok:
        print("  OK Standard edition paths verified. Safe to build.\\n")
    else:
        print("  STOP: Standard required paths missing. Fix before building.\\n")
