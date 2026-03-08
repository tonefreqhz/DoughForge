"""
composite_cover.py
DoughForge — composites the approved_stamp.png over the top quarter
of base_cover.png and saves the result to covers\front_cover.png

Canvas : 1024 x 1792 px
Top quarter : y = 0 .. 447 px
Stamp target: centred horizontally, vertically centred in top quarter
              scaled so stamp width = 40% of canvas width (~410px)
"""

import os
from PIL import Image

# ── Paths (relative to repo root) ────────────────────────────────
ROOT        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_COVER  = os.path.join(ROOT, "assets", "cover", "base_cover.png")
STAMP_PATH  = os.path.join(ROOT, "assets", "cover", "approved_stamp.png")
OUTPUT_DIR  = os.path.join(ROOT, "covers")
FINAL_COVER = os.path.join(OUTPUT_DIR, "front_cover.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Load base (convert to RGBA for clean alpha composite) ─────────
base = Image.open(BASE_COVER).convert("RGBA")
canvas_w, canvas_h = base.size          # 1024, 1792
top_quarter_h = canvas_h // 4           # 448

# ── Load stamp (already has transparency) ─────────────────────────
stamp = Image.open(STAMP_PATH).convert("RGBA")

# ── Scale stamp: 40% of canvas width, preserve aspect ratio ───────
target_w = int(canvas_w * 0.40)         # ~410 px
ratio     = target_w / stamp.width
target_h  = int(stamp.height * ratio)
stamp     = stamp.resize((target_w, target_h), Image.LANCZOS)

# ── Position: centred horizontally, centred in top quarter ────────
x = (canvas_w - target_w) // 2
y = (top_quarter_h - target_h) // 2

# Clamp so stamp never bleeds above y=0
y = max(0, y)

# ── Composite and save ────────────────────────────────────────────
base.paste(stamp, (x, y), stamp)        # third arg = alpha mask

final_rgb = base.convert("RGB")         # EPUB/PDF prefer RGB JPEG-friendly
final_rgb.save(FINAL_COVER, "PNG")

print(f"Canvas  : {canvas_w} x {canvas_h}")
print(f"Stamp   : {target_w} x {target_h}  at ({x}, {y})")
print(f"Saved   : {FINAL_COVER}")
