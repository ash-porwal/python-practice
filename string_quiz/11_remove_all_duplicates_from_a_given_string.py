"""
Input : geeksforgeeks 
Output : geksfor
"""

s="geeksforgeeks"
ns=""
for i in s:
    if i not in ns:
        ns+=i
print(ns)
