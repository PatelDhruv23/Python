
#! WAP to print the reversed string only if the string is starting with vowel and ending with consonanat along with it should have a middle value

char = input("Enter String (ODD length): ")

if len(char) % 2 != 0:

    if char[0] in 'AEIOUaeiou' and char[-1] not in 'AEIOUaeiou':
        print(f'Reversed string: {char[::-1]}')
    
    else:
        print(f'Either string not staring with VOWEL or not ending with CONSONANT')
    
else:
    print(f'Length of String is EVEN')