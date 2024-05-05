# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def is_power_of_two(number):
    return number != 0 and (number & (number - 1)) == 0

def calc_y(n):
    b = bin(n)[2:]  
    b = '0' * (32 - len(b)) + b  
    

    ans = ['0'] * len(b)  
    

    for i in range(31, -1, -1):
        if b[i] == '1':
            ans[i] = '1'
            break

    if is_power_of_two(n):
        for i in range(len(b) - 1, 1, -1):
            if b[i] == '0':
                ans[i] = '1'
                break

    return int(''.join(ans), 2)


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(calc_y(n))

for r in res:
    print(r)


