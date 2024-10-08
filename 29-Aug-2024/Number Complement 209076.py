# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:

        x = list(bin(num)[2:])

        for i in range(len(x)):
            if x[i] == '1':
                x[i] = '0'
            else:
                x[i] = '1'
                
        return int(''.join(x), 2)

        