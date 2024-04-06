lst = [1,2,3]
print("lst id is: ", id(lst))

# Cloning
lst2 = lst[:]
print("lst2 id is: ", id(lst2))

# or we can clone with
lst3 = lst.copy() # it creates a shallow copy
print("lst3 id is: ", id(lst3))

# if need deep copy then 
lst4 = lst
print("lst4 id is: ", id(lst4))

# or we can import 
import copy
lst5 = copy.deepcopy(lst) # this is the slowest method
print("lst5 id is: ", id(lst5))