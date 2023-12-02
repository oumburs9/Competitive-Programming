class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        dic = {index: letter for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}  
        res = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                res += dic[int(s[i] + s[i+1]) - 1]
                i += 3  
            else:
                res += dic[int(s[i]) - 1]
                i += 1
        return res

            
            
            
        