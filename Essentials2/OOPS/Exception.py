def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division Failed")
        return None
    else:
        print("Everything went fine")
        return n
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))

##########################
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
#############################
"""
Exception tree - to display all exceptions
"""
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("    |" * (nest - 1), end ="")
    if nest > 0:
        print("    +---", end="")
    
    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)
print_exception_tree(BaseException)
##############################################
"""
The BaseException class introduces a property named args. It's a tuple designed to gather all arguments passed to the class constructor. It is empty if the construct has been invoked without any arguments, or contains just one element when the constructor gets one argument (we don't count the self argument here), and so on.

We've prepared a simple function to print the args property in an elegant way
"""
def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))

try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep =' : ', end =' : ')
    print()
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end =' : ')
    print()
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep =' : ', end =' : ')
    print()
    print_args(e.args)

#########################################
"""
Own exception
"""
class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")

for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

##########################################
"""
own exception
PizzaError - Request wrong pizza
TooMuchCheeseError - too much cheese
"""
class PizzaError(Exception):
    def __init__(self, pizza = 'unknown', message =''):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza = 'unknown', cheese = '>100', message =''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such piza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print(f"Pizza ready! - {pizza}")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz,ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.pizza, '-', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
######################################################################
"""
Section summary
1. The else: branch of the try statement is executed when there has been no exception during the execution of the try: block.


2. The finally: branch of the try statement is always executed.


3. The syntax except Exception_Name as an exception_object: lets you intercept an object carrying information about a pending exception. The object's property named args (a tuple) stores all arguments passed to the object's constructor.


4. The exception classes can be extended to enrich them with new capabilities, or to adopt their traits to newly defined exceptions.


    try:
        assert __name__ == "__main__"
    except:
        print("fail", end=' ')
    else:
        print("success", end=' ')
    finally:
        print("done")

"""