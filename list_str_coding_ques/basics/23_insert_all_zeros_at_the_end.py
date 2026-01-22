l = [0,5,0,10,0,15]
# expected output: [5,10,15,0,0,0]

# for i in l:
#     if i==0:
#         l.remove(i)
#         l.append(i)
#     else:
#         continue

class MoveZerosAtEnd:

    def __init__(self, dummy_list):
        self.temp_list = dummy_list
    
    def remove_zeros(self):
        c = 0
        for i in self.temp_list:
            c+=1
            if i==0:
                print(f"Loop count {c} and value of temp_list is -> {self.temp_list}")
                self.temp_list.remove(i)
                print(f"Loop count {c} and value of temp_list is  after remove operation-> {self.temp_list}")
                self.temp_list.append(i)
                print(f"Loop count {c} and value of temp_list is  after append operation-> {self.temp_list}")
        return self.temp_list

mz = MoveZerosAtEnd(l)
print(mz.remove_zeros())