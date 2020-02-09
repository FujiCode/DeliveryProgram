#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#2/01/2020    

from Hash.HashMap import ChainHashMap

class DeliveryTruck:
    
    def __init__(self, graph, main_package_list, capacity, hour = 8, minute = 0):
        
        __slots__ = '_package_list, _hour, _minute, _graph,' 
        '_main_package_list, _capacity, _total_distance, _counter,'
        '_last_location'
        
        self._hour = hour
        self._minute = minute
        self._total_distance = 0
        self._counter = 0
        self._num_of_packages = 0
        self._graph = graph
        self._capacity = capacity
        self._last_location = None
        self._last_delivered_package = None
        self._main_package_list = main_package_list
        self._truck_cargo = ChainHashMap()
        
        self._drive(graph, self._main_package_list, self._truck_cargo, self._capacity)
    
    """Computes the actual route for a given truck, with a predetermined graph and 
       capacity. We first initialize the constant variable _counter (will be used to
       count how many packages are "loaded" into the given truck), and we have a 
       for-loop, with several constant operations, and two nested loops; the
       nested loops included checking for all packages at a given location, and
       locating and changing the status of a particular package in the main
       package list. We can say that the _drive method runs in O(n^3) time. 
       The _drive method retrieves a ordered list of edges, and ordered in this 
       context means that the sequence of edges in the list denote the path, 
       and is retrieved by the path() method. This list grows proportional to the 
       number of edges in the computed graph. Also, the main package list an hash table 
       which usually takes more space than there are number of entries."""    
    def _drive(self, graph, main_package_list, truck_cargo, capacity):
        for edge in graph.path():
            (distance, current, end) = edge
            self._total_distance += distance.weight()
            minutes = int(distance.weight() / .3)
            address = end.address()
            """Locates all packages at a given address from the main
               package list. All found packages are "loaded" into the 
               DeliveryTruck object's truck_cargo list. We note this point
               as the delivery time."""
            for package in self._packages_at_address(address, 
                                                     main_package_list):
                delivered_package = self.DeliveredPackage(package, 
                                                          self._hour, 
                                                          self._minute)
                main_package_list._get_package(package.ID()).delivery_status(True)
                """Assigns the package (delivered_package) to the
                   trucks cargo. _counter is used to denote the order
                   of insertion, and used for informational purposes."""
                truck_cargo._setitem(self._counter, delivered_package)
                self._counter += 1
            """If the number of packages exceed the truck's capacity,
               note the last package delivered, last location, and 
               then break from loop."""     
            if self._counter >= capacity:
                self._last_delivered_package = delivered_package
                self._last_location = end
                break     
            """Record the time at each location object"""
            if self._minute + minutes >= 60:
                self._hour += 1
                self._minute = 0
            else: 
                self._minute += minutes
    
    """Retrieves a package, or packages to be delivered at a location""" 
    def _packages_at_address(self, location_address, main_package_list):
        package_list = []
        for package in main_package_list:
            if package._itemvalue().address() == location_address:
                new_package = package._itemvalue()
                package_list.append(new_package)
        return package_list         
    
    """Prints the route of the delivery truck by ordered locations""" 
    def print_route(self):
        count = 0
        while count < self._counter:
            delivered_package = self._truck_cargo._getitem(count)
            print("Package ID:",delivered_package.package().ID())
            print("Address:",delivered_package.package().address())
            print("Time delivered:", delivered_package.time())
            print()
            count += 1
        print("Distance traveled:",self._total_distance)
    
    """Returns a list of stored packages in delivery truck"""
    def packages(self):
        package_list = []
        count = 0
        while count < self._counter:
            delivered_package = self._truck_cargo._getitem(count)
            package_list.append(delivered_package.package())
            count += 1
        return package_list
    
    """Returns a hash list of DeliveredPackage objects.
       DeliveredPackage objects contain a Package object, and delivery
       time information."""
    def delievered_packages(self):
        delievered_package_list = []
        for item in self._truck_cargo:
            d_package = item._itemvalue()
            delievered_package_list.append(d_package)
        return delievered_package_list
        
    """Returns a list of package IDs"""
    def packages_id(self):
        id_list = []
        count = 0
        while count < self._counter:
            delivered_package = self._truck_cargo._getitem(count)
            package = delivered_package.package()
            package_id = package.ID()
            id_list.append(package_id)
            count += 1
        return id_list
    
    """Adds additional units to total traveled distance"""
    def _add_distance(self, distance):
        self._total_distance += distance
    
    """Returns the total distance traveled of the delivery truck"""
    def distance_traveled(self):
        return self._total_distance
    
    """Returns the last location"""
    def last_location(self):
        return self._last_location
    
    """Returns the last package and delivered time""" 
    def last_package_time(self):
        return self._last_delivered_package 
    
    """Stores a package object and the associated delivered time"""
    class DeliveredPackage():
        
        def __init__(self, package, hour, minute):
        
            __slots__ = '_package, hour, minute'
            
            self._package = package
            self._hour = hour
            self._minute = minute
        
        def package(self):
            return self._package
        
        def hour(self):
            return self._hour
        
        def minute(self):
            return self._minute
        
        def time(self):
            if self._minute < 10:
                x = "0" + str(self._minute)
            else:
                x = str(self._minute)    
            return str(self._hour) + ":"+ x    
            
             
            
        