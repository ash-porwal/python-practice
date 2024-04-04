"""
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
"""

# My first approach - but complexity of O(n^2)
some_list = [12, 67, 98, 34]
new_list = []
for i in some_list:
    full_dig = 0
    for j in str(i):
        full_dig += int(j)
    new_list.append(full_dig)

print(new_list)


# GFG way
lst = [12, 67, 98, 34]
def digit_sum(num):
	digit_sum = 0
	while num > 0:
		print("before num: ", num)
		print("before digital_sum: ",digit_sum)
		print("num % 10: ", num % 10)
		digit_sum += num % 10
		print("after digital_sum: ",digit_sum)
		num //= 10
		print("after num: ",num)
	return digit_sum

def sum_of_digits_list(lst):
	return list(map(digit_sum, lst))

print(sum_of_digits_list(lst))
