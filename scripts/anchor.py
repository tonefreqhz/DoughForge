import os

# Anchor: repo root is ONE level above this file (scripts/)
REPO_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(REPO_ROOT, "assets")
COVER_DIR  = os.path.join(ASSETS_DIR, "cover")
BASE_COVER = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER = os.path.join(COVER_DIR, "front_cover.jpg")

print(f"Repo Root:        {REPO_ROOT}")
print(f"Base Cover Path:  {BASE_COVER}")
print(f"Final Cover Path: {FINAL_COVER}")
