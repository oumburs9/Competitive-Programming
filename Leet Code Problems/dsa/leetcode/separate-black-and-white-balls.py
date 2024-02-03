class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        zero_count = 0
        for c in reversed(s):
            if c == '0':
                zero_count += 1
            else:
                ans += zero_count
            
        return ans
            
        