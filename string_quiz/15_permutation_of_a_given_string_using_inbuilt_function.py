"""
Input :  str = 'ABC'
Output : ABC 
         ACB 
         BAC 
         BCA 
         CAB 
         CBA
"""
from itertools import permutations
str = 'ABC'
permList = permutations(str)

print(permList)
for perm in list(permList):
    print (''.join(perm))