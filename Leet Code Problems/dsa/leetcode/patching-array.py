class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
        patch_needed = 0
        i = 0
        cumSum = 0
        
        while cumSum < n:
            
            if i < len(nums) and nums[i] <= cumSum + 1:
                cumSum += nums[i]
                i += 1
            else:
                cumSum += cumSum + 1
                patch_needed += 1
        
        return patch_needed

