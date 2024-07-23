# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

from heapq import heappop, heappush
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_end_times = [0] * n
        meeting_count = [0] * n

        meetings.sort()

        for start, end in meetings:
            earliest_end_time = float('inf')
            available_room = -1
            for room in range(n):
                if room_end_times[room] <= start:
                    available_room = room
                    break
                elif room_end_times[room] < earliest_end_time:
                    earliest_end_time = room_end_times[room]
                    available_room = room
            
            if room_end_times[available_room] <= start:
                room_end_times[available_room] = end
            else:
                room_end_times[available_room] += (end - start)
            
            meeting_count[available_room] += 1

        return meeting_count.index(max(meeting_count))
