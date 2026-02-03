a = "ashishporwal"
b = 'wal'

for i in a:
    if i==b[0]:
        idx = a.index(i)
        len_b = len(b)
        if a[idx: idx+len_b] == b:
            print(idx)
