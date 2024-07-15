# Problem: C - The Lakes - https://codeforces.com/gym/535309/problem/C

def dfs(r, c, grid):
    stack = [(r, c)]
    volume = grid[r][c]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    grid[r][c] = 0
    
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0:
                volume += grid[nx][ny]
                grid[nx][ny] = 0
                stack.append((nx, ny))
    
    return volume

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for r in range(n):
        x = list(map(int, input().split()))
        for c in range(m):
            grid[r][c] = x[c]
    
    volume = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] != 0:
                volume = max(volume, dfs(r, c, grid))
    
    print(volume)
