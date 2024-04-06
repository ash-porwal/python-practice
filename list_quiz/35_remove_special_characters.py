"""
Input: "Ge;ek * s:fo ! r;Ge * e*k:s !"
Output: GeeksForGeeks
Explanation: In This, we are removing special characters from string in Python.
"""

stringg = "Ge;ek * s:fo ! r;Ge * e*k:s !"

"""
isalnum() method checks 
whether all the characters in a given string are either alphabet or numeric (alphanumeric) characters.
isalnum() method takes no parameters
"""

# tuple comprehension will create generator
test_tuple = (letter for letter in stringg if letter.isalnum())
print(test_tuple)

for i in test_tuple:
    print(i, end="")