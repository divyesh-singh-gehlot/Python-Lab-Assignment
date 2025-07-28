i1 = int(input("Enter first index: "))
i2 = int(input("Enter second index: "))

fruits = ["Apple" , "Mango" , "Banana" , "Pineapple" , "Custard Apple"]

print(fruits)

if((i1<0 or i1>=len(fruits)) or (i2<0 or i2>=len(fruits))):
    print("Invalid Index")
else:
    fruits[i1] , fruits[i2] = fruits[i2] , fruits[i1]

print(fruits)