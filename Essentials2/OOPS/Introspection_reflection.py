class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
###########################################
"""
Quiz
"""
class Snake:
    def __init__(self, val):
        self.victims = val

    def increment(self):
        self.victims +=1

obj = Snake(5)
print(obj.victims)

############################
class Snake:
    pass
 
class Python(Snake):
    pass 
 
print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be', Python.__name__)