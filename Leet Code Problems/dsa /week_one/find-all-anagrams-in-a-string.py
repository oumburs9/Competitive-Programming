class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k= len(p)
        window = Counter(s[:k])
        target = Counter(p)

        startWin = 0
        res = []

        for endWin in range(k,len(s)):
            if window == target:
                res.append(startWin)

            window[s[startWin]] -= 1
            if window[s[startWin]] ==0:
                del window[s[startWin]]
            startWin +=1
            if s[endWin] not in window:
                window[s[endWin]] = 1
            else:
                window[s[endWin]] +=1
        if window == target:
            res.append(startWin)
        return res
            


            



        
        

        