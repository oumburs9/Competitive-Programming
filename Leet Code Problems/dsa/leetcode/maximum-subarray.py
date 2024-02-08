class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum ,windowSum = nums[0],nums[0]
        
        for endwindow in range(1,len(nums)):
            if windowSum < 0:
                windowSum = 0
                
            windowSum += nums[endwindow]
            
            maxSum = max(maxSum,windowSum)
            
        return maxSum
        
        
        