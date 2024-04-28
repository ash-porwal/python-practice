"""
Output:

    * 
   * * 
  * * * 
 * * * * 
* * * * * 


Logic to built programs like this

Here's how you could write the logic for the star pattern:

- Determine the number of stars in the largest row - this is the midpoint of the pattern.
- Determine the number of spaces before the first star in each row.
- Print each row with the appropriate number of spaces and stars.
"""

rows = int(input("Enter number of rows: "))

# ---- Someone from YT solution
# for i in range(rows): # this for loop is for rows
    # print("Vlaue of i: ", i)
    # for j in range(rows-i-1): # internal for loop is for columns
    #     print(end=" ") # printing spaces
    # for j in range(i+1): # internal for loop is for columns
    #     print("*", end=" ") # printing stars
    # print()

# My own solution
space_before = rows-1
for i in range(rows):
    print(" "*space_before +"* "*i)
    space_before-=1