class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen , startWindow, hashMap = 0 ,0, {}
        
        for endWindow in range(len(s)):
            if s[endWindow] in hashMap:
                startWindow = max(startWindow,hashMap[s[endWindow]]+1)
            hashMap[s[endWindow]]= endWindow
            
            maxLen = max(maxLen,endWindow - startWindow + 1)
        return maxLen
        