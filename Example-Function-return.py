# return without an expression

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")

happy_new_year(False)

###################################################
# return with expression
# def boring_function():
#     return 123

# x = boring_function()
# print("The boring function has returned its result.  It is", x)

#####################################################
# function returns a value and we ignore it
def boring_function():
    print("Its Boring")
    return 123

print("Hello")
boring_function()
print("bye")

#######################################################
# None Keyword (similar to nothing)
value = None
if value is None:
    print("There is no value")

def strange_function(n):
    if(n % 2 == 0):
        return True

print("strange_function:" , strange_function(2))
print("strange_function:" , strange_function(1))

################################################
def list_sum(lst):
    s=0
    for elem in lst:
        s+= elem
    return s

print(list_sum([5, 4, 3]))
# print(list_sum(5))

##########################################
# function result list
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5))
###########################################
# Leap year or not
# if its divisible by 4 and if its divisible by 100, then it should be divisible by 400

def is_year_leap(year):    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#testing - with data and expected result
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)   
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# How many days: writing and using your own functions
def days_in_month(year, month):
    #Gregorian calendar after 1582
    if(year <= 1582 or month < 1 or month > 12):
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if(is_year_leap(year) and month == 2):
        res = 29
    return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# Day of the year

def days_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        
        if md is None:
            return None
        days += md
        
    # find day for current month passed
    md = days_in_month(year, month)
    
    # if day passed is between 1 and days of current month, passed day is added
    if day >= 1 and day <= md:
        return days + day
    else:
        return None
  
print(days_of_year(2015, 4, 16))
###############################################################
# Prime numbers

def is_prime(n):
    x = int(n ** 0.5)
    result = True
    for j in range(2, x+1):
        if n % j == 0:
            result = False
    
    return result

for i in range(1, 50):    
    if is_prime(i + 1):
        print(i + 1, end=" ")
        
print()

#######################################
# Converting fuel consumption
# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

def litres_100km_to_miles_gallon(litres):
    gallon = litres / 3.78511784
    miles = 100 * 1000/1609.344
    return miles / gallon

def miles_gallon_to_liters_100km(miles):
    km =  miles * 1.609344
    km100 = km / 100
    litres = 3.785411784
    return litres / km100

print(litres_100km_to_miles_gallon(3.9))
print(litres_100km_to_miles_gallon(7.5))
print(litres_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))



