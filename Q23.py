even = [2,2,4,4,4,6,8,10,12,14,16,18,20]

n = int(input("Enter number: "))
count = 0

for i in even:
    if(n==i):
        count+=1

print(count)