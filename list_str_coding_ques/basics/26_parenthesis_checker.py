"""
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. 
Determine whether the Expression is balanced or not.

An expression is balanced if:
    1. Each opening bracket has a corresponding closing bracket of the same type.
    2. Opening brackets must be closed in the correct order.

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.

Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end
"""

# no matter what we will find a pair of it, which are open and closed right away
# if we dont find even a single pair which doesnt open and close right away - then the brackets are not in correct form.

s = "[{()}]"
s = "([{])"
c= 0
while True:
    c+=1
    print(f"Value of s -> {s} in {c} loop")
    if '[]' in s:
        s = s.replace('[]', '')
    if '()' in s:
        s = s.replace('()', '')
    if '{}' in s:
        s = s.replace('{}', '')
    else:
        break

if not s:
    print("All brakcets are well formed")
else:
    print(f"The expression is not balanced, found not balanced {s}")