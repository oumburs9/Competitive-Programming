class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        op = 0

        while startValue < target:
            if target % 2:
                op += 1
                target += 1
            op += 1
            target //= 2

        return startValue - target + op 
