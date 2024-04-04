"""
Input: [2, 3, 5, 6, 7]
Output: []
"""
n_ist = [2, 3, 5, 6, 7]

# clear()
# n_ist.clear()
# print(n_ist)

n_ist*=0
print(n_ist)

n_ist = [2, 3, 5, 6, 7]
del n_ist[:]
print(n_ist)