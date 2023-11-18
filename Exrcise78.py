a=int(input("decimal:"))
result=""
while a!=0:
    r=a%2
    result+=str(r)
    a=int(a/2)
for i in range(len(result),0,-1):
    print(result[i-1],end="")