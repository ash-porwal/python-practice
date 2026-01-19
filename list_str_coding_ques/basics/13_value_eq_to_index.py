# Given an array arr. 
# Your task is to find the elements whose value is equal to that of its index value
"""
Input: arr[] = [15, 2, 45, 4 , 7]
Output: [2, 4]
Explanation: Here, arr[2] = 2 exists here and arr[4] = 4 exists here.
"""

arr = [15, 2, 45, 4 , 7]

for i, v in enumerate(arr):
    if i==v:
        print(v)
