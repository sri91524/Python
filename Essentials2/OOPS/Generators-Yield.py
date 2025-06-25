def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)
print("_____________________________")
#################################
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(8):
    print(v)
print("_____________________________")
#########################################
"""
List Comprehensions
"""
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *=2

t = [x for x in powers_of_2(5)]
print(t)
print("_____________________________")
########################################
"""
list()
"""
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *=2

t = list(powers_of_2(3))
print(t)
print("_____________________________")
#############################################
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for i in range(20):
    if i in powers_of_2(4):
        print(i)
print("_____________________________")
#############################################
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0,1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
print("_____________________________")
############################################
"""
List comprehension
"""
list_1 = []
for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]
print(list_1)
print(list_2)
##############################################
"""
conditional expression – a way of selecting one of two different values based on the result of a Boolean expression.

Look:
expression_one if condition else expression_two
"""
the_list = []

for x in range(10):
    the_list.append(str(x)+' even' if x % 2 == 0 else str(x)+' odd')

print(the_list)
print("_____________________________")

"""
List comprehension
"""
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)
##############################################
"""
List comprehensions Vs. generators
"""
the_list = [1 if x % 2  == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end = " ")
print()

for v in the_generator:
    print(v, end= " ")
print()

##############################################
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end = " ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end = " ")
print()
print("_____________________________")
##############################################
