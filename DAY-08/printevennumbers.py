
#! WAP to print even numbers upto n

n = int(input("Enter number: "))

for i in range(2,n+1,2):
    print(i)

for i in range(1,n+1):
    if i%2 == 0:
        print(i)