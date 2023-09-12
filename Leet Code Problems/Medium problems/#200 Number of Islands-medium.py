class Solution:

    def inBound(self, row: int, col: int, grid: List[List[str]]) -> bool:
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        return True

    def getNeighbors(self, row: int, col: int, grid: List[List[str]]) -> List[Tuple[int]]:
        nbrs = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in directions:
            new_row, new_col = row + x, col + y
            if self.inBound(new_row, new_col, grid) and grid[new_row][new_col] == "1":
                nbrs.append((new_row, new_col))
        return nbrs

    def dfs(self, row: int, col: int, grid: List[List[str]]) -> None:
        grid[row][col] = "0"
        for nbr_row, nbr_col in self.getNeighbors(row, col, grid):
            self.dfs(nbr_row, nbr_col, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        count = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(row, col, grid)

        return count
