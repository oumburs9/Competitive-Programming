# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

import sys
from collections import deque, defaultdict

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
a = int(data[2])

b = int(data[3])

graph = defaultdict(list)

index = 4
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

queue = deque([a])
visited = {a}
parent = {a: None}
found = False

while queue:
    current = queue.popleft()
    if current == b:
        found = True
        break
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

if not found:
    print(-1)
else:
    path = []
    step = b
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()
    
    l = len(path) - 1
    print(f"{l}")
    print(" ".join(map(str, path)))
