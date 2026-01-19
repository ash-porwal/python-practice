# Given an array arr[]. 
# Your task is to find the minimum and maximum elements in the array.

"""
Input: arr[] = [1, 4, 3, 5, 8, 6]
Output: [1, 8]
Explanation: minimum and maximum elements of array are 1 and 8.
"""

# first way
arr = [1, 4, 3, 5, 8, 6]
arr.sort()

max_val = arr[-1]
min_val = arr[0]
print(max_val, min_val)

# second way - if we cant sort it
# lets say - first element is min, and last element is max
arr = [1, 4, 3, 5, 8, 6]
temp_min = arr[0]
temp_max = arr[-1]
for i in arr:
    if i > temp_max:
        temp_max = i
    if i< temp_min:
        temp_min = i
print(temp_max, temp_min)

# with functions
arr = [1, 4, 3, 5, 8, 6]
print(max(arr), min(arr))
