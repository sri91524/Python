"""
1. The uname function returns an object that contains information about the current operating system. The object has the following attributes:

systemname (stores the name of the operating system)
nodename (stores the machine name on the network)
release (stores the operating system release)
version (stores the operating system version)
machine (stores the hardware identifier, e.g. x86_64).
2. The name attribute available in the os module allows you to distinguish the operating system. It returns one of the following three values:

posix (you'll get this name if you use Unix)
nt (you'll get this name if you use Windows)
java (you'll get this name if your code is written in something like Jython)
3. The mkdir function creates a directory in the path passed as its argument. The path can be either relative or absolute, e.g:

import os
 
os.mkdir("hello") # the relative path
os.mkdir("/home/python/hello") # the absolute path
 
Note: If the directory exists, a FileExistsError exception will be thrown. In addition to the mkdir function, the os module provides the makedirs function, which allows you to recursively create all directories in a path.

4. The result of the listdir() function is a list containing the names of the files and directories that are in the path passed as its argument.
It's important to remember that the listdir function omits the entries '.' and '..', which are displayed, for example, when using the ls -a command on Unix systems. If the path isn't passed, the result will be returned for the current working directory.

5. To move between directories, you can use a function called chdir(), which changes the current working directory to the specified path. As its argument, it takes any relative or absolute path.
If you want to find out what the current working directory is, you can use the getcwd() function, which returns the path to it.

6. To remove a directory, you can use the rmdir() function, but to remove a directory and its subdirectories, use the removedirs() function.

7. On both Unix and Windows, you can use the system function, which executes a command passed to it as a string, e.g.:

import os 
returned_value = os.system("mkdir hello")
 
The system function on Windows returns the value returned by the shell after running the command given, while on Unix it returns the exit status of the process.
"""