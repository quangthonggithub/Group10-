#a=String Entered By User(Chuỗi Xuôi)
a=str(input('Enter string:'))
b=''
while ' ' in a:
    a=a.replace(' ','')
for i in a :
    while True:
        if i==(' '):
            b=b
        break
    b=i+b
if (a==b):
    print('It is Palindrome')
else:
    print('It is not Palindromes')

