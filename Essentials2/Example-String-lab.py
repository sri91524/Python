"""
*****************Lab 1 split method creation***********************
Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

it should accept exactly one argument – a string;
it should return a list of words created from the string, divided in the places where the string contains whitespaces;
if the string is empty, the function should return an empty list;
its name should be mysplit()
"""
def mysplit(strng):
    result = []
    word = ""
    if strng.isspace() or strng == "":
        return result
    else:
        for ch in strng.strip():
            if not ch.isspace():
                word = word + ch
            else:
                # it appends word to list if there is space but for lastword, there will not be space after it
                if word:
                    result.append(word)
                    word = ""
        # to add last word 
        if word:
            result.append(word)
        return result


# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

################################################################

# Python offers two different ways to sort lists.
# The first is implemented as a function named sorted().
# returns a new list

# # Demonstrating the sorted() function:
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)
# print(first_greek_2)

# # no new list is created. Ordering is performed in situ by the method named sort()
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)

# second_greek.sort()
# print(second_greek)
###########################################################
# int to str
# itg = 13
# flt = 1.3
# si = str(itg)
# sf = str(flt)

# print(si + ' ' + sf)
###########################################################
# str to int / float
# if not valid number, ValueError exception
# si = '13'
# sf = '1.3'
# itg = int(si)
# flt = float(sf)

# print(itg + flt)

"""
Summary:
1. Strings can be compared to other strings using general comparison operators, but comparing them to numbers gives no reasonable result, because no string can be equal to any number. For example:

string == number is always False;
string != number is always True;
string >= number always raises an exception.
2. Sorting lists of strings can be done by:

a function named sorted(), creating a new, sorted list;
a method named sort(), which sorts the list in situ
3. A number can be converted to a string using the str() function.

4. A string can be converted to a number (although not every string) using either the int() or float() function. The conversion fails if a string doesn't contain a valid number image (an exception is raised then).
"""

# s1 = 'Where are the snows of yesteryear?'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3)
# print(s3[1])

# s1 = '12.8'
# i = int(s1) # ValueError exception
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)

"""
**************Lab 2 -  LED Display project************

program which is able to simulate the work of a seven-display device
Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

Test Data
Sample input:

123

Sample output:

# ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

 --0--
|     |
5     1
|     |
 --6--
|     |
4     2
|     |
 --3--
"""

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

def print_number(num):  
    lines = [""] * 5 # 5 rows for display
    for i in str(num):
        seg = digits[int(i)]
        lines[0] += " " + ("---" if seg[0] == "1" else "   ") + " "   
        lines[1] += ("|" if seg[5] == "1" else " ") + "   " + ("|" if seg[1] == "1" else " ")
        lines[2] += " " + ("---" if seg[6] == "1" else "   ") + " "
        lines[3] += ("|" if seg[4] == "1" else " ") + "   " + ("|" if seg[2] == "1" else " ")
        lines[4] += " " + ("---" if seg[3] == "1" else "   ") + " "

    for line in lines:
        print(line)

number = input("Enter the number you wish to display: ")
if number.isdigit():
    print_number(int(number))
else:
    print("Invalid input. Please enter a non negative integer")
    