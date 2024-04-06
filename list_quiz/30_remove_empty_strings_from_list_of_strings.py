test_list = ["", "GeeksforGeeks", "", "is", "best", ""]


nl = [i for i in test_list if i]
print(nl)

# other way
while ("" in test_list):
    test_list.remove("")
print(test_list)