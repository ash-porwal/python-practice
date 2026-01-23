"""
Given an unsorted array arr[] of size n, 
containing elements from the range 1 to n, 
it is known that one number in this range is missing, 
and another number occurs twice in the array, 

find both the duplicate number and the missing number.


Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and the missing number is 1.
"""

class Solution:
    def find_two_element(self, arr):
        temp_d = {}
        for i in arr:
            if i not in temp_d:
                temp_d[i] = 1
            else:
                temp_d[i] = temp_d[i]+1
        for k, v in temp_d.items():
            if v>1:
                repeated_num = k
        

        temp_s = set(range(1, len(arr)+1))
        missing_num = temp_s.difference(set(arr)).pop()
        
        return [repeated_num, missing_num]
