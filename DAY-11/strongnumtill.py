
#!WAP to print Strong Numbers upto n

start = int(input("Enter Start Number: "))
end = int(input("Enter End Number: "))
sum = 0
out=[]
for i in range(start,end+1):
    
    for j in str(i):
        fact=1
        for k in range(1,int(j)+1):
            fact = fact * k
        sum = sum + fact

    if sum == i:
        out.append(i)
    sum = 0    

print(f"Strong Numbers in between {start} and {end} are: {out}")


        

