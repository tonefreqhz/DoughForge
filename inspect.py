src = open('anchor.py', encoding='utf-8').read()
for i, line in enumerate(src.splitlines(), 1):
    if i == 102:
        print(repr(line))
