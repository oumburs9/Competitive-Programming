class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_sum = 0
        curr_sum = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                curr_sum += sum(grid[i][j:j+3]) + sum(grid[i+2][j:j+3]) + grid[i+1][j+1]

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    curr_sum = 0
                else:
                    curr_sum = 0

        return max_sum

        
        


        