# Ap series
s=int(input("enter starting point:"))
d=int(input("enter difference:"))
n=int(input("number of series:"))
print("the series will: ",end='')
for i in range(0,n):
    print(s,end=',')
    s+=d

