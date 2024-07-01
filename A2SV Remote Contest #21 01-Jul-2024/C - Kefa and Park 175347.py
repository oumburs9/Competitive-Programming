# Problem: C - Kefa and Park - https://codeforces.com/gym/532332/problem/C

import sys
from collections import defaultdict, deque

input = sys.stdin.read
_list = input().split()

idx = 0
n = int(_list[idx])
m = int(_list[idx + 1])

idx += 2

cats = list(map(int, _list[idx:idx + n]))
idx += n

edges = []
for _ in range(n - 1):
    u = int(_list[idx])
    v = int(_list[idx + 1])
    edges.append((u, v))
    idx += 2

tree = defaultdict(list)
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (n + 1)
valid_rest = 0

stack = [(1, 0, 0)]

while stack:
    node, conse_cats, parent = stack.pop()

    if visited[node]:
        continue

    visited[node] = True

    if cats[node - 1] == 1:
        conse_cats += 1
    else:
        conse_cats = 0

    if conse_cats > m:
        continue

    is_lf = True

    for neighbor in tree[node]:
        if not visited[neighbor] and neighbor != parent:
            is_lf = False
            stack.append((neighbor, conse_cats, node))

    if is_lf:
        valid_rest += 1

print(valid_rest)