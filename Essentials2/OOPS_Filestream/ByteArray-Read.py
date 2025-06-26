from os import strerror

data = bytearray(10)
try:
    binary_file = open("file.bin", 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end = ' ')
    print()
except IOError as e:
    print("IO error occurred:    ", strerror(e.errno))

##############################################
from os import strerror

try:
    binary_file = open("file.bin", 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end =' ')
    print()
except IOError as e:
    print("IO error occured", strerror(e.errno))
##############################################
try:
    binary_file = open("File.bin", "rb")
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end = ' ')
    print("________________________________")
except IOError as e:
    print("IO error occurred:", strerror(e.errno))

##############################################
"""
copying files
"""
from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file:  ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destinatin file name: ")
try:
    dst = open(dstname, 'wb')
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file:", strerror(e.errno))
    exit(e.errno)

print(total,' byte(s) successfully written')
src.close()
dst.close()


