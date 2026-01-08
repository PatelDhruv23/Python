
#! WAP to accept a number if num is div by 3 and 5 print "FizzBuzz".
#! If divisible by 3 -> "Fizz"
#! If divisible by 5 -> "Buzz"

num = int(input('Enter the number: '))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print(f'{num} is not a valid input.')