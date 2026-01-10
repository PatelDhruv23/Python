
#! WAP to check if the string is palindrome or not

str = input("Enter String: ")

out=''
i=0
while i<len(str):
    out = str[i] + out
    i=i+1

if str == out:
    print(f'{str} is a PALINDROME String i.e {out}')

else:
    print(f'{str} is not a PALINDROME String i.e {out}')