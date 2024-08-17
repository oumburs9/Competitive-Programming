# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
    def isCycleUtil(self, u, par, adj, vis):
        vis[u] = True


        for v in adj[u]:
            if v == par:
                continue
            elif vis[v]:
                return True
            elif self.isCycleUtil(v, u, adj, vis):
                return True
        return False
        
    def isCycle(self, V, adj):
        vis = [False] * V
        for i in range(V):
            if not vis[i] and self.isCycleUtil(i, -1, adj, vis):
                return True
        return False