"""
Input:  geekforgeeks
Output: eeeefggkkors
Explaination:The Sorting the characters in ascending order gives us "eeeefggkkors".
"""
s= "geekforgeeks"

# another way, we can create dic and count val
min_ord=200
temp_d=[]
for i in s:
    if min_ord>ord(i):
        print(i)
        print(ord(i))
        min_ord=ord(i)
    temp_d.append(min_ord)
    min_ord=200
print(temp_d)
    