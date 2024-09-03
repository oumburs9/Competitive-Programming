# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, x):
        # Path comp
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        # Count uniq r
        unique_roots = len(set(uf.find(i) for i in range(n)))
        
        return unique_roots
