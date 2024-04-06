"""
Input: 8
Output: Yes

Input: 34
Output: Yes

Input: 41
Output: No
"""
n = int(input("Enter to check: "))

start =0
next_num=1
fibo_list = [0]
for i in range(0,n+1):
    fibo_list.append(next_num)
    temp=start+next_num
    start=next_num
    next_num=temp
print(n)
print(fibo_list)
if n in fibo_list:
    print("yes")
else:
    print("No")
    
