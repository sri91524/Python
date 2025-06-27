"""
calendar module with a simple function called calendar, which allows you to display the calendar for the whole year.
w – date column width (default 2)
l – number of lines per week (default 1)
c – number of spaces between month columns (default 6)
m – number of columns (default 3)
"""
import calendar
# print(calendar.calendar(2020))
"""
A good alternative to the above function is the function called prcal, which also takes the same parameters as the calendar function, but doesn't require the use of the print function to display the calendar.
"""
calendar.prcal(2020)