# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = (1 << num.bit_length()) - 1
        return num ^ bitmask

        