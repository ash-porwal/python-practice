# count frequency of words in a string


# first way
from collections import Counter

s = 'Ashish is struggling in solving DSA.'
print(Counter(s))
# print(Counter(s.split()))  # in case if we want to count words instead of each letters

# Custom way - 
print()
# print(s.split(' '))
temp_dict = {}
for i in s:
    if i not in temp_dict:
        temp_dict[i] = 1
    else:
        temp_dict[i] = temp_dict[i] + 1
print(temp_dict)


# shorted way
s = "count frequency of words in a string count"
temp_d = {}
for i in s.split():
    temp_d[i] = temp_d.get(i, 0) + 1
print("shorted frequency counter:", temp_d)