class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_freq = defaultdict(int)
        prefix_sum_freq[0] = 1
        
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            count += prefix_sum_freq[complement]
            prefix_sum_freq[prefix_sum] += 1
        
        return count
