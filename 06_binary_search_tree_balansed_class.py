
# coding: utf-8

# In[1]:


from math import log2, ceil

class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 1
        
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
                
    
    def WideAllNodes(self):
        list_nodes = []
        if self.Root is None:
            return list_nodes    
        
        list_nodes.append(self.Root)
        for i in list_nodes:
            if i.LeftChild is not None:
                list_nodes.append(i.LeftChild)
            if i.RightChild is not None:
                list_nodes.append(i.RightChild)

        return list_nodes
    
    
    def DeepestNode(self, node):
        
        list_nodes = []
        
        if node is None:

            return 0    
        
        list_nodes.append(node)
        
        for i in list_nodes:
            
            if i.LeftChild is not None:
                
                list_nodes.append(i.LeftChild)
            
            if i.RightChild is not None:
                
                list_nodes.append(i.RightChild)

        return list_nodes[-1].Level - (node.Level - 1)
    
    
    def IsBalanced(self, root_node, list_d = 'started'):
        
        if list_d == 'started':
            
            list_d = []
        
        if root_node is not None:
            
            d = abs(self.DeepestNode(root_node.LeftChild) - self.DeepestNode(root_node.RightChild))
            
            list_d.append(d)
                
            self.IsBalanced(root_node.LeftChild, list_d)
            
            self.IsBalanced(root_node.RightChild, list_d)
        
        if max (list_d) > 1:
            
            return False
        
        else:
            
            return True

