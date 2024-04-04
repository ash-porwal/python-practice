"""
Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5 

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4
"""

start = -4
end = 5

for i in range(start, end+1):
    if i>-1:
        print(i, end=",")