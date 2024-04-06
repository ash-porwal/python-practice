file_num = input("Please enter file number: ")
string_val = input("Please enter: ")
file_name = file_num + "_" + string_val.replace(" ", "_").lower() + ".py"

with open(file_name, 'w') as f:
    ...