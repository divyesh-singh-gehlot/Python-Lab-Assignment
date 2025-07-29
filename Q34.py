num = [1,2,-1,-3,3,4,5, -7]
even = 0
odd = 0

for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(odd)
print(even)