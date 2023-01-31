class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic  = defaultdict(int)
        res, pL, sL = [], len(p), len(s)
        
        if pL > sL: return []
        
        for ch in p: dic[ch] += 1
            
        for i in range(pL-1):
            if s[i] in dic: dic[s[i]] -= 1
                
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in dic:
                dic[s[i]] += 1
            if i+pL < sL and s[i+pL] in dic: 
                dic[s[i+pL]] -= 1
            if all(v == 0 for v in dic.values()): 
                res.append(i+1)
                
        return res
        