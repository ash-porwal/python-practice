"""
Input: geeks
Output : ['g', 'e', 'e', 'k', 's']
Input: Word
Output : ['W', 'o', 'r', 'd']
"""
s="geeks"
temp_list=[]
for i in s:
    temp_list.append(i)
print(temp_list)

# another method - if we just unpack
print([*s])

# or if we just convert into a list
print(list(s))