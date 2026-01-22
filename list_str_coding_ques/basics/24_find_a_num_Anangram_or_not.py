"""
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, 
determine whether they are anagrams of each other or not.

Two strings are considered anagrams if they contain the same characters 
with exactly the same frequencies, regardless of their order.

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
"""

s1 = "geeks"
s2 = "kseeg"


def find_freq(text:str):
    temp_d = {}
    for i in text:
        if i not in temp_d:
            temp_d[i] = 1
        else:
            temp_d[i] = temp_d[i]+1
    return temp_d

freq_s1 = find_freq(s1)
freq_s2 = find_freq(s2)
print(freq_s1==freq_s2)