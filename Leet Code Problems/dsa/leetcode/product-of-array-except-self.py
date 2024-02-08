class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        # cal prefix
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        

        # cal suffix  and update res
        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result
        

        