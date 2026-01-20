"""
Given a non-empty sequence of characters s, 
return true if sequence is Binary, else return false.

Input: s = "101"
Output: true
Explanation: Since string contains only '0' and '1', output is true
"""

s = '101'

# best way
print(set(s).issubset({'0', '1'}))


# full custom way
if sorted(set(s)) == ['0', '1'] or sorted(set(s)) == ['0'] or sorted(set(s)) == ['1']:
    print(True)
else:
    print(False)