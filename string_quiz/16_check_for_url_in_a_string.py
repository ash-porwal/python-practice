"""
Input : string = 'My Profile: 
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
in the portal of https://www.geeksforgeeks.org/'

Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
'https://www.geeksforgeeks.org/']

Input : string = 'I am a blogger at https://geeksforgeeks.org'
Output : URL :  ['https://geeksforgeeks.org']
"""
stringg = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'

for i in stringg.split():
    if i.find("https")==0 or i.find("http")==0:
        print(i)


