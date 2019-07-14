
# coding: utf-8

# In[1]:


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        
class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        vertex_to_add = Vertex(v)
        
        for vertex in self.vertex:
            if not vertex:
                index = self.vertex.index(vertex)
                self.vertex[index] = vertex_to_add
                break
    
    def RemoveVertex(self, v):
        for row in self.m_adjacency:
            row[v] = 0
            
        self.m_adjacency[v] = [0 for x in self.m_adjacency[v]]
            
        self.vertex[v] = None

    def IsEdge(self, v1, v2):
        return bool (self.m_adjacency[v1][v2])

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        
    def DepthFirstSearch(self, VFrom, VTo):
        stack = []
        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False
            
        stack.append(self.vertex[VFrom])
        self.vertex[VFrom].Hit = True
        
        while len (stack) > 0:
            if self.m_adjacency[VFrom][VTo]:
                stack.append(self.vertex[VTo])
                return stack
            else:
                for vertex in self.vertex:
                    if not vertex.Hit and self.m_adjacency[VFrom][self.vertex.index(vertex)]:
                        vertex.Hit = True
                        stack.append(vertex)
                        VFrom = self.vertex.index(vertex)
                        del_stack = False
                        break
                    del_stack = True
                if del_stack:
                    del stack[-1]
                    if len (stack) > 0:
                        VFrom = self.vertex.index(stack[-1])
        
        return stack

