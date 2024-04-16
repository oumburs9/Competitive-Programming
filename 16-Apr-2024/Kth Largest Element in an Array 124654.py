# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for i in range(k,len(nums)):
            if heap[0] < nums[i]:
                heappop(heap)
                heappush(heap,nums[i])
        return heap[0]