class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        minLen = min(len(word2),len(word1))
        index = 0 

        for i in range(minLen):
            res += word1[index]
            res += word2[index]
            index +=1

        if len(word1) != minLen:
            res += word1[index :]
        else:
            res += word2[index :]
            
        return res
        