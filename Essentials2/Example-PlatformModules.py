from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine
print(machine())

from platform import processor
print(processor())

from platform import system
print(system())

from platform import version
print(version()) #OS Version

from platform import python_implementation, python_version_tuple

print(python_implementation()) #expect CPython

# the major part of Python's version;
# the minor part;
# the patch level number
for atr in python_version_tuple():
    print(atr)

