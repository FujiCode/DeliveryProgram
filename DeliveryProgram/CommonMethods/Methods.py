#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#2/01/2020    

"""Method will search for a Location object."""
def _get_location(location, graph):
    for l in graph.vertices():
            if l.name() == location:
                return l
    
"""Searches and returns a Location object given an address"""
def _get_location_by_address(address, graph):
    for l in graph.vertices():
        if l.address() == address:
            return l    

"""Stores a list of locations from using package IDs"""
def _locations_from_IDs(list1, main_package_list, base_graph):
    id_list = []
    for package_id in list1:
        package = main_package_list._get_package(package_id)
        a = package.address()
        location = _get_location_by_address(a, base_graph)
        id_list.append(location)
    return id_list
    
"""Stores and returns a list of locations to avoid using lists using
lists of locations"""
def _void_locations(list1, list2):
    void = []
    for location in list1:
        void.append(location)
    for location in list2:
        void.append(location)
    return void

def _merge_lists(list1, list2):
    list3 = []
    for element in list1:
        list3.append(element)
    for element in list2:
        list3.append(element)
    return list3