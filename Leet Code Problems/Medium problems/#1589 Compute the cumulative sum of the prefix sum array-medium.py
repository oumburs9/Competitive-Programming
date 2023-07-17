class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)  # Initialize the prefix sum array with zeros

        # Compute the frequency of each index in requests
        for start, end in requests:
            prefixSum[start] += 1
            prefixSum[end + 1] -= 1

        # Compute the cumulative sum of the prefix sum array
        for i in range(1, n + 1):
            prefixSum[i] += prefixSum[i - 1]

        prefixSum.sort(reverse=True)  # Sort the prefix sum array in descending order
        nums.sort(reverse=True)  # Sort the nums array in descending order

        result = 0
        mod = 10**9 + 7

        # Compute the maximum sum by multiplying prefix sum and nums elements
        for p, num in zip(prefixSum, nums):
            result = (result + p * num) % mod

        return result
