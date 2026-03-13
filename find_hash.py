lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
in_fence = False
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        in_fence = not in_fence
    if '#' in line and not in_fence:
        if not stripped.startswith('#'):
            print(f'{i:4d}: {line}', end='')
