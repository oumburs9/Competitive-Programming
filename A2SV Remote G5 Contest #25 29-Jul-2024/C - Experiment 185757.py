# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C

n = int(input())
experiments = []
for _ in range(n):
    si, ti, bi = map(int, input().split())
    experiments.append((si, ti, bi))


events = []
for exp in experiments:
    start, end, rooms = exp
    
    events.append((start, rooms))  
    events.append((end + 1, -rooms))

events.sort()

max_rooms = 0
current_rooms = 0

for event in events:
    time, room_change = event
    current_rooms += room_change
    if current_rooms > max_rooms:
        max_rooms = current_rooms

print(max_rooms)

