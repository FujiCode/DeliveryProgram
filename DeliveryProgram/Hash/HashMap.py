#James Fujimura 
#Western Governors University 
#Data Structures and Algorithms II 
#Performance Assessment - WGUPS ROUTING PROGRAM
#2/01/2020  

from random import randint

class ChainHashMap:
    
    """Initializes an instance of a HashMap where p is a prime number, a
       and b are chosen at random in the range of 0 to p, and N is the size 
       of the bucket array (p, a, b, and N will be used for the hash function
       in this class)"""
    def __init__(self, capacity = 20, p = 5795593):
        self.__table = capacity * [None]
        self.__size = 0
        self.__prime = p
        self.__a = randint(0,p)
        self.__b = randint(0,p)         
    
    
    """Once the integer hash code has been
       determined, a compression function will map the integer hash code
       into the table. In this case, the compression function uses the M.A.D method
       to perform this operation"""
    def __hash(self, key):
        return (hash(key)*self.__a + self.__b) % self.__prime % len(self.__table)    
    
    """Returns the number items stored in data structure"""
    def __len__(self):
        return self.__size
    
    """Method will input a key-value pair, and then 
       computes the hash code (__hash). Once the hash has
       been determined, the key-value pair is inserted into the 
       appropriate table (a new one is created if there is no 
       table in the specified table location). To keep the load factor
       below 1 as much as possible, the table array is double in 
       size if the total number of entry table spots is greater than
       the length of the table array"""
    def _setitem(self, key, value):
        found = False
        h = self.__hash(key)
        if self.__table[h] is None:
            self.__table[h] = []  
        oldsize = len(self.__table[h])
        """Searches for an existing key, and if found,
           preserves key and replaces the input value"""
        if len(self.__table[h]) != 0:
            for item in self.__table[h]:
                if item._itemkey() == key:
                    found = True
                    item._setvalue(value)
        """Insert a new Item object if the key is not in the selected table"""            
        if found == False:
            self.__table[h].append(self.__Item(key, value))
        if len(self.__table[h]) > oldsize:    
            self.__size += 1                  
        if self.__size > len(self.__table) // 2:        
            self._resize(2 * len(self.__table) - 1) 
    
    
    """Computes the hash number (h) for a given key,retrieves 
       the appropriate table (bucket) from the table array,
       and then retrieves the appropriate value"""
    def _getitem(self, key):
        h = self.__hash(key)
        bucket = self.__table[h]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))
        for item in bucket:
            if item._itemkey() == key:
                return item._itemvalue()
    
    """Method retrieves the hash number and the appropriate 
       table from the table array. A search is done through the 
       retrieved table, and if there is a match between keys, 
       that Item object in the retrieved table is deleted""" 
    def _delitem(self, key):
        h = self.__hash(key)
        bucket = self.__table[h]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))
        index = 0 
        for item in bucket:
            if item._itemkey() == key:
                break
            index += 1
        del bucket[index]        
        self.__size -= 1
    
    def _containskey(self, key):
        h = self.__hash(key)
        bucket = self.__table[h]
        if bucket is None:
            return False
        for k in bucket:
            if k._itemkey() == key:
                return True 
        return False
    
    def _resize(self, constant):           
        temp = []
        for bucket in self.__table:
            temp.append(bucket)
        self.__table = constant * [None]    
        self.__size = 0
        for bucket in temp:
            if bucket is not None:
                for item in bucket:
                    self._setitem(item._itemkey(), item._itemvalue())
        temp.clear()             
    
    def __iter__(self):
        for bucket in self.__table:
            if bucket is not None:
                for item in bucket:
                    yield item 
       
    """Nested Item class to store a key-value pair"""
    class __Item:
        
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def _itemkey(self):
            return self._key 
        
        def _itemvalue(self):
            return self._value  
        
        def _setvalue(self, v):
            self._value = v
        