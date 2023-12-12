class OrderedStream:

    def __init__(self, n: int):
        self._list = [0]*n
        self.curPtr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
         
        self._list[idKey-1] = value 
        if idKey - 1 > self.curPtr: 
            return [] 
        while self.curPtr < len(self._list) and self._list[self.curPtr]: 
            self.curPtr += 1
        return self._list[idKey - 1 : self.curPtr]
        


        



   



        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)