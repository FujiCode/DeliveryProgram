#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#2/01/2020   

from Graph.Minimum import MinimumAcyclicGraph
from Vehicle.DeliveryVehicle import DeliveryTruck
from CommonMethods import Methods
from Hash.HashMap import ChainHashMap

class RouteMap: 
 
    def __init__(self, initial_v, base_graph, main_package_list, delay_packages_ids, 
                       id_package_list_truck2):
        
        __slots__ = 'initail_v, _base_graph, _main_package_list,' 
        '_delay_packages_ids,_id_package_list_truck2,'
        '_truck1, _truck2, _truck3, _truck3_s_h, _truck3_s_m'
        
        self._initial_v = initial_v
        self._base_graph = base_graph
        self._main_package_list = main_package_list
        self._delay_packages_ids = delay_packages_ids
        self._id_package_list_truck2 = id_package_list_truck2
        self._truck3_s_h = 0
        self._truck3_s_m = 0
    
    #----------------------------------------------------------------------------------
        void_package_ids_truck1 = Methods._merge_lists(self._delay_packages_ids, 
                                                    self._id_package_list_truck2)
        void_locations_truck1 = Methods._locations_from_IDs(void_package_ids_truck1,
                                                         self._main_package_list,
                                                         self._base_graph)
        """Computes a generic path with minimum distances between locations, and given 
        locations to avoid. Path assumes unlimited capacity, and actual path for 
        truck 1 will be computed when truck 1 object is initialized."""
        print("""Initializing first graph""")
        graph_truck1 = MinimumAcyclicGraph(self._initial_v, self._base_graph, 
                                           void_locations_truck1)
        
        """Computes the route with given graph for truck, main package list, and 
        capacity"""
        print("""Computing route for Truck 1 using first graph""")
        self._truck1 = DeliveryTruck(graph_truck1, self._main_package_list, 16)
        
        """List containing delivered packages for truck 1""" 
        print("""Retrieving package IDs from Truck 1""")
        packages_delivered_truck1 = self._truck1.packages_id()
        print("""Packages delivered from Truck 1:""")
        for p_ID in self._truck1.packages_id():
            print(p_ID,end="|")
        print()
        print()
    #----------------------------------------------------------------------------------
        """Repeat above process for truck 2"""
        void_package_ids_truck2 = Methods._merge_lists(packages_delivered_truck1, 
                                                    self._delay_packages_ids)
        void_locations_truck2 = Methods._locations_from_IDs(void_package_ids_truck2,
                                                         self._main_package_list,
                                                         self._base_graph)
        print("""Initializing second graph""")
        graph_truck2 = MinimumAcyclicGraph(self._initial_v, self._base_graph, 
                                           void_locations_truck2)
        
        print("""Computing route for Truck 2 using second graph""")
        self._truck2 = DeliveryTruck(graph_truck2, self._main_package_list, 16)
        
        print("""Retrieving package IDs from truck 2""")
        packages_delivered_truck2 = self._truck2.packages_id()
        print("""Packages delivered from Truck 2:""")
        for p_ID in self._truck2.packages_id():
            print(p_ID,end="|")
        print()
        print()
    #----------------------------------------------------------------------------------
        """Computes the distances from the last location for each route to
           the hub. The closer driver will drive truck 3"""
        d_truck1 = base_graph._get_distance(self._initial_v, self._truck1.last_location())
        d_truck2 = base_graph._get_distance(self._initial_v, self._truck2.last_location())
        if d_truck1 < d_truck2:
            """Adds distance to return to hub"""
            self._truck1._add_distance(d_truck1)
            hour = self._truck1.last_package_time().hour()
            minute = self._truck1.last_package_time().minute()
            if minute + 15 >= 60:
                hour += 1
                minute = 0
            else:
                minute += 15
        else:
            """Adds distance to return to hub"""
            self._truck2._add_distance(d_truck2)
            hour = self._truck2.last_package_time().hour()
            minute = self._truck2.last_package_time().minute()
            if minute + 15 >= 60:
                hour += 1
                minute = 0
            else:
                minute += 15
        """Truck 3 will pull out of hub 15 minutes after whichever driver
           is due to switch vehicles"""
        self._truck3_s_h = hour
        self._truck3_s_m = minute
                    
    #----------------------------------------------------------------------------------
        """Repeat the two processes above for truck 3"""
        packages_delivered_truck_1_2 = Methods._merge_lists(packages_delivered_truck1, 
                                                         packages_delivered_truck2)
        void_package_ids_truck3 = packages_delivered_truck_1_2
        void_locations_truck3 = Methods._locations_from_IDs(void_package_ids_truck3,
                                                         self._main_package_list,
                                                         self._base_graph)
        print("""Initializing third graph""")
        graph_truck3 = MinimumAcyclicGraph(self._initial_v, self._base_graph, 
                                           void_locations_truck3)
        
        print("""Computing route for Truck 3 using third graph""")
        self._truck3 = DeliveryTruck(graph_truck3, self._main_package_list, 16,
                                     self._truck3_s_h, self._truck3_s_m)
        print("""Packages delivered from Truck 3:""")
        for p_ID in self._truck3.packages_id():
            print(p_ID,end="|")
        print()
        print()
        print("All packages delivered in",self.all_trucks_distance(),"""miles""")
        print("""Last package delivered at""",self._time_last_delivery(self._truck1, 
                                                                       self._truck2, 
                                                                       self._truck3))
    #----------------------------------------------------------------------------------
    
    def truck1(self):
        return self._truck1
    
    def truck2(self):
        return self._truck2
    
    def truck3(self):
        return self._truck3    
    
    """Searches for, and returns the delivery time of the last package"""
    def _time_last_delivery(self, truck1, truck2, truck3):
        max_hour = 0
        max_min = 0
        for package in truck1.delievered_packages():
            if package.hour() > max_hour:
                max_hour = package.hour()
                max_min = package.minute()
            if package.hour() == max_hour:
                if package.minute() > max_min:
                    max_min = package.minute()
        for package in truck2.delievered_packages():
            if package.hour() > max_hour:
                max_hour = package.hour()
                max_min = package.minute()
            if package.hour() == max_hour:
                if package.minute() > max_min:
                    max_min = package.minute()
        for package in truck3.delievered_packages():
            if package.hour() > max_hour:
                max_hour = package.hour()
                max_min = package.minute()
            if package.hour() == max_hour:
                if package.minute() > max_min:
                    max_min = package.minute()
        if max_min < 10:            
            return str(max_hour) + ":" + str(max_min) + "0"
        else:
            return str(max_hour) + ":" + str(max_min)
    
    def print_status(self, end_hour, end_minute):
        """delivered_package_list is a list containing the id as key, and
           delivered package object which contains a package object and delivered time.
           DeliveredPackage objects are nested in the DeliveryTruck class."""
        all_delivered_packages_list = self._combine_del_pack_lists(self._truck1, 
                                                                   self._truck2, 
                                                                   self._truck3) 
        """Id list retrieve from main list"""
        package_id_list = self._main_package_list.id_list()
        self._sort_list(package_id_list)
        for package_id in package_id_list:
            for hash_item in all_delivered_packages_list:
                status = "In Route "
                d_package = hash_item._itemkey()
                if package_id == int(d_package.package().ID()):
                    if self._check(d_package, 
                                   end_hour, 
                                   end_minute) == True:
                        status = "Delivered "
                    else:
                        status = "In Route "
                    print("Status:",status,
                        "| ID:",d_package.package().ID(),
                        "| Address:",d_package.package().address(),
                        "| City:",d_package.package().city(),
                        "| State:",d_package.package().state(),
                        "| Zip:",d_package.package().zip_code(),
                        "| Deadline:",d_package.package().deadline(),
                        "| Weight:",d_package.package().package_weight(),
                        "| Notes:",d_package.package().notes())
            
    """Checks to see if the hour and minute variables from 
       the DeliveredPackage object is within user's specified 
       hour and minute"""             
    def _check(self, delivered_package, end_hour, end_minute):
        if delivered_package.hour() < end_hour:
            return True
        elif  delivered_package.hour() == end_hour:
            if delivered_package.minute() <= end_minute:
                return True
            else:
                return False
        else:
            return False    
            
    def _sort_list(self, num_list):
        i = 0
        while i < len(num_list):
            min_index = self._find_min_index(num_list[i:len(num_list)])
            if min_index != 0:
                temp = num_list[i]
                num_list[i] = num_list[min_index] 
                num_list[min_index] = temp
            i += 1
    def _find_min_index(self, num_list):
        if len(num_list) == 0:
            return None
        else:
            i = 0
            index = 0
            min_num = num_list[0]
            while i < len(num_list):
                if min_num > num_list[i]:
                    min_num = num_list[i]
                    index = i
                i += 1
        return index
    
    """Combines and returns a list of delivered packages from all trucks""" 
    def _combine_del_pack_lists(self, truck1, truck2, truck3):
        delivered_package_list = ChainHashMap()
        for d_package in truck1.delievered_packages():
            delivered_package_list._setitem(d_package, "")
        for d_package in truck2.delievered_packages():
            delivered_package_list._setitem(d_package, "")
        for d_package in truck3.delievered_packages():
            delivered_package_list._setitem(d_package, "")
        return delivered_package_list
    
    def all_trucks_distance(self):
        d1 = self._truck1.distance_traveled()
        d2 = self._truck2.distance_traveled()
        d3 = self._truck3.distance_traveled()
        return d1 + d2 + d3
    
    
        


    
    