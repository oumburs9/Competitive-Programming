class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        startWindow , maxLen , maxRepeatChar, fMap = 0, 0, 0 ,{}
        
        for endWindow in range(len(s)):
            if s[endWindow] not in fMap:
                fMap[s[endWindow]] = 0
            fMap[s[endWindow]] += 1
            
            maxRepeatChar = max(maxRepeatChar,fMap[s[endWindow]])
            
            
            if (endWindow - startWindow + 1 -maxRepeatChar) > k:
                fMap[s[startWindow]] -= 1
                startWindow += 1
            maxLen = max(maxLen,endWindow - startWindow + 1)
        return maxLen
        