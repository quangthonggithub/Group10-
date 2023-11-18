s=0.00
while True:
    age=(input("enter age:"))
    if age=="":
        break
    age=int(age)
    if age<=2:
        s+=0.00
    if 3<=age<=12:
        s+=14.00
    if age>=65:
        s+=18.00
    if 13<=age<=64:
        s+=23.00
print("cost for group:",round(float(s),2))
