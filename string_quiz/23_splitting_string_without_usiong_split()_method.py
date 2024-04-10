#  it depends upon the delimeter we are using

s = "Hello,World,Here"
delimiter = ","
temp_list=[]
temp_s=""
for i in s:
    if i==delimiter:
        temp_list.append(temp_s)
        temp_s=""   
    else:
        temp_s+=i
temp_list.append(temp_s) # add last word
print(temp_list)