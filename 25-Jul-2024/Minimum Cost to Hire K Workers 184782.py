# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        combined = sorted([(wage[ind]/quality[ind], quality[ind], wage[ind]) for ind in range(len(wage))])
        minHeap = []
        ans = float('inf')
        currQuality = 0
        for ind in range(len(wage)):
            rate, qual, wage = combined[ind]
            heapq.heappush(minHeap, -qual)
            currQuality += qual
            if len(minHeap) == k:
                q = heapq.heappop(minHeap)
                ans = min(ans, currQuality * rate)
                currQuality += q
        return ans