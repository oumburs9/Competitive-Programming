# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

t = int(input().strip())
res = []

for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    # init the AND result with all bits set on
    target = (1 << 31) - 1

    for bit in range(30, -1, -1):
        opers = 0

        for i in range(n):
            if not (a[i] & (1 << bit)):
                opers += 1

        if opers <= k:
            k -= opers
        else:
            target &= ~(1 << bit)

    res.append(str(target))

print("\n".join(res))