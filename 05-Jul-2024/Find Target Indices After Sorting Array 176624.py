# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        outPut = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                outPut.append(i)
        return outPut
                