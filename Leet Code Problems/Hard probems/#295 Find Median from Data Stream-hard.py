class MedianFinder:

    def __init__(self):
        # Initialize two pointers and a list to store the data.
        self.data = []
        self.left = 0
        self.right = -1

    def addNum(self, num: int) -> None:
        # Insert the number in the correct position using two pointers.
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.data[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        self.data.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            # If the number of elements is even, return the average of the middle elements.
            return (self.data[mid] + self.data[mid - 1]) / 2.0
        else:
            # If the number of elements is odd, return the middle element.
            return float(self.data[mid])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()