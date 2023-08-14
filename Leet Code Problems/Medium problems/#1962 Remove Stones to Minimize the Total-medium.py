import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest_pile = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -((largest_pile + 1) // 2))
        
        return -sum(max_heap)