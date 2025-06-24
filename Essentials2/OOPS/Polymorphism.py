class One:
    def do_it(self):
        print("do it from One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do it from Two")

one = One()
two = Two()
one.doanything()
two.doanything()

##############################################
"""
above functionality achieved using Inheritance
"""
import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)

class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)

########################################
"""
Composition example
inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;

composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.
"""
import time
class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)
    
class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller
    
    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())
wheeled.turn(True)
tracked.turn(False)
