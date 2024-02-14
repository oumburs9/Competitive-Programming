class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = 0
        nums.sort(reverse=True)

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                res = max(res,sum(nums[i:i+3]))
        return res
        