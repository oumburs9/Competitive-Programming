class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        totalSum = 0
        res = 0
        for i in range(len(nums)):
            totalSum += nums[i]
            res = max(res, (totalSum + i) // (i + 1))
        return res
        