"""
1. A stack is an object designed to store data using the LIFO model. The stack usually performs at least two operations, named push() and pop().


2. Implementing the stack in a procedural model raises several problems which can be solved by the techniques offered by OOP (Object Oriented Programming).


3. A class method is actually a function declared inside the class and able to access all the class's components.


4. The part of the Python class responsible for creating new objects is called the constructor, and it's implemented as a method of the name __init__.


5. Each class method declaration must contain at least one parameter (always the first one) usually referred to as self, and is used by the objects to identify themselves.


6. If we want to hide any of a class's components from the outside world, we should start its name with __. Such components are called private.
"""

# *********self parameter-  It allows the method to access entities (properties and activities/methods) carried out by the actual object. You cannot omit it. Every time Python invokes a method, it implicitly sends the current object as the first argument.

# Defining class and constructor

class Stack: # Defining the Stack class
    def __init__(self): # Defining constructor function
        print("Hi!")

stack_object = Stack() # instantiating the object

########################################################
# Defining object properties
class Stack:
    def __init__(self):
        self.stack_list = []

stack_object = Stack()
print(len(stack_object.stack_list))

###########################################################
# Access Modifiers - private (Achieving encapsulation)
# class Stack:
#     def __init__(self):
#         self.__stack_list = []

# stack_object = Stack()
# print(len(stack_object.__stack_list))  # private property __ cannot be accessed outside of class (AttributeError)
#################################################
# Push and Pop methods (public)
# Python expect one parameter for methods always as it passes object
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
###########################################
# 2 stack object
class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object_1 = Stack()
stack_object_2 = Stack()
stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())
###########################################
"""
created three objects of the class Stack. Next, we've juggled them up.
"""
class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() -2)
print(funny_stack.pop())

#######################################################
# Subclass and super class
# calculate sum
class Stack:
    def __init__(self):
        self.stack_list = []
    
    def push(self, val):
        self.stack_list.append(val)
    
    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)    # Mandatory to invoke superclass constructor in python
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum
    
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(f"sum: {stack_object.get_sum()}")

for i in range(5):
    print(stack_object.pop())



