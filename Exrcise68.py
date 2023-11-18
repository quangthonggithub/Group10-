from collections import Counter
a=input('Enter 8 bits:')
while Counter(a)['1']+Counter(a)['0']!=8 or len(a)!=8:
    a=input('Enter 8 bits:')
else:
    x=Counter(a)['1']
    if x%2==1:
        print('The parity bit should be 0.')
    else:
        print('The parity bit should be 1.')

        
 

    

