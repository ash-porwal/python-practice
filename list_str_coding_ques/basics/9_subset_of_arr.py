"""
Given two arrays a[] and b[], 
your task is to determine whether b[] is a subset of a[].

-- b is a subset of a if every element of b exists in a.
-- The elements of b do not need to appear in the same order as in a.

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
"""
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7, 11]


# first custom way
for i in b[:]:
    if i in a:
        b.remove(i)
if not b:
    print("yes")



# second custom way - should work if duplicate doesn't matter
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7, 11]

print(set(b).issubset(set(a)))


# but above approach fails when we have duplicate values like - 
a = [1]
b = [1,1]
# for a solid appraoch alawys get their frequency

def count_fre(arr):
    word_freq = {}
    for i in arr:
        if i not in word_freq:
            word_freq[i] = 1
        else:
            word_freq[i] = word_freq[i]+1
    return word_freq 

freq_a = count_fre(a)
freq_b = count_fre(b)

# Check subset condition
is_subset = True
for k in freq_b:
    if k not in freq_a or freq_b[k]>freq_a[k]:
        is_subset = False
        break
print(is_subset)
