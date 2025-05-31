char_1 = 'a'
char_2 = ' '
print(ord(char_1))
print(ord(char_2))
print(chr(97))
print(chr(945))
print(chr(ord('x')) == 'x')
print(ord('x'))

#Indexing strings
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()
print(the_string[-2])

alpha = "welcome"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:7]) 
print(alpha[::2])
print(alpha[1::2]) # step  2

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("m" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

print("f" not in alphabet)
print("F" not in alphabet)

# strings are immutable
alphabet = "bcdefghijklmnopqrstuvwxy"
# del alphabet[0] #TypeError: 'str' object doesn't support item deletion
# del alphabet # can delete entire string

# alphabet.append("A") #AttributeError: 'str' object has no attribute 'append'
# alphabet.insert(0, "A") #AttributeError: 'str' object has no attribute 'insert'

# possible to concatenate string
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)

print(min("aAbByYzZ"))
t= 'The Knights Who Say "Ni!"'
print('[' + min(t) +']')
t=[0, 1, 2]
print(min(t))

print(max("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
t=[0,1,2]
print(max(t))

print("aAbByYzZaA".index("b"))

print(list("abcabc"))
print("abcabc".count("b"))
print("abcabc".count("d"))

#*********************************** String Methods *************************************
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6,'*') + ']')

if "epsilon".endswith("on") :
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

print("Eta".find("ta"))
print("Eta".find("mma"))
print("kappa".find('a', 2))

# The second argument specifies the index at which the search will be started

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = the_text.find("the")
while fnd != -1:
    print(fnd)
    fnd = the_text.find("the", fnd + 1)

# the third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4)) #start index, end index (not included)

# Demonstrating the isalnum() method:
# digits or alphabetical characters
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())
print("Moooo".isalpha())
print('Mu40'.isalpha())

print('2018'.isdigit())
print("Year2019".isdigit())

print("Moooo".islower())
print('moooo'.islower())

# Example: Demonstrating the isspace() method:
print(' \n'.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
print("-".join(["omicron", "pi", "rho"])) # seperator.join(list of strings)
print(" ".join(["welcome", "world"])) 

print("SiGmA=60".lower())

print("[" +" tau ".lstrip()+ "]") # remove leading white space
print("www.cisco.com".lstrip("w.")) #removes all characters enlisted in its argument (a string)
print("pythoninstitute.org".lstrip(".org"))

# # Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice",""))
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2)) #the third argument (a number) to limit the number of replacements

# Demonstrating the rfind() method: search from end
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 7)) # starting position 
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 11)) # start and end position

# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demonstrating the split() method:
print("phi       chi\npsi".split())
# print("ken,john".split(","))

# # Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print("[" +" Hari ".strip() + "]")

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

# Demonstrating the title() method:
#  it changes every word's first letter to upper-case, turning all other ones to lower-case.
print("I kNow thAt I know nothing. Part 1.".title())

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

"""
 Some of the methods offered by strings are:

capitalize() – changes all string letters to capitals;
center() – centers the string inside the field of a known length;
count() – counts the occurrences of a given character;
join() – joins all items of a tuple/list into one string;
lower() – converts all the string's letters into lower-case letters;
lstrip() – removes the white characters from the beginning of the string;
replace() – replaces a given substring with another;
rfind() – finds a substring starting from the end of the string;
rstrip() – removes the trailing white spaces from the end of the string;
split() – splits the string into a substring using a given delimiter;
strip() – removes the leading and trailing white spaces;
swapcase() – swaps the letters' cases (lower to upper and vice versa)
title() – makes the first letter in each word upper-case;
upper() – converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

endswith() – does the string end with a given substring?
isalnum() – does the string consist only of letters and digits?
isalpha() – does the string consist only of letters?
islower() – does the string consists only of lower-case letters?
isspace() – does the string consists only of white spaces?
isupper() – does the string consists only of upper-case letters?
startswith() – does the string begin with a given substring?
"""