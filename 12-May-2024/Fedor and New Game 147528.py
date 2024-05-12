# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())

players = [int(input()) for _ in range(m + 1)]

fe = players[-1]


count = 0
for p in players[:-1]:
    if bin(p ^ fe).count('1') <= k:
        count += 1



print(count)