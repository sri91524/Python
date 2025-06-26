# unix
# import os
# print(os.uname())
#Windows
import platform
print(platform.uname())

# import os
# os.mkdir("OS")
# print(os.listdir()) # list all directories in current working directory

# The makedirs function enables recursive directory creation, which means that all directories in the path will be created.
# import os
# os.makedirs("my_first_dir/my_second_dir")
# os.chdir("my_first_dir") # change dir
# print(os.listdir())

"""
NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, while in Windows, simply the mkdir command with the path:

Unix-like systems:
mkdir -p my_first_directory/my_second_directory
Windows:
mkdir my_first_directory/my_second_directory
"""
# current working directory
import os
# os.makedirs("test/example")
# os.chdir("test")
# print(os.getcwd())
# os.chdir("example")
# print(os.getcwd())

# NOTE: On Unix-like systems, the equivalent of the getcwd function is the pwd command, which prints the name of the current working directory.
os.mkdir("test")
print(os.getcwd())
os.rmdir("test")
print(os.listdir())

os.makedirs("test/example")
print(os.getcwd())
os.removedirs("test\example")
print(os.listdir())

# NOTE: In both Windows and Unix, there's a command called rmdir, which, just like the rmdir function, removes directories. What's more, both systems have commands to delete a directory and its contents. In Unix, this is the rm command with the -r flag.
"""
All functions presented in this part of the course can be replaced by a function called system, which executes a command passed to it as a string.
The system function is available in both Windows and Unix. Depending on the system, it returns a different result.
In Windows, it returns the value returned by the shell after running the command given, while in Unix, it returns the exit status of the process.
"""
import os
ret_val = os.system("mkdir example1")
print(ret_val)
# we receive exit status 0, which indicates success