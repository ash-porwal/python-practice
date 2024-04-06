"""
A monotonic array is an array that is either entirely non-increasing or entirely non-decreasing. 
In simpler terms, 
the elements in a monotonic array are either always increasing or always decreasing 
(or remaining constant) but do not mix both behaviors.

Example =
[1,1,2,3,4]
[9,5,3,2,1]
"""
lst=[9,5,3,2,1]

# Not good when we have mix numbers in list- 9,5,3,2,10]
mono_increase=""
mono_dec=""
for i in range(1,len(lst)):
    if lst[i-1]<lst[i]:
        mono_increase="Monotone increasing"
    if lst[i-1]>lst[i]:
        mono_increase="Monotone decreasing"
if mono_dec:
    print(mono_dec)
if mono_increase:
    print(mono_increase)


#GFG logic - works for all cases
lst1,lst2=[],[]
lst1.extend(lst)
lst2.extend(lst)

#sorting
lst1.sort()
lst2.sort(reverse=False)

if lst1==lst or lst2==lst:
    print(True)
else:
    print(False)