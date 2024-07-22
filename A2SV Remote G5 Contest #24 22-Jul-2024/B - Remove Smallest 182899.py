# Problem: B - Remove Smallest - https://codeforces.com/gym/536373/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    positive_nums = list(map(int,input().split()))
    
    positive_nums.sort()
    
    flag = True
    for i in range(n-1):
        # if abs(positive_nums[i+1] - positive_nums[i]) <= 1:
            # positive_nums.pop(0)
            # print(positive_nums)
        if abs(positive_nums[i+1] - positive_nums[i]) > 1:
            flag = False
            break
        
    if flag:
        print("YES")
    else:
        print("NO")