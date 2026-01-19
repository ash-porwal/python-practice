# Given two strings txt and pat, 
# return the 0-based index of the first occurrence of the substring pat in txt. 
# If pat is not found, return -1.
# Note: You are not allowed to use the inbuilt function.

"""
Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.

Second example:
Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: "For" is present as substring in "GeeksForGeeks" from index 5 (0 based indexing).
"""
txt = "GeeksForGeeks"
pat = "For"

val = -1
for i in txt:
    if pat[0] == i:
        val = txt.index(i)
print(val)
    