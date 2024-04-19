# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]

        heapify(heap)

        while len(heap) > 1:
            largest = -heappop(heap)
            sLargest = -heappop(heap)
            diff = largest - sLargest
            heappush(heap,-diff)
        if heap:
            return -heappop(heap)
        return 0
        