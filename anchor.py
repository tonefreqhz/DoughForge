# Outputs
OUTPUT_PDF   = os.path.join(OUTPUTS_DIR, "your_book.pdf")
OUTPUT_EPUB  = os.path.join(OUTPUTS_DIR, "your_book.epub")
OUTPUT_DOCX  = os.path.join(OUTPUTS_DIR, "your_book.docx")

# Assets
FONTS_DIR    = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR   = os.path.join(ASSETS_DIR, "images")

# Tools
TOOLS_DIR    = os.path.join(REPO_ROOT, "tools")
PREAMBLE_TEX = os.path.join(REPO_ROOT, "preamble.tex")
ANCHOR_MD    = os.path.join(REPO_ROOT, "ANCHOR.md")
PROGRESS_LOG = os.path.join(REPO_ROOT, "INTERIM_PROGRESS_LOG.md")

# Build commands
BUILD_DOCX = f'pandoc "{MANUSCRIPT}" -o "{OUTPUT_DOCX}"'
BUILD_EPUB = f'pandoc "{MANUSCRIPT}" --epub-cover-image="{FINAL_COVER}" -o "{OUTPUT_EPUB}"'
BUILD_PDF  = f'pandoc "{MANUSCRIPT}" --pdf-engine=lualatex --include-in-header="{PREAMBLE_TEX}" -o "{OUTPUT_PDF}"'
