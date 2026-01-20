
#! 1. WAP to print the characters present at odd index from a string.

#! 2. WAP input = 'HoLIdaY'
#!       output = 'hOliDAy'
  
#! 3. WAP to extract the lowercase characters frpm the string only if ascii value is even

#! 4. WAP to replace space by * in the string


""" #? 1st
s = input("Enter the String: ")
outs = ''
for i in range(1,len(s),2):
        outs = outs + s[i]

print(f"'{outs}' is the desired string with odd index characters only.")

print("------------------------------------------------------------------------")

#? 2nd
input = 'HoLIdaY'
output = ''

for i in input:
    if i.isupper():
        output = output + i.lower()
    else:
        output = output + i.upper()

print(input)
print(output)  

print("------------------------------------------------------------------------") """

#? 3rd
st = input("Enter the string: ")
out = ''

for j in st:
    if 'a'<= j <= 'z':
        if ord(j) % 2 == 0:
             out = out + j

print(out)

print("------------------------------------------------------------------------")

#? 4th
string = input("Enter the String with space: ")
out2 = ''

for i in string:
    if i == ' ':
        out2 = out2 + '*'
    else:
        out2 = out2 + i

print(out2)