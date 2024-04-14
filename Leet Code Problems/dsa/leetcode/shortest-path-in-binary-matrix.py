class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1

        q = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        direct = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, l = q.popleft()

            if r == N - 1 and c == N - 1:
                return l

            for newR, newC in direct:
                nr, nc = r + newR, c + newC
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    q.append((nr, nc, l + 1))
                    visited.add((nr, nc))
            # 
        return -1  