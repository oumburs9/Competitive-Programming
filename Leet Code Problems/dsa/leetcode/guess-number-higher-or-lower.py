# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low+(high - low)//2
            pick = guess(mid)

            if pick > 0: 
                low = mid+1
            elif pick < 0: 
                high = mid - 1
            else: 
                return mid
        
        return -1
        