class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            
            horizontal_distance = abs(x2 - x1)
            vertical_distance = abs(y2 - y1)

            total_time += max(horizontal_distance, vertical_distance) 

        return total_time
