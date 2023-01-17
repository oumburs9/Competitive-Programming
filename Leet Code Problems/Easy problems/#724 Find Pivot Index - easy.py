from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        leftSum =0
        
        for u,v in enumerate(nums):
            rightSum = total - v - leftSum
            if leftSum == rightSum:
                return u
            leftSum += v
        return -1
        