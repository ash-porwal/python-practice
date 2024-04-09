test_str = "GeeksforGeeks"
temp_dict={}
temp_val=1
for i in test_str:
    if temp_dict.keys():
        temp_val+=1
        temp_dict[i]=temp_val
    else:
        temp_dict[i]=temp_val


print(temp_dict)
print(list(temp_dict.values()))

# or we can use counter from collections
from collections import Counter

test_str = "GeeksforGeeks"
res = Counter(test_str)
res = min(res, key = res.get) 
print(res)
