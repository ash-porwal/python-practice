#  54321

n = 4
fac = 1
for i in range(1, n+1):
    fac *= i

print(fac)


# recursive way of doing it
def recur_case(n):
    # base
    if n==0:
        return 1
    # recursive case
    else:
        return n * recur_case(n-1)
print(recur_case(5))