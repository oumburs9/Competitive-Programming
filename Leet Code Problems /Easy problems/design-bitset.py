class Bitset:

    def __init__(self, size: int):
        self.bits0 = ['0' for _ in range(size)] # main ref
        self.bits1 = ['1' for _ in range(size)]
        self.ones = 0
        

    def fix(self, idx: int) -> None:
        if self.bits0[idx] != '1':
            self.ones += 1
            self.bits0[idx] = '1'
            self.bits1[idx] = '0'

    def unfix(self, idx: int) -> None:
        if self.bits0[idx] != '0':
            self.bits0[idx] = '0'
            self.bits1[idx] = '1'
            self.ones -= 1
    
        

    def flip(self) -> None:
        self.bits0 , self.bits1 = self.bits1 , self.bits0
        self.ones = len(self.bits0) - self.ones
               
    def all(self) -> bool:
        return len(self.bits0 ) == self.ones
        

    def one(self) -> bool:
        return self.ones >= 1        

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(self.bits0)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()