class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        largestBit = count = 0

        for i, bit in enumerate(flips, 1):
            largestBit = max(largestBit, bit)
            
            if largestBit == i:
                count += 1

        return count


    
    
        