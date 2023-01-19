from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0
        r = 1
        
        while r <= len(nums)-1:
            
            if nums[l]== nums[r] and l !=r:
                nums.pop(r)
            else:
                l +=1
                r +=1
        return len(nums)
                
                
        