# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = sorted([  (e, p, i) for i, (e, p) in enumerate(tasks)  ])
        que = []
        res = []
        t, i, n = 0, 0, len(tasks)
        
        while i < n or que:
            if not que:
                t = max(t, tasks[i][0] )

            while i < n and tasks[i][0] <= t:
                heapq.heappush(que, (tasks[i][1], tasks[i][2]))
                i += 1

            p, idx = heapq.heappop(que)
            t += p
            res.append(idx)
        
        return res