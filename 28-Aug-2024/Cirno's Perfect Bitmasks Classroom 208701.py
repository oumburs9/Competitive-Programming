# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
res = []

for _ in range(t):
    n = int(input())
    b = bin(n)[2:]
    b = '0' * (32 - len(b)) + b
    
    ans = ['0'] * len(b)
    
    for i in range(31, -1, -1):
        if b[i] == '1':
            ans[i] = '1'
            break
    
    if n != 0 and (n & (n - 1)) == 0:
        for i in range(len(b) - 1, 1, -1):
            if b[i] == '0':
                ans[i] = '1'
                break
    
    y = int(''.join(ans), 2)
    res.append(y)

for r in res:
    print(r)
