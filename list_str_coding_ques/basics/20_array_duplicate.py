"""
Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
"""
temp_d = {}
arr = [2, 3, 1, 2, 3]
for i in arr:
    if i not in temp_d:
        temp_d[i] = 1
    else:
        temp_d[i] = temp_d[i]+1

print(temp_d)
for k,v in temp_d.items():
    if v>1:
        print(k, end=' ')
