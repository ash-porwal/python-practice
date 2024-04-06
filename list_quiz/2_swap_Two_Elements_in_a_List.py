"""
Given a list in Python and provided the positions of the elements, 
write a program to swap the two elements in the list. 

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""

# def generate_index(pos):
#     return pos - 1


given_list = [1, 2, 3, 4, 5]
pos1 = 2
pos2 = 5

index_num1 = pos1 - 1
index_num2 = pos2 - 1
given_list[index_num1], given_list[index_num2] = given_list[index_num2], given_list[index_num1]
print(given_list)
