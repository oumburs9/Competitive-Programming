# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
seq = list(map(int, data[1:]))

s = 0
max_neg_odd = float('-inf')
min_pos_odd = float('inf')

for num in seq:
    if num > 0:
        s += num
    if num < 0 and num % 2 != 0:
        max_neg_odd = max(max_neg_odd, num)
    if num > 0 and num % 2 != 0:
        min_pos_odd = min(min_pos_odd, num)

if s % 2 == 0:
    if min_pos_odd != float('inf') and max_neg_odd != float('-inf'):
        s -= min(min_pos_odd, -max_neg_odd)
    elif min_pos_odd != float('inf'):
        s -= min_pos_odd
    elif max_neg_odd != float('-inf'):
        s -= -max_neg_odd

print(s)
