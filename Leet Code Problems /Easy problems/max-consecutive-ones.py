class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxRes = 0
        startWin = 0

        for endWin in range(len(nums)):
            if nums[endWin] == 0:
                startWin = endWin + 1
            maxRes =  max( maxRes, endWin - startWin + 1)
        return maxRes



        