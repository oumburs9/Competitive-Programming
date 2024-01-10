class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        startWi , res , k = 0,0,1

        for endWi in range(len(nums)):
            if nums[endWi] == 0:
                k -=1
          
            while k < 0:
                if nums[startWi]==0:
                    k+=1
                startWi += 1
            res = max(res,endWi - startWi)
        return res