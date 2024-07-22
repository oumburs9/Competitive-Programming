# Problem: A - Hit the Lottery - https://codeforces.com/gym/536373/problem/A

n = int(input())

denoms = [100, 20, 10, 5,1]

cnt = 0

for denom in denoms:
    cnt += n//denom
    
    n %= denom
    
print(cnt)