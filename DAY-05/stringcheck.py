
#! WAP to print the midddle charcter of the string only if the character is UPPERCASE

char = input("Enter String (odd length): ")

if len(char) % 2 != 0:
    length = len(char)//2
    if 'A' <= char[length] <= 'Z':
        print(f"Middle Character of '{char}' is UPPERCASE Character i.e '{char[length]}'")
    else:
        print(f"Middle Character of '{char}' is LOWERCASE Character i.e '{char[length]}'")

else:
    print(f"length of '{char}' is EVEN")