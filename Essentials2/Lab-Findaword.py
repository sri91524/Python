# Find a word
"""
are the characters comprising the first string hidden inside the second string?
For example:
    if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
    if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)
Hints:
    you should use the two-argument variants of the pos() functions inside your code;
    don't worry about case sensitivity.
"""

searchstr = input("Enter word you wish to search: ").lower().strip()
text = input("Enter the string you wish to search through: ").lower().strip()
found = True
start = 0

if not text and not searchstr:
    print("Invalid Input")
else:
    for ch in searchstr:
        pos = text.find(ch, start)
        if pos < 0:
            found = False
            break
        start = pos + 1 # to start from next position not on 0
if found:
    print("Yes")
else:
    print("No")


