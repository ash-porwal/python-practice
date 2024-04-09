"""
Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
"""
s="hello"

temp_l=[]

for i in s:
    if i not in temp_l and s.count(i)>1:
        temp_l.append(i)
print(temp_l)

# or

s="hello"
temp_dict={}
for i in s:
    temp_val=1
    if i in temp_dict:
        print(i)
        temp_val+=1
    temp_dict[i]=temp_val
print(temp_dict)
for k,v in temp_dict.items():
    if v>1:
        print("Found duplicate: ", k)