start=int(input("Enter start number: "))
end=int(input("Enter end number: "))

prime_list = []
for i in range(start, end+1):
    if i%2!=0:
        prime_list.append(i)
print(prime_list)
