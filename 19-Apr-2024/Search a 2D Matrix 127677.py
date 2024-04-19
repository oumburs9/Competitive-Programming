# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        r, c = len(matrix), len(matrix[0])
        l, r = 0, r * c - 1

        while l <= r:
            mid = (l + r) // 2
            mid_el = matrix[mid // c][mid % c]

            if mid_el == target:
                return True
            elif mid_el < target:
                l = mid + 1
            else:
                r = mid - 1

        return False