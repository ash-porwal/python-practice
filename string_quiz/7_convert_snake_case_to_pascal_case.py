"""
Input : geeks_for_geeks 
Output : GeeksforGeeks 

Input : left_index 
Output : leftIndex
"""
s="geeks_for_geeks"
for i in s.split("_"):
    print(i.capitalize(), end="")