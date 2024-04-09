#Input:
# code = 
#""" a = 6+5
#    print(a)"""
# Output:
# 11

s="""a = 6+5
print(a)"""

# we can use exec() function
#  exec() function in Python dynamically executes the Python code it receives.
# The code can be a string, an object, or a code object. 
exec(s)


code = """
def greet(name):
    return 'Hello, ' + name

result = greet('Alice')
"""
exec(code)
print(result)  # This will print "Hello, Alice"



# we can use eval() function
# eval() function in Python evaluates a given expression string and 
# executes it as a Python expression. 
# Unlike exec(), which can execute a block of Python code including statements, 
# print(eval(s))
result = eval('5 + 3')
print(result)  # This will print 8
