class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # base case
        if 0 not in nums:
            return True
        
        pointer = len(nums) - 1

        while pointer > 0:
            left = pointer - 1
            while left >= 0:
                if nums[left] >= pointer - left:
                    pointer = left
                    break
                left -= 1
            else:
                return False
        
        return True




 
        