class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value  # Value to compare against
        self.k = k  
        self.queue = deque()
        self.counter = {}
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.counter[num] = self.counter.get(num, 0) + 1

        self.queue.append(num)
        if len(self.queue) > self.k:
            oldest = self.queue.popleft()
            if oldest == self.value:
                self.counter[oldest] -= 1
                if self.counter[oldest] == 0:
                    del self.counter[oldest]

        return self.counter.get(self.value, 0) == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

