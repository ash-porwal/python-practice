# Aim: Make a list in 1-D
matrix = [[9, 3, 8, 3],[4, 5, 2, 8],[6, 4, 3, 1],[1, 0, 4, 5]]

"""
Note: It's important to note that the examples will only work on lists with one nesting level. 
      For deeper nesting, you’d need a different and more complex algorithm.
"""

# First way: my first try - with for loop and empty list
temp_list = []
for each_list in matrix:
    for each_item in each_list:
        temp_list.append(each_item)

print(f"First way output: {temp_list}")

# Second way: we can decrease one for loop from above logic if we use .extend() function
second_temp_list = []
for each_list in matrix:
    second_temp_list.extend(each_list)  # extend expects an iterable, so make just the object we pass in extend function is an iterable.
print(f"Second way output: {second_temp_list}")


# Third way: We can use argumented concatination operator (+=) which works same as .extend()
third_temp_list = []
for each_list in matrix:
    third_temp_list+=each_list  # this only works with if we are adding an iterable to another list
print(f"Third way output: {third_temp_list}")


# Fourth way: Using List comprehension
fourth_temp_list = [each_item for item in matrix for each_item in item]
print(f"Fourth way output: {fourth_temp_list}")

# Fifth way: built-in function sum()
print(f"Fifth way output: {sum(matrix, [])}")
"""
The sum() function in Python typically adds numbers together. 
However, it can also be used more flexibly with its two parameters: 
the first parameter is the iterable you want to sum up, 
and the second parameter is the starting value

Flattening with sum(): 
When you use sum() to flatten a list of lists, 
you pass the list of lists as the first argument and an empty list [] as the second argument. 
What happens is that sum() starts with the empty list 
and then concatenates each sublist in your matrix to this starting list.
"""

# Sixth way: Using Chain function from built-in itertools module
from itertools import chain
print(f"Sixth way output: {list(chain.from_iterable(matrix))}")

"""
Note:
    itertools.chain() can efficiently flatten lists by creating an iterator 
    that yields items from all input iterables, which can be more memory-efficient.
"""