"""
Input: a = 2, b = 4
Output: 4
"""
a = 2
b = 4

if a > b:
    print(a)
else:
    print(b)

# better way
print(a if a>b else b)