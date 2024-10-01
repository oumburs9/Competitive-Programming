# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary =  bin(n)[2:]

        for i in range(len(binary) - 1):
            if binary[i] == binary[i+1]:
                return False
        return True




        