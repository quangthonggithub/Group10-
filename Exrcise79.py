import random
maximum = random.randint(1, 100)
count=0
for i in range(99): 
    number = random.randint(1, 100)
    print(number) 
    if number > maximum:
        maximum = number
        count+=1
        

print("The maximum value found was:", maximum)
print("the maximun value was updated",count,"time" )