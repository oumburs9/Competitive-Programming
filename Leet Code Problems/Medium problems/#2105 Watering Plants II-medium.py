class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        l, r, capA, capB = 0 , len(plants)-1 ,capacityA ,capacityB
        score = 0
        
        while l < r:
            if plants[l] > capA:
                score +=1
                capA = capacityA
                
            if plants[r] > capB:
                score +=1
                capB = capacityB
               
                
            
            capA -= plants[l]
            capB -= plants[r]
            l += 1
            r -= 1
        if l == r and plants[l] > capA and plants[l] > capB:
            score +=1
                
        return score
                
            

            