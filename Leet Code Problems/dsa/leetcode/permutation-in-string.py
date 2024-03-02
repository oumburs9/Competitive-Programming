class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1freq = [0] * 26
        s2freq = [0] * 26
        
        for i in range(len(s1)):
            s1freq[ord(s1[i]) - ord('a')] += 1
            s2freq[ord(s2[i]) - ord('a')] += 1
        
        count = 0
        for i in range(26):
            if s1freq[i] == s2freq[i]:
                count += 1
        
        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')
            
            if count == 26:
                return True
            
            s2freq[r] += 1
            if s2freq[r] == s1freq[r]:
                count += 1
            elif s2freq[r] == s1freq[r] + 1:
                count -= 1
            
            s2freq[l] -= 1
            if s2freq[l] == s1freq[l]:
                count += 1
            elif s2freq[l] == s1freq[l] - 1:
                count -= 1
        
        return count == 26
        