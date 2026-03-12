"""
build_toc.py
Reads book.yaml -> writes src/nav.xhtml and src/toc.ncx
"""
import os, yaml
from anchor import REPO_ROOT

BOOK_YAML = os.path.join(REPO_ROOT, "book.yaml")
SRC_DIR   = os.path.join(REPO_ROOT, "src")
os.makedirs(SRC_DIR, exist_ok=True)

with open(BOOK_YAML, encoding="utf-8") as f:
    book = yaml.safe_load(f)

chapters = book.get("chapters", [])
title    = book.get("title", "Book")

nav_items = "\n".join(
    f'      <li><a href="../{ch["file"]}">{ch["title"]}</a></li>'
    for ch in chapters
)
nav_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Table of Contents</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Table of Contents</h1>
    <ol>
{nav_items}
    </ol>
  </nav>
</body>
</html>"""

nav_path = os.path.join(SRC_DIR, "nav.xhtml")
with open(nav_path, "w", encoding="utf-8") as f:
    f.write(nav_xhtml)
print(f"Written: {nav_path}")

nav_points = "\n".join(
    f"""  <navPoint id="{ch['id']}" playOrder="{i+1}">
    <navLabel><text>{ch['title']}</text></navLabel>
    <content src="../{ch['file']}"/>
  </navPoint>"""
    for i, ch in enumerate(chapters)
)
toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{title}"/></head>
<docTitle><text>{title}</text></docTitle>
<navMap>
{nav_points}
</navMap>
</ncx>"""

ncx_path = os.path.join(SRC_DIR, "toc.ncx")
with open(ncx_path, "w", encoding="utf-8") as f:
    f.write(toc_ncx)
print(f"Written: {ncx_path}")
