"""
Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

Input: list2 = [12, 14, 95, 3]
Output: Even = 2, odd = 2
"""
list1 = [12, 14, 95, 3]
Even = 0
odd = 0

for i in list1:
    if i%2==0:
        Even+=1
    else:
        odd+=1
print(f"{Even}, {odd}")