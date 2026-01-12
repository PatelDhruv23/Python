
#! WAP to find sum of digits of a number eg: 145 -> 1+4+5 = 10

num = int(input('Enter Number: '))
org_num = num

ld = 0
sum = 0

while num > 0:
    ld = num % 10
    sum = sum + ld
    num = num // 10

print(f'Sum of the digits of {org_num} is : {sum}')