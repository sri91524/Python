from datetime import date

today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

##################################
from datetime import date
my_date = date(2019, 11, 4)
print(my_date)

###################################
"""
The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds.
"""
from datetime import date 
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

print(date.fromisoformat("2019-12-14"))

"""
# Replace function

Sometimes you may need to replace the year, month, or day with a different value. You can’t do this with the year, month, and day attributes because they're read-only. In this case, you can use the method named replace.
"""
d1 = date(1991, 2, 5)
print(d1)

d2 = d1.replace(year =1992, month = 1, day = 1)
print(d2)

d = date.today()
print(d.weekday())

# The date class has a similar method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday

d = date(2025, 6, 26)
print(d.isoweekday())

###########################################
from datetime import time

t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

############################################
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired.  I have to take a nap. See you later.")
        # time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

#############################################
"""
ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a stri
"""
timestamp = 1572879180
print(time.ctime(timestamp))
print(time.ctime())  # returns current time in string
print(time.time()) # return current timestamp 
##############################################
timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

##############################################
"""
asctime, converts a struct_time object or a tuple to a string

mktime converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch. In our example, we passed a tuple to it
"""
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
##############################################
"""
In the datetime module, date and time can be represented either as separate objects or as one object. The class that combines date and time is called datetime.

datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

The method called date returns the date object with the given year, month, and day, while the method called time returns the time object with the given hour and minute.
"""
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

dt = datetime(2025, 6, 26, 15, 33)
print("Timestamp:", dt.timestamp())
print(dt.fromtimestamp(dt.timestamp()))
##############################################
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

##############################################
"""
%Y – returns the year with the century as a decimal number. In our example, this is 2020.
%m – returns the month as a zero-padded decimal number. In our example, it's 01.
%d – returns the day as a zero-padded decimal number. In our example, it's 04.

In our example, %H is replaced by 14, %M by 53, and %S by 00.

There are two new directives, %Y and %B. The directive %Y returns the year without a century as a zero-padded decimal number (in our example it's 20). The %B directive returns the month as the locale’s full name (in our example, it's November).
"""
from datetime import time
t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

import time
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S")) # current time
"""
unlike the strftime method, it creates a datetime object from a string representing a date and time

The first is a date and time as a string: "2019/11/04 14:53:00", while the second is a format that facilitates parsing to a datetime object. Be careful, because if the format you specify doesn't match the date and time in the string, it'll raise a ValueError.
"""
print(datetime.strptime("2019/11/04 14:53:00","%Y/%m/%d %H:%M:%S"))
###########################################
from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)

###########################################
from datetime import timedelta
delta = timedelta(weeks = 2, days = 2, hours = 3)
print(delta)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

