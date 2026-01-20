
#! WAP to to check if the number is prime or not

n = int(input("Enter the number: "))
counter = 0

for i in range(2,n):
    if n % i == 0:
        counter += 1
        break

if counter == 0:
    print(f'{n} is a Prime Number')
else:
    print(f'{n} is not a Prime Number')
