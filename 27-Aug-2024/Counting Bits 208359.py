# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            cnt = 0
            while i > 0:
                r = i & 1
                if r == 1:
                    cnt +=1
                i >>= 1
            res.append(cnt)

        return res

        
        