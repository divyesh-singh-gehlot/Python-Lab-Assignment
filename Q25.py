num = [11,12,13,14,15, 16]
sum = 0

for i in num:
    j=i
    while(j > 0):
        digit = j % 10
        j //= 10
        sum += digit

print(sum)