#a=String Entered By User(Chuỗi Xuôi)
a=str(input('Enter string:'))
b=''
for i in a :
    b=i+b
if (a==b):
    print('It is Palindrome')
else:
    print('It is not Palindromes')

