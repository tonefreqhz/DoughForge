src = open('anchor.py', encoding='utf-8').read()
src = src.replace(
    'f\'pandoc "{}" \'',
    'f\'pandoc "{MANUSCRIPT}" \''
)
open('anchor.py', 'w', encoding='utf-8').write(src)
print('Done')
