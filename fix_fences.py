lines = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()

# Fix 1: insert closing fence after line 371 (index 371, i.e. after "# Result: 3 fix commits")
# After insert, indices shift by 1
lines.insert(371, '```\n')

# Fix 2: line 847 is now at index 848 (shifted +1). Replace the mangled \\n line
# with a closing fence + blank line + the original prose
for i, line in enumerate(lines):
    if line.startswith('\\\\n'):
        lines[i] = '```\n\n' + line[4:]  # strip the \\n prefix, prepend fence
        print(f'Fixed mangled line at index {i}')
        break

with open('publication/THE CONQUEST OF DOUGHFORGE.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Patch complete. Verifying...')
lines2 = open('publication/THE CONQUEST OF DOUGHFORGE.md', encoding='utf-8').readlines()
print('=== Lines 364-380 ===')
for i, line in enumerate(lines2, 1):
    if 364 <= i <= 380:
        print(f'{i:4d}: {line}', end='')
print()
print('=== Lines 844-855 ===')
for i, line in enumerate(lines2, 1):
    if 844 <= i <= 857:
        print(f'{i:4d}: {line}', end='')
