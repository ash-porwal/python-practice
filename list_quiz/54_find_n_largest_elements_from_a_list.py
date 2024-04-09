"""
Input : [4, 5, 1, 2, 9] 
        N = 2
Output :  [9, 5]

Input : [81, 52, 45, 10, 3, 2, 96] 
        N = 3
Output : [81, 96, 52]
"""
lst=[81, 52, 45, 10, 3, 2, 96] 
lst.sort()
n=3
nl=[]
for i in range(n):
    nl.append(lst[-1-i])
print(nl)

# without .sort
# need to sort the list

# using bubble sort
n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("sorted list: ", lst)