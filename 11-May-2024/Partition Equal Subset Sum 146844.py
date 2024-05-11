# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        t = s // 2
        memo = {}  # 

        def dp(i, cs):  # dp function for i --> 'depth' and cs __>'current sum'
            if cs == t:
                return True

            if i >= len(nums) or cs > t:
                return False

            if (i, cs) in memo:
                return memo[(i, cs)]
             
            memo[(i, cs)] = dp(i + 1, cs + nums[i]) or dp(i + 1, cs)
           
            return memo[(i, cs)]

        return dp(0, 0)