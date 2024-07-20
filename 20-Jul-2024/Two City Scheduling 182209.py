# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n =len(costs) // 2
        costA = sorted(costs,key=lambda x: x[0]-x[1])
        
        res = 0
        for i in range(n):
            res += costA[i][0]

        for i in range(n,n*2):
            res += costA[i][1]
            
        return res

