# Anagrams
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# Note:
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check – treat them as non-existent

text1 = input("Enter text1 : ").strip()
text2 = input("Enter text2 : ").strip()

if not text1 and not text2:
    print("Entered text are not anagrams")
else:
    if ''.join(sorted(text1.replace(' ','').lower())) != ''.join(sorted(text2.replace(' ','').lower())):
        print(text1," and ", text2, " are not anagrams")
    else:
        print(text1," and ", text2, " are anagrams")
