"""
Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]

Input : list = [4, 10, 15, 18, 20]
Output : [4, 14, 29, 47, 67]
"""

lst=[10, 20, 30, 40, 50]
temp_num = 0
nl=[]
for i in range(len(lst)):
    temp_num+=lst[i]
    nl.append(temp_num)
print(nl)