"""
Input : [1, 2, 3]
Output : 123

Input : [55, 32, 890]
Output : 5532890
"""

l = [55, 32, 890]
for i in l:
    print(i, end="")

print()
# other way
ll = [str(i) for i in l]
print("". join(ll))