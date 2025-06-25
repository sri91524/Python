from os import strerror
try:
    file = open("text-Write.txt", "wt")
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print("IO error occurred:    ", strerror(e.errno))
#############################################
"""
We've modified the previous code to write whole lines to the text file
"""
from os import strerror
try:
    file = open("newtext.txt", "wt")
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("IO error occurred:   ", strerror(e.errno))
##############################################
import sys
sys.stderr.write("Error message")