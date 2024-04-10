s="Geeksforgeeks is best Computer Science Portal"
temp_n=0
for i in s.split():
    temp_n+=1
print(temp_n)

# or
print(len(s.split()))

# without using split
print(s.count(" ")+1)