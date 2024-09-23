"""
Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4] 
"""
custom_list = [4, 5, 6, 7, 8, 9]
new_list = []
indexx = -1
for i in custom_list:
    new_list.insert(indexx, i)
    indexx-=1
    print(indexx)
print(new_list)


# if i dont need to use any custom methods
new_list = []
for i in custom_list:
    new_list.insert(0, i)
print("I think the best way:\n",new_list)


## GFG solutions
# 1. Reverse List Using Slicing Technique

custom_list = [4, 5, 6, 7, 8, 9]
print(custom_list[::-1])

# List comprehension
print("List comprehension")
original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i]
			for i in range(1, len(original_list)+1)]
print(new_list)



#### Concept -
# I did this
l=[5,4]
# and if we print
print(l[-1]) # then we get 4 as on output

# but when i do 
l.insert(-1, 100)
print(l) # then we get output: [5, 100, 4]
# but why??

# Explain - 
"""
In Python, using the -1 index refers to the position just before the last element.

The key difference here is that negative indexing (like l[-1]) 
and the behavior of the insert method are two separate mechanisms in Python

- Negative indexing:
    When you access an element using a negative index, Python counts from the end of the list.
    l[-1] means "give me the last element."
    So, l[-1] fetches the value at the last position.

- insert method:
    The insert(index, value) method places the value before the given index.
    So when you do l.insert(-1, 100), 
    Python inserts 100 before the element at index -1, which is the last element.
"""