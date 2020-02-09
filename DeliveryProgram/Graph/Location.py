#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#1/29/2020  

from Graph.Undirected import UndirectedGraph

"""Creates a new instance of a graph of connected, and undirected
   locations in a region when invoked."""
class LocationGraph(UndirectedGraph):
    
    def __init__(self):
        
        super().__init__()
        __slots__ = '_location_list'
        file = open("../DeliveryProgram/Text/LocationList")
       
        """location_list will store a list of "Location" objects.
           Each location object will store the name, address, postal code
           and a distance list to all adjacent locations connected to that particular
           one.
           Ordering for the location list is from top to bottom; the first entry corresponds to
           the first index, and so on"""
        self._location_list = self.__load_location_list(file)
        self.__insert_vertices(self._location_list)
        self.__insert_edges(self._location_list)
    
    """Reads file, and converts the appropriate line
       to name, address, postal code, and a distance list.
       Returns a list of "Location" objects"""    
    def __load_location_list(self, file):
        location_list = []
        line = file.readline()
        while line:
            name = line.strip()
            line = file.readline()
            address = line.strip()
            line = file.readline()
            postal_code = line.strip()
            line = file.readline()
            
            new_name = name
            new_address = address
            new_postal_code = postal_code 
            numbers = self.__convert_line_to_numbers(line)
            
            new_location = self.Location(new_name, new_address, new_postal_code, numbers)
            location_list.append(new_location)
            line = file.readline()
        return location_list
    """Reading from lines of numbers, this method will return a 
       list of ints."""
    def __convert_line_to_numbers(self, line):
        list = []
        i = 0
        k = 0
        count = 0
        index1 = 0
        index2 = 0
        number = 0
        while i < len(line):
            if line[i] != " ":
                index1 += 1 
            if self.__condition1(line[i], line[i - 1], i, len(line)) == True: 
                index2 = i
                index1 = index2 - index1
                list.append(float(line[index1:index2]))
                index1 = 0
            if self.__condition2(line[i], i, len(line)) == True:
                index2 = i + 1
                index1 = index2 - index1
                list.append(float(line[index1:index2]))
                index1 = 0
            i += 1
        return list
    def __condition1(self, char1, char2, index, length):
        if char1 == " " and char2 != " " and index != 0 and index != length:
            return True
        else:
            return False
    def __condition2(self, char, index, length):
        if index == length - 1 and char != " ":
            return True
        else:
            return False            
    
    """To find the distance from location1 to location2, method will retrieve
       the index for location1, and using that index, will find the corresponding
       index in location2's adjacency list, to retrieve the float value (distance) in that
       list location"""
    def _get_distance(self, location1, location2):
        if isinstance(location1, self.Location) == False or isinstance(location2, self.Location) == False:
            raise TypeError('Parameters for _get_distance method must be location type')
        i = 0
        while i < len(self._location_list):
            if location1 == self._location_list[i]:
                return location2.distance(i)
            i += 1
        return -1
    
    """Insert vertices for all location objects"""
    def __insert_vertices(self, location_list):
        for l in location_list:
            self.insert_vertex(l)
    
    """Override insert_vertex method from base class to 
       insert a Location object, and not a Vertex object."""        
    def insert_vertex(self, v = None):
        self._vertex[v] = {}
        self._num_of_vertices += 1
        return v
    
    """Picks a Location object (i) from the list, and stores all associated distances
       as edges to all other Location objects(k)"""           
    def __insert_edges(self, location_list):
        i = 0
        k = i + 1
        while i <= len(location_list) - 2:
            while k <= len(location_list) - 1:
                self.insert_edge(location_list[i], location_list[k], location_list[k].distance(i))
                k += 1
            i += 1
            k = i + 1    
    
    """Finds the next closest location by distance, and returns that location object""" 
    def closest(self, location, graph):
        min_distance = 0
        set_min = False 
        for l in graph.vertices():
            if set_min is False:
                if l is not location:
                    min_distance = graph.edge(location, l).weight()
                    closest_location = location
                    set_min = True
            if location is not l and graph.edge(location, l).weight() < min_distance:
                min_distance = graph.edge(location, l).weight()
                closest_location = l 
        return closest_location
    
    """Nested Location class"""    
    class Location:
    
        def __init__(self, name, address, postal_code, distance_list):
            __slots__ = '__name, __address, __postal_code, __visited'
        
            self.__name = name
            self.__address = address
            self.__postal_code = postal_code
            """Stores connected locations, and the distance to these locations"""
            self.__distance_list = distance_list
            self.__visited = {}     
    
        """Returns string representation of the location name"""
        def name(self):
            return "" + self.__name
    
        """Returns postal code for this location"""
        def postal_code(self):
            return self.__postal_code
        
        """Returns a list of distances to adjacent locations.
           List contains only numbers, numbers in particular 
           order corresponds to particular locations. For example,
           every first entry, represents the distance from the first location.
           This will be used as a reference when creating the 
           actual distances to other locations."""
        def distance_list(self):
            return self.__adjancency_list
    
        """Returns the distance of a location"""
        def distance(self, index):
            return self.__distance_list[index]
    
        """Returns street address of location"""
        def address(self):
            return self.__address 
    
    
    
    