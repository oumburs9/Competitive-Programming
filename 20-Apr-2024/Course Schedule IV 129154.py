# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def dfs_new(self, graph: List[List[int]], vis: List[bool], source: int, c: int):
        if source != c:
            graph[source][c] = 1
        if not vis[c]:
            vis[c] = True
            for i in range(len(graph[c])):
                if graph[c][i]:
                    if source != i:
                        graph[source][i] = 1
                    self.dfs_new(graph, vis, source, i)

    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[0] * n for _ in range(n)]

        for u, v in pre:
            graph[u][v] = 1

        for i in range(n):
            vis = [False] * n
            self.dfs_new(graph, vis, i, i)

        res = []
        for u, v in queries:
            res.append(graph[u][v])

        return res