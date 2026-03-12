"""
build_cover.py
Inputs:
  assets/cover/base_cover.png
  assets/cover/stamp_check_red2.png
  book.yaml

Output flavours -> covers/
  final_cover.jpg        (KDP print, 300dpi equivalent, high quality)
  final_cover_ebook.jpg  (eBook / Kindle, 1600x2560, compressed)
  final_cover_thumb.jpg  (thumbnail / social, 400x640)
"""
import os, yaml
from PIL import Image, ImageDraw, ImageFont
from anchor import REPO_ROOT

COVER_DIR   = os.path.join(REPO_ROOT, "assets", "cover")
OUTPUT_DIR  = os.path.join(REPO_ROOT, "covers")
BASE_COVER  = os.path.join(COVER_DIR, "base_cover.png")
STAMP_FILE  = os.path.join(COVER_DIR, "stamp_check_red2.png")

os.makedirs(COVER_DIR,  exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 60)
print(f"REPO_ROOT  : {REPO_ROOT}")
print(f"BASE_COVER : {BASE_COVER}  exists={os.path.exists(BASE_COVER)}")
print(f"STAMP_FILE : {STAMP_FILE}  exists={os.path.exists(STAMP_FILE)}")
print(f"OUTPUT_DIR : {OUTPUT_DIR}")
print("=" * 60)

BOOK_YAML = os.path.join(REPO_ROOT, "book.yaml")
with open(BOOK_YAML, encoding="utf-8") as f:
    book = yaml.safe_load(f)

TITLE    = book.get("title",    "Untitled")
SUBTITLE = book.get("subtitle", "")
AUTHOR   = book.get("author",   "")

print(f"Title    : {TITLE}")
print(f"Subtitle : {SUBTITLE}")
print(f"Author   : {AUTHOR}")
print()

GREEN_BRIGHT  = (51,  255,  51)
GREEN_MID     = (0,   210,   0)
AMBER_DARK    = (28,  18,    4)
SCANLINE      = (18,  10,    2)
BORDER_GREEN  = (51,  255,  51)

W, H = 1600, 2560

if os.path.exists(BASE_COVER):
    base = Image.open(BASE_COVER).convert("RGBA").resize((W, H), Image.LANCZOS)
    print("Base cover loaded OK")
else:
    base = Image.new("RGBA", (W, H), (10, 10, 10, 255))
    print("WARNING: No base_cover.png — using dark placeholder")

def load_font(size):
    candidates = [
        "CourierNew.ttf", "cour.ttf",
        "LucidaConsole.ttf", "lucon.ttf",
        "DejaVuSansMono.ttf",
        "Georgia.ttf", "georgia.ttf",
        "arial.ttf",
    ]
    roots = [
        r"C:\Windows\Fonts",
        r"C:\Users\peewe\AppData\Local\Microsoft\Windows\Fonts",
        "/usr/share/fonts/truetype/dejavu",
    ]
    for name in candidates:
        for root in roots:
            path = os.path.join(root, name)
            if os.path.exists(path):
                print(f"  Font: {name} @ {size}px")
                return ImageFont.truetype(path, size)
    print(f"  Font: default @ {size}px")
    return ImageFont.load_default()

font_title    = load_font(118)
font_subtitle = load_font(58)
font_author   = load_font(88)
font_prompt   = load_font(36)
print()

_dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))

def measure(text, font):
    bb = _dummy.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]

def centered_text(draw, canvas_w, y, text, font, fill):
    tw, _ = measure(text, font)
    x = (canvas_w - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)

def make_crt_panel(panel_w, panel_h, alpha=175):
    panel = Image.new("RGBA", (panel_w, panel_h), (*AMBER_DARK, alpha))
    d = ImageDraw.Draw(panel)
    for y in range(0, panel_h, 4):
        d.line([(0, y), (panel_w, y)], fill=(*SCANLINE, max(0, alpha - 20)))
    d.rectangle([(0, 0), (panel_w-1, panel_h-1)],
                outline=(*BORDER_GREEN, 220), width=3)
    d.rectangle([(6, 6), (panel_w-7, panel_h-7)],
                outline=(*BORDER_GREEN, 120), width=1)
    return panel

PAD = 40
title_tw, _ = measure(TITLE,    font_title)
sub_tw,   _ = measure(SUBTITLE, font_subtitle)

panel_title_w = max(title_tw, sub_tw) + PAD * 4
panel_title_h = 230
panel_title_x = (W - panel_title_w) // 2
panel_title_y = 200

title_panel = make_crt_panel(panel_title_w, panel_title_h)
td = ImageDraw.Draw(title_panel)
centered_text(td, panel_title_w, 16,  TITLE,    font_title,    fill=(*GREEN_BRIGHT, 255))
centered_text(td, panel_title_w, 152, SUBTITLE, font_subtitle, fill=(*GREEN_MID,    255))

auth_tw, _   = measure(AUTHOR, font_author)
panel_auth_w = auth_tw + PAD * 6
panel_auth_h = 190
panel_auth_x = (W - panel_auth_w) // 2
panel_auth_y = H - panel_auth_h - 120

author_panel = make_crt_panel(panel_auth_w, panel_auth_h)
ad = ImageDraw.Draw(author_panel)
centered_text(ad, panel_auth_w, 10, "READY>",  font_prompt, fill=(51, 200, 51, 180))
centered_text(ad, panel_auth_w, 56, AUTHOR,    font_author, fill=(*GREEN_BRIGHT, 255))

composite = base.copy()
composite.paste(title_panel,  (panel_title_x, panel_title_y),  title_panel)
composite.paste(author_panel, (panel_auth_x,  panel_auth_y),   author_panel)

if os.path.exists(STAMP_FILE):
    stamp_raw = Image.open(STAMP_FILE).convert("RGBA")
    STAMP_W = 1100
    ratio   = STAMP_W / stamp_raw.width
    STAMP_H = int(stamp_raw.height * ratio)
    stamp   = stamp_raw.resize((STAMP_W, STAMP_H), Image.LANCZOS)
    pixels  = stamp.load()
    for sy in range(STAMP_H):
        for sx in range(STAMP_W):
            r, g, b, a = pixels[sx, sy]
            if r > 140 and g < 90 and b < 90:
                pixels[sx, sy] = (r, g, b, 0)
    stamp_x = (W - STAMP_W) // 2
    stamp_y = panel_title_y + panel_title_h + 60
    composite.paste(stamp, (stamp_x, stamp_y), stamp)
    print(f"Stamp placed at ({stamp_x}, {stamp_y})  {STAMP_W}x{STAMP_H}px")
else:
    print(f"WARNING: Stamp not found at {STAMP_FILE}")

flavours = [
    {"name": "final_cover.jpg",       "desc": "KDP Print — full res",          "size": (1600, 2560), "quality": 97},
    {"name": "final_cover_ebook.jpg",  "desc": "eBook / Kindle",                "size": (1600, 2560), "quality": 85},
    {"name": "final_cover_thumb.jpg",  "desc": "Thumbnail / social 400x640",    "size": (400,   640), "quality": 82},
]

print()
print("Saving flavours:")
for fl in flavours:
    out_path = os.path.join(OUTPUT_DIR, fl["name"])
    img = composite.copy()
    if fl["size"] != (W, H):
        img = img.resize(fl["size"], Image.LANCZOS)
    img.convert("RGB").save(out_path, "JPEG", quality=fl["quality"])
    size_kb = os.path.getsize(out_path) // 1024
    print(f"  ✅ {fl['name']:<35} {fl['desc']:<35} {size_kb:>6} KB")

print()
print("All covers written to:", OUTPUT_DIR)
