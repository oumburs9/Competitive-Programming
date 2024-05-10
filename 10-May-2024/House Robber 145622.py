# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def helper(i):
            #bc
            if i >= len(nums):
                return 0

            # ret if exi
            if i in memo:
                return memo[i]
            
            rob_curr = nums[i] + helper(i + 2)
            skip_curr = helper(i + 1)
            
            memo[i] = max(rob_curr, skip_curr)
            return memo[i]

        return helper(0)

        