from typing import Counter, List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLen = 0
        currLen = 0
        l = 0
        unique = 0
        dic = Counter()
        n =len(fruits)
        
        
        for r in range(n):
            dic[fruits[r]] +=1
            
            if dic[fruits[r]] == 1:
                unique +=1
                
                
            while unique > 2:
                dic[fruits[l]]-=1
                
                if dic[fruits[l]] ==0:
                    unique -= 1
                l +=1
            currLen = r -l +1
            maxLen = max(maxLen,currLen)
        return maxLen
            
            
                    
                    
                 
                
        