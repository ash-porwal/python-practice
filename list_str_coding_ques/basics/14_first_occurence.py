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

print(txt.find(pat))


# way 2
for i in txt:
    if i == pat[0]:
        idx = txt.index(i)
        len_pat = len(pat)
        # print(txt[idx: idx+len_pat])
        if txt[idx: idx+len_pat] == pat:
            print("pattern matched")
            print(idx)