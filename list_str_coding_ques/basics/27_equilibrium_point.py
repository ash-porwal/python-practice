"""
Given an array of integers arr[], 
the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) 
such that the sum of all elements before that index is the same as the sum of 
elements after it. Return -1 if no such point exists. 


Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.


Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
"""

# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def find_equilibrium(self, arr):
        # code here
        for i in range(len(arr)):
            if sum(arr[:i])== sum(arr[i+1:]):
                return i
        return -1


# optimized code
class OSolution:
    def find_equilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            print("total sum", total_sum )
            right_sum = total_sum - left_sum - arr[i]
            print("right_sum ", right_sum )

            if left_sum == right_sum:
                return i

            print("left_sum before ->", left_sum )
            print('Value of arr[i]', arr[i])
            left_sum += arr[i]
            print("left_sum after ->", left_sum )
            print()

        return -1
    
arr = [8, 6, 10, 6, 3, 1, 4, 3, 8, 4, 14]

o_sol = OSolution()
print(o_sol.find_equilibrium(arr=arr))