# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        ancestors = defaultdict(set)
        
        def dfs(node, origin):
            for neighbor in graph[node]:
                if origin not in ancestors[neighbor]:
                    ancestors[neighbor].add(origin)
                    dfs(neighbor, origin)
        
        for i in range(n):
            dfs(i, i)
        

        result = []
        for i in range(n):
            result.append(sorted(ancestors[i]))
        
        return result