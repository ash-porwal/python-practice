"""
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : ['Learning', 'from']

Input : A = “apple banana mango” , B = “banana fruits mango”
Output : ['apple', 'fruits']
"""
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

for i in B.split():
    if i not in A.split():
        print(i, end=" ")