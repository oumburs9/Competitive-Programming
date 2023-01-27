from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
     
        n = len(nums)
        
        def window(l, r):
            if l == r:
                return nums[l]
            
            return max(nums[l] - window(l + 1, r), nums[r] - window(l, r - 1))
        
       
        return window(0,n - 1) >= 0

        
        
        
        
        