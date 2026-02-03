"""
https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1?page=1&category=Arrays,Strings&difficulty=Easy&status=unsolved&sortBy=submissions
"""

arr = [0,0,0]

full_list = []
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i], arr[j])
        if arr[i] != arr[j] and arr[i]+arr[j] ==0:
            temp_list = [arr[i], arr[j]]
            temp_list.sort()
            if temp_list not in full_list:
                full_list.append(temp_list)
print(full_list)
                