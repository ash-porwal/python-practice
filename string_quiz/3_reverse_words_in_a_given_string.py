"""
Input : str ="geeks quiz practice code"
Output : str = code practice quiz geeks  
Input : str = "my name is laxmi"
output : str= laxmi is name my 
"""
s="geeks quiz practice code"
nl=[]
for i in s.split():
    nl.insert(0,i)

print(" ".join(nl))
