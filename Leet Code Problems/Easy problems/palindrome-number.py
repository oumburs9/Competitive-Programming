class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        d = 1
        while x >= d *10:
            d *= 10
        
        while x > 0:
            right = x % 10
            left = x // d
            
            if left != right:
                return False
            
            # chop of the the r and left
            x = ( x % d ) // 10
            #update the d
            d /= 100
            
        return True
            
            

