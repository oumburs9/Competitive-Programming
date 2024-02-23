class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        res = [0]*n
        
        deck.sort()
        dq = deque([i for i in range(n)])

        for i in range(n):
            res[dq.popleft()] = deck[i]
            if dq:
                dq.append(dq.popleft())
        return res

        