test_list = [4, 5, 2, 6, 7, 8, 10]

n = 5 # want last 5 elements
print(test_list[-n:])

# or
l_index = -1
for i in range(n):
    print(test_list[l_index])
    l_index-=1