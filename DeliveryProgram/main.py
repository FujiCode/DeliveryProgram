#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#2/01/2020   

from DeliveryMapping.Route import RouteMap
from CommonMethods import Methods
from Graph.Location import LocationGraph 
from Package import PackageLoader

if __name__ == "__main__":
    
    """Creates a undirected graph containing all locations, 
       where each location (in the form of a location object) 
       is connected to every other location, 
       by means of edges (distances). For the algorithm analysis
       for the main operation, please see the _min_path method located 
       in the Minimum file."""
    print("""Initializing base graph""")   
    base_graph = LocationGraph()
    
    """Creates a master list of package objects.
       Initialization involves one loop-operation along 
       with several constant operations, so we say 
       that initialization this list runs in O(n) time"""
    main_package_list = PackageLoader.PackageList()
    
    """Variable to indicate our "start" location"""
    initial_v = Methods._get_location("Western Governors University", base_graph)
    
    """IDs of packages arriving late to the hub"""
    delay_packages_ids = [6, 25, 28, 32]
    
    """IDs of packages required to be on truck 2"""
    id_package_list_truck2 = [3, 18, 36, 38]
    
    """Computes, and contains graphs for each truck (routes) using
       the Greedy Algorithm. Actual Algorithm can be found in Graph.Minimum directory 
       in the MinimumAcyclicGraph class, and is called _min_path.
       There are two major operations when creating the route map of all
       trucks: the initialization of MinimumAcyclicGraph instances, and 
       the initialization of DeliveryTruck instances. These two operations are 
       implemented sequentially, and the algorithmic analysis of these 
       two operations can be found in their respective classes. """
    main_delivery_map = RouteMap(initial_v, base_graph, main_package_list,
                                 delay_packages_ids, id_package_list_truck2)
    exit_program = False
    while exit_program == False:
        print()
        print("Select from the choices below")
        print("1. Status of all packages")
        print("2. Package Information")
        print("3. Combined Mileage")
        print("4. Print Route")
        print("5. Exit")
        print("Selection:", end="")
        selection = int(input())
        print()
        if selection == 1:
            print("Hour (24-hour format):",end="")
            e_hour = int(input())
            print("Minute:",end="")
            e_minute = int(input())
            print()
            h = str(e_hour)
            if e_minute < 10:
                m = "0" + str(e_minute)
            else:
                m = e_minute
            print("Status at ",h,":",m)
            main_delivery_map.print_status(e_hour, e_minute)
            print()
        if selection == 2:
            print("Enter ID:",end="")
            id_package = int(input())
            main_package_list._print_package_information(id_package)
        if selection == 3:
            print("Total Mileage:",main_delivery_map.all_trucks_distance(),"miles")
        if selection == 4:
            print("Truck (choices are 1, 2, or 3):",end="")
            choice = int(input())
            if choice == 1:
                main_delivery_map.truck1().print_route()
            if choice == 2:
                main_delivery_map.truck2().print_route()
            if choice == 3:
                main_delivery_map.truck3().print_route()                
        if selection == 5:
            exit_program = True
    print()
    print("Goodbye")    
   
    
    








