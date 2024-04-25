# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def get_sum_of_factors(self, n: int) -> int:
        divisor = 2
        ans = 0
        while n > 1:
            if n % divisor == 0:
                ans += divisor
                n //= divisor
            else:
                divisor += 1
        return ans

    def smallestValue(self, n: int) -> int:
        while True:
            sum_of_factors = self.get_sum_of_factors(n)
            if n == sum_of_factors:
                break
            n = sum_of_factors
        return n