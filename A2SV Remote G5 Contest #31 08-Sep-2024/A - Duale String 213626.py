# Problem: A - Duale String - https://codeforces.com/gym/547609/problem/A

test  = int(input())

for _ in range(test):
    _str = input().strip()
    
    n =  len(_str)
    
    # if odd
    if n% 2 == 1:
        print('NO')
    else:
        if _str[:n//2] == _str[n//2:]:
            print('YES')
        else:
            print('NO')