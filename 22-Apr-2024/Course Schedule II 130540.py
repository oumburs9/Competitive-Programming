# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [ [] for _ in range(numCourses)]
        incoming = [ 0 for _ in range(numCourses)]
        que = deque()
        res = []
# 
        for course, pre in prerequisites:
            graph[pre].append(course)

            incoming[course] += 1
        for course in range(numCourses):
            if incoming[course] == 0:
                que.append(course)
        
        while que:
            node = que.popleft()
            res.append(node)

            for nei in graph[node]:
                incoming[nei] -= 1

                if incoming[nei] == 0:
                    que.append(nei)

        return [] if len(res) != numCourses else res


 