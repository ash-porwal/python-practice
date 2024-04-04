lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

uni_l = []
# for i in lst1:
#     if i in lst2:
#         uni_l.append(i)
# print(list(set(uni_l)))

uni_l = [i for i in lst1 if i in lst2]
print(uni_l)