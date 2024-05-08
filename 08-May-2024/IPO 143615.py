# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = sorted(zip(profits, capital), key=lambda x: x[1])
        
        max_heap = []
        cur = 0
        
        for _ in range(k):
            while cur < len(proj) and proj[cur][1] <= w:

                heapq.heappush(max_heap, -proj[cur][0])
                cur +=1
            
            if max_heap:
                w += -heapq.heappop(max_heap)

            else:

                break
        
        return w