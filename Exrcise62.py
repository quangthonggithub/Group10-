discount=0.6
p=[4.95,9.95,14.95,19.95,24.95]
print("original price  |   discount    |   new price  ")
print("--------------------------------------------------")
for i in p:
    print("$",i,"       \t$",round(i*0.6,2),"       \t$",round(i-i*0.6,2),)