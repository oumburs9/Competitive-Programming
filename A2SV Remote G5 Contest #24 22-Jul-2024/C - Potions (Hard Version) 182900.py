# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq
n = int(input())
potions = list(map(int, input().split()))

health = 0
cnt  = 0
min_heap = []

for i in range(n):
    if potions[i] >= 0:
        health += potions[i]
        cnt += 1
    else:
        if potions[i] + health >= 0:
            health += potions[i]
            cnt += 1
            heapq.heappush(min_heap,potions[i])
        elif min_heap and min_heap[0] < potions[i]:
            health -= heapq.heappop(min_heap)
            health += potions[i]
            heapq.heappush(min_heap,potions[i])
            
print(cnt)