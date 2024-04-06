"""
Input : list1 = [10, 20, 4]
Output : 20
"""
list1 = [10, 20, 4]

max_val = list1[0]
for i in range(len(list1)):
    if list1[i] > max_val:
        max_val = list1[i]
print(max_val)