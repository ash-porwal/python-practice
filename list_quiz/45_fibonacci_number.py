"""
A Fibonacci number is part of a sequence where each number (after the first two) 
is the sum of the two preceding ones. 
The sequence typically starts with 0 and 1, but it can also start with two ones. 
Here's how the sequence starts:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

# start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

start_num=0
next_num=1
for i in range(end+1):
    print(next_num)
    temp_num=start_num+next_num
    start_num =next_num
    next_num=temp_num

# with recusion


