# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

num=int(input("Enter number to take factorial!: "))

#using loop
temp_val = 1
for i in range(1, num+1):
    temp_val*=i
print(temp_val)


# using recursion
def find_factorial(num):
    if num==1:
        return 1
    else:
        return num * find_factorial(num-1)

val = find_factorial(num)
print(val)
