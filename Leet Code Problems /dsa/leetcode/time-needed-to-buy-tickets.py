class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dq = deque([ (i,v) for i,v in enumerate(tickets) ])
        secs = 0

        while True:
            i, v = dq.popleft()
            secs += 1

            if i == k and v -1 == 0:
                return secs
            
            if v - 1 > 0:
                dq.append((i,v-1))




        