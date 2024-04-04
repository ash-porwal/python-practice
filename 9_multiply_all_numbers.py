"""
Input :  list1 = [1, 2, 3]
Output : 6
"""
c_l = [1,2,3]

temp_val = 1
# first way
for i in c_l:
    temp_val *= i

print(temp_val)