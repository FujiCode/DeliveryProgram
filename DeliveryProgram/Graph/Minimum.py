#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#1/29/2020  

from Hash.HashMap import ChainHashMap 
from Graph.Undirected import UndirectedGraph


class MinimumAcyclicGraph(UndirectedGraph):
    
    def __init__(self, start_vertex, main_graph, void_vertices):
        
        super().__init__()
        
        __slots__ = '_start_vertex, _main_graph, _visited_vertices,' 
        '_total_weight, _void_vertices, _path'
        self._start_vertex = start_vertex
        
        self._main_graph = main_graph
        
        self._void_vertices = void_vertices
        
        self._path = []
        
        """Main graph that will be reference when creating a new 
           graph""" 
        self._main_graph = main_graph
        
        """Storage for visited vertices""" 
        self._visited_vertices = ChainHashMap()
        
        """Locations to be ignored during path computation will
           be added to the visited list"""
        for vertex in self._void_vertices:
            self._visited_vertices._setitem(vertex, "")
        
        (self._path, self._total_distance) = self._min_path(self._start_vertex, 
                                                            self._main_graph, 
                                                            self._visited_vertices)
    
    """_min_path is the primary algorithm used to create the minimum acyclic 
       graph. First, all operations in the _min_path method run in constant time:
       initialization of total_weight variable, and of path list. Next, the helper
       method for _min_path is called. First, we find the minimum weighted edge, 
       _min_edge which has one loop and several constant operations, so we say this 
       operation runs in O(n) (proportional to the number of adjacent edges at a vertex).
       Next, we run several constant operations until we reach the while-loop. In this 
       while-loop, we check to see if a given proposed minimum edge has already been considered.
       A hash table is used to check for a given value, and computing the hash function for
       traversing to the correct "bucket" in the list usually run in constant time. 
       However, once we arrived at the correct bucket, checking in this bucket may require 
       n-operations, but rehashing the structure helps to avoid collisons, so in this case, 
       we'll assume this runs in constant time (O(1)). After checking for vertices, we perform
       several constant operations including another operation to  _min_edge (to prepared for 
       the next iteration in the while loop). So, if the number of iterations for the 
       while-loop is proportional to the number of edges (we keep going until all edges have 
       been visited), and we perform n-number of _min_edge operations, we say that this 
       Greedy Algorithm performs in O(n^2) time. In terms of space usage, the path list, 
       and the list to stored visited edges is proportional to the number of objects inserted
       into these two list: the objects containing the edge along with the associated vertices,
       and the objects containing the vertices."""    
    def _min_path(self, starting_vertex, graph, visited_vertices):
        total_weight = 0
        path = []
        return self._min_path_helper(starting_vertex, graph, total_weight, 
                                     visited_vertices, path)
    
    def _min_path_helper(self, vertex, graph, total_weight, visited_vertices, path):
        (edge, u, v) = self._min_edge(vertex, graph, visited_vertices)
        path.append((edge, u, v))
        self._total_weight += edge.weight()
        e = edge
        front = u
        end = v
        while edge != None:
            if self._containsVertex(visited_vertices, front) == False:
                self.insert_vertex(front)
                visited_vertices._setitem(front,"")
            if self._containsVertex(visited_vertices, end) == False:    
                self.insert_vertex(end)
                visited_vertices._setitem(end,"")
            self.insert_edge(front, end, e.weight())
            total_weight += e.weight()
            (edge, u, v) = self._min_edge(end, graph, visited_vertices)
            e = edge
            front = u
            end = v
            if e is not None and front is not None and end is not None:
                self._total_weight += e.weight()
                path.append((edge, u, v))
        return (path, total_weight)
             
    """Method returns two connected vertices of the minimum weighted edge."""
    def _min_edge(self, start_vertex, graph,visited_vertices):
        set_min = False
        end = None
        min_edge = None
        for edge in graph.adjacent_edges(start_vertex):
            if self._containsVertex(visited_vertices, edge.opposite(start_vertex)) == False:
                end = edge.opposite(start_vertex)
                if set_min == False:
                    min_weight = edge.weight()
                    min_edge = edge
                    set_min = True
                if min_weight > edge.weight():
                    min_weight = edge.weight()
                    min_edge = edge
        if min_edge is not None:
            end = min_edge.opposite(start_vertex)
        return (min_edge, start_vertex, end)
    
    """Checks to see if the computed path contains the vertices from the
       required locations list. If the computed path contains the proper
       vertices, and is within vertex limit range (vertex_limit) then 
       method will return True, or otherwise will return False."""
    def _condition(self, start_vertex, vertex_limit, required_vertices):
        count1 = 0
        count2 = 0
        for vertex in self._traverse(start_vertex):
            if required_vertices._containskey(vertex):
                count1 += 1
            count2 += 1
            if count2 > vertex_limit:
                return False
        return count1 == len(required_vertices)        
    
    def _containsVertex(self, visited_list, u):
        return visited_list._containskey(u)
    
    """Traverses the current path (from superclass) starting 
       at a given starting vertex. Method will return a list
       object containing traversed vertices."""
    def _traverse(self,start_vertex):
        path = []
        return self._traverse_help(start_vertex, path)  
    
    def _traverse_help(self, start_vertex, path):
        for edge in self.adjacent_edges(start_vertex):
            destination = edge.opposite(start_vertex)
            if destination not in path:
                path.append(destination)
                self._traverse_help(destination, path)
        return path
    
    """Override insert_vertex method from base class to 
       insert a Location object, and not a Vertex object."""        
    def insert_vertex(self, v = None):
        self._vertex[v] = {}
        self._num_of_vertices += 1
        return v
    
    def path(self):
        return self._path
    
    def _clear_path(self):
        self._vertex.clear()        
    
             
            