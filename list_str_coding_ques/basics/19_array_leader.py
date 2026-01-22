"""
Your task is to find all the leaders in the array. 
An element is considered a leader if it is greater than or equal to all elements to its right.
The rightmost element is always a leader.

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

Input: arr = [10, 4, 2, 4, 1]
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, 
    as to be a leader an equal element is also allowed on the right. side
"""

arr = [16, 17, 4, 3, 5, 2]

all_learders = []
temp_leader = -1

for i in range(len(arr)-1, -1, -1):
    if arr[i]>=temp_leader:
        temp_leader=arr[i]
        all_learders.append(temp_leader)
print(all_learders[::-1])
