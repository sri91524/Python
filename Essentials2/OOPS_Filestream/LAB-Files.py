"""
Character Frequency Histogram

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
"""
from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used a comprehension to do that.
counters = {chr(ch):0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    file.close()

    # Let's output the counters.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("IO error occurred: ", strerror(e.errno))
##############################################
"""
Sorted character frequency histogram
Code	                                            What it sorts by	            Output
sorted(d)	                                        Just the keys	        ['a', 'b', 'c']
sorted(d, key=lambda x: d[x])	                The values (ascending)	    ['b', 'a', 'c']
sorted(d, key=lambda x: d[x], reverse=True)	    The values (descending)	    ['c', 'a', 'b']
"""
from os import strerror

counters ={chr(ch):0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to anlyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1

    file.close()
    file = open(file_name + '.hist', 'wt')
    for char in sorted(counters, key = lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + '->' + str(c) + "\n")
    file.close()
except IOError as e:
    print("IO error occurred: ", strerror(e.errno))
#############################################
