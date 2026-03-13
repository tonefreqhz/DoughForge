lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()

# Fix 1: line 402 (index 401) — split "<command> ```" into two lines
for i, line in enumerate(lines):
    if line.strip() == '<command> ```':
        lines[i] = '<command>\n'
        lines.insert(i + 1, '```\n')
        print(f'Fixed <command>+fence at line {i+1}')
        break

# Fix 2: find the stray ``` / --- / ``` triplet around old line 407-408
# After above insert, indices shift +1. Look for pattern: fence, ---, fence
for i in range(len(lines) - 2):
    if (lines[i].strip() == '```' and
        lines[i+1].strip() == '---' and
        lines[i+2].strip() == '```'):
        lines[i]   = '\n'   # remove opening stray fence
        lines[i+2] = '\n'   # remove closing stray fence
        print(f'Removed stray fence pair at lines {i+1} and {i+3}')
        break

with open('publication/THE CONQUEST OF DOUGHFORGE.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Patch complete. Verifying...')
lines2 = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
for i, line in enumerate(lines2, 1):
    if 376 <= i <= 420:
        print(f'{i:4d}: {line}', end='')
