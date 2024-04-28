# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])
        
        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)
            
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
        
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((manhattan_distance(points[i], points[j]), i, j))
        
        edges.sort()  # Sort edges by weight
        
        parent = list(range(n))
        rank = [0] * n
        mst_weight = 0
        num_edges_added = 0
        
        for edge in edges:
            weight, u, v = edge
            u_root = find(parent, u)
            v_root = find(parent, v)
            
            if u_root != v_root: 
                mst_weight += weight
                union(parent, rank, u_root, v_root)
                num_edges_added += 1
                
                if num_edges_added == n - 1: 
                    break
        
        return mst_weight
