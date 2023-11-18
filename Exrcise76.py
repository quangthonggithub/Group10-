n=int(input("enter n:"))
if n <=2:
    print("error")
factor=2
while factor <=n:
    while n %  factor ==0:
        print(factor)
        n=n/factor
    factor+=1