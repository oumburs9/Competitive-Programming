# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l_day = days[-1]
        t_days = set(days)


        dp = [0] * (l_day + 1)
        
        for i in range(1, l_day + 1):
            if i not in t_days:
                dp[i] = dp[i - 1]
                
            else:
                cost1 = dp[i - 1] + costs[0]

                cost7 = dp[i - 7] + costs[1] if i >= 7 else costs[1]
                cost30 = dp[i - 30] + costs[2] if i >= 30 else costs[2]
                
                dp[i] = min(cost1, cost7, cost30)
        
        return dp[l_day]