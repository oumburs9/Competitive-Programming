# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
    
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        return (self.min_heap[0] - self.max_heap[0]) / 2.0

# Usage example:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
