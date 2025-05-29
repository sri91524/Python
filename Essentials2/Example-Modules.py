import math

def sin(x):
    if 2 * x == pi:
        return 0.9999999
    else:
        return None

pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))

# ##################################
from math import sin, pi
print(sin(pi/2))
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

# ################################
import math as m
print(m.sin(m.pi/2))

from math import sin as sine, pi as PI
print(sine(PI/2))

# ################################
from math import *

import math
for name in dir(math):
    print(name, end ="\t")
#####################################
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi/2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

from math import e, exp, log

print(pow(e,1) == exp(log(e)))
print(pow(2,2) == exp(2* log(2)))
print(log(e, e) == exp(0))  

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

###############################################
from random import random

# for i in range(5):
#     print(random())

from random import random, seed
seed(0)
for i in range(5):
    print(random())

########################################
# The randrange and randint functions
# randrange(end)
# randrange(beg, end)
# randrange(beg, end, step)
# randint(left, right) 
# randint(left, right)  === randrange(beg, end + 1)

from random import randrange, randint

print(randrange(1), end = ' ')
print(randrange(0, 1), end =' ')
print(randrange(0, 1, 1), end =' ')
print(randint(0, 1))

from random import randint
for i in range(10):
    print(randint(1, 10), end = ',')

#######################################
# choice(sequence)
# sample(sequence, elements_to_choose)
from random import choice, sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

####################################################
# to import a module, add to path abolute or relative path of module and import and access it

from sys import path

path.append("C:\\Users\\hari_\\OneDrive\\Desktop\\Learning\\Python-Projects\\Essentials2\\Test")
print(path)
import module

import os
print(os.listdir("C:\\Users\\hari_\\OneDrive\\Desktop\\Learning\\Python-Projects\\Essentials2\\Test"))
 
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.sum1(zeroes))
print(module.prod1(ones))