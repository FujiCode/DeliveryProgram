#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#1/29/2020  

from Graph.Base import GraphBase

class UndirectedGraph(GraphBase):
    """Undirected Graph representation using adjacency maps"""
    
    def __init__(self):
        
        __slots__ = '_total_weight'
        
        self._total_weight = 0
        self._vertex = {}
        self._num_of_edges = 0
        self._num_of_vertices = 0
    
    """Iteration on vertices"""
    def vertices(self):
        return self._vertex.keys()
    
    """Insert a new vertex"""
    def insert_vertex(self, x = None):
        v = self.Vertex(x)
        self._vertex[v] = {}
        self._num_of_vertices += 1
        return v
    
    """Insert and return a new Edge element x."""
    def insert_edge(self, u, v, x = None):
        e = self.Edge(u, v, x)
        self._num_of_edges += 1
        self._vertex[u][v] = e
        self._vertex[v][u] = e
    
    """Deletes the edge from some vertex u to some vertex v"""
    def delete_edge(self, u, v):
        for edge in self._vertex[u].values():
            if edge.opposite(u) == v:
                del self._vertex[u][v]
                del self._vertex[v][u]
                self._num_of_edges -= 1
                break
    def total_weight(self):
        return self._total_weight   
    
    
    
 
        
    
    
