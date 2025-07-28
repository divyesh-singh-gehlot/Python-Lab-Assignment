x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

maximum = x if x > y else y
if z > maximum : maximum = z

print("Maximum number: ", maximum)