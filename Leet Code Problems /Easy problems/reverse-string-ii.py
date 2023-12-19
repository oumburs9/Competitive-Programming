class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return ''
        if k == 0:
            return s
        
        s = list(s)
        ans = []
        for i in range(0, len(s), 2*k):
            s[i:i+k] = s[i+k-1:i-1:-1] if i - 1 > 0 else s[i+k-1::-1]
        
        
        return ''.join(s)


        