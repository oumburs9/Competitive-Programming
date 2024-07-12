# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        # init
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        # extract
        while k > 0 and min_heap :
            sum_val, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            k -= 1

            if j + 1 < len(nums2):
                    heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
