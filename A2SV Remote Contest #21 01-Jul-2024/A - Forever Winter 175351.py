# Problem: A - Forever Winter - https://codeforces.com/gym/532332/problem/A

inp = int(input())

for i in range(inp):
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    
    for j in range(m):
        x, y = map(int, input().split())
        l[x] += 1
        l[y] += 1
    
    z = l.count(1)
    X = n - z - 1
    
    print(X, z // X)