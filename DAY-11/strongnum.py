
#! WAP to check if a number is strong number or not

num = input("Enter Number: ")
sum = 0

for i in num:
    fact=1
    for j in range(int(i),0,-1):
        fact = fact * j
    
    sum = sum + fact

print(sum)
if sum == int(num) :
    print(f"{num} is Strong Number.")
else:
    print(f"{num} is not a Strong Number.")