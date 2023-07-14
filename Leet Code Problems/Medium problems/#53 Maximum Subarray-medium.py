
from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  
        prefix_sum = 0  # running sum
        min_prefix_sum = 0  # Variable to track the minimum prefix sum encountered so far (initialized with 0)
        
        for num in nums:
            prefix_sum += num  
            
            current_sum = prefix_sum - min_prefix_sum  
            
            max_sum = max(max_sum, current_sum)  # Update the max_sum with the maximum value between max_sum and current_sum
            
            min_prefix_sum = min(min_prefix_sum, prefix_sum)  # Update the min_prefix_sum with the minimum value between min_prefix_sum and prefix_sum
        
        return max_sum  

        