pi=3
k=1
for i in range(1,16,1):
    t=(2*i)*(2*i+1)*(2*i+2)
    p=4/t
    pi+=k*p
    k*=-1
    print("approximation",i,round(pi,i))