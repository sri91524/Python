var = 1
account_balance = 1000.0
client_name = 'John Doe'
var = var + 1
print(var, account_balance, client_name)

"""
var = '3.13.3'
print('Python Version: '+ var)
"""
# Pythagorean theorem
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print(c)

#calculate sum

john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=",", end=" ")
print("Welcome")
total_apples = john + mary + adam
print("Total number of apples: ", total_apples)

""" 
# miles to kilometers conversion and vice versa
# Expected -- 7.38 miles is 11.88 kilometers
              12.25 kilometers is 7.61 miles
"""
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers,3), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles,3), "miles")

"""
Evaluate algebraic expression
3x3 - 2x2 + 3x - 1
x = 0
x = 1
x = -1
"""
x = -1
x = float(x)
y = 3 * (x ** 3) - 2 * (x ** 2) + 3 * x - 1
print("y=", y)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

"""
# input a float value for variable a here
a = float(input("Enter value of a:"))

# input a float value for variable b here
b = float(input("Enter value fo b:"))

# output the result of addition here
print("Addition:" + str(a + b))
# output the result of subtraction here
print("Difference: " + str(a -b))
# output the result of multiplication here
print("Multiplication: " + str(a * b))
# output the result of division here
print("Division: " + str(a/b))

print("\nThat's all, folks!")
"""
# To evaluate this expression
# 1/(X + 1/(x + 1/(x + 1/X)))
x = float(input("Enter a value:"))
result = 1/(x + 1/(x + 1/(x + 1/x)))
print("Result of the expression:" + str(result))

"""
Scenario
=========
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
"""
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura
hour = hour + mins // 60
mins = mins % 60
hour = hour % 24
print(hour, ":", mins, sep="")