# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cntStations = len(gas)
        begin = 0

        current = begin
        cntVisited = 0
        fuel = 0

        while cntVisited < cntStations:
            residual = fuel + gas[current] - cost[current]

            if residual >= 0:
                fuel += gas[current] - cost[current]
                current = (current + 1) % cntStations
            else:
                begin = (begin - 1 + cntStations) % cntStations
                fuel += gas[begin] - cost[begin]

            cntVisited += 1

        return begin if fuel >= 0 else -1