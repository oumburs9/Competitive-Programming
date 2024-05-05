# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def trial_division_simple(n: int):
    factorization = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.add(d)
            n //= d
        d += 1
    if n > 1:
        factorization.add(n)

    return factorization
cnt = 0
n = int(input())
for i in range(1,n+1):
    res = trial_division_simple(i)
    if len(res) == 2:
        cnt += 1
print(cnt)