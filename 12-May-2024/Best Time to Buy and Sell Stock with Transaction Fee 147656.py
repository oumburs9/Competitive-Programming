# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)

        def dfs(idx, holding):
            if idx == len(prices):
                return 0

            if (idx, holding) in memo:
                return memo[(idx, holding)]

            if not holding:
                do_nothing = dfs(idx + 1, False)
                buy = dfs(idx + 1, True) - prices[idx] - fee
                res = max(do_nothing, buy)
            else:
                do_nothing = dfs(idx + 1, True)

                sell = dfs(idx + 1, False) + prices[idx]
                res = max(do_nothing, sell)

            memo[(idx, holding)] = res
            return res

        return dfs(0, False)
        