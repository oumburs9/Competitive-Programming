class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxRow = [0] * rows
        maxCol = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                maxRow[i] = max(maxRow[i], grid[i][j])
                maxCol[j] = max(maxCol[j], grid[i][j])
        

        totalDiff = 0 
        for i in range(rows):
            for j in range(cols):
                totalDiff += min(maxRow[i], maxCol[j]) - grid[i][j]
        
        return totalDiff