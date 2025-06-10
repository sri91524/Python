def bad_fun(n):
    return 1 / n
 
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

########################################################
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
    
##########################################################
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

##############################################
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

###############################################
# The code shows an extravagant way
# of leaving the loop.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')

###########################################
# This code cannot be terminated
# by pressing Ctrl-C.

# from time import sleep

# seconds = 0

# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Don't do that!")

##################################################
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!
 
# string = 'x'
# try:
#     while True:
#         string = string + string
#         print(len(string))
# except MemoryError:
#     print('This is not funny!')
##############################################
# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...
# OverflowError
from math import exp
 
ex = 1
 
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

#################################################
# One of these imports will fail – which one?
 
try:
    import math
    import time
    import abracadabra
 
except:
    print('One of your imports has failed.')

################################################
# How to abuse the dictionary
# and how to deal with it?
# a concrete exception raised when you try to access a non-existent element in a collection
 
dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
 
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)


    