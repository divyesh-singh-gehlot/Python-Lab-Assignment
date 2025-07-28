i1 = int(input("Enter first index: "))
i2 = int(input("Enter second index: "))

even = [2,4,6,8,10,12,14,16,18,20]

print(even)

if((i1<0 or i1>=len(even)) or (i2<0 or i2>=len(even))):
    print("Invalid Index")
else:
    even[i1] , even[i2] = even[i2] , even[i1]

print(even)