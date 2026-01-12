
char = input("Enter a String: ")

upper=''
lower=''
digit=''
special=''

i=0
while i < len(char):

    if 'A' <= char[i] <= 'Z':
        upper = upper + char[i]
    elif 'a' <= char[i] <= 'z':
        lower = lower + char[i]
    elif '0' <= char[i] <= '9':
        digit = digit + char[i]
    else:
        special = special + char[i]
    
    i=i+1


output = str(lower + upper + digit + special)
print(f"Output: '{output}' ")
