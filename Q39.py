num = [1,2,-1,-3,3,4,5, -7, 0]
positive = 0
negative = 0

for i in num:
    if i ==0:
        continue
    if i>0:
        positive+=1
    else:
        negative+=1

print(positive)
print(negative)