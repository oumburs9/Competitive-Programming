# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

test = int(input())
for _ in range(test):
    size = int(input())
    nums = list(map(int, input().split()))
    ans = max(nums)
    for ind in range(size - 1):
        maxNum = max(nums[ind], nums[ind + 1])
        ans = min(ans, maxNum)
    print(ans - 1)