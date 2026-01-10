
#! WAP to check if the number is palindrome or not

num = int(input("Enter the number: "))
org_num = num
rev = 0

while num > 0:
    ld = num % 10 #Extract
    rev = (rev * 10) + ld #Store
    num = num // 10 #Remove/Update

if org_num == rev:
    print(f'{org_num} is a palindrome number i.e {rev}')

else:
    print(f'{org_num} is not a palindrome number')

