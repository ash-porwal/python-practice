"""
Input: s = 'Geeks'
Output: 'skeeG'
"""

s = 'Ashish'
# first way - we can use slicing in reverse
print(s[::-1])


# second way, a bit more custom
temp_s = ''
for i in s:
    temp_s = i+temp_s
print(temp_s)
