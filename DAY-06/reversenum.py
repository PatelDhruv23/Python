#WAP to print the reverse of any number

num = int(input("Enter the number: "))
org_num = num
rev = 0

while num > 0:
    ld = num % 10 #Extract
    rev = (rev * 10) + ld #Store
    num = num // 10 #Remove/Update

print(f'{rev} is the Reversed order of number {org_num}')
