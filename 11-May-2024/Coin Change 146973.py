# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        def dp(a):
            # bc
            if a == 0:
                return 0 
            if a < 0:
                return float('inf')
            
            if a in memo:
                return memo[a]
            
            # rr
            min_coins = float('inf')
            for c in coins:
                res = dp(a - c)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            
            memo[a] = min_coins # cache
            return memo[a]

        res = dp(amount)
        return res if res !=float('inf') else -1

        