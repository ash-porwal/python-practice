start_val = int(input("Enter start number: "))
end_val = int(input("Enter end number: "))


armstrong_list = []
for i in range(start_val, end_val+1):
    temp_num = 0
    len_of_num = len(str(i))
    for j in str(i):
        temp_num+=int(j)**len_of_num
    if temp_num == i:
        armstrong_list.append(i)
print(armstrong_list)