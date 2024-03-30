a = 0
b = 1
n = int(input("enter the series number:"))
if n < 0 or n == 1:
    print("The series will:", a)
elif n == 2:
    print("the series will:", a, b)
else:
    print("the series will:", a, end=',')
    print(b, end=',')
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
        print(c, end=',')
