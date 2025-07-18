"""
1. To read a file’s contents, the following stream methods can be used:

read(number) – reads the number characters/bytes from the file and returns them as a string; is able to read the whole file at once;
readline() – reads a single line from the text file;
readlines(number) – reads the number lines from the text file; is able to read all lines at once;
readinto(bytearray) – reads the bytes from the file and fills the bytearray with them;

2. To write new content into a file, the following stream methods can be used:

write(string) – writes a string to a text file;
write(bytearray) – writes all the bytes of bytearray to a file;

3. The open() method returns an iterable object which can be used to iterate through all the file's lines inside a for loop. For example:

for line in open("file", "rt"):
    print(line, end='')
 
The code copies the file's contents to the console, line by line. Note: the stream closes itself automatically when it reaches the end of the file.
"""