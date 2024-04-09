"""
Input : malayalam
Output : Yes

Input : geeks
Output : No
"""

strr= "asdsad"
if strr==strr[::-1]:
    print("Yes")
else:
    print("No")

# Or

strr= "asdsad"

new_str = ""
for i in strr:
	new_str = i + new_str

if (strr == new_str):
	print("Yes")
else:
	print("No")
