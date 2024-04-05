"""
Input : list1 = [1, 2, 3, 4, 5] 
        list2 = [5, 6, 7, 8, 9]
Output : {5}
Explanation: The common element of the lists is 5. 

Input : list1 = [1, 2, 3, 4, 5] 
        list2 = [6, 7, 8, 9]
Output : No common elements 
"""
list1 = [1, 2, 3, 4, 5] 
list2 = [5, 6, 7, 8, 9]

for i in list1:
    if i in list2:
        print(i, end="")