import os

REPO_ROOT         = os.path.dirname(os.path.abspath(__file__))
PUBLICATION_DIR   = os.path.join(REPO_ROOT, "publication")
MANUSCRIPT        = os.path.join(PUBLICATION_DIR, "your_book.md")
MANUSCRIPT_BUMPER = os.path.join(PUBLICATION_DIR, "THE CONQUEST OF DOUGHFORGE.md")
FRONT_MATTER_DIR      = os.path.join(PUBLICATION_DIR, "front_matter")
FOREWORD_FOSTER       = os.path.join(FRONT_MATTER_DIR, "foreword_foster_lewis.md")
FOREWORD_BUMPER       = os.path.join(FRONT_MATTER_DIR, "foreword_bumper.md")
DEDICATION_BUMPER     = os.path.join(FRONT_MATTER_DIR, "dedication_bumper.md")
PREFACE_BUMPER        = os.path.join(FRONT_MATTER_DIR, "preface_bumper.md")
OUTPUTS_DIR        = os.path.join(REPO_ROOT, "outputs")
OUTPUT_PDF         = os.path.join(OUTPUTS_DIR, "your_book.pdf")
OUTPUT_EPUB        = os.path.join(OUTPUTS_DIR, "your_book.epub")
OUTPUT_DOCX        = os.path.join(OUTPUTS_DIR, "your_book.docx")
OUTPUT_PDF_BUMPER  = os.path.join(OUTPUTS_DIR, "conquest_of_doughforge_bumper.pdf")
OUTPUT_EPUB_BUMPER = os.path.join(OUTPUTS_DIR, "conquest_of_doughforge_bumper.epub")
OUTPUT_DOCX_BUMPER = os.path.join(OUTPUTS_DIR, "conquest_of_doughforge_bumper.docx")
ASSETS_DIR         = os.path.join(REPO_ROOT, "assets")
COVER_DIR          = os.path.join(ASSETS_DIR, "cover")
FONTS_DIR          = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR         = os.path.join(ASSETS_DIR, "images")
BASE_COVER         = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER        = os.path.join(COVER_DIR, "front_cover.jpg")
BASE_COVER_BUMPER  = os.path.join(COVER_DIR, "base_cover_bumper.png")
FINAL_COVER_BUMPER = os.path.join(COVER_DIR, "front_cover_bumper.jpg")
TOOLS_DIR           = os.path.join(REPO_ROOT, "tools")
PREAMBLE_TEX        = os.path.join(REPO_ROOT, "preamble.tex")
PREAMBLE_TEX_BUMPER = os.path.join(REPO_ROOT, "preamble_bumper.tex")
ANCHOR_MD           = os.path.join(REPO_ROOT, "ANCHOR.md")
PROGRESS_LOG        = os.path.join(REPO_ROOT, "INTERIM_PROGRESS_LOG.md")
BOOK_TITLE_STANDARD  = "DoughForge: The Reproducible Self-Publishing Desktop Kit"
BOOK_TITLE_BUMPER    = "The Conquest of DoughForge"
BOOK_SUBTITLE_BUMPER = "The Truth Will Set You Free - But First It Will Piss You Off"
BOOK_AUTHOR          = "Roger G Lewis"
FOREWORD_AUTHOR      = "Foster Lewis"
EDITION_BUMPER       = "Bumper Edition"
EDITION_PRICE        = ""
REQUIRED_PATHS = {
    "Repo Root":            REPO_ROOT,
    "Manuscript":           MANUSCRIPT,
    "Front Matter Dir":     FRONT_MATTER_DIR,
    "Foreword Foster":      FOREWORD_FOSTER,
    "Assets Dir":           ASSETS_DIR,
    "Cover Dir":            COVER_DIR,
    "Base Cover":           BASE_COVER,
    "Fonts Dir":            FONTS_DIR,
    "Images Dir":           IMAGES_DIR,
    "Tools Dir":            TOOLS_DIR,
    "Preamble TeX":         PREAMBLE_TEX,
    "Anchor MD":            ANCHOR_MD,
    "Progress Log":         PROGRESS_LOG,
}
REQUIRED_PATHS_BUMPER = {
    "Base Cover Bumper":    BASE_COVER_BUMPER,
    "Foreword Bumper":      FOREWORD_BUMPER,
    "Dedication Bumper":    DEDICATION_BUMPER,
    "Preface Bumper":       PREFACE_BUMPER,
    "Preamble TeX Bumper":  PREAMBLE_TEX_BUMPER,
}
GENERATED_PATHS = {
    "Outputs Dir":  OUTPUTS_DIR,
    "PDF Output":   OUTPUT_PDF,
    "EPUB Output":  OUTPUT_EPUB,
    "DOCX Output":  OUTPUT_DOCX,
    "Final Cover":  FINAL_COVER,
}
GENERATED_PATHS_BUMPER = {
    "Final Cover Bumper":   FINAL_COVER_BUMPER,
    "PDF Output Bumper":    OUTPUT_PDF_BUMPER,
    "EPUB Output Bumper":   OUTPUT_EPUB_BUMPER,
    "DOCX Output Bumper":   OUTPUT_DOCX_BUMPER,
}
if __name__ == "__main__":
    required_ok = True
    bumper_ok = True
    print("\n=== DoughForge W-Anchor - Path Verification ===")
    print("  -- Standard Edition: Required --\n")
    for label, path in REQUIRED_PATHS.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "MISSING"
        if not exists: required_ok = False
        print(f"  [{status}] {label:<26} {path}")
    print("\n  -- Bumper Edition: Required --\n")
    for label, path in REQUIRED_PATHS_BUMPER.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "MISSING"
        if not exists: bumper_ok = False
        print(f"  [{status}] {label:<26} {path}")
    print("\n  -- Generated (missing is normal before first build) --\n")
    for label, path in {**GENERATED_PATHS, **GENERATED_PATHS_BUMPER}.items():
        exists = os.path.exists(path)
        status = "OK     " if exists else "not yet"
        print(f"  [{status}] {label:<26} {path}")
    print()
    print("  OK Standard paths verified.\n" if required_ok else "  STOP: Standard paths missing.\n")
    print("  OK Bumper paths verified.\n" if bumper_ok else "  Bumper paths incomplete.\n")