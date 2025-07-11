"""
1. To create a date object, you must pass the year, month, and day arguments as follows:


from datetime import date
 
my_date = date(2020, 9, 29)
print("Year:", my_date.year) # Year: 2020
print("Month:", my_date.month) # Month: 9
print("Day:", my_date.day) # Day: 29
 
The date object has three (read-only) attributes: year, month, and day.


2. The today method returns a date object representing the current local date:


from datetime import date
print("Today:", date.today()) # Displays: Today: 2020-09-29
 

3. In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). This date is called the "Unix epoch", because it began the counting of time on Unix systems. The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds. To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method:


from datetime import date
import time
 
timestamp = time.time()
d = date.fromtimestamp(timestamp)
 

Note: The time function returns the number of seconds from January 1, 1970 to the current moment in the form of a float number.

4. The constructor of the time class accepts six arguments (hour, minute, second, microsecond, tzinfo, and fold). Each of these arguments is optional.


from datetime import time
 
t = time(13, 22, 20)
 
print("Hour:", t.hour) # Hour: 13
print("Minute:", t.minute) # Minute: 22
print("Second:", t.second) # Second: 20
 

5. The time module contains the sleep function, which suspends program execution for a given number of seconds, e.g.:


import time
 
time.sleep(10)
print("Hello world!") # This text will be displayed after 10 seconds.
 

6. In the datetime module, date and time can be represented either as separate objects, or as one object. The class that combines date and time is called datetime. All arguments passed to the constructor go to read-only class attributes. They are year, month, day, hour, minute, second, microsecond, tzinfo, and fold:


from datetime import datetime
 
dt = datetime(2020, 9, 29, 13, 51)
print("Datetime:", dt) # Displays: Datetime: 2020-09-29 13:51:00
 

7. The strftime method takes only one argument in the form of a string specifying a format that can consist of directives. A directive is a string consisting of the character % (percent) and a lower-case or upper-case letter. Below are some useful directives:

%Y – returns the year with the century as a decimal number;
%m – returns the month as a zero-padded decimal number;
%d – returns the day as a zero-padded decimal number;
%H – returns the hour as a zero-padded decimal number;
%M – returns the minute as a zero-padded decimal number;
%S – returns the second as a zero-padded decimal number.
Example:


from datetime import date
 
d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) # Displays: 2020/09/29
 

8. It's possible to perform calculations on date and datetime objects, e.g.:


from datetime import date
 
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
 
d = d1 - d2
print(d) # Displays: 366 days, 0:00:00.
print(d * 2) # Displays: 732 days, 0:00:00.
 

The result of the subtraction is returned as a timedelta object that expresses the difference in days between the two dates in the example above.

Note that the difference in hours, minutes, and seconds is also displayed. The timedelta object can be used for further calculations (e.g. you can multiply it by 2).
"""