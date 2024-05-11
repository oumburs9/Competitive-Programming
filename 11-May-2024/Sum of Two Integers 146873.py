# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  
        
        while b != 0:
            carry = (a & b) << 1 & MASK
        
            a = (a ^ b) &MASK
            
            b = carry
        
        if a > 0x7FFFFFFF:

            a = ~(a ^ MASK)
        
        return a
