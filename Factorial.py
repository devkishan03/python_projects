# import math

# factorial of a number
n = int(input("Enter the number:"))
num = n
if n < 2:
    print("factorial will be: 1")
else:
    for i in range(1, n):
        num = num * i
    print("Factorial will be:", num)

# inbuilt factorial function
# print(math.factorial(n))


