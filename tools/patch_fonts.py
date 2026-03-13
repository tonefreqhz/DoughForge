import os

path = os.path.join("tools", "composite_cover.py")
src = open(path, encoding="utf-8").read()

src = src.replace(
    'os.path.join(FONTS_DIR, "title_font.ttf")',
    'os.path.join(FONTS_DIR, "VT323-Regular.ttf")',
)
src = src.replace(
    'os.path.join(FONTS_DIR, "body_font.ttf")',
    'os.path.join(FONTS_DIR, "Noto_Sans", "NotoSans-VariableFont_wdth,wght.ttf")',
)

open(path, "w", encoding="utf-8").write(src)
print("Patched.")
