"""
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]
"""
lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)]

print(sorted(lst, key= lambda x:x[1]))


# Another way - TODO