# Problem: A - Algorithm Test I - https://codeforces.com/gym/544347/problem/A

import math

n = int(input())
colors = list(map(int, input().split()))
unique_cnt = len(set(colors))

res = math.factorial(unique_cnt)

print(res)
