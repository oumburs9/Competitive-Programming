class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)


# class Solution:
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]

#     def solution(self, board, word, x, y, cur):
#         if(x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == ' '):
#             return False
#         cur += board[x][y]

#         if(len(cur) > len(word)):
#             return False
#         if(cur[len(cur)-1] != word[len(cur)-1]):
#             return False
#         if(cur == word):
#             return True

#         temp = board[x][y]
#         board[x][y] = ' '

#         for i in range(4):
#             if(self.solution(board, word, x+self.dx[i], y+self.dy[i], cur)):
#                 return True

#         board[x][y] = temp
#         return False

#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if(len(word) == 0):
#             return True
#         n = len(board)
#         for i in range(n):
#             m = len(board[i])
#             for j in range(m):
#                 if(word[0] == board[i][j] and self.solution(board, word, i, j, "")):
#                     return True
#         return False