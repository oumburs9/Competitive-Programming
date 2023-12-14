class FrequencyTracker:

    def __init__(self):
        self.freqDict = defaultdict(int) # number -> freq
        self.countDict = defaultdict(int) # freq -> count
        

    def add(self, number: int) -> None:
        freq = self.freqDict[number]
        self.freqDict[number] += 1

        self.countDict[freq] -= 1
        if self.countDict[freq] < 1:
            del self.countDict[freq]

        self.countDict[freq + 1] += 1

    def deleteOne(self, number: int) -> None:
        freq = self.freqDict[number]
        self.freqDict[number] -= 1
        if self.freqDict[number] < 1:
            del self.freqDict[number]

        self.countDict[freq] -= 1
        if self.countDict[freq] < 1:
            del self.countDict[freq]

        if freq > 1:
            self.countDict[freq - 1] += 1


    def hasFrequency(self, frequency: int) -> bool:
        return self.countDict[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)