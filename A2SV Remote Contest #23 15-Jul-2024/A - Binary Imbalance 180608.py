# Problem: A - Binary Imbalance - https://codeforces.com/gym/535309/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    zeros = s.count('0')
    ones = s.count('1')
    
    if zeros > ones:
        print('YES')
    else:
        flag = False
        for j in range(n-1):
            if s[j] != s[j+1]:
                flag = True
                break
        if flag:
            print("YES")
        else:
            print("NO")