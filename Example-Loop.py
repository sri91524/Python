# largest_number = -999999999

# number = int(input("Enter a number or type -1 to stop: "))

# while(number != -1):
#         if(number > largest_number):
#                 largest_number = number
        
#         number = int(input("Enter a number or type -1 to stop: "))

# print(f"Largest number is {largest_number}")

#=============================================================
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# number = int(input("Enter a number or 0 to stop: "))

# while(number != 0):
#     if(number % 2 == 0):
#         even_numbers += 1
#     else:
#         odd_numbers += 1
#     number = int(input("Enter a number or 0 to stop: "))

# print(f"Odd numbers count: {odd_numbers}")
# print(f"Even numbers count: {even_numbers}")

# Using a counter variable to exit a loop
# counter = 5
# while counter:
#     print("Inside the loop", counter)
#     counter += -1

# print("Outside the loop", counter)

"""
will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
"""

# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# number = int(input("Guess a number: "))

# while number != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     number = int(input("Guess a number: "))

# print(f"You guessed correct number {number}")
# print("Well done, muggle! You are free now.")

#==================================================
# 0-9
# for i in range(10):
#     print("The value of i is currently", i)

# # 2-7
# for i in range(2, 8):
#     print("The value of i is currently", i)
# # 2- 7, step 3
# for i in range(2, 8, 3):
#     print("The value of i is currently", i)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2

""" 
for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
"""
# import time

# for i in range(1,6):
#     print(f"{i} Mississippi")
#     time.sleep(1)

# print("Ready or not, here I come!")

#===========================================================
# print("The break instruction:")
# for i in range(1,6):
#     if(i==3):
#         break
#     print("Inside the loop", i)
# print("Outside the loop")
#===========================================================
# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if(i==3):
#         continue
#     print("Inside the loop", i)
# print("Outside the loop")
#============================================================
"""
Find largest number with break stt
"""
# largest_number = -999999999
# counter = 0
# while True:
#     number = int(input("Enter a number:"))
#     if number == -1:
#         break
#     counter +=1
#     if(number > largest_number):
#         largest_number = number
# if counter > 0:
#     print("Largest number is", largest_number)
# else:
#     print("You haven't entered any number")

#====================================================
# """
# Find largest number with continue stt
# """
# largest_number = -999999999
# counter = 0
# number = int(input("Enter a number: "))
# while number != -1:
#     if number == -1:
#         print("Continue stt called")
#         continue
#     counter +=1
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number (loop): "))

# if counter > 0:
#     print("Largest number  is: ", largest_number)
# else:
#     print("You haven't entered any number")

#============================================================
# """
# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
# """
# word = input("Enter secret word: ")
# while True:
#     if(word == "chupacabra"):
#         break
#     word = input("Enter secret word: ")

# print("You've successfully left the loop.")
#=============================================================\
"""
# Your task here is very special: you must design a vowel eater! Write a program that uses:

# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:

# ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.
# """
# user_word = input("Enter a word: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'O':
#         continue
#     elif letter == 'U':
#         continue
#     else:
#         print(letter)
#=======================================================
"""
ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
"""
# user_word = input("Enter a word: ")
# user_word = user_word.upper()
# word_without_vowels = ""

# for letter in user_word:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'O':
#         continue
#     elif letter == 'U':
#         continue
#     else:
#         word_without_vowels += letter
# print(word_without_vowels)

#=============================================
# i = 1
# while i < 5:
#     print(i)
#     i +=1
# else:
#     print("else:", i)

# i = 5
# while i < 5:
#     print(i)
#     i +=1
# else:
#     print("else:", i)

#=============================================
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

# i = 111
# for i in range(2,1):
#     print(i)
# else:
#     print(i)

#=========================================
"""
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
"""
# total_blocks = int(input("Enter number of blocks: "))
# layer = 1
# blocks = 1
# height = 0
# while blocks <= total_blocks:
#     layer += 1
#     blocks += layer
#     height +=1

# print(f"The height of the pyramid: {height}")

#================================
"""
In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
"""
# c0 = int(input("Enter a number greater than 0: "))
# steps = 0
# if c0 > 0:
#     while c0 != 1:
#         if c0 % 2 == 0:
#             c0 = c0/2
#         else:
#             c0 = 3 * c0 + 1
#         steps += 1
#         print(int(c0))
# print("Steps: ", steps)
#=====================================================
"""
Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
"""
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)

"""
Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
"""
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

"""
Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:
"""
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end ="")

"""
Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:
"""
for digit in "0165031806510":
    if digit == "0":
        print("x", end ="")
        continue
    print(digit, end ="")

       




