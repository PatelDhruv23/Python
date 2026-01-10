
#! WAP to check if the given number is perfect number or not

# If Addition of its factors/divisors equals to the number then it is said to be perfect number

# If the SUM of divisors of a number is equal to the original number then it is said to be perfect number
# eg: 6,28

num = int(input("Enter the Number: "))

sum=0
i=1
while i < num:

    if (num % i == 0):
        sum = sum + i
    i+=1

if num == sum:
    print(f'{num} is a PERFECT NUMBER')
else:
    print(f'{num} not a PERFECT NUMBER')