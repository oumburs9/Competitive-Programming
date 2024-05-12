# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engrs = list(zip(speed, efficiency)) # pairing sp and eff
        engrs.sort(key=lambda x: x[1], reverse=True)
        
        max_perform =0
        cur_speed_sum = 0
        speed_heap = []
        
        for cur_speed, cur_efficiency in engrs:

            heapq.heappush(speed_heap, cur_speed)

            cur_speed_sum += cur_speed # currrent sum of speed


            if len(speed_heap) > k:
                cur_speed_sum -= heapq.heappop(speed_heap)
            
            cur_perform = cur_speed_sum * cur_efficiency
            max_perform = max(max_perform, cur_perform)
        return max_perform % MOD
        