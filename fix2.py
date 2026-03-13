src = open('anchor.py', encoding='utf-8').read()
src = src.replace(
    'MANUSCRIPT        = os.path.join(PUBLICATION_DIR, "your_book.md")',
    'PUBLICATION_DIR   = os.path.join(REPO_ROOT, "publication")\nMANUSCRIPT        = os.path.join(PUBLICATION_DIR, "your_book.md")'
)
open('anchor.py', 'w', encoding='utf-8').write(src)
print('Done')
