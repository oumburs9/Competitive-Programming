# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}  

        def dp(i, holding):
            if i >= n:
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                sell = prices[i] + (dp(i + 2, False) if i + 2 < n else 0)
                not_sell = dp(i + 1, True)

                res = max(sell, not_sell)
            else:
                buy = -prices[i] + dp(i + 1, True)
                not_buy = dp(i + 1, False)
                
                res = max(buy, not_buy)

            memo[(i, holding)] = res
            return res

        return dp(0, False)
