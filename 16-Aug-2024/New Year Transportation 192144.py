# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

def can_reach(n, t, a):
    current_position = 1
    while current_position < t:
        current_position += a[current_position - 1]
    return current_position == t



#input
n, t = map(int, input().split())
a = list(map(int, input().split()))



# chec if can reach t
if can_reach(n, t, a):
    print("YES")
else:
    print("NO")