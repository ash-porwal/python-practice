"""
A string is said to be symmetrical if both the halves of the string are the same 
and a string is said to be a palindrome string if one half of the string is the reverse 
of the other half.

Example:
Symmetrical string: khokho
Plaindrome string: anna
"""

s="khokho"
len_of_string=len(s)//2
if s==s[::-1]:
    print("String is palindrome")
if s[:len_of_string]==s[len_of_string:]:
    print("String is symmetrical")