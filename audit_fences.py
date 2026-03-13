lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
depth = 0
for i, line in enumerate(lines, 1):
    if line.strip() == '```':
        depth += 1 if depth == 0 else -1
        state = 'OPEN' if depth == 1 else 'CLOSE'
        print(f'{i:4d}: {state}  depth={depth}')
print(f'Final depth: {depth} (0 = balanced)')
