class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    
    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun = Star("Sun", "Milky Way")
print(sun)

#############################################
"""
To find subclass
"""
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(f"Issubclass - {cls1} and {cls2} - {issubclass(cls1, cls2)}", end="\n")
    print()
    print()

#####################################################################################
"""
isinstance - to find object is instance of class
"""
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

vehicle = Vehicle()
land_vehicle = LandVehicle()
tracked_vehicle = TrackedVehicle()

for obj in [vehicle, land_vehicle, tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(f"Isinstance - {obj} and {cls} - {isinstance(obj, cls)}", end="\n")
    print()
    print()

#############################################
"""
isOperator
"""
class SampleClass:
    def __init__(self, val):
        self.val = val
    
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
print(object_1.val, object_2.val, object_3.val)
object_3.val += 1
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
############################################
class Super:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "My name is " + self.name

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Andy")
print(obj)

#######################################
"""
In the last example, we explicitly named the superclass. In this example, we make use of the super() function, which accesses the superclass without needing to know its name

In the last example, we explicitly named the superclass. In this example, we make use of the super() function, which accesses the superclass without needing to know its name
"""
class Super:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "My name is " + self.name

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Super("Andy")
print(obj)

################################################################
"""
Class variables
"""
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()
print(obj.subVar)
print(obj.supVar)
#########################################
"""
Instance Variable
"""
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()
print(obj.subVar)
print(obj.supVar)
##########################################3
"""
3 level inheritance
"""    
class Level1:
    vaiable_1 = 100
    def __init__(self):
        self.var_1 = 101
    
    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202
    
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302

obj = Level3()
print(obj.vaiable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
##############################################
"""
Multiple Inheritance
"""
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
    
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
    
class Sub(SuperA, SuperB):
    pass

obj = Sub()
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())
#######################################
"""
Overriding
"""
class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())
####################################
"""
Python looks for object components in the following order:

inside the object itself;
in its superclasses, from bottom to top;
if there is more than one class on a particular inheritance path, Python scans them from left to right.
"""
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right ="RR"
    def fun(self):
        return "Right"

# class Sub(Left, Right):
#     pass
class Sub(Right, Left):
    pass

obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())
