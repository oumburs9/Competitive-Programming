# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        
        def dfs(idx, cur_sum):
            # bc
            if idx == len(nums):
                return 1 if cur_sum == target else 0
            
            # rr
            if (idx, cur_sum) in memo:
                return memo[(idx, cur_sum)]
                
            add = dfs(idx + 1, cur_sum + nums[idx])
            sub = dfs(idx + 1, cur_sum - nums[idx])
            

            # mem / cache
            memo[(idx, cur_sum)] = add + sub

            return memo[(idx, cur_sum)]
        
        return dfs(0, 0)