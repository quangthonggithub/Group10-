m=int(input("enter m:"))
n=int(input("enter n:"))
if m<=n:
    min=m
else:
    min=n
d=min
while d>0:
    if m%d==0 and n%d==0:
        print("greatest common divisor is",d)
        break
    d=d-1