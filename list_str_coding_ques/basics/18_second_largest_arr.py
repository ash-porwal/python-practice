"""
return the second largest element from the array. 
If the second largest element doesn't exist then return -1.

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
"""

# considering all the cases - 
arr = [12, 35, 1, 10, 34, 1]
# arr = [1]
# arr = [5,5,5]
arr = [10,5,10]
arr.sort()

if arr[0] == sum(arr)//len(arr):
    print(-1)
else:
    print(arr[-2])


# or we can convert into set(), and then get the second highest
arr = [10,5,10]
new_set = set(arr)
if len(new_set) == 1: 
    print(-1)
else:
    #sort it
    new_list = sorted(new_set)
    print(new_list[-2])