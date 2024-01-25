class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        changes = [0] * (n + 1)
        for start, end, seats in bookings:
            changes[start - 1] += seats
            changes[end] -= seats

        current_bookings = list(accumulate(changes[:-1]))
        return current_bookings
        