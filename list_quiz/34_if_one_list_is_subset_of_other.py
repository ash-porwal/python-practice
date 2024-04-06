l1 = [9, 4, 5, 8, 10]
l2 = [10, 5, 4]

any_num = ""
for i in l2:
    if i in l1:
        pass
    else:
        any_num = "Got new num"
if not any_num:
    print("Yes, list2 is a subset of list1")