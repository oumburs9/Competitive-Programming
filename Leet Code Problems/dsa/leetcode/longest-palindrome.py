class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        odd = 0
        result = 0
        for val in s_counter.values():
            if val % 2 == 0: 
                result += val
            else:
                odd = 1
                result += (val-1) 
        
        return result + odd








