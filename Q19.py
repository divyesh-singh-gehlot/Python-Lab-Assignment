n = int(input("Enter number: "))

even = [2,4,6,8,10,12,14,16,18,20]

found = False

for i in (even):
    if(n == i):
        found = True

print("Found!") if found else print("Not found")