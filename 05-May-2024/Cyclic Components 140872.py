# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

import sys
from collections import defaultdict, deque

def find_cycle_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)  #visited nodes
    cycle_count = 0
    
    def is_cycle_component(node):
        queue = deque([node])
        visited[node] = True
        
        local_visited = {node}
        num_edges = 0
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                num_edges += 1
                if not visited[neighbor]:
                    visited[neighbor] = True
                    local_visited.add(neighbor)
                    queue.append(neighbor)
        
        num_edges //= 2 
        if num_edges == len(local_visited) and all(len(graph[v]) == 2 for v in local_visited):
            return True
        return False

    for i in range(1, n + 1):
        if not visited[i]:
            if i in graph and is_cycle_component(i):
                cycle_count += 1
            else:
                visited[i] = True

    return cycle_count


input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
edges = []

index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    edges.append((u, v))
    index += 2

print(find_cycle_components(n, edges))


