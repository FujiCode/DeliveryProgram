#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#2/01/2020   

from Hash import HashMap

class PackageList:
    
    def __init__(self):
        
        __slots__ = '_main_list, _id_list'
        
        self._main_list = HashMap.ChainHashMap()
        
        self._id_list = []
        
        self._create_list(self._main_list)
        
    def _create_list(self, package_list):
        id_file = open("../DeliveryProgram/Text/IdList")
        city_file = open("../DeliveryProgram/Text/CityList")
        address_file = open("../DeliveryProgram/Text/AddressList")
        state_file = open("../DeliveryProgram/Text/StateList")
        weight_file = open("../DeliveryProgram/Text/WeightList")
        zip_file = open("../DeliveryProgram/Text/ZipList")
        deadline_file = open("../DeliveryProgram/Text/DeadlineList")
        
        id_line = id_file.readline()
        city_line = city_file.readline()
        address_line = address_file.readline()
        state_line = state_file.readline()
        weight_line = weight_file.readline()
        zip_line = zip_file.readline()
        deadline_line = deadline_file.readline()
        
        while id_line or city_line or address_line or state_line or weight_line or zip_line or deadline_line:
            package_id = id_line.strip()
            city = city_line.strip()
            address = address_line.strip()
            state = state_line.strip()
            weight = weight_line.strip()
            zip_code = zip_line.strip()
            deadline = deadline_line.strip()
            
            new_package = self.Package(package_id, address, city, state, zip_code, deadline, weight, notes = "")
            package_list._setitem(package_id, new_package)
            self._id_list.append(int(package_id))
            
            id_line = id_file.readline()
            city_line = city_file.readline()
            address_line = address_file.readline()
            state_line = state_file.readline()
            weight_line = weight_file.readline()
            zip_line = zip_file.readline()
            deadline_line = deadline_file.readline()
    
    """Returns a list of all package IDs"""
    def id_list(self):
        return self._id_list
    
    """Searches through the main list, and obtains 
       the package using the input id. The main list
       stores the package ID as a key, and the entire package 
       object as the value""" 
    def _get_package(self, ID):
        for entry in self._main_list:
            if entry._itemvalue().ID() == str(ID):
                return entry._itemvalue()
        raise ValueError('Package not found:', ID)
    
    """Prints package information"""    
    def _print_package_information(self, ID):
        package = self._main_list._getitem(str(ID))
        if package.delivered() == True:
            status = "Delivered"
        else: 
            status = "In route"
        print("Status:",status,
              "ID:", package.ID(),
              "Address:", package.address(),
              "City:", package.city(),
              "State:", package.state(),
              "Zip:", package.zip_code(),
              "Deadline:", package.deadline(),
              "Weight:", package.package_weight(),
              "Notes:", package.notes())
        
    def __iter__(self):
        for package in self._main_list:
            yield package 
    
    """Nested class to represent a package"""
    class Package:
    
        def __init__(self, package_id, address, city, state, zip_code, deadline, pack_weight, notes = ""):
            __slots__ = 'id, _address, _city, _state, _zip_code, _deadline, _pack_weight, _notes'
            '_delivered'
            
            self._package_id = package_id
            self._address = address
            self._city = city
            self._state = state
            self._zip_code = zip_code
            self._deadline = deadline
            self._pack_weight = pack_weight
            self._notes = notes
            self._delivered = False
    
        def ID(self):
            return self._package_id
    
        def address(self):
            return self._address
    
        def city(self):
            return self._city
    
        def state(self):
            return self._state
    
        def zip_code(self):
            return self._zip_code
    
        def deadline(self):
            return self._deadline
    
        def package_weight(self):
            return self._pack_weight
        
        def delivery_status(self, status):
            self._delivered = status
        
        def delivered(self):
            return self._delivered
        
        def notes(self):
            return self._notes          