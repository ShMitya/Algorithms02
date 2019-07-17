
# coding: utf-8

# In[1]:


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.Hit_level = 0
        
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
    
    def BreadthFirstSearch(self, VFrom, VTo):
        queue = []
        route = []
        for vertex in  self.vertex:
            if vertex:
                vertex.Hit = False
        
        queue.append(self.vertex[VFrom])
        
        while len (queue) > 0:
            route.append(queue[0])
            
            if self.vertex[VTo] == queue[0]:
                next_vertex = route[-1]
                for vertex in reversed(route[:-1]):
                    if self.m_adjacency[self.vertex.index(vertex)][self.vertex.index(next_vertex)] and vertex.Hit_level == next_vertex.Hit_level - 1:
                        next_vertex = vertex
                    else:
                        route.remove(vertex)
                if VFrom == VTo:
                    route.append(route[0])
                return route
            
            VFrom = self.vertex.index(queue[0])
            self.vertex[VFrom].Hit = True
            del queue[0]
            
            for vertex in self.vertex:
                if not vertex.Hit and self.m_adjacency[VFrom][self.vertex.index(vertex)] and vertex not in queue:
                    queue.append(vertex)
                    vertex.Hit_level = self.vertex[VFrom].Hit_level + 1
                    
        return []

