# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        MAX_BIT = 30


        xor_contribs = [0] *MAX_BIT
        
        bit_count = [0] *MAX_BIT
        for num in nums:
            for bit in range(MAX_BIT):
                if num & (1 << bit):
                    bit_count[bit] += 1
        
        for bit in range(MAX_BIT):
            bit_mask = 1 << bit
            total = 0
            for num in nums:
                if num & bit_mask:
                    total += len(nums)
                else:
                    total += bit_count[bit]
            xor_contribs[bit] = total % 2 * bit_mask
        
        f_xor = 0
        for contrib in xor_contribs:
            f_xor ^= contrib

        return f_xor

