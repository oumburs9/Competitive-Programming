import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        
       
        for row in matrix:
            heapq.heappush(min_heap, (row[0], 0, row))
        
       
        for _ in range(k - 1):
            val, col, row = heapq.heappop(min_heap)
            if col + 1 < len(row):
                heapq.heappush(min_heap, (row[col + 1], col + 1, row))
        
        return min_heap[0][0]