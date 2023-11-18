#a=Letter Grade
#b=Mark
Total=0
Count=0
a=input('Letter grades:')
while a!='':
    if a=='A+':
        b=4.0
    elif a=='A':
        b=4.0
    elif a=='A-':
        b=3.7
    elif a=='B+':
        b=3.3
    elif a=='B':
        b=3.0
    elif a=='B-':
        b=2.7  
    elif a=='C+':
        b=2.3
    elif a=='C':
        b=2.0
    elif a=='C-':
        b=1.7
    elif a=='D+':
        b=1.3
    elif a=='D':
        b=1.0
    elif a=='F':
        b=0
    Total = Total+b
    Count=Count+1
    a=input('Letter grades:')
else:
    print('Grade point average:',Total/(Count)) 
    



