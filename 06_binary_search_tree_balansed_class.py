
# coding: utf-8

# In[1]:


from math import log2, ceil

class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0
        
class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray = []

    def CreateFromArray(self, a, BST_array = [], slot = 0, index = 0):
        
        if len(BST_array) == 0:
            self.BSTArray = [None] * (2**(ceil(log2((len(a)+1)/2))+1)-1)
            a = sorted (a)
           
        index = len(a)//2
    
        if index < len(a) and a[index] not in BST_array:
        
            self.BSTArray[slot] = a[index]
        
            self.CreateFromArray(a[:index], self.BSTArray, slot * 2 + 1, index )

            self.CreateFromArray(a[index+1:], self.BSTArray, slot * 2 + 2, index )
    
        return

    def GenerateTree(self):
        
        to_left = True
        
        self.Root = BSTNode(self.BSTArray[0], None)
        
        queue = [self.Root]
        
        for key in self.BSTArray[1:]:
                
            if key is not None:
                
                node = BSTNode(key, queue[0])
                
                node.Level = node.Parent.Level + 1
            
            else:
                
                node = None
             
            queue.append(node)
            
            if to_left:
                    
                if queue[0] is not None:
                
                    queue[0].LeftChild = node
                    
                to_left = False
                
            else:
                
                if queue[0] is not None:
                    
                    queue[0].RightChild = node
                    
                to_left = True
                    
                del queue[0]         
    
    def WideAllNodes(self, node):
        
        list_nodes = []
        
        if node is None:
            
            return list_nodes    
        
        list_nodes.append(node)
        
        for i in list_nodes:
            
            if i.LeftChild is not None:
                
                list_nodes.append(i.LeftChild)
            
            if i.RightChild is not None:
                
                list_nodes.append(i.RightChild)

        return list_nodes
    
    def IsBalanced(self, root_node):
        
        if root_node:
        
            list_left = self.WideAllNodes(root_node.LeftChild)
        
            list_left = [x for x in list_left if x.Level is (ceil(log2(len(self.BSTArray)+1)/2))+1]
        
            list_right = self.WideAllNodes(root_node.RightChild)
        
            list_right = [x for x in list_right if x.Level is (ceil(log2(len(self.BSTArray)+1)/2))+1]
            
            if abs((len(list_left) - len(list_right))) > 1:
                
                return False
        
            self.IsBalanced(root_node.LeftChild)
                
            self.IsBalanced(root_node.RightChild)

        return True

