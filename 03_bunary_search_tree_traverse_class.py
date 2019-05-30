
# coding: utf-8

# In[1]:


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False 
        
class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        node = self.Root
        result = BSTFind()
        
        while node is not None:
            if node.NodeKey > key:
                node_parent = node
                node = node.LeftChild
            elif node.NodeKey < key:
                node_parent = node
                node = node.RightChild
            elif node.NodeKey == key:
                result.Node = node
                result.NodeHasKey = True
                return result
        
        if self.Root.LeftChild is None and self.Root.RightChild is None:
            result.Node = None
        else:
            result.Node = node_parent
        #result.NodeHasKey = False
        if node_parent.NodeKey > key:
            result.ToLeft = True
        return result
    
    
    def AddKeyValue(self, key, val):
        new_node = BSTNode(key, val, None)
        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False
        
        if result.Node is None:
            if result.ToLeft:
                self.Root.LeftChild = new_node
            else:
                self.Root.RightChild = new_node
            new_node.Parent = self.Root
            return True
                    
        if result.ToLeft:
            result.Node.LeftChild = new_node
        else:
            result.Node.RightChild = new_node
        new_node.Parent = result.Node
        return True
  
    def FinMinMax(self, FromNode, FindMax):           
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
            return node                                 
        
        elif FindMax == False:
            while node.LeftChild is not None:
                node = node.LeftChild
            return node
        
        
         
    def DeleteNodeByKey (self, key):
        node = self.FindNodeByKey (key)
        if node is None or node.NodeHasKey == False:
            return False
        node = node.Node
                
        if node.LeftChild is not None and node.RightChild is not None:
            node_hair = node.RightChild
            while node_hair.LeftChild is not None:
                node_hair = node_hair.LeftChild
                    
            node_hair.LeftChild = node.LeftChild
            node_hair.LeftChild.Parent = node_hair
            if node_hair.Parent is not node:
                if node_hair.RightChild is not None:
                    node_hair.RightChild.Parent = node_hair.Parent
                    node_hair.Parent.LeftChild = node_hair.RightChild
                else:
                    node_hair.Parent.LeftChild = None
                node_hair.RightChild = node.RightChild
                node_hair.RightChild.Parent = node_hair
                
            node_hair.Parent = node.Parent            
            if node is self.Root:                                              
                self.Root = node_hair
            else:                                                              
                if node.Parent.LeftChild == node:                                   
                    node_hair.Parent.LeftChild = node_hair
                elif node_hair.Parent.RightChild == node:                           
                    node_hair.Parent.RightChild = node_hair                        
            return True
                
        if node.LeftChild is not None:                              
            if node is self.Root:                               
                self.Root = node.LeftChild
                self.Root.Parent = None
            else:                                       
                node.LeftChild.Parent = node.Parent      
                if node.Parent.LeftChild == node:                                   
                    node.Parent.LeftChild = node.LeftChild
                elif node.Parent.RightChild == node:            
                    node.Parent.RightChild = node.LeftChild
                
        elif node.RightChild is not None:                                 
            if node is self.Root:                               
                self.Root = node.RightChild
                self.Root.Parent = None
            else:                                       
                node.RightChild.Parent = node.Parent 
                if node.Parent.LeftChild == node:                       
                    node.Parent.LeftChild = node.RightChild
                elif node.Parent.RightChild == node:            
                    node.Parent.RightChild = node.RightChild                
                
        else:                                                   
            if node is self.Root:                            
                self.Root = None
            else:                                                       
                if node.Parent.LeftChild == node:                                   
                    node.Parent.LeftChild = None
                elif node.Parent.RightChild == node:                    
                    node.Parent.RightChild = None            
        return True

    def Count(self):
        if self.Root is None:
            return 0
        list_nodes = []
        list_nodes.append(self.Root)
        for i in list_nodes:
            if i.LeftChild is not None:
                list_nodes.append(i.LeftChild)
            if i.RightChild is not None:
                list_nodes.append(i.RightChild)
        return len(list_nodes)
    
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
    
    def DeepAllNodes(self, order, node = 'started', list = []):
        
        if node is 'started':
            node = self.Root
            list = []
        if order is 0:
            if node:
                self.DeepAllNodes(0, node.LeftChild, list)
                list.append(node)
                self.DeepAllNodes(0, node.RightChild, list)
                
        if order is 2:
            if node:
                list.append(node)
                self.DeepAllNodes(2, node.LeftChild, list)
                self.DeepAllNodes(2, node.RightChild, list)
                
        if order is 1:
            if node:
                self.DeepAllNodes(1, node.LeftChild, list)
                self.DeepAllNodes(1, node.RightChild, list)
                list.append(node)     
        
        return list

