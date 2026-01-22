a = "ashishporwal"
b = 'wal'

m = len(a)
n = len(b)

_value = None          
for i in range(m - n + 1):
  if a[i:i+n] == b:
    _value = i
print(_value)