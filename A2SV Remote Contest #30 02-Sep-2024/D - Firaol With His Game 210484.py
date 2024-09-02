# Problem: D - Firaol With His Game - https://codeforces.com/gym/545837/problem/D

import heapq


t = int(input())

for _ in range(t):
    challanges, time = map(int, input().split())
    times = list(map(int, input().split()))
    total = sum(times)

    if time >= total:
        print(0)
        continue
    curr = 0
    heap = []
    ans = 0

    for ind in range(challanges):
        t = times[ind]
        curr += t
        heapq.heappush(heap, (-t, ind))
        if curr > time:
            timeTaken, ind = heapq.heappop(heap)
            ans = ind + 1
            break

    print(ans)
