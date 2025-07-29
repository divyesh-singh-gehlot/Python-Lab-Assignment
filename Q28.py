num = [1,2,-1,-3,3,4,5, -7]
largest = num[0]
s_largest = num[0]

print(largest)

for i in num:
    if(i>largest):
        largest = i

print(largest)
