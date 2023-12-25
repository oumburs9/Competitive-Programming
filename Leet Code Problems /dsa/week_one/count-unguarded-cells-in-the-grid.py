class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[1] * n for _ in range(m)]

        for x, y in guards:
            grid[x][y] = "G"

        for x, y in walls:
            grid[x][y] = "W"

        count = 0
        for x, y in guards:
            for j in range(x - 1, -1, -1):
                curr = grid[j][y]
                if curr == 'W' or curr == 'G':
                    break
                else:
                    grid[j][y] = 0

            for j in range(x + 1, m):
                curr = grid[j][y]
                if curr == 'W' or curr == 'G':
                    break
                else:
                    grid[j][y] = 0

            for j in range(y - 1, -1, -1):
                curr = grid[x][j]
                if curr == 'W' or curr == 'G':
                    break
                else:
                    grid[x][j] = 0

            for j in range(y + 1, n):
                curr = grid[x][j]
                if curr == 'W' or curr == 'G':
                    break
                else:
                    grid[x][j] = 0

        for row in grid:
            for j in row:
                if j == 1:
                    count += 1
        return count