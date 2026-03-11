import os

# DoughForge W⚓ Protocol — Single Source of Truth for All Paths
# Import anywhere with: from anchor import REPO_ROOT, PUBLICATION_DIR, etc.

# -----------------------------------------------------------------------
# REPO ROOT
# -----------------------------------------------------------------------
REPO_ROOT        = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------
# PUBLICATION
# -----------------------------------------------------------------------
PUBLICATION_DIR  = os.path.join(REPO_ROOT, "publication")
MANUSCRIPT       = os.path.join(PUBLICATION_DIR, "your_book.md")

# -----------------------------------------------------------------------
# OUTPUTS
# -----------------------------------------------------------------------
OUTPUTS_DIR      = os.path.join(REPO_ROOT, "outputs")
OUTPUT_PDF       = os.path.join(OUTPUTS_DIR, "your_book.pdf")
OUTPUT_EPUB      = os.path.join(OUTPUTS_DIR, "your_book.epub")
OUTPUT_DOCX      = os.path.join(OUTPUTS_DIR, "your_book.docx")

# -----------------------------------------------------------------------
# ASSETS
# -----------------------------------------------------------------------
ASSETS_DIR       = os.path.join(REPO_ROOT, "assets")
COVER_DIR        = os.path.join(ASSETS_DIR, "cover")
BASE_COVER       = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER = os.path.join(COVER_DIR, "final_cover.jpg")
FONTS_DIR        = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR       = os.path.join(ASSETS_DIR, "images")

# -----------------------------------------------------------------------
# TOOLS
# -----------------------------------------------------------------------
TOOLS_DIR        = os.path.join(REPO_ROOT, "tools")
PREAMBLE_TEX     = os.path.join(REPO_ROOT, "preamble.tex")
ANCHOR_MD        = os.path.join(REPO_ROOT, "ANCHOR.md")
PROGRESS_LOG     = os.path.join(REPO_ROOT, "INTERIM_PROGRESS_LOG.md")

# -----------------------------------------------------------------------
# BUILD COMMANDS
# -----------------------------------------------------------------------
BUILD_DOCX = f'pandoc "{MANUSCRIPT}" -o "{OUTPUT_DOCX}"'
BUILD_EPUB = f'pandoc "{MANUSCRIPT}" --epub-cover-image="{FINAL_COVER}" -o "{OUTPUT_EPUB}"'
BUILD_PDF  = f'pandoc "{MANUSCRIPT}" --pdf-engine=lualatex --include-in-header="{PREAMBLE_TEX}" -o "{OUTPUT_PDF}"'

# -----------------------------------------------------------------------
# VERIFICATION — two tiers
# Required: must exist before building
# Generated: created by build, missing before first run is normal
# -----------------------------------------------------------------------
REQUIRED_PATHS = {
    "Repo Root":     REPO_ROOT,
    "Manuscript":    MANUSCRIPT,
    "Assets Dir":    ASSETS_DIR,
    "Cover Dir":     COVER_DIR,
    "Base Cover":    BASE_COVER,
    "Fonts Dir":     FONTS_DIR,
    "Images Dir":    IMAGES_DIR,
    "Tools Dir":     TOOLS_DIR,
    "Preamble TeX":  PREAMBLE_TEX,
    "Anchor MD":     ANCHOR_MD,
    "Progress Log":  PROGRESS_LOG,
}

GENERATED_PATHS = {
    "Outputs Dir":   OUTPUTS_DIR,
    "PDF Output":    OUTPUT_PDF,
    "EPUB Output":   OUTPUT_EPUB,
    "DOCX Output":   OUTPUT_DOCX,
    "Final Cover":   FINAL_COVER,
}

if __name__ == "__main__":
    print("\n=== DoughForge W-Anchor Path Verification ===\n")

    print("  -- Required (must exist before building) --\n")
    required_ok = True
    for label, path in REQUIRED_PATHS.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "MISSING"
        if not exists:
            required_ok = False
        print(f"  [{status}] {label:<20} {path}")

    print("\n  -- Generated (created by build, missing is normal) --\n")
    for label, path in GENERATED_PATHS.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "not yet"
        print(f"  [{status}] {label:<20} {path}")

    print()
    if required_ok:
        print("  All required paths verified. Safe to build.\n")
    else:
        print("  STOP: Required paths missing. Fix before building.\n")

    print("=== Canonical Build Commands ===\n")
    print(f"  DOCX:  {BUILD_DOCX}\n")
    print(f"  EPUB:  {BUILD_EPUB}\n")
    print(f"  PDF:   {BUILD_PDF}\n")
