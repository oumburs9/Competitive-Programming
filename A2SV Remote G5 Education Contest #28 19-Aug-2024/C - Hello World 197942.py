# Problem: C - Hello World - https://codeforces.com/gym/543262/problem/C

t = int(input())
res = []

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split())  )
    c.sort()

    if c[0] != 1:
        res.append("NO")
    else:
        s = 1  # Start with a sum of 1
        ok = True
        for i in range(1, n):
            if c[i] > s:
                ok = False
                break
            s += c[i]
        
        if ok:
            res.append("YES" )
        else:
            res.append("NO" )

for r in res:
    print(r)
