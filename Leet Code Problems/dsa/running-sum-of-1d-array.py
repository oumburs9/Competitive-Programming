class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        acc = 0
        
        for i in range(len(nums)):
            acc += nums[i]
            runningSum.append(acc)
        return runningSum
            
        