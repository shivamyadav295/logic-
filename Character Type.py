#Input one character and identify whether it is a vowel, consonant, digit, or special character.
char=input("Enter a charactor:")
if len(char)!=1:
    print("enter only one digit!")
elif char in "aeiouAEIOU":
    print("its a vowel")
elif char.isalpha():
    print("consonent")
elif char.isdigit():
    print("digit")
else:
    print("special charactor")


