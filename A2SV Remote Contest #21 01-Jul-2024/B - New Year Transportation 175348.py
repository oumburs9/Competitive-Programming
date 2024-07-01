# Problem: B - New Year Transportation - https://codeforces.com/gym/532332/problem/B

n,m = map(int, input().split())
_list = list(map(int, input().split()))

cur = 1

while cur < m:
    cur += _list[cur - 1]


if cur ==m:
    print("YES")
    
else:
    print("NO")
