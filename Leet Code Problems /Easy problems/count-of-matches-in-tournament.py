class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            print(n)
      
            if n % 2 != 0:
                res += 1
                
            
            res += n//2
            n //= 2
        return res

            


            

            
        