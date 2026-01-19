# convert str into list
s = 'I am Ashish Porwal'


# Input: s = 'I am Ashish Porwal'
# Output: ['I', 'am', 'Ashish', 'Porwal']

# with method
print("This is with method:",s.split())

# custom way to extract each element
temp_str = ''
temp_list = []
for each_letter in s:
    temp_str+=each_letter
    # print(temp_str)
    if each_letter == ' ':
        temp_list.append(temp_str)
        temp_str=''


# Appending last word
temp_list.append(temp_str)
print("Custom way:",temp_list)

