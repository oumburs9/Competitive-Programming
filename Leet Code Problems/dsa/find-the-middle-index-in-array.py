class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right_total = sum(nums)
        left_total = 0
        
        for i, val in enumerate(nums):
            right_total -= val
            
            if left_total == right_total:
                return i
            
            left_total += val
            
        return -1 
        