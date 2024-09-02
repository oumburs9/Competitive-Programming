# Problem: E - Good Will Hunting - https://codeforces.com/gym/545837/problem/E

l, r = map(int, input().split())

a = l ^ r

nums = list(bin(a)[2:])

if '1' not in nums:
    print(0)
else:
    idx = nums.index('1')
    for i in range(idx, len(nums)):
        nums[i] = '1'
        
    s = ''.join(nums)
    print(int(s, 2))
