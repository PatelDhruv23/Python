
#!WAP to check if a given number is positive or negative or zero

num = int(input('ENTER THE NUMBER: '))

if num > 0:
    print(f'{num} is Positive.')

elif num < 0:
    print(f'{num} is Negative.')

else:
    print(f'{num} is Zero.')