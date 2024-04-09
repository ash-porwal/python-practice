"""
Input : str = "hello geeks for geeks 
          is computer science portal" 
        k = 4
Output : hello geeks geeks computer 
         science portal
Explanation : The output is list of all 
words that are of length more than k.
"""
s="hello geeks for geeks is computer science portal" 
k=4
for i in s.split():
    if len(i)>k:
        print(i, end=" ")
