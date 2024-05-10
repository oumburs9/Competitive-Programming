# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        res = 0
        n = len(prices)
        
        # loop through prices
        for i in range(n):
            # update buy and sell
            if i < n-1 and prices[i] < prices[buy]:
                buy = i
                sell = i

            # update sell
            if i > 0 and prices[i] > prices[sell] :
                sell = i
            res = max(res, prices[sell] - prices[buy])
        return res
    


        