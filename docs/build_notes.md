# DoughForge — Cover Build Notes

## What We Built

A Python cover compositor that:
- Loads a base AI-generated cover image (assets/cover/base_cover.png)
- Overlays VT323 monospace title, subtitle, and author text with green glow
- Composites an approval stamp (assets/cover/stamp_clean.png) centred below subtitle
- Purges and rebuilds the covers/ folder on every run
- Outputs front_cover.png, front_cover.jpg, front_cover.gif
- Mirrors final_cover.png and final_cover.jpg back to assets/cover/

## Canvas Spec

| Property     | Value                                       |
|--------------|---------------------------------------------|
| Dimensions   | 1024 x 1792 px                              |
| Colour space | RGBA during compositing, RGB for final JPG  |
| Print target | Draft2Digital (JPG, 96 DPI minimum)         |
| Font         | VT323-Regular.ttf @ 120pt / 60pt / 52pt     |

## File Locations

| File                           | Purpose                            |
|--------------------------------|------------------------------------|
| assets/cover/base_cover.png    | AI-generated background            |
| assets/cover/stamp_clean.png   | Transparent PNG approval stamp     |
| assets/fonts/VT323-Regular.ttf | Display font                       |
| scripts/build_cover.py         | Cover compositor script            |
| covers/front_cover.png         | Final PNG for web / GitHub         |
| covers/front_cover.jpg         | Final JPG for Draft2Digital upload |
| covers/front_cover.gif         | Final GIF for social / preview     |

## How to Run

    cd C:\Users\peewe\DoughForge
    python scripts\build_cover.py

## Key Design Decisions

- Purge before write: shutil.rmtree(covers/) prevents stale files reaching publisher
- Sized by height: stamp resized as 16% of H regardless of source PNG aspect ratio
- Percentage-based layout: all Y positions are fractions of H, resolution-independent
- Glow layer: Gaussian blur at 50% opacity gives terminal/CRT aesthetic

## Dependencies

    pip install Pillow numpy

## Adapting for Other Projects

Change only the config block at the top of build_cover.py:

    BASE_DIR = r'C:\Users\peewe\YourProject'
    TITLE    = 'Your Title'
    SUBTITLE = 'Your Subtitle'
    AUTHOR   = 'Your Name'

Eventually this config block will be replaced by a book.yaml reader.
