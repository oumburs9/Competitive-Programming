# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = []

        carry = 0

        i, j = len(a) - 1,  len(b) - 1
        
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += int(a[i])
                i -= 1

            if j >= 0:
                _sum += int(b[j])

                j -= 1
            
            res.append(str(_sum % 2))
            
            carry = _sum // 2
        
        if carry != 0: #hh
            res.append(str(carry))
        
        return ''.join(reversed(res))
