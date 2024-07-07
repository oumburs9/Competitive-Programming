# Problem: Honest Coach - https://codeforces.com/problemset/problem/1360/B

t = int(input()) 

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))  # Strengths of the athletes

    for i in range(n):
        for j in range(0, n-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]

    min_diff = 1001 

    for i in range(1, n):
        diff = s[i] - s[i-1]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)