\# anchor.py

\# DoughForge W⚓ Protocol — Single Source of Truth for All Paths

\# Import anywhere with: from anchor import REPO\_ROOT, PUBLICATION\_DIR, etc.

\# -----------------------------------------------------------------------



import os



\# -----------------------------------------------------------------------

\# REPO ROOT — everything derives from here

\# -----------------------------------------------------------------------



REPO\_ROOT = os.path.dirname(os.path.abspath(\_\_file\_\_))



\# -----------------------------------------------------------------------

\# PUBLICATION — canonical manuscript lives here (edit these, never outputs)

\# -----------------------------------------------------------------------



PUBLICATION\_DIR   = os.path.join(REPO\_ROOT, "publication")

MANUSCRIPT        = os.path.join(PUBLICATION\_DIR, "your\_book.md")



\# -----------------------------------------------------------------------

\# OUTPUTS — generated artefacts (never edit directly, always rebuild)

\# -----------------------------------------------------------------------



OUTPUTS\_DIR       = os.path.join(REPO\_ROOT, "outputs")

OUTPUT\_PDF        = os.path.join(OUTPUTS\_DIR, "your\_book.pdf")

OUTPUT\_EPUB       = os.path.join(OUTPUTS\_DIR, "your\_book.epub")

OUTPUT\_DOCX       = os.path.join(OUTPUTS\_DIR, "your\_book.docx")



\# -----------------------------------------------------------------------

\# ASSETS — covers, images, fonts

\# -----------------------------------------------------------------------



ASSETS\_DIR        = os.path.join(REPO\_ROOT, "assets")

COVER\_DIR         = os.path.join(ASSETS\_DIR, "cover")

BASE\_COVER        = os.path.join(COVER\_DIR, "base\_cover.png")

FINAL\_COVER       = os.path.join(COVER\_DIR, "front\_cover.jpg")

FONTS\_DIR         = os.path.join(ASSETS\_DIR, "fonts")

IMAGES\_DIR        = os.path.join(ASSETS\_DIR, "images")



\# -----------------------------------------------------------------------

\# TOOLS — build support files

\# -----------------------------------------------------------------------



TOOLS\_DIR         = os.path.join(REPO\_ROOT, "tools")

PREAMBLE\_TEX      = os.path.join(REPO\_ROOT, "preamble.tex")

ANCHOR\_MD         = os.path.join(REPO\_ROOT, "ANCHOR.md")

PROGRESS\_LOG      = os.path.join(REPO\_ROOT, "INTERIM\_PROGRESS\_LOG.md")



\# -----------------------------------------------------------------------

\# BUILD COMMANDS — canonical Pandoc commands for this project

\# (use subprocess.run(BUILD\_PDF, shell=True) to invoke from Python)

\# -----------------------------------------------------------------------



BUILD\_DOCX = (

&nbsp;   f'pandoc "{MANUSCRIPT}" '

&nbsp;   f'-o "{OUTPUT\_DOCX}"'

)



BUILD\_EPUB = (

&nbsp;   f'pandoc "{MANUSCRIPT}" '

&nbsp;   f'--epub-cover-image="{FINAL\_COVER}" '

&nbsp;   f'-o "{OUTPUT\_EPUB}"'

)



BUILD\_PDF = (

&nbsp;   f'pandoc "{MANUSCRIPT}" '

&nbsp;   f'--pdf-engine=lualatex '

&nbsp;   f'--include-in-header="{PREAMBLE\_TEX}" '

&nbsp;   f'-o "{OUTPUT\_PDF}"'

)



\# -----------------------------------------------------------------------

\# VERIFICATION — run this file directly to confirm all paths resolve

\# python anchor.py

\# -----------------------------------------------------------------------



PATHS\_TO\_CHECK = {

&nbsp;   "Repo Root":        REPO\_ROOT,

&nbsp;   "Manuscript":       MANUSCRIPT,

&nbsp;   "Outputs Dir":      OUTPUTS\_DIR,

&nbsp;   "PDF Output":       OUTPUT\_PDF,

&nbsp;   "EPUB Output":      OUTPUT\_EPUB,

&nbsp;   "DOCX Output":      OUTPUT\_DOCX,

&nbsp;   "Assets Dir":       ASSETS\_DIR,

&nbsp;   "Cover Dir":        COVER\_DIR,

&nbsp;   "Base Cover":       BASE\_COVER,

&nbsp;   "Final Cover":      FINAL\_COVER,

&nbsp;   "Fonts Dir":        FONTS\_DIR,

&nbsp;   "Images Dir":       IMAGES\_DIR,

&nbsp;   "Tools Dir":        TOOLS\_DIR,

&nbsp;   "Preamble TeX":     PREAMBLE\_TEX,

&nbsp;   "Anchor MD":        ANCHOR\_MD,

&nbsp;   "Progress Log":     PROGRESS\_LOG,

}



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   print("\\n=== DoughForge W⚓ Anchor — Path Verification ===\\n")

&nbsp;   all\_ok = True

&nbsp;   for label, path in PATHS\_TO\_CHECK.items():

&nbsp;       exists = os.path.exists(path)

&nbsp;       status = "✓" if exists else "✗ MISSING"

&nbsp;       if not exists:

&nbsp;           all\_ok = False

&nbsp;       print(f"  {status:<12} {label:<20} {path}")

&nbsp;   print()

&nbsp;   if all\_ok:

&nbsp;       print("  All paths verified. Build environment is clean.\\n")

&nbsp;   else:

&nbsp;       print("  WARNING: Some paths are missing. Create them before building.\\n")



&nbsp;   print("=== Canonical Build Commands ===\\n")

&nbsp;   print(f"  DOCX:  {BUILD\_DOCX}\\n")

&nbsp;   print(f"  EPUB:  {BUILD\_EPUB}\\n")

&nbsp;   print(f"  PDF:   {BUILD\_PDF}\\n")




---

## Git Status
Initialised: yes
First commit: "Initial commit: DoughForge project structure and first clean build"
Branch: master

## Confirmed Working Builds
DOCX: pandoc publication\your_book.md -o outputs\your_book.docx
EPUB: pandoc publication\your_book.md -o outputs\your_book.epub
PDF:  pandoc publication\your_book.md --pdf-engine=lualatex --include-in-header=preamble.tex -o outputs\your_book.pdf
