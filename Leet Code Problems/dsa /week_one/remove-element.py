class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        indx  = 0 
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[indx] = nums[right]
                indx  +=1
        return indx
        
        