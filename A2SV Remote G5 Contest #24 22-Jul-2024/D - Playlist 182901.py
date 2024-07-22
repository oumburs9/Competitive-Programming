# Problem: D - Playlist - https://codeforces.com/gym/536373/problem/D

import heapq

n, k = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]

songs.sort(key=lambda x: x[1], reverse=True)
# songs.sort(key=lambda x: -x[1])

max_pleasure = 0
current_sum_length = 0
min_heap = []

for length, beauty in songs:
    heapq.heappush(min_heap, length)
    
    current_sum_length += length
    
    if len(min_heap) > k:
        current_sum_length -= heapq.heappop(min_heap)
    
    if len(min_heap) <= k:
        max_pleasure = max(max_pleasure, current_sum_length * beauty)

print(max_pleasure)
