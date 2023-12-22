class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        r = len(digits)-1
        while digits[r] == 9:
            digits[r] = 0
            r -= 1

        if r == -1:
            digits.insert(0,1)
        else:
            digits[r] += 1
        
        
        if len(digits) == 1 and digits[0] == 9:
            digits.append(0)

        return digits
    
            


        
        