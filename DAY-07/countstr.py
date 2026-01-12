
#! WAP to count the types of characters

char = input("Enter a String: ")

upper=0
lower=0
digit=0
special=0

i=0
while i < len(char):

    if 'A' <= char[i] <= 'Z':
        upper = upper + 1
    elif 'a' <= char[i] <= 'z':
        lower = lower + 1
    elif '0' <= char[i] <= '9':
        digit = digit + 1
    else:
        special = special + 1
    
    i=i+1


print(f'Upper: {upper}')
print(f'Lower: {lower}')
print(f'Digit: {digit}')
print(f'Special: {special}')
