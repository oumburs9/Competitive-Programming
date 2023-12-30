class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        resSum = 0
        
        l = len(piles)-2
        j = 0
        while(j < len(piles)/3):
            resSum +=piles[l]
            l -= 2
            j+=1
        return resSum
        