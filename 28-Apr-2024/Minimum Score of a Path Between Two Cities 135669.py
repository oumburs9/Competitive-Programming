# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        min_score = float('inf')
        for road in roads:
            self.union(road[0], road[1])
        for road in roads:
            if self.find(1) == self.find(road[0]) == self.find(road[1]):
                min_score = min(min_score, road[2])
        return min_score
