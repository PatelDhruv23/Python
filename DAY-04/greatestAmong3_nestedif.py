
#! WAP to find greatest among Three numbers using Nested If

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

if a != b or b != c:
    if a > b:
        if b > c:
            print(f'{b} is greater than {a} and {c}')
        else:
            print(f'{c} is greater than {a} and {b}')

    else:
        if b > c:
            print(f'{b} is greater than {a} and {c}')
        else:
            print(f'{c} is greater than {a} and {b}')

else:
    print("All the three numbers are same i.e {a}, {b}, {c}")