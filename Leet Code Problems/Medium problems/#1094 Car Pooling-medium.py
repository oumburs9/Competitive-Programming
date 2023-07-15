from ast import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        timeline = [0] * 1001  # Initialize timeline array

        # Update timeline based on passenger pickups and drop-offs
        for numPassengers, start, end in trips:
            timeline[start] += numPassengers
            timeline[end] -= numPassengers

        passengers = 0  

        # Check if the passenger count exceeds capacity at any point
        for count in timeline:
            passengers += count
            if passengers > capacity:
                return False

        return True

