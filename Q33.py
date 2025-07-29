start = int(input("Enter starting point: "))
end = int(input("Enter ending pont: "))

for i in range(start, end+1):
    if(i % 2 != 0):
        print(i)