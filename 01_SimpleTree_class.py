
# coding: utf-8

# In[1]:


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, Root):
        self.Root = Root
        
    def AddChild(self, ParentNode, NewChild):
        if self.Root is None:
            self.Root = NewChild
            NewChild.Parent = None
        else:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild) 
  
    def DeleteNode(self, NodeToDelete):
        if self.Root is not NodeToDelete:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete = None
            
    def GetAllNodes(self):
        
        if self.Root is None:
            return list_to_return
    
        list_to_return = []
        list_to_return.append(self.Root)
        for node in list_to_return:
            list_to_return += node.Children

        return list_to_return

    def FindNodesByValue(self, val):
        nodes_list = self.GetAllNodes()
        list_to_return = []
        for node in nodes_list:
            if node.NodeValue == val:
                list_to_return.append(node)
        return list_to_return
   
    def MoveNode(self, OriginalNode, NewParent):
        if NewParent is None:
            self.Root = OriginalNode
            OriginalNode.Parent = None
        
        if self.Root is not OriginalNode:
            self.DeleteNode(OriginalNode)
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent
   
    def Count(self):
        all_nodes_list = self.GetAllNodes()
        i = 0
        for node in all_nodes_list:
            if len(node.Children) is not 0:
                i+=1
        return i

    def LeafCount(self):
        all_nodes_list = self.GetAllNodes()
        i = 0
        for node in all_nodes_list:
            if len(node.Children) is 0:
                i+=1
        return i

