lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if line.startswith('56 commits in three weeks'):
        lines[i] = '156' + line[2:]
        print(f'Restored "156" at line {i+1}')
        break
with open('publication/THE CONQUEST OF DOUGHFORGE.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
