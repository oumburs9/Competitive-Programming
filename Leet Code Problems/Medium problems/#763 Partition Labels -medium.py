from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndxDict = {}
        res = []
       
    
        for i,c in enumerate(s):
            lastIndxDict[c] =i
            

        size = 0
        end = 0
        for i,c in enumerate(s):
            size +=1
            if lastIndxDict[c] > end:
                end = lastIndxDict[c] 
           

            if end == i:
                res.append(size)
                size = 0
            
        return res

          

                
                
            
        
        
        