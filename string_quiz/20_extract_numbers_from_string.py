"""
Input: "There are 2 apples for 4 persons"
Output: [2, 4]
"""
s="There are 2 apples for 4 persons"
for i in s:
    if i.isdigit():
        print(i)