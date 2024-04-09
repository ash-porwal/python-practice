"""
Input: Substring = "geeks" 
            String="geeks for geeks"
Output: yes
Input: Substring = "geek"
           String="geeks for geeks"
Output: yes
Explanation: In this, we are checking if the substring is present in a given string or not.

"""
s="geeks for geeks"
find_word="geeks"

print("Yes" if find_word in s else "No")