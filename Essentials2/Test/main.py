import module
# print(module.__counter)

from module import sum1, prod1

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(sum1(zeros))
print(prod1(ones))

# path where modules are listed
import sys
for p in sys.path:
    print(p)


