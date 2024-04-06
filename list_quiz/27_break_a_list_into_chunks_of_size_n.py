my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 

# first way: yield

def do_chunks(lst, num):
    for i in range(0, len(lst), num):
        yield lst[i:i+num]

call_back = do_chunks(my_list, 3)
for i in call_back:
    print(i)

# Method 2: Break a list into chunks of size N in Python using a loop
print("With for loop")
num = 3
for i in range(0, len(my_list), num): 
	print(my_list[i:i+num]) 
