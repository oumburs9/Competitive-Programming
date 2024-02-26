class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n =len(costs)
        costA = sorted(costs,key=lambda x: x[0]-x[1])
        res = 0
        for i in range(n//2):
            res += costA[i][0]
            res += costA[n-i-1][1]
        return res

