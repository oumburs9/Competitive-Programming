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

          

                
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndx = {}
        res = []


        for i,c in enumerate(s):
            lastIndx[c] = i

        start,end = 0,0

        for i,c in enumerate(s):
            end = max(end,lastIndx[c])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

                   
            
        
        
        