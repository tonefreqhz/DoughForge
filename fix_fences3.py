lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()

# Find the ``` immediately followed by --- (with optional blank line between)
# Replace the ``` with nothing, keep the ---
for i in range(len(lines) - 3):
    if lines[i].strip() == '```' and lines[i+1].strip() == '---':
        # Check this is the stray one (not the code block closers we already fixed)
        # Confirm line before is prose, not code
        if i > 0 and lines[i-1].strip() not in ('', '```'):
            continue
        lines[i] = '\n'  # remove the stray opening fence
        print(f'Removed stray fence at line {i+1}')
        break

with open('publication/THE CONQUEST OF DOUGHFORGE.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Verifying lines 400-415:')
lines2 = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
for i, line in enumerate(lines2, 1):
    if 400 <= i <= 415:
        print(f'{i:4d}: {line}', end='')
