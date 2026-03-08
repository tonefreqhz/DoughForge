from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os, shutil

BASE_DIR   = r'C:\Users\peewe\DoughForge'
ASSET_DIR  = os.path.join(BASE_DIR, 'assets', 'cover')
COVERS_DIR = os.path.join(BASE_DIR, 'covers')
FONT_PATH  = os.path.join(BASE_DIR, 'assets', 'fonts', 'VT323-Regular.ttf')

TITLE    = 'DOUGHFORGE'
SUBTITLE = 'Reproducible Pub Kit'
AUTHOR   = 'Roger S Lewis'

if os.path.exists(COVERS_DIR):
    shutil.rmtree(COVERS_DIR)
    print('Purged: covers/')
os.makedirs(COVERS_DIR, exist_ok=True)
print('Created: covers/')

base      = Image.open(os.path.join(ASSET_DIR, 'base_cover.png')).convert('RGBA')
stamp_raw = Image.open(os.path.join(ASSET_DIR, 'stamp_clean.png')).convert('RGBA')
W, H = base.size
print(f'Canvas: {W}x{H}')

# ── Autocrop transparent padding from stamp ──────────────────────
bbox = stamp_raw.getbbox()
if bbox:
    stamp_raw = stamp_raw.crop(bbox)
    print(f'Stamp cropped to: {stamp_raw.size}')
else:
    print('Stamp: no visible content found — check stamp_clean.png')

txt  = Image.new('RGBA', (W, H), (0,0,0,0))
draw = ImageDraw.Draw(txt)

GREEN     = (0, 255, 70, 255)
GREEN_DIM = (0, 210, 60, 230)
SHADOW    = (0, 50, 10, 200)

f_title    = ImageFont.truetype(FONT_PATH, 120)
f_subtitle = ImageFont.truetype(FONT_PATH, 60)
f_author   = ImageFont.truetype(FONT_PATH, 52)

def centred(draw, text, font, fill, shadow, y):
    bb = draw.textbbox((0,0), text, font=font)
    tw = bb[2] - bb[0]
    x  = (W - tw) // 2
    draw.text((x+3, y+3), text, font=font, fill=shadow)
    draw.text((x,   y  ), text, font=font, fill=fill)
    return bb[3] - bb[1]

y  = int(H * 0.03)
y += centred(draw, TITLE,    f_title,    GREEN,     SHADOW, y) + 16
y += centred(draw, SUBTITLE, f_subtitle, GREEN_DIM, SHADOW, y) + 20

sh = int(H * 0.16)
sw = int(stamp_raw.width * (sh / stamp_raw.height))
stamp_r = stamp_raw.resize((sw, sh), Image.LANCZOS)
sx = (W - sw) // 2
sy = y
print(f'Stamp resized: {stamp_r.size}  pos: ({sx},{sy})')

centred(draw, AUTHOR, f_author, GREEN, SHADOW, int(H * 0.93))

glow_arr = np.array(txt.filter(ImageFilter.GaussianBlur(8)), dtype=float)
glow_arr[:,:,3] *= 0.55
glow = Image.fromarray(glow_arr.astype('uint8'), 'RGBA')

out = base.copy()
out.paste(glow,    (0,0),    glow)
out.paste(txt,     (0,0),    txt)
out.paste(stamp_r, (sx, sy), stamp_r)

outputs = {
    'front_cover.png': lambda p: out.save(p),
    'front_cover.jpg': lambda p: out.convert('RGB').save(p, quality=95),
    'front_cover.gif': lambda p: out.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=256).save(p),
}

for filename, save_fn in outputs.items():
    covers_path = os.path.join(COVERS_DIR, filename)
    save_fn(covers_path)
    print(f'Written: covers/{filename}')
    if filename.endswith('.png'):
        shutil.copy2(covers_path, os.path.join(ASSET_DIR, 'final_cover.png'))
        print('Mirrored: assets/cover/final_cover.png')
    if filename.endswith('.jpg'):
        shutil.copy2(covers_path, os.path.join(ASSET_DIR, 'final_cover.jpg'))
        print('Mirrored: assets/cover/final_cover.jpg')

print()
print('Output manifest:')
for f in sorted(os.listdir(COVERS_DIR)):
    fp = os.path.join(COVERS_DIR, f)
    print(f'  covers/{f}  ({os.path.getsize(fp)//1024} KB)')
