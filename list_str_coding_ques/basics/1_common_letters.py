s1 = 'NAINA'
s2 = 'REENE'

# find common letters between strings
# common_letter = []
# for i in s1:
#     if i in s2:
#         common_letter.append(i)
# print(set(common_letter))

common_letter = set(s1) & set(s2)
print(common_letter)