# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [ None ] * (n + 1)
        def h(n):
            if n <= 2:
                return n

            if not dp[n]:
                dp[n] = h(n - 1) + h(n - 2)
                
            return dp[n]
        
        return h(n)