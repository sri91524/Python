class Stack:
    def __init__(self):
        self.__stk = []
    
    def push(self, val):
        self.__stk.append(val)
    
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__cnt = 0
    
    def get_counter(self):
        return self.__cnt
    
    def push(self, val):
        Stack.push(self, val)
    
    def pop(self):        
        val = Stack.pop(self)
        self.__cnt +=1
        return val
    
stk = CountingStack()

for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())
    