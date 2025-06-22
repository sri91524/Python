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