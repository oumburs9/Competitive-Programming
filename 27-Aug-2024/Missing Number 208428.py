# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 
        array_xor = 0
        range_xor = 0
        for idx , num in enumerate(nums):

            array_xor ^= num  
            range_xor ^= idx + 1  

        return array_xor ^ range_xor


    
        