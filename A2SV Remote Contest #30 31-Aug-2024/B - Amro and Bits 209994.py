# Problem: B - Amro and Bits - https://codeforces.com/gym/545837/problem/B


t = int(input())

res = []

for _ in range(t):
    x = int(input())
    
    if x == 1:
        res.append(3)
        
    elif x % 2 == 1:
        res.append(1)
        
    elif (x & (x - 1)) == 0:
        res.append(x + 1)
        
    else:
        y = 1
        while x & y == 0:
            y <<=1
            
        res.append(y)

for r in res:
    print(r)