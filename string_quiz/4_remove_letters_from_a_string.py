"""
Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.
"""
s="Geeks123For123Geeks"

for i in s:
    if i.isnumeric():
        print(i)
        s = s.replace(i, "")
print(s)