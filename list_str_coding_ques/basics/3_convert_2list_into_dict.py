# Python program to convert two lists into dict
l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10,11,12]


# zip way 1
new_dict = {}
for k, v in zip(l1, l2):
    new_dict[k] = v
print(new_dict)

# zip way 2
print(dict(zip(l1, l2)))

# comprehensive way
dd = {k:v for k, v in zip(l1, l2)}
print(dd)

# full custom way
custom_dict = {}
for each_element in range(len(l1)):
    custom_dict[l1[each_element]] = l2[each_element]

print(custom_dict)