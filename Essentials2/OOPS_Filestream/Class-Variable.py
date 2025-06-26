"""
1. An instance variable is a property whose existence depends on the creation of an object. Every object can have a different set of instance variables.

Moreover, they can be freely added to and removed from objects during their lifetime. All object instance variables are stored inside a dedicated dictionary named __dict__, contained in every object separately.


2. An instance variable can be private when its name starts with __, but don't forget that such a property is still accessible from outside the class using a mangled name constructed as _ClassName__PrivatePropertyName.


3. A class variable is a property which exists in exactly one copy, and doesn't need any created object to be accessible. Such variables are not shown as __dict__ content.

All a class's class variables are stored inside a dedicated dictionary named __dict__, contained in every class separately.


4. A function named hasattr() can be used to determine if any object/class contains a specified property.
"""
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
    
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

###################################################
# Private variable
class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
#####################################################
# the difference between these two __dict__ variables
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val
    
print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)
############################################
# may not expect that all objects of the same class have the same sets of properties
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)
print(example_object.a)
try:
    print(example_object.b)
except AttributeError:
    pass
##########################################
# hasattr
class ExampleClass:
    def __init__(self, val):
        if val % 2 !=0:
            self.a = 1
        else:
            self.b =1

example_object = ExampleClass(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)
############################################
class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))
###########################################
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

example_object = ExampleClass()
print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))


