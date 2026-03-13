import re

path = 'publication/THE CONQUEST OF DOUGHFORGE.md'
lines = open(path, encoding='utf-8').readlines()

in_fence = False
fixed = []
changes = 0

for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        in_fence = not in_fence
    
    if not in_fence and not stripped.startswith('#'):
        # Escape bare # not already escaped
        new_line = re.sub(r'(?<!\\)#', r'\\#', line)
        if new_line != line:
            print(f'  Line {i:4d}: {line.rstrip()}')
            print(f'       --> {new_line.rstrip()}')
            changes += 1
            line = new_line
    
    fixed.append(line)

open(path, 'w', encoding='utf-8').writelines(fixed)
print(f'\nDone. {changes} lines fixed.')
