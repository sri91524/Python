class Queue:
    def __init__(self):
        self.__stk = []
    
    def put(self, val):
        self.__stk.append(val)
    
    def get(self):    
        if len(self.__stk) == 0:
            raise QueueError
        else:
            val = self.__stk[0]
            del self.__stk[0]
            return val

fifo = Queue()
fifo.put(1)
fifo.put("dog")
fifo.put(False)
try:
    for i in range(4):
        print(fifo.get())
    
except:
    print("Queue Error")
            
######################################################
# part 2
class Queue:
    def __init__(self):
        self.stk = []
    
    def put(self, val):
        self.stk.append(val)
    
    def get(self): 
        val = self.stk[0]
        del self.stk[0]
        return val
        
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):        
        return len(self.stk) == 0

que = SuperQueue()
que.put(1)  
que.put("dog")
que.put(False)         
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
    
    