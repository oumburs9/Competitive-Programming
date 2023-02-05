from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        maxPrefixSum = 0
        
        for i in range(len(gain)):
            total += gain[i]
            maxPrefixSum = max(maxPrefixSum,total)
        return maxPrefixSum
        