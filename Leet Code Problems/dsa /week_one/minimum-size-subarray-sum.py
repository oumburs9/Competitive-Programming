class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen ,startWindow,windowSum = float('inf'),0,0
        
        for endWindow in range(len(nums)):
            windowSum += nums[endWindow]
            
            while windowSum >= target:
                minLen = min(minLen,endWindow - startWindow +1)
                
                windowSum -= nums[startWindow]
                startWindow +=1
        return 0 if minLen== float('inf') else minLen
            
            
        