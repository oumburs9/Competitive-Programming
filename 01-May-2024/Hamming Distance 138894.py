# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xor_res = x ^ y
        dist = 0

        while xor_res:
            
            dist += xor_res & 1
            xor_res >>=   1


        return dist
            