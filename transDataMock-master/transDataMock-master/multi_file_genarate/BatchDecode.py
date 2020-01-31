from os import listdir
from chardet import detect

fns = (fn for fn in listdir() if fn.endswith('.csv'))

for fn in fns:
    with open(fn, 'rb+') as fp:
        content = fp.read()
        encoding = detect(content)['encoding']
        content = content.decode(encoding).encode('utf8')
        fp.seek(0)
        fp.write(content)