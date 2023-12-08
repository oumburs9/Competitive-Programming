class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        res = ''
        j = 0
        for i in range(len(spaces)):
            res += s[j:spaces[i]] + " "
            j = spaces[i]
        res += s[j:] 
        return res



        
        