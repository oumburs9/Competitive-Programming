# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        res = 0
        heap = [-p  for p in piles ]

        heapify(heap)
        for _ in range(k):
            p = heappop(heap)
            heappush(heap, p//2)
            
        for h in heap:
            res += -h

        return res
        
        