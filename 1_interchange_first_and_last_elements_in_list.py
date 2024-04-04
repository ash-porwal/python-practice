"""
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
"""

custom_lenght = int(input("Please lenght of list:"))

if custom_lenght <= 0:
    raise ValueError("List length should be a positive integer.")

custom_list = []

while custom_lenght:
    custom_lenght -= 1
    val = int(input("Please enter number: "))
    custom_list.append(val)
print("List before swapping: ", custom_list)
# first_element = custom_list[0]
# last_element = custom_list[-1]

# custom_list[0] = last_element
# custom_list[-1] = first_element

# better way
custom_list[0], custom_list[-1] = custom_list[-1], custom_list[0]
print(custom_list)