
# coding: utf-8

# In[1]:


class aBST:
    
    def __init__(self, depth):
        
        tree_size = 2**depth - 1
        
        self.Tree = [None] * tree_size
        

    def FindKeyIndex(self, key):
        
        slot = 0
        
        tree_size = len (self.Tree)
        
        while slot <= tree_size-1:
            
            if self.Tree[slot] is None:
                
                return -slot
            
            elif key < self.Tree[slot]:
                
                slot = 2*slot + 1
            
            elif key > self.Tree[slot]:
                
                slot = 2*slot + 2
            
            elif key == self.Tree[slot]:
                
                return slot
        
        return None
    

    def AddKey(self, key):
        
        slot = self.FindKeyIndex(key)
        
        if slot is not None:
        
            slot = abs(slot)
            
            self.Tree[slot] = key
        
            return slot 
        
        else:
            
            return -1

