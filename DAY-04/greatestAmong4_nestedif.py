
#! WAP to find greatest among Four numbers using Nested If

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
d = int(input("Enter Number 4: "))


if a>b:

    if b>c:
        if b>d:
            print(f'{b} is greatest')
        else:
            print(f'{d} is greatest')
    
    else:
        if c>d:
            print(f'{c} is greatest')
        else:
            print(f'{d} is greatest')

else:

    if a>c:
        if a>d:
            print(f'{a} is greatest')
        else:
            print(f'{d} is greatest')
    
    else:
        if c>d:
            print(f'{c} is greatest')
        else:
            print(f'{d} is greatest')


