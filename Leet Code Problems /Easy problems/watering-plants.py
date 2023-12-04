class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        c = capacity

        for i in range(len(plants)):
            if c < plants[i]:
                steps += 2*i
                c = capacity
                
            c -= plants[i]
            steps += 1
        return steps


        