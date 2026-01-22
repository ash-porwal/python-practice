# find missing number in an array - with XOR and summation method
arr = [1, 2, 4, 5, 6, 7, 9]

# my own custom way
for i, v in enumerate(arr):
    if i == 0:
        continue
    if v-1 != arr[i-1]:
        print(v-1)


print("-"*10)
## other solution is when we generate a new list in that range
arr = [1, 3]
arr.sort()  # always sort it

new_list = list(range(arr[0],arr[-1]+1))
print(new_list)
print(set(new_list).difference(set(arr)))



#Third way - 
print("-"*10)
arr = [1,2,3,4,5,6,8]
# missing element

def missing_num(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    print("expected_sum",expected_sum)
    actual_sum = sum(arr)
    print("actual_sum",actual_sum)
    return expected_sum - actual_sum

print(missing_num(arr))