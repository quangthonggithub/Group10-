n=float(input("enter number: "))
if n==0:
    print("unvalid")
else:
    sum =n
    count =1
    while True:
        n=float(input("enter number:"))
        if n==0:
            break
        else:
            sum=sum+n
            count=count+1
        
    print("average:",sum/count)