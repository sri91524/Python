var = 0
print(var == 0)
var = 1
print(var == 0)
var = 0
print(var != 0)
var = 1
print(var != 0)

n = int(input("Enter a value: "))
print(n >=100)
#==========================================================================

"""
Example 1:
We'll start with the simplest case – how to identify the larger of two numbers:
"""
# Read 2 numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#choose larger number
if(number1 > number2):
    larger_number = number1
else:
    larger_number = number2

#print larger number
print("Larger number is: ", larger_number)

#========================================================================
# Read 3 numbers and find largest
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest_number = num1

if(num2 > largest_number):
    largest_number = num2 

if(num3 > largest_number):
    largest_number = num3

print("Largest number is : ", largest_number)

#====================================================================================
"""
prints the sentence "Yes - Spathiphyllum is the best 
plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
"""
plant = input("Enter a plant name: ")
if(plant == "Spathiphyllum"):
    print("Yes - Spathiphyllum is the best plant ever!")
elif(plant == "spathiphyllum"):
    print("No, I want a big Spathiphyllum!")
elif(plant != "spathiphyllum"):
    #interpolation
    print(f"Spathiphyllum! Not {plant}!")

#=================================================================
"""
if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero)
"""
income = float(input("Enter the income: "))
if(income <= 85528):
    tax = income * 0.18 - 556.2
else:
    tax = 14839.2 + (income - 85528) * 0.32

if(tax < 0.0):
    tax = 0.0

tax = round(tax, 0)
print(f"Calculated tax: {tax} thalers")

#==============================================================================

"""
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
 if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period
"""
year = int(input("Enter year: "))
# if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period
if(year < 1582):
    print("Not within the Gregorian calendar period")
else:
    if(year % 4 != 0):        
        print(f"{year} is a common year")
    elif(year % 100 !=0):
        print(f"{year} is a leap year")        
    elif(year % 400 !=0):
        print(f"{year} is a common year")
    else:
        print(f"{year} is a leap year")

