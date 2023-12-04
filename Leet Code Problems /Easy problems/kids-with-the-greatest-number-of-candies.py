class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [ max(candies) <= n + extraCandies for n in candies]


        