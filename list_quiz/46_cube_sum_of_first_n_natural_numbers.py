n = int(input("Enter num: "))

add_cube = 0
for i in range(1, n+1):
    add_cube+=i**3
print(add_cube)

# Using list comprehension
print(sum([i**3 for i in range(1,n+1)]))