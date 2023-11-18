a=(input("enter a binary:"))
b=len(a)
decimal=0
for i in a:
    i=int(i)
    c=i*(2**(b-1))
    decimal+=c
    b=b-1
print(decimal)