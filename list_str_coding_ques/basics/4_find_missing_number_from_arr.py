# find missing number in an array - with XOR and summation method
arr = [1, 2, 4, 5, 6, 7, 9]

# my own custom way
for i, v in enumerate(arr):
    if i == 0:
        continue
    if v-1 != arr[i-1]:
        print(v-1)


# for i in range(len(arr)):
#     if i ==0: continue
#     if arr[i]-1 != arr[i-1]:
#         print("Missing number: ", arr[i]-1)