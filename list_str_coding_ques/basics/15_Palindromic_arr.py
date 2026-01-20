"""
Given an array arr[] of positive integers. 
Return true if all the array elements are palindrome otherwise, return false.

Input: arr[] = [111, 222, 333, 444, 555]
Output: true
"""
arr = [111, 222, 333, 444, 555]
for i in arr[:]:
    if str(i) == str(i)[::-1]:
        arr.remove(i)
if not arr:
    print(True)
