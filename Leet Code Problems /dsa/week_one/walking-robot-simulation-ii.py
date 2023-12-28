class Robot:

    def __init__(self, width: int, height: int):
        self.perimeter = 2 * width + 2 * (height - 2)
        self.position = 0
        self.at_start = True

        self.bottom_right = width - 1
        self.top_right = self.bottom_right + (height - 1)
        self.top_left = self.top_right + (width - 1)

    def step(self, num: int) -> None:
        self.at_start = False
        self.position = (self.position + num) % self.perimeter

    def getPos(self) -> List[int]:
        if 0 <= self.position <= self.bottom_right:
            return [self.position, 0]

        if self.bottom_right < self.position <= self.top_right:
            return [self.bottom_right, self.position - self.bottom_right]

        if self.top_right < self.position <= self.top_left:
            return [self.bottom_right - (self.position - self.top_right), self.top_right - self.bottom_right]

        return [0, self.top_right - self.bottom_right - (self.position - self.top_left)]

    def getDir(self) -> str:
        if self.at_start or 0 < self.position <= self.bottom_right:
            return 'East'

        if self.bottom_right < self.position <= self.top_right:
            return 'North'

        if self.top_right < self.position <= self.top_left:
            return 'West'

        return 'South'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()