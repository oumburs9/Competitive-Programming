import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calculate_sum(divisor):
            total_sum = 0
            for num in nums:
                total_sum += math.ceil(num / divisor)
            return total_sum
        
        # Binary search 
        def binary_search(low, high):
            while low < high:
                mid = (low + high) // 2
                total_sum = calculate_sum(mid)
                
                if total_sum > threshold:
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        # Finding the min divisor using bs within the range 1 to max(nums)
        return binary_search(1, max(nums))