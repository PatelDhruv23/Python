
#! WAP to check if the string is palindrome or not

chr = input("Enter String: ")

i=0
out=''

while i<len(chr):
    out = chr[i] + out
    i=i+1

if chr == out:
    print("PALINDROME.")

else:
    print("Not a PALINDROME ")