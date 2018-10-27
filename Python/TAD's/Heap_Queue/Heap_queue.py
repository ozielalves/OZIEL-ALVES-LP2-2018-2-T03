
# coding: utf-8

# In[7]:


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def push(self,k): # Insertion
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.top(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def top(self,i): # Min child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def pop(self): # Delete min
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    

    def heapfy(self,alist): # Heap building
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


# In[9]:


bh = BinHeap()
bh.heapfy([12,5,8,4,2,3])

print(bh.pop())
print(bh.pop())
print(bh.pop())
print(bh.pop())
print(bh.pop())
print(bh.pop())

