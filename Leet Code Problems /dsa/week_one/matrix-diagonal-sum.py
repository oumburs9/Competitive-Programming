class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        rows = len(mat)
        # primary diagonal (1,1) , (2,2)
        r, c = 0, 0
        priSum = 0
        while r < rows:
            priSum += mat[r][c]
            r += 1
            c += 1


        # secondary diagonal (r,0) -> (r-1,0+1)
        r, c = rows-1, 0
        secSum = 0
        while 0 <= r:
            secSum += mat[r][c]
            r -= 1
            c += 1

        
        #  removing the commmon element for the two diagonal if n is odd
        mid = 0
        if rows % 2 != 0:
            idx = rows//2 
            mid = mat[idx][idx]

        return priSum + secSum - mid


        