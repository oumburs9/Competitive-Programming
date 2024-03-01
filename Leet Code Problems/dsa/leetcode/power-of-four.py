class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 :
            return False
        log_4 = log(n,4)

        return log_4 == int(log_4)
        