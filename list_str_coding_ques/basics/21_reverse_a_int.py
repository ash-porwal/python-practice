n = 123
# output expected: 321

# first way
print(int(str(n)[::-1]))


# without shortcut
inital_value = 0

while n > 0:
    remainer = n%10
    inital_value = (inital_value*10) + remainer
    n = n//10

print(inital_value)