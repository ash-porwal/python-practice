# Find out pairs with given sum value of an arr
arr = [5,7,4,3,9,8,19,21]
s_sum = 17

# below is first i tried but i think is wrong
for ev in arr:
    if ev<s_sum:
        rem_val = s_sum-ev
        if rem_val in arr:
            print(f"{rem_val} and {ev}")
            

# For these questions:
# Step1: Sort the arr in ASC
# arr.sort()
# print(arr)

# Step2: We need target sum, which is 17 in our case
# Step3: Take the first index value and last index value