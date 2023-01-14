from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        fResult = []
        for i in range(len(nums)):
            if nums[i] == target:
                fResult.append(i)
        return fResult 