ini_list = "[1, 2, 3, 4, 5]"

# one way we can use JSON object
import json

some_val = json.loads(ini_list)
print(f"{some_val} ---> {type(some_val)}")

# stripping
# some_val = ini_list.strip('][').split(', ')
some_val = ini_list.strip('[]').split(', ')
print(f"{some_val} ---> {type(some_val)}")
