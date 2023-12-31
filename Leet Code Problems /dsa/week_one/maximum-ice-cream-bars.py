class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        _sum, count = 0, 0
        for i in range(len(costs)):
            _sum += costs[i]
            if _sum > coins:
                return count
            else:
                count += 1
        return count
        