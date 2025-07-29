n = int(input("Enter number: "))

flag = True

for i in range(2 , n):
    if(n%i == 0):
        flag = False

flag ? print("Prime") : print("Not Prime.")