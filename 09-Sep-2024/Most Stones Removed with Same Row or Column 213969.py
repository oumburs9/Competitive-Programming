# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        uf = UnionFind()
        
        for x, y in stones:
            uf.add(x)
            uf.add(y + 10001)  
            uf.union(x, y + 10001)
        
        unique_roots = len(set(uf.find(x) for x, _ in stones))
        return len(stones) - unique_roots


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0