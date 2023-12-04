class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination , start
        clockwiseDis = sum(distance[start:destination])
       
        return min(clockwiseDis, sum(distance) - clockwiseDis)
  

        