"""
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
"""
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

uni_l = []
dupli_l = []
for i in list1:
    print("Value of i: ", i)
    if i not in uni_l:
        uni_l.append(i)
        print("Unique list: ", uni_l)
    elif i not in dupli_l:
        dupli_l.append(i)
        print("Duplicated list: ", dupli_l)
print(dupli_l)
    
    
# Using Counter 
from collections import Counter

l1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item]>1])
print(new_list)
