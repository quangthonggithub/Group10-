import math
x = float(input("Nhập một số để tính căn bậc hai: "))
epsilon=1e-12
guess=x/2
while abs(guess * guess - x) > epsilon :
    guess=(guess+x/guess)/2
print('Guess is not good enough do:',guess) #Chưa đủ tốt
while abs(guess * guess - x) < epsilon :
    guess=(guess+x/guess)/2
print('The quality of the approximation depends on','The square root of a number:',guess) #Đủ tốt
    
    
     
    

