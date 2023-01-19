from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minLen = float('inf')

        for r in range(len(nums)):
            
            curSum += nums[r]

            while curSum >= target and l <= r:

                minLen = min(minLen, (r - l)+1)
                if minLen == 1:
                    return 1
                curSum -= nums[l]
                l += 1

        return minLen if minLen != float('inf') else 0
        