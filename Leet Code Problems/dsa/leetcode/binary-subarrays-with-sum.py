class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_freq = defaultdict(int)
        prefix_sum_freq[0] = 1
        
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - goal
            count += prefix_sum_freq[complement]
            prefix_sum_freq[prefix_sum] += 1
        
        return count
