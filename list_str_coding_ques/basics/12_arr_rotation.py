# Given an array arr, 
# rotate the array by one position in clockwise direction.
"""
Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
"""

# my first approach
arr = [1, 2, 3, 4, 5]
last_idx = arr[-1]
arr.insert(0, last_idx)
arr.pop(-1)
print(arr)

# best approach - slicing
arr = [1, 2, 3, 4, 5]
arr = arr[-1:] + arr[:-1]
print(arr)
