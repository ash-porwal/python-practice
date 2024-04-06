"""
Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
"""

list1 = [10, 20, 4]

# My first way
list1.sort()
print(list1[-2])

# second way

largest = secondLargest = float('-inf')  # Initialize to negative infinity
for number in list1:
    if number > largest:  # Found a new largest number
        secondLargest = largest  # Update second largest
        largest = number  # Update largest
    elif largest > number > secondLargest:  # Found a new second largest
        secondLargest = number
print(secondLargest)
