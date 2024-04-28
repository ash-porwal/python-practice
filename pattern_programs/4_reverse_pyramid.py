"""
Output:

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""

rows = int(input("Enter number of rows: "))

space_before = 0
for i in range(rows, 0, -1):
    print(" "*space_before + "* "*i)
    space_before+=1