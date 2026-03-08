import os

# Anchor: Define repo root and key paths
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLICATION_DIR = os.path.join(REPO_ROOT, "publication")
MANUSCRIPT = os.path.join(PUBLICATION_DIR, "your_book.md")
OUTPUTS_DIR = os.path.join(REPO_ROOT, "outputs")
ASSETS_DIR = os.path.join(REPO_ROOT, "assets")
COVER_DIR = os.path.join(ASSETS_DIR, "cover")
BASE_COVER = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER = os.path.join(COVER_DIR, "front_cover.jpg")
FONTS_NOTO = os.path.join(REPO_ROOT, "Noto_Sans")
FONTS_SORA = os.path.join(REPO_ROOT, "Sora")

# Verify on import
if __name__ == "__main__":
    paths = {
        "Repo Root": REPO_ROOT,
        "Manuscript": MANUSCRIPT,
        "Outputs": OUTPUTS_DIR,
        "Base Cover": BASE_COVER,
        "Final Cover": FINAL_COVER,
    }
    for name, path in paths.items():
        status = "OK" if os.path.exists(path) else "MISSING"
        print(f"[{status}] {name}: {path}")
