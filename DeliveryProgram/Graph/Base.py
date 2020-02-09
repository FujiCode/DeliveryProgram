#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#1/29/2020  

class GraphBase:
    
    """Returns all incident edges of vertex v"""
    def adjacent_edges(self, u):
        for edge in self._vertex[u].values():
            yield edge
    
    """Return a list of all edges of the graph"""
    def edges(self):
        result = []
        for vertex in self._vertex.values():
            for edge in vertex.values():
                if edge not in result:
                    result.append(edge)
        return result
    
    """Return a total count of all vertices"""    
    def num_of_vertices(self):
        return self._num_of_vertices   
    
    """Return a total count of all edges"""  
    def num_of_edges(self):
        return self._num_of_edges
    
    """Return count of all edges for a given vertex"""  
    def num_edges_vertex(self, u):
        return len(self._vertex[u].values())
        
    """Return the edge from u to v, or None if not adjacent"""
    def edge(self, u, v):
        return self._vertex[u][v]
    
    """Nested Vertex class"""
    class Vertex:
    
        __slots__ = '__element'
    
        def __init__(self, x):
            self.__element = x
        
        def element(self):
            """Return element associated with this vertex"""
            return self.__element
    
        def __str__(self):
            return "" + self.__element
                       
    """Nested Edge class"""
    class Edge:
        
        __slots__ = '__origin', '__destination', '__edge_weight'
    
        def __init__(self, u, v, weight):
            self.__origin = u
            self.__destination = v
            self.__edge_weight = weight
        
        """Return opposite vertex v with given vertex u"""    
        def opposite(self, u):
            if u is self.__origin:
                return self.__destination
            else:
                return self.__origin
        
        """Returns the vertices of an edge"""    
        def ends(self):
            return (self.__origin, self.__destination)
        
        """Return weight of given edge"""
        def weight(self):
            return self.__edge_weight