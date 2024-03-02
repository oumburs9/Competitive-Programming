class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        two = float('-inf') 
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num < two:
                return True
                
            while stack and stack[-1] < num:
                two = stack.pop()

            stack.append(num)
        
        return False

