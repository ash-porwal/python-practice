"""
Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am
"""
s = "This is a python language"
s=s.split()
for i in range(1,len(s)+1):
    if i%2==0:
        print(s[i])