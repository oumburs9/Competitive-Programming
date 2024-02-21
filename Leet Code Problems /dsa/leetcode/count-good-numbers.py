class Solution:
    def countGoodNumbers(self, n: int) -> int:
        '''
        if N is odd: ans = 5^(n/2+1) * 4^(n/2),
        if N is even: ans = 5^(n/2)*4^(n/2).

        '''
        def pw(x,n):
            if n == 0:
                return 1

            res = pw(x,n//2)

            if n % 2 == 0:
                return (res * res) % MOD
            else:
                return (x * res * res) % MOD

        MOD = 10**9 + 7

        odd = n//2
        even = (n+1)//2

        return (pw(5,even) * pw(4,odd)) % MOD


