"""
Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.

Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
Output: [-3, 4, 5, 6, 7, -1, -2]

Input: arr[] = [1, 3, 4, 2], d = 3 
Output: [2, 1, 3, 4]
"""

k = 3
arr = [1,3,4,2]
print(arr[k:]+arr[:k])
