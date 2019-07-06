
# coding: utf-8

# In[1]:


class Heap:

    def __init__(self):
        self.HeapArray = []
        
    def MakeHeap(self, a, depth):
        
        heap_size = 2**(depth + 1) - 1
        
        self.HeapArray = [None]*heap_size
        
        for i in a:
            self.Add(i)

    def GetMax(self):
        if not self.HeapArray[0]:
            return -1
        
        node_to_return = self.HeapArray[0]
        
        if not self.HeapArray[1]:
            self.HeapArray[0] = None
            return node_to_return
        
        # находим последний элемент в массиве
        
        for node in self.HeapArray:
            if not node:
                node_index = self.HeapArray.index(node)-1
                break
            node_index = len(self.HeapArray) - 1
               
        # перемещаем последний элемент в корень
        
        self.HeapArray [0] = self.HeapArray[node_index]
        self.HeapArray[node_index] = None
        
        node = self.HeapArray[0] 
        max_from_children = max (self.HeapArray[1] if self.HeapArray[1] else 0, self.HeapArray[2] if self.HeapArray[2] else 0)
        
        #перемещаем элемент до своего места
        
        while node < max_from_children:
            
            self.HeapArray[self.HeapArray.index(max_from_children)] = node
            self.HeapArray[self.HeapArray.index(node)] = max_from_children
            
            index = self.HeapArray.index(node)
            if index*2+1 < len (self.HeapArray) - 1:
                max_from_children = max (self.HeapArray[index*2+1] if self.HeapArray[index*2+1] else 0, self.HeapArray[index*2+2] if self.HeapArray[index*2+2] else 0) 
            else:
                return node_to_return
        return node_to_return
        

    def Add(self, key):
        
        if not self.HeapArray[0]:
            self.HeapArray[0] = key
            return
        
        
        key_index = 0
        while self.HeapArray[key_index]:
            key_index += 1
            if key_index > len(self.HeapArray) - 1:
                return False
        
        self.HeapArray[key_index] = key
        
        while key > self.HeapArray[(key_index - 1)//2] if self.HeapArray[(key_index - 1)//2] else 0:
            
            self.HeapArray[key_index] = self.HeapArray[(key_index - 1)//2]
            key_index = (key_index-1)//2
            self.HeapArray[key_index] = key
            if key_index == 0:
                return

