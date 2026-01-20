
#! WAP to print reverse the string using for loop

s = input("Enter the string: ")
rev = ''
rev2 = ''
for i in s:
    rev = i + rev
print(rev)

for j in range(0,len(s)):
    rev2 = s[j] + rev2
    
print(rev2)