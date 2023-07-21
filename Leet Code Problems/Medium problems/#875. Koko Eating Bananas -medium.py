from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(piles, capacity, h):
            hours_needed = 0
            
            for pile in piles:
                hours_needed += (pile + capacity - 1) // capacity
            
            return hours_needed <= h

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
