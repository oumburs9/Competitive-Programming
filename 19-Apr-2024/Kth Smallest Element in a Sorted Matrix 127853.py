# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heap.extend(matrix[i])
        
        heapify(heap)
        i = 0
        res = 0
        while i != k:
            res = heappop(heap)
            i += 1
        return res


        



        