
#! WAP to check if the given character is Vowel or Consonant

char = input('Enter an Alphabet Character: ')

if 'A'<= char <='Z' or 'a' <= char <= 'z':
    
    if char in 'AEIOUaeiou':
        print(f"'{char}' is a Vowel")
    
    else:
        print(f"'{char}' is a Consonant")

else:
    print(f"'{char}' is not an Alphabet")