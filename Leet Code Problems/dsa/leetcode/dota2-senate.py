class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        kD = 0
        kR = 0

        queue = deque()
        for s in senate:
            if queue:
                if queue[-1] != s:
                    if kD > 0 or kR > 0:
                        if s == 'R':
                            kD -= 1
                        else:
                            kR -= 1
                        continue
                    else:
                        queue.popleft()
            queue.append(s)
            if s == 'R':
                kR += 1
            elif s == 'D':
                kD += 1
        kD = 0
        kR = 0

        x = ''.join(queue)
        queue2 = deque()
        for s in x:
            if queue2:
                if queue2[-1] != s:
                    if kD > 0 or kR > 0:
                        if s == 'R':
                            kD -= 1
                        else:
                            kR -= 1
                        continue
                    else:
                        queue2.popleft()
            queue2.append(s)
            if s == 'R':
                kR += 1
            elif s == 'D':
                kD += 1

        return 'Dire' if "D" in set(queue2) else "Radiant"
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))
        
        return "Radiant" if R else "Dire"
        