class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0

        while maxDoubles > 0 and target != 1:
            if target % 2:
                op += 1
                target -= 1

            else:
                op += 1
                target //= 2

                maxDoubles -= 1
        _minMoves = op + target - 1
        return _minMoves

 

        