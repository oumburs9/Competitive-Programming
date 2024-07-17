# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess_table = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def solve(col_index):
            if col_index == n:
                res.append(["".join(row) for row in chess_table])
                return 
            
            for row_index in range(n):
                if is_place_valid(row_index,col_index):
                    chess_table[row_index][col_index] = 'Q'

                    solve(col_index + 1)  

                    chess_table[row_index][col_index] = '.'  # backtrack

        def is_place_valid(row_index, col_index):
            # col conf
            for i in range(col_index):
                if chess_table[row_index][i] == 'Q':
                    return False
            
            #  upper dia conf
            i, j = row_index, col_index
            while i >= 0 and j >= 0:
                if chess_table[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # lower diagonal conf
            i, j = row_index, col_index
            while i < n and j >= 0:
                if chess_table[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            return True

        solve(0)
        return res
