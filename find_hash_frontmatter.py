import re

files = [
    'publication/front_matter/dedication_bumper.md',
    'publication/front_matter/foreword_bumper.md',
    'publication/front_matter/preface_bumper.md',
]

for path in files:
    lines = open(path, encoding='utf-8').readlines()
    in_fence = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
        if '#' in line and not in_fence:
            if not stripped.startswith('#'):
                print(f'  [{path}] line {i:4d}: {line.rstrip()}')
