"""
Input: list1 = [2, 7, 5, 64, 14]
Output: [7, 5]

Input: list2 = [12, 14, 95, 3, 73]
Output: [95, 3, 73]
"""
list1 = [2, 7, 5, 64, 14]
nl = []
for i in list1:
    if i%2!=0:
        nl.append(i)
print(nl)