
#! WAP to check smallest among the three numbers

a = int(input('Enter Number A:'))
b = int(input('Enter Number B:'))
c = int(input('Enter Number C:'))

if a==b and b==c:
    print(f'All the values are same i.e {a} {b} {c}')

elif a<b and a<c:
    print(f'{a} is smaller than {b} and {c}')

elif b<c:
    print(f'{b} is smaller than {a} and {c}')

else:
    print(f'{c} is smaller than {a} and {b}')
   