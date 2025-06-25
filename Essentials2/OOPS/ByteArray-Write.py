data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

###########################################
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open("file.bin", "wb")
    bf.write(data)
    bf.close()
except IOError as e:
    print("IO error occurred:", strerror())
    