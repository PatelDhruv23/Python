
#! WAP to find Factorial of given Number.
num = int(input("ENTER A NUMBER: "))

i = num
fact = 1

while (i >= 1):

    fact = fact * i
    i=i-1

print(f'Factorial of {num} is: {fact}')