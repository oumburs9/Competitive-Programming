# Problem: E - Office Keys - https://codeforces.com/gym/543262/problem/E

n, k, room = list(map(int, input().split()))
people = sorted(list(map(int, input().split())))
keys = sorted(list(map(int, input().split())))

def can_reach(time):
    j = 0
    for i in range(n):
        
        while j < k and abs(keys[j] - people[i]) + abs(keys[j] - room) > time:
            j += 1
        if j == k:
            return False
        j += 1 
    return True

l = 0
r = int(1e18)

while l < r:
    mid = (l + r) // 2
    if can_reach(mid):
        r = mid
    else:
        l = mid + 1

print(l)
