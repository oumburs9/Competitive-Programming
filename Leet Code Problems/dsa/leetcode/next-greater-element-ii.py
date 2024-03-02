class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        
        nextGr = [-1] * n 
        
        for i in range(2 * n): 
            while stack and nums[stack[-1]] < nums[i % n]:
                index = stack.pop()

                nextGr[index] = nums[i % n] 
                
            if i < n:
                stack.append(i)
        
        return nextGr

