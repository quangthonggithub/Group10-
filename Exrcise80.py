import random

sum=0
for i in range(1,11):
    count_T=0
    count_H=0
    flip=0
    result=""
    while True:
      a= random.randint(1,2)
      flip+=1
      if a==1:
        count_T+=1
        count_H=0
        result+=" T"
      else:
        count_H+=1
        count_T=0
        result+=" H"
      if (count_T==3) or count_H==3:
        print(result,flip,"(flips)")
      
        break
    print("")
    sum+=flip
print("on average,",sum/10,"flips were needed")