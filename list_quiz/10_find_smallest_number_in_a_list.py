"""
Input : list1 = [10, 20, 4]
Output : 4
"""
l = [10, 20, 4]
print(min(l))

# or

# so, in this approach we first need to assume first element as min, without knowing
# if it is sorted or not

min_elem =l[0]
for i in range(len(l)):
    if l[i] < min_elem:
        min_elem=l[i]
print(min_elem)