lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()

# Remove fence at line 377 (index 376)
if lines[376].strip() == '```':
    lines[376] = '\n'
    print('Removed fence at line 377')

# Remove fence at line 403 (index 402)
if lines[402].strip() == '```':
    lines[402] = '\n'
    print('Removed fence at line 403')

with open('publication/THE CONQUEST OF DOUGHFORGE.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Verifying lines 374-412:')
lines2 = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
for i, line in enumerate(lines2, 1):
    if 374 <= i <= 412:
        print(f'{i:4d}: {line}', end='')
