"""
build_epub.py
Reads book.yaml -> runs build_toc.py -> calls Pandoc -> outputs dist/doughforge.epub
"""
import os, sys, yaml, subprocess
from anchor import REPO_ROOT

BOOK_YAML = os.path.join(REPO_ROOT, "book.yaml")
DIST_DIR  = os.path.join(REPO_ROOT, "dist")
os.makedirs(DIST_DIR, exist_ok=True)

with open(BOOK_YAML, encoding="utf-8") as f:
    book = yaml.safe_load(f)

subprocess.run(
    [sys.executable, os.path.join(REPO_ROOT, "scripts", "build_toc.py")],
    check=True
)

chapter_files = [
    os.path.join(REPO_ROOT, ch["file"])
    for ch in book.get("chapters", [])
]

cover    = os.path.join(REPO_ROOT, book.get("cover_image", ""))
out_epub = os.path.join(DIST_DIR, "doughforge.epub")

cmd = [
    "pandoc",
    "--from", "markdown",
    "--to", "epub3",
    "--output", out_epub,
    f"--metadata=title:{book['title']}",
    f"--metadata=author:{book['author']}",
    f"--metadata=lang:{book.get('language','en')}",
    f"--metadata=publisher:{book.get('publisher','')}",
    f"--metadata=rights:{book.get('rights','')}",
    f"--epub-cover-image={cover}",
    "--toc",
    "--toc-depth=2",
    "--epub-chapter-level=1",
] + chapter_files

print("Running Pandoc...")
subprocess.run(cmd, check=True)
print(f"\nEPUB written to: {out_epub}")
