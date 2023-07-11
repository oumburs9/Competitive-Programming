class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum,windowSum ,startwindow = -float("inf") , 0,0
        
        for endwindow in range(len(nums)):
            windowSum +=nums[endwindow]
            
            if endwindow >= k-1:
                maxSum = max(maxSum,windowSum)
                windowSum -= nums[startwindow]
                startwindow += 1
        return  maxSum/k