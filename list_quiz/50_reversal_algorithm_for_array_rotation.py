"""
Write a function rotate(arr[], d, n) 
that rotates arr[] of size n by d elements. 

Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output: arr[] = [3, 4, 5, 6, 7, 1, 2] 
"""
def rotate_arr(lst, d):
    return lst[d:]+lst[:d]



lst=[1, 2, 3, 4, 5, 6, 7]
d=2
print(rotate_arr(lst, d=d))
