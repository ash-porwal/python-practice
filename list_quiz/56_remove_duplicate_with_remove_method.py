# First Way
some_list = ["54123", "54123", "54456", "54789", "54789", "54123"]
for each_val in some_list[:]:
    while some_list.count(each_val)>1:
        some_list.remove(each_val)

print(some_list)


# Second way
# For a more concise way to remove duplicates, you can also use a dictionary.
some_list = ["54123", "54123", "54456", "54789", "54789", "54123"]
print(list(dict.fromkeys(some_list)))

# Third way
# type casting list into set
some_list = ["54123", "54123", "54456", "54789", "54789", "54123"]
print(set(some_list))