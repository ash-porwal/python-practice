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
