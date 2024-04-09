"""
Input : test_str = 'Gfg is best' 
Output : {'Gfg': 1, 'is': 1, 'best': 1} 
"""
# s="Gfg is best Gfg"
s="Gfg is best . Geeks are good and Geeks like Gfg"

count_dict={}
val=1
for i in s.split():
    if i in count_dict.keys():
        val+=val
    count_dict[i]=val
print(count_dict)