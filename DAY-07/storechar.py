
char = input("Enter a String: ")

upper=[]
lower=[]
digit=[]
special=[]

i=0
while i < len(char):

    if 'A' <= char[i] <= 'Z':
        upper.append(char[i])
    elif 'a' <= char[i] <= 'z':
        lower.append(char[i])
    elif '0' <= char[i] <= '9':
        digit.append(char[i])
    else:
        special.append(char[i])
    
    i=i+1

print(f'Upper: {upper}')
print(f'Lower: {lower}')
print(f'Digit: {digit}')
print(f'Special: {special}')