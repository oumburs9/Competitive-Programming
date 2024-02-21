class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
     
        n = len(nums)
        
        def window(left, right):
            if left == right:
                return nums[left]
            
            return max(nums[left] - window(left + 1, right), nums[right] - window(left, right - 1))
        
         
       
        return window(0,n - 1) >= 0
        
        
        
        
        