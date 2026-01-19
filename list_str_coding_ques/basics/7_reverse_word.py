# Reverse Words but Not Characters
# Constraint:
#   Do not use split() or join()
'''
s ="python is fun"
output: "fun is python"
'''


# Let's first try with split()
new_s = ''

s ="python is fun"
for i in s.split():
    new_s = i + ' ' + new_s
print(new_s)

# second way
# following constraint of question
l = []
word = ''
for i in s:   #"python is fun"
    if i == ' ':
        l.append(word)
        word=''
    else:
        word+=i
l.append(word)
print(l)  # till here we got str into list

rev_l = l[::-1]
temp_str = ''
for each_word in rev_l:
    if temp_str:
        temp_str = temp_str + ' ' + each_word
    else:
        temp_str = temp_str + each_word


print(temp_str)
