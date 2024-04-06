"""
Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]
"""
org_list = [12, 15, 3, 10]
Remove = [12, 3]

for i in Remove:
    # org_list.pop(org_list.index(i))
    org_list.remove(i)
print(org_list)