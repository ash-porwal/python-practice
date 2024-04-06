"""
An Armstrong number (also known as a narcissistic number) 
is a number that is equal to the sum of its own digits each raised to the power of the number 
of digits in the number. 

Example: 
153
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""
n = int(input("Enter number to checek if it is Armstrong or not: "))
len_of_n = len(str(n))

compare_num = 0
for i in str(n):
    compare_num+=int(i)**len_of_n
if compare_num == n:
    print("yes")
else:
    print("No")