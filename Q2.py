a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
c = int(input("Choose Operation: "))

if(c == 1):
    print("Sum is: ", a+b)
elif(c == 2):
    print("Difference is: ", a-b)
elif(c == 3):
    print("Product is: ", a*b)
elif(c == 4):
    print("Quotient is: ", a/b)
else:
    print("Choose a valid operation.")