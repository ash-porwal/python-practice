"""
Input : [1, 2, 3, 4]
Output : (1, 2, 3, 4)

Input : ['a', 'b', 'c']
Output : ('a', 'b', 'c')
"""
l =[1,2,3]

# First way
print(tuple(l))

# Second way
print(*l,)

print()
# Creating a dictionary
myDict = {}
myDict['Geeks'] = "test"

print(myDict)
