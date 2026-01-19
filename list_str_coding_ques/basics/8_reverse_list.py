l  = [1,2,3,4]

# easiest way, but it is like shorthand
print(l[::-1])

# with reverse function
l.reverse()
print(l)

# custom way
l  = [1,2,3,4]
rev_l = []

for item in l:
    rev_l.insert(0, item)

print(rev_l)


# other custom way
lst = [1, 2, 3, 4]
rev = []

for i in range(len(lst) - 1, -1, -1):  # running range() in reverse
    rev.append(lst[i])

print(rev)
