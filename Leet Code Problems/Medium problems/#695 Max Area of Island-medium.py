class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):
            if not is_valid(r, c) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # Mark the cell as visited
            area = 1

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area

        