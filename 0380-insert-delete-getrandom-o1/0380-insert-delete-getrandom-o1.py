class RandomizedSet:
    
    def __init__(self):
        self.table = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if self.table[val] == 0:
            self.table[val] += 1
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.table[val] == 0:
            return False
        else:
            self.table[val] -= 1
            idx = self.arr.index(val)
            del self.arr[idx]
            
            return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()