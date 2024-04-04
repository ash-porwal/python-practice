"""
Input : tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (','), ()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (',')]


Input : tuples = [(”,”,"8"), (), ("0", "00", "000"), ("birbal", ”, "45"), (”), (),  (”,”),()]
Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]
"""
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (','), ()]

for i in tuples:
    # print(i)
    if not i:
        # print(i)
        tuples.remove(i)
print(tuples)