# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        def get_coord(s):
            q, r = divmod(s-1, n)
            row = n - 1 - q
            col = r if row % 2 != n % 2 else n - 1 - r
            
            return row, col




        target = n*n
        que = deque([(1, 0)]  )
        visited = set([1])
        
        while que:
            current, dist = que.popleft()

            if current == target:
                return dist

            for step in range(1, 7):
                next_square = current + step

                if next_square > target:
                    continue

                row, col = get_coord(next_square)

                if board[row][col] != -1:
                    next_square = board[row][col]

                if next_square not in visited:
                    visited.add(next_square)
                    que.append((next_square, dist + 1))

        
        return -1