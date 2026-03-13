src = open('anchor.py', encoding='utf-8').read()
for i, line in enumerate(src.splitlines(), 1):
    if 1 <= i <= 60:
        print(f'{i:>4}  {line}')
