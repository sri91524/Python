# Palindrome
"""
asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent;
there are more than a few correct solutions – try to find more than one.
"""
text = input("Enter text : ").strip()
if not text:
    print("Entered text is not a Palindrome")
else:
    ltext = list(text.lower().replace(' ',''))  
    is_Palindrome = True
    
    for i in range(len(ltext)//2):
        if ltext[i] != ltext[-(i+1)]:
            is_Palindrome = False
            break

    if is_Palindrome:
        print(text, " is a Palidrome")
    else:
        print(text, " is not a Palindrome")