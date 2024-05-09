# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #   fffffff
        xor_res = 0
        for num in nums:
            xor_res ^= num

        diff_bit = xor_res & -xor_res

        num1, num2 = 0, 0



        # k
        for num in nums:
            if num & diff_bit:
                num1 ^= num
                
            else:
                num2 ^= num

        return [num1, num2]