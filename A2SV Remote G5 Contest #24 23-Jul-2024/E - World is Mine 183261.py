# Problem: E - World is Mine - https://codeforces.com/gym/536373/problem/E

from collections import Counter
import heapq

# Accepting the input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    counter = Counter(arr)
    # It will contain a list of tastiness values and the number of cakes.
    cakes = []
    for tastiness in counter:
        cakes.append([tastiness, counter[tastiness]])
    
    cakes.sort()
    total_cakes_eaten_by_bob = 0
    cakes_eaten_by_bob = []
    for i in range(len(cakes)):
        # How many turns Bob will take if he eats the current tastiness.
        bob_turns = total_cakes_eaten_by_bob + cakes[i][1]
        # How many turns Alice will take to eat all the previous cakes that were not eaten by Bob.
        alice_turns = i - len(cakes_eaten_by_bob)
        
        # Bob eating the cakes of the current tastiness.
        total_cakes_eaten_by_bob += cakes[i][1]
        heapq.heappush(cakes_eaten_by_bob, -cakes[i][1])
        
        # Checking if Bob eats a cake he should not have eaten because Alice reaches one of the cakes.
        if bob_turns > alice_turns:
            # Removing (vomiting ) the cake we ate before which had a higher quantity.
            total_cakes_eaten_by_bob += heapq.heappop(cakes_eaten_by_bob)
    
    # To determine the number of cakes eaten by Alice, subtract the number of unique tastiness values
    # eaten by Bob from the total number of unique tastiness values.
    print(len(cakes) - len(cakes_eaten_by_bob))
