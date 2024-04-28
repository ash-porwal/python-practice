"""
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""
# My own logic
rows= int(input("number of rows: "))
space_before = rows-1
for i in range(1, rows+1):
    if i==rows:
        continue
    print(" "*space_before+"* "*i)
    space_before-=1
space_after = 0
for j in range(rows, 0, -1):
    print(" "*space_after + "* "*j)
    space_after+=1
