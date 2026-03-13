# DoughForge

A publishing pipeline for independent authors, built on the W-Anchor Protocol.

## What This Is

DoughForge is a book project and a toolkit. It contains:

- **The manuscript** — *The Conquest of DoughForge*
- **The pipeline** — Pandoc builds producing EPUB, PDF, and DOCX from one Markdown source
- **The anchor** — `anchor.py`, a path verifier that keeps every session grounded

---

## 🔒 Session Anchor — Start Here Every Time

Before every session (human or AI), run:

```powershell
cd "C:\Users\peewe\Documents\DoughForge"
.\anchor_verify.ps1
