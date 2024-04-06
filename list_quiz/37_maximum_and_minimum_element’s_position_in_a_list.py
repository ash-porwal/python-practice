"""
Input:  3, 4, 1, 3, 4, 5
Output:  
    The maximum is at position 6
    The minimum is at position 3
"""
lst = [3, 4, 1, 3, 4, 5]

let_max = lst[0]
for i in lst:
    if i>=let_max:
        let_max = i

print(f"The maximum is at position {lst.index(let_max)+1}")