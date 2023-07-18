class LRUCache:
    
    def __init__(self, capacity: int):
        self.__capacity=capacity
        self.__cache=OrderedDict()
        

    def get(self, key: int) -> int:
        value=self.__cache.get(key,-1)
        if value !=-1: # If key exists
            self.__cache.move_to_end(key,last=True) # Update time(Move to header)
        
        return value
        
    def put(self, key: int, value: int) -> None:
        if self.__cache.get(key,False): # If key exists
            self.__cache.move_to_end(key,last=True) # Update time (Move to header)
        elif len(self.__cache)==self.__capacity: # If cache exceeds capacity
            self.__cache.popitem(last=False) # FIFO
                        
        self.__cache[key]=value # Update key-value 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)