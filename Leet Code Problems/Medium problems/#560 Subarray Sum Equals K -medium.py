# from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ans = 0
#         currentSum = 0
        
#         prefixSum = {0:1}
        
        
#         for i in nums:
#             currentSum +=i
#             diff = currentSum - k
            
#             ans += prefixSum.get(diff,0)
#             prefixSum[currentSum] = 1 + prefixSum.get(currentSum,0)
        # return ans
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0  # Variable to store the running sum
        prefix_sum_freq = defaultdict(int)  # Dictionary to store prefix sum frequencies
        prefix_sum_freq[0] = 1  # Initialize the frequency of prefix sum 0 as 1
        
        for num in nums:
            prefix_sum += num  # Calculate the running sum by adding the current number
            
            complement = prefix_sum - k  # Calculate the complement (prefix sum - k)
            count += prefix_sum_freq[complement]  # Add the frequency of the complement to the count
            
            prefix_sum_freq[prefix_sum] += 1  # Increment the frequency of the current prefix sum
        
        return count

        
        
        