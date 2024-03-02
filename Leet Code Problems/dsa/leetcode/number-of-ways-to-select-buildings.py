class Solution:
    def numberOfWays(self, s: str) -> int:
        res = 0
        n = len(s)

        prefix_zeros = [0] * n
        prefix_ones = [0] * n
        
        for i in range(n):
            ch = s[i]
            if i == 0:

                prefix_zeros[i] = 1 if ch == '0' else 0
                prefix_ones[i] = 1 if ch == '1' else 0

                continue
        
            prefix_zeros[i] = prefix_zeros[i - 1] + (1 if ch == '0' else 0)

            prefix_ones[i] = prefix_ones[i - 1] + (1 if ch == '1' else 0)
        
        for i in range(1, n - 1):
            ch = s[i]
            if ch == '0':
                x = prefix_ones[i - 1]
                y = prefix_ones[n - 1] - prefix_ones[i]
                res += x * y
            else:

                x = prefix_zeros[i - 1]
                y = prefix_zeros[n - 1] - prefix_zeros[i]
                
                res += x * y
        
        return res
