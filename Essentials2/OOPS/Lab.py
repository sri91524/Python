"""
Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from the range [0..23] – we will be using military time), minutes (from the range [0..59]) and seconds (from the range [0..59]).
    Zero is the default value for all of the above parameters. There is no need to perform any validation checks.
The class itself should provide the following facilities:
    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
    the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside the objects by +1/-1 second respectively.
Use the following hints:
    all object properties should be private;
    consider writing a separate function (not method!) to format the time string
"""
class Timer:
    def __init__(self, hr = 0, min =0 , sec = 0):
        self.__hour = hr
        self.__minute = min
        self.__second = sec

    def next_second(self):
        self.__second += 1 
        if self.__second ==  60:
            self.__minute += 1
            self.__second = 0
            if self.__minute == 60:
                self.__hour += 1
                self.__minute = 0
                if self.__hour == 24:
                    self.__hour = 0       

    def prev_second(self):
        self.__second -= 1
        if self.__second < 0:
            self.__second = 59
            self.__minute -= 1            
            if self.__minute < 0:
                self.__minute = 59
                self.__hour -= 1            
                if self.__hour < 0:
                    self.__hour = 23 

    def __str__(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

###############################################################################
"""
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you - this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.
The class constructor accepts one argument - a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:
    Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:
    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
    the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
    all object's properties should be private;
"""
class WeekDayError(Exception):
    pass

class Weeker:
    dow = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.dow:
             raise WeekDayError("Sorry, I can't serve your request.")
        self._day = day

    def __str__(self):
        return self._day
    
    def add_days(self, n):
        self._totdays = self.dow.index(self._day) + n
        self._day = self.dow[self._totdays % 7]        
    
    def subtract_days(self, n):
        self._remdays = self.dow.index(self._day) - n
        self._day = self.dow[self._remdays % 7]          
          
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

#######################################################
# Efficient code
class WeekDayError(Exception):
    pass

class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

##########################################################
import math

class Point:
    def __init__(self, x =0.0, y = 0.0):
        self.__X = x
        self.__Y = y
    
    def getx(self):
        return self.__X
    
    def gety(self):
        return self.__Y
    
    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__X - x), abs(self.__Y - y))
        
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())
    
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

##########################################################################
"""
Lab - Triangle
The new class will be called Triangle and this is what we want:
the constructor accepts three arguments – all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)
"""
import math

class Point:
    def __init__(self, x= 0.0, y= 0.0):
        self._X = x
        self._Y = y
    
    def getx(self):
        return self._X
    
    def gety(self):
        return self._Y
    
    def distance_from_xy(self, x, y):
        return math.hypot(abs(self._X - x), abs(self._Y - y))
    
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i+1) % 3])
        return per
          
triangle = Triangle(Point(0,0), Point(1,0), Point(0,1))
print(f"Perimeter of triangle - {triangle.perimeter()}")

