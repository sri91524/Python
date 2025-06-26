"""
 A method is a function embedded inside a class. The first (or only) parameter of each method is usually named self, which is designed to identify the object for which the method is invoked in order to access the object's properties or invoke its methods.
2. If a class contains a constructor (a method named __init__) it cannot return any value and cannot be invoked directly.
3. All classes (but not objects) contain a property named __name__, which stores the name of the class. Additionally, a property named __module__ stores the name of the module in which the class has been declared, while the property named __bases__ is a tuple containing a class's superclasses.
"""

# self
class Classy:
    def method(self):
        print("method")
    
obj = Classy()
obj.method()
############################################
# self and parameter
class Classy:
    def method(self, par):
        print("method:", par)
    
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)
#########################################
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3
obj.method()
########################################
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()
########################################
class Classy:
    def __init__(self, value):
        self.var = value

obj_1 = Classy("object")
print(obj_1.var)
###########################################
class Classy:
    def __init__(self, value = None):
        self.var = value

obj_1 = Classy("object1")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)
############################################
"""
In Python, name mangling refers to a mechanism that alters the names of class attributes that start with two underscores (__) but do not end with two underscores.
"""
class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")

obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden() # (accessing the mangled name)
########################################
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2
    
    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()
print(obj.__dict__)
print(Classy.__dict__)
########################################
"""
__name__ -- The property contains the name of the class
 the __name__ attribute is absent from the object – it exists only inside classes
"""
class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)
# print(obj.__name__)
##########################################
"""
__module__ is a string, too, it stores the name of the module which contains the definition of the class.
"""
class Classy:
    pass

print(Classy.__module__)
obj = Classy()
print(obj.__module__)
##########################################
"""
__bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.
"""
class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('(', end ='')

    for x in cls.__bases__:
        print(x.__name__, end = ' ')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)