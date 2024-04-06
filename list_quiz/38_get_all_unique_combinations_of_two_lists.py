"""
List_1 = ["a","b"]
List_2 = [1,2]
Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 
"""
list_1 = ["b", "c", "d"]
list_2 = [1, 4, 9]
 
unique_combinations = []
 
for i in range(len(list_1)):
    for j in range(len(list_2)):
        unique_combinations.append((list_1[i], list_2[j]))
 
print(unique_combinations)
print()

# Using permutation() of itertools package and zip() function.

import itertools

# initialize lists
list_1 = ["a", "b", "c","d"]
list_2 = [1,4,9]

# create empty list to store the combinations
unique_combinations = []

# Getting all permutations of list_1 
# with length of list_2
permut = itertools.permutations(list_1, len(list_2))

# zip() is called to pair each permutation
# and shorter list element into combination
for comb in permut:
	zipped = zip(comb, list_2)
	unique_combinations.append(list(zipped))

# printing unique_combination list 
print(unique_combinations)
