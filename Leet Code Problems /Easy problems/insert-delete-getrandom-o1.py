class RandomizedSet:
    def __init__(self):
        self.elements = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.elements.append(val)
        self.indices[val] = len(self.elements) - 1
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices[val]
        last_element = self.elements[-1]

        self.indices[last_element] = index

        self.elements[index], self.elements[-1] = self.elements[-1], self.elements[index]
        
        self.elements.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()