"""
A lambda function is a function without a name (you can also call it an anonymous function)
"""
two = lambda:2
sqr = lambda x: x*x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end =" ")
    print(pwr(a, two()))

#############################################
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep ='')

def poly(x):
    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2,3)], poly)
##############################################
"""
The print_function() has remained exactly the same, but there is no poly() function. We don't need it anymore, as the polynomial is now directly inside the print_function() invocation in the form of a lambda defined in the following way:
lambda x: 2 * x**2 - 4 * x + 2
"""
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')

print_function([x for x in range(-2,3)], lambda x: 2 * x**2 - 4 * x + 2)
#############################################
"""
Lambdas and the map function
map(function, list)
"""
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end =' ')
print()

##############################################
"""
Lambdas and the filter
"""
from random import seed, randint
seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)

##################################################################
# Write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console.

any_list = [1, 2, 3, 4]
even_list = list(map(lambda x : x |1, any_list))
print(even_list)