# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        c = ''.join('1' if bit == '0' else '0' for bit in b)
        return int(c, 2)
        