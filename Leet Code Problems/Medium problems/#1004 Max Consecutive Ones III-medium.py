from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,ans = 0, 0
        
        for i in range(len(nums)):
            k -=(1-nums[i])
            
            if k<0:
                k += (1-nums[l])
                l +=1
            if i-l+1 > ans:
                ans = i-l+1
        
        return ans