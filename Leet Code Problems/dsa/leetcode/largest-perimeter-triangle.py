class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse =True)
        n = len(nums)
        area = 0
        for i in range(n-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                 ar = sum(nums[i:i+3])
                 area = max(area,ar)
        return area

                 
            



        