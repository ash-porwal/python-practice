"""
Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
"""

some_list = [1, 6, 3, 5, 3, 4]
n = int(input("Number to test: "))

for i in some_list:
    if n == i:
        print(True)

# better is if we do like below - 
if n in some_list:
    print("Yes")

# or as a one liner
print("Yes") if n in some_list else "No"