
#! WAP to check is the number is perfect number or not

n = int(input("Enter Number: "))

sum = 1

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if n == sum:
    print(f"{n} is Perfect Number")
else:
    print(f"{n} is not a Perfect Number")
