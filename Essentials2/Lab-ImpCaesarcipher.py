# Improving Casearcipher
"""
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
"""
try:
    text = input("Enter your message: ")
    flag = True
    while flag:
        shift = int(input("Enter shift value in the range of 1-25: "))
        if 1 <= shift <= 25:
            flag = False
        else:
            print("Invalid Input. Enter number range from 1-25")

    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            code = ord(char)
            code = code + shift
            if char.islower() and code > ord("z"):
                code = ord("a") + (code - ord("z") - 1)               
            elif char.isupper() and code > ord("Z") :
                code = ord("A") + (code - ord("Z")- 1)                
            cipher += chr(code)
            # print("code-", code)
    print(cipher)          
       
except ValueError:
    print("Invalid input. Please enter a valid integer")