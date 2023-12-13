class UndergroundSystem:

    def __init__(self):
        self.checkinDict = {} # id -> [stationName , t]
        self.totalDict = {} # startStation_endStation -> [total, count] 
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinDict[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation , time = self.checkinDict[id]
        keyPath = startStation + '_' + stationName

        if keyPath not in self.totalDict:
            self.totalDict[keyPath] = [0, 0]

        self.totalDict[keyPath][0] += t - time 
        self.totalDict[keyPath][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalDict[startStation + '_' + endStation]
        return total /count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)