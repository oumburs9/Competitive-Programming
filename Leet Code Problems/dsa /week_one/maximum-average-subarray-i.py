class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        startWin = 0
        windowSum = 0
        res = float('-inf')
        
        for endWin in range(len(nums)):
            windowSum += nums[endWin]

            if k == endWin - startWin + 1:
                res = max(res,windowSum)
                windowSum -= nums[startWin]
                startWin +=1

        return res/k



              

        