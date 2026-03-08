# Quick Start Guide

This guide gets you from zero to a built cover and packaged EPUB in minutes.

## Prerequisites

- Python 3.12+
- Pandoc 3.x
- Pillow (`pip install pillow`)
- PyYAML (`pip install pyyaml`)

## 1. Clone the repo

Clone from GitHub and enter the project directory.

## 2. Configure your book

Edit `book.yaml` with your title, author, and chapter list.

## 3. Build the cover

Run the cover compositor:

    python scripts/build_cover.py

Output: `assets/cover/final_cover.jpg`

## 4. Build the EPUB

    python scripts/build_epub.py

Output: `dist/doughforge.epub`

## 5. Proofread

Open `dist/doughforge.epub` in Calibre or upload directly to
Draft2Digital for preview.
