class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        while self.reqs and t - self.reqs[0] > 3000:
            self.reqs.pop(0)  
        self.reqs.append(t)
        return len(self.reqs)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)