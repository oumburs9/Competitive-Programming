from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        beg , ed = 0, len(nums)-1
        ans = [0]*len(nums)
        idx = len(nums)-1
        
        while(beg<=ed):
            if abs(nums[beg]) > abs(nums[ed]):
                ans[idx] = nums[beg]**2
                beg +=1
            else:
                ans[idx] = nums[ed]**2
                ed -=1
            idx -=1
        return ans
                
                
                
        