class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[0])
        interval = points[0] # [1,6] -> [2,8]

        res = 0
        for i in range(1, len(points)):
            if points[i][0] <= interval[1]:
                interval[0] =  points[i][0] 
                interval[1] = min( points[i][1], interval[1]) # [2,_]
            else:
                interval[0] =  points[i][0] 
                interval[1] =  points[i][1]
                res += 1
        return res + 1
        


        