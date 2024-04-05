"""
Output expected:
*
* * *
* * * * *
"""
n = int(input("Enter number of stars: "))

for i in range(1,n+1, 2):
    print("* "*i)

# Another way
print()
print("Other way")
print()
for i in range(1, n+1, 2):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
