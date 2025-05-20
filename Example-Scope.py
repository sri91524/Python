# variable outside function
var = 2
def mult_by_var(x):
    return x * var

print(mult_by_var(7))

#####################################
# variable inside function
def mult(x):
    var = 5
    return x * var

print(mult(7))

######################################
# Outside variable replaced within function
def mult(x):
    var = 7
    return x* var

var = 3
print(mult(7))

######################################
# A variable that exists inside a function has scope inside the function body
def adding(x):
    var = 7
    return x + var

print(adding(4))
print(var) # NameError
####################################
# You can use the global keyword followed by a variable name to make the variable's scope global
var = 2
print(var)

def return_var():
    global var
    var = 5
    return var

print(return_var())
print(var)

########################################
# To calculate ft and inch to meter
# feet and inches: 1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

# To calculate pound to kg
# 1 lb = 0.45359237 kg
def lb_to_kg(lb):
    return lb * 0.4535923

# To calculate BMI (kg, m^2)
def bmi(weight, height):
    if (height < 1.0 or height > 2.5 or weight < 20 or weight > 200) :
        return None
    
    return weight / height ** 2

print(bmi(lb_to_kg(176), ft_and_inch_to_m(5, 7)))
#######################################
# to test if it forms a triange
# sum of two arbitrary sides has to be longer than the third side.
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
  
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))
########################################
# Is a right triangle
"""
certain triangle is a right-angle triangle.
We will need to make use of the Pythagorean theorem:
c2 = a2 + b2

How do we recognize which of the three sides is the hypotenuse?
The hypotenuse is the longest side.
"""
def is_a_right_triangle(a, b, c):
    if not is_a_triangle:
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(5, 13, 12))
# print(is_a_right_triangle(1, 3, 12))

########################################
# Area of a triangle
# s = (a + b + c)/2
# A = s(s-a)(s-b)(s-c) ** 0.5

def heron(a, b, c):
    p = (a + b + c)/2
    return (p * (p-a) * (p-b) * (p-c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_triangle(1., 1., 2. ** 0.5))

#######################################
# Factorial function
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6):
    print(n, factorial_function(n))

###########################################
# Fibonacci numbers
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     a = b = 1
#     sum = 0
#     for i in range(3, n+1):
#         sum = a + b
#         a, b = b, sum
#     return sum


###########################################
# Using Recursion - Fibonacci numbers
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

for n in range(1, 10):
    print(n, fib(n))

# Using Recursion - Factorial
def fact(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n* fact(n -1) 
