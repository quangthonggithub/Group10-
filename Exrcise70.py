text = input("enter massage: ") 
k = int(input("enter shift amount: ")) 
result = ''
for i in range(len(text)):
    char = text[i]
    if "A"<=char<="Z":
        result = result + chr((ord(char) -65 +k) % 26 + 65) 
    elif 97<=ord(char)<=122: 
        result = result + chr((ord(char) - 97 +k) % 26 + 97)
    else:
        result = result + char
print(result)