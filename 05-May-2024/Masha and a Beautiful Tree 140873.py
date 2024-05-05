# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def solve(l, r):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    mal = max(arr[l:mid])
    mar = max(arr[mid:r])
    
    ans = 0
    if mal > mar:
        ans += 1
        arr[l:mid], arr[mid:r] = arr[mid:r], arr[l:mid]
    return solve(l, mid) + solve(mid, r) + ans

def main():
    t = int(input())
    for _ in range(t):
        m = int(input())
        global arr 
        
        arr = list(map(int, input().split()))
        ans = solve(0, m)
        
        if sorted(arr) == arr:
            print(ans)
        else:
            print(-1)

if __name__ == "__main__":
    main()
