from os import strerror

try:
    counter = 0
    stream = open('text.txt', 'rt')
    char = stream.read(1)  # Read 1 character
    while char != '':   # To check eof
        print(char, end='')
        counter += 1
        char= stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("IO Error occured", strerror(e.errno))
print("___________________________________")
##############################################
"""
read() entire stream and use for loop
"""
from os import strerror
try:
    counter = 0
    stream = open("text.txt", "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter +=1
    stream.close()
    print("\n\nCharacters in file:", counter)

except IOError as e:
    print("IO error occured:", strerror(e.errno))
print("___________________________________")
##############################################
"""
readline()
"""
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open("text.txt", "rt")
    line = stream.readline()
    while line !='':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:   ", line_counter)
except IOError as e:
    print("IO error occured:", strerror(e.errno))   
print("___________________________________")
##############################################
"""
readlines
"""
from os import strerror
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    print(len(lines))
    while len(lines) !=0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end ='')
                ccnt += 1
        lines = s.readlines(10)
        print(lines)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:   ", lcnt)

except IOError as e:
    print("IO Error occured:", strerror)
print("___________________________________")
###################################################
"""
The iteration protocol defined for the file object is very simple – its __next__ method just returns the next line read in from the file.
Moreover, you can expect that the object automatically invokes close() when any of the file reads reaches the end of the file.
"""
from os import strerror
try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end ='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:    ", lcnt)
except IOError as e:
    print("IO error occured:    ", strerror(e.errno))