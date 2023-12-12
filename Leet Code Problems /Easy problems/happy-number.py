class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        def sumSquare(n):
            _sumSqr = 0
            for i in str(n):
                _sumSqr  += (int(i))**2
            return _sumSqr

        while n != 1:
           
            n = sumSquare(n)

            if n in set1:
                return False
                
            set1.add(n)

        
        return True
        
