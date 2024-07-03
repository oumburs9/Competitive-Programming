# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        r = 0
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0

            # swapping
            if nums[i] != 0:
                nums[i],nums[r] = nums[r],nums[i]
                r += 1
        return nums


        