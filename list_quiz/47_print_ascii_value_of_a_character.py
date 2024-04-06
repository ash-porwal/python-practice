"""
he ASCII (American Standard Code for Information Interchange) value 
is a numerical representation of characters in computers
Each character (like a letter, number, or symbol) is assigned a unique number from 0 to 127
"""

# finding ASCII or Unicode value of alphabet
strng = input("Enter alpha to find its ASCII: ")
print(f"ASCII is: {ord(strng)}")

# finding char from ASCII value
print(chr(97))