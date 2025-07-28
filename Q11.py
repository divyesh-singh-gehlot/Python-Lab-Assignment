first = 0
second = 1
n = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(n):
    print(first)
    current = first + second
    first = second
    second = current
