class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        res = [0] * (n + 1)  
        
        for start, end, direction in shifts:
            if direction == 1:  
                res[start] += 1
                res[end + 1] -= 1
            else: 
                res[start] -= 1
                res[end + 1] += 1
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        result = ""
        for i, c in enumerate(s):
            shift = (ord(c) - 97 + res[i]) % 26  
            shifted_char = chr(shift + 97)  
            result += shifted_char  
        
        return result 

