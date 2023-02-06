from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefixSum = 0
        minStartVal = 1
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            minStartVal = max(minStartVal, 1 - prefixSum)
        
        return minStartVal
        