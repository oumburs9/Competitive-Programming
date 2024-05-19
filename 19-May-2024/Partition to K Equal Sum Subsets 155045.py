# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        n = len(nums)
        nums.sort(reverse=True)
        dp = [-1] * (1 << n)  
        dp[0] = 0

        for mask in range(1 << n):  
            if dp[mask] == -1:
                continue
            for i in range(n):
                if not (mask & (1 << i)) and dp[mask] + nums[i] <= target:
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target
                    if dp[-1] == 0:  
                        return True
        return dp[-1] == 0