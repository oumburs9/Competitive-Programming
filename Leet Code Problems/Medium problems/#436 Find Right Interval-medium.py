from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        n = len(intervals)
        # Create a sorted list of start, index tuples to make searching easy
        starts = [(interval[0], i) for i, interval in enumerate(intervals)]
        starts.sort()

        result = [-1] * n

        for i, interval in enumerate(intervals):
            end = interval[1]
            right_idx = -1

            # the right interval index using bs
            index = binary_search(starts, end)
            if index < n:
                right_idx = starts[index][1]

            result[i] = right_idx

        return result
 