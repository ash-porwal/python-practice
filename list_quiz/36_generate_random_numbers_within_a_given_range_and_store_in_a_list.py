"""
Input: num = 10, start = 20, end = 40
Output: [23, 20, 30, 33, 30, 36, 37, 27, 28, 38]
Explanation: The output contains 10 random numbers in range [20, 40]

Input: num = 5, start = 10, end = 15
Output: [15, 11, 15, 12, 11]
Explanation: The output contains 5 random numbers in range [10, 15]
"""

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
len_of_list = int(input("Enter length of list: "))

import random

result = random.sample(range(start, end + 1), len_of_list)
 
print(result)