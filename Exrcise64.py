#a=Pennies(Xu)
#b=Nickel(1 nickel=5 xu)
a=input('Enter the amount:')
Total=0
while a!="":
    Total=Total+float(a)
    a=(input('Enter the amount:'))
if Total%5<2.5:
    b=int(Total/5)
elif Total%5>2.5:
    b=int(Total/5)+1
print('The total cost of all the entered itemsL:',Total,'Pennies[Xu]')
print('Pays with cash:',b)



    