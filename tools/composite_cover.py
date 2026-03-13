# tools/composite_cover.py
# DoughForge W⚓ — Cover Compositor
#
# Reads base images and metadata from anchor.py.
# Writes composited covers to the paths anchor.py defines.
#
# Run from repo root:
#   cd "C:\Users\peewe\Documents\DoughForge"
#   python tools\composite_cover.py
#
# -----------------------------------------------------------------------
# POWERSHELL RULE
# -----------------------------------------------------------------------
# Always start every PS session with:
#   cd "C:\Users\peewe\Documents\DoughForge"
# -----------------------------------------------------------------------

import os
import sys

# -----------------------------------------------------------------------
# ANCHOR IMPORT — everything comes from here, nothing invented here
# -----------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from anchor import (
    COVER_DIR,
    FONTS_DIR,
    BASE_COVER,
    BASE_COVER_BUMPER,
    FINAL_COVER,
    FINAL_COVER_BUMPER,
    BOOK_TITLE_STANDARD,
    BOOK_TITLE_BUMPER,
    BOOK_SUBTITLE_BUMPER,
    BOOK_AUTHOR,
    EDITION_BUMPER,
    EDITION_PRICE,
    POWERSHELL_CD_NOTE,
)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("\n  STOP: Pillow not installed.")
    print("  Run: pip install Pillow\n")
    sys.exit(1)


# -----------------------------------------------------------------------
# FONT PATHS — drop .ttf files into assets\fonts\ and update these
# -----------------------------------------------------------------------
FONT_TITLE_PATH    = os.path.join(FONTS_DIR, "VT323-Regular.ttf")
FONT_SUBTITLE_PATH = os.path.join(FONTS_DIR, "Noto_Sans", "NotoSans-VariableFont_wdth,wght.ttf")
FONT_AUTHOR_PATH   = os.path.join(FONTS_DIR, "Noto_Sans", "NotoSans-VariableFont_wdth,wght.ttf")

FONT_TITLE_SIZE    = 120
FONT_SUBTITLE_SIZE = 52
FONT_AUTHOR_SIZE   = 64
FONT_EDITION_SIZE  = 44

TEXT_COLOUR_GOLD   = (212, 175, 55, 255)
TEXT_COLOUR_CREAM  = (255, 253, 240, 255)
TEXT_COLOUR_WHITE  = (255, 255, 255, 255)


# -----------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------
def load_font(path, size):
    """Load a TTF font, fall back to PIL default if file missing."""
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    print(f"  WARNING  Font not found: {path}")
    print("           Falling back to PIL default — replace with real font.")
    return ImageFont.load_default()


def check_base(path, label):
    """Confirm the base image exists before attempting to open it."""
    if not os.path.exists(path):
        print(f"\n  STOP: {label} not found at:\n  {path}")
        print("  Drop the base image into assets\\cover\\ and re-run.\n")
        return False
    return True


def ensure_outputs_dir():
    """assets\cover\ must exist for the compositor to write into."""
    os.makedirs(COVER_DIR, exist_ok=True)


# -----------------------------------------------------------------------
# COMPOSITOR
# -----------------------------------------------------------------------
def composite(
    base_path,
    output_path,
    title,
    author,
    subtitle=None,
    edition=None,
    price=None,
    label="",
):
    print(f"\n  -- {label} --")
    print(f"  Base:   {base_path}")
    print(f"  Output: {output_path}")

    img  = Image.open(base_path).convert("RGBA")
    W, H = img.size
    draw = ImageDraw.Draw(img)

    font_title    = load_font(FONT_TITLE_PATH,    FONT_TITLE_SIZE)
    font_subtitle = load_font(FONT_SUBTITLE_PATH, FONT_SUBTITLE_SIZE)
    font_author   = load_font(FONT_AUTHOR_PATH,   FONT_AUTHOR_SIZE)
    font_edition  = load_font(FONT_SUBTITLE_PATH, FONT_EDITION_SIZE)

    # ---- TITLE — upper third, centred ----
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_w    = title_bbox[2] - title_bbox[0]
    title_x    = (W - title_w) // 2
    title_y    = int(H * 0.08)
    draw.text((title_x, title_y), title, font=font_title, fill=TEXT_COLOUR_GOLD)

    # ---- SUBTITLE — below title ----
    if subtitle:
        sub_bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
        sub_w    = sub_bbox[2] - sub_bbox[0]
        sub_x    = (W - sub_w) // 2
        sub_y    = title_y + (title_bbox[3] - title_bbox[1]) + 24
        draw.text((sub_x, sub_y), subtitle, font=font_subtitle, fill=TEXT_COLOUR_CREAM)

    # ---- AUTHOR — lower fifth, centred ----
    auth_bbox = draw.textbbox((0, 0), author, font=font_author)
    auth_w    = auth_bbox[2] - auth_bbox[0]
    auth_x    = (W - auth_w) // 2
    auth_y    = int(H * 0.82)
    draw.text((auth_x, auth_y), author, font=font_author, fill=TEXT_COLOUR_WHITE)

    # ---- EDITION + PRICE — bottom strip ----
    if edition and price:
        tag      = f"{edition}  ·  {price}"
        tag_bbox = draw.textbbox((0, 0), tag, font=font_edition)
        tag_w    = tag_bbox[2] - tag_bbox[0]
        tag_x    = (W - tag_w) // 2
        tag_y    = int(H * 0.90)
        draw.text((tag_x, tag_y), tag, font=font_edition, fill=TEXT_COLOUR_GOLD)

    # ---- WRITE OUTPUT ----
    img.convert("RGB").save(output_path, "JPEG", quality=95)
    print(f"  WRITTEN {output_path}")


# -----------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=== DoughForge W⚓ Cover Compositor ===")
    print(POWERSHELL_CD_NOTE)

    ensure_outputs_dir()

    # Standard Edition
    if check_base(BASE_COVER, "Base Cover (Standard)"):
        composite(
            base_path   = BASE_COVER,
            output_path = FINAL_COVER,
            title       = BOOK_TITLE_STANDARD,
            author      = BOOK_AUTHOR,
            label       = "Standard Edition",
        )

    # Bumper Edition
    if check_base(BASE_COVER_BUMPER, "Base Cover (Bumper)"):
        composite(
            base_path   = BASE_COVER_BUMPER,
            output_path = FINAL_COVER_BUMPER,
            title       = BOOK_TITLE_BUMPER,
            author      = BOOK_AUTHOR,
            subtitle    = BOOK_SUBTITLE_BUMPER,
            edition     = EDITION_BUMPER,
            price       = EDITION_PRICE,
            label       = "Bumper Edition",
        )

    print("\n=== Compositor Done ===\n")
