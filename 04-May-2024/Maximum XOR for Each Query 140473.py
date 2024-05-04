# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_poss = 2**maximumBit - 1
        array_xor = 0
        DRES = []
        for i in nums:
            array_xor ^= i

        DRES.append(max_poss ^ array_xor)

        for i in range(len(nums) - 1, 0, -1):
            array_xor ^= nums[i]
            DRES.append(array_xor ^ max_poss)

        return DRES
