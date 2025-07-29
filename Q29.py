num = [1,2,-1,-3,3,4,5, -7]
largest = num[0]
s_largest = num[0]

for i in num:
    if(i>largest):
        s_largest = largest
        largest = i

print(s_largest)
